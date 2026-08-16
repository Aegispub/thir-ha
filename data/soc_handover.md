# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T16:29:17Z |
| **Shift Time** | 16:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **4487** |
| Confirmed Threats | **4467** |
| False Positives Filtered | **20** (0.4%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **27** |
| High Severity Cases | **60** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **4427** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **13** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **65** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `test` | 11 |
| `centos` | 8 |
| `pi` | 6 |
| `postgres` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456789` | 10 |
| `admin123` | 5 |
| `administrator` | 4 |
| `password` | 4 |
| `test` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `pi` | `123456789` | 6 |
| `ubnt` | `admin123` | 5 |
| `centos` | `123456789` | 4 |
| `test` | `administrator` | 4 |
| `centos` | `password` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `aa123123` | `45.142.193.164` | 2026-08-16T12:55:41 |
| `pi` | `123456789` | `10.0.0.73` | 2026-08-16T12:56:01 |
| `pi` | `123456789` | `222.116.11.230` | 2026-08-16T12:57:37 |
| `pi` | `123456789` | `222.139.245.137` | 2026-08-16T12:57:47 |
| `centos` | `123456789` | `120.198.138.185` | 2026-08-16T12:59:15 |
| `centos` | `123456789` | `144.22.210.132` | 2026-08-16T12:59:24 |
| `config` | `passw0rd` | `68.7.114.69` | 2026-08-16T13:02:16 |
| `config` | `passw0rd` | `14.54.22.11` | 2026-08-16T13:02:29 |
| `sysop` | `sysop` | `217.165.22.192` | 2026-08-16T13:04:51 |
| `pi` | `123456789` | `60.249.252.94` | 2026-08-16T13:13:39 |
| `pi` | `123456789` | `31.41.84.98` | 2026-08-16T13:13:47 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T13:16:40 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `45.79.181.179` | 2026-08-16T13:17:51 |
| `root` | `aaaa8888` | `45.142.193.164` | 2026-08-16T13:18:57 |
| `postgres` | `123` | `217.165.22.192` | 2026-08-16T13:23:58 |
| `centos` | `123456789` | `186.103.136.43` | 2026-08-16T13:27:49 |
| `centos` | `123456789` | `220.132.170.64` | 2026-08-16T13:28:01 |
| `test` | `administrator` | `113.28.86.1` | 2026-08-16T13:31:31 |
| `test` | `administrator` | `77.106.78.215` | 2026-08-16T13:31:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-16T13:32:35 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-16T13:32:35 |
| `test` | `987654321` | `146.255.228.189` | 2026-08-16T13:33:06 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.38` | 2026-08-16T13:34:51 |
| `root` | `hp@123` | `45.142.193.164` | 2026-08-16T13:42:22 |
| `postgres` | `123456` | `217.165.22.192` | 2026-08-16T13:43:06 |
| `test` | `987654321` | `10.0.0.73` | 2026-08-16T13:44:45 |
| `test` | `administrator` | `181.129.31.42` | 2026-08-16T13:47:38 |
| `test` | `administrator` | `202.129.35.8` | 2026-08-16T13:47:48 |
| `ubuntu` | `QWE123qwe` | `185.74.59.14` | 2026-08-16T13:52:12 |
| `test` | `987654321` | `31.173.2.182` | 2026-08-16T14:01:40 |
| `postgres` | `1234.com` | `217.165.22.192` | 2026-08-16T14:02:12 |
| `ubnt` | `admin123` | `10.0.0.73` | 2026-08-16T14:03:54 |
| `ubuntu` | `Passw0rd` | `185.74.59.14` | 2026-08-16T14:04:13 |
| `ubnt` | `admin123` | `202.72.196.75` | 2026-08-16T14:05:24 |
| `ubnt` | `admin123` | `61.12.86.90` | 2026-08-16T14:05:33 |
| `root` | `cc123456` | `45.142.193.164` | 2026-08-16T14:05:51 |
| `centos` | `password` | `182.156.35.238` | 2026-08-16T14:06:33 |
| `centos` | `password` | `185.112.148.66` | 2026-08-16T14:06:47 |
| `centos` | `password` | `125.35.109.214` | 2026-08-16T14:06:52 |
| `centos` | `password` | `138.118.213.68` | 2026-08-16T14:07:01 |
| `ftpuser` | `test` | `10.0.0.73` | 2026-08-16T14:18:24 |
| `postgres` | `123.com` | `217.165.22.192` | 2026-08-16T14:21:19 |
| `ubnt` | `admin123` | `197.242.170.10` | 2026-08-16T14:21:32 |
| `test` | `3333` | `10.0.0.73` | 2026-08-16T14:22:06 |
| `root` | `Cc123456` | `45.142.193.164` | 2026-08-16T14:29:18 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `43.248.108.70` | 2026-08-16T14:31:49 |
| `root` | `123qwerty` | `92.118.39.71` | 2026-08-16T14:33:32 |
| `ftpuser` | `test` | `218.29.231.106` | 2026-08-16T14:35:34 |
| `ftpuser` | `test` | `117.204.1.45` | 2026-08-16T14:35:51 |
| `root` | `21` | `92.118.39.71` | 2026-08-16T14:35:54 |
| `default` | `default123` | `10.0.0.73` | 2026-08-16T14:37:55 |
| `root` | `321` | `92.118.39.71` | 2026-08-16T14:38:07 |
| `default` | `default123` | `122.187.229.220` | 2026-08-16T14:39:31 |
| `default` | `default123` | `111.70.32.10` | 2026-08-16T14:39:40 |
| `root` | `4321` | `92.118.39.71` | 2026-08-16T14:40:04 |
| `postgres` | `1qaz@WSX3edc` | `217.165.22.192` | 2026-08-16T14:40:26 |
| `test` | `3333` | `77.106.78.215` | 2026-08-16T14:40:39 |
| `test` | `3333` | `1.212.225.99` | 2026-08-16T14:40:55 |
| `root` | `54321` | `92.118.39.71` | 2026-08-16T14:42:13 |
| `root` | `P4ssw0rd` | `92.118.39.71` | 2026-08-16T14:44:26 |
| `root` | `toortoor` | `77.90.185.20` | 2026-08-16T14:47:03 |
| `root` | `P4ssword` | `92.118.39.71` | 2026-08-16T14:47:19 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-08-16T14:49:20 |
| `root` | `1qaz2wsx!@` | `45.142.193.164` | 2026-08-16T14:52:19 |
| `ubuntu` | `!qaz@wsx3edc` | `185.74.59.14` | 2026-08-16T14:52:30 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **4487** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 35 |
| OpenSSH | 31 |
| libssh | 7 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 31 | 30 |
| `98ddc5604ef6...` | Modern SSH client | 9 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 1 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `4e066189c3bb...` | Generic scanner | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 31 | 30 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 9 | 2 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **57** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 7 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS45820` | Tata Teleservices ISP AS | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (60)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f7f0d9b6aeab

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 12:55 |
| **Last Seen** | 2026-08-16 12:55 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:55:12` | `cowrie.session.connect` |
| `2026-08-16 12:55:19` | `cowrie.client.version` |
| `2026-08-16 12:55:19` | `cowrie.client.kex` |
| `2026-08-16 12:55:41` | `cowrie.login.success` |
| `2026-08-16 12:55:54` | `cowrie.session.params` |
| `2026-08-16 12:55:54` | `cowrie.command.input` |
| `2026-08-16 12:55:59` | `cowrie.log.closed` |
| `2026-08-16 12:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d693c2f0819

| Field | Detail |
|---|---|
| **Source IP** | `222.116.11[.]230` |
| **First Seen** | 2026-08-16 12:57 |
| **Last Seen** | 2026-08-16 12:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:57:35` | `cowrie.session.connect` |
| `2026-08-16 12:57:35` | `cowrie.client.version` |
| `2026-08-16 12:57:35` | `cowrie.client.kex` |
| `2026-08-16 12:57:37` | `cowrie.login.success` |
| `2026-08-16 12:57:38` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.116.11[.]230` to AbuseIPDB if not already reported
- [ ] Block `222.116.11[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f483b096c40f

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-08-16 12:57 |
| **Last Seen** | 2026-08-16 12:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:57:43` | `cowrie.session.connect` |
| `2026-08-16 12:57:44` | `cowrie.client.version` |
| `2026-08-16 12:57:44` | `cowrie.client.kex` |
| `2026-08-16 12:57:47` | `cowrie.login.success` |
| `2026-08-16 12:57:48` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad42f9653eda

| Field | Detail |
|---|---|
| **Source IP** | `120.198.138[.]185` |
| **First Seen** | 2026-08-16 12:59 |
| **Last Seen** | 2026-08-16 12:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:59:11` | `cowrie.session.connect` |
| `2026-08-16 12:59:12` | `cowrie.client.version` |
| `2026-08-16 12:59:12` | `cowrie.client.kex` |
| `2026-08-16 12:59:15` | `cowrie.login.success` |
| `2026-08-16 12:59:15` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.198.138[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.198.138[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-275b66c7e15d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.210[.]132` |
| **First Seen** | 2026-08-16 12:59 |
| **Last Seen** | 2026-08-16 12:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:59:21` | `cowrie.session.connect` |
| `2026-08-16 12:59:22` | `cowrie.client.version` |
| `2026-08-16 12:59:22` | `cowrie.client.kex` |
| `2026-08-16 12:59:24` | `cowrie.login.success` |
| `2026-08-16 12:59:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.210[.]132` to AbuseIPDB if not already reported
- [ ] Block `144.22.210[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b72d994a54

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-08-16 13:02 |
| **Last Seen** | 2026-08-16 13:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:02:13` | `cowrie.session.connect` |
| `2026-08-16 13:02:14` | `cowrie.client.version` |
| `2026-08-16 13:02:14` | `cowrie.client.kex` |
| `2026-08-16 13:02:16` | `cowrie.login.success` |
| `2026-08-16 13:02:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7aa3bcecd8

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-16 13:02 |
| **Last Seen** | 2026-08-16 13:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:02:26` | `cowrie.session.connect` |
| `2026-08-16 13:02:27` | `cowrie.client.version` |
| `2026-08-16 13:02:27` | `cowrie.client.kex` |
| `2026-08-16 13:02:29` | `cowrie.login.success` |
| `2026-08-16 13:02:29` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7c5fa7d313

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 13:04 |
| **Last Seen** | 2026-08-16 13:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:04:51` | `cowrie.session.connect` |
| `2026-08-16 13:04:51` | `cowrie.client.version` |
| `2026-08-16 13:04:51` | `cowrie.client.kex` |
| `2026-08-16 13:04:51` | `cowrie.login.success` |
| `2026-08-16 13:04:52` | `cowrie.session.params` |
| `2026-08-16 13:04:52` | `cowrie.command.input` |
| `2026-08-16 13:04:53` | `cowrie.log.closed` |
| `2026-08-16 13:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4506e137daa4

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-08-16 13:13 |
| **Last Seen** | 2026-08-16 13:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:13:36` | `cowrie.session.connect` |
| `2026-08-16 13:13:36` | `cowrie.client.version` |
| `2026-08-16 13:13:36` | `cowrie.client.kex` |
| `2026-08-16 13:13:39` | `cowrie.login.success` |
| `2026-08-16 13:13:39` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee92326041c

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-08-16 13:13 |
| **Last Seen** | 2026-08-16 13:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:13:46` | `cowrie.session.connect` |
| `2026-08-16 13:13:46` | `cowrie.client.version` |
| `2026-08-16 13:13:46` | `cowrie.client.kex` |
| `2026-08-16 13:13:47` | `cowrie.login.success` |
| `2026-08-16 13:13:47` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895da044b17e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 13:16 |
| **Last Seen** | 2026-08-16 13:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:16:40` | `cowrie.session.connect` |
| `2026-08-16 13:16:40` | `cowrie.client.version` |
| `2026-08-16 13:16:40` | `cowrie.client.kex` |
| `2026-08-16 13:16:40` | `cowrie.login.success` |
| `2026-08-16 13:16:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:16:40` | `cowrie.direct-tcpip.data` |
| `2026-08-16 13:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96fdbb1a91f8

| Field | Detail |
|---|---|
| **Source IP** | `45.79.181[.]179` |
| **First Seen** | 2026-08-16 13:17 |
| **Last Seen** | 2026-08-16 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:17:51` | `cowrie.session.connect` |
| `2026-08-16 13:17:51` | `cowrie.login.success` |
| `2026-08-16 13:17:52` | `cowrie.session.params` |
| `2026-08-16 13:17:52` | `cowrie.command.input` |
| `2026-08-16 13:17:52` | `cowrie.command.input` |
| `2026-08-16 13:17:52` | `cowrie.command.failed` |
| `2026-08-16 13:17:52` | `cowrie.command.input` |
| `2026-08-16 13:17:52` | `cowrie.command.failed` |
| `2026-08-16 13:17:52` | `cowrie.command.input` |
| `2026-08-16 13:17:52` | `cowrie.log.closed` |
| `2026-08-16 13:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.181[.]179` to AbuseIPDB if not already reported
- [ ] Block `45.79.181[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421b5775d1c2

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 13:18 |
| **Last Seen** | 2026-08-16 13:19 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:18:29` | `cowrie.session.connect` |
| `2026-08-16 13:18:34` | `cowrie.client.version` |
| `2026-08-16 13:18:34` | `cowrie.client.kex` |
| `2026-08-16 13:18:57` | `cowrie.login.success` |
| `2026-08-16 13:19:09` | `cowrie.session.params` |
| `2026-08-16 13:19:09` | `cowrie.command.input` |
| `2026-08-16 13:19:15` | `cowrie.log.closed` |
| `2026-08-16 13:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16ceda801d3

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 13:23 |
| **Last Seen** | 2026-08-16 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:23:58` | `cowrie.session.connect` |
| `2026-08-16 13:23:58` | `cowrie.client.version` |
| `2026-08-16 13:23:58` | `cowrie.client.kex` |
| `2026-08-16 13:23:58` | `cowrie.login.success` |
| `2026-08-16 13:23:59` | `cowrie.session.params` |
| `2026-08-16 13:23:59` | `cowrie.command.input` |
| `2026-08-16 13:23:59` | `cowrie.log.closed` |
| `2026-08-16 13:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4436aa7081c

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-08-16 13:27 |
| **Last Seen** | 2026-08-16 13:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:27:47` | `cowrie.session.connect` |
| `2026-08-16 13:27:48` | `cowrie.client.version` |
| `2026-08-16 13:27:48` | `cowrie.client.kex` |
| `2026-08-16 13:27:49` | `cowrie.login.success` |
| `2026-08-16 13:27:50` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9155a10204df

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-08-16 13:27 |
| **Last Seen** | 2026-08-16 13:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:27:58` | `cowrie.session.connect` |
| `2026-08-16 13:27:59` | `cowrie.client.version` |
| `2026-08-16 13:27:59` | `cowrie.client.kex` |
| `2026-08-16 13:28:01` | `cowrie.login.success` |
| `2026-08-16 13:28:02` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80168b4c4cde

| Field | Detail |
|---|---|
| **Source IP** | `113.28.86[.]1` |
| **First Seen** | 2026-08-16 13:31 |
| **Last Seen** | 2026-08-16 13:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:31:26` | `cowrie.session.connect` |
| `2026-08-16 13:31:28` | `cowrie.client.version` |
| `2026-08-16 13:31:28` | `cowrie.client.kex` |
| `2026-08-16 13:31:31` | `cowrie.login.success` |
| `2026-08-16 13:31:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.28.86[.]1` to AbuseIPDB if not already reported
- [ ] Block `113.28.86[.]1` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-450b0504331d

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-08-16 13:31 |
| **Last Seen** | 2026-08-16 13:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:31:37` | `cowrie.session.connect` |
| `2026-08-16 13:31:37` | `cowrie.client.version` |
| `2026-08-16 13:31:37` | `cowrie.client.kex` |
| `2026-08-16 13:31:38` | `cowrie.login.success` |
| `2026-08-16 13:31:39` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026ac6a2a8ef

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 13:32 |
| **Last Seen** | 2026-08-16 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:32:34` | `cowrie.session.connect` |
| `2026-08-16 13:32:34` | `cowrie.client.version` |
| `2026-08-16 13:32:34` | `cowrie.client.kex` |
| `2026-08-16 13:32:35` | `cowrie.login.success` |
| `2026-08-16 13:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f04e670d85

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 13:32 |
| **Last Seen** | 2026-08-16 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:32:34` | `cowrie.session.connect` |
| `2026-08-16 13:32:34` | `cowrie.client.version` |
| `2026-08-16 13:32:35` | `cowrie.client.kex` |
| `2026-08-16 13:32:35` | `cowrie.login.success` |
| `2026-08-16 13:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c298eb97781b

| Field | Detail |
|---|---|
| **Source IP** | `146.255.228[.]189` |
| **First Seen** | 2026-08-16 13:33 |
| **Last Seen** | 2026-08-16 13:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:33:04` | `cowrie.session.connect` |
| `2026-08-16 13:33:04` | `cowrie.client.version` |
| `2026-08-16 13:33:04` | `cowrie.client.kex` |
| `2026-08-16 13:33:06` | `cowrie.login.success` |
| `2026-08-16 13:33:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.255.228[.]189` to AbuseIPDB if not already reported
- [ ] Block `146.255.228[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726694f16a77

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]38` |
| **First Seen** | 2026-08-16 13:34 |
| **Last Seen** | 2026-08-16 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:34:51` | `cowrie.session.connect` |
| `2026-08-16 13:34:51` | `cowrie.login.success` |
| `2026-08-16 13:34:52` | `cowrie.session.params` |
| `2026-08-16 13:34:52` | `cowrie.command.input` |
| `2026-08-16 13:34:52` | `cowrie.command.input` |
| `2026-08-16 13:34:52` | `cowrie.command.failed` |
| `2026-08-16 13:34:52` | `cowrie.command.input` |
| `2026-08-16 13:34:52` | `cowrie.command.failed` |
| `2026-08-16 13:34:52` | `cowrie.command.input` |
| `2026-08-16 13:34:52` | `cowrie.log.closed` |
| `2026-08-16 13:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]38` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c4e15bebec

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 13:41 |
| **Last Seen** | 2026-08-16 13:42 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:41:53` | `cowrie.session.connect` |
| `2026-08-16 13:41:58` | `cowrie.client.version` |
| `2026-08-16 13:41:58` | `cowrie.client.kex` |
| `2026-08-16 13:42:22` | `cowrie.login.success` |
| `2026-08-16 13:42:33` | `cowrie.session.params` |
| `2026-08-16 13:42:33` | `cowrie.command.input` |
| `2026-08-16 13:42:40` | `cowrie.log.closed` |
| `2026-08-16 13:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb55f3eb1d6

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 13:43 |
| **Last Seen** | 2026-08-16 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:43:05` | `cowrie.session.connect` |
| `2026-08-16 13:43:05` | `cowrie.client.version` |
| `2026-08-16 13:43:05` | `cowrie.client.kex` |
| `2026-08-16 13:43:06` | `cowrie.login.success` |
| `2026-08-16 13:43:07` | `cowrie.session.params` |
| `2026-08-16 13:43:07` | `cowrie.command.input` |
| `2026-08-16 13:43:07` | `cowrie.log.closed` |
| `2026-08-16 13:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f52a8ff5037d

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-08-16 13:47 |
| **Last Seen** | 2026-08-16 13:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:47:36` | `cowrie.session.connect` |
| `2026-08-16 13:47:36` | `cowrie.client.version` |
| `2026-08-16 13:47:36` | `cowrie.client.kex` |
| `2026-08-16 13:47:38` | `cowrie.login.success` |
| `2026-08-16 13:47:39` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b81b7d760bb

| Field | Detail |
|---|---|
| **Source IP** | `202.129.35[.]8` |
| **First Seen** | 2026-08-16 13:47 |
| **Last Seen** | 2026-08-16 13:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:47:45` | `cowrie.session.connect` |
| `2026-08-16 13:47:46` | `cowrie.client.version` |
| `2026-08-16 13:47:46` | `cowrie.client.kex` |
| `2026-08-16 13:47:48` | `cowrie.login.success` |
| `2026-08-16 13:47:48` | `cowrie.direct-tcpip.request` |
| `2026-08-16 13:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.129.35[.]8` to AbuseIPDB if not already reported
- [ ] Block `202.129.35[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a048f757e8f5

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 13:52 |
| **Last Seen** | 2026-08-16 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 13:52:11` | `cowrie.session.connect` |
| `2026-08-16 13:52:11` | `cowrie.client.version` |
| `2026-08-16 13:52:12` | `cowrie.client.kex` |
| `2026-08-16 13:52:12` | `cowrie.login.success` |
| `2026-08-16 13:52:13` | `cowrie.session.params` |
| `2026-08-16 13:52:13` | `cowrie.command.input` |
| `2026-08-16 13:52:13` | `cowrie.log.closed` |
| `2026-08-16 13:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8adee655599b

| Field | Detail |
|---|---|
| **Source IP** | `31.173.2[.]182` |
| **First Seen** | 2026-08-16 14:01 |
| **Last Seen** | 2026-08-16 14:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:01:38` | `cowrie.session.connect` |
| `2026-08-16 14:01:38` | `cowrie.client.version` |
| `2026-08-16 14:01:38` | `cowrie.client.kex` |
| `2026-08-16 14:01:40` | `cowrie.login.success` |
| `2026-08-16 14:01:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.2[.]182` to AbuseIPDB if not already reported
- [ ] Block `31.173.2[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc58a9578c5

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 14:02 |
| **Last Seen** | 2026-08-16 14:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:02:11` | `cowrie.session.connect` |
| `2026-08-16 14:02:11` | `cowrie.client.version` |
| `2026-08-16 14:02:12` | `cowrie.client.kex` |
| `2026-08-16 14:02:12` | `cowrie.login.success` |
| `2026-08-16 14:02:13` | `cowrie.session.params` |
| `2026-08-16 14:02:13` | `cowrie.command.input` |
| `2026-08-16 14:02:13` | `cowrie.log.closed` |
| `2026-08-16 14:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfcbed236b1f

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 14:04 |
| **Last Seen** | 2026-08-16 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:04:13` | `cowrie.session.connect` |
| `2026-08-16 14:04:13` | `cowrie.client.version` |
| `2026-08-16 14:04:13` | `cowrie.client.kex` |
| `2026-08-16 14:04:13` | `cowrie.login.success` |
| `2026-08-16 14:04:14` | `cowrie.session.params` |
| `2026-08-16 14:04:14` | `cowrie.command.input` |
| `2026-08-16 14:04:14` | `cowrie.log.closed` |
| `2026-08-16 14:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f287c67a3a96

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-16 14:05 |
| **Last Seen** | 2026-08-16 14:10 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:05:22` | `cowrie.session.connect` |
| `2026-08-16 14:05:22` | `cowrie.client.version` |
| `2026-08-16 14:05:22` | `cowrie.client.kex` |
| `2026-08-16 14:05:24` | `cowrie.login.success` |
| `2026-08-16 14:05:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ad4366508e

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 14:05 |
| **Last Seen** | 2026-08-16 14:06 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:05:22` | `cowrie.session.connect` |
| `2026-08-16 14:05:27` | `cowrie.client.version` |
| `2026-08-16 14:05:27` | `cowrie.client.kex` |
| `2026-08-16 14:05:51` | `cowrie.login.success` |
| `2026-08-16 14:06:03` | `cowrie.session.params` |
| `2026-08-16 14:06:03` | `cowrie.command.input` |
| `2026-08-16 14:06:09` | `cowrie.log.closed` |
| `2026-08-16 14:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02730757e82

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-08-16 14:05 |
| **Last Seen** | 2026-08-16 14:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:05:31` | `cowrie.session.connect` |
| `2026-08-16 14:05:32` | `cowrie.client.version` |
| `2026-08-16 14:05:32` | `cowrie.client.kex` |
| `2026-08-16 14:05:33` | `cowrie.login.success` |
| `2026-08-16 14:05:34` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66dbdbb44fa

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-08-16 14:06 |
| **Last Seen** | 2026-08-16 14:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:06:30` | `cowrie.session.connect` |
| `2026-08-16 14:06:31` | `cowrie.client.version` |
| `2026-08-16 14:06:31` | `cowrie.client.kex` |
| `2026-08-16 14:06:33` | `cowrie.login.success` |
| `2026-08-16 14:06:34` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dadfd4f7221e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-08-16 14:06 |
| **Last Seen** | 2026-08-16 14:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:06:41` | `cowrie.session.connect` |
| `2026-08-16 14:06:42` | `cowrie.client.version` |
| `2026-08-16 14:06:42` | `cowrie.client.kex` |
| `2026-08-16 14:06:47` | `cowrie.login.success` |
| `2026-08-16 14:06:49` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e114344d1530

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-08-16 14:06 |
| **Last Seen** | 2026-08-16 14:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:06:48` | `cowrie.session.connect` |
| `2026-08-16 14:06:49` | `cowrie.client.version` |
| `2026-08-16 14:06:49` | `cowrie.client.kex` |
| `2026-08-16 14:06:52` | `cowrie.login.success` |
| `2026-08-16 14:06:53` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a2b309985b

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-16 14:06 |
| **Last Seen** | 2026-08-16 14:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:06:58` | `cowrie.session.connect` |
| `2026-08-16 14:06:59` | `cowrie.client.version` |
| `2026-08-16 14:06:59` | `cowrie.client.kex` |
| `2026-08-16 14:07:01` | `cowrie.login.success` |
| `2026-08-16 14:07:02` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f3bfea5910

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 14:21 |
| **Last Seen** | 2026-08-16 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:21:18` | `cowrie.session.connect` |
| `2026-08-16 14:21:18` | `cowrie.client.version` |
| `2026-08-16 14:21:18` | `cowrie.client.kex` |
| `2026-08-16 14:21:19` | `cowrie.login.success` |
| `2026-08-16 14:21:20` | `cowrie.session.params` |
| `2026-08-16 14:21:20` | `cowrie.command.input` |
| `2026-08-16 14:21:20` | `cowrie.log.closed` |
| `2026-08-16 14:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82ff459bc46

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-16 14:21 |
| **Last Seen** | 2026-08-16 14:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:21:28` | `cowrie.session.connect` |
| `2026-08-16 14:21:29` | `cowrie.client.version` |
| `2026-08-16 14:21:29` | `cowrie.client.kex` |
| `2026-08-16 14:21:32` | `cowrie.login.success` |
| `2026-08-16 14:21:33` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ace8fc0e045

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 14:28 |
| **Last Seen** | 2026-08-16 14:29 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:28:49` | `cowrie.session.connect` |
| `2026-08-16 14:28:55` | `cowrie.client.version` |
| `2026-08-16 14:28:55` | `cowrie.client.kex` |
| `2026-08-16 14:29:18` | `cowrie.login.success` |
| `2026-08-16 14:29:31` | `cowrie.session.params` |
| `2026-08-16 14:29:31` | `cowrie.command.input` |
| `2026-08-16 14:29:36` | `cowrie.log.closed` |
| `2026-08-16 14:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56d589b9ddd

| Field | Detail |
|---|---|
| **Source IP** | `43.248.108[.]70` |
| **First Seen** | 2026-08-16 14:31 |
| **Last Seen** | 2026-08-16 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:31:49` | `cowrie.session.connect` |
| `2026-08-16 14:31:49` | `cowrie.login.success` |
| `2026-08-16 14:31:50` | `cowrie.session.params` |
| `2026-08-16 14:31:50` | `cowrie.command.input` |
| `2026-08-16 14:31:50` | `cowrie.command.failed` |
| `2026-08-16 14:31:50` | `cowrie.command.input` |
| `2026-08-16 14:31:51` | `cowrie.log.closed` |
| `2026-08-16 14:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.248.108[.]70` to AbuseIPDB if not already reported
- [ ] Block `43.248.108[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1de333f5df4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:33 |
| **Last Seen** | 2026-08-16 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:33:31` | `cowrie.session.connect` |
| `2026-08-16 14:33:31` | `cowrie.client.version` |
| `2026-08-16 14:33:31` | `cowrie.client.kex` |
| `2026-08-16 14:33:32` | `cowrie.login.success` |
| `2026-08-16 14:33:32` | `cowrie.session.params` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.success` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.command.input` |
| `2026-08-16 14:33:32` | `cowrie.log.closed` |
| `2026-08-16 14:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54b32235413e

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-08-16 14:35 |
| **Last Seen** | 2026-08-16 14:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:35:30` | `cowrie.session.connect` |
| `2026-08-16 14:35:31` | `cowrie.client.version` |
| `2026-08-16 14:35:31` | `cowrie.client.kex` |
| `2026-08-16 14:35:34` | `cowrie.login.success` |
| `2026-08-16 14:35:35` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9395dc93e9b5

| Field | Detail |
|---|---|
| **Source IP** | `117.204.1[.]45` |
| **First Seen** | 2026-08-16 14:35 |
| **Last Seen** | 2026-08-16 14:35 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:35:43` | `cowrie.session.connect` |
| `2026-08-16 14:35:47` | `cowrie.client.version` |
| `2026-08-16 14:35:47` | `cowrie.client.kex` |
| `2026-08-16 14:35:51` | `cowrie.login.success` |
| `2026-08-16 14:35:51` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.204.1[.]45` to AbuseIPDB if not already reported
- [ ] Block `117.204.1[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafd404ac0ee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:35 |
| **Last Seen** | 2026-08-16 14:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:35:53` | `cowrie.session.connect` |
| `2026-08-16 14:35:53` | `cowrie.client.version` |
| `2026-08-16 14:35:53` | `cowrie.client.kex` |
| `2026-08-16 14:35:54` | `cowrie.login.success` |
| `2026-08-16 14:35:55` | `cowrie.session.params` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.success` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.command.input` |
| `2026-08-16 14:35:55` | `cowrie.log.closed` |
| `2026-08-16 14:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443aa076fd97

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:38 |
| **Last Seen** | 2026-08-16 14:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:38:06` | `cowrie.session.connect` |
| `2026-08-16 14:38:06` | `cowrie.client.version` |
| `2026-08-16 14:38:06` | `cowrie.client.kex` |
| `2026-08-16 14:38:07` | `cowrie.login.success` |
| `2026-08-16 14:38:08` | `cowrie.session.params` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.success` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.command.input` |
| `2026-08-16 14:38:08` | `cowrie.log.closed` |
| `2026-08-16 14:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d68233e31fe

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]220` |
| **First Seen** | 2026-08-16 14:39 |
| **Last Seen** | 2026-08-16 14:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:39:28` | `cowrie.session.connect` |
| `2026-08-16 14:39:29` | `cowrie.client.version` |
| `2026-08-16 14:39:29` | `cowrie.client.kex` |
| `2026-08-16 14:39:31` | `cowrie.login.success` |
| `2026-08-16 14:39:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]220` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc4d624d459

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-08-16 14:39 |
| **Last Seen** | 2026-08-16 14:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:39:37` | `cowrie.session.connect` |
| `2026-08-16 14:39:38` | `cowrie.client.version` |
| `2026-08-16 14:39:38` | `cowrie.client.kex` |
| `2026-08-16 14:39:40` | `cowrie.login.success` |
| `2026-08-16 14:39:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44dd0164d050

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:40 |
| **Last Seen** | 2026-08-16 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:40:04` | `cowrie.session.connect` |
| `2026-08-16 14:40:04` | `cowrie.client.version` |
| `2026-08-16 14:40:04` | `cowrie.client.kex` |
| `2026-08-16 14:40:04` | `cowrie.login.success` |
| `2026-08-16 14:40:05` | `cowrie.session.params` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.success` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.command.input` |
| `2026-08-16 14:40:05` | `cowrie.log.closed` |
| `2026-08-16 14:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7f57bf7b49

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 14:40 |
| **Last Seen** | 2026-08-16 14:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:40:25` | `cowrie.session.connect` |
| `2026-08-16 14:40:25` | `cowrie.client.version` |
| `2026-08-16 14:40:25` | `cowrie.client.kex` |
| `2026-08-16 14:40:26` | `cowrie.login.success` |
| `2026-08-16 14:40:27` | `cowrie.session.params` |
| `2026-08-16 14:40:27` | `cowrie.command.input` |
| `2026-08-16 14:40:27` | `cowrie.log.closed` |
| `2026-08-16 14:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705491eaaa01

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-08-16 14:40 |
| **Last Seen** | 2026-08-16 14:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:40:37` | `cowrie.session.connect` |
| `2026-08-16 14:40:38` | `cowrie.client.version` |
| `2026-08-16 14:40:38` | `cowrie.client.kex` |
| `2026-08-16 14:40:39` | `cowrie.login.success` |
| `2026-08-16 14:40:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 14:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2218953b5cec

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-16 14:40 |
| **Last Seen** | 2026-08-16 14:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:40:52` | `cowrie.session.connect` |
| `2026-08-16 14:40:53` | `cowrie.client.version` |
| `2026-08-16 14:40:53` | `cowrie.client.kex` |
| `2026-08-16 14:40:55` | `cowrie.login.success` |
| `2026-08-16 14:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5179220dbde4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:42 |
| **Last Seen** | 2026-08-16 14:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:42:12` | `cowrie.session.connect` |
| `2026-08-16 14:42:12` | `cowrie.client.version` |
| `2026-08-16 14:42:12` | `cowrie.client.kex` |
| `2026-08-16 14:42:13` | `cowrie.login.success` |
| `2026-08-16 14:42:13` | `cowrie.session.params` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.success` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:13` | `cowrie.command.input` |
| `2026-08-16 14:42:14` | `cowrie.log.closed` |
| `2026-08-16 14:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc48c2d198a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:44 |
| **Last Seen** | 2026-08-16 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:44:26` | `cowrie.session.connect` |
| `2026-08-16 14:44:26` | `cowrie.client.version` |
| `2026-08-16 14:44:26` | `cowrie.client.kex` |
| `2026-08-16 14:44:26` | `cowrie.login.success` |
| `2026-08-16 14:44:27` | `cowrie.session.params` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.success` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.command.input` |
| `2026-08-16 14:44:27` | `cowrie.log.closed` |
| `2026-08-16 14:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b538b0141505

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-16 14:46 |
| **Last Seen** | 2026-08-16 14:47 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:46:53` | `cowrie.session.connect` |
| `2026-08-16 14:46:54` | `cowrie.client.version` |
| `2026-08-16 14:46:54` | `cowrie.client.kex` |
| `2026-08-16 14:47:03` | `cowrie.login.success` |
| `2026-08-16 14:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f81db19ef4

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-16 14:47 |
| **Last Seen** | 2026-08-16 14:47 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:47:07` | `cowrie.session.connect` |
| `2026-08-16 14:47:07` | `cowrie.client.version` |
| `2026-08-16 14:47:07` | `cowrie.client.kex` |
| `2026-08-16 14:47:07` | `cowrie.login.success` |
| `2026-08-16 14:47:42` | `cowrie.session.params` |
| `2026-08-16 14:47:42` | `cowrie.command.input` |
| `2026-08-16 14:47:42` | `cowrie.log.closed` |
| `2026-08-16 14:47:42` | `cowrie.session.file_upload` |
| `2026-08-16 14:47:42` | `cowrie.session.file_upload` |
| `2026-08-16 14:47:42` | `cowrie.session.file_upload` |
| `2026-08-16 14:47:42` | `cowrie.session.file_upload` |
| `2026-08-16 14:47:42` | `cowrie.session.file_upload` |
| `2026-08-16 14:47:42` | `cowrie.session.file_upload` |
| `2026-08-16 14:47:42` | `cowrie.session.file_upload` |
| `2026-08-16 14:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b471df4a7c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:47 |
| **Last Seen** | 2026-08-16 14:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:47:17` | `cowrie.session.connect` |
| `2026-08-16 14:47:17` | `cowrie.client.version` |
| `2026-08-16 14:47:17` | `cowrie.client.kex` |
| `2026-08-16 14:47:19` | `cowrie.login.success` |
| `2026-08-16 14:47:21` | `cowrie.session.params` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.success` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.command.input` |
| `2026-08-16 14:47:21` | `cowrie.log.closed` |
| `2026-08-16 14:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca2ff46a3c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 14:49 |
| **Last Seen** | 2026-08-16 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:49:20` | `cowrie.session.connect` |
| `2026-08-16 14:49:20` | `cowrie.client.version` |
| `2026-08-16 14:49:20` | `cowrie.client.kex` |
| `2026-08-16 14:49:20` | `cowrie.login.success` |
| `2026-08-16 14:49:21` | `cowrie.session.params` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.success` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.command.input` |
| `2026-08-16 14:49:21` | `cowrie.log.closed` |
| `2026-08-16 14:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64fe809c41c5

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 14:51 |
| **Last Seen** | 2026-08-16 14:52 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:51:54` | `cowrie.session.connect` |
| `2026-08-16 14:51:59` | `cowrie.client.version` |
| `2026-08-16 14:51:59` | `cowrie.client.kex` |
| `2026-08-16 14:52:19` | `cowrie.login.success` |
| `2026-08-16 14:52:31` | `cowrie.session.params` |
| `2026-08-16 14:52:31` | `cowrie.command.input` |
| `2026-08-16 14:52:36` | `cowrie.log.closed` |
| `2026-08-16 14:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a4855c6195

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 14:52 |
| **Last Seen** | 2026-08-16 14:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 14:52:29` | `cowrie.session.connect` |
| `2026-08-16 14:52:29` | `cowrie.client.version` |
| `2026-08-16 14:52:29` | `cowrie.client.kex` |
| `2026-08-16 14:52:30` | `cowrie.login.success` |
| `2026-08-16 14:52:31` | `cowrie.session.params` |
| `2026-08-16 14:52:31` | `cowrie.command.input` |
| `2026-08-16 14:52:31` | `cowrie.log.closed` |
| `2026-08-16 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4326** | 2026-08-16 12:55 | 2026-08-16 14:54 | 5047m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **43** | 2026-08-16 12:59 | 2026-08-16 14:53 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-16 12:57 | 2026-08-16 14:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]111` | **3** | 2026-08-16 14:36 | 2026-08-16 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-16 13:38 | 2026-08-16 14:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.175.213[.]4` | **3** | 2026-08-16 13:38 | 2026-08-16 13:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-08-16 14:25 | 2026-08-16 14:30 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.113.89[.]128` | 1 | 2026-08-16 14:31 | 2026-08-16 14:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `122.96.28[.]146` | 1 | 2026-08-16 14:31 | 2026-08-16 14:31 | 8s | 0 | `T1592` | 🟢 LOW |
| `158.94.210[.]42` | 1 | 2026-08-16 13:47 | 2026-08-16 13:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.244.203[.]96` | 1 | 2026-08-16 14:44 | 2026-08-16 14:44 | 11s | 0 | `T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-08-16 14:06 | 2026-08-16 14:06 | 9s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-08-16 13:02 | 2026-08-16 13:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.239.41[.]170` | 1 | 2026-08-16 14:23 | 2026-08-16 14:23 | 11s | 0 | `T1592` | 🟢 LOW |
| `185.74.59[.]14` | 1 | 2026-08-16 14:16 | 2026-08-16 14:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.66.23[.]215` | 1 | 2026-08-16 13:32 | 2026-08-16 13:32 | 10s | 0 | `T1592` | 🟢 LOW |
| `191.241.142[.]170` | 1 | 2026-08-16 13:32 | 2026-08-16 13:32 | 4s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-08-16 14:01 | 2026-08-16 14:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-08-16 13:33 | 2026-08-16 13:34 | 62s | 0 | `T1592` | 🟢 LOW |
| `223.210.27[.]53` | 1 | 2026-08-16 14:06 | 2026-08-16 14:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | 1 | 2026-08-16 13:17 | 2026-08-16 13:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-08-16 14:35 | 2026-08-16 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-16 13:37 | 2026-08-16 13:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]80` | 1 | 2026-08-16 12:56 | 2026-08-16 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.146[.]109` | 1 | 2026-08-16 13:02 | 2026-08-16 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]35` | 1 | 2026-08-16 14:51 | 2026-08-16 14:51 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]83` | 1 | 2026-08-16 14:24 | 2026-08-16 14:24 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-16 13:38 | 2026-08-16 13:38 | 2s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]157` | 1 | 2026-08-16 13:42 | 2026-08-16 13:42 | 2s | 0 | `T1592` | 🟢 LOW |

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
| `185.112.148[.]66` | IR | Sefroyek Pardaz Engineering PJSC | **100** ⚠️ | 15 |
| `61.12.86[.]90` | IN | TTSL-ISP DIVISION | **100** ⚠️ | 50 |
| `218.29.231[.]106` | CN | China Unicom Henan province network | **100** ⚠️ | 50 |
| `66.132.224[.]83` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `45.79.207[.]71` | US | Linode | **100** ⚠️ | 50 |
| `31.173.2[.]182` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `120.198.138[.]185` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `45.79.8[.]221` | US | Linode | **100** ⚠️ | 50 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 50 |
| `222.139.245[.]137` | CN | China Unicom Henan province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 60 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 8 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 10 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 4487 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (0.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 60 priority case(s) shown individually · 29 recon entry/entries in table (7 group(s) consolidating 4385 session(s)).

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
_Report time: 2026-08-16T16:29:17Z_

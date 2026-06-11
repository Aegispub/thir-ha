# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T20:30:35Z |
| **Shift Time** | 20:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **233** |
| Confirmed Threats | **209** |
| False Positives Filtered | **24** (10.3%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **15** |
| High Severity Cases | **130** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **103** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **130** |
| Unique Credential Pairs | **65** |
| Unique Usernames | **25** |
| Unique Passwords | **52** |
| Successful Auth Pairs | **70** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `sol` | 24 |
| `solana` | 24 |
| `root` | 23 |
| `trader` | 9 |
| `ubuntu` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 6 |
| `123` | 6 |
| `soul` | 6 |
| `trader` | 6 |
| `LeitboGi0ro` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 4 |
| `sol` | `sol` | 4 |
| `solana` | `solana` | 4 |
| `sol` | `1234` | 4 |
| `sol` | `123` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `june` | `june` | `213.209.159.56` | 2026-06-11T15:45:55 |
| `admin` | `admin` | `109.100.14.222` | 2026-06-11T16:03:00 |
| `root` | `password` | `188.64.139.147` | 2026-06-11T16:07:14 |
| `admin` | `cocopuff` | `2.57.121.112` | 2026-06-11T16:07:17 |
| `root` | `LeitboGi0ro` | `188.64.139.147` | 2026-06-11T16:07:18 |
| `root` | `MoeClub.org` | `188.64.139.147` | 2026-06-11T16:07:22 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-11T16:15:04 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-11T16:15:04 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-11T16:15:15 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-11T16:29:09 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-11T16:29:09 |
| `sol` | `sol` | `45.148.10.183` | 2026-06-11T16:32:03 |
| `solana` | `solana` | `45.148.10.183` | 2026-06-11T16:34:39 |
| `solana` | `1234` | `45.148.10.183` | 2026-06-11T16:36:22 |
| `sol` | `1234` | `45.148.10.183` | 2026-06-11T16:38:03 |
| `sol` | `123` | `45.148.10.183` | 2026-06-11T16:39:51 |
| `sol` | `Solana` | `45.148.10.183` | 2026-06-11T16:41:42 |
| `solana` | `123456789` | `45.148.10.183` | 2026-06-11T16:43:26 |
| `solana` | `12345678` | `45.148.10.183` | 2026-06-11T16:45:17 |
| `solana` | `1234567` | `45.148.10.183` | 2026-06-11T16:47:13 |
| `sol` | `1234567` | `45.148.10.183` | 2026-06-11T16:49:03 |
| `sol` | `1234567890` | `45.148.10.183` | 2026-06-11T16:50:49 |
| `sol` | `!@#$%^` | `45.148.10.183` | 2026-06-11T16:52:42 |
| `sol` | `Solana!` | `45.148.10.183` | 2026-06-11T16:54:34 |
| `root` | `Solana!` | `45.148.10.183` | 2026-06-11T16:56:21 |
| `admin` | `admin` | `195.178.110.204` | 2026-06-11T16:57:34 |
| `root` | `solana!@#` | `45.148.10.183` | 2026-06-11T16:58:14 |
| `solana` | `qwer1234` | `45.148.10.183` | 2026-06-11T17:00:12 |
| `marla` | `marla` | `213.209.159.56` | 2026-06-11T17:00:23 |
| `solana` | `1234qwer` | `45.148.10.183` | 2026-06-11T17:02:03 |
| `solana` | `1qaz@WSX3edc` | `45.148.10.183` | 2026-06-11T17:03:53 |
| `admin` | `admin` | `185.38.148.2` | 2026-06-11T17:04:52 |
| `solana` | `SOL` | `45.148.10.183` | 2026-06-11T17:05:50 |
| `solana` | `sols` | `45.148.10.183` | 2026-06-11T17:07:44 |
| `sols` | `sols` | `45.148.10.183` | 2026-06-11T17:09:33 |
| `jito` | `jito` | `45.148.10.183` | 2026-06-11T17:11:29 |
| `soul` | `soul` | `45.148.10.183` | 2026-06-11T17:13:26 |
| `sol` | `soul` | `45.148.10.183` | 2026-06-11T17:15:16 |
| `solana` | `soul` | `45.148.10.183` | 2026-06-11T17:17:08 |
| `sole` | `sole` | `45.148.10.183` | 2026-06-11T17:19:07 |
| `solv` | `solv123` | `45.148.10.183` | 2026-06-11T17:21:01 |
| `solv` | `123456` | `45.148.10.183` | 2026-06-11T17:22:54 |
| `admin` | `cleodog` | `2.57.121.112` | 2026-06-11T17:22:56 |
| `solb` | `solb` | `45.148.10.183` | 2026-06-11T17:24:55 |
| `solz` | `solz` | `45.148.10.183` | 2026-06-11T17:26:52 |
| `firedancer` | `firedancer` | `45.148.10.183` | 2026-06-11T17:28:46 |
| `root` | `firedancer` | `45.148.10.183` | 2026-06-11T17:30:43 |
| `root` | `shredstream` | `45.148.10.183` | 2026-06-11T17:32:43 |
| `shred` | `shred` | `45.148.10.183` | 2026-06-11T17:34:41 |
| `validator` | `123` | `45.148.10.183` | 2026-06-11T17:36:42 |
| `binance` | `binance` | `45.148.10.183` | 2026-06-11T17:38:45 |
| `trader` | `trader` | `45.148.10.183` | 2026-06-11T17:40:41 |
| `trading` | `trading` | `45.148.10.183` | 2026-06-11T17:42:39 |
| `ubuntu` | `trader` | `45.148.10.183` | 2026-06-11T17:44:37 |
| `bitcoin` | `bitcoin` | `45.148.10.183` | 2026-06-11T17:46:34 |
| `ethereum` | `ethereum` | `45.148.10.183` | 2026-06-11T17:48:31 |
| `root` | `trader` | `45.148.10.183` | 2026-06-11T17:50:34 |
| `trader` | `trader123` | `45.148.10.183` | 2026-06-11T17:52:33 |
| `trader` | `trader1234` | `45.148.10.183` | 2026-06-11T17:54:31 |
| `trader` | `ibkr123` | `45.148.10.183` | 2026-06-11T17:56:32 |
| `root` | `ibkr123` | `45.148.10.183` | 2026-06-11T17:58:28 |
| `exchange` | `exchange` | `45.148.10.183` | 2026-06-11T18:00:22 |
| `root` | `kipCAjudrK` | `10.0.0.73` | 2026-06-11T18:01:36 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-11T18:02:34 |
| `ubuntu` | `ubuntu` | `45.148.10.183` | 2026-06-11T18:10:26 |
| `ubuntu` | `123456` | `45.148.10.183` | 2026-06-11T18:12:22 |
| `michael` | `michael` | `213.209.159.56` | 2026-06-11T18:14:09 |
| `ubuntu` | `12345678` | `45.148.10.183` | 2026-06-11T18:14:18 |
| `pool` | `pool` | `45.148.10.183` | 2026-06-11T18:20:12 |
| `admin` | `cisco123` | `2.57.121.112` | 2026-06-11T18:38:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **233** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 130 |
| PuTTY | 7 |
| Paramiko (Python) | 6 |
| OpenSSH | 2 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 115 | 4 |
| `57446c12547a...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `9052c4ab4164...` | Mirai/variant | 2 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 115 | 4 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 13 | 4 | — |
| `57446c12547a...` | PuTTY | 6 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `9052c4ab4164...` | OpenSSH | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **28** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | LOW |
| `AS396982` | Google LLC | 3 | LOW |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (128)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3a000a03807c

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 15:45 |
| **Last Seen** | 2026-06-11 15:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 15:45:54` | `cowrie.session.connect` |
| `2026-06-11 15:45:54` | `cowrie.client.version` |
| `2026-06-11 15:45:55` | `cowrie.client.kex` |
| `2026-06-11 15:45:55` | `cowrie.login.success` |
| `2026-06-11 15:45:55` | `cowrie.direct-tcpip.request` |
| `2026-06-11 15:45:55` | `cowrie.direct-tcpip.data` |
| `2026-06-11 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afd278a565dc

| Field | Detail |
|---|---|
| **Source IP** | `109.100.14[.]222` |
| **First Seen** | 2026-06-11 16:01 |
| **Last Seen** | 2026-06-11 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:01:59` | `cowrie.session.connect` |
| `2026-06-11 16:01:59` | `cowrie.telnet.option` |
| `2026-06-11 16:02:00` | `cowrie.telnet.option` |
| `2026-06-11 16:03:00` | `cowrie.login.success` |
| `2026-06-11 16:03:01` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `109.100.14[.]222` to AbuseIPDB if not already reported
- [ ] Block `109.100.14[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13dfafdab75b

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-11 16:07 |
| **Last Seen** | 2026-06-11 16:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:07:12` | `cowrie.session.connect` |
| `2026-06-11 16:07:12` | `cowrie.client.version` |
| `2026-06-11 16:07:12` | `cowrie.client.kex` |
| `2026-06-11 16:07:14` | `cowrie.login.success` |
| `2026-06-11 16:07:15` | `cowrie.session.params` |
| `2026-06-11 16:07:15` | `cowrie.command.input` |
| `2026-06-11 16:07:16` | `cowrie.log.closed` |
| `2026-06-11 16:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c298193969

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-11 16:07 |
| **Last Seen** | 2026-06-11 16:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:07:16` | `cowrie.session.connect` |
| `2026-06-11 16:07:16` | `cowrie.client.version` |
| `2026-06-11 16:07:16` | `cowrie.client.kex` |
| `2026-06-11 16:07:18` | `cowrie.login.success` |
| `2026-06-11 16:07:19` | `cowrie.session.params` |
| `2026-06-11 16:07:19` | `cowrie.command.input` |
| `2026-06-11 16:07:20` | `cowrie.log.closed` |
| `2026-06-11 16:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152ad64b84d9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 16:07 |
| **Last Seen** | 2026-06-11 16:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:07:16` | `cowrie.session.connect` |
| `2026-06-11 16:07:16` | `cowrie.client.version` |
| `2026-06-11 16:07:16` | `cowrie.client.kex` |
| `2026-06-11 16:07:17` | `cowrie.login.success` |
| `2026-06-11 16:07:17` | `cowrie.direct-tcpip.request` |
| `2026-06-11 16:07:17` | `cowrie.direct-tcpip.data` |
| `2026-06-11 16:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498557fb8e25

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-11 16:07 |
| **Last Seen** | 2026-06-11 16:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:07:20` | `cowrie.session.connect` |
| `2026-06-11 16:07:21` | `cowrie.client.version` |
| `2026-06-11 16:07:21` | `cowrie.client.kex` |
| `2026-06-11 16:07:22` | `cowrie.login.success` |
| `2026-06-11 16:07:24` | `cowrie.session.params` |
| `2026-06-11 16:07:24` | `cowrie.command.input` |
| `2026-06-11 16:07:24` | `cowrie.log.closed` |
| `2026-06-11 16:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b824d0d14c7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 16:15 |
| **Last Seen** | 2026-06-11 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:15:04` | `cowrie.session.connect` |
| `2026-06-11 16:15:04` | `cowrie.client.version` |
| `2026-06-11 16:15:04` | `cowrie.client.kex` |
| `2026-06-11 16:15:04` | `cowrie.login.success` |
| `2026-06-11 16:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfdd56b8461d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 16:15 |
| **Last Seen** | 2026-06-11 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:15:04` | `cowrie.session.connect` |
| `2026-06-11 16:15:04` | `cowrie.client.version` |
| `2026-06-11 16:15:04` | `cowrie.client.kex` |
| `2026-06-11 16:15:04` | `cowrie.login.success` |
| `2026-06-11 16:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3225f1f712ac

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 16:15 |
| **Last Seen** | 2026-06-11 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:15:15` | `cowrie.session.connect` |
| `2026-06-11 16:15:15` | `cowrie.client.version` |
| `2026-06-11 16:15:15` | `cowrie.client.kex` |
| `2026-06-11 16:15:15` | `cowrie.login.success` |
| `2026-06-11 16:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621728306cdc

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 16:29 |
| **Last Seen** | 2026-06-11 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:29:08` | `cowrie.session.connect` |
| `2026-06-11 16:29:08` | `cowrie.client.version` |
| `2026-06-11 16:29:08` | `cowrie.client.kex` |
| `2026-06-11 16:29:09` | `cowrie.login.success` |
| `2026-06-11 16:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1756d90be3

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 16:29 |
| **Last Seen** | 2026-06-11 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:29:08` | `cowrie.session.connect` |
| `2026-06-11 16:29:08` | `cowrie.client.version` |
| `2026-06-11 16:29:08` | `cowrie.client.kex` |
| `2026-06-11 16:29:09` | `cowrie.login.success` |
| `2026-06-11 16:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d18bc9365e

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 16:29 |
| **Last Seen** | 2026-06-11 16:31 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:29:28` | `cowrie.session.connect` |
| `2026-06-11 16:29:28` | `cowrie.client.version` |
| `2026-06-11 16:29:28` | `cowrie.client.kex` |
| `2026-06-11 16:29:30` | `cowrie.login.success` |
| `2026-06-11 16:29:32` | `cowrie.session.file_upload` |
| `2026-06-11 16:29:33` | `cowrie.session.params` |
| `2026-06-11 16:29:33` | `cowrie.command.input` |
| `2026-06-11 16:29:33` | `cowrie.command.input` |
| `2026-06-11 16:29:33` | `cowrie.command.input` |
| `2026-06-11 16:29:33` | `cowrie.command.failed` |
| `2026-06-11 16:29:33` | `cowrie.log.closed` |
| `2026-06-11 16:29:34` | `cowrie.session.params` |
| `2026-06-11 16:29:34` | `cowrie.command.input` |
| `2026-06-11 16:29:35` | `cowrie.log.closed` |
| `2026-06-11 16:29:35` | `cowrie.session.params` |
| `2026-06-11 16:29:35` | `cowrie.command.input` |
| `2026-06-11 16:29:36` | `cowrie.log.closed` |
| `2026-06-11 16:29:37` | `cowrie.session.params` |
| `2026-06-11 16:29:37` | `cowrie.command.input` |
| `2026-06-11 16:29:37` | `cowrie.command.failed` |
| `2026-06-11 16:29:37` | `cowrie.command.failed` |
| `2026-06-11 16:30:38` | `cowrie.session.params` |
| `2026-06-11 16:30:38` | `cowrie.command.input` |
| `2026-06-11 16:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfbef7d06263

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:32 |
| **Last Seen** | 2026-06-11 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:32:03` | `cowrie.session.connect` |
| `2026-06-11 16:32:03` | `cowrie.client.version` |
| `2026-06-11 16:32:03` | `cowrie.client.kex` |
| `2026-06-11 16:32:03` | `cowrie.login.success` |
| `2026-06-11 16:32:04` | `cowrie.session.params` |
| `2026-06-11 16:32:04` | `cowrie.command.input` |
| `2026-06-11 16:32:04` | `cowrie.log.closed` |
| `2026-06-11 16:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993165ef55fd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:32 |
| **Last Seen** | 2026-06-11 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:32:48` | `cowrie.session.connect` |
| `2026-06-11 16:32:48` | `cowrie.client.version` |
| `2026-06-11 16:32:48` | `cowrie.client.kex` |
| `2026-06-11 16:32:49` | `cowrie.login.success` |
| `2026-06-11 16:32:50` | `cowrie.session.params` |
| `2026-06-11 16:32:50` | `cowrie.command.input` |
| `2026-06-11 16:32:50` | `cowrie.log.closed` |
| `2026-06-11 16:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07f07730c57

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:34 |
| **Last Seen** | 2026-06-11 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:34:38` | `cowrie.session.connect` |
| `2026-06-11 16:34:38` | `cowrie.client.version` |
| `2026-06-11 16:34:38` | `cowrie.client.kex` |
| `2026-06-11 16:34:39` | `cowrie.login.success` |
| `2026-06-11 16:34:39` | `cowrie.session.params` |
| `2026-06-11 16:34:39` | `cowrie.command.input` |
| `2026-06-11 16:34:39` | `cowrie.log.closed` |
| `2026-06-11 16:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2312438378

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:34 |
| **Last Seen** | 2026-06-11 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:34:53` | `cowrie.session.connect` |
| `2026-06-11 16:34:53` | `cowrie.client.version` |
| `2026-06-11 16:34:53` | `cowrie.client.kex` |
| `2026-06-11 16:34:54` | `cowrie.login.success` |
| `2026-06-11 16:34:55` | `cowrie.session.params` |
| `2026-06-11 16:34:55` | `cowrie.command.input` |
| `2026-06-11 16:34:55` | `cowrie.log.closed` |
| `2026-06-11 16:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072a5c8e3e51

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:36 |
| **Last Seen** | 2026-06-11 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:36:22` | `cowrie.session.connect` |
| `2026-06-11 16:36:22` | `cowrie.client.version` |
| `2026-06-11 16:36:22` | `cowrie.client.kex` |
| `2026-06-11 16:36:22` | `cowrie.login.success` |
| `2026-06-11 16:36:23` | `cowrie.session.params` |
| `2026-06-11 16:36:23` | `cowrie.command.input` |
| `2026-06-11 16:36:23` | `cowrie.log.closed` |
| `2026-06-11 16:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a618ac3a8b0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:37 |
| **Last Seen** | 2026-06-11 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:37:18` | `cowrie.session.connect` |
| `2026-06-11 16:37:18` | `cowrie.client.version` |
| `2026-06-11 16:37:18` | `cowrie.client.kex` |
| `2026-06-11 16:37:18` | `cowrie.login.success` |
| `2026-06-11 16:37:19` | `cowrie.session.params` |
| `2026-06-11 16:37:19` | `cowrie.command.input` |
| `2026-06-11 16:37:19` | `cowrie.log.closed` |
| `2026-06-11 16:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc72223c7f8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:38 |
| **Last Seen** | 2026-06-11 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:38:03` | `cowrie.session.connect` |
| `2026-06-11 16:38:03` | `cowrie.client.version` |
| `2026-06-11 16:38:03` | `cowrie.client.kex` |
| `2026-06-11 16:38:03` | `cowrie.login.success` |
| `2026-06-11 16:38:04` | `cowrie.session.params` |
| `2026-06-11 16:38:04` | `cowrie.command.input` |
| `2026-06-11 16:38:04` | `cowrie.log.closed` |
| `2026-06-11 16:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e267f623985

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:39 |
| **Last Seen** | 2026-06-11 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:39:50` | `cowrie.session.connect` |
| `2026-06-11 16:39:50` | `cowrie.client.version` |
| `2026-06-11 16:39:50` | `cowrie.client.kex` |
| `2026-06-11 16:39:51` | `cowrie.login.success` |
| `2026-06-11 16:39:51` | `cowrie.session.params` |
| `2026-06-11 16:39:51` | `cowrie.command.input` |
| `2026-06-11 16:39:52` | `cowrie.log.closed` |
| `2026-06-11 16:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-773511e62912

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:39 |
| **Last Seen** | 2026-06-11 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:39:50` | `cowrie.session.connect` |
| `2026-06-11 16:39:50` | `cowrie.client.version` |
| `2026-06-11 16:39:51` | `cowrie.client.kex` |
| `2026-06-11 16:39:51` | `cowrie.login.success` |
| `2026-06-11 16:39:52` | `cowrie.session.params` |
| `2026-06-11 16:39:52` | `cowrie.command.input` |
| `2026-06-11 16:39:52` | `cowrie.log.closed` |
| `2026-06-11 16:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717856aa52d9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:41 |
| **Last Seen** | 2026-06-11 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:41:41` | `cowrie.session.connect` |
| `2026-06-11 16:41:41` | `cowrie.client.version` |
| `2026-06-11 16:41:41` | `cowrie.client.kex` |
| `2026-06-11 16:41:42` | `cowrie.login.success` |
| `2026-06-11 16:41:42` | `cowrie.session.params` |
| `2026-06-11 16:41:42` | `cowrie.command.input` |
| `2026-06-11 16:41:43` | `cowrie.log.closed` |
| `2026-06-11 16:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352632168330

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:42 |
| **Last Seen** | 2026-06-11 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:42:27` | `cowrie.session.connect` |
| `2026-06-11 16:42:27` | `cowrie.client.version` |
| `2026-06-11 16:42:27` | `cowrie.client.kex` |
| `2026-06-11 16:42:27` | `cowrie.login.success` |
| `2026-06-11 16:42:28` | `cowrie.session.params` |
| `2026-06-11 16:42:28` | `cowrie.command.input` |
| `2026-06-11 16:42:28` | `cowrie.log.closed` |
| `2026-06-11 16:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06780e53ad8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:43 |
| **Last Seen** | 2026-06-11 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:43:26` | `cowrie.session.connect` |
| `2026-06-11 16:43:26` | `cowrie.client.version` |
| `2026-06-11 16:43:26` | `cowrie.client.kex` |
| `2026-06-11 16:43:26` | `cowrie.login.success` |
| `2026-06-11 16:43:27` | `cowrie.session.params` |
| `2026-06-11 16:43:27` | `cowrie.command.input` |
| `2026-06-11 16:43:27` | `cowrie.log.closed` |
| `2026-06-11 16:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6be9af2b01a1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:45 |
| **Last Seen** | 2026-06-11 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:45:02` | `cowrie.session.connect` |
| `2026-06-11 16:45:02` | `cowrie.client.version` |
| `2026-06-11 16:45:02` | `cowrie.client.kex` |
| `2026-06-11 16:45:02` | `cowrie.login.success` |
| `2026-06-11 16:45:03` | `cowrie.session.params` |
| `2026-06-11 16:45:03` | `cowrie.command.input` |
| `2026-06-11 16:45:03` | `cowrie.log.closed` |
| `2026-06-11 16:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909a4f7f2580

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:45 |
| **Last Seen** | 2026-06-11 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:45:17` | `cowrie.session.connect` |
| `2026-06-11 16:45:17` | `cowrie.client.version` |
| `2026-06-11 16:45:17` | `cowrie.client.kex` |
| `2026-06-11 16:45:17` | `cowrie.login.success` |
| `2026-06-11 16:45:18` | `cowrie.session.params` |
| `2026-06-11 16:45:18` | `cowrie.command.input` |
| `2026-06-11 16:45:18` | `cowrie.log.closed` |
| `2026-06-11 16:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1218318d29d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:47 |
| **Last Seen** | 2026-06-11 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:47:13` | `cowrie.session.connect` |
| `2026-06-11 16:47:13` | `cowrie.client.version` |
| `2026-06-11 16:47:13` | `cowrie.client.kex` |
| `2026-06-11 16:47:13` | `cowrie.login.success` |
| `2026-06-11 16:47:14` | `cowrie.session.params` |
| `2026-06-11 16:47:14` | `cowrie.command.input` |
| `2026-06-11 16:47:14` | `cowrie.log.closed` |
| `2026-06-11 16:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4caa54ed6e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:47 |
| **Last Seen** | 2026-06-11 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:47:48` | `cowrie.session.connect` |
| `2026-06-11 16:47:48` | `cowrie.client.version` |
| `2026-06-11 16:47:49` | `cowrie.client.kex` |
| `2026-06-11 16:47:49` | `cowrie.login.success` |
| `2026-06-11 16:47:50` | `cowrie.session.params` |
| `2026-06-11 16:47:50` | `cowrie.command.input` |
| `2026-06-11 16:47:50` | `cowrie.log.closed` |
| `2026-06-11 16:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e637f6a787c3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:49 |
| **Last Seen** | 2026-06-11 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:49:03` | `cowrie.session.connect` |
| `2026-06-11 16:49:03` | `cowrie.client.version` |
| `2026-06-11 16:49:03` | `cowrie.client.kex` |
| `2026-06-11 16:49:03` | `cowrie.login.success` |
| `2026-06-11 16:49:04` | `cowrie.session.params` |
| `2026-06-11 16:49:04` | `cowrie.command.input` |
| `2026-06-11 16:49:04` | `cowrie.log.closed` |
| `2026-06-11 16:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54cbb51566a6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:50 |
| **Last Seen** | 2026-06-11 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:50:15` | `cowrie.session.connect` |
| `2026-06-11 16:50:15` | `cowrie.client.version` |
| `2026-06-11 16:50:16` | `cowrie.client.kex` |
| `2026-06-11 16:50:16` | `cowrie.login.success` |
| `2026-06-11 16:50:17` | `cowrie.session.params` |
| `2026-06-11 16:50:17` | `cowrie.command.input` |
| `2026-06-11 16:50:17` | `cowrie.log.closed` |
| `2026-06-11 16:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a062292abf10

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:50 |
| **Last Seen** | 2026-06-11 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:50:49` | `cowrie.session.connect` |
| `2026-06-11 16:50:49` | `cowrie.client.version` |
| `2026-06-11 16:50:49` | `cowrie.client.kex` |
| `2026-06-11 16:50:49` | `cowrie.login.success` |
| `2026-06-11 16:50:50` | `cowrie.session.params` |
| `2026-06-11 16:50:50` | `cowrie.command.input` |
| `2026-06-11 16:50:50` | `cowrie.log.closed` |
| `2026-06-11 16:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8c1d660d92

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:52 |
| **Last Seen** | 2026-06-11 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:52:41` | `cowrie.session.connect` |
| `2026-06-11 16:52:41` | `cowrie.client.version` |
| `2026-06-11 16:52:42` | `cowrie.client.kex` |
| `2026-06-11 16:52:42` | `cowrie.login.success` |
| `2026-06-11 16:52:42` | `cowrie.session.params` |
| `2026-06-11 16:52:42` | `cowrie.command.input` |
| `2026-06-11 16:52:43` | `cowrie.log.closed` |
| `2026-06-11 16:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1e11bf309e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:52 |
| **Last Seen** | 2026-06-11 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:52:52` | `cowrie.session.connect` |
| `2026-06-11 16:52:52` | `cowrie.client.version` |
| `2026-06-11 16:52:52` | `cowrie.client.kex` |
| `2026-06-11 16:52:52` | `cowrie.login.success` |
| `2026-06-11 16:52:53` | `cowrie.session.params` |
| `2026-06-11 16:52:53` | `cowrie.command.input` |
| `2026-06-11 16:52:53` | `cowrie.log.closed` |
| `2026-06-11 16:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5121e9b244d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:54 |
| **Last Seen** | 2026-06-11 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:54:34` | `cowrie.session.connect` |
| `2026-06-11 16:54:34` | `cowrie.client.version` |
| `2026-06-11 16:54:34` | `cowrie.client.kex` |
| `2026-06-11 16:54:34` | `cowrie.login.success` |
| `2026-06-11 16:54:35` | `cowrie.session.params` |
| `2026-06-11 16:54:35` | `cowrie.command.input` |
| `2026-06-11 16:54:35` | `cowrie.log.closed` |
| `2026-06-11 16:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84872b25977

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:55 |
| **Last Seen** | 2026-06-11 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:55:27` | `cowrie.session.connect` |
| `2026-06-11 16:55:27` | `cowrie.client.version` |
| `2026-06-11 16:55:27` | `cowrie.client.kex` |
| `2026-06-11 16:55:28` | `cowrie.login.success` |
| `2026-06-11 16:55:28` | `cowrie.session.params` |
| `2026-06-11 16:55:28` | `cowrie.command.input` |
| `2026-06-11 16:55:29` | `cowrie.log.closed` |
| `2026-06-11 16:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a16c39eba2b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:56 |
| **Last Seen** | 2026-06-11 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:56:21` | `cowrie.session.connect` |
| `2026-06-11 16:56:21` | `cowrie.client.version` |
| `2026-06-11 16:56:21` | `cowrie.client.kex` |
| `2026-06-11 16:56:21` | `cowrie.login.success` |
| `2026-06-11 16:56:22` | `cowrie.session.params` |
| `2026-06-11 16:56:22` | `cowrie.command.input` |
| `2026-06-11 16:56:22` | `cowrie.log.closed` |
| `2026-06-11 16:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbcdb71e4d2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]204` |
| **First Seen** | 2026-06-11 16:57 |
| **Last Seen** | 2026-06-11 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:57:03` | `cowrie.session.connect` |
| `2026-06-11 16:57:03` | `cowrie.telnet.option` |
| `2026-06-11 16:57:03` | `cowrie.telnet.option` |
| `2026-06-11 16:57:34` | `cowrie.login.success` |
| `2026-06-11 16:57:34` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]204` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91123875efd2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:58 |
| **Last Seen** | 2026-06-11 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:58:05` | `cowrie.session.connect` |
| `2026-06-11 16:58:05` | `cowrie.client.version` |
| `2026-06-11 16:58:05` | `cowrie.client.kex` |
| `2026-06-11 16:58:06` | `cowrie.login.success` |
| `2026-06-11 16:58:07` | `cowrie.session.params` |
| `2026-06-11 16:58:07` | `cowrie.command.input` |
| `2026-06-11 16:58:07` | `cowrie.log.closed` |
| `2026-06-11 16:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ec656cabb2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 16:58 |
| **Last Seen** | 2026-06-11 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:58:13` | `cowrie.session.connect` |
| `2026-06-11 16:58:13` | `cowrie.client.version` |
| `2026-06-11 16:58:13` | `cowrie.client.kex` |
| `2026-06-11 16:58:14` | `cowrie.login.success` |
| `2026-06-11 16:58:15` | `cowrie.session.params` |
| `2026-06-11 16:58:15` | `cowrie.command.input` |
| `2026-06-11 16:58:15` | `cowrie.log.closed` |
| `2026-06-11 16:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78f91239260

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:00 |
| **Last Seen** | 2026-06-11 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:00:12` | `cowrie.session.connect` |
| `2026-06-11 17:00:12` | `cowrie.client.version` |
| `2026-06-11 17:00:12` | `cowrie.client.kex` |
| `2026-06-11 17:00:12` | `cowrie.login.success` |
| `2026-06-11 17:00:13` | `cowrie.session.params` |
| `2026-06-11 17:00:13` | `cowrie.command.input` |
| `2026-06-11 17:00:13` | `cowrie.log.closed` |
| `2026-06-11 17:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0528da6667

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 17:00 |
| **Last Seen** | 2026-06-11 17:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:00:22` | `cowrie.session.connect` |
| `2026-06-11 17:00:22` | `cowrie.client.version` |
| `2026-06-11 17:00:22` | `cowrie.client.kex` |
| `2026-06-11 17:00:23` | `cowrie.login.success` |
| `2026-06-11 17:00:23` | `cowrie.direct-tcpip.request` |
| `2026-06-11 17:00:23` | `cowrie.direct-tcpip.data` |
| `2026-06-11 17:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a18737a8bc7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:00 |
| **Last Seen** | 2026-06-11 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:00:52` | `cowrie.session.connect` |
| `2026-06-11 17:00:52` | `cowrie.client.version` |
| `2026-06-11 17:00:52` | `cowrie.client.kex` |
| `2026-06-11 17:00:52` | `cowrie.login.success` |
| `2026-06-11 17:00:53` | `cowrie.session.params` |
| `2026-06-11 17:00:53` | `cowrie.command.input` |
| `2026-06-11 17:00:53` | `cowrie.log.closed` |
| `2026-06-11 17:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ffc8a2374df

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:02 |
| **Last Seen** | 2026-06-11 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:02:02` | `cowrie.session.connect` |
| `2026-06-11 17:02:02` | `cowrie.client.version` |
| `2026-06-11 17:02:02` | `cowrie.client.kex` |
| `2026-06-11 17:02:03` | `cowrie.login.success` |
| `2026-06-11 17:02:03` | `cowrie.session.params` |
| `2026-06-11 17:02:03` | `cowrie.command.input` |
| `2026-06-11 17:02:03` | `cowrie.log.closed` |
| `2026-06-11 17:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4e28d509b6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:03 |
| **Last Seen** | 2026-06-11 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:03:23` | `cowrie.session.connect` |
| `2026-06-11 17:03:23` | `cowrie.client.version` |
| `2026-06-11 17:03:23` | `cowrie.client.kex` |
| `2026-06-11 17:03:23` | `cowrie.login.success` |
| `2026-06-11 17:03:24` | `cowrie.session.params` |
| `2026-06-11 17:03:24` | `cowrie.command.input` |
| `2026-06-11 17:03:24` | `cowrie.log.closed` |
| `2026-06-11 17:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74032d453eee

| Field | Detail |
|---|---|
| **Source IP** | `185.38.148[.]2` |
| **First Seen** | 2026-06-11 17:03 |
| **Last Seen** | 2026-06-11 17:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:03:52` | `cowrie.session.connect` |
| `2026-06-11 17:03:52` | `cowrie.telnet.option` |
| `2026-06-11 17:03:52` | `cowrie.telnet.option` |
| `2026-06-11 17:04:52` | `cowrie.login.success` |
| `2026-06-11 17:04:52` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `185.38.148[.]2` to AbuseIPDB if not already reported
- [ ] Block `185.38.148[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f3b03bbb5c3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:03 |
| **Last Seen** | 2026-06-11 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:03:52` | `cowrie.session.connect` |
| `2026-06-11 17:03:52` | `cowrie.client.version` |
| `2026-06-11 17:03:52` | `cowrie.client.kex` |
| `2026-06-11 17:03:53` | `cowrie.login.success` |
| `2026-06-11 17:03:53` | `cowrie.session.params` |
| `2026-06-11 17:03:53` | `cowrie.command.input` |
| `2026-06-11 17:03:53` | `cowrie.log.closed` |
| `2026-06-11 17:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc63f40a2f12

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:05 |
| **Last Seen** | 2026-06-11 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:05:49` | `cowrie.session.connect` |
| `2026-06-11 17:05:49` | `cowrie.client.version` |
| `2026-06-11 17:05:50` | `cowrie.client.kex` |
| `2026-06-11 17:05:50` | `cowrie.login.success` |
| `2026-06-11 17:05:51` | `cowrie.session.params` |
| `2026-06-11 17:05:51` | `cowrie.command.input` |
| `2026-06-11 17:05:51` | `cowrie.log.closed` |
| `2026-06-11 17:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ecac553ecc3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:06 |
| **Last Seen** | 2026-06-11 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:06:03` | `cowrie.session.connect` |
| `2026-06-11 17:06:03` | `cowrie.client.version` |
| `2026-06-11 17:06:04` | `cowrie.client.kex` |
| `2026-06-11 17:06:04` | `cowrie.login.success` |
| `2026-06-11 17:06:05` | `cowrie.session.params` |
| `2026-06-11 17:06:05` | `cowrie.command.input` |
| `2026-06-11 17:06:05` | `cowrie.log.closed` |
| `2026-06-11 17:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289fb395a244

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:07 |
| **Last Seen** | 2026-06-11 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:07:43` | `cowrie.session.connect` |
| `2026-06-11 17:07:43` | `cowrie.client.version` |
| `2026-06-11 17:07:43` | `cowrie.client.kex` |
| `2026-06-11 17:07:44` | `cowrie.login.success` |
| `2026-06-11 17:07:44` | `cowrie.session.params` |
| `2026-06-11 17:07:44` | `cowrie.command.input` |
| `2026-06-11 17:07:44` | `cowrie.log.closed` |
| `2026-06-11 17:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd973602fe2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:08 |
| **Last Seen** | 2026-06-11 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:08:41` | `cowrie.session.connect` |
| `2026-06-11 17:08:41` | `cowrie.client.version` |
| `2026-06-11 17:08:41` | `cowrie.client.kex` |
| `2026-06-11 17:08:41` | `cowrie.login.success` |
| `2026-06-11 17:08:42` | `cowrie.session.params` |
| `2026-06-11 17:08:42` | `cowrie.command.input` |
| `2026-06-11 17:08:42` | `cowrie.log.closed` |
| `2026-06-11 17:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecdefcd0ca75

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:09 |
| **Last Seen** | 2026-06-11 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:09:33` | `cowrie.session.connect` |
| `2026-06-11 17:09:33` | `cowrie.client.version` |
| `2026-06-11 17:09:33` | `cowrie.client.kex` |
| `2026-06-11 17:09:33` | `cowrie.login.success` |
| `2026-06-11 17:09:34` | `cowrie.session.params` |
| `2026-06-11 17:09:34` | `cowrie.command.input` |
| `2026-06-11 17:09:34` | `cowrie.log.closed` |
| `2026-06-11 17:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba6b5bdb8cb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:11 |
| **Last Seen** | 2026-06-11 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:11:23` | `cowrie.session.connect` |
| `2026-06-11 17:11:23` | `cowrie.client.version` |
| `2026-06-11 17:11:23` | `cowrie.client.kex` |
| `2026-06-11 17:11:24` | `cowrie.login.success` |
| `2026-06-11 17:11:24` | `cowrie.session.params` |
| `2026-06-11 17:11:24` | `cowrie.command.input` |
| `2026-06-11 17:11:25` | `cowrie.log.closed` |
| `2026-06-11 17:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef67bd1786e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:11 |
| **Last Seen** | 2026-06-11 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:11:28` | `cowrie.session.connect` |
| `2026-06-11 17:11:28` | `cowrie.client.version` |
| `2026-06-11 17:11:29` | `cowrie.client.kex` |
| `2026-06-11 17:11:29` | `cowrie.login.success` |
| `2026-06-11 17:11:30` | `cowrie.session.params` |
| `2026-06-11 17:11:30` | `cowrie.command.input` |
| `2026-06-11 17:11:30` | `cowrie.log.closed` |
| `2026-06-11 17:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a0bd269898

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:13 |
| **Last Seen** | 2026-06-11 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:13:26` | `cowrie.session.connect` |
| `2026-06-11 17:13:26` | `cowrie.client.version` |
| `2026-06-11 17:13:26` | `cowrie.client.kex` |
| `2026-06-11 17:13:26` | `cowrie.login.success` |
| `2026-06-11 17:13:27` | `cowrie.session.params` |
| `2026-06-11 17:13:27` | `cowrie.command.input` |
| `2026-06-11 17:13:27` | `cowrie.log.closed` |
| `2026-06-11 17:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e3323238d3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:14 |
| **Last Seen** | 2026-06-11 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:14:07` | `cowrie.session.connect` |
| `2026-06-11 17:14:07` | `cowrie.client.version` |
| `2026-06-11 17:14:07` | `cowrie.client.kex` |
| `2026-06-11 17:14:07` | `cowrie.login.success` |
| `2026-06-11 17:14:08` | `cowrie.session.params` |
| `2026-06-11 17:14:08` | `cowrie.command.input` |
| `2026-06-11 17:14:08` | `cowrie.log.closed` |
| `2026-06-11 17:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b92f53bbf02

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:15 |
| **Last Seen** | 2026-06-11 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:15:15` | `cowrie.session.connect` |
| `2026-06-11 17:15:15` | `cowrie.client.version` |
| `2026-06-11 17:15:16` | `cowrie.client.kex` |
| `2026-06-11 17:15:16` | `cowrie.login.success` |
| `2026-06-11 17:15:17` | `cowrie.session.params` |
| `2026-06-11 17:15:17` | `cowrie.command.input` |
| `2026-06-11 17:15:17` | `cowrie.log.closed` |
| `2026-06-11 17:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9243f1ba656b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:16 |
| **Last Seen** | 2026-06-11 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:16:37` | `cowrie.session.connect` |
| `2026-06-11 17:16:37` | `cowrie.client.version` |
| `2026-06-11 17:16:37` | `cowrie.client.kex` |
| `2026-06-11 17:16:37` | `cowrie.login.success` |
| `2026-06-11 17:16:38` | `cowrie.session.params` |
| `2026-06-11 17:16:38` | `cowrie.command.input` |
| `2026-06-11 17:16:38` | `cowrie.log.closed` |
| `2026-06-11 17:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d439f60b699c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:17 |
| **Last Seen** | 2026-06-11 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:17:07` | `cowrie.session.connect` |
| `2026-06-11 17:17:07` | `cowrie.client.version` |
| `2026-06-11 17:17:07` | `cowrie.client.kex` |
| `2026-06-11 17:17:08` | `cowrie.login.success` |
| `2026-06-11 17:17:09` | `cowrie.session.params` |
| `2026-06-11 17:17:09` | `cowrie.command.input` |
| `2026-06-11 17:17:09` | `cowrie.log.closed` |
| `2026-06-11 17:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11787b7f105

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:19 |
| **Last Seen** | 2026-06-11 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:19:07` | `cowrie.session.connect` |
| `2026-06-11 17:19:07` | `cowrie.client.version` |
| `2026-06-11 17:19:07` | `cowrie.client.kex` |
| `2026-06-11 17:19:07` | `cowrie.login.success` |
| `2026-06-11 17:19:08` | `cowrie.session.params` |
| `2026-06-11 17:19:08` | `cowrie.command.input` |
| `2026-06-11 17:19:08` | `cowrie.log.closed` |
| `2026-06-11 17:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f488c9243d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:19 |
| **Last Seen** | 2026-06-11 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:19:20` | `cowrie.session.connect` |
| `2026-06-11 17:19:20` | `cowrie.client.version` |
| `2026-06-11 17:19:21` | `cowrie.client.kex` |
| `2026-06-11 17:19:21` | `cowrie.login.success` |
| `2026-06-11 17:19:22` | `cowrie.session.params` |
| `2026-06-11 17:19:22` | `cowrie.command.input` |
| `2026-06-11 17:19:22` | `cowrie.log.closed` |
| `2026-06-11 17:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0555c32bfb73

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:21 |
| **Last Seen** | 2026-06-11 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:21:00` | `cowrie.session.connect` |
| `2026-06-11 17:21:00` | `cowrie.client.version` |
| `2026-06-11 17:21:01` | `cowrie.client.kex` |
| `2026-06-11 17:21:01` | `cowrie.login.success` |
| `2026-06-11 17:21:02` | `cowrie.session.params` |
| `2026-06-11 17:21:02` | `cowrie.command.input` |
| `2026-06-11 17:21:02` | `cowrie.log.closed` |
| `2026-06-11 17:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ce655fd4275

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:21 |
| **Last Seen** | 2026-06-11 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:21:56` | `cowrie.session.connect` |
| `2026-06-11 17:21:56` | `cowrie.client.version` |
| `2026-06-11 17:21:56` | `cowrie.client.kex` |
| `2026-06-11 17:21:56` | `cowrie.login.success` |
| `2026-06-11 17:21:57` | `cowrie.session.params` |
| `2026-06-11 17:21:57` | `cowrie.command.input` |
| `2026-06-11 17:21:57` | `cowrie.log.closed` |
| `2026-06-11 17:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa387541d1d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:22 |
| **Last Seen** | 2026-06-11 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:22:54` | `cowrie.session.connect` |
| `2026-06-11 17:22:54` | `cowrie.client.version` |
| `2026-06-11 17:22:54` | `cowrie.client.kex` |
| `2026-06-11 17:22:54` | `cowrie.login.success` |
| `2026-06-11 17:22:55` | `cowrie.session.params` |
| `2026-06-11 17:22:55` | `cowrie.command.input` |
| `2026-06-11 17:22:55` | `cowrie.log.closed` |
| `2026-06-11 17:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3eae6b70e6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 17:22 |
| **Last Seen** | 2026-06-11 17:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:22:55` | `cowrie.session.connect` |
| `2026-06-11 17:22:55` | `cowrie.client.version` |
| `2026-06-11 17:22:55` | `cowrie.client.kex` |
| `2026-06-11 17:22:56` | `cowrie.login.success` |
| `2026-06-11 17:22:56` | `cowrie.direct-tcpip.request` |
| `2026-06-11 17:22:56` | `cowrie.direct-tcpip.data` |
| `2026-06-11 17:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba5b3b5a795

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:24 |
| **Last Seen** | 2026-06-11 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:24:42` | `cowrie.session.connect` |
| `2026-06-11 17:24:42` | `cowrie.client.version` |
| `2026-06-11 17:24:42` | `cowrie.client.kex` |
| `2026-06-11 17:24:42` | `cowrie.login.success` |
| `2026-06-11 17:24:43` | `cowrie.session.params` |
| `2026-06-11 17:24:43` | `cowrie.command.input` |
| `2026-06-11 17:24:43` | `cowrie.log.closed` |
| `2026-06-11 17:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b54e8ccbbe0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:24 |
| **Last Seen** | 2026-06-11 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:24:54` | `cowrie.session.connect` |
| `2026-06-11 17:24:54` | `cowrie.client.version` |
| `2026-06-11 17:24:54` | `cowrie.client.kex` |
| `2026-06-11 17:24:55` | `cowrie.login.success` |
| `2026-06-11 17:24:56` | `cowrie.session.params` |
| `2026-06-11 17:24:56` | `cowrie.command.input` |
| `2026-06-11 17:24:56` | `cowrie.log.closed` |
| `2026-06-11 17:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2c074f2b0c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:26 |
| **Last Seen** | 2026-06-11 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:26:51` | `cowrie.session.connect` |
| `2026-06-11 17:26:51` | `cowrie.client.version` |
| `2026-06-11 17:26:52` | `cowrie.client.kex` |
| `2026-06-11 17:26:52` | `cowrie.login.success` |
| `2026-06-11 17:26:53` | `cowrie.session.params` |
| `2026-06-11 17:26:53` | `cowrie.command.input` |
| `2026-06-11 17:26:53` | `cowrie.log.closed` |
| `2026-06-11 17:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083b7d04bec8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:27 |
| **Last Seen** | 2026-06-11 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:27:24` | `cowrie.session.connect` |
| `2026-06-11 17:27:24` | `cowrie.client.version` |
| `2026-06-11 17:27:24` | `cowrie.client.kex` |
| `2026-06-11 17:27:24` | `cowrie.login.success` |
| `2026-06-11 17:27:25` | `cowrie.session.params` |
| `2026-06-11 17:27:25` | `cowrie.command.input` |
| `2026-06-11 17:27:25` | `cowrie.log.closed` |
| `2026-06-11 17:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aec5af2005c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:28 |
| **Last Seen** | 2026-06-11 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:28:45` | `cowrie.session.connect` |
| `2026-06-11 17:28:45` | `cowrie.client.version` |
| `2026-06-11 17:28:45` | `cowrie.client.kex` |
| `2026-06-11 17:28:46` | `cowrie.login.success` |
| `2026-06-11 17:28:46` | `cowrie.session.params` |
| `2026-06-11 17:28:46` | `cowrie.command.input` |
| `2026-06-11 17:28:46` | `cowrie.log.closed` |
| `2026-06-11 17:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81db396add3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:29 |
| **Last Seen** | 2026-06-11 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:29:59` | `cowrie.session.connect` |
| `2026-06-11 17:29:59` | `cowrie.client.version` |
| `2026-06-11 17:29:59` | `cowrie.client.kex` |
| `2026-06-11 17:30:00` | `cowrie.login.success` |
| `2026-06-11 17:30:00` | `cowrie.session.params` |
| `2026-06-11 17:30:00` | `cowrie.command.input` |
| `2026-06-11 17:30:00` | `cowrie.log.closed` |
| `2026-06-11 17:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6cb7b382e21

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:30 |
| **Last Seen** | 2026-06-11 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:30:43` | `cowrie.session.connect` |
| `2026-06-11 17:30:43` | `cowrie.client.version` |
| `2026-06-11 17:30:43` | `cowrie.client.kex` |
| `2026-06-11 17:30:43` | `cowrie.login.success` |
| `2026-06-11 17:30:44` | `cowrie.session.params` |
| `2026-06-11 17:30:44` | `cowrie.command.input` |
| `2026-06-11 17:30:44` | `cowrie.log.closed` |
| `2026-06-11 17:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67fb6a793906

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:32 |
| **Last Seen** | 2026-06-11 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:32:42` | `cowrie.session.connect` |
| `2026-06-11 17:32:42` | `cowrie.client.version` |
| `2026-06-11 17:32:42` | `cowrie.client.kex` |
| `2026-06-11 17:32:42` | `cowrie.login.success` |
| `2026-06-11 17:32:43` | `cowrie.session.params` |
| `2026-06-11 17:32:43` | `cowrie.command.input` |
| `2026-06-11 17:32:43` | `cowrie.log.closed` |
| `2026-06-11 17:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4bef4cd4f3c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:32 |
| **Last Seen** | 2026-06-11 17:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:32:42` | `cowrie.session.connect` |
| `2026-06-11 17:32:42` | `cowrie.client.version` |
| `2026-06-11 17:32:42` | `cowrie.client.kex` |
| `2026-06-11 17:32:43` | `cowrie.login.success` |
| `2026-06-11 17:32:44` | `cowrie.session.params` |
| `2026-06-11 17:32:44` | `cowrie.command.input` |
| `2026-06-11 17:32:44` | `cowrie.log.closed` |
| `2026-06-11 17:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2c19db030c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:34 |
| **Last Seen** | 2026-06-11 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:34:40` | `cowrie.session.connect` |
| `2026-06-11 17:34:40` | `cowrie.client.version` |
| `2026-06-11 17:34:40` | `cowrie.client.kex` |
| `2026-06-11 17:34:41` | `cowrie.login.success` |
| `2026-06-11 17:34:41` | `cowrie.session.params` |
| `2026-06-11 17:34:41` | `cowrie.command.input` |
| `2026-06-11 17:34:41` | `cowrie.log.closed` |
| `2026-06-11 17:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee5b922aa70

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:35 |
| **Last Seen** | 2026-06-11 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:35:22` | `cowrie.session.connect` |
| `2026-06-11 17:35:22` | `cowrie.client.version` |
| `2026-06-11 17:35:22` | `cowrie.client.kex` |
| `2026-06-11 17:35:22` | `cowrie.login.success` |
| `2026-06-11 17:35:23` | `cowrie.session.params` |
| `2026-06-11 17:35:23` | `cowrie.command.input` |
| `2026-06-11 17:35:23` | `cowrie.log.closed` |
| `2026-06-11 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669bc7d2169d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:36 |
| **Last Seen** | 2026-06-11 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:36:42` | `cowrie.session.connect` |
| `2026-06-11 17:36:42` | `cowrie.client.version` |
| `2026-06-11 17:36:42` | `cowrie.client.kex` |
| `2026-06-11 17:36:42` | `cowrie.login.success` |
| `2026-06-11 17:36:43` | `cowrie.session.params` |
| `2026-06-11 17:36:43` | `cowrie.command.input` |
| `2026-06-11 17:36:43` | `cowrie.log.closed` |
| `2026-06-11 17:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59a8f920163

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:38 |
| **Last Seen** | 2026-06-11 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:38:13` | `cowrie.session.connect` |
| `2026-06-11 17:38:13` | `cowrie.client.version` |
| `2026-06-11 17:38:13` | `cowrie.client.kex` |
| `2026-06-11 17:38:13` | `cowrie.login.success` |
| `2026-06-11 17:38:14` | `cowrie.session.params` |
| `2026-06-11 17:38:14` | `cowrie.command.input` |
| `2026-06-11 17:38:14` | `cowrie.log.closed` |
| `2026-06-11 17:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645cdf036753

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:38 |
| **Last Seen** | 2026-06-11 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:38:45` | `cowrie.session.connect` |
| `2026-06-11 17:38:45` | `cowrie.client.version` |
| `2026-06-11 17:38:45` | `cowrie.client.kex` |
| `2026-06-11 17:38:45` | `cowrie.login.success` |
| `2026-06-11 17:38:46` | `cowrie.session.params` |
| `2026-06-11 17:38:46` | `cowrie.command.input` |
| `2026-06-11 17:38:46` | `cowrie.log.closed` |
| `2026-06-11 17:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74870f789d0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:40 |
| **Last Seen** | 2026-06-11 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:40:41` | `cowrie.session.connect` |
| `2026-06-11 17:40:41` | `cowrie.client.version` |
| `2026-06-11 17:40:41` | `cowrie.client.kex` |
| `2026-06-11 17:40:41` | `cowrie.login.success` |
| `2026-06-11 17:40:42` | `cowrie.session.params` |
| `2026-06-11 17:40:42` | `cowrie.command.input` |
| `2026-06-11 17:40:42` | `cowrie.log.closed` |
| `2026-06-11 17:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b51dacd87e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:40 |
| **Last Seen** | 2026-06-11 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:40:54` | `cowrie.session.connect` |
| `2026-06-11 17:40:54` | `cowrie.client.version` |
| `2026-06-11 17:40:54` | `cowrie.client.kex` |
| `2026-06-11 17:40:54` | `cowrie.login.success` |
| `2026-06-11 17:40:55` | `cowrie.session.params` |
| `2026-06-11 17:40:55` | `cowrie.command.input` |
| `2026-06-11 17:40:55` | `cowrie.log.closed` |
| `2026-06-11 17:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad169c95d81

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:42 |
| **Last Seen** | 2026-06-11 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:42:39` | `cowrie.session.connect` |
| `2026-06-11 17:42:39` | `cowrie.client.version` |
| `2026-06-11 17:42:39` | `cowrie.client.kex` |
| `2026-06-11 17:42:39` | `cowrie.login.success` |
| `2026-06-11 17:42:40` | `cowrie.session.params` |
| `2026-06-11 17:42:40` | `cowrie.command.input` |
| `2026-06-11 17:42:40` | `cowrie.log.closed` |
| `2026-06-11 17:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77161e388557

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:43 |
| **Last Seen** | 2026-06-11 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:43:33` | `cowrie.session.connect` |
| `2026-06-11 17:43:33` | `cowrie.client.version` |
| `2026-06-11 17:43:33` | `cowrie.client.kex` |
| `2026-06-11 17:43:33` | `cowrie.login.success` |
| `2026-06-11 17:43:34` | `cowrie.session.params` |
| `2026-06-11 17:43:34` | `cowrie.command.input` |
| `2026-06-11 17:43:34` | `cowrie.log.closed` |
| `2026-06-11 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac053de6b9f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:44 |
| **Last Seen** | 2026-06-11 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:44:37` | `cowrie.session.connect` |
| `2026-06-11 17:44:37` | `cowrie.client.version` |
| `2026-06-11 17:44:37` | `cowrie.client.kex` |
| `2026-06-11 17:44:37` | `cowrie.login.success` |
| `2026-06-11 17:44:38` | `cowrie.session.params` |
| `2026-06-11 17:44:38` | `cowrie.command.input` |
| `2026-06-11 17:44:38` | `cowrie.log.closed` |
| `2026-06-11 17:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674f236e1fa8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:46 |
| **Last Seen** | 2026-06-11 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:46:13` | `cowrie.session.connect` |
| `2026-06-11 17:46:13` | `cowrie.client.version` |
| `2026-06-11 17:46:13` | `cowrie.client.kex` |
| `2026-06-11 17:46:13` | `cowrie.login.success` |
| `2026-06-11 17:46:14` | `cowrie.session.params` |
| `2026-06-11 17:46:14` | `cowrie.command.input` |
| `2026-06-11 17:46:14` | `cowrie.log.closed` |
| `2026-06-11 17:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7075c6a4c715

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:46 |
| **Last Seen** | 2026-06-11 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:46:33` | `cowrie.session.connect` |
| `2026-06-11 17:46:33` | `cowrie.client.version` |
| `2026-06-11 17:46:33` | `cowrie.client.kex` |
| `2026-06-11 17:46:34` | `cowrie.login.success` |
| `2026-06-11 17:46:34` | `cowrie.session.params` |
| `2026-06-11 17:46:34` | `cowrie.command.input` |
| `2026-06-11 17:46:35` | `cowrie.log.closed` |
| `2026-06-11 17:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3fd708ace6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:48 |
| **Last Seen** | 2026-06-11 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:48:30` | `cowrie.session.connect` |
| `2026-06-11 17:48:30` | `cowrie.client.version` |
| `2026-06-11 17:48:30` | `cowrie.client.kex` |
| `2026-06-11 17:48:31` | `cowrie.login.success` |
| `2026-06-11 17:48:31` | `cowrie.session.params` |
| `2026-06-11 17:48:31` | `cowrie.command.input` |
| `2026-06-11 17:48:32` | `cowrie.log.closed` |
| `2026-06-11 17:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5092c36634e1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:48 |
| **Last Seen** | 2026-06-11 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:48:51` | `cowrie.session.connect` |
| `2026-06-11 17:48:51` | `cowrie.client.version` |
| `2026-06-11 17:48:51` | `cowrie.client.kex` |
| `2026-06-11 17:48:51` | `cowrie.login.success` |
| `2026-06-11 17:48:52` | `cowrie.session.params` |
| `2026-06-11 17:48:52` | `cowrie.command.input` |
| `2026-06-11 17:48:52` | `cowrie.log.closed` |
| `2026-06-11 17:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c9b8e17408

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:50 |
| **Last Seen** | 2026-06-11 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:50:34` | `cowrie.session.connect` |
| `2026-06-11 17:50:34` | `cowrie.client.version` |
| `2026-06-11 17:50:34` | `cowrie.client.kex` |
| `2026-06-11 17:50:34` | `cowrie.login.success` |
| `2026-06-11 17:50:35` | `cowrie.session.params` |
| `2026-06-11 17:50:35` | `cowrie.command.input` |
| `2026-06-11 17:50:35` | `cowrie.log.closed` |
| `2026-06-11 17:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8b657e8b60

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:51 |
| **Last Seen** | 2026-06-11 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:51:40` | `cowrie.session.connect` |
| `2026-06-11 17:51:40` | `cowrie.client.version` |
| `2026-06-11 17:51:40` | `cowrie.client.kex` |
| `2026-06-11 17:51:41` | `cowrie.login.success` |
| `2026-06-11 17:51:42` | `cowrie.session.params` |
| `2026-06-11 17:51:42` | `cowrie.command.input` |
| `2026-06-11 17:51:42` | `cowrie.log.closed` |
| `2026-06-11 17:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b27600b5bf4a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:52 |
| **Last Seen** | 2026-06-11 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:52:32` | `cowrie.session.connect` |
| `2026-06-11 17:52:33` | `cowrie.client.version` |
| `2026-06-11 17:52:33` | `cowrie.client.kex` |
| `2026-06-11 17:52:33` | `cowrie.login.success` |
| `2026-06-11 17:52:34` | `cowrie.session.params` |
| `2026-06-11 17:52:34` | `cowrie.command.input` |
| `2026-06-11 17:52:34` | `cowrie.log.closed` |
| `2026-06-11 17:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc5db58d9e0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:54 |
| **Last Seen** | 2026-06-11 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:54:22` | `cowrie.session.connect` |
| `2026-06-11 17:54:22` | `cowrie.client.version` |
| `2026-06-11 17:54:22` | `cowrie.client.kex` |
| `2026-06-11 17:54:22` | `cowrie.login.success` |
| `2026-06-11 17:54:23` | `cowrie.session.params` |
| `2026-06-11 17:54:23` | `cowrie.command.input` |
| `2026-06-11 17:54:23` | `cowrie.log.closed` |
| `2026-06-11 17:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84ddb3b0657

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:54 |
| **Last Seen** | 2026-06-11 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:54:30` | `cowrie.session.connect` |
| `2026-06-11 17:54:30` | `cowrie.client.version` |
| `2026-06-11 17:54:30` | `cowrie.client.kex` |
| `2026-06-11 17:54:31` | `cowrie.login.success` |
| `2026-06-11 17:54:31` | `cowrie.session.params` |
| `2026-06-11 17:54:31` | `cowrie.command.input` |
| `2026-06-11 17:54:32` | `cowrie.log.closed` |
| `2026-06-11 17:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22f5ffdecd2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:56 |
| **Last Seen** | 2026-06-11 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:56:32` | `cowrie.session.connect` |
| `2026-06-11 17:56:32` | `cowrie.client.version` |
| `2026-06-11 17:56:32` | `cowrie.client.kex` |
| `2026-06-11 17:56:32` | `cowrie.login.success` |
| `2026-06-11 17:56:33` | `cowrie.session.params` |
| `2026-06-11 17:56:33` | `cowrie.command.input` |
| `2026-06-11 17:56:33` | `cowrie.log.closed` |
| `2026-06-11 17:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf4a11b9da9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:57 |
| **Last Seen** | 2026-06-11 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:57:07` | `cowrie.session.connect` |
| `2026-06-11 17:57:07` | `cowrie.client.version` |
| `2026-06-11 17:57:07` | `cowrie.client.kex` |
| `2026-06-11 17:57:08` | `cowrie.login.success` |
| `2026-06-11 17:57:08` | `cowrie.session.params` |
| `2026-06-11 17:57:08` | `cowrie.command.input` |
| `2026-06-11 17:57:09` | `cowrie.log.closed` |
| `2026-06-11 17:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84fc13b3c5c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:58 |
| **Last Seen** | 2026-06-11 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:58:28` | `cowrie.session.connect` |
| `2026-06-11 17:58:28` | `cowrie.client.version` |
| `2026-06-11 17:58:28` | `cowrie.client.kex` |
| `2026-06-11 17:58:28` | `cowrie.login.success` |
| `2026-06-11 17:58:29` | `cowrie.session.params` |
| `2026-06-11 17:58:29` | `cowrie.command.input` |
| `2026-06-11 17:58:29` | `cowrie.log.closed` |
| `2026-06-11 17:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e18bcca5a0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 17:59 |
| **Last Seen** | 2026-06-11 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:59:45` | `cowrie.session.connect` |
| `2026-06-11 17:59:45` | `cowrie.client.version` |
| `2026-06-11 17:59:45` | `cowrie.client.kex` |
| `2026-06-11 17:59:45` | `cowrie.login.success` |
| `2026-06-11 17:59:46` | `cowrie.session.params` |
| `2026-06-11 17:59:46` | `cowrie.command.input` |
| `2026-06-11 17:59:46` | `cowrie.log.closed` |
| `2026-06-11 17:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d13a112d5b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:00 |
| **Last Seen** | 2026-06-11 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:00:22` | `cowrie.session.connect` |
| `2026-06-11 18:00:22` | `cowrie.client.version` |
| `2026-06-11 18:00:22` | `cowrie.client.kex` |
| `2026-06-11 18:00:22` | `cowrie.login.success` |
| `2026-06-11 18:00:23` | `cowrie.session.params` |
| `2026-06-11 18:00:23` | `cowrie.command.input` |
| `2026-06-11 18:00:23` | `cowrie.log.closed` |
| `2026-06-11 18:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e36daaa779

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:02 |
| **Last Seen** | 2026-06-11 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:02:21` | `cowrie.session.connect` |
| `2026-06-11 18:02:21` | `cowrie.client.version` |
| `2026-06-11 18:02:21` | `cowrie.client.kex` |
| `2026-06-11 18:02:21` | `cowrie.login.success` |
| `2026-06-11 18:02:22` | `cowrie.session.params` |
| `2026-06-11 18:02:22` | `cowrie.command.input` |
| `2026-06-11 18:02:22` | `cowrie.log.closed` |
| `2026-06-11 18:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47fb6829c0ac

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:02 |
| **Last Seen** | 2026-06-11 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:02:27` | `cowrie.session.connect` |
| `2026-06-11 18:02:27` | `cowrie.client.version` |
| `2026-06-11 18:02:27` | `cowrie.client.kex` |
| `2026-06-11 18:02:27` | `cowrie.login.success` |
| `2026-06-11 18:02:28` | `cowrie.session.params` |
| `2026-06-11 18:02:28` | `cowrie.command.input` |
| `2026-06-11 18:02:28` | `cowrie.log.closed` |
| `2026-06-11 18:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a3c88dda6d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:04 |
| **Last Seen** | 2026-06-11 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:04:22` | `cowrie.session.connect` |
| `2026-06-11 18:04:22` | `cowrie.client.version` |
| `2026-06-11 18:04:22` | `cowrie.client.kex` |
| `2026-06-11 18:04:23` | `cowrie.login.success` |
| `2026-06-11 18:04:23` | `cowrie.session.params` |
| `2026-06-11 18:04:23` | `cowrie.command.input` |
| `2026-06-11 18:04:23` | `cowrie.log.closed` |
| `2026-06-11 18:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951e5a5193c7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:05 |
| **Last Seen** | 2026-06-11 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:05:12` | `cowrie.session.connect` |
| `2026-06-11 18:05:12` | `cowrie.client.version` |
| `2026-06-11 18:05:12` | `cowrie.client.kex` |
| `2026-06-11 18:05:12` | `cowrie.login.success` |
| `2026-06-11 18:05:13` | `cowrie.session.params` |
| `2026-06-11 18:05:13` | `cowrie.command.input` |
| `2026-06-11 18:05:13` | `cowrie.log.closed` |
| `2026-06-11 18:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53be6a385360

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:06 |
| **Last Seen** | 2026-06-11 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:06:19` | `cowrie.session.connect` |
| `2026-06-11 18:06:19` | `cowrie.client.version` |
| `2026-06-11 18:06:19` | `cowrie.client.kex` |
| `2026-06-11 18:06:19` | `cowrie.login.success` |
| `2026-06-11 18:06:20` | `cowrie.session.params` |
| `2026-06-11 18:06:20` | `cowrie.command.input` |
| `2026-06-11 18:06:20` | `cowrie.log.closed` |
| `2026-06-11 18:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa38be063aa0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:07 |
| **Last Seen** | 2026-06-11 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:07:54` | `cowrie.session.connect` |
| `2026-06-11 18:07:54` | `cowrie.client.version` |
| `2026-06-11 18:07:54` | `cowrie.client.kex` |
| `2026-06-11 18:07:54` | `cowrie.login.success` |
| `2026-06-11 18:07:55` | `cowrie.session.params` |
| `2026-06-11 18:07:55` | `cowrie.command.input` |
| `2026-06-11 18:07:55` | `cowrie.log.closed` |
| `2026-06-11 18:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e818b7c86dc3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:08 |
| **Last Seen** | 2026-06-11 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:08:20` | `cowrie.session.connect` |
| `2026-06-11 18:08:20` | `cowrie.client.version` |
| `2026-06-11 18:08:20` | `cowrie.client.kex` |
| `2026-06-11 18:08:21` | `cowrie.login.success` |
| `2026-06-11 18:08:22` | `cowrie.session.params` |
| `2026-06-11 18:08:22` | `cowrie.command.input` |
| `2026-06-11 18:08:22` | `cowrie.log.closed` |
| `2026-06-11 18:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c31a431eb53

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:10 |
| **Last Seen** | 2026-06-11 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:10:25` | `cowrie.session.connect` |
| `2026-06-11 18:10:25` | `cowrie.client.version` |
| `2026-06-11 18:10:25` | `cowrie.client.kex` |
| `2026-06-11 18:10:26` | `cowrie.login.success` |
| `2026-06-11 18:10:27` | `cowrie.session.params` |
| `2026-06-11 18:10:27` | `cowrie.command.input` |
| `2026-06-11 18:10:27` | `cowrie.log.closed` |
| `2026-06-11 18:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac50e32195ed

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:10 |
| **Last Seen** | 2026-06-11 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:10:40` | `cowrie.session.connect` |
| `2026-06-11 18:10:40` | `cowrie.client.version` |
| `2026-06-11 18:10:41` | `cowrie.client.kex` |
| `2026-06-11 18:10:41` | `cowrie.login.success` |
| `2026-06-11 18:10:42` | `cowrie.session.params` |
| `2026-06-11 18:10:42` | `cowrie.command.input` |
| `2026-06-11 18:10:42` | `cowrie.log.closed` |
| `2026-06-11 18:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9e97f4ed24

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:12 |
| **Last Seen** | 2026-06-11 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:12:21` | `cowrie.session.connect` |
| `2026-06-11 18:12:21` | `cowrie.client.version` |
| `2026-06-11 18:12:21` | `cowrie.client.kex` |
| `2026-06-11 18:12:22` | `cowrie.login.success` |
| `2026-06-11 18:12:22` | `cowrie.session.params` |
| `2026-06-11 18:12:22` | `cowrie.command.input` |
| `2026-06-11 18:12:22` | `cowrie.log.closed` |
| `2026-06-11 18:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01d6ad42aa1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:13 |
| **Last Seen** | 2026-06-11 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:13:18` | `cowrie.session.connect` |
| `2026-06-11 18:13:18` | `cowrie.client.version` |
| `2026-06-11 18:13:18` | `cowrie.client.kex` |
| `2026-06-11 18:13:18` | `cowrie.login.success` |
| `2026-06-11 18:13:19` | `cowrie.session.params` |
| `2026-06-11 18:13:19` | `cowrie.command.input` |
| `2026-06-11 18:13:19` | `cowrie.log.closed` |
| `2026-06-11 18:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ce493a0b41

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 18:14 |
| **Last Seen** | 2026-06-11 18:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:14:09` | `cowrie.session.connect` |
| `2026-06-11 18:14:09` | `cowrie.client.version` |
| `2026-06-11 18:14:09` | `cowrie.client.kex` |
| `2026-06-11 18:14:09` | `cowrie.login.success` |
| `2026-06-11 18:14:09` | `cowrie.direct-tcpip.request` |
| `2026-06-11 18:14:09` | `cowrie.direct-tcpip.data` |
| `2026-06-11 18:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93bc26627175

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:14 |
| **Last Seen** | 2026-06-11 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:14:18` | `cowrie.session.connect` |
| `2026-06-11 18:14:18` | `cowrie.client.version` |
| `2026-06-11 18:14:18` | `cowrie.client.kex` |
| `2026-06-11 18:14:18` | `cowrie.login.success` |
| `2026-06-11 18:14:19` | `cowrie.session.params` |
| `2026-06-11 18:14:19` | `cowrie.command.input` |
| `2026-06-11 18:14:19` | `cowrie.log.closed` |
| `2026-06-11 18:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d750546912

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:16 |
| **Last Seen** | 2026-06-11 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:16:04` | `cowrie.session.connect` |
| `2026-06-11 18:16:04` | `cowrie.client.version` |
| `2026-06-11 18:16:04` | `cowrie.client.kex` |
| `2026-06-11 18:16:04` | `cowrie.login.success` |
| `2026-06-11 18:16:05` | `cowrie.session.params` |
| `2026-06-11 18:16:05` | `cowrie.command.input` |
| `2026-06-11 18:16:05` | `cowrie.log.closed` |
| `2026-06-11 18:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdee406e7e7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:16 |
| **Last Seen** | 2026-06-11 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:16:20` | `cowrie.session.connect` |
| `2026-06-11 18:16:20` | `cowrie.client.version` |
| `2026-06-11 18:16:20` | `cowrie.client.kex` |
| `2026-06-11 18:16:20` | `cowrie.login.success` |
| `2026-06-11 18:16:21` | `cowrie.session.params` |
| `2026-06-11 18:16:21` | `cowrie.command.input` |
| `2026-06-11 18:16:21` | `cowrie.log.closed` |
| `2026-06-11 18:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63984f22eb42

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:18 |
| **Last Seen** | 2026-06-11 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:18:17` | `cowrie.session.connect` |
| `2026-06-11 18:18:17` | `cowrie.client.version` |
| `2026-06-11 18:18:17` | `cowrie.client.kex` |
| `2026-06-11 18:18:17` | `cowrie.login.success` |
| `2026-06-11 18:18:18` | `cowrie.session.params` |
| `2026-06-11 18:18:18` | `cowrie.command.input` |
| `2026-06-11 18:18:18` | `cowrie.log.closed` |
| `2026-06-11 18:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a37d61235b1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:18 |
| **Last Seen** | 2026-06-11 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:18:42` | `cowrie.session.connect` |
| `2026-06-11 18:18:42` | `cowrie.client.version` |
| `2026-06-11 18:18:42` | `cowrie.client.kex` |
| `2026-06-11 18:18:42` | `cowrie.login.success` |
| `2026-06-11 18:18:43` | `cowrie.session.params` |
| `2026-06-11 18:18:43` | `cowrie.command.input` |
| `2026-06-11 18:18:43` | `cowrie.log.closed` |
| `2026-06-11 18:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf131db222e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:20 |
| **Last Seen** | 2026-06-11 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:20:12` | `cowrie.session.connect` |
| `2026-06-11 18:20:12` | `cowrie.client.version` |
| `2026-06-11 18:20:12` | `cowrie.client.kex` |
| `2026-06-11 18:20:12` | `cowrie.login.success` |
| `2026-06-11 18:20:13` | `cowrie.session.params` |
| `2026-06-11 18:20:13` | `cowrie.command.input` |
| `2026-06-11 18:20:13` | `cowrie.log.closed` |
| `2026-06-11 18:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84cf49817df4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:21 |
| **Last Seen** | 2026-06-11 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:21:28` | `cowrie.session.connect` |
| `2026-06-11 18:21:28` | `cowrie.client.version` |
| `2026-06-11 18:21:28` | `cowrie.client.kex` |
| `2026-06-11 18:21:28` | `cowrie.login.success` |
| `2026-06-11 18:21:29` | `cowrie.session.params` |
| `2026-06-11 18:21:29` | `cowrie.command.input` |
| `2026-06-11 18:21:29` | `cowrie.log.closed` |
| `2026-06-11 18:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8329e2370955

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:24 |
| **Last Seen** | 2026-06-11 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:24:14` | `cowrie.session.connect` |
| `2026-06-11 18:24:14` | `cowrie.client.version` |
| `2026-06-11 18:24:14` | `cowrie.client.kex` |
| `2026-06-11 18:24:15` | `cowrie.login.success` |
| `2026-06-11 18:24:15` | `cowrie.session.params` |
| `2026-06-11 18:24:15` | `cowrie.command.input` |
| `2026-06-11 18:24:15` | `cowrie.log.closed` |
| `2026-06-11 18:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640da398019a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:26 |
| **Last Seen** | 2026-06-11 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:26:57` | `cowrie.session.connect` |
| `2026-06-11 18:26:57` | `cowrie.client.version` |
| `2026-06-11 18:26:57` | `cowrie.client.kex` |
| `2026-06-11 18:26:57` | `cowrie.login.success` |
| `2026-06-11 18:26:58` | `cowrie.session.params` |
| `2026-06-11 18:26:58` | `cowrie.command.input` |
| `2026-06-11 18:26:58` | `cowrie.log.closed` |
| `2026-06-11 18:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48214efc5855

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:29 |
| **Last Seen** | 2026-06-11 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:29:48` | `cowrie.session.connect` |
| `2026-06-11 18:29:48` | `cowrie.client.version` |
| `2026-06-11 18:29:48` | `cowrie.client.kex` |
| `2026-06-11 18:29:49` | `cowrie.login.success` |
| `2026-06-11 18:29:50` | `cowrie.session.params` |
| `2026-06-11 18:29:50` | `cowrie.command.input` |
| `2026-06-11 18:29:50` | `cowrie.log.closed` |
| `2026-06-11 18:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef3f8371e04f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:32 |
| **Last Seen** | 2026-06-11 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:32:30` | `cowrie.session.connect` |
| `2026-06-11 18:32:30` | `cowrie.client.version` |
| `2026-06-11 18:32:30` | `cowrie.client.kex` |
| `2026-06-11 18:32:30` | `cowrie.login.success` |
| `2026-06-11 18:32:31` | `cowrie.session.params` |
| `2026-06-11 18:32:31` | `cowrie.command.input` |
| `2026-06-11 18:32:31` | `cowrie.log.closed` |
| `2026-06-11 18:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4db9cae65fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:35 |
| **Last Seen** | 2026-06-11 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:35:26` | `cowrie.session.connect` |
| `2026-06-11 18:35:26` | `cowrie.client.version` |
| `2026-06-11 18:35:26` | `cowrie.client.kex` |
| `2026-06-11 18:35:26` | `cowrie.login.success` |
| `2026-06-11 18:35:27` | `cowrie.session.params` |
| `2026-06-11 18:35:27` | `cowrie.command.input` |
| `2026-06-11 18:35:27` | `cowrie.log.closed` |
| `2026-06-11 18:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5de8dc1b2a3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 18:38 |
| **Last Seen** | 2026-06-11 18:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:38:08` | `cowrie.session.connect` |
| `2026-06-11 18:38:08` | `cowrie.client.version` |
| `2026-06-11 18:38:09` | `cowrie.client.kex` |
| `2026-06-11 18:38:09` | `cowrie.login.success` |
| `2026-06-11 18:38:09` | `cowrie.direct-tcpip.request` |
| `2026-06-11 18:38:09` | `cowrie.direct-tcpip.data` |
| `2026-06-11 18:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5ec3304c3c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:38 |
| **Last Seen** | 2026-06-11 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:38:11` | `cowrie.session.connect` |
| `2026-06-11 18:38:11` | `cowrie.client.version` |
| `2026-06-11 18:38:11` | `cowrie.client.kex` |
| `2026-06-11 18:38:11` | `cowrie.login.success` |
| `2026-06-11 18:38:12` | `cowrie.session.params` |
| `2026-06-11 18:38:12` | `cowrie.command.input` |
| `2026-06-11 18:38:12` | `cowrie.log.closed` |
| `2026-06-11 18:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61ec7377e98

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:41 |
| **Last Seen** | 2026-06-11 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:41:07` | `cowrie.session.connect` |
| `2026-06-11 18:41:07` | `cowrie.client.version` |
| `2026-06-11 18:41:07` | `cowrie.client.kex` |
| `2026-06-11 18:41:07` | `cowrie.login.success` |
| `2026-06-11 18:41:08` | `cowrie.session.params` |
| `2026-06-11 18:41:08` | `cowrie.command.input` |
| `2026-06-11 18:41:08` | `cowrie.log.closed` |
| `2026-06-11 18:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11752cb82858

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:43 |
| **Last Seen** | 2026-06-11 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:43:51` | `cowrie.session.connect` |
| `2026-06-11 18:43:51` | `cowrie.client.version` |
| `2026-06-11 18:43:51` | `cowrie.client.kex` |
| `2026-06-11 18:43:51` | `cowrie.login.success` |
| `2026-06-11 18:43:52` | `cowrie.session.params` |
| `2026-06-11 18:43:52` | `cowrie.command.input` |
| `2026-06-11 18:43:52` | `cowrie.log.closed` |
| `2026-06-11 18:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3fd53f4eac

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:46 |
| **Last Seen** | 2026-06-11 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:46:35` | `cowrie.session.connect` |
| `2026-06-11 18:46:35` | `cowrie.client.version` |
| `2026-06-11 18:46:35` | `cowrie.client.kex` |
| `2026-06-11 18:46:35` | `cowrie.login.success` |
| `2026-06-11 18:46:36` | `cowrie.session.params` |
| `2026-06-11 18:46:36` | `cowrie.command.input` |
| `2026-06-11 18:46:36` | `cowrie.log.closed` |
| `2026-06-11 18:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a82c94e9e7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:49 |
| **Last Seen** | 2026-06-11 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:49:22` | `cowrie.session.connect` |
| `2026-06-11 18:49:22` | `cowrie.client.version` |
| `2026-06-11 18:49:22` | `cowrie.client.kex` |
| `2026-06-11 18:49:23` | `cowrie.login.success` |
| `2026-06-11 18:49:23` | `cowrie.session.params` |
| `2026-06-11 18:49:23` | `cowrie.command.input` |
| `2026-06-11 18:49:24` | `cowrie.log.closed` |
| `2026-06-11 18:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418c1c845812

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:52 |
| **Last Seen** | 2026-06-11 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:52:08` | `cowrie.session.connect` |
| `2026-06-11 18:52:08` | `cowrie.client.version` |
| `2026-06-11 18:52:08` | `cowrie.client.kex` |
| `2026-06-11 18:52:08` | `cowrie.login.success` |
| `2026-06-11 18:52:09` | `cowrie.session.params` |
| `2026-06-11 18:52:09` | `cowrie.command.input` |
| `2026-06-11 18:52:09` | `cowrie.log.closed` |
| `2026-06-11 18:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **37** | 2026-06-11 15:29 | 2026-06-11 18:54 | 23m | 0 | `T1592` | 🟠 MEDIUM |
| `5.101.64[.]7` | **20** | 2026-06-11 18:48 | 2026-06-11 18:51 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `8.152.209[.]0` | **3** | 2026-06-11 16:40 | 2026-06-11 16:43 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-11 16:38 | 2026-06-11 18:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | **2** | 2026-06-11 16:19 | 2026-06-11 16:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | **2** | 2026-06-11 17:13 | 2026-06-11 17:42 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]162` | **2** | 2026-06-11 18:27 | 2026-06-11 18:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]171` | **2** | 2026-06-11 16:05 | 2026-06-11 16:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.185.27[.]51` | 1 | 2026-06-11 18:48 | 2026-06-11 18:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `112.5.89[.]227` | 1 | 2026-06-11 16:46 | 2026-06-11 16:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.236.49[.]131` | 1 | 2026-06-11 16:18 | 2026-06-11 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.163.98[.]34` | 1 | 2026-06-11 16:28 | 2026-06-11 16:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]38` | 1 | 2026-06-11 18:43 | 2026-06-11 18:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `220.134.33[.]198` | 1 | 2026-06-11 17:57 | 2026-06-11 17:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `24.234.202[.]117` | 1 | 2026-06-11 16:51 | 2026-06-11 16:51 | 38s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-06-11 16:07 | 2026-06-11 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]183` | 1 | 2026-06-11 16:30 | 2026-06-11 16:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-06-11 15:33 | 2026-06-11 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.218.254[.]239` | 1 | 2026-06-11 15:45 | 2026-06-11 15:45 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `220.134.33[.]198` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 1 |
| `5.101.64[.]7` | RU | public vlans of DC | **100** ⚠️ | 5 |
| `112.5.89[.]227` | CN | China Mobile Communications Corporation | **100** ⚠️ | 6 |
| `195.178.110[.]204` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `185.38.148[.]2` | GB | Hydra Communications Ltd | **100** ⚠️ | 50 |
| `24.234.202[.]117` | US | Cox Communications Inc. | **100** ⚠️ | 50 |
| `164.163.98[.]34` | BR | INFO TELECOM INTERNET LTDA | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 148 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 130 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 233 cases |
| Tool 34  | Credential Extractor        | ✅ 130 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (10.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 128 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 70 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `Aegispub/thir-ha · Oracle Cloud HA_  
_Report time: 2026-06-11T20:30:35Z_

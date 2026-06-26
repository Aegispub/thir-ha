# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-26 |
| **Generated At** | 2026-06-26T23:11:12Z |
| **Shift Time** | 23:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **352** |
| Confirmed Threats | **345** |
| False Positives Filtered | **7** (2.0%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **9** |
| High Severity Cases | **181** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **171** |
| Malware Samples Analyzed | **5** HIGH · **42** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **189** |
| Unique Credential Pairs | **177** |
| Unique Usernames | **81** |
| Unique Passwords | **160** |
| Successful Auth Pairs | **180** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 85 |
| `admin` | 14 |
| `ubuntu` | 9 |
| `jinL` | 2 |
| `nginx` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `admin` | 8 |
| `1234` | 4 |
| `` | 4 |
| `jinL` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 7 |
| `admin` | `` | 4 |
| `jinL` | `jinL` | 2 |
| `root` | `123456` | 2 |
| `root` | `smo@@kkklss` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `erpeng` | `erpeng` | `209.99.185.59` | 2026-06-26T20:55:32 |
| `root` | `qaz12wsx` | `209.99.185.59` | 2026-06-26T20:56:24 |
| `jinL` | `jinL` | `45.198.224.92` | 2026-06-26T20:56:31 |
| `admin` | `123wsx` | `209.99.185.59` | 2026-06-26T20:57:15 |
| `root` | `P@ssword123$` | `209.99.185.59` | 2026-06-26T20:58:08 |
| `wwwlogs` | `wwwlogs` | `209.99.185.59` | 2026-06-26T20:59:00 |
| `testuser` | `test123` | `45.198.224.120` | 2026-06-26T20:59:50 |
| `root` | `admin@9000` | `209.99.185.59` | 2026-06-26T20:59:53 |
| `new` | `new` | `209.99.185.59` | 2026-06-26T21:00:58 |
| `csgo` | `csgocsgocsgo` | `209.99.185.59` | 2026-06-26T21:01:57 |
| `root` | `1234567891` | `209.99.185.59` | 2026-06-26T21:02:49 |
| `root` | `pass123` | `45.205.1.42` | 2026-06-26T21:02:52 |
| `root` | `ubuntu123456` | `209.99.185.59` | 2026-06-26T21:03:41 |
| `ubuntu` | `abc123456` | `209.99.185.59` | 2026-06-26T21:04:34 |
| `ubuntu` | `deploy` | `209.99.185.59` | 2026-06-26T21:05:28 |
| `gyq` | `gyq` | `209.99.185.59` | 2026-06-26T21:06:21 |
| `wpyan` | `qwer1234` | `209.99.185.59` | 2026-06-26T21:07:14 |
| `suliyilei1` | `suliyilei1` | `209.99.185.59` | 2026-06-26T21:08:07 |
| `zxc` | `123123123456` | `209.99.185.59` | 2026-06-26T21:09:00 |
| `root` | `qaz_2wsx` | `209.99.185.59` | 2026-06-26T21:09:53 |
| `root` | `P@ssword1234567` | `209.99.185.59` | 2026-06-26T21:10:47 |
| `root` | `qpwoeiru` | `45.198.224.120` | 2026-06-26T21:11:08 |
| `sixu-srt` | `245` | `209.99.185.59` | 2026-06-26T21:11:42 |
| `applmgr` | `applmgr@123` | `209.99.185.59` | 2026-06-26T21:12:38 |
| `admin` | `admin` | `47.253.5.130` | 2026-06-26T21:12:50 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-26T21:12:51 |
| `vision` | `1234` | `209.99.185.59` | 2026-06-26T21:13:32 |
| `admin` | `admin` | `223.84.239.151` | 2026-06-26T21:14:09 |
| `root` | `mjunhybgtvfrcdexswzaq` | `209.99.185.59` | 2026-06-26T21:14:27 |
| `sysmon` | `sysmon` | `209.99.185.59` | 2026-06-26T21:15:20 |
| `root` | `123qwerty` | `195.178.110.217` | 2026-06-26T21:15:30 |
| `root` | `sitonholy` | `209.99.185.59` | 2026-06-26T21:16:15 |
| `lcd` | `lcd` | `209.99.185.59` | 2026-06-26T21:17:10 |
| `root` | `21` | `195.178.110.217` | 2026-06-26T21:17:35 |
| `root` | `samsung` | `45.205.1.42` | 2026-06-26T21:18:03 |
| `nginx` | `12345` | `209.99.185.59` | 2026-06-26T21:18:06 |
| `root` | `"4f9b14bbb11b0c9c0220e62198"` | `209.99.185.59` | 2026-06-26T21:19:02 |
| `root` | `321` | `195.178.110.217` | 2026-06-26T21:19:48 |
| `root` | `centos` | `209.99.185.59` | 2026-06-26T21:19:58 |
| `student` | `student123` | `209.99.185.59` | 2026-06-26T21:20:53 |
| `oeh` | `123456` | `209.99.185.59` | 2026-06-26T21:21:48 |
| `root` | `1q2w3e` | `45.198.224.120` | 2026-06-26T21:22:08 |
| `root` | `4321` | `195.178.110.217` | 2026-06-26T21:22:29 |
| `hanul` | `korea2011` | `209.99.185.59` | 2026-06-26T21:22:44 |
| `xuyong` | `,,wait05642881299` | `209.99.185.59` | 2026-06-26T21:23:41 |
| `redis` | `redis123#` | `209.99.185.59` | 2026-06-26T21:24:39 |
| `www` | `123456` | `209.99.185.59` | 2026-06-26T21:25:37 |
| `test1` | `12345678` | `209.99.185.59` | 2026-06-26T21:26:33 |
| `root` | `sommer` | `209.99.185.59` | 2026-06-26T21:27:29 |
| `root` | `qwert0123` | `209.99.185.59` | 2026-06-26T21:28:23 |
| `yangyu` | `yangyu2016` | `209.99.185.59` | 2026-06-26T21:29:16 |
| `root` | `qwas12` | `209.99.185.59` | 2026-06-26T21:30:12 |
| `root` | `banned` | `209.99.185.59` | 2026-06-26T21:31:07 |
| `root` | `Wxyd@20210106` | `209.99.185.59` | 2026-06-26T21:32:01 |
| `yl` | `yl` | `209.99.185.59` | 2026-06-26T21:32:55 |
| `root` | `gwerty` | `45.198.224.120` | 2026-06-26T21:33:32 |
| `root` | `Qwe1!2345` | `45.205.1.42` | 2026-06-26T21:33:34 |
| `root` | `rootteam` | `209.99.185.59` | 2026-06-26T21:33:50 |
| `root` | `leibo` | `209.99.185.59` | 2026-06-26T21:34:45 |
| `jinL` | `jinL` | `10.0.0.73` | 2026-06-26T21:35:10 |
| `ceshi3` | `ceshi31` | `209.99.185.59` | 2026-06-26T21:35:40 |
| `ubuntu` | `UBUNTU` | `209.99.185.59` | 2026-06-26T21:36:37 |
| `ftpuser` | `changeme` | `209.99.185.59` | 2026-06-26T21:37:35 |
| `mailman` | `mailman` | `209.99.185.59` | 2026-06-26T21:38:32 |
| `liangwenzhe` | `liangwenzhe` | `209.99.185.59` | 2026-06-26T21:39:29 |
| `ubuntu` | `q1w2e3` | `209.99.185.59` | 2026-06-26T21:40:25 |
| `root` | `qazwe123` | `209.99.185.59` | 2026-06-26T21:41:20 |
| `wroot` | `wroot123` | `209.99.185.59` | 2026-06-26T21:42:17 |
| `dis` | `1` | `209.99.185.59` | 2026-06-26T21:43:15 |
| `shaoxin` | `shaoxin` | `209.99.185.59` | 2026-06-26T21:44:14 |
| `ubuntu` | `12341234` | `45.198.224.120` | 2026-06-26T21:45:09 |
| `fax` | `password` | `209.99.185.59` | 2026-06-26T21:45:14 |
| `DJ` | `DJ` | `209.99.185.59` | 2026-06-26T21:46:12 |
| `buaa` | `buaa` | `209.99.185.59` | 2026-06-26T21:47:11 |
| `student3` | `123456` | `209.99.185.59` | 2026-06-26T21:48:12 |
| `root` | `qwerasdf` | `45.205.1.42` | 2026-06-26T21:48:26 |
| `root` | `zxmn` | `209.99.185.59` | 2026-06-26T21:49:13 |
| `root` | `Huawei123` | `209.99.185.59` | 2026-06-26T21:50:15 |
| `root` | `pwdpwd` | `209.99.185.59` | 2026-06-26T21:51:16 |
| `proud` | `proud` | `209.99.185.59` | 2026-06-26T21:52:17 |
| `root` | `svn` | `209.99.185.59` | 2026-06-26T21:53:18 |
| `root` | `doudou` | `209.99.185.59` | 2026-06-26T21:54:19 |
| `admin` | `admin` | `185.211.94.76` | 2026-06-26T21:54:58 |
| `root` | `Oracle!@#456` | `209.99.185.59` | 2026-06-26T21:55:20 |
| `NeverDie` | `11111111` | `209.99.185.59` | 2026-06-26T21:56:23 |
| `professor` | `professor` | `45.198.224.120` | 2026-06-26T21:57:18 |
| `sup` | `sup::` | `209.99.185.59` | 2026-06-26T21:57:26 |
| `liujm1` | `Aa123456788` | `209.99.185.59` | 2026-06-26T21:58:29 |
| `root` | `Uq8hBhV3gR` | `10.0.0.73` | 2026-06-26T21:59:09 |
| `root` | `qazqwe!#%&` | `209.99.185.59` | 2026-06-26T21:59:31 |
| `local` | `local123` | `209.99.185.59` | 2026-06-26T22:00:28 |
| `root` | `86981198` | `91.92.40.90` | 2026-06-26T22:01:08 |
| `acs` | `123456` | `209.99.185.59` | 2026-06-26T22:01:15 |
| `ubuntu` | `q1q2q3q4` | `209.99.185.59` | 2026-06-26T22:02:02 |
| `root` | `Pass12345678` | `209.99.185.59` | 2026-06-26T22:02:49 |
| `root` | `PassW0rd` | `45.205.1.42` | 2026-06-26T22:03:30 |
| `root` | `1qazxsw23edc` | `209.99.185.59` | 2026-06-26T22:03:37 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-26T22:04:03 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-26T22:04:03 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-26T22:04:08 |
| `gaomengge` | `gaomengge` | `209.99.185.59` | 2026-06-26T22:04:23 |
| `iexcel_wuhan` | `iexcel_wuhan321` | `209.99.185.59` | 2026-06-26T22:05:10 |
| `root` | `111111` | `80.94.92.55` | 2026-06-26T22:05:23 |
| `dell` | `Admin@2015` | `209.99.185.59` | 2026-06-26T22:05:56 |
| `liuchang` | `wert2345` | `209.99.185.59` | 2026-06-26T22:06:42 |
| `di` | `di` | `209.99.185.59` | 2026-06-26T22:07:29 |
| `root` | `123123` | `80.94.92.55` | 2026-06-26T22:07:44 |
| `oracle` | `manager` | `209.99.185.59` | 2026-06-26T22:08:16 |
| `root` | `Tele@123` | `209.99.185.59` | 2026-06-26T22:09:04 |
| `fcx` | `123456` | `209.99.185.59` | 2026-06-26T22:09:52 |
| `root` | `Qwerty1` | `45.198.224.120` | 2026-06-26T22:09:53 |
| `root` | `1234` | `80.94.92.55` | 2026-06-26T22:10:10 |
| `root` | `2011` | `209.99.185.59` | 2026-06-26T22:10:39 |
| `root` | `﻿------fuck------` | `115.190.145.176` | 2026-06-26T22:11:11 |
| `root` | `kernel` | `209.99.185.59` | 2026-06-26T22:11:25 |
| `wsm` | `wsm` | `209.99.185.59` | 2026-06-26T22:12:10 |
| `root` | `12345` | `80.94.92.55` | 2026-06-26T22:12:25 |
| `root` | `yw@123456` | `209.99.185.59` | 2026-06-26T22:12:57 |
| `admin` | `admin` | `64.227.0.95` | 2026-06-26T22:13:00 |
| `journal` | `journal` | `209.99.185.59` | 2026-06-26T22:13:45 |
| `focus` | `1234` | `209.99.185.59` | 2026-06-26T22:14:32 |
| `admin` | `admin123` | `209.99.185.59` | 2026-06-26T22:15:21 |
| `root` | `2007` | `209.99.185.59` | 2026-06-26T22:16:09 |
| `root` | `qazxsw!@#` | `209.99.185.59` | 2026-06-26T22:16:58 |
| `root` | `12345678` | `80.94.92.55` | 2026-06-26T22:17:10 |
| `root` | `Passw0rd@1234` | `209.99.185.59` | 2026-06-26T22:17:46 |
| `root` | `qwertz1234` | `45.205.1.42` | 2026-06-26T22:18:33 |
| `nginx` | `changeme` | `209.99.185.59` | 2026-06-26T22:18:33 |
| `root` | `abcdefgh123456` | `209.99.185.59` | 2026-06-26T22:19:20 |
| `root` | `123456789` | `80.94.92.55` | 2026-06-26T22:19:33 |
| `hadoop` | `wasd` | `209.99.185.59` | 2026-06-26T22:20:08 |
| `server` | `qwerty123` | `209.99.185.59` | 2026-06-26T22:20:56 |
| `ubuntu` | `ubnt` | `209.99.185.59` | 2026-06-26T22:21:45 |
| `root` | `Password1` | `80.94.92.55` | 2026-06-26T22:22:02 |
| `root` | `q1w2e3,.` | `45.198.224.120` | 2026-06-26T22:22:18 |
| `zhoux` | `123456` | `209.99.185.59` | 2026-06-26T22:22:34 |
| `tanglulu` | `lulu` | `209.99.185.59` | 2026-06-26T22:23:22 |
| `root` | `P@ssword1234` | `209.99.185.59` | 2026-06-26T22:24:09 |
| `root` | `admin` | `80.94.92.55` | 2026-06-26T22:24:30 |
| `weblogic` | `123456` | `209.99.185.59` | 2026-06-26T22:24:56 |
| `root` | `Pass!@` | `209.99.185.59` | 2026-06-26T22:25:44 |
| `root` | `safekeeping` | `209.99.185.59` | 2026-06-26T22:26:32 |
| `user` | `user123#` | `209.99.185.59` | 2026-06-26T22:27:22 |
| `root` | `9999` | `209.99.185.59` | 2026-06-26T22:28:13 |
| `admin` | `123qwe!@#` | `209.99.185.59` | 2026-06-26T22:29:05 |
| `Soyoun` | `korea2018` | `209.99.185.59` | 2026-06-26T22:29:54 |
| `testing` | `123` | `209.99.185.59` | 2026-06-26T22:30:44 |
| `root` | `sugonhpctest` | `209.99.185.59` | 2026-06-26T22:31:32 |
| `sk` | `sksk` | `209.99.185.59` | 2026-06-26T22:32:21 |
| `root` | `root0000` | `209.99.185.59` | 2026-06-26T22:33:11 |
| `root` | `qazWSXedc` | `45.205.1.42` | 2026-06-26T22:33:32 |
| `root` | `qwerty56` | `209.99.185.59` | 2026-06-26T22:34:02 |
| `yangliusha14` | `yangliusha14` | `45.198.224.120` | 2026-06-26T22:34:26 |
| `root` | `test1234567890` | `209.99.185.59` | 2026-06-26T22:34:53 |
| `ubuntu` | `Passw0rd1111` | `209.99.185.59` | 2026-06-26T22:35:44 |
| `postgres` | `1234` | `209.99.185.59` | 2026-06-26T22:36:34 |
| `zhangyh` | `1` | `45.198.224.92` | 2026-06-26T22:36:36 |
| `hsj` | `korea2022` | `209.99.185.59` | 2026-06-26T22:37:24 |
| `weixiao` | `weixiao` | `209.99.185.59` | 2026-06-26T22:38:12 |
| `zhangxc` | `zhangxc` | `209.99.185.59` | 2026-06-26T22:39:03 |
| `sugon` | `Sugon@123` | `209.99.185.59` | 2026-06-26T22:39:54 |
| `root` | `nicole` | `209.99.185.59` | 2026-06-26T22:40:45 |
| `clara` | `clara` | `209.99.185.59` | 2026-06-26T22:41:37 |
| `wartung` | `222222` | `209.99.185.59` | 2026-06-26T22:42:28 |
| `es` | `abc123` | `209.99.185.59` | 2026-06-26T22:43:19 |
| `pico` | `pico` | `209.99.185.59` | 2026-06-26T22:44:09 |
| `root` | `4444` | `209.99.185.59` | 2026-06-26T22:45:00 |
| `user1` | `user1pwla` | `209.99.185.59` | 2026-06-26T22:45:52 |
| `root` | `qweqscqaz123#@!` | `209.99.185.59` | 2026-06-26T22:46:41 |
| `root` | `PaSsWoRd0` | `45.198.224.120` | 2026-06-26T22:46:52 |
| `root` | `Root-123` | `209.99.185.59` | 2026-06-26T22:47:31 |
| `panyang` | `panyang` | `209.99.185.59` | 2026-06-26T22:48:21 |
| `ubuntu` | `deploy1234567` | `45.205.1.42` | 2026-06-26T22:48:26 |
| `khem` | `khem` | `209.99.185.59` | 2026-06-26T22:49:11 |
| `oyh` | `123456` | `209.99.185.59` | 2026-06-26T22:50:00 |
| `root` | `Oracle@1234` | `209.99.185.59` | 2026-06-26T22:50:53 |
| `user` | `clumsy0770534694` | `209.99.185.59` | 2026-06-26T22:51:43 |
| `root` | `Pass@word123!@#` | `209.99.185.59` | 2026-06-26T22:52:36 |
| `root` | `1988` | `209.99.185.59` | 2026-06-26T22:53:30 |
| `martin` | `123456` | `209.99.185.59` | 2026-06-26T22:54:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **352** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 177 |
| libssh | 10 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 156 | 4 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `19532158b559...` | Mirai/variant | 3 | 3 |
| `5f904648ee89...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 156 | 4 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 3 | 3 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 12 | 2 | `T1082, T1592, T1078, T1083` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ;
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null | cut -d. -f1
```
```
echo '123qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `195.178.110.217`, `80.94.92.55`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **22** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS215925` | VPSVAULT.HOST LTD | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS202412` | Omegatech LTD | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS197170` | TechTies Inc. | 1 | HIGH |
| `AS63835` | CT HuNan Changsha IDC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (181)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8dc7540ae72f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 20:55 |
| **Last Seen** | 2026-06-26 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:55:32` | `cowrie.session.connect` |
| `2026-06-26 20:55:32` | `cowrie.client.version` |
| `2026-06-26 20:55:32` | `cowrie.client.kex` |
| `2026-06-26 20:55:32` | `cowrie.login.success` |
| `2026-06-26 20:55:33` | `cowrie.session.params` |
| `2026-06-26 20:55:33` | `cowrie.command.input` |
| `2026-06-26 20:55:33` | `cowrie.log.closed` |
| `2026-06-26 20:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0c2df1d8d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 20:56 |
| **Last Seen** | 2026-06-26 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:56:23` | `cowrie.session.connect` |
| `2026-06-26 20:56:23` | `cowrie.client.version` |
| `2026-06-26 20:56:23` | `cowrie.client.kex` |
| `2026-06-26 20:56:24` | `cowrie.login.success` |
| `2026-06-26 20:56:25` | `cowrie.session.params` |
| `2026-06-26 20:56:25` | `cowrie.command.input` |
| `2026-06-26 20:56:25` | `cowrie.log.closed` |
| `2026-06-26 20:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c63caf037e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-26 20:56 |
| **Last Seen** | 2026-06-26 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:56:31` | `cowrie.session.connect` |
| `2026-06-26 20:56:31` | `cowrie.client.version` |
| `2026-06-26 20:56:31` | `cowrie.client.kex` |
| `2026-06-26 20:56:31` | `cowrie.login.success` |
| `2026-06-26 20:56:32` | `cowrie.session.params` |
| `2026-06-26 20:56:32` | `cowrie.command.input` |
| `2026-06-26 20:56:33` | `cowrie.log.closed` |
| `2026-06-26 20:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e90ef90c5d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 20:57 |
| **Last Seen** | 2026-06-26 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:57:15` | `cowrie.session.connect` |
| `2026-06-26 20:57:15` | `cowrie.client.version` |
| `2026-06-26 20:57:15` | `cowrie.client.kex` |
| `2026-06-26 20:57:15` | `cowrie.login.success` |
| `2026-06-26 20:57:16` | `cowrie.session.params` |
| `2026-06-26 20:57:16` | `cowrie.command.input` |
| `2026-06-26 20:57:16` | `cowrie.log.closed` |
| `2026-06-26 20:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b47cdb3b818

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 20:58 |
| **Last Seen** | 2026-06-26 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:58:08` | `cowrie.session.connect` |
| `2026-06-26 20:58:08` | `cowrie.client.version` |
| `2026-06-26 20:58:08` | `cowrie.client.kex` |
| `2026-06-26 20:58:08` | `cowrie.login.success` |
| `2026-06-26 20:58:09` | `cowrie.session.params` |
| `2026-06-26 20:58:09` | `cowrie.command.input` |
| `2026-06-26 20:58:09` | `cowrie.log.closed` |
| `2026-06-26 20:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c3c8aa64240

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 20:59 |
| **Last Seen** | 2026-06-26 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:59:00` | `cowrie.session.connect` |
| `2026-06-26 20:59:00` | `cowrie.client.version` |
| `2026-06-26 20:59:00` | `cowrie.client.kex` |
| `2026-06-26 20:59:00` | `cowrie.login.success` |
| `2026-06-26 20:59:01` | `cowrie.session.params` |
| `2026-06-26 20:59:01` | `cowrie.command.input` |
| `2026-06-26 20:59:01` | `cowrie.log.closed` |
| `2026-06-26 20:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00647fa83e81

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 20:59 |
| **Last Seen** | 2026-06-26 20:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:59:42` | `cowrie.session.connect` |
| `2026-06-26 20:59:44` | `cowrie.client.version` |
| `2026-06-26 20:59:44` | `cowrie.client.kex` |
| `2026-06-26 20:59:50` | `cowrie.login.success` |
| `2026-06-26 20:59:53` | `cowrie.session.params` |
| `2026-06-26 20:59:53` | `cowrie.command.input` |
| `2026-06-26 20:59:55` | `cowrie.log.closed` |
| `2026-06-26 20:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd92429fd461

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 20:59 |
| **Last Seen** | 2026-06-26 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 20:59:53` | `cowrie.session.connect` |
| `2026-06-26 20:59:53` | `cowrie.client.version` |
| `2026-06-26 20:59:53` | `cowrie.client.kex` |
| `2026-06-26 20:59:53` | `cowrie.login.success` |
| `2026-06-26 20:59:54` | `cowrie.session.params` |
| `2026-06-26 20:59:54` | `cowrie.command.input` |
| `2026-06-26 20:59:54` | `cowrie.log.closed` |
| `2026-06-26 20:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae633f4c2ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:00 |
| **Last Seen** | 2026-06-26 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:00:57` | `cowrie.session.connect` |
| `2026-06-26 21:00:57` | `cowrie.client.version` |
| `2026-06-26 21:00:57` | `cowrie.client.kex` |
| `2026-06-26 21:00:58` | `cowrie.login.success` |
| `2026-06-26 21:00:58` | `cowrie.session.params` |
| `2026-06-26 21:00:58` | `cowrie.command.input` |
| `2026-06-26 21:00:58` | `cowrie.log.closed` |
| `2026-06-26 21:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff8909cba67f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:01 |
| **Last Seen** | 2026-06-26 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:01:57` | `cowrie.session.connect` |
| `2026-06-26 21:01:57` | `cowrie.client.version` |
| `2026-06-26 21:01:57` | `cowrie.client.kex` |
| `2026-06-26 21:01:57` | `cowrie.login.success` |
| `2026-06-26 21:01:58` | `cowrie.session.params` |
| `2026-06-26 21:01:58` | `cowrie.command.input` |
| `2026-06-26 21:01:58` | `cowrie.log.closed` |
| `2026-06-26 21:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2246faae97e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:02 |
| **Last Seen** | 2026-06-26 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:02:48` | `cowrie.session.connect` |
| `2026-06-26 21:02:48` | `cowrie.client.version` |
| `2026-06-26 21:02:49` | `cowrie.client.kex` |
| `2026-06-26 21:02:49` | `cowrie.login.success` |
| `2026-06-26 21:02:50` | `cowrie.session.params` |
| `2026-06-26 21:02:50` | `cowrie.command.input` |
| `2026-06-26 21:02:50` | `cowrie.log.closed` |
| `2026-06-26 21:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b2db567901

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 21:02 |
| **Last Seen** | 2026-06-26 21:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:02:49` | `cowrie.session.connect` |
| `2026-06-26 21:02:50` | `cowrie.client.version` |
| `2026-06-26 21:02:50` | `cowrie.client.kex` |
| `2026-06-26 21:02:52` | `cowrie.login.success` |
| `2026-06-26 21:02:54` | `cowrie.session.params` |
| `2026-06-26 21:02:54` | `cowrie.command.input` |
| `2026-06-26 21:02:54` | `cowrie.log.closed` |
| `2026-06-26 21:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60f6405f0db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:03 |
| **Last Seen** | 2026-06-26 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:03:41` | `cowrie.session.connect` |
| `2026-06-26 21:03:41` | `cowrie.client.version` |
| `2026-06-26 21:03:41` | `cowrie.client.kex` |
| `2026-06-26 21:03:41` | `cowrie.login.success` |
| `2026-06-26 21:03:42` | `cowrie.session.params` |
| `2026-06-26 21:03:42` | `cowrie.command.input` |
| `2026-06-26 21:03:42` | `cowrie.log.closed` |
| `2026-06-26 21:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acfc7a3dd850

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:04 |
| **Last Seen** | 2026-06-26 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:04:34` | `cowrie.session.connect` |
| `2026-06-26 21:04:34` | `cowrie.client.version` |
| `2026-06-26 21:04:34` | `cowrie.client.kex` |
| `2026-06-26 21:04:34` | `cowrie.login.success` |
| `2026-06-26 21:04:35` | `cowrie.session.params` |
| `2026-06-26 21:04:35` | `cowrie.command.input` |
| `2026-06-26 21:04:35` | `cowrie.log.closed` |
| `2026-06-26 21:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59bef6fac9b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:05 |
| **Last Seen** | 2026-06-26 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:05:27` | `cowrie.session.connect` |
| `2026-06-26 21:05:27` | `cowrie.client.version` |
| `2026-06-26 21:05:28` | `cowrie.client.kex` |
| `2026-06-26 21:05:28` | `cowrie.login.success` |
| `2026-06-26 21:05:29` | `cowrie.session.params` |
| `2026-06-26 21:05:29` | `cowrie.command.input` |
| `2026-06-26 21:05:29` | `cowrie.log.closed` |
| `2026-06-26 21:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2858455f2c40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:06 |
| **Last Seen** | 2026-06-26 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:06:20` | `cowrie.session.connect` |
| `2026-06-26 21:06:20` | `cowrie.client.version` |
| `2026-06-26 21:06:20` | `cowrie.client.kex` |
| `2026-06-26 21:06:21` | `cowrie.login.success` |
| `2026-06-26 21:06:22` | `cowrie.session.params` |
| `2026-06-26 21:06:22` | `cowrie.command.input` |
| `2026-06-26 21:06:22` | `cowrie.log.closed` |
| `2026-06-26 21:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063773e69f3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:07 |
| **Last Seen** | 2026-06-26 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:07:14` | `cowrie.session.connect` |
| `2026-06-26 21:07:14` | `cowrie.client.version` |
| `2026-06-26 21:07:14` | `cowrie.client.kex` |
| `2026-06-26 21:07:14` | `cowrie.login.success` |
| `2026-06-26 21:07:15` | `cowrie.session.params` |
| `2026-06-26 21:07:15` | `cowrie.command.input` |
| `2026-06-26 21:07:15` | `cowrie.log.closed` |
| `2026-06-26 21:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e32c41adf63

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:08 |
| **Last Seen** | 2026-06-26 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:08:07` | `cowrie.session.connect` |
| `2026-06-26 21:08:07` | `cowrie.client.version` |
| `2026-06-26 21:08:07` | `cowrie.client.kex` |
| `2026-06-26 21:08:07` | `cowrie.login.success` |
| `2026-06-26 21:08:08` | `cowrie.session.params` |
| `2026-06-26 21:08:08` | `cowrie.command.input` |
| `2026-06-26 21:08:08` | `cowrie.log.closed` |
| `2026-06-26 21:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2f90f0882d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:08 |
| **Last Seen** | 2026-06-26 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:08:59` | `cowrie.session.connect` |
| `2026-06-26 21:08:59` | `cowrie.client.version` |
| `2026-06-26 21:08:59` | `cowrie.client.kex` |
| `2026-06-26 21:09:00` | `cowrie.login.success` |
| `2026-06-26 21:09:01` | `cowrie.session.params` |
| `2026-06-26 21:09:01` | `cowrie.command.input` |
| `2026-06-26 21:09:01` | `cowrie.log.closed` |
| `2026-06-26 21:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507160755cb9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:09 |
| **Last Seen** | 2026-06-26 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:09:52` | `cowrie.session.connect` |
| `2026-06-26 21:09:52` | `cowrie.client.version` |
| `2026-06-26 21:09:53` | `cowrie.client.kex` |
| `2026-06-26 21:09:53` | `cowrie.login.success` |
| `2026-06-26 21:09:54` | `cowrie.session.params` |
| `2026-06-26 21:09:54` | `cowrie.command.input` |
| `2026-06-26 21:09:54` | `cowrie.log.closed` |
| `2026-06-26 21:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-830b6892490c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:10 |
| **Last Seen** | 2026-06-26 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:10:47` | `cowrie.session.connect` |
| `2026-06-26 21:10:47` | `cowrie.client.version` |
| `2026-06-26 21:10:47` | `cowrie.client.kex` |
| `2026-06-26 21:10:47` | `cowrie.login.success` |
| `2026-06-26 21:10:48` | `cowrie.session.params` |
| `2026-06-26 21:10:48` | `cowrie.command.input` |
| `2026-06-26 21:10:48` | `cowrie.log.closed` |
| `2026-06-26 21:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3325b91cee21

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 21:11 |
| **Last Seen** | 2026-06-26 21:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:11:02` | `cowrie.session.connect` |
| `2026-06-26 21:11:03` | `cowrie.client.version` |
| `2026-06-26 21:11:03` | `cowrie.client.kex` |
| `2026-06-26 21:11:08` | `cowrie.login.success` |
| `2026-06-26 21:11:12` | `cowrie.session.params` |
| `2026-06-26 21:11:12` | `cowrie.command.input` |
| `2026-06-26 21:11:14` | `cowrie.log.closed` |
| `2026-06-26 21:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42eed9025e0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:11 |
| **Last Seen** | 2026-06-26 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:11:42` | `cowrie.session.connect` |
| `2026-06-26 21:11:42` | `cowrie.client.version` |
| `2026-06-26 21:11:42` | `cowrie.client.kex` |
| `2026-06-26 21:11:42` | `cowrie.login.success` |
| `2026-06-26 21:11:43` | `cowrie.session.params` |
| `2026-06-26 21:11:43` | `cowrie.command.input` |
| `2026-06-26 21:11:43` | `cowrie.log.closed` |
| `2026-06-26 21:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846c6e5171b6

| Field | Detail |
|---|---|
| **Source IP** | `223.84.239[.]151` |
| **First Seen** | 2026-06-26 21:12 |
| **Last Seen** | 2026-06-26 21:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:12:09` | `cowrie.session.connect` |
| `2026-06-26 21:12:10` | `cowrie.telnet.option` |
| `2026-06-26 21:12:12` | `cowrie.telnet.option` |
| `2026-06-26 21:14:09` | `cowrie.login.success` |
| `2026-06-26 21:14:10` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `223.84.239[.]151` to AbuseIPDB if not already reported
- [ ] Block `223.84.239[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad98ccfcffb9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:12 |
| **Last Seen** | 2026-06-26 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:12:37` | `cowrie.session.connect` |
| `2026-06-26 21:12:37` | `cowrie.client.version` |
| `2026-06-26 21:12:38` | `cowrie.client.kex` |
| `2026-06-26 21:12:38` | `cowrie.login.success` |
| `2026-06-26 21:12:39` | `cowrie.session.params` |
| `2026-06-26 21:12:39` | `cowrie.command.input` |
| `2026-06-26 21:12:39` | `cowrie.log.closed` |
| `2026-06-26 21:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec85120fc135

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-06-26 21:12 |
| **Last Seen** | 2026-06-26 21:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:12:50` | `cowrie.session.connect` |
| `2026-06-26 21:12:50` | `cowrie.client.version` |
| `2026-06-26 21:12:50` | `cowrie.client.kex` |
| `2026-06-26 21:12:50` | `cowrie.login.success` |
| `2026-06-26 21:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00be447ef2b6

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-26 21:12 |
| **Last Seen** | 2026-06-26 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:12:51` | `cowrie.session.connect` |
| `2026-06-26 21:12:51` | `cowrie.client.version` |
| `2026-06-26 21:12:51` | `cowrie.client.kex` |
| `2026-06-26 21:12:51` | `cowrie.login.success` |
| `2026-06-26 21:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371e00ad52e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:13 |
| **Last Seen** | 2026-06-26 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:13:32` | `cowrie.session.connect` |
| `2026-06-26 21:13:32` | `cowrie.client.version` |
| `2026-06-26 21:13:32` | `cowrie.client.kex` |
| `2026-06-26 21:13:32` | `cowrie.login.success` |
| `2026-06-26 21:13:33` | `cowrie.session.params` |
| `2026-06-26 21:13:33` | `cowrie.command.input` |
| `2026-06-26 21:13:33` | `cowrie.log.closed` |
| `2026-06-26 21:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d11d26a5150

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:14 |
| **Last Seen** | 2026-06-26 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:14:26` | `cowrie.session.connect` |
| `2026-06-26 21:14:26` | `cowrie.client.version` |
| `2026-06-26 21:14:27` | `cowrie.client.kex` |
| `2026-06-26 21:14:27` | `cowrie.login.success` |
| `2026-06-26 21:14:27` | `cowrie.session.params` |
| `2026-06-26 21:14:27` | `cowrie.command.input` |
| `2026-06-26 21:14:28` | `cowrie.log.closed` |
| `2026-06-26 21:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccab8cfce92d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:15 |
| **Last Seen** | 2026-06-26 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:15:20` | `cowrie.session.connect` |
| `2026-06-26 21:15:20` | `cowrie.client.version` |
| `2026-06-26 21:15:20` | `cowrie.client.kex` |
| `2026-06-26 21:15:20` | `cowrie.login.success` |
| `2026-06-26 21:15:21` | `cowrie.session.params` |
| `2026-06-26 21:15:21` | `cowrie.command.input` |
| `2026-06-26 21:15:21` | `cowrie.log.closed` |
| `2026-06-26 21:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3abb58e039

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-26 21:15 |
| **Last Seen** | 2026-06-26 21:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:15:29` | `cowrie.session.connect` |
| `2026-06-26 21:15:29` | `cowrie.client.version` |
| `2026-06-26 21:15:29` | `cowrie.client.kex` |
| `2026-06-26 21:15:30` | `cowrie.login.success` |
| `2026-06-26 21:15:31` | `cowrie.session.params` |
| `2026-06-26 21:15:31` | `cowrie.command.input` |
| `2026-06-26 21:15:31` | `cowrie.command.input` |
| `2026-06-26 21:15:31` | `cowrie.command.input` |
| `2026-06-26 21:15:31` | `cowrie.command.input` |
| `2026-06-26 21:15:32` | `cowrie.log.closed` |
| `2026-06-26 21:15:33` | `cowrie.session.params` |
| `2026-06-26 21:15:33` | `cowrie.command.input` |
| `2026-06-26 21:15:33` | `cowrie.command.input` |
| `2026-06-26 21:15:33` | `cowrie.command.failed` |
| `2026-06-26 21:15:33` | `cowrie.command.failed` |
| `2026-06-26 21:15:33` | `cowrie.command.failed` |
| `2026-06-26 21:15:33` | `cowrie.command.failed` |
| `2026-06-26 21:15:33` | `cowrie.log.closed` |
| `2026-06-26 21:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4201b78be770

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:16 |
| **Last Seen** | 2026-06-26 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:16:14` | `cowrie.session.connect` |
| `2026-06-26 21:16:14` | `cowrie.client.version` |
| `2026-06-26 21:16:14` | `cowrie.client.kex` |
| `2026-06-26 21:16:15` | `cowrie.login.success` |
| `2026-06-26 21:16:16` | `cowrie.session.params` |
| `2026-06-26 21:16:16` | `cowrie.command.input` |
| `2026-06-26 21:16:16` | `cowrie.log.closed` |
| `2026-06-26 21:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d2dc545b25

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:17 |
| **Last Seen** | 2026-06-26 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:17:09` | `cowrie.session.connect` |
| `2026-06-26 21:17:09` | `cowrie.client.version` |
| `2026-06-26 21:17:10` | `cowrie.client.kex` |
| `2026-06-26 21:17:10` | `cowrie.login.success` |
| `2026-06-26 21:17:11` | `cowrie.session.params` |
| `2026-06-26 21:17:11` | `cowrie.command.input` |
| `2026-06-26 21:17:11` | `cowrie.log.closed` |
| `2026-06-26 21:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494c7658953a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-26 21:17 |
| **Last Seen** | 2026-06-26 21:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '21' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:17:33` | `cowrie.session.connect` |
| `2026-06-26 21:17:33` | `cowrie.client.version` |
| `2026-06-26 21:17:33` | `cowrie.client.kex` |
| `2026-06-26 21:17:35` | `cowrie.login.success` |
| `2026-06-26 21:17:36` | `cowrie.session.params` |
| `2026-06-26 21:17:36` | `cowrie.command.input` |
| `2026-06-26 21:17:36` | `cowrie.command.input` |
| `2026-06-26 21:17:36` | `cowrie.command.input` |
| `2026-06-26 21:17:36` | `cowrie.command.input` |
| `2026-06-26 21:17:36` | `cowrie.log.closed` |
| `2026-06-26 21:17:37` | `cowrie.session.params` |
| `2026-06-26 21:17:37` | `cowrie.command.input` |
| `2026-06-26 21:17:37` | `cowrie.command.input` |
| `2026-06-26 21:17:37` | `cowrie.command.failed` |
| `2026-06-26 21:17:37` | `cowrie.command.failed` |
| `2026-06-26 21:17:37` | `cowrie.command.failed` |
| `2026-06-26 21:17:37` | `cowrie.command.failed` |
| `2026-06-26 21:17:38` | `cowrie.log.closed` |
| `2026-06-26 21:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9462a9d9eac

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 21:18 |
| **Last Seen** | 2026-06-26 21:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:18:00` | `cowrie.session.connect` |
| `2026-06-26 21:18:00` | `cowrie.client.version` |
| `2026-06-26 21:18:00` | `cowrie.client.kex` |
| `2026-06-26 21:18:03` | `cowrie.login.success` |
| `2026-06-26 21:18:04` | `cowrie.session.params` |
| `2026-06-26 21:18:04` | `cowrie.command.input` |
| `2026-06-26 21:18:05` | `cowrie.log.closed` |
| `2026-06-26 21:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9805f569a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:18 |
| **Last Seen** | 2026-06-26 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:18:05` | `cowrie.session.connect` |
| `2026-06-26 21:18:05` | `cowrie.client.version` |
| `2026-06-26 21:18:05` | `cowrie.client.kex` |
| `2026-06-26 21:18:06` | `cowrie.login.success` |
| `2026-06-26 21:18:07` | `cowrie.session.params` |
| `2026-06-26 21:18:07` | `cowrie.command.input` |
| `2026-06-26 21:18:07` | `cowrie.log.closed` |
| `2026-06-26 21:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99bdd6634d5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:19 |
| **Last Seen** | 2026-06-26 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:19:02` | `cowrie.session.connect` |
| `2026-06-26 21:19:02` | `cowrie.client.version` |
| `2026-06-26 21:19:02` | `cowrie.client.kex` |
| `2026-06-26 21:19:02` | `cowrie.login.success` |
| `2026-06-26 21:19:03` | `cowrie.session.params` |
| `2026-06-26 21:19:03` | `cowrie.command.input` |
| `2026-06-26 21:19:03` | `cowrie.log.closed` |
| `2026-06-26 21:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca66d593965

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-26 21:19 |
| **Last Seen** | 2026-06-26 21:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:19:48` | `cowrie.session.connect` |
| `2026-06-26 21:19:48` | `cowrie.client.version` |
| `2026-06-26 21:19:48` | `cowrie.client.kex` |
| `2026-06-26 21:19:48` | `cowrie.login.success` |
| `2026-06-26 21:19:49` | `cowrie.session.params` |
| `2026-06-26 21:19:49` | `cowrie.command.input` |
| `2026-06-26 21:19:49` | `cowrie.command.input` |
| `2026-06-26 21:19:49` | `cowrie.command.input` |
| `2026-06-26 21:19:49` | `cowrie.command.input` |
| `2026-06-26 21:19:50` | `cowrie.log.closed` |
| `2026-06-26 21:19:51` | `cowrie.session.params` |
| `2026-06-26 21:19:51` | `cowrie.command.input` |
| `2026-06-26 21:19:51` | `cowrie.command.input` |
| `2026-06-26 21:19:51` | `cowrie.command.failed` |
| `2026-06-26 21:19:51` | `cowrie.command.failed` |
| `2026-06-26 21:19:51` | `cowrie.command.failed` |
| `2026-06-26 21:19:51` | `cowrie.command.failed` |
| `2026-06-26 21:19:51` | `cowrie.log.closed` |
| `2026-06-26 21:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2463607694cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:19 |
| **Last Seen** | 2026-06-26 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:19:58` | `cowrie.session.connect` |
| `2026-06-26 21:19:58` | `cowrie.client.version` |
| `2026-06-26 21:19:58` | `cowrie.client.kex` |
| `2026-06-26 21:19:58` | `cowrie.login.success` |
| `2026-06-26 21:19:59` | `cowrie.session.params` |
| `2026-06-26 21:19:59` | `cowrie.command.input` |
| `2026-06-26 21:19:59` | `cowrie.log.closed` |
| `2026-06-26 21:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36173651ee91

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:20 |
| **Last Seen** | 2026-06-26 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:20:53` | `cowrie.session.connect` |
| `2026-06-26 21:20:53` | `cowrie.client.version` |
| `2026-06-26 21:20:53` | `cowrie.client.kex` |
| `2026-06-26 21:20:53` | `cowrie.login.success` |
| `2026-06-26 21:20:54` | `cowrie.session.params` |
| `2026-06-26 21:20:54` | `cowrie.command.input` |
| `2026-06-26 21:20:54` | `cowrie.log.closed` |
| `2026-06-26 21:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ac15f3092c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:21 |
| **Last Seen** | 2026-06-26 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:21:48` | `cowrie.session.connect` |
| `2026-06-26 21:21:48` | `cowrie.client.version` |
| `2026-06-26 21:21:48` | `cowrie.client.kex` |
| `2026-06-26 21:21:48` | `cowrie.login.success` |
| `2026-06-26 21:21:49` | `cowrie.session.params` |
| `2026-06-26 21:21:49` | `cowrie.command.input` |
| `2026-06-26 21:21:49` | `cowrie.log.closed` |
| `2026-06-26 21:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e807e7ab63

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 21:22 |
| **Last Seen** | 2026-06-26 21:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:22:01` | `cowrie.session.connect` |
| `2026-06-26 21:22:02` | `cowrie.client.version` |
| `2026-06-26 21:22:02` | `cowrie.client.kex` |
| `2026-06-26 21:22:08` | `cowrie.login.success` |
| `2026-06-26 21:22:12` | `cowrie.session.params` |
| `2026-06-26 21:22:12` | `cowrie.command.input` |
| `2026-06-26 21:22:13` | `cowrie.log.closed` |
| `2026-06-26 21:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0972ac707180

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-26 21:22 |
| **Last Seen** | 2026-06-26 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '4321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:22:28` | `cowrie.session.connect` |
| `2026-06-26 21:22:28` | `cowrie.client.version` |
| `2026-06-26 21:22:28` | `cowrie.client.kex` |
| `2026-06-26 21:22:29` | `cowrie.login.success` |
| `2026-06-26 21:22:30` | `cowrie.session.params` |
| `2026-06-26 21:22:30` | `cowrie.command.input` |
| `2026-06-26 21:22:30` | `cowrie.command.input` |
| `2026-06-26 21:22:30` | `cowrie.command.input` |
| `2026-06-26 21:22:30` | `cowrie.command.input` |
| `2026-06-26 21:22:30` | `cowrie.log.closed` |
| `2026-06-26 21:22:31` | `cowrie.session.params` |
| `2026-06-26 21:22:31` | `cowrie.command.input` |
| `2026-06-26 21:22:31` | `cowrie.command.input` |
| `2026-06-26 21:22:31` | `cowrie.command.failed` |
| `2026-06-26 21:22:31` | `cowrie.command.failed` |
| `2026-06-26 21:22:31` | `cowrie.command.failed` |
| `2026-06-26 21:22:31` | `cowrie.command.failed` |
| `2026-06-26 21:22:31` | `cowrie.log.closed` |
| `2026-06-26 21:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1bc82bc271e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:22 |
| **Last Seen** | 2026-06-26 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:22:44` | `cowrie.session.connect` |
| `2026-06-26 21:22:44` | `cowrie.client.version` |
| `2026-06-26 21:22:44` | `cowrie.client.kex` |
| `2026-06-26 21:22:44` | `cowrie.login.success` |
| `2026-06-26 21:22:45` | `cowrie.session.params` |
| `2026-06-26 21:22:45` | `cowrie.command.input` |
| `2026-06-26 21:22:45` | `cowrie.log.closed` |
| `2026-06-26 21:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1536c3be2de9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:23 |
| **Last Seen** | 2026-06-26 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:23:41` | `cowrie.session.connect` |
| `2026-06-26 21:23:41` | `cowrie.client.version` |
| `2026-06-26 21:23:41` | `cowrie.client.kex` |
| `2026-06-26 21:23:41` | `cowrie.login.success` |
| `2026-06-26 21:23:42` | `cowrie.session.params` |
| `2026-06-26 21:23:42` | `cowrie.command.input` |
| `2026-06-26 21:23:42` | `cowrie.log.closed` |
| `2026-06-26 21:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9618d1213707

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:24 |
| **Last Seen** | 2026-06-26 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:24:39` | `cowrie.session.connect` |
| `2026-06-26 21:24:39` | `cowrie.client.version` |
| `2026-06-26 21:24:39` | `cowrie.client.kex` |
| `2026-06-26 21:24:39` | `cowrie.login.success` |
| `2026-06-26 21:24:40` | `cowrie.session.params` |
| `2026-06-26 21:24:40` | `cowrie.command.input` |
| `2026-06-26 21:24:40` | `cowrie.log.closed` |
| `2026-06-26 21:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b8db48367b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:25 |
| **Last Seen** | 2026-06-26 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:25:36` | `cowrie.session.connect` |
| `2026-06-26 21:25:36` | `cowrie.client.version` |
| `2026-06-26 21:25:37` | `cowrie.client.kex` |
| `2026-06-26 21:25:37` | `cowrie.login.success` |
| `2026-06-26 21:25:38` | `cowrie.session.params` |
| `2026-06-26 21:25:38` | `cowrie.command.input` |
| `2026-06-26 21:25:38` | `cowrie.log.closed` |
| `2026-06-26 21:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c1dc16044c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:26 |
| **Last Seen** | 2026-06-26 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:26:33` | `cowrie.session.connect` |
| `2026-06-26 21:26:33` | `cowrie.client.version` |
| `2026-06-26 21:26:33` | `cowrie.client.kex` |
| `2026-06-26 21:26:33` | `cowrie.login.success` |
| `2026-06-26 21:26:34` | `cowrie.session.params` |
| `2026-06-26 21:26:34` | `cowrie.command.input` |
| `2026-06-26 21:26:34` | `cowrie.log.closed` |
| `2026-06-26 21:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad97ddfc29f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:27 |
| **Last Seen** | 2026-06-26 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:27:28` | `cowrie.session.connect` |
| `2026-06-26 21:27:28` | `cowrie.client.version` |
| `2026-06-26 21:27:28` | `cowrie.client.kex` |
| `2026-06-26 21:27:29` | `cowrie.login.success` |
| `2026-06-26 21:27:30` | `cowrie.session.params` |
| `2026-06-26 21:27:30` | `cowrie.command.input` |
| `2026-06-26 21:27:30` | `cowrie.log.closed` |
| `2026-06-26 21:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515c5de0c9aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:28 |
| **Last Seen** | 2026-06-26 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:28:22` | `cowrie.session.connect` |
| `2026-06-26 21:28:22` | `cowrie.client.version` |
| `2026-06-26 21:28:22` | `cowrie.client.kex` |
| `2026-06-26 21:28:23` | `cowrie.login.success` |
| `2026-06-26 21:28:23` | `cowrie.session.params` |
| `2026-06-26 21:28:23` | `cowrie.command.input` |
| `2026-06-26 21:28:23` | `cowrie.log.closed` |
| `2026-06-26 21:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac65b21a44e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:29 |
| **Last Seen** | 2026-06-26 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:29:16` | `cowrie.session.connect` |
| `2026-06-26 21:29:16` | `cowrie.client.version` |
| `2026-06-26 21:29:16` | `cowrie.client.kex` |
| `2026-06-26 21:29:16` | `cowrie.login.success` |
| `2026-06-26 21:29:17` | `cowrie.session.params` |
| `2026-06-26 21:29:17` | `cowrie.command.input` |
| `2026-06-26 21:29:17` | `cowrie.log.closed` |
| `2026-06-26 21:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0afaf91c97cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:30 |
| **Last Seen** | 2026-06-26 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:30:11` | `cowrie.session.connect` |
| `2026-06-26 21:30:11` | `cowrie.client.version` |
| `2026-06-26 21:30:11` | `cowrie.client.kex` |
| `2026-06-26 21:30:12` | `cowrie.login.success` |
| `2026-06-26 21:30:12` | `cowrie.session.params` |
| `2026-06-26 21:30:12` | `cowrie.command.input` |
| `2026-06-26 21:30:12` | `cowrie.log.closed` |
| `2026-06-26 21:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6883909f8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:31 |
| **Last Seen** | 2026-06-26 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:31:06` | `cowrie.session.connect` |
| `2026-06-26 21:31:06` | `cowrie.client.version` |
| `2026-06-26 21:31:07` | `cowrie.client.kex` |
| `2026-06-26 21:31:07` | `cowrie.login.success` |
| `2026-06-26 21:31:08` | `cowrie.session.params` |
| `2026-06-26 21:31:08` | `cowrie.command.input` |
| `2026-06-26 21:31:08` | `cowrie.log.closed` |
| `2026-06-26 21:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a45115dd1d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:32 |
| **Last Seen** | 2026-06-26 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:32:01` | `cowrie.session.connect` |
| `2026-06-26 21:32:01` | `cowrie.client.version` |
| `2026-06-26 21:32:01` | `cowrie.client.kex` |
| `2026-06-26 21:32:01` | `cowrie.login.success` |
| `2026-06-26 21:32:02` | `cowrie.session.params` |
| `2026-06-26 21:32:02` | `cowrie.command.input` |
| `2026-06-26 21:32:02` | `cowrie.log.closed` |
| `2026-06-26 21:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-064044f53461

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:32 |
| **Last Seen** | 2026-06-26 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:32:55` | `cowrie.session.connect` |
| `2026-06-26 21:32:55` | `cowrie.client.version` |
| `2026-06-26 21:32:55` | `cowrie.client.kex` |
| `2026-06-26 21:32:55` | `cowrie.login.success` |
| `2026-06-26 21:32:56` | `cowrie.session.params` |
| `2026-06-26 21:32:56` | `cowrie.command.input` |
| `2026-06-26 21:32:56` | `cowrie.log.closed` |
| `2026-06-26 21:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b7607548d7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 21:33 |
| **Last Seen** | 2026-06-26 21:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:33:26` | `cowrie.session.connect` |
| `2026-06-26 21:33:28` | `cowrie.client.version` |
| `2026-06-26 21:33:28` | `cowrie.client.kex` |
| `2026-06-26 21:33:32` | `cowrie.login.success` |
| `2026-06-26 21:33:36` | `cowrie.session.params` |
| `2026-06-26 21:33:36` | `cowrie.command.input` |
| `2026-06-26 21:33:37` | `cowrie.log.closed` |
| `2026-06-26 21:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dcf256e183a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 21:33 |
| **Last Seen** | 2026-06-26 21:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:33:31` | `cowrie.session.connect` |
| `2026-06-26 21:33:32` | `cowrie.client.version` |
| `2026-06-26 21:33:32` | `cowrie.client.kex` |
| `2026-06-26 21:33:34` | `cowrie.login.success` |
| `2026-06-26 21:33:35` | `cowrie.session.params` |
| `2026-06-26 21:33:35` | `cowrie.command.input` |
| `2026-06-26 21:33:36` | `cowrie.log.closed` |
| `2026-06-26 21:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30bf94686662

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:33 |
| **Last Seen** | 2026-06-26 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:33:50` | `cowrie.session.connect` |
| `2026-06-26 21:33:50` | `cowrie.client.version` |
| `2026-06-26 21:33:50` | `cowrie.client.kex` |
| `2026-06-26 21:33:50` | `cowrie.login.success` |
| `2026-06-26 21:33:51` | `cowrie.session.params` |
| `2026-06-26 21:33:51` | `cowrie.command.input` |
| `2026-06-26 21:33:51` | `cowrie.log.closed` |
| `2026-06-26 21:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fae04051da0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:34 |
| **Last Seen** | 2026-06-26 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:34:44` | `cowrie.session.connect` |
| `2026-06-26 21:34:44` | `cowrie.client.version` |
| `2026-06-26 21:34:45` | `cowrie.client.kex` |
| `2026-06-26 21:34:45` | `cowrie.login.success` |
| `2026-06-26 21:34:46` | `cowrie.session.params` |
| `2026-06-26 21:34:46` | `cowrie.command.input` |
| `2026-06-26 21:34:46` | `cowrie.log.closed` |
| `2026-06-26 21:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8052ccba16e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:35 |
| **Last Seen** | 2026-06-26 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:35:40` | `cowrie.session.connect` |
| `2026-06-26 21:35:40` | `cowrie.client.version` |
| `2026-06-26 21:35:40` | `cowrie.client.kex` |
| `2026-06-26 21:35:40` | `cowrie.login.success` |
| `2026-06-26 21:35:41` | `cowrie.session.params` |
| `2026-06-26 21:35:41` | `cowrie.command.input` |
| `2026-06-26 21:35:41` | `cowrie.log.closed` |
| `2026-06-26 21:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e3307250e04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:36 |
| **Last Seen** | 2026-06-26 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:36:37` | `cowrie.session.connect` |
| `2026-06-26 21:36:37` | `cowrie.client.version` |
| `2026-06-26 21:36:37` | `cowrie.client.kex` |
| `2026-06-26 21:36:37` | `cowrie.login.success` |
| `2026-06-26 21:36:38` | `cowrie.session.params` |
| `2026-06-26 21:36:38` | `cowrie.command.input` |
| `2026-06-26 21:36:38` | `cowrie.log.closed` |
| `2026-06-26 21:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc3b0a6f874

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:37 |
| **Last Seen** | 2026-06-26 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:37:34` | `cowrie.session.connect` |
| `2026-06-26 21:37:34` | `cowrie.client.version` |
| `2026-06-26 21:37:35` | `cowrie.client.kex` |
| `2026-06-26 21:37:35` | `cowrie.login.success` |
| `2026-06-26 21:37:36` | `cowrie.session.params` |
| `2026-06-26 21:37:36` | `cowrie.command.input` |
| `2026-06-26 21:37:36` | `cowrie.log.closed` |
| `2026-06-26 21:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f9d2bf4d328

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:38 |
| **Last Seen** | 2026-06-26 21:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:38:32` | `cowrie.session.connect` |
| `2026-06-26 21:38:32` | `cowrie.client.version` |
| `2026-06-26 21:38:32` | `cowrie.client.kex` |
| `2026-06-26 21:38:32` | `cowrie.login.success` |
| `2026-06-26 21:38:33` | `cowrie.session.params` |
| `2026-06-26 21:38:33` | `cowrie.command.input` |
| `2026-06-26 21:38:33` | `cowrie.log.closed` |
| `2026-06-26 21:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5789e2387a47

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:39 |
| **Last Seen** | 2026-06-26 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:39:28` | `cowrie.session.connect` |
| `2026-06-26 21:39:28` | `cowrie.client.version` |
| `2026-06-26 21:39:28` | `cowrie.client.kex` |
| `2026-06-26 21:39:29` | `cowrie.login.success` |
| `2026-06-26 21:39:30` | `cowrie.session.params` |
| `2026-06-26 21:39:30` | `cowrie.command.input` |
| `2026-06-26 21:39:30` | `cowrie.log.closed` |
| `2026-06-26 21:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954b9be35bc9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:40 |
| **Last Seen** | 2026-06-26 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:40:24` | `cowrie.session.connect` |
| `2026-06-26 21:40:24` | `cowrie.client.version` |
| `2026-06-26 21:40:24` | `cowrie.client.kex` |
| `2026-06-26 21:40:25` | `cowrie.login.success` |
| `2026-06-26 21:40:25` | `cowrie.session.params` |
| `2026-06-26 21:40:25` | `cowrie.command.input` |
| `2026-06-26 21:40:26` | `cowrie.log.closed` |
| `2026-06-26 21:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ddb7bd9def

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:41 |
| **Last Seen** | 2026-06-26 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:41:20` | `cowrie.session.connect` |
| `2026-06-26 21:41:20` | `cowrie.client.version` |
| `2026-06-26 21:41:20` | `cowrie.client.kex` |
| `2026-06-26 21:41:20` | `cowrie.login.success` |
| `2026-06-26 21:41:21` | `cowrie.session.params` |
| `2026-06-26 21:41:21` | `cowrie.command.input` |
| `2026-06-26 21:41:21` | `cowrie.log.closed` |
| `2026-06-26 21:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da37812d41ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:42 |
| **Last Seen** | 2026-06-26 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:42:17` | `cowrie.session.connect` |
| `2026-06-26 21:42:17` | `cowrie.client.version` |
| `2026-06-26 21:42:17` | `cowrie.client.kex` |
| `2026-06-26 21:42:17` | `cowrie.login.success` |
| `2026-06-26 21:42:18` | `cowrie.session.params` |
| `2026-06-26 21:42:18` | `cowrie.command.input` |
| `2026-06-26 21:42:18` | `cowrie.log.closed` |
| `2026-06-26 21:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4971ce6cf732

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:43 |
| **Last Seen** | 2026-06-26 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:43:15` | `cowrie.session.connect` |
| `2026-06-26 21:43:15` | `cowrie.client.version` |
| `2026-06-26 21:43:15` | `cowrie.client.kex` |
| `2026-06-26 21:43:15` | `cowrie.login.success` |
| `2026-06-26 21:43:16` | `cowrie.session.params` |
| `2026-06-26 21:43:16` | `cowrie.command.input` |
| `2026-06-26 21:43:16` | `cowrie.log.closed` |
| `2026-06-26 21:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7af7e46f0d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:44 |
| **Last Seen** | 2026-06-26 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:44:13` | `cowrie.session.connect` |
| `2026-06-26 21:44:13` | `cowrie.client.version` |
| `2026-06-26 21:44:14` | `cowrie.client.kex` |
| `2026-06-26 21:44:14` | `cowrie.login.success` |
| `2026-06-26 21:44:15` | `cowrie.session.params` |
| `2026-06-26 21:44:15` | `cowrie.command.input` |
| `2026-06-26 21:44:15` | `cowrie.log.closed` |
| `2026-06-26 21:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d1bd2c1041

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 21:45 |
| **Last Seen** | 2026-06-26 21:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:45:01` | `cowrie.session.connect` |
| `2026-06-26 21:45:03` | `cowrie.client.version` |
| `2026-06-26 21:45:03` | `cowrie.client.kex` |
| `2026-06-26 21:45:09` | `cowrie.login.success` |
| `2026-06-26 21:45:13` | `cowrie.session.params` |
| `2026-06-26 21:45:13` | `cowrie.command.input` |
| `2026-06-26 21:45:14` | `cowrie.log.closed` |
| `2026-06-26 21:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5178f1d939c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:45 |
| **Last Seen** | 2026-06-26 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:45:13` | `cowrie.session.connect` |
| `2026-06-26 21:45:13` | `cowrie.client.version` |
| `2026-06-26 21:45:13` | `cowrie.client.kex` |
| `2026-06-26 21:45:14` | `cowrie.login.success` |
| `2026-06-26 21:45:14` | `cowrie.session.params` |
| `2026-06-26 21:45:14` | `cowrie.command.input` |
| `2026-06-26 21:45:15` | `cowrie.log.closed` |
| `2026-06-26 21:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9be2d16b48

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:46 |
| **Last Seen** | 2026-06-26 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:46:12` | `cowrie.session.connect` |
| `2026-06-26 21:46:12` | `cowrie.client.version` |
| `2026-06-26 21:46:12` | `cowrie.client.kex` |
| `2026-06-26 21:46:12` | `cowrie.login.success` |
| `2026-06-26 21:46:13` | `cowrie.session.params` |
| `2026-06-26 21:46:13` | `cowrie.command.input` |
| `2026-06-26 21:46:13` | `cowrie.log.closed` |
| `2026-06-26 21:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2398c5034dd9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:47 |
| **Last Seen** | 2026-06-26 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:47:11` | `cowrie.session.connect` |
| `2026-06-26 21:47:11` | `cowrie.client.version` |
| `2026-06-26 21:47:11` | `cowrie.client.kex` |
| `2026-06-26 21:47:11` | `cowrie.login.success` |
| `2026-06-26 21:47:12` | `cowrie.session.params` |
| `2026-06-26 21:47:12` | `cowrie.command.input` |
| `2026-06-26 21:47:12` | `cowrie.log.closed` |
| `2026-06-26 21:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce43f4e63323

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:48 |
| **Last Seen** | 2026-06-26 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:48:12` | `cowrie.session.connect` |
| `2026-06-26 21:48:12` | `cowrie.client.version` |
| `2026-06-26 21:48:12` | `cowrie.client.kex` |
| `2026-06-26 21:48:12` | `cowrie.login.success` |
| `2026-06-26 21:48:13` | `cowrie.session.params` |
| `2026-06-26 21:48:13` | `cowrie.command.input` |
| `2026-06-26 21:48:13` | `cowrie.log.closed` |
| `2026-06-26 21:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e455927b43d7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 21:48 |
| **Last Seen** | 2026-06-26 21:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:48:24` | `cowrie.session.connect` |
| `2026-06-26 21:48:24` | `cowrie.client.version` |
| `2026-06-26 21:48:24` | `cowrie.client.kex` |
| `2026-06-26 21:48:26` | `cowrie.login.success` |
| `2026-06-26 21:48:27` | `cowrie.session.params` |
| `2026-06-26 21:48:27` | `cowrie.command.input` |
| `2026-06-26 21:48:28` | `cowrie.log.closed` |
| `2026-06-26 21:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac056ddf633f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:49 |
| **Last Seen** | 2026-06-26 21:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:49:13` | `cowrie.session.connect` |
| `2026-06-26 21:49:13` | `cowrie.client.version` |
| `2026-06-26 21:49:13` | `cowrie.client.kex` |
| `2026-06-26 21:49:13` | `cowrie.login.success` |
| `2026-06-26 21:49:14` | `cowrie.session.params` |
| `2026-06-26 21:49:14` | `cowrie.command.input` |
| `2026-06-26 21:49:14` | `cowrie.log.closed` |
| `2026-06-26 21:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99bc0c857e55

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:50 |
| **Last Seen** | 2026-06-26 21:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:50:14` | `cowrie.session.connect` |
| `2026-06-26 21:50:14` | `cowrie.client.version` |
| `2026-06-26 21:50:15` | `cowrie.client.kex` |
| `2026-06-26 21:50:15` | `cowrie.login.success` |
| `2026-06-26 21:50:16` | `cowrie.session.params` |
| `2026-06-26 21:50:16` | `cowrie.command.input` |
| `2026-06-26 21:50:16` | `cowrie.log.closed` |
| `2026-06-26 21:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c79126ddfdb2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:51 |
| **Last Seen** | 2026-06-26 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:51:16` | `cowrie.session.connect` |
| `2026-06-26 21:51:16` | `cowrie.client.version` |
| `2026-06-26 21:51:16` | `cowrie.client.kex` |
| `2026-06-26 21:51:16` | `cowrie.login.success` |
| `2026-06-26 21:51:17` | `cowrie.session.params` |
| `2026-06-26 21:51:17` | `cowrie.command.input` |
| `2026-06-26 21:51:17` | `cowrie.log.closed` |
| `2026-06-26 21:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6463f28ca9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:52 |
| **Last Seen** | 2026-06-26 21:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:52:17` | `cowrie.session.connect` |
| `2026-06-26 21:52:17` | `cowrie.client.version` |
| `2026-06-26 21:52:17` | `cowrie.client.kex` |
| `2026-06-26 21:52:17` | `cowrie.login.success` |
| `2026-06-26 21:52:18` | `cowrie.session.params` |
| `2026-06-26 21:52:18` | `cowrie.command.input` |
| `2026-06-26 21:52:18` | `cowrie.log.closed` |
| `2026-06-26 21:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f20ce40eaebb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:53 |
| **Last Seen** | 2026-06-26 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:53:17` | `cowrie.session.connect` |
| `2026-06-26 21:53:17` | `cowrie.client.version` |
| `2026-06-26 21:53:17` | `cowrie.client.kex` |
| `2026-06-26 21:53:18` | `cowrie.login.success` |
| `2026-06-26 21:53:18` | `cowrie.session.params` |
| `2026-06-26 21:53:18` | `cowrie.command.input` |
| `2026-06-26 21:53:19` | `cowrie.log.closed` |
| `2026-06-26 21:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5a580fc8d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:54 |
| **Last Seen** | 2026-06-26 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:54:18` | `cowrie.session.connect` |
| `2026-06-26 21:54:18` | `cowrie.client.version` |
| `2026-06-26 21:54:18` | `cowrie.client.kex` |
| `2026-06-26 21:54:19` | `cowrie.login.success` |
| `2026-06-26 21:54:19` | `cowrie.session.params` |
| `2026-06-26 21:54:19` | `cowrie.command.input` |
| `2026-06-26 21:54:19` | `cowrie.log.closed` |
| `2026-06-26 21:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13370e9b4a1d

| Field | Detail |
|---|---|
| **Source IP** | `185.211.94[.]76` |
| **First Seen** | 2026-06-26 21:54 |
| **Last Seen** | 2026-06-26 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:54:58` | `cowrie.session.connect` |
| `2026-06-26 21:54:58` | `cowrie.client.version` |
| `2026-06-26 21:54:58` | `cowrie.client.kex` |
| `2026-06-26 21:54:58` | `cowrie.login.success` |
| `2026-06-26 21:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.211.94[.]76` to AbuseIPDB if not already reported
- [ ] Block `185.211.94[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25350a6c21e2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-26 21:54 |
| **Last Seen** | 2026-06-26 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:54:59` | `cowrie.session.connect` |
| `2026-06-26 21:54:59` | `cowrie.client.version` |
| `2026-06-26 21:54:59` | `cowrie.client.kex` |
| `2026-06-26 21:54:59` | `cowrie.login.success` |
| `2026-06-26 21:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa92f3f4b9ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:55 |
| **Last Seen** | 2026-06-26 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:55:20` | `cowrie.session.connect` |
| `2026-06-26 21:55:20` | `cowrie.client.version` |
| `2026-06-26 21:55:20` | `cowrie.client.kex` |
| `2026-06-26 21:55:20` | `cowrie.login.success` |
| `2026-06-26 21:55:21` | `cowrie.session.params` |
| `2026-06-26 21:55:21` | `cowrie.command.input` |
| `2026-06-26 21:55:21` | `cowrie.log.closed` |
| `2026-06-26 21:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b8b2b6fdb8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:56 |
| **Last Seen** | 2026-06-26 21:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:56:23` | `cowrie.session.connect` |
| `2026-06-26 21:56:23` | `cowrie.client.version` |
| `2026-06-26 21:56:23` | `cowrie.client.kex` |
| `2026-06-26 21:56:23` | `cowrie.login.success` |
| `2026-06-26 21:56:24` | `cowrie.session.params` |
| `2026-06-26 21:56:24` | `cowrie.command.input` |
| `2026-06-26 21:56:24` | `cowrie.log.closed` |
| `2026-06-26 21:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9410754e20c2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 21:57 |
| **Last Seen** | 2026-06-26 21:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:57:10` | `cowrie.session.connect` |
| `2026-06-26 21:57:12` | `cowrie.client.version` |
| `2026-06-26 21:57:12` | `cowrie.client.kex` |
| `2026-06-26 21:57:18` | `cowrie.login.success` |
| `2026-06-26 21:57:22` | `cowrie.session.params` |
| `2026-06-26 21:57:22` | `cowrie.command.input` |
| `2026-06-26 21:57:24` | `cowrie.log.closed` |
| `2026-06-26 21:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa84999ee57e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:57 |
| **Last Seen** | 2026-06-26 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:57:26` | `cowrie.session.connect` |
| `2026-06-26 21:57:26` | `cowrie.client.version` |
| `2026-06-26 21:57:26` | `cowrie.client.kex` |
| `2026-06-26 21:57:26` | `cowrie.login.success` |
| `2026-06-26 21:57:27` | `cowrie.session.params` |
| `2026-06-26 21:57:27` | `cowrie.command.input` |
| `2026-06-26 21:57:27` | `cowrie.log.closed` |
| `2026-06-26 21:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e29b96ff9b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:58 |
| **Last Seen** | 2026-06-26 21:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:58:29` | `cowrie.session.connect` |
| `2026-06-26 21:58:29` | `cowrie.client.version` |
| `2026-06-26 21:58:29` | `cowrie.client.kex` |
| `2026-06-26 21:58:29` | `cowrie.login.success` |
| `2026-06-26 21:58:30` | `cowrie.session.params` |
| `2026-06-26 21:58:30` | `cowrie.command.input` |
| `2026-06-26 21:58:30` | `cowrie.log.closed` |
| `2026-06-26 21:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e851857e5be6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 21:59 |
| **Last Seen** | 2026-06-26 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 21:59:31` | `cowrie.session.connect` |
| `2026-06-26 21:59:31` | `cowrie.client.version` |
| `2026-06-26 21:59:31` | `cowrie.client.kex` |
| `2026-06-26 21:59:31` | `cowrie.login.success` |
| `2026-06-26 21:59:32` | `cowrie.session.params` |
| `2026-06-26 21:59:32` | `cowrie.command.input` |
| `2026-06-26 21:59:32` | `cowrie.log.closed` |
| `2026-06-26 21:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8df1a312936

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:00 |
| **Last Seen** | 2026-06-26 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:00:27` | `cowrie.session.connect` |
| `2026-06-26 22:00:27` | `cowrie.client.version` |
| `2026-06-26 22:00:27` | `cowrie.client.kex` |
| `2026-06-26 22:00:28` | `cowrie.login.success` |
| `2026-06-26 22:00:28` | `cowrie.session.params` |
| `2026-06-26 22:00:28` | `cowrie.command.input` |
| `2026-06-26 22:00:29` | `cowrie.log.closed` |
| `2026-06-26 22:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf5aa501857

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]90` |
| **First Seen** | 2026-06-26 22:01 |
| **Last Seen** | 2026-06-26 22:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:01:08` | `cowrie.session.connect` |
| `2026-06-26 22:01:08` | `cowrie.login.success` |
| `2026-06-26 22:01:09` | `cowrie.session.params` |
| `2026-06-26 22:01:09` | `cowrie.log.closed` |
| `2026-06-26 22:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]90` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d007fee9782

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:01 |
| **Last Seen** | 2026-06-26 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:01:15` | `cowrie.session.connect` |
| `2026-06-26 22:01:15` | `cowrie.client.version` |
| `2026-06-26 22:01:15` | `cowrie.client.kex` |
| `2026-06-26 22:01:15` | `cowrie.login.success` |
| `2026-06-26 22:01:16` | `cowrie.session.params` |
| `2026-06-26 22:01:16` | `cowrie.command.input` |
| `2026-06-26 22:01:16` | `cowrie.log.closed` |
| `2026-06-26 22:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570899b9870f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:02 |
| **Last Seen** | 2026-06-26 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:02:01` | `cowrie.session.connect` |
| `2026-06-26 22:02:01` | `cowrie.client.version` |
| `2026-06-26 22:02:01` | `cowrie.client.kex` |
| `2026-06-26 22:02:02` | `cowrie.login.success` |
| `2026-06-26 22:02:02` | `cowrie.session.params` |
| `2026-06-26 22:02:02` | `cowrie.command.input` |
| `2026-06-26 22:02:02` | `cowrie.log.closed` |
| `2026-06-26 22:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68c8b33da829

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:02 |
| **Last Seen** | 2026-06-26 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:02:49` | `cowrie.session.connect` |
| `2026-06-26 22:02:49` | `cowrie.client.version` |
| `2026-06-26 22:02:49` | `cowrie.client.kex` |
| `2026-06-26 22:02:49` | `cowrie.login.success` |
| `2026-06-26 22:02:50` | `cowrie.session.params` |
| `2026-06-26 22:02:50` | `cowrie.command.input` |
| `2026-06-26 22:02:50` | `cowrie.log.closed` |
| `2026-06-26 22:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02cabbc3661c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 22:03 |
| **Last Seen** | 2026-06-26 22:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:03:28` | `cowrie.session.connect` |
| `2026-06-26 22:03:29` | `cowrie.client.version` |
| `2026-06-26 22:03:29` | `cowrie.client.kex` |
| `2026-06-26 22:03:30` | `cowrie.login.success` |
| `2026-06-26 22:03:31` | `cowrie.session.params` |
| `2026-06-26 22:03:31` | `cowrie.command.input` |
| `2026-06-26 22:03:32` | `cowrie.log.closed` |
| `2026-06-26 22:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18642e5d02f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:03 |
| **Last Seen** | 2026-06-26 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:03:37` | `cowrie.session.connect` |
| `2026-06-26 22:03:37` | `cowrie.client.version` |
| `2026-06-26 22:03:37` | `cowrie.client.kex` |
| `2026-06-26 22:03:37` | `cowrie.login.success` |
| `2026-06-26 22:03:38` | `cowrie.session.params` |
| `2026-06-26 22:03:38` | `cowrie.command.input` |
| `2026-06-26 22:03:38` | `cowrie.log.closed` |
| `2026-06-26 22:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba71bbae1d99

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 22:04 |
| **Last Seen** | 2026-06-26 22:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:04:02` | `cowrie.session.connect` |
| `2026-06-26 22:04:02` | `cowrie.client.version` |
| `2026-06-26 22:04:02` | `cowrie.client.kex` |
| `2026-06-26 22:04:03` | `cowrie.login.success` |
| `2026-06-26 22:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d63adcc7938

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 22:04 |
| **Last Seen** | 2026-06-26 22:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:04:02` | `cowrie.session.connect` |
| `2026-06-26 22:04:02` | `cowrie.client.version` |
| `2026-06-26 22:04:02` | `cowrie.client.kex` |
| `2026-06-26 22:04:03` | `cowrie.login.success` |
| `2026-06-26 22:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758fb779af51

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 22:04 |
| **Last Seen** | 2026-06-26 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:04:08` | `cowrie.session.connect` |
| `2026-06-26 22:04:08` | `cowrie.client.version` |
| `2026-06-26 22:04:08` | `cowrie.client.kex` |
| `2026-06-26 22:04:08` | `cowrie.login.success` |
| `2026-06-26 22:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-685625426c9b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-26 22:04 |
| **Last Seen** | 2026-06-26 22:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:04:09` | `cowrie.session.connect` |
| `2026-06-26 22:04:09` | `cowrie.client.version` |
| `2026-06-26 22:04:09` | `cowrie.client.kex` |
| `2026-06-26 22:04:09` | `cowrie.login.success` |
| `2026-06-26 22:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a71d540cbe7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:04 |
| **Last Seen** | 2026-06-26 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:04:23` | `cowrie.session.connect` |
| `2026-06-26 22:04:23` | `cowrie.client.version` |
| `2026-06-26 22:04:23` | `cowrie.client.kex` |
| `2026-06-26 22:04:23` | `cowrie.login.success` |
| `2026-06-26 22:04:24` | `cowrie.session.params` |
| `2026-06-26 22:04:24` | `cowrie.command.input` |
| `2026-06-26 22:04:24` | `cowrie.log.closed` |
| `2026-06-26 22:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4e03f7563e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:05 |
| **Last Seen** | 2026-06-26 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:05:09` | `cowrie.session.connect` |
| `2026-06-26 22:05:09` | `cowrie.client.version` |
| `2026-06-26 22:05:09` | `cowrie.client.kex` |
| `2026-06-26 22:05:10` | `cowrie.login.success` |
| `2026-06-26 22:05:10` | `cowrie.session.params` |
| `2026-06-26 22:05:10` | `cowrie.command.input` |
| `2026-06-26 22:05:10` | `cowrie.log.closed` |
| `2026-06-26 22:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a92627004f1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:05 |
| **Last Seen** | 2026-06-26 22:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '111111' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:05:19` | `cowrie.session.connect` |
| `2026-06-26 22:05:20` | `cowrie.client.version` |
| `2026-06-26 22:05:20` | `cowrie.client.kex` |
| `2026-06-26 22:05:23` | `cowrie.login.success` |
| `2026-06-26 22:05:25` | `cowrie.session.params` |
| `2026-06-26 22:05:25` | `cowrie.command.input` |
| `2026-06-26 22:05:25` | `cowrie.command.input` |
| `2026-06-26 22:05:25` | `cowrie.command.input` |
| `2026-06-26 22:05:25` | `cowrie.command.input` |
| `2026-06-26 22:05:26` | `cowrie.log.closed` |
| `2026-06-26 22:05:28` | `cowrie.session.params` |
| `2026-06-26 22:05:28` | `cowrie.command.input` |
| `2026-06-26 22:05:28` | `cowrie.command.input` |
| `2026-06-26 22:05:28` | `cowrie.command.failed` |
| `2026-06-26 22:05:28` | `cowrie.command.failed` |
| `2026-06-26 22:05:28` | `cowrie.command.failed` |
| `2026-06-26 22:05:28` | `cowrie.command.failed` |
| `2026-06-26 22:05:29` | `cowrie.log.closed` |
| `2026-06-26 22:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210e63886005

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:05 |
| **Last Seen** | 2026-06-26 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:05:55` | `cowrie.session.connect` |
| `2026-06-26 22:05:55` | `cowrie.client.version` |
| `2026-06-26 22:05:55` | `cowrie.client.kex` |
| `2026-06-26 22:05:56` | `cowrie.login.success` |
| `2026-06-26 22:05:56` | `cowrie.session.params` |
| `2026-06-26 22:05:56` | `cowrie.command.input` |
| `2026-06-26 22:05:56` | `cowrie.log.closed` |
| `2026-06-26 22:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a1211ff4d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:06 |
| **Last Seen** | 2026-06-26 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:06:41` | `cowrie.session.connect` |
| `2026-06-26 22:06:41` | `cowrie.client.version` |
| `2026-06-26 22:06:42` | `cowrie.client.kex` |
| `2026-06-26 22:06:42` | `cowrie.login.success` |
| `2026-06-26 22:06:43` | `cowrie.session.params` |
| `2026-06-26 22:06:43` | `cowrie.command.input` |
| `2026-06-26 22:06:43` | `cowrie.log.closed` |
| `2026-06-26 22:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879ac0559d13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:07 |
| **Last Seen** | 2026-06-26 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:07:28` | `cowrie.session.connect` |
| `2026-06-26 22:07:28` | `cowrie.client.version` |
| `2026-06-26 22:07:28` | `cowrie.client.kex` |
| `2026-06-26 22:07:29` | `cowrie.login.success` |
| `2026-06-26 22:07:29` | `cowrie.session.params` |
| `2026-06-26 22:07:29` | `cowrie.command.input` |
| `2026-06-26 22:07:30` | `cowrie.log.closed` |
| `2026-06-26 22:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81acb38c8135

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:07 |
| **Last Seen** | 2026-06-26 22:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:07:41` | `cowrie.session.connect` |
| `2026-06-26 22:07:41` | `cowrie.client.version` |
| `2026-06-26 22:07:41` | `cowrie.client.kex` |
| `2026-06-26 22:07:44` | `cowrie.login.success` |
| `2026-06-26 22:07:46` | `cowrie.session.params` |
| `2026-06-26 22:07:46` | `cowrie.command.input` |
| `2026-06-26 22:07:46` | `cowrie.command.input` |
| `2026-06-26 22:07:46` | `cowrie.command.input` |
| `2026-06-26 22:07:46` | `cowrie.command.input` |
| `2026-06-26 22:07:47` | `cowrie.log.closed` |
| `2026-06-26 22:07:49` | `cowrie.session.params` |
| `2026-06-26 22:07:49` | `cowrie.command.input` |
| `2026-06-26 22:07:49` | `cowrie.command.input` |
| `2026-06-26 22:07:49` | `cowrie.command.failed` |
| `2026-06-26 22:07:49` | `cowrie.command.failed` |
| `2026-06-26 22:07:49` | `cowrie.command.failed` |
| `2026-06-26 22:07:49` | `cowrie.command.failed` |
| `2026-06-26 22:07:50` | `cowrie.log.closed` |
| `2026-06-26 22:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e052eca11634

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:08 |
| **Last Seen** | 2026-06-26 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:08:16` | `cowrie.session.connect` |
| `2026-06-26 22:08:16` | `cowrie.client.version` |
| `2026-06-26 22:08:16` | `cowrie.client.kex` |
| `2026-06-26 22:08:16` | `cowrie.login.success` |
| `2026-06-26 22:08:17` | `cowrie.session.params` |
| `2026-06-26 22:08:17` | `cowrie.command.input` |
| `2026-06-26 22:08:17` | `cowrie.log.closed` |
| `2026-06-26 22:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d59c01ce7df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:09 |
| **Last Seen** | 2026-06-26 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:09:04` | `cowrie.session.connect` |
| `2026-06-26 22:09:04` | `cowrie.client.version` |
| `2026-06-26 22:09:04` | `cowrie.client.kex` |
| `2026-06-26 22:09:04` | `cowrie.login.success` |
| `2026-06-26 22:09:05` | `cowrie.session.params` |
| `2026-06-26 22:09:05` | `cowrie.command.input` |
| `2026-06-26 22:09:05` | `cowrie.log.closed` |
| `2026-06-26 22:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee0fa180fb03

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 22:09 |
| **Last Seen** | 2026-06-26 22:09 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:09:44` | `cowrie.session.connect` |
| `2026-06-26 22:09:46` | `cowrie.client.version` |
| `2026-06-26 22:09:46` | `cowrie.client.kex` |
| `2026-06-26 22:09:53` | `cowrie.login.success` |
| `2026-06-26 22:09:57` | `cowrie.session.params` |
| `2026-06-26 22:09:57` | `cowrie.command.input` |
| `2026-06-26 22:09:59` | `cowrie.log.closed` |
| `2026-06-26 22:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b6cd40f865

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:09 |
| **Last Seen** | 2026-06-26 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:09:52` | `cowrie.session.connect` |
| `2026-06-26 22:09:52` | `cowrie.client.version` |
| `2026-06-26 22:09:52` | `cowrie.client.kex` |
| `2026-06-26 22:09:52` | `cowrie.login.success` |
| `2026-06-26 22:09:53` | `cowrie.session.params` |
| `2026-06-26 22:09:53` | `cowrie.command.input` |
| `2026-06-26 22:09:53` | `cowrie.log.closed` |
| `2026-06-26 22:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea87bf6967c1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:10 |
| **Last Seen** | 2026-06-26 22:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:10:07` | `cowrie.session.connect` |
| `2026-06-26 22:10:07` | `cowrie.client.version` |
| `2026-06-26 22:10:07` | `cowrie.client.kex` |
| `2026-06-26 22:10:10` | `cowrie.login.success` |
| `2026-06-26 22:10:12` | `cowrie.session.params` |
| `2026-06-26 22:10:12` | `cowrie.command.input` |
| `2026-06-26 22:10:12` | `cowrie.command.input` |
| `2026-06-26 22:10:12` | `cowrie.command.input` |
| `2026-06-26 22:10:12` | `cowrie.command.input` |
| `2026-06-26 22:10:13` | `cowrie.log.closed` |
| `2026-06-26 22:10:15` | `cowrie.session.params` |
| `2026-06-26 22:10:15` | `cowrie.command.input` |
| `2026-06-26 22:10:15` | `cowrie.command.input` |
| `2026-06-26 22:10:15` | `cowrie.command.failed` |
| `2026-06-26 22:10:15` | `cowrie.command.failed` |
| `2026-06-26 22:10:15` | `cowrie.command.failed` |
| `2026-06-26 22:10:15` | `cowrie.command.failed` |
| `2026-06-26 22:10:16` | `cowrie.log.closed` |
| `2026-06-26 22:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327978bd7eb7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:10 |
| **Last Seen** | 2026-06-26 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:10:39` | `cowrie.session.connect` |
| `2026-06-26 22:10:39` | `cowrie.client.version` |
| `2026-06-26 22:10:39` | `cowrie.client.kex` |
| `2026-06-26 22:10:39` | `cowrie.login.success` |
| `2026-06-26 22:10:40` | `cowrie.session.params` |
| `2026-06-26 22:10:40` | `cowrie.command.input` |
| `2026-06-26 22:10:40` | `cowrie.log.closed` |
| `2026-06-26 22:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b0794618ff

| Field | Detail |
|---|---|
| **Source IP** | `115.190.145[.]176` |
| **First Seen** | 2026-06-26 22:10 |
| **Last Seen** | 2026-06-26 22:11 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:10:44` | `cowrie.session.connect` |
| `2026-06-26 22:10:44` | `cowrie.client.version` |
| `2026-06-26 22:10:44` | `cowrie.client.kex` |
| `2026-06-26 22:11:11` | `cowrie.login.success` |
| `2026-06-26 22:11:22` | `cowrie.session.params` |
| `2026-06-26 22:11:22` | `cowrie.command.input` |
| `2026-06-26 22:11:23` | `cowrie.log.closed` |
| `2026-06-26 22:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.145[.]176` to AbuseIPDB if not already reported
- [ ] Block `115.190.145[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd502bd88c4e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:11 |
| **Last Seen** | 2026-06-26 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:11:25` | `cowrie.session.connect` |
| `2026-06-26 22:11:25` | `cowrie.client.version` |
| `2026-06-26 22:11:25` | `cowrie.client.kex` |
| `2026-06-26 22:11:25` | `cowrie.login.success` |
| `2026-06-26 22:11:26` | `cowrie.session.params` |
| `2026-06-26 22:11:26` | `cowrie.command.input` |
| `2026-06-26 22:11:26` | `cowrie.log.closed` |
| `2026-06-26 22:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e77f34b2a53a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:12 |
| **Last Seen** | 2026-06-26 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:12:10` | `cowrie.session.connect` |
| `2026-06-26 22:12:10` | `cowrie.client.version` |
| `2026-06-26 22:12:10` | `cowrie.client.kex` |
| `2026-06-26 22:12:10` | `cowrie.login.success` |
| `2026-06-26 22:12:11` | `cowrie.session.params` |
| `2026-06-26 22:12:11` | `cowrie.command.input` |
| `2026-06-26 22:12:11` | `cowrie.log.closed` |
| `2026-06-26 22:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380b18262b0c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:12 |
| **Last Seen** | 2026-06-26 22:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:12:22` | `cowrie.session.connect` |
| `2026-06-26 22:12:23` | `cowrie.client.version` |
| `2026-06-26 22:12:23` | `cowrie.client.kex` |
| `2026-06-26 22:12:25` | `cowrie.login.success` |
| `2026-06-26 22:12:26` | `cowrie.session.params` |
| `2026-06-26 22:12:26` | `cowrie.command.input` |
| `2026-06-26 22:12:26` | `cowrie.command.input` |
| `2026-06-26 22:12:26` | `cowrie.command.input` |
| `2026-06-26 22:12:26` | `cowrie.command.input` |
| `2026-06-26 22:12:27` | `cowrie.log.closed` |
| `2026-06-26 22:12:29` | `cowrie.session.params` |
| `2026-06-26 22:12:29` | `cowrie.command.input` |
| `2026-06-26 22:12:29` | `cowrie.command.input` |
| `2026-06-26 22:12:29` | `cowrie.command.failed` |
| `2026-06-26 22:12:29` | `cowrie.command.failed` |
| `2026-06-26 22:12:29` | `cowrie.command.failed` |
| `2026-06-26 22:12:29` | `cowrie.command.failed` |
| `2026-06-26 22:12:29` | `cowrie.log.closed` |
| `2026-06-26 22:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e74f9fd5dc3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:12 |
| **Last Seen** | 2026-06-26 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:12:57` | `cowrie.session.connect` |
| `2026-06-26 22:12:57` | `cowrie.client.version` |
| `2026-06-26 22:12:57` | `cowrie.client.kex` |
| `2026-06-26 22:12:57` | `cowrie.login.success` |
| `2026-06-26 22:12:58` | `cowrie.session.params` |
| `2026-06-26 22:12:58` | `cowrie.command.input` |
| `2026-06-26 22:12:58` | `cowrie.log.closed` |
| `2026-06-26 22:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01440eee9f99

| Field | Detail |
|---|---|
| **Source IP** | `64.227.0[.]95` |
| **First Seen** | 2026-06-26 22:12 |
| **Last Seen** | 2026-06-26 22:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:12:59` | `cowrie.session.connect` |
| `2026-06-26 22:13:00` | `cowrie.client.version` |
| `2026-06-26 22:13:00` | `cowrie.client.kex` |
| `2026-06-26 22:13:00` | `cowrie.login.success` |
| `2026-06-26 22:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.0[.]95` to AbuseIPDB if not already reported
- [ ] Block `64.227.0[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc54ea3c8f3

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-26 22:13 |
| **Last Seen** | 2026-06-26 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:13:00` | `cowrie.session.connect` |
| `2026-06-26 22:13:00` | `cowrie.client.version` |
| `2026-06-26 22:13:01` | `cowrie.client.kex` |
| `2026-06-26 22:13:01` | `cowrie.login.success` |
| `2026-06-26 22:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6929303d35c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:13 |
| **Last Seen** | 2026-06-26 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:13:44` | `cowrie.session.connect` |
| `2026-06-26 22:13:44` | `cowrie.client.version` |
| `2026-06-26 22:13:44` | `cowrie.client.kex` |
| `2026-06-26 22:13:45` | `cowrie.login.success` |
| `2026-06-26 22:13:45` | `cowrie.session.params` |
| `2026-06-26 22:13:45` | `cowrie.command.input` |
| `2026-06-26 22:13:45` | `cowrie.log.closed` |
| `2026-06-26 22:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7922a3e0ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:14 |
| **Last Seen** | 2026-06-26 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:14:32` | `cowrie.session.connect` |
| `2026-06-26 22:14:32` | `cowrie.client.version` |
| `2026-06-26 22:14:32` | `cowrie.client.kex` |
| `2026-06-26 22:14:32` | `cowrie.login.success` |
| `2026-06-26 22:14:33` | `cowrie.session.params` |
| `2026-06-26 22:14:33` | `cowrie.command.input` |
| `2026-06-26 22:14:33` | `cowrie.log.closed` |
| `2026-06-26 22:14:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201d4eeabf34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:15 |
| **Last Seen** | 2026-06-26 22:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:15:21` | `cowrie.session.connect` |
| `2026-06-26 22:15:21` | `cowrie.client.version` |
| `2026-06-26 22:15:21` | `cowrie.client.kex` |
| `2026-06-26 22:15:21` | `cowrie.login.success` |
| `2026-06-26 22:15:22` | `cowrie.session.params` |
| `2026-06-26 22:15:22` | `cowrie.command.input` |
| `2026-06-26 22:15:22` | `cowrie.log.closed` |
| `2026-06-26 22:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c97831b6370

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:16 |
| **Last Seen** | 2026-06-26 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:16:09` | `cowrie.session.connect` |
| `2026-06-26 22:16:09` | `cowrie.client.version` |
| `2026-06-26 22:16:09` | `cowrie.client.kex` |
| `2026-06-26 22:16:09` | `cowrie.login.success` |
| `2026-06-26 22:16:10` | `cowrie.session.params` |
| `2026-06-26 22:16:10` | `cowrie.command.input` |
| `2026-06-26 22:16:10` | `cowrie.log.closed` |
| `2026-06-26 22:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b154c8ce3edd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:16 |
| **Last Seen** | 2026-06-26 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:16:57` | `cowrie.session.connect` |
| `2026-06-26 22:16:57` | `cowrie.client.version` |
| `2026-06-26 22:16:57` | `cowrie.client.kex` |
| `2026-06-26 22:16:58` | `cowrie.login.success` |
| `2026-06-26 22:16:59` | `cowrie.session.params` |
| `2026-06-26 22:16:59` | `cowrie.command.input` |
| `2026-06-26 22:16:59` | `cowrie.log.closed` |
| `2026-06-26 22:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863b6cfdaeec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:17 |
| **Last Seen** | 2026-06-26 22:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:17:07` | `cowrie.session.connect` |
| `2026-06-26 22:17:08` | `cowrie.client.version` |
| `2026-06-26 22:17:08` | `cowrie.client.kex` |
| `2026-06-26 22:17:10` | `cowrie.login.success` |
| `2026-06-26 22:17:12` | `cowrie.session.params` |
| `2026-06-26 22:17:12` | `cowrie.command.input` |
| `2026-06-26 22:17:12` | `cowrie.command.input` |
| `2026-06-26 22:17:12` | `cowrie.command.input` |
| `2026-06-26 22:17:12` | `cowrie.command.input` |
| `2026-06-26 22:17:12` | `cowrie.log.closed` |
| `2026-06-26 22:17:14` | `cowrie.session.params` |
| `2026-06-26 22:17:14` | `cowrie.command.input` |
| `2026-06-26 22:17:14` | `cowrie.command.input` |
| `2026-06-26 22:17:14` | `cowrie.command.failed` |
| `2026-06-26 22:17:14` | `cowrie.command.failed` |
| `2026-06-26 22:17:14` | `cowrie.command.failed` |
| `2026-06-26 22:17:14` | `cowrie.command.failed` |
| `2026-06-26 22:17:15` | `cowrie.log.closed` |
| `2026-06-26 22:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe63bf7f21ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:17 |
| **Last Seen** | 2026-06-26 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:17:45` | `cowrie.session.connect` |
| `2026-06-26 22:17:45` | `cowrie.client.version` |
| `2026-06-26 22:17:45` | `cowrie.client.kex` |
| `2026-06-26 22:17:46` | `cowrie.login.success` |
| `2026-06-26 22:17:46` | `cowrie.session.params` |
| `2026-06-26 22:17:46` | `cowrie.command.input` |
| `2026-06-26 22:17:47` | `cowrie.log.closed` |
| `2026-06-26 22:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfc334cf0ba

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 22:18 |
| **Last Seen** | 2026-06-26 22:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:18:30` | `cowrie.session.connect` |
| `2026-06-26 22:18:31` | `cowrie.client.version` |
| `2026-06-26 22:18:31` | `cowrie.client.kex` |
| `2026-06-26 22:18:33` | `cowrie.login.success` |
| `2026-06-26 22:18:35` | `cowrie.session.params` |
| `2026-06-26 22:18:35` | `cowrie.command.input` |
| `2026-06-26 22:18:36` | `cowrie.log.closed` |
| `2026-06-26 22:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d7b0e4b5cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:18 |
| **Last Seen** | 2026-06-26 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:18:32` | `cowrie.session.connect` |
| `2026-06-26 22:18:32` | `cowrie.client.version` |
| `2026-06-26 22:18:32` | `cowrie.client.kex` |
| `2026-06-26 22:18:33` | `cowrie.login.success` |
| `2026-06-26 22:18:33` | `cowrie.session.params` |
| `2026-06-26 22:18:33` | `cowrie.command.input` |
| `2026-06-26 22:18:34` | `cowrie.log.closed` |
| `2026-06-26 22:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8098a025b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:19 |
| **Last Seen** | 2026-06-26 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:19:19` | `cowrie.session.connect` |
| `2026-06-26 22:19:19` | `cowrie.client.version` |
| `2026-06-26 22:19:19` | `cowrie.client.kex` |
| `2026-06-26 22:19:20` | `cowrie.login.success` |
| `2026-06-26 22:19:21` | `cowrie.session.params` |
| `2026-06-26 22:19:21` | `cowrie.command.input` |
| `2026-06-26 22:19:21` | `cowrie.log.closed` |
| `2026-06-26 22:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338853e6e5c0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:19 |
| **Last Seen** | 2026-06-26 22:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:19:31` | `cowrie.session.connect` |
| `2026-06-26 22:19:31` | `cowrie.client.version` |
| `2026-06-26 22:19:31` | `cowrie.client.kex` |
| `2026-06-26 22:19:33` | `cowrie.login.success` |
| `2026-06-26 22:19:34` | `cowrie.session.params` |
| `2026-06-26 22:19:34` | `cowrie.command.input` |
| `2026-06-26 22:19:34` | `cowrie.command.input` |
| `2026-06-26 22:19:34` | `cowrie.command.input` |
| `2026-06-26 22:19:34` | `cowrie.command.input` |
| `2026-06-26 22:19:35` | `cowrie.log.closed` |
| `2026-06-26 22:19:36` | `cowrie.session.params` |
| `2026-06-26 22:19:36` | `cowrie.command.input` |
| `2026-06-26 22:19:36` | `cowrie.command.input` |
| `2026-06-26 22:19:36` | `cowrie.command.failed` |
| `2026-06-26 22:19:36` | `cowrie.command.failed` |
| `2026-06-26 22:19:36` | `cowrie.command.failed` |
| `2026-06-26 22:19:36` | `cowrie.command.failed` |
| `2026-06-26 22:19:37` | `cowrie.log.closed` |
| `2026-06-26 22:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6d71a3ce02

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:20 |
| **Last Seen** | 2026-06-26 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:20:07` | `cowrie.session.connect` |
| `2026-06-26 22:20:07` | `cowrie.client.version` |
| `2026-06-26 22:20:07` | `cowrie.client.kex` |
| `2026-06-26 22:20:08` | `cowrie.login.success` |
| `2026-06-26 22:20:08` | `cowrie.session.params` |
| `2026-06-26 22:20:08` | `cowrie.command.input` |
| `2026-06-26 22:20:09` | `cowrie.log.closed` |
| `2026-06-26 22:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7bb950717e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:20 |
| **Last Seen** | 2026-06-26 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:20:56` | `cowrie.session.connect` |
| `2026-06-26 22:20:56` | `cowrie.client.version` |
| `2026-06-26 22:20:56` | `cowrie.client.kex` |
| `2026-06-26 22:20:56` | `cowrie.login.success` |
| `2026-06-26 22:20:57` | `cowrie.session.params` |
| `2026-06-26 22:20:57` | `cowrie.command.input` |
| `2026-06-26 22:20:57` | `cowrie.log.closed` |
| `2026-06-26 22:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93202f5a2e2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:21 |
| **Last Seen** | 2026-06-26 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:21:44` | `cowrie.session.connect` |
| `2026-06-26 22:21:44` | `cowrie.client.version` |
| `2026-06-26 22:21:45` | `cowrie.client.kex` |
| `2026-06-26 22:21:45` | `cowrie.login.success` |
| `2026-06-26 22:21:46` | `cowrie.session.params` |
| `2026-06-26 22:21:46` | `cowrie.command.input` |
| `2026-06-26 22:21:46` | `cowrie.log.closed` |
| `2026-06-26 22:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59211915bab0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:21 |
| **Last Seen** | 2026-06-26 22:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'Password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:21:59` | `cowrie.session.connect` |
| `2026-06-26 22:21:59` | `cowrie.client.version` |
| `2026-06-26 22:21:59` | `cowrie.client.kex` |
| `2026-06-26 22:22:02` | `cowrie.login.success` |
| `2026-06-26 22:22:02` | `cowrie.session.params` |
| `2026-06-26 22:22:02` | `cowrie.command.input` |
| `2026-06-26 22:22:02` | `cowrie.command.input` |
| `2026-06-26 22:22:02` | `cowrie.command.input` |
| `2026-06-26 22:22:02` | `cowrie.command.input` |
| `2026-06-26 22:22:03` | `cowrie.log.closed` |
| `2026-06-26 22:22:04` | `cowrie.session.params` |
| `2026-06-26 22:22:04` | `cowrie.command.input` |
| `2026-06-26 22:22:04` | `cowrie.command.input` |
| `2026-06-26 22:22:04` | `cowrie.command.failed` |
| `2026-06-26 22:22:04` | `cowrie.command.failed` |
| `2026-06-26 22:22:04` | `cowrie.command.failed` |
| `2026-06-26 22:22:04` | `cowrie.command.failed` |
| `2026-06-26 22:22:05` | `cowrie.log.closed` |
| `2026-06-26 22:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57cf2bef0696

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 22:22 |
| **Last Seen** | 2026-06-26 22:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:22:10` | `cowrie.session.connect` |
| `2026-06-26 22:22:11` | `cowrie.client.version` |
| `2026-06-26 22:22:11` | `cowrie.client.kex` |
| `2026-06-26 22:22:18` | `cowrie.login.success` |
| `2026-06-26 22:22:21` | `cowrie.session.params` |
| `2026-06-26 22:22:21` | `cowrie.command.input` |
| `2026-06-26 22:22:22` | `cowrie.log.closed` |
| `2026-06-26 22:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab1b2c6fab1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:22 |
| **Last Seen** | 2026-06-26 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:22:33` | `cowrie.session.connect` |
| `2026-06-26 22:22:33` | `cowrie.client.version` |
| `2026-06-26 22:22:34` | `cowrie.client.kex` |
| `2026-06-26 22:22:34` | `cowrie.login.success` |
| `2026-06-26 22:22:35` | `cowrie.session.params` |
| `2026-06-26 22:22:35` | `cowrie.command.input` |
| `2026-06-26 22:22:35` | `cowrie.log.closed` |
| `2026-06-26 22:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04400efad40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:23 |
| **Last Seen** | 2026-06-26 22:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:23:21` | `cowrie.session.connect` |
| `2026-06-26 22:23:21` | `cowrie.client.version` |
| `2026-06-26 22:23:21` | `cowrie.client.kex` |
| `2026-06-26 22:23:22` | `cowrie.login.success` |
| `2026-06-26 22:23:23` | `cowrie.session.params` |
| `2026-06-26 22:23:23` | `cowrie.command.input` |
| `2026-06-26 22:23:23` | `cowrie.log.closed` |
| `2026-06-26 22:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b7614ba248

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:24 |
| **Last Seen** | 2026-06-26 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:24:09` | `cowrie.session.connect` |
| `2026-06-26 22:24:09` | `cowrie.client.version` |
| `2026-06-26 22:24:09` | `cowrie.client.kex` |
| `2026-06-26 22:24:09` | `cowrie.login.success` |
| `2026-06-26 22:24:10` | `cowrie.session.params` |
| `2026-06-26 22:24:10` | `cowrie.command.input` |
| `2026-06-26 22:24:10` | `cowrie.log.closed` |
| `2026-06-26 22:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f60e919831

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-06-26 22:24 |
| **Last Seen** | 2026-06-26 22:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:24:29` | `cowrie.session.connect` |
| `2026-06-26 22:24:29` | `cowrie.client.version` |
| `2026-06-26 22:24:29` | `cowrie.client.kex` |
| `2026-06-26 22:24:30` | `cowrie.login.success` |
| `2026-06-26 22:24:32` | `cowrie.session.params` |
| `2026-06-26 22:24:32` | `cowrie.command.input` |
| `2026-06-26 22:24:32` | `cowrie.command.input` |
| `2026-06-26 22:24:32` | `cowrie.command.input` |
| `2026-06-26 22:24:32` | `cowrie.command.input` |
| `2026-06-26 22:24:32` | `cowrie.log.closed` |
| `2026-06-26 22:24:33` | `cowrie.session.params` |
| `2026-06-26 22:24:33` | `cowrie.command.input` |
| `2026-06-26 22:24:33` | `cowrie.command.input` |
| `2026-06-26 22:24:33` | `cowrie.command.failed` |
| `2026-06-26 22:24:33` | `cowrie.command.failed` |
| `2026-06-26 22:24:33` | `cowrie.command.failed` |
| `2026-06-26 22:24:33` | `cowrie.command.failed` |
| `2026-06-26 22:24:34` | `cowrie.log.closed` |
| `2026-06-26 22:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499b4c690625

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:24 |
| **Last Seen** | 2026-06-26 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:24:56` | `cowrie.session.connect` |
| `2026-06-26 22:24:56` | `cowrie.client.version` |
| `2026-06-26 22:24:56` | `cowrie.client.kex` |
| `2026-06-26 22:24:56` | `cowrie.login.success` |
| `2026-06-26 22:24:57` | `cowrie.session.params` |
| `2026-06-26 22:24:57` | `cowrie.command.input` |
| `2026-06-26 22:24:57` | `cowrie.log.closed` |
| `2026-06-26 22:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f4f94819d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:25 |
| **Last Seen** | 2026-06-26 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:25:43` | `cowrie.session.connect` |
| `2026-06-26 22:25:43` | `cowrie.client.version` |
| `2026-06-26 22:25:43` | `cowrie.client.kex` |
| `2026-06-26 22:25:44` | `cowrie.login.success` |
| `2026-06-26 22:25:44` | `cowrie.session.params` |
| `2026-06-26 22:25:44` | `cowrie.command.input` |
| `2026-06-26 22:25:45` | `cowrie.log.closed` |
| `2026-06-26 22:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23fef7b3af60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:26 |
| **Last Seen** | 2026-06-26 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:26:32` | `cowrie.session.connect` |
| `2026-06-26 22:26:32` | `cowrie.client.version` |
| `2026-06-26 22:26:32` | `cowrie.client.kex` |
| `2026-06-26 22:26:32` | `cowrie.login.success` |
| `2026-06-26 22:26:33` | `cowrie.session.params` |
| `2026-06-26 22:26:33` | `cowrie.command.input` |
| `2026-06-26 22:26:33` | `cowrie.log.closed` |
| `2026-06-26 22:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c928529d82f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:27 |
| **Last Seen** | 2026-06-26 22:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:27:22` | `cowrie.session.connect` |
| `2026-06-26 22:27:22` | `cowrie.client.version` |
| `2026-06-26 22:27:22` | `cowrie.client.kex` |
| `2026-06-26 22:27:22` | `cowrie.login.success` |
| `2026-06-26 22:27:23` | `cowrie.session.params` |
| `2026-06-26 22:27:23` | `cowrie.command.input` |
| `2026-06-26 22:27:23` | `cowrie.log.closed` |
| `2026-06-26 22:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-167fcb8c2ef7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:28 |
| **Last Seen** | 2026-06-26 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:28:13` | `cowrie.session.connect` |
| `2026-06-26 22:28:13` | `cowrie.client.version` |
| `2026-06-26 22:28:13` | `cowrie.client.kex` |
| `2026-06-26 22:28:13` | `cowrie.login.success` |
| `2026-06-26 22:28:14` | `cowrie.session.params` |
| `2026-06-26 22:28:14` | `cowrie.command.input` |
| `2026-06-26 22:28:14` | `cowrie.log.closed` |
| `2026-06-26 22:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b00674336d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:29 |
| **Last Seen** | 2026-06-26 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:29:04` | `cowrie.session.connect` |
| `2026-06-26 22:29:04` | `cowrie.client.version` |
| `2026-06-26 22:29:04` | `cowrie.client.kex` |
| `2026-06-26 22:29:05` | `cowrie.login.success` |
| `2026-06-26 22:29:06` | `cowrie.session.params` |
| `2026-06-26 22:29:06` | `cowrie.command.input` |
| `2026-06-26 22:29:06` | `cowrie.log.closed` |
| `2026-06-26 22:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45ac27ddac6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:29 |
| **Last Seen** | 2026-06-26 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:29:54` | `cowrie.session.connect` |
| `2026-06-26 22:29:54` | `cowrie.client.version` |
| `2026-06-26 22:29:54` | `cowrie.client.kex` |
| `2026-06-26 22:29:54` | `cowrie.login.success` |
| `2026-06-26 22:29:55` | `cowrie.session.params` |
| `2026-06-26 22:29:55` | `cowrie.command.input` |
| `2026-06-26 22:29:55` | `cowrie.log.closed` |
| `2026-06-26 22:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e5c592829d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:30 |
| **Last Seen** | 2026-06-26 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:30:43` | `cowrie.session.connect` |
| `2026-06-26 22:30:43` | `cowrie.client.version` |
| `2026-06-26 22:30:43` | `cowrie.client.kex` |
| `2026-06-26 22:30:44` | `cowrie.login.success` |
| `2026-06-26 22:30:44` | `cowrie.session.params` |
| `2026-06-26 22:30:44` | `cowrie.command.input` |
| `2026-06-26 22:30:45` | `cowrie.log.closed` |
| `2026-06-26 22:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e0cc0b1b03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:31 |
| **Last Seen** | 2026-06-26 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:31:32` | `cowrie.session.connect` |
| `2026-06-26 22:31:32` | `cowrie.client.version` |
| `2026-06-26 22:31:32` | `cowrie.client.kex` |
| `2026-06-26 22:31:32` | `cowrie.login.success` |
| `2026-06-26 22:31:33` | `cowrie.session.params` |
| `2026-06-26 22:31:33` | `cowrie.command.input` |
| `2026-06-26 22:31:33` | `cowrie.log.closed` |
| `2026-06-26 22:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9a918fecc4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:32 |
| **Last Seen** | 2026-06-26 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:32:21` | `cowrie.session.connect` |
| `2026-06-26 22:32:21` | `cowrie.client.version` |
| `2026-06-26 22:32:21` | `cowrie.client.kex` |
| `2026-06-26 22:32:21` | `cowrie.login.success` |
| `2026-06-26 22:32:22` | `cowrie.session.params` |
| `2026-06-26 22:32:22` | `cowrie.command.input` |
| `2026-06-26 22:32:22` | `cowrie.log.closed` |
| `2026-06-26 22:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489a09bd3222

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:33 |
| **Last Seen** | 2026-06-26 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:33:10` | `cowrie.session.connect` |
| `2026-06-26 22:33:10` | `cowrie.client.version` |
| `2026-06-26 22:33:11` | `cowrie.client.kex` |
| `2026-06-26 22:33:11` | `cowrie.login.success` |
| `2026-06-26 22:33:12` | `cowrie.session.params` |
| `2026-06-26 22:33:12` | `cowrie.command.input` |
| `2026-06-26 22:33:12` | `cowrie.log.closed` |
| `2026-06-26 22:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c507be4158fa

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 22:33 |
| **Last Seen** | 2026-06-26 22:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:33:29` | `cowrie.session.connect` |
| `2026-06-26 22:33:30` | `cowrie.client.version` |
| `2026-06-26 22:33:30` | `cowrie.client.kex` |
| `2026-06-26 22:33:32` | `cowrie.login.success` |
| `2026-06-26 22:33:33` | `cowrie.session.params` |
| `2026-06-26 22:33:33` | `cowrie.command.input` |
| `2026-06-26 22:33:34` | `cowrie.log.closed` |
| `2026-06-26 22:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b8187c02cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:34 |
| **Last Seen** | 2026-06-26 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:34:01` | `cowrie.session.connect` |
| `2026-06-26 22:34:01` | `cowrie.client.version` |
| `2026-06-26 22:34:01` | `cowrie.client.kex` |
| `2026-06-26 22:34:02` | `cowrie.login.success` |
| `2026-06-26 22:34:02` | `cowrie.session.params` |
| `2026-06-26 22:34:02` | `cowrie.command.input` |
| `2026-06-26 22:34:03` | `cowrie.log.closed` |
| `2026-06-26 22:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b90d750038

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 22:34 |
| **Last Seen** | 2026-06-26 22:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:34:19` | `cowrie.session.connect` |
| `2026-06-26 22:34:20` | `cowrie.client.version` |
| `2026-06-26 22:34:20` | `cowrie.client.kex` |
| `2026-06-26 22:34:26` | `cowrie.login.success` |
| `2026-06-26 22:34:30` | `cowrie.session.params` |
| `2026-06-26 22:34:30` | `cowrie.command.input` |
| `2026-06-26 22:34:32` | `cowrie.log.closed` |
| `2026-06-26 22:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e746e39799

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:34 |
| **Last Seen** | 2026-06-26 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:34:53` | `cowrie.session.connect` |
| `2026-06-26 22:34:53` | `cowrie.client.version` |
| `2026-06-26 22:34:53` | `cowrie.client.kex` |
| `2026-06-26 22:34:53` | `cowrie.login.success` |
| `2026-06-26 22:34:54` | `cowrie.session.params` |
| `2026-06-26 22:34:54` | `cowrie.command.input` |
| `2026-06-26 22:34:54` | `cowrie.log.closed` |
| `2026-06-26 22:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1795089ea9d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:35 |
| **Last Seen** | 2026-06-26 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:35:44` | `cowrie.session.connect` |
| `2026-06-26 22:35:44` | `cowrie.client.version` |
| `2026-06-26 22:35:44` | `cowrie.client.kex` |
| `2026-06-26 22:35:44` | `cowrie.login.success` |
| `2026-06-26 22:35:45` | `cowrie.session.params` |
| `2026-06-26 22:35:45` | `cowrie.command.input` |
| `2026-06-26 22:35:45` | `cowrie.log.closed` |
| `2026-06-26 22:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35499a3a4651

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:36 |
| **Last Seen** | 2026-06-26 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:36:34` | `cowrie.session.connect` |
| `2026-06-26 22:36:34` | `cowrie.client.version` |
| `2026-06-26 22:36:34` | `cowrie.client.kex` |
| `2026-06-26 22:36:34` | `cowrie.login.success` |
| `2026-06-26 22:36:35` | `cowrie.session.params` |
| `2026-06-26 22:36:35` | `cowrie.command.input` |
| `2026-06-26 22:36:35` | `cowrie.log.closed` |
| `2026-06-26 22:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7733a9811e53

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-26 22:36 |
| **Last Seen** | 2026-06-26 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:36:35` | `cowrie.session.connect` |
| `2026-06-26 22:36:35` | `cowrie.client.version` |
| `2026-06-26 22:36:35` | `cowrie.client.kex` |
| `2026-06-26 22:36:36` | `cowrie.login.success` |
| `2026-06-26 22:36:37` | `cowrie.session.params` |
| `2026-06-26 22:36:37` | `cowrie.command.input` |
| `2026-06-26 22:36:37` | `cowrie.log.closed` |
| `2026-06-26 22:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1a0185ecd5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:37 |
| **Last Seen** | 2026-06-26 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:37:23` | `cowrie.session.connect` |
| `2026-06-26 22:37:23` | `cowrie.client.version` |
| `2026-06-26 22:37:23` | `cowrie.client.kex` |
| `2026-06-26 22:37:24` | `cowrie.login.success` |
| `2026-06-26 22:37:25` | `cowrie.session.params` |
| `2026-06-26 22:37:25` | `cowrie.command.input` |
| `2026-06-26 22:37:25` | `cowrie.log.closed` |
| `2026-06-26 22:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c39a4e0c5c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:38 |
| **Last Seen** | 2026-06-26 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:38:12` | `cowrie.session.connect` |
| `2026-06-26 22:38:12` | `cowrie.client.version` |
| `2026-06-26 22:38:12` | `cowrie.client.kex` |
| `2026-06-26 22:38:12` | `cowrie.login.success` |
| `2026-06-26 22:38:13` | `cowrie.session.params` |
| `2026-06-26 22:38:13` | `cowrie.command.input` |
| `2026-06-26 22:38:13` | `cowrie.log.closed` |
| `2026-06-26 22:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f677d98fe2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:39 |
| **Last Seen** | 2026-06-26 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:39:02` | `cowrie.session.connect` |
| `2026-06-26 22:39:02` | `cowrie.client.version` |
| `2026-06-26 22:39:02` | `cowrie.client.kex` |
| `2026-06-26 22:39:03` | `cowrie.login.success` |
| `2026-06-26 22:39:04` | `cowrie.session.params` |
| `2026-06-26 22:39:04` | `cowrie.command.input` |
| `2026-06-26 22:39:04` | `cowrie.log.closed` |
| `2026-06-26 22:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d57d224adb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:39 |
| **Last Seen** | 2026-06-26 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:39:53` | `cowrie.session.connect` |
| `2026-06-26 22:39:53` | `cowrie.client.version` |
| `2026-06-26 22:39:53` | `cowrie.client.kex` |
| `2026-06-26 22:39:54` | `cowrie.login.success` |
| `2026-06-26 22:39:54` | `cowrie.session.params` |
| `2026-06-26 22:39:54` | `cowrie.command.input` |
| `2026-06-26 22:39:55` | `cowrie.log.closed` |
| `2026-06-26 22:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdac9c63faea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:40 |
| **Last Seen** | 2026-06-26 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:40:45` | `cowrie.session.connect` |
| `2026-06-26 22:40:45` | `cowrie.client.version` |
| `2026-06-26 22:40:45` | `cowrie.client.kex` |
| `2026-06-26 22:40:45` | `cowrie.login.success` |
| `2026-06-26 22:40:46` | `cowrie.session.params` |
| `2026-06-26 22:40:46` | `cowrie.command.input` |
| `2026-06-26 22:40:46` | `cowrie.log.closed` |
| `2026-06-26 22:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e941a2f0fd1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:41 |
| **Last Seen** | 2026-06-26 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:41:37` | `cowrie.session.connect` |
| `2026-06-26 22:41:37` | `cowrie.client.version` |
| `2026-06-26 22:41:37` | `cowrie.client.kex` |
| `2026-06-26 22:41:37` | `cowrie.login.success` |
| `2026-06-26 22:41:38` | `cowrie.session.params` |
| `2026-06-26 22:41:38` | `cowrie.command.input` |
| `2026-06-26 22:41:38` | `cowrie.log.closed` |
| `2026-06-26 22:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ac21393770

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:42 |
| **Last Seen** | 2026-06-26 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:42:28` | `cowrie.session.connect` |
| `2026-06-26 22:42:28` | `cowrie.client.version` |
| `2026-06-26 22:42:28` | `cowrie.client.kex` |
| `2026-06-26 22:42:28` | `cowrie.login.success` |
| `2026-06-26 22:42:29` | `cowrie.session.params` |
| `2026-06-26 22:42:29` | `cowrie.command.input` |
| `2026-06-26 22:42:29` | `cowrie.log.closed` |
| `2026-06-26 22:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669302253ed2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:43 |
| **Last Seen** | 2026-06-26 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:43:19` | `cowrie.session.connect` |
| `2026-06-26 22:43:19` | `cowrie.client.version` |
| `2026-06-26 22:43:19` | `cowrie.client.kex` |
| `2026-06-26 22:43:19` | `cowrie.login.success` |
| `2026-06-26 22:43:20` | `cowrie.session.params` |
| `2026-06-26 22:43:20` | `cowrie.command.input` |
| `2026-06-26 22:43:20` | `cowrie.log.closed` |
| `2026-06-26 22:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbd0a6fb7fb2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:44 |
| **Last Seen** | 2026-06-26 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:44:08` | `cowrie.session.connect` |
| `2026-06-26 22:44:08` | `cowrie.client.version` |
| `2026-06-26 22:44:08` | `cowrie.client.kex` |
| `2026-06-26 22:44:09` | `cowrie.login.success` |
| `2026-06-26 22:44:09` | `cowrie.session.params` |
| `2026-06-26 22:44:10` | `cowrie.command.input` |
| `2026-06-26 22:44:10` | `cowrie.log.closed` |
| `2026-06-26 22:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d158657272e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:44 |
| **Last Seen** | 2026-06-26 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:44:59` | `cowrie.session.connect` |
| `2026-06-26 22:44:59` | `cowrie.client.version` |
| `2026-06-26 22:45:00` | `cowrie.client.kex` |
| `2026-06-26 22:45:00` | `cowrie.login.success` |
| `2026-06-26 22:45:00` | `cowrie.session.params` |
| `2026-06-26 22:45:00` | `cowrie.command.input` |
| `2026-06-26 22:45:01` | `cowrie.log.closed` |
| `2026-06-26 22:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46d13238b24

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:45 |
| **Last Seen** | 2026-06-26 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:45:51` | `cowrie.session.connect` |
| `2026-06-26 22:45:51` | `cowrie.client.version` |
| `2026-06-26 22:45:51` | `cowrie.client.kex` |
| `2026-06-26 22:45:52` | `cowrie.login.success` |
| `2026-06-26 22:45:53` | `cowrie.session.params` |
| `2026-06-26 22:45:53` | `cowrie.command.input` |
| `2026-06-26 22:45:53` | `cowrie.log.closed` |
| `2026-06-26 22:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99a0e5e11989

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:46 |
| **Last Seen** | 2026-06-26 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:46:41` | `cowrie.session.connect` |
| `2026-06-26 22:46:41` | `cowrie.client.version` |
| `2026-06-26 22:46:41` | `cowrie.client.kex` |
| `2026-06-26 22:46:41` | `cowrie.login.success` |
| `2026-06-26 22:46:42` | `cowrie.session.params` |
| `2026-06-26 22:46:42` | `cowrie.command.input` |
| `2026-06-26 22:46:42` | `cowrie.log.closed` |
| `2026-06-26 22:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b50d3f92eb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-26 22:46 |
| **Last Seen** | 2026-06-26 22:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:46:45` | `cowrie.session.connect` |
| `2026-06-26 22:46:46` | `cowrie.client.version` |
| `2026-06-26 22:46:46` | `cowrie.client.kex` |
| `2026-06-26 22:46:52` | `cowrie.login.success` |
| `2026-06-26 22:46:55` | `cowrie.session.params` |
| `2026-06-26 22:46:55` | `cowrie.command.input` |
| `2026-06-26 22:46:56` | `cowrie.log.closed` |
| `2026-06-26 22:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1a2e9d1222

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:47 |
| **Last Seen** | 2026-06-26 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:47:31` | `cowrie.session.connect` |
| `2026-06-26 22:47:31` | `cowrie.client.version` |
| `2026-06-26 22:47:31` | `cowrie.client.kex` |
| `2026-06-26 22:47:31` | `cowrie.login.success` |
| `2026-06-26 22:47:32` | `cowrie.session.params` |
| `2026-06-26 22:47:32` | `cowrie.command.input` |
| `2026-06-26 22:47:32` | `cowrie.log.closed` |
| `2026-06-26 22:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a8fedc4250

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:48 |
| **Last Seen** | 2026-06-26 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:48:21` | `cowrie.session.connect` |
| `2026-06-26 22:48:21` | `cowrie.client.version` |
| `2026-06-26 22:48:21` | `cowrie.client.kex` |
| `2026-06-26 22:48:21` | `cowrie.login.success` |
| `2026-06-26 22:48:22` | `cowrie.session.params` |
| `2026-06-26 22:48:22` | `cowrie.command.input` |
| `2026-06-26 22:48:22` | `cowrie.log.closed` |
| `2026-06-26 22:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c7f1edf5551

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-26 22:48 |
| **Last Seen** | 2026-06-26 22:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:48:23` | `cowrie.session.connect` |
| `2026-06-26 22:48:24` | `cowrie.client.version` |
| `2026-06-26 22:48:24` | `cowrie.client.kex` |
| `2026-06-26 22:48:26` | `cowrie.login.success` |
| `2026-06-26 22:48:27` | `cowrie.session.params` |
| `2026-06-26 22:48:27` | `cowrie.command.input` |
| `2026-06-26 22:48:27` | `cowrie.log.closed` |
| `2026-06-26 22:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2c7be4134e2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:49 |
| **Last Seen** | 2026-06-26 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:49:11` | `cowrie.session.connect` |
| `2026-06-26 22:49:11` | `cowrie.client.version` |
| `2026-06-26 22:49:11` | `cowrie.client.kex` |
| `2026-06-26 22:49:11` | `cowrie.login.success` |
| `2026-06-26 22:49:12` | `cowrie.session.params` |
| `2026-06-26 22:49:12` | `cowrie.command.input` |
| `2026-06-26 22:49:12` | `cowrie.log.closed` |
| `2026-06-26 22:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952e688781ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:50 |
| **Last Seen** | 2026-06-26 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:50:00` | `cowrie.session.connect` |
| `2026-06-26 22:50:00` | `cowrie.client.version` |
| `2026-06-26 22:50:00` | `cowrie.client.kex` |
| `2026-06-26 22:50:00` | `cowrie.login.success` |
| `2026-06-26 22:50:01` | `cowrie.session.params` |
| `2026-06-26 22:50:01` | `cowrie.command.input` |
| `2026-06-26 22:50:01` | `cowrie.log.closed` |
| `2026-06-26 22:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b7a927fa892

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:50 |
| **Last Seen** | 2026-06-26 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:50:52` | `cowrie.session.connect` |
| `2026-06-26 22:50:52` | `cowrie.client.version` |
| `2026-06-26 22:50:53` | `cowrie.client.kex` |
| `2026-06-26 22:50:53` | `cowrie.login.success` |
| `2026-06-26 22:50:54` | `cowrie.session.params` |
| `2026-06-26 22:50:54` | `cowrie.command.input` |
| `2026-06-26 22:50:54` | `cowrie.log.closed` |
| `2026-06-26 22:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605d5dbe0431

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:51 |
| **Last Seen** | 2026-06-26 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:51:43` | `cowrie.session.connect` |
| `2026-06-26 22:51:43` | `cowrie.client.version` |
| `2026-06-26 22:51:43` | `cowrie.client.kex` |
| `2026-06-26 22:51:43` | `cowrie.login.success` |
| `2026-06-26 22:51:44` | `cowrie.session.params` |
| `2026-06-26 22:51:44` | `cowrie.command.input` |
| `2026-06-26 22:51:44` | `cowrie.log.closed` |
| `2026-06-26 22:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b8d7919f1de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:52 |
| **Last Seen** | 2026-06-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:52:36` | `cowrie.session.connect` |
| `2026-06-26 22:52:36` | `cowrie.client.version` |
| `2026-06-26 22:52:36` | `cowrie.client.kex` |
| `2026-06-26 22:52:36` | `cowrie.login.success` |
| `2026-06-26 22:52:37` | `cowrie.session.params` |
| `2026-06-26 22:52:37` | `cowrie.command.input` |
| `2026-06-26 22:52:37` | `cowrie.log.closed` |
| `2026-06-26 22:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3602be353b33

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:53 |
| **Last Seen** | 2026-06-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:53:30` | `cowrie.session.connect` |
| `2026-06-26 22:53:30` | `cowrie.client.version` |
| `2026-06-26 22:53:30` | `cowrie.client.kex` |
| `2026-06-26 22:53:30` | `cowrie.login.success` |
| `2026-06-26 22:53:31` | `cowrie.session.params` |
| `2026-06-26 22:53:31` | `cowrie.command.input` |
| `2026-06-26 22:53:31` | `cowrie.log.closed` |
| `2026-06-26 22:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b2ec65f44c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-26 22:54 |
| **Last Seen** | 2026-06-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-26 22:54:22` | `cowrie.session.connect` |
| `2026-06-26 22:54:22` | `cowrie.client.version` |
| `2026-06-26 22:54:22` | `cowrie.client.kex` |
| `2026-06-26 22:54:22` | `cowrie.login.success` |
| `2026-06-26 22:54:23` | `cowrie.session.params` |
| `2026-06-26 22:54:23` | `cowrie.command.input` |
| `2026-06-26 22:54:23` | `cowrie.log.closed` |
| `2026-06-26 22:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `209.99.185[.]59` | **136** | 2026-06-26 20:55 | 2026-06-26 22:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `104.238.81[.]133` | **10** | 2026-06-26 21:12 | 2026-06-26 22:42 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.19.117[.]129` | **2** | 2026-06-26 21:42 | 2026-06-26 22:41 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]217` | **2** | 2026-06-26 21:08 | 2026-06-26 21:13 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.3.114[.]90` | **2** | 2026-06-26 22:40 | 2026-06-26 22:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `209.141.46[.]66` | **2** | 2026-06-26 22:14 | 2026-06-26 22:25 | 1m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-06-26 21:58 | 2026-06-26 22:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.145[.]176` | 1 | 2026-06-26 22:10 | 2026-06-26 22:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.72.195[.]41` | 1 | 2026-06-26 22:35 | 2026-06-26 22:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-26 22:21 | 2026-06-26 22:23 | 74s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-06-26 21:40 | 2026-06-26 21:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.87.67[.]230` | 1 | 2026-06-26 22:40 | 2026-06-26 22:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-26 22:02 | 2026-06-26 22:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-06-26 21:34 | 2026-06-26 21:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]90` | 1 | 2026-06-26 22:01 | 2026-06-26 22:01 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 40/100 | 🟡 MEDIUM | 0/75 ✅ |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 44/100 | 🟡 MEDIUM | **11/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 48/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 42/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 61/100 | 🟡 MEDIUM | **4/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 42/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 46/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `f11dd1e4a3d27eef85d44154d662ce94234ee71b54468aeb2c23edb30b74a5c5` | ELF Binary (Linux executable) (x86-64 64-bit) | `f11dd1e4a3d27eef...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |

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

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `223.84.239[.]151` | CN | China Mobile Communications Corporation | **100** ⚠️ | 2 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `213.177.179[.]80` | NL | wcd | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `104.238.81[.]133` | US | GoDaddy.com, LLC | **100** ⚠️ | 16 |
| `80.94.92[.]55` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 11 |
| `209.141.46[.]66` | US | FranTech Solutions | **100** ⚠️ | 8 |
| `47.253.5[.]130` | US | Alibaba Cloud - US | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 193 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 181 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 12 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 12 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 352 cases |
| Tool 34  | Credential Extractor        | ✅ 189 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 42 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 181 priority case(s) shown individually · 15 recon entry/entries in table (7 group(s) consolidating 156 session(s)).

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
_Report time: 2026-06-26T23:11:12Z_

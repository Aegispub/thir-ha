# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-27 |
| **Generated At** | 2026-06-27T10:13:16Z |
| **Shift Time** | 10:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **595** |
| Confirmed Threats | **586** |
| False Positives Filtered | **9** (1.5%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **13** |
| High Severity Cases | **174** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **421** |
| Malware Samples Analyzed | **5** HIGH · **42** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **187** |
| Unique Credential Pairs | **167** |
| Unique Usernames | **86** |
| Unique Passwords | **149** |
| Successful Auth Pairs | **180** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 72 |
| `ubuntu` | 13 |
| `admin` | 8 |
| `GET / HTTP/1.1` | 3 |
| `seller` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 12 |
| `admin` | 5 |
| `smo@@kkklss` | 4 |
| `LeitboGi0ro` | 3 |
| `123@@@` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `LeitboGi0ro` | 3 |
| `root` | `123@@@` | 3 |
| `seller` | `seller` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `seller` | `seller` | `45.198.224.92` | 2026-06-27T06:55:24 |
| `seller` | `seller` | `10.0.0.73` | 2026-06-27T06:55:39 |
| `user` | `siton-2022` | `209.99.185.59` | 2026-06-27T06:55:44 |
| `el` | `el` | `209.99.185.59` | 2026-06-27T06:56:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.235.41.245` | 2026-06-27T06:57:14 |
| `meklis` | `meklis1234` | `209.99.185.59` | 2026-06-27T06:57:40 |
| `root` | `Passw0rd!` | `209.99.185.59` | 2026-06-27T06:58:36 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-27T06:59:13 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-27T06:59:13 |
| `jct` | `jct` | `209.99.185.59` | 2026-06-27T06:59:30 |
| `root` | `8x9mft82UBJdj6R4` | `209.99.185.59` | 2026-06-27T07:00:24 |
| `hbw22` | `hbw306459` | `209.99.185.59` | 2026-06-27T07:01:26 |
| `root` | `Foodvry@123` | `209.99.185.59` | 2026-06-27T07:02:21 |
| `jiaorc` | `jiaorc` | `209.99.185.59` | 2026-06-27T07:03:19 |
| `teamspeak3` | `teamspeak3` | `209.99.185.59` | 2026-06-27T07:04:17 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.58.196` | 2026-06-27T07:04:54 |
| `*1` | `$4` | `207.175.58.196` | 2026-06-27T07:05:08 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5911` | `207.175.58.196` | 2026-06-27T07:05:10 |
| `liuzhaoxing` | `liuzhaoxing` | `209.99.185.59` | 2026-06-27T07:05:13 |
| `oracle` | `oracle123` | `45.198.224.120` | 2026-06-27T07:05:40 |
| `root` | `david` | `209.99.185.59` | 2026-06-27T07:06:07 |
| `root` | `qazWSXedcrfv` | `45.205.1.42` | 2026-06-27T07:06:23 |
| `root` | `Pa$$s0rd` | `209.99.185.59` | 2026-06-27T07:07:01 |
| `root` | `﻿------fuck------` | `111.26.6.111` | 2026-06-27T07:07:04 |
| `cam` | `cam` | `209.99.185.59` | 2026-06-27T07:07:57 |
| `tong` | `666666` | `209.99.185.59` | 2026-06-27T07:08:56 |
| `wch` | `123456` | `209.99.185.59` | 2026-06-27T07:09:55 |
| `root` | `passwd123456` | `45.198.224.92` | 2026-06-27T07:10:35 |
| `root` | `passwd123456` | `10.0.0.73` | 2026-06-27T07:10:48 |
| `yt` | `yt` | `209.99.185.59` | 2026-06-27T07:10:54 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-27T07:11:01 |
| `milan` | `milan` | `209.99.185.59` | 2026-06-27T07:11:55 |
| `root` | `123000` | `209.99.185.59` | 2026-06-27T07:12:56 |
| `ubuntu` | `ubuntu` | `209.99.185.59` | 2026-06-27T07:13:58 |
| `sea` | `sea123` | `209.99.185.59` | 2026-06-27T07:14:59 |
| `dmdba` | `123456` | `209.99.185.59` | 2026-06-27T07:15:56 |
| `test` | `0000` | `209.99.185.59` | 2026-06-27T07:16:55 |
| `backdoor` | `123456` | `209.99.185.59` | 2026-06-27T07:17:59 |
| `root` | `qwer1234@#$` | `45.198.224.120` | 2026-06-27T07:18:26 |
| `root` | `qazwsx@#$` | `209.99.185.59` | 2026-06-27T07:18:57 |
| `qinyi` | `qy520816` | `209.99.185.59` | 2026-06-27T07:19:56 |
| `admin` | `1234!@#$` | `209.99.185.59` | 2026-06-27T07:20:57 |
| `tftp` | `tftp` | `209.99.185.59` | 2026-06-27T07:21:58 |
| `root` | `qwer4321!@#$` | `209.99.185.59` | 2026-06-27T07:23:00 |
| `root` | `Pass@2023` | `209.99.185.59` | 2026-06-27T07:24:02 |
| `ubuntu` | `dev12345` | `45.205.1.42` | 2026-06-27T07:24:41 |
| `mass` | `123456` | `209.99.185.59` | 2026-06-27T07:25:06 |
| `root` | `hyinfo8106` | `209.99.185.59` | 2026-06-27T07:26:07 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-27T07:27:01 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-27T07:27:02 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-27T07:27:04 |
| `wangfei` | `123456` | `209.99.185.59` | 2026-06-27T07:27:05 |
| `root` | `zxcv1234` | `209.99.185.59` | 2026-06-27T07:28:05 |
| `zfwang` | `zfwang123` | `45.198.224.92` | 2026-06-27T07:28:58 |
| `wangyijin` | `wangyijin` | `209.99.185.59` | 2026-06-27T07:29:09 |
| `zfwang` | `zfwang123` | `10.0.0.73` | 2026-06-27T07:29:10 |
| `root` | `root1234` | `45.198.224.120` | 2026-06-27T07:29:51 |
| `caja6` | `caja6` | `209.99.185.59` | 2026-06-27T07:30:13 |
| `root` | `Aa@2019` | `209.99.185.59` | 2026-06-27T07:31:16 |
| `mini` | `123456` | `209.99.185.59` | 2026-06-27T07:32:14 |
| `root` | `qq` | `209.99.185.59` | 2026-06-27T07:33:13 |
| `Data` | `korea2014` | `209.99.185.59` | 2026-06-27T07:34:14 |
| `root` | `QAZXSW` | `209.99.185.59` | 2026-06-27T07:35:17 |
| `weblogic` | `123321` | `209.99.185.59` | 2026-06-27T07:36:21 |
| `server` | `P@ssw0rd` | `209.99.185.59` | 2026-06-27T07:37:24 |
| `ubuntu` | `blackinclub!@#123` | `209.99.185.59` | 2026-06-27T07:38:25 |
| `root` | `asdfghjk` | `45.205.1.42` | 2026-06-27T07:39:11 |
| `bahrami` | `123456` | `209.99.185.59` | 2026-06-27T07:39:27 |
| `alex` | `alex` | `45.198.224.120` | 2026-06-27T07:40:26 |
| `zhouh` | `321123` | `209.99.185.59` | 2026-06-27T07:40:30 |
| `jszhang` | `jszhang` | `209.99.185.59` | 2026-06-27T07:41:36 |
| `root` | `soleil` | `209.99.185.59` | 2026-06-27T07:42:42 |
| `ubuntu` | `P@$$W0RD` | `209.99.185.59` | 2026-06-27T07:43:46 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-27T07:43:47 |
| `qym` | `123456` | `209.99.185.59` | 2026-06-27T07:44:49 |
| `root` | `2WSX_ZAQ1` | `45.198.224.92` | 2026-06-27T07:45:06 |
| `root` | `2WSX_ZAQ1` | `10.0.0.73` | 2026-06-27T07:45:18 |
| `daniel` | `daniel123` | `209.99.185.59` | 2026-06-27T07:45:52 |
| `root` | `password321` | `209.99.185.59` | 2026-06-27T07:47:02 |
| `hubert` | `1` | `209.99.185.59` | 2026-06-27T07:48:13 |
| `wangyuhan` | `WYH12520` | `209.99.185.59` | 2026-06-27T07:49:20 |
| `jira` | `password123` | `209.99.185.59` | 2026-06-27T07:50:26 |
| `root` | `P@ssword123$` | `45.198.224.120` | 2026-06-27T07:50:46 |
| `root` | `8ik!WSX3edc` | `209.99.185.59` | 2026-06-27T07:51:31 |
| `zhouxs` | `Ggty1234` | `209.99.185.59` | 2026-06-27T07:52:37 |
| `ubuntu` | `asdlkj12` | `45.205.1.42` | 2026-06-27T07:53:32 |
| `root` | `ginger` | `209.99.185.59` | 2026-06-27T07:53:45 |
| `root` | `acc3ssd3n13d` | `209.99.185.59` | 2026-06-27T07:54:53 |
| `yuanwd` | `qwerty123` | `209.99.185.59` | 2026-06-27T07:56:01 |
| `root` | `shit` | `209.99.185.59` | 2026-06-27T07:57:08 |
| `jira` | `test123` | `209.99.185.59` | 2026-06-27T07:58:14 |
| `was` | `was` | `209.99.185.59` | 2026-06-27T07:59:21 |
| `root` | `admin` | `149.118.135.252` | 2026-06-27T07:59:25 |
| `root` | `pulamea123` | `209.99.185.59` | 2026-06-27T08:00:26 |
| `oracle` | `xsw21qaz` | `209.99.185.59` | 2026-06-27T08:01:12 |
| `root` | `tingting` | `45.198.224.92` | 2026-06-27T08:01:26 |
| `root` | `tingting` | `10.0.0.73` | 2026-06-27T08:01:38 |
| `rui` | `123` | `209.99.185.59` | 2026-06-27T08:02:01 |
| `root` | `102030` | `45.198.224.120` | 2026-06-27T08:02:28 |
| `ubuntu` | `qazwsx!@#` | `209.99.185.59` | 2026-06-27T08:02:50 |
| `root` | `W123456` | `209.99.185.59` | 2026-06-27T08:03:36 |
| `tianxiang` | `tianxiang` | `209.99.185.59` | 2026-06-27T08:04:20 |
| `root` | `Aaaa1111` | `209.99.185.59` | 2026-06-27T08:05:05 |
| `yuww` | `ZLsNeuiYq5` | `209.99.185.59` | 2026-06-27T08:05:51 |
| `ansible` | `ansible123` | `209.99.185.59` | 2026-06-27T08:06:37 |
| `backupuser` | `backupuser` | `209.99.185.59` | 2026-06-27T08:07:24 |
| `ubuntu` | `123!@#` | `45.205.1.42` | 2026-06-27T08:07:57 |
| `station` | `123456` | `209.99.185.59` | 2026-06-27T08:08:13 |
| `root` | `code1` | `209.99.185.59` | 2026-06-27T08:09:03 |
| `root` | `administrator1` | `209.99.185.59` | 2026-06-27T08:09:50 |
| `deploy` | `qwe123` | `209.99.185.59` | 2026-06-27T08:10:36 |
| `zhusf` | `NEWPASS123` | `209.99.185.59` | 2026-06-27T08:11:22 |
| `jerry` | `jerry` | `209.99.185.59` | 2026-06-27T08:12:10 |
| `ubuntu` | `123132123` | `209.99.185.59` | 2026-06-27T08:13:02 |
| `shlee` | `1234` | `209.99.185.59` | 2026-06-27T08:13:52 |
| `www1` | `www1` | `45.198.224.120` | 2026-06-27T08:14:10 |
| `weblogic` | `test` | `209.99.185.59` | 2026-06-27T08:14:41 |
| `root` | `sugon@hpc123` | `209.99.185.59` | 2026-06-27T08:15:30 |
| `root` | `44444444` | `209.99.185.59` | 2026-06-27T08:16:19 |
| `root` | `Password#1234567` | `209.99.185.59` | 2026-06-27T08:17:12 |
| `a` | `!!@@` | `45.198.224.92` | 2026-06-27T08:17:51 |
| `nvidia02` | `nvidia02` | `209.99.185.59` | 2026-06-27T08:18:02 |
| `a` | `!!@@` | `10.0.0.73` | 2026-06-27T08:18:03 |
| `ceshi2` | `ceshi2321` | `209.99.185.59` | 2026-06-27T08:18:52 |
| `ubuntu` | `user1234567` | `209.99.185.59` | 2026-06-27T08:19:42 |
| `root` | `123457` | `209.99.185.59` | 2026-06-27T08:20:31 |
| `vps` | `321123` | `209.99.185.59` | 2026-06-27T08:21:20 |
| `server` | `password` | `209.99.185.59` | 2026-06-27T08:22:08 |
| `root` | `animoto` | `45.205.1.42` | 2026-06-27T08:22:27 |
| `kos` | `123456` | `209.99.185.59` | 2026-06-27T08:22:55 |
| `rendszer` | `1` | `209.99.185.59` | 2026-06-27T08:23:42 |
| `apache` | `321` | `209.99.185.59` | 2026-06-27T08:24:31 |
| `airflow` | `22&%DJO*8Ph@1ZlfyaT^Y8#Iw&Od0B&W` | `209.99.185.59` | 2026-06-27T08:25:21 |
| `ubuntu` | `qazzxc` | `45.198.224.120` | 2026-06-27T08:25:31 |
| `zywang` | `zywang` | `209.99.185.59` | 2026-06-27T08:26:13 |
| `ubuntu` | `qaz123` | `209.99.185.59` | 2026-06-27T08:27:05 |
| `operator` | `111111` | `209.99.185.59` | 2026-06-27T08:27:54 |
| `sourabh` | `123` | `209.99.185.59` | 2026-06-27T08:28:43 |
| `root` | `Huawei12#$%` | `209.99.185.59` | 2026-06-27T08:29:32 |
| `atlas` | `atlas` | `209.99.185.59` | 2026-06-27T08:30:21 |
| `zhzhang` | `123456` | `209.99.185.59` | 2026-06-27T08:31:11 |
| `uftp` | `test` | `209.99.185.59` | 2026-06-27T08:32:01 |
| `LiuJX` | `ljx112233` | `209.99.185.59` | 2026-06-27T08:32:53 |
| `root` | `admin0` | `209.99.185.59` | 2026-06-27T08:33:44 |
| `root` | `Abc12#$` | `45.198.224.92` | 2026-06-27T08:34:31 |
| `root` | `TqhdWsRx` | `209.99.185.59` | 2026-06-27T08:34:36 |
| `root` | `Abc12#$` | `10.0.0.73` | 2026-06-27T08:34:46 |
| `database` | `database!` | `209.99.185.59` | 2026-06-27T08:35:27 |
| `root` | `0987654321` | `209.99.185.59` | 2026-06-27T08:36:15 |
| `root` | `qcp` | `45.205.1.42` | 2026-06-27T08:36:42 |
| `root` | `Qwerty123!` | `45.198.224.120` | 2026-06-27T08:36:59 |
| `test_user` | `1234` | `209.99.185.59` | 2026-06-27T08:37:06 |
| `info` | `123456` | `209.99.185.59` | 2026-06-27T08:37:58 |
| `root` | `1234root` | `209.99.185.59` | 2026-06-27T08:38:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.133.11` | 2026-06-27T08:38:53 |
| `aitech` | `222222` | `209.99.185.59` | 2026-06-27T08:39:42 |
| `apache` | `P@ssw0rd` | `209.99.185.59` | 2026-06-27T08:40:33 |
| `zf` | `zf:` | `209.99.185.59` | 2026-06-27T08:41:24 |
| `hilab_admin` | `hilabadmin102938` | `209.99.185.59` | 2026-06-27T08:42:13 |
| `root` | `Passwort2020` | `209.99.185.59` | 2026-06-27T08:43:07 |
| `root` | `toyota` | `209.99.185.59` | 2026-06-27T08:43:59 |
| `root` | `P@ssw0rd2016` | `209.99.185.59` | 2026-06-27T08:44:51 |
| `admin` | `asdlkj` | `209.99.185.59` | 2026-06-27T08:45:44 |
| `guest` | `iloveyou` | `209.99.185.59` | 2026-06-27T08:46:36 |
| `root` | `Aa123...` | `209.99.185.59` | 2026-06-27T08:47:29 |
| `lichen` | `lichen` | `209.99.185.59` | 2026-06-27T08:48:23 |
| `root` | `Password@369` | `45.198.224.120` | 2026-06-27T08:48:34 |
| `root` | `marseille` | `209.99.185.59` | 2026-06-27T08:49:20 |
| `lx` | `lx123` | `209.99.185.59` | 2026-06-27T08:50:13 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-27T08:50:22 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-27T08:50:22 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-27T08:50:31 |
| `shelleicemlian` | `cIFfB6AWPz` | `209.99.185.59` | 2026-06-27T08:51:07 |
| `nagios` | `nagios1` | `45.198.224.92` | 2026-06-27T08:51:21 |
| `ubuntu` | `asd123456` | `45.205.1.42` | 2026-06-27T08:51:26 |
| `nagios` | `nagios1` | `10.0.0.73` | 2026-06-27T08:51:34 |
| `ubuntu` | `serve` | `209.99.185.59` | 2026-06-27T08:52:03 |
| `root` | `Primo` | `209.99.185.59` | 2026-06-27T08:52:58 |
| `lihaoyu` | `lihaoyu` | `209.99.185.59` | 2026-06-27T08:53:52 |
| `root` | `serverroot` | `209.99.185.59` | 2026-06-27T08:54:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **595** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 164 |
| Paramiko (Python) | 10 |
| libssh | 9 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 156 | 5 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 156 | 5 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **21** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS8075` | Microsoft Corporation | 1 | HIGH |
| `AS202425` | IP Volume inc | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (173)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b1fe01c9658e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 06:55 |
| **Last Seen** | 2026-06-27 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:55:24` | `cowrie.session.connect` |
| `2026-06-27 06:55:24` | `cowrie.client.version` |
| `2026-06-27 06:55:24` | `cowrie.client.kex` |
| `2026-06-27 06:55:24` | `cowrie.login.success` |
| `2026-06-27 06:55:25` | `cowrie.session.params` |
| `2026-06-27 06:55:25` | `cowrie.command.input` |
| `2026-06-27 06:55:25` | `cowrie.log.closed` |
| `2026-06-27 06:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-085d479592e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 06:55 |
| **Last Seen** | 2026-06-27 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:55:43` | `cowrie.session.connect` |
| `2026-06-27 06:55:43` | `cowrie.client.version` |
| `2026-06-27 06:55:43` | `cowrie.client.kex` |
| `2026-06-27 06:55:44` | `cowrie.login.success` |
| `2026-06-27 06:55:44` | `cowrie.session.params` |
| `2026-06-27 06:55:44` | `cowrie.command.input` |
| `2026-06-27 06:55:45` | `cowrie.log.closed` |
| `2026-06-27 06:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f289580a0c5c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 06:56 |
| **Last Seen** | 2026-06-27 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:56:43` | `cowrie.session.connect` |
| `2026-06-27 06:56:43` | `cowrie.client.version` |
| `2026-06-27 06:56:43` | `cowrie.client.kex` |
| `2026-06-27 06:56:43` | `cowrie.login.success` |
| `2026-06-27 06:56:44` | `cowrie.session.params` |
| `2026-06-27 06:56:44` | `cowrie.command.input` |
| `2026-06-27 06:56:44` | `cowrie.log.closed` |
| `2026-06-27 06:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da90b9ca28bc

| Field | Detail |
|---|---|
| **Source IP** | `172.235.41[.]245` |
| **First Seen** | 2026-06-27 06:57 |
| **Last Seen** | 2026-06-27 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:57:14` | `cowrie.session.connect` |
| `2026-06-27 06:57:14` | `cowrie.login.success` |
| `2026-06-27 06:57:14` | `cowrie.session.params` |
| `2026-06-27 06:57:14` | `cowrie.command.input` |
| `2026-06-27 06:57:14` | `cowrie.command.input` |
| `2026-06-27 06:57:14` | `cowrie.command.failed` |
| `2026-06-27 06:57:14` | `cowrie.command.input` |
| `2026-06-27 06:57:14` | `cowrie.command.failed` |
| `2026-06-27 06:57:14` | `cowrie.command.input` |
| `2026-06-27 06:57:14` | `cowrie.log.closed` |
| `2026-06-27 06:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.235.41[.]245` to AbuseIPDB if not already reported
- [ ] Block `172.235.41[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bd243a3dd5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 06:57 |
| **Last Seen** | 2026-06-27 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:57:40` | `cowrie.session.connect` |
| `2026-06-27 06:57:40` | `cowrie.client.version` |
| `2026-06-27 06:57:40` | `cowrie.client.kex` |
| `2026-06-27 06:57:40` | `cowrie.login.success` |
| `2026-06-27 06:57:41` | `cowrie.session.params` |
| `2026-06-27 06:57:41` | `cowrie.command.input` |
| `2026-06-27 06:57:41` | `cowrie.log.closed` |
| `2026-06-27 06:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6cbd766ac0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 06:58 |
| **Last Seen** | 2026-06-27 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:58:35` | `cowrie.session.connect` |
| `2026-06-27 06:58:35` | `cowrie.client.version` |
| `2026-06-27 06:58:35` | `cowrie.client.kex` |
| `2026-06-27 06:58:36` | `cowrie.login.success` |
| `2026-06-27 06:58:37` | `cowrie.session.params` |
| `2026-06-27 06:58:37` | `cowrie.command.input` |
| `2026-06-27 06:58:37` | `cowrie.log.closed` |
| `2026-06-27 06:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a7d308481a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 06:59 |
| **Last Seen** | 2026-06-27 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:59:12` | `cowrie.session.connect` |
| `2026-06-27 06:59:12` | `cowrie.client.version` |
| `2026-06-27 06:59:12` | `cowrie.client.kex` |
| `2026-06-27 06:59:13` | `cowrie.login.success` |
| `2026-06-27 06:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d3cb2ea5a54

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 06:59 |
| **Last Seen** | 2026-06-27 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:59:12` | `cowrie.session.connect` |
| `2026-06-27 06:59:12` | `cowrie.client.version` |
| `2026-06-27 06:59:12` | `cowrie.client.kex` |
| `2026-06-27 06:59:13` | `cowrie.login.success` |
| `2026-06-27 06:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-698ed57f3435

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 06:59 |
| **Last Seen** | 2026-06-27 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 06:59:30` | `cowrie.session.connect` |
| `2026-06-27 06:59:30` | `cowrie.client.version` |
| `2026-06-27 06:59:30` | `cowrie.client.kex` |
| `2026-06-27 06:59:30` | `cowrie.login.success` |
| `2026-06-27 06:59:31` | `cowrie.session.params` |
| `2026-06-27 06:59:31` | `cowrie.command.input` |
| `2026-06-27 06:59:31` | `cowrie.log.closed` |
| `2026-06-27 06:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f9220e010f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:00 |
| **Last Seen** | 2026-06-27 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:00:24` | `cowrie.session.connect` |
| `2026-06-27 07:00:24` | `cowrie.client.version` |
| `2026-06-27 07:00:24` | `cowrie.client.kex` |
| `2026-06-27 07:00:24` | `cowrie.login.success` |
| `2026-06-27 07:00:25` | `cowrie.session.params` |
| `2026-06-27 07:00:25` | `cowrie.command.input` |
| `2026-06-27 07:00:25` | `cowrie.log.closed` |
| `2026-06-27 07:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392f68898f63

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:01 |
| **Last Seen** | 2026-06-27 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:01:25` | `cowrie.session.connect` |
| `2026-06-27 07:01:25` | `cowrie.client.version` |
| `2026-06-27 07:01:25` | `cowrie.client.kex` |
| `2026-06-27 07:01:26` | `cowrie.login.success` |
| `2026-06-27 07:01:26` | `cowrie.session.params` |
| `2026-06-27 07:01:26` | `cowrie.command.input` |
| `2026-06-27 07:01:26` | `cowrie.log.closed` |
| `2026-06-27 07:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea221c181fb4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:02 |
| **Last Seen** | 2026-06-27 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:02:21` | `cowrie.session.connect` |
| `2026-06-27 07:02:21` | `cowrie.client.version` |
| `2026-06-27 07:02:21` | `cowrie.client.kex` |
| `2026-06-27 07:02:21` | `cowrie.login.success` |
| `2026-06-27 07:02:22` | `cowrie.session.params` |
| `2026-06-27 07:02:22` | `cowrie.command.input` |
| `2026-06-27 07:02:22` | `cowrie.log.closed` |
| `2026-06-27 07:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cf898d0a71f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:03 |
| **Last Seen** | 2026-06-27 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:03:19` | `cowrie.session.connect` |
| `2026-06-27 07:03:19` | `cowrie.client.version` |
| `2026-06-27 07:03:19` | `cowrie.client.kex` |
| `2026-06-27 07:03:19` | `cowrie.login.success` |
| `2026-06-27 07:03:20` | `cowrie.session.params` |
| `2026-06-27 07:03:20` | `cowrie.command.input` |
| `2026-06-27 07:03:20` | `cowrie.log.closed` |
| `2026-06-27 07:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ff84553eb6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:04 |
| **Last Seen** | 2026-06-27 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:04:17` | `cowrie.session.connect` |
| `2026-06-27 07:04:17` | `cowrie.client.version` |
| `2026-06-27 07:04:17` | `cowrie.client.kex` |
| `2026-06-27 07:04:17` | `cowrie.login.success` |
| `2026-06-27 07:04:18` | `cowrie.session.params` |
| `2026-06-27 07:04:18` | `cowrie.command.input` |
| `2026-06-27 07:04:18` | `cowrie.log.closed` |
| `2026-06-27 07:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b8593b2d2e6

| Field | Detail |
|---|---|
| **Source IP** | `207.175.58[.]196` |
| **First Seen** | 2026-06-27 07:04 |
| **Last Seen** | 2026-06-27 07:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:04:54` | `cowrie.session.connect` |
| `2026-06-27 07:04:54` | `cowrie.login.success` |
| `2026-06-27 07:04:55` | `cowrie.session.params` |
| `2026-06-27 07:04:55` | `cowrie.command.input` |
| `2026-06-27 07:04:55` | `cowrie.command.input` |
| `2026-06-27 07:04:55` | `cowrie.command.failed` |
| `2026-06-27 07:04:55` | `cowrie.command.input` |
| `2026-06-27 07:04:55` | `cowrie.log.closed` |
| `2026-06-27 07:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.58[.]196` to AbuseIPDB if not already reported
- [ ] Block `207.175.58[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106c5943028b

| Field | Detail |
|---|---|
| **Source IP** | `207.175.58[.]196` |
| **First Seen** | 2026-06-27 07:05 |
| **Last Seen** | 2026-06-27 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:05:08` | `cowrie.session.connect` |
| `2026-06-27 07:05:08` | `cowrie.login.success` |
| `2026-06-27 07:05:08` | `cowrie.session.params` |
| `2026-06-27 07:05:08` | `cowrie.command.input` |
| `2026-06-27 07:05:08` | `cowrie.command.failed` |
| `2026-06-27 07:05:09` | `cowrie.log.closed` |
| `2026-06-27 07:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.58[.]196` to AbuseIPDB if not already reported
- [ ] Block `207.175.58[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1c1b23ad7e

| Field | Detail |
|---|---|
| **Source IP** | `207.175.58[.]196` |
| **First Seen** | 2026-06-27 07:05 |
| **Last Seen** | 2026-06-27 07:05 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:05:10` | `cowrie.session.connect` |
| `2026-06-27 07:05:10` | `cowrie.login.success` |
| `2026-06-27 07:05:10` | `cowrie.session.params` |
| `2026-06-27 07:05:10` | `cowrie.command.input` |
| `2026-06-27 07:05:26` | `cowrie.log.closed` |
| `2026-06-27 07:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.58[.]196` to AbuseIPDB if not already reported
- [ ] Block `207.175.58[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6643a49449

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:05 |
| **Last Seen** | 2026-06-27 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:05:12` | `cowrie.session.connect` |
| `2026-06-27 07:05:12` | `cowrie.client.version` |
| `2026-06-27 07:05:12` | `cowrie.client.kex` |
| `2026-06-27 07:05:13` | `cowrie.login.success` |
| `2026-06-27 07:05:14` | `cowrie.session.params` |
| `2026-06-27 07:05:14` | `cowrie.command.input` |
| `2026-06-27 07:05:14` | `cowrie.log.closed` |
| `2026-06-27 07:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec925ae0ac6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 07:05 |
| **Last Seen** | 2026-06-27 07:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:05:33` | `cowrie.session.connect` |
| `2026-06-27 07:05:34` | `cowrie.client.version` |
| `2026-06-27 07:05:34` | `cowrie.client.kex` |
| `2026-06-27 07:05:40` | `cowrie.login.success` |
| `2026-06-27 07:05:43` | `cowrie.session.params` |
| `2026-06-27 07:05:43` | `cowrie.command.input` |
| `2026-06-27 07:05:44` | `cowrie.log.closed` |
| `2026-06-27 07:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8e1e65571f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:06 |
| **Last Seen** | 2026-06-27 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:06:07` | `cowrie.session.connect` |
| `2026-06-27 07:06:07` | `cowrie.client.version` |
| `2026-06-27 07:06:07` | `cowrie.client.kex` |
| `2026-06-27 07:06:07` | `cowrie.login.success` |
| `2026-06-27 07:06:08` | `cowrie.session.params` |
| `2026-06-27 07:06:08` | `cowrie.command.input` |
| `2026-06-27 07:06:08` | `cowrie.log.closed` |
| `2026-06-27 07:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4fecd02972

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 07:06 |
| **Last Seen** | 2026-06-27 07:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:06:20` | `cowrie.session.connect` |
| `2026-06-27 07:06:21` | `cowrie.client.version` |
| `2026-06-27 07:06:21` | `cowrie.client.kex` |
| `2026-06-27 07:06:23` | `cowrie.login.success` |
| `2026-06-27 07:06:24` | `cowrie.session.params` |
| `2026-06-27 07:06:24` | `cowrie.command.input` |
| `2026-06-27 07:06:25` | `cowrie.log.closed` |
| `2026-06-27 07:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de07f86c9526

| Field | Detail |
|---|---|
| **Source IP** | `111.26.6[.]111` |
| **First Seen** | 2026-06-27 07:06 |
| **Last Seen** | 2026-06-27 07:07 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:06:36` | `cowrie.session.connect` |
| `2026-06-27 07:06:36` | `cowrie.client.version` |
| `2026-06-27 07:06:36` | `cowrie.client.kex` |
| `2026-06-27 07:07:04` | `cowrie.login.success` |
| `2026-06-27 07:07:08` | `cowrie.session.params` |
| `2026-06-27 07:07:08` | `cowrie.command.input` |
| `2026-06-27 07:07:08` | `cowrie.log.closed` |
| `2026-06-27 07:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.26.6[.]111` to AbuseIPDB if not already reported
- [ ] Block `111.26.6[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e040a468f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:07 |
| **Last Seen** | 2026-06-27 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:07:00` | `cowrie.session.connect` |
| `2026-06-27 07:07:00` | `cowrie.client.version` |
| `2026-06-27 07:07:00` | `cowrie.client.kex` |
| `2026-06-27 07:07:01` | `cowrie.login.success` |
| `2026-06-27 07:07:01` | `cowrie.session.params` |
| `2026-06-27 07:07:01` | `cowrie.command.input` |
| `2026-06-27 07:07:02` | `cowrie.log.closed` |
| `2026-06-27 07:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209eb8c3d9d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:07 |
| **Last Seen** | 2026-06-27 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:07:56` | `cowrie.session.connect` |
| `2026-06-27 07:07:56` | `cowrie.client.version` |
| `2026-06-27 07:07:56` | `cowrie.client.kex` |
| `2026-06-27 07:07:57` | `cowrie.login.success` |
| `2026-06-27 07:07:58` | `cowrie.session.params` |
| `2026-06-27 07:07:58` | `cowrie.command.input` |
| `2026-06-27 07:07:58` | `cowrie.log.closed` |
| `2026-06-27 07:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70756d233a5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:08 |
| **Last Seen** | 2026-06-27 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:08:55` | `cowrie.session.connect` |
| `2026-06-27 07:08:55` | `cowrie.client.version` |
| `2026-06-27 07:08:55` | `cowrie.client.kex` |
| `2026-06-27 07:08:56` | `cowrie.login.success` |
| `2026-06-27 07:08:56` | `cowrie.session.params` |
| `2026-06-27 07:08:56` | `cowrie.command.input` |
| `2026-06-27 07:08:57` | `cowrie.log.closed` |
| `2026-06-27 07:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4fed320b7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:09 |
| **Last Seen** | 2026-06-27 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:09:55` | `cowrie.session.connect` |
| `2026-06-27 07:09:55` | `cowrie.client.version` |
| `2026-06-27 07:09:55` | `cowrie.client.kex` |
| `2026-06-27 07:09:55` | `cowrie.login.success` |
| `2026-06-27 07:09:56` | `cowrie.session.params` |
| `2026-06-27 07:09:56` | `cowrie.command.input` |
| `2026-06-27 07:09:56` | `cowrie.log.closed` |
| `2026-06-27 07:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9d4e76d084

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 07:10 |
| **Last Seen** | 2026-06-27 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:10:35` | `cowrie.session.connect` |
| `2026-06-27 07:10:35` | `cowrie.client.version` |
| `2026-06-27 07:10:35` | `cowrie.client.kex` |
| `2026-06-27 07:10:35` | `cowrie.login.success` |
| `2026-06-27 07:10:36` | `cowrie.session.params` |
| `2026-06-27 07:10:36` | `cowrie.command.input` |
| `2026-06-27 07:10:36` | `cowrie.log.closed` |
| `2026-06-27 07:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ba3a52a61f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:10 |
| **Last Seen** | 2026-06-27 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:10:53` | `cowrie.session.connect` |
| `2026-06-27 07:10:53` | `cowrie.client.version` |
| `2026-06-27 07:10:54` | `cowrie.client.kex` |
| `2026-06-27 07:10:54` | `cowrie.login.success` |
| `2026-06-27 07:10:55` | `cowrie.session.params` |
| `2026-06-27 07:10:55` | `cowrie.command.input` |
| `2026-06-27 07:10:55` | `cowrie.log.closed` |
| `2026-06-27 07:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955032e57d9d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-27 07:11 |
| **Last Seen** | 2026-06-27 07:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:11:00` | `cowrie.session.connect` |
| `2026-06-27 07:11:00` | `cowrie.client.version` |
| `2026-06-27 07:11:00` | `cowrie.client.kex` |
| `2026-06-27 07:11:01` | `cowrie.login.success` |
| `2026-06-27 07:11:01` | `cowrie.direct-tcpip.request` |
| `2026-06-27 07:11:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-27 07:11:01` | `cowrie.direct-tcpip.data` |
| `2026-06-27 07:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60995aded14a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-27 07:11 |
| **Last Seen** | 2026-06-27 07:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:11:01` | `cowrie.session.connect` |
| `2026-06-27 07:11:01` | `cowrie.client.version` |
| `2026-06-27 07:11:01` | `cowrie.client.kex` |
| `2026-06-27 07:11:01` | `cowrie.login.success` |
| `2026-06-27 07:11:02` | `cowrie.direct-tcpip.request` |
| `2026-06-27 07:11:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-27 07:11:02` | `cowrie.direct-tcpip.data` |
| `2026-06-27 07:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60984da066c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:11 |
| **Last Seen** | 2026-06-27 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:11:54` | `cowrie.session.connect` |
| `2026-06-27 07:11:54` | `cowrie.client.version` |
| `2026-06-27 07:11:54` | `cowrie.client.kex` |
| `2026-06-27 07:11:55` | `cowrie.login.success` |
| `2026-06-27 07:11:55` | `cowrie.session.params` |
| `2026-06-27 07:11:55` | `cowrie.command.input` |
| `2026-06-27 07:11:55` | `cowrie.log.closed` |
| `2026-06-27 07:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ade481cad7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:12 |
| **Last Seen** | 2026-06-27 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:12:56` | `cowrie.session.connect` |
| `2026-06-27 07:12:56` | `cowrie.client.version` |
| `2026-06-27 07:12:56` | `cowrie.client.kex` |
| `2026-06-27 07:12:56` | `cowrie.login.success` |
| `2026-06-27 07:12:57` | `cowrie.session.params` |
| `2026-06-27 07:12:57` | `cowrie.command.input` |
| `2026-06-27 07:12:57` | `cowrie.log.closed` |
| `2026-06-27 07:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f98652cb0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:13 |
| **Last Seen** | 2026-06-27 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:13:58` | `cowrie.session.connect` |
| `2026-06-27 07:13:58` | `cowrie.client.version` |
| `2026-06-27 07:13:58` | `cowrie.client.kex` |
| `2026-06-27 07:13:58` | `cowrie.login.success` |
| `2026-06-27 07:13:59` | `cowrie.session.params` |
| `2026-06-27 07:13:59` | `cowrie.command.input` |
| `2026-06-27 07:13:59` | `cowrie.log.closed` |
| `2026-06-27 07:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ef87d476f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:14 |
| **Last Seen** | 2026-06-27 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:14:59` | `cowrie.session.connect` |
| `2026-06-27 07:14:59` | `cowrie.client.version` |
| `2026-06-27 07:14:59` | `cowrie.client.kex` |
| `2026-06-27 07:14:59` | `cowrie.login.success` |
| `2026-06-27 07:15:00` | `cowrie.session.params` |
| `2026-06-27 07:15:00` | `cowrie.command.input` |
| `2026-06-27 07:15:00` | `cowrie.log.closed` |
| `2026-06-27 07:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da6983e3aee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:15 |
| **Last Seen** | 2026-06-27 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:15:56` | `cowrie.session.connect` |
| `2026-06-27 07:15:56` | `cowrie.client.version` |
| `2026-06-27 07:15:56` | `cowrie.client.kex` |
| `2026-06-27 07:15:56` | `cowrie.login.success` |
| `2026-06-27 07:15:57` | `cowrie.session.params` |
| `2026-06-27 07:15:57` | `cowrie.command.input` |
| `2026-06-27 07:15:57` | `cowrie.log.closed` |
| `2026-06-27 07:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e309e6ee75e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:16 |
| **Last Seen** | 2026-06-27 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:16:55` | `cowrie.session.connect` |
| `2026-06-27 07:16:55` | `cowrie.client.version` |
| `2026-06-27 07:16:55` | `cowrie.client.kex` |
| `2026-06-27 07:16:55` | `cowrie.login.success` |
| `2026-06-27 07:16:56` | `cowrie.session.params` |
| `2026-06-27 07:16:56` | `cowrie.command.input` |
| `2026-06-27 07:16:56` | `cowrie.log.closed` |
| `2026-06-27 07:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837bfcc0c0e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:17 |
| **Last Seen** | 2026-06-27 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:17:59` | `cowrie.session.connect` |
| `2026-06-27 07:17:59` | `cowrie.client.version` |
| `2026-06-27 07:17:59` | `cowrie.client.kex` |
| `2026-06-27 07:17:59` | `cowrie.login.success` |
| `2026-06-27 07:18:00` | `cowrie.session.params` |
| `2026-06-27 07:18:00` | `cowrie.command.input` |
| `2026-06-27 07:18:00` | `cowrie.log.closed` |
| `2026-06-27 07:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c4dfb86d7c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 07:18 |
| **Last Seen** | 2026-06-27 07:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:18:20` | `cowrie.session.connect` |
| `2026-06-27 07:18:22` | `cowrie.client.version` |
| `2026-06-27 07:18:22` | `cowrie.client.kex` |
| `2026-06-27 07:18:26` | `cowrie.login.success` |
| `2026-06-27 07:18:30` | `cowrie.session.params` |
| `2026-06-27 07:18:30` | `cowrie.command.input` |
| `2026-06-27 07:18:31` | `cowrie.log.closed` |
| `2026-06-27 07:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de4648bffc9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:18 |
| **Last Seen** | 2026-06-27 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:18:57` | `cowrie.session.connect` |
| `2026-06-27 07:18:57` | `cowrie.client.version` |
| `2026-06-27 07:18:57` | `cowrie.client.kex` |
| `2026-06-27 07:18:57` | `cowrie.login.success` |
| `2026-06-27 07:18:58` | `cowrie.session.params` |
| `2026-06-27 07:18:58` | `cowrie.command.input` |
| `2026-06-27 07:18:58` | `cowrie.log.closed` |
| `2026-06-27 07:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8cd42d7636

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:19 |
| **Last Seen** | 2026-06-27 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:19:56` | `cowrie.session.connect` |
| `2026-06-27 07:19:56` | `cowrie.client.version` |
| `2026-06-27 07:19:56` | `cowrie.client.kex` |
| `2026-06-27 07:19:56` | `cowrie.login.success` |
| `2026-06-27 07:19:57` | `cowrie.session.params` |
| `2026-06-27 07:19:57` | `cowrie.command.input` |
| `2026-06-27 07:19:57` | `cowrie.log.closed` |
| `2026-06-27 07:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce0efc5f2f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:20 |
| **Last Seen** | 2026-06-27 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:20:56` | `cowrie.session.connect` |
| `2026-06-27 07:20:56` | `cowrie.client.version` |
| `2026-06-27 07:20:56` | `cowrie.client.kex` |
| `2026-06-27 07:20:57` | `cowrie.login.success` |
| `2026-06-27 07:20:57` | `cowrie.session.params` |
| `2026-06-27 07:20:57` | `cowrie.command.input` |
| `2026-06-27 07:20:58` | `cowrie.log.closed` |
| `2026-06-27 07:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d71f953c60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:21 |
| **Last Seen** | 2026-06-27 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:21:57` | `cowrie.session.connect` |
| `2026-06-27 07:21:57` | `cowrie.client.version` |
| `2026-06-27 07:21:57` | `cowrie.client.kex` |
| `2026-06-27 07:21:58` | `cowrie.login.success` |
| `2026-06-27 07:21:58` | `cowrie.session.params` |
| `2026-06-27 07:21:58` | `cowrie.command.input` |
| `2026-06-27 07:21:58` | `cowrie.log.closed` |
| `2026-06-27 07:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60ae8057706

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:22 |
| **Last Seen** | 2026-06-27 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:22:59` | `cowrie.session.connect` |
| `2026-06-27 07:22:59` | `cowrie.client.version` |
| `2026-06-27 07:23:00` | `cowrie.client.kex` |
| `2026-06-27 07:23:00` | `cowrie.login.success` |
| `2026-06-27 07:23:01` | `cowrie.session.params` |
| `2026-06-27 07:23:01` | `cowrie.command.input` |
| `2026-06-27 07:23:01` | `cowrie.log.closed` |
| `2026-06-27 07:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3265edf47e76

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:24 |
| **Last Seen** | 2026-06-27 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:24:01` | `cowrie.session.connect` |
| `2026-06-27 07:24:01` | `cowrie.client.version` |
| `2026-06-27 07:24:01` | `cowrie.client.kex` |
| `2026-06-27 07:24:02` | `cowrie.login.success` |
| `2026-06-27 07:24:02` | `cowrie.session.params` |
| `2026-06-27 07:24:02` | `cowrie.command.input` |
| `2026-06-27 07:24:03` | `cowrie.log.closed` |
| `2026-06-27 07:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b64b5da45e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 07:24 |
| **Last Seen** | 2026-06-27 07:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:24:38` | `cowrie.session.connect` |
| `2026-06-27 07:24:38` | `cowrie.client.version` |
| `2026-06-27 07:24:38` | `cowrie.client.kex` |
| `2026-06-27 07:24:41` | `cowrie.login.success` |
| `2026-06-27 07:24:42` | `cowrie.session.params` |
| `2026-06-27 07:24:42` | `cowrie.command.input` |
| `2026-06-27 07:24:42` | `cowrie.log.closed` |
| `2026-06-27 07:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f226a36187b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:25 |
| **Last Seen** | 2026-06-27 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:25:05` | `cowrie.session.connect` |
| `2026-06-27 07:25:05` | `cowrie.client.version` |
| `2026-06-27 07:25:05` | `cowrie.client.kex` |
| `2026-06-27 07:25:06` | `cowrie.login.success` |
| `2026-06-27 07:25:07` | `cowrie.session.params` |
| `2026-06-27 07:25:07` | `cowrie.command.input` |
| `2026-06-27 07:25:07` | `cowrie.log.closed` |
| `2026-06-27 07:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed26bc644ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:26 |
| **Last Seen** | 2026-06-27 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:26:06` | `cowrie.session.connect` |
| `2026-06-27 07:26:06` | `cowrie.client.version` |
| `2026-06-27 07:26:06` | `cowrie.client.kex` |
| `2026-06-27 07:26:07` | `cowrie.login.success` |
| `2026-06-27 07:26:07` | `cowrie.session.params` |
| `2026-06-27 07:26:07` | `cowrie.command.input` |
| `2026-06-27 07:26:07` | `cowrie.log.closed` |
| `2026-06-27 07:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5a6d83eee5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 07:27 |
| **Last Seen** | 2026-06-27 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:27:01` | `cowrie.session.connect` |
| `2026-06-27 07:27:01` | `cowrie.client.version` |
| `2026-06-27 07:27:01` | `cowrie.client.kex` |
| `2026-06-27 07:27:01` | `cowrie.login.success` |
| `2026-06-27 07:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6811f90db05

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 07:27 |
| **Last Seen** | 2026-06-27 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:27:02` | `cowrie.session.connect` |
| `2026-06-27 07:27:02` | `cowrie.client.version` |
| `2026-06-27 07:27:02` | `cowrie.client.kex` |
| `2026-06-27 07:27:02` | `cowrie.login.success` |
| `2026-06-27 07:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c00dfe70364

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 07:27 |
| **Last Seen** | 2026-06-27 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:27:04` | `cowrie.session.connect` |
| `2026-06-27 07:27:04` | `cowrie.client.version` |
| `2026-06-27 07:27:04` | `cowrie.client.kex` |
| `2026-06-27 07:27:04` | `cowrie.login.success` |
| `2026-06-27 07:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2e1c89c43b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 07:27 |
| **Last Seen** | 2026-06-27 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:27:04` | `cowrie.session.connect` |
| `2026-06-27 07:27:04` | `cowrie.client.version` |
| `2026-06-27 07:27:04` | `cowrie.client.kex` |
| `2026-06-27 07:27:04` | `cowrie.login.success` |
| `2026-06-27 07:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb2fc502fc8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:27 |
| **Last Seen** | 2026-06-27 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:27:05` | `cowrie.session.connect` |
| `2026-06-27 07:27:05` | `cowrie.client.version` |
| `2026-06-27 07:27:05` | `cowrie.client.kex` |
| `2026-06-27 07:27:05` | `cowrie.login.success` |
| `2026-06-27 07:27:06` | `cowrie.session.params` |
| `2026-06-27 07:27:06` | `cowrie.command.input` |
| `2026-06-27 07:27:06` | `cowrie.log.closed` |
| `2026-06-27 07:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594cf21b0777

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:28 |
| **Last Seen** | 2026-06-27 07:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:28:05` | `cowrie.session.connect` |
| `2026-06-27 07:28:05` | `cowrie.client.version` |
| `2026-06-27 07:28:05` | `cowrie.client.kex` |
| `2026-06-27 07:28:05` | `cowrie.login.success` |
| `2026-06-27 07:28:06` | `cowrie.session.params` |
| `2026-06-27 07:28:06` | `cowrie.command.input` |
| `2026-06-27 07:28:06` | `cowrie.log.closed` |
| `2026-06-27 07:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6080cd4b46

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 07:28 |
| **Last Seen** | 2026-06-27 07:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:28:57` | `cowrie.session.connect` |
| `2026-06-27 07:28:57` | `cowrie.client.version` |
| `2026-06-27 07:28:57` | `cowrie.client.kex` |
| `2026-06-27 07:28:58` | `cowrie.login.success` |
| `2026-06-27 07:28:58` | `cowrie.session.params` |
| `2026-06-27 07:28:58` | `cowrie.command.input` |
| `2026-06-27 07:28:58` | `cowrie.log.closed` |
| `2026-06-27 07:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716e613fa615

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:29 |
| **Last Seen** | 2026-06-27 07:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:29:09` | `cowrie.session.connect` |
| `2026-06-27 07:29:09` | `cowrie.client.version` |
| `2026-06-27 07:29:09` | `cowrie.client.kex` |
| `2026-06-27 07:29:09` | `cowrie.login.success` |
| `2026-06-27 07:29:10` | `cowrie.session.params` |
| `2026-06-27 07:29:10` | `cowrie.command.input` |
| `2026-06-27 07:29:10` | `cowrie.log.closed` |
| `2026-06-27 07:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-460ffb1fdc33

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 07:29 |
| **Last Seen** | 2026-06-27 07:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:29:44` | `cowrie.session.connect` |
| `2026-06-27 07:29:45` | `cowrie.client.version` |
| `2026-06-27 07:29:45` | `cowrie.client.kex` |
| `2026-06-27 07:29:51` | `cowrie.login.success` |
| `2026-06-27 07:29:54` | `cowrie.session.params` |
| `2026-06-27 07:29:54` | `cowrie.command.input` |
| `2026-06-27 07:29:55` | `cowrie.log.closed` |
| `2026-06-27 07:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b6b8f91d27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:30 |
| **Last Seen** | 2026-06-27 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:30:12` | `cowrie.session.connect` |
| `2026-06-27 07:30:12` | `cowrie.client.version` |
| `2026-06-27 07:30:12` | `cowrie.client.kex` |
| `2026-06-27 07:30:13` | `cowrie.login.success` |
| `2026-06-27 07:30:14` | `cowrie.session.params` |
| `2026-06-27 07:30:14` | `cowrie.command.input` |
| `2026-06-27 07:30:14` | `cowrie.log.closed` |
| `2026-06-27 07:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f948fb59db28

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:31 |
| **Last Seen** | 2026-06-27 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:31:15` | `cowrie.session.connect` |
| `2026-06-27 07:31:15` | `cowrie.client.version` |
| `2026-06-27 07:31:15` | `cowrie.client.kex` |
| `2026-06-27 07:31:16` | `cowrie.login.success` |
| `2026-06-27 07:31:17` | `cowrie.session.params` |
| `2026-06-27 07:31:17` | `cowrie.command.input` |
| `2026-06-27 07:31:17` | `cowrie.log.closed` |
| `2026-06-27 07:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f989c0b614a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:32 |
| **Last Seen** | 2026-06-27 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:32:14` | `cowrie.session.connect` |
| `2026-06-27 07:32:14` | `cowrie.client.version` |
| `2026-06-27 07:32:14` | `cowrie.client.kex` |
| `2026-06-27 07:32:14` | `cowrie.login.success` |
| `2026-06-27 07:32:15` | `cowrie.session.params` |
| `2026-06-27 07:32:15` | `cowrie.command.input` |
| `2026-06-27 07:32:15` | `cowrie.log.closed` |
| `2026-06-27 07:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ffa0d0e531

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:33 |
| **Last Seen** | 2026-06-27 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:33:13` | `cowrie.session.connect` |
| `2026-06-27 07:33:13` | `cowrie.client.version` |
| `2026-06-27 07:33:13` | `cowrie.client.kex` |
| `2026-06-27 07:33:13` | `cowrie.login.success` |
| `2026-06-27 07:33:14` | `cowrie.session.params` |
| `2026-06-27 07:33:14` | `cowrie.command.input` |
| `2026-06-27 07:33:14` | `cowrie.log.closed` |
| `2026-06-27 07:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b8e697cf674

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:34 |
| **Last Seen** | 2026-06-27 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:34:14` | `cowrie.session.connect` |
| `2026-06-27 07:34:14` | `cowrie.client.version` |
| `2026-06-27 07:34:14` | `cowrie.client.kex` |
| `2026-06-27 07:34:14` | `cowrie.login.success` |
| `2026-06-27 07:34:15` | `cowrie.session.params` |
| `2026-06-27 07:34:15` | `cowrie.command.input` |
| `2026-06-27 07:34:15` | `cowrie.log.closed` |
| `2026-06-27 07:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9bc9ca4bd2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:35 |
| **Last Seen** | 2026-06-27 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:35:17` | `cowrie.session.connect` |
| `2026-06-27 07:35:17` | `cowrie.client.version` |
| `2026-06-27 07:35:17` | `cowrie.client.kex` |
| `2026-06-27 07:35:17` | `cowrie.login.success` |
| `2026-06-27 07:35:18` | `cowrie.session.params` |
| `2026-06-27 07:35:18` | `cowrie.command.input` |
| `2026-06-27 07:35:18` | `cowrie.log.closed` |
| `2026-06-27 07:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba68822eb74

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:36 |
| **Last Seen** | 2026-06-27 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:36:20` | `cowrie.session.connect` |
| `2026-06-27 07:36:20` | `cowrie.client.version` |
| `2026-06-27 07:36:21` | `cowrie.client.kex` |
| `2026-06-27 07:36:21` | `cowrie.login.success` |
| `2026-06-27 07:36:22` | `cowrie.session.params` |
| `2026-06-27 07:36:22` | `cowrie.command.input` |
| `2026-06-27 07:36:22` | `cowrie.log.closed` |
| `2026-06-27 07:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-753471b26d48

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:37 |
| **Last Seen** | 2026-06-27 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:37:23` | `cowrie.session.connect` |
| `2026-06-27 07:37:23` | `cowrie.client.version` |
| `2026-06-27 07:37:24` | `cowrie.client.kex` |
| `2026-06-27 07:37:24` | `cowrie.login.success` |
| `2026-06-27 07:37:25` | `cowrie.session.params` |
| `2026-06-27 07:37:25` | `cowrie.command.input` |
| `2026-06-27 07:37:25` | `cowrie.log.closed` |
| `2026-06-27 07:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031d0f13ac7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:38 |
| **Last Seen** | 2026-06-27 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:38:25` | `cowrie.session.connect` |
| `2026-06-27 07:38:25` | `cowrie.client.version` |
| `2026-06-27 07:38:25` | `cowrie.client.kex` |
| `2026-06-27 07:38:25` | `cowrie.login.success` |
| `2026-06-27 07:38:26` | `cowrie.session.params` |
| `2026-06-27 07:38:26` | `cowrie.command.input` |
| `2026-06-27 07:38:26` | `cowrie.log.closed` |
| `2026-06-27 07:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651e41a4ad81

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 07:39 |
| **Last Seen** | 2026-06-27 07:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:39:09` | `cowrie.session.connect` |
| `2026-06-27 07:39:09` | `cowrie.client.version` |
| `2026-06-27 07:39:09` | `cowrie.client.kex` |
| `2026-06-27 07:39:11` | `cowrie.login.success` |
| `2026-06-27 07:39:13` | `cowrie.session.params` |
| `2026-06-27 07:39:13` | `cowrie.command.input` |
| `2026-06-27 07:39:13` | `cowrie.log.closed` |
| `2026-06-27 07:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dab2b66ebaa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:39 |
| **Last Seen** | 2026-06-27 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:39:27` | `cowrie.session.connect` |
| `2026-06-27 07:39:27` | `cowrie.client.version` |
| `2026-06-27 07:39:27` | `cowrie.client.kex` |
| `2026-06-27 07:39:27` | `cowrie.login.success` |
| `2026-06-27 07:39:28` | `cowrie.session.params` |
| `2026-06-27 07:39:28` | `cowrie.command.input` |
| `2026-06-27 07:39:28` | `cowrie.log.closed` |
| `2026-06-27 07:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6f4cab7057

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 07:40 |
| **Last Seen** | 2026-06-27 07:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:40:19` | `cowrie.session.connect` |
| `2026-06-27 07:40:20` | `cowrie.client.version` |
| `2026-06-27 07:40:20` | `cowrie.client.kex` |
| `2026-06-27 07:40:26` | `cowrie.login.success` |
| `2026-06-27 07:40:30` | `cowrie.session.params` |
| `2026-06-27 07:40:30` | `cowrie.command.input` |
| `2026-06-27 07:40:31` | `cowrie.log.closed` |
| `2026-06-27 07:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7dc417c90d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:40 |
| **Last Seen** | 2026-06-27 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:40:30` | `cowrie.session.connect` |
| `2026-06-27 07:40:30` | `cowrie.client.version` |
| `2026-06-27 07:40:30` | `cowrie.client.kex` |
| `2026-06-27 07:40:30` | `cowrie.login.success` |
| `2026-06-27 07:40:31` | `cowrie.session.params` |
| `2026-06-27 07:40:31` | `cowrie.command.input` |
| `2026-06-27 07:40:31` | `cowrie.log.closed` |
| `2026-06-27 07:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5ee05eb17e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:41 |
| **Last Seen** | 2026-06-27 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:41:35` | `cowrie.session.connect` |
| `2026-06-27 07:41:35` | `cowrie.client.version` |
| `2026-06-27 07:41:35` | `cowrie.client.kex` |
| `2026-06-27 07:41:36` | `cowrie.login.success` |
| `2026-06-27 07:41:36` | `cowrie.session.params` |
| `2026-06-27 07:41:36` | `cowrie.command.input` |
| `2026-06-27 07:41:36` | `cowrie.log.closed` |
| `2026-06-27 07:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51285d63641b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:42 |
| **Last Seen** | 2026-06-27 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:42:42` | `cowrie.session.connect` |
| `2026-06-27 07:42:42` | `cowrie.client.version` |
| `2026-06-27 07:42:42` | `cowrie.client.kex` |
| `2026-06-27 07:42:42` | `cowrie.login.success` |
| `2026-06-27 07:42:43` | `cowrie.session.params` |
| `2026-06-27 07:42:43` | `cowrie.command.input` |
| `2026-06-27 07:42:43` | `cowrie.log.closed` |
| `2026-06-27 07:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db8361b01f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:43 |
| **Last Seen** | 2026-06-27 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:43:45` | `cowrie.session.connect` |
| `2026-06-27 07:43:45` | `cowrie.client.version` |
| `2026-06-27 07:43:45` | `cowrie.client.kex` |
| `2026-06-27 07:43:46` | `cowrie.login.success` |
| `2026-06-27 07:43:46` | `cowrie.session.params` |
| `2026-06-27 07:43:46` | `cowrie.command.input` |
| `2026-06-27 07:43:46` | `cowrie.log.closed` |
| `2026-06-27 07:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5718f5a359b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:44 |
| **Last Seen** | 2026-06-27 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:44:48` | `cowrie.session.connect` |
| `2026-06-27 07:44:48` | `cowrie.client.version` |
| `2026-06-27 07:44:48` | `cowrie.client.kex` |
| `2026-06-27 07:44:49` | `cowrie.login.success` |
| `2026-06-27 07:44:49` | `cowrie.session.params` |
| `2026-06-27 07:44:49` | `cowrie.command.input` |
| `2026-06-27 07:44:50` | `cowrie.log.closed` |
| `2026-06-27 07:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b7ae42cd13

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 07:45 |
| **Last Seen** | 2026-06-27 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:45:05` | `cowrie.session.connect` |
| `2026-06-27 07:45:05` | `cowrie.client.version` |
| `2026-06-27 07:45:05` | `cowrie.client.kex` |
| `2026-06-27 07:45:06` | `cowrie.login.success` |
| `2026-06-27 07:45:06` | `cowrie.session.params` |
| `2026-06-27 07:45:06` | `cowrie.command.input` |
| `2026-06-27 07:45:06` | `cowrie.log.closed` |
| `2026-06-27 07:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187384510abd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:45 |
| **Last Seen** | 2026-06-27 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:45:51` | `cowrie.session.connect` |
| `2026-06-27 07:45:51` | `cowrie.client.version` |
| `2026-06-27 07:45:52` | `cowrie.client.kex` |
| `2026-06-27 07:45:52` | `cowrie.login.success` |
| `2026-06-27 07:45:53` | `cowrie.session.params` |
| `2026-06-27 07:45:53` | `cowrie.command.input` |
| `2026-06-27 07:45:53` | `cowrie.log.closed` |
| `2026-06-27 07:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f33253dd78c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:47 |
| **Last Seen** | 2026-06-27 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:47:01` | `cowrie.session.connect` |
| `2026-06-27 07:47:01` | `cowrie.client.version` |
| `2026-06-27 07:47:01` | `cowrie.client.kex` |
| `2026-06-27 07:47:02` | `cowrie.login.success` |
| `2026-06-27 07:47:02` | `cowrie.session.params` |
| `2026-06-27 07:47:02` | `cowrie.command.input` |
| `2026-06-27 07:47:03` | `cowrie.log.closed` |
| `2026-06-27 07:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3255254022d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:48 |
| **Last Seen** | 2026-06-27 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:48:13` | `cowrie.session.connect` |
| `2026-06-27 07:48:13` | `cowrie.client.version` |
| `2026-06-27 07:48:13` | `cowrie.client.kex` |
| `2026-06-27 07:48:13` | `cowrie.login.success` |
| `2026-06-27 07:48:14` | `cowrie.session.params` |
| `2026-06-27 07:48:14` | `cowrie.command.input` |
| `2026-06-27 07:48:14` | `cowrie.log.closed` |
| `2026-06-27 07:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b217fd870a17

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:49 |
| **Last Seen** | 2026-06-27 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:49:19` | `cowrie.session.connect` |
| `2026-06-27 07:49:19` | `cowrie.client.version` |
| `2026-06-27 07:49:20` | `cowrie.client.kex` |
| `2026-06-27 07:49:20` | `cowrie.login.success` |
| `2026-06-27 07:49:21` | `cowrie.session.params` |
| `2026-06-27 07:49:21` | `cowrie.command.input` |
| `2026-06-27 07:49:21` | `cowrie.log.closed` |
| `2026-06-27 07:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b7fc8efb854

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:50 |
| **Last Seen** | 2026-06-27 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:50:26` | `cowrie.session.connect` |
| `2026-06-27 07:50:26` | `cowrie.client.version` |
| `2026-06-27 07:50:26` | `cowrie.client.kex` |
| `2026-06-27 07:50:26` | `cowrie.login.success` |
| `2026-06-27 07:50:27` | `cowrie.session.params` |
| `2026-06-27 07:50:27` | `cowrie.command.input` |
| `2026-06-27 07:50:27` | `cowrie.log.closed` |
| `2026-06-27 07:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63de44fd1eef

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 07:50 |
| **Last Seen** | 2026-06-27 07:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:50:38` | `cowrie.session.connect` |
| `2026-06-27 07:50:40` | `cowrie.client.version` |
| `2026-06-27 07:50:40` | `cowrie.client.kex` |
| `2026-06-27 07:50:46` | `cowrie.login.success` |
| `2026-06-27 07:50:49` | `cowrie.session.params` |
| `2026-06-27 07:50:49` | `cowrie.command.input` |
| `2026-06-27 07:50:51` | `cowrie.log.closed` |
| `2026-06-27 07:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f29c463c81

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:51 |
| **Last Seen** | 2026-06-27 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:51:31` | `cowrie.session.connect` |
| `2026-06-27 07:51:31` | `cowrie.client.version` |
| `2026-06-27 07:51:31` | `cowrie.client.kex` |
| `2026-06-27 07:51:31` | `cowrie.login.success` |
| `2026-06-27 07:51:32` | `cowrie.session.params` |
| `2026-06-27 07:51:32` | `cowrie.command.input` |
| `2026-06-27 07:51:32` | `cowrie.log.closed` |
| `2026-06-27 07:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aaf5ff8a7eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:52 |
| **Last Seen** | 2026-06-27 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:52:36` | `cowrie.session.connect` |
| `2026-06-27 07:52:36` | `cowrie.client.version` |
| `2026-06-27 07:52:36` | `cowrie.client.kex` |
| `2026-06-27 07:52:37` | `cowrie.login.success` |
| `2026-06-27 07:52:37` | `cowrie.session.params` |
| `2026-06-27 07:52:37` | `cowrie.command.input` |
| `2026-06-27 07:52:37` | `cowrie.log.closed` |
| `2026-06-27 07:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31425e3947a4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 07:53 |
| **Last Seen** | 2026-06-27 07:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:53:30` | `cowrie.session.connect` |
| `2026-06-27 07:53:30` | `cowrie.client.version` |
| `2026-06-27 07:53:30` | `cowrie.client.kex` |
| `2026-06-27 07:53:32` | `cowrie.login.success` |
| `2026-06-27 07:53:33` | `cowrie.session.params` |
| `2026-06-27 07:53:33` | `cowrie.command.input` |
| `2026-06-27 07:53:34` | `cowrie.log.closed` |
| `2026-06-27 07:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4505fd31c523

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:53 |
| **Last Seen** | 2026-06-27 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:53:44` | `cowrie.session.connect` |
| `2026-06-27 07:53:44` | `cowrie.client.version` |
| `2026-06-27 07:53:44` | `cowrie.client.kex` |
| `2026-06-27 07:53:45` | `cowrie.login.success` |
| `2026-06-27 07:53:46` | `cowrie.session.params` |
| `2026-06-27 07:53:46` | `cowrie.command.input` |
| `2026-06-27 07:53:46` | `cowrie.log.closed` |
| `2026-06-27 07:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7b2a49513d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:54 |
| **Last Seen** | 2026-06-27 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:54:53` | `cowrie.session.connect` |
| `2026-06-27 07:54:53` | `cowrie.client.version` |
| `2026-06-27 07:54:53` | `cowrie.client.kex` |
| `2026-06-27 07:54:53` | `cowrie.login.success` |
| `2026-06-27 07:54:54` | `cowrie.session.params` |
| `2026-06-27 07:54:54` | `cowrie.command.input` |
| `2026-06-27 07:54:54` | `cowrie.log.closed` |
| `2026-06-27 07:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c337ee6956c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:56 |
| **Last Seen** | 2026-06-27 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:56:00` | `cowrie.session.connect` |
| `2026-06-27 07:56:00` | `cowrie.client.version` |
| `2026-06-27 07:56:00` | `cowrie.client.kex` |
| `2026-06-27 07:56:01` | `cowrie.login.success` |
| `2026-06-27 07:56:02` | `cowrie.session.params` |
| `2026-06-27 07:56:02` | `cowrie.command.input` |
| `2026-06-27 07:56:02` | `cowrie.log.closed` |
| `2026-06-27 07:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b21f8b969ba4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:57 |
| **Last Seen** | 2026-06-27 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:57:07` | `cowrie.session.connect` |
| `2026-06-27 07:57:07` | `cowrie.client.version` |
| `2026-06-27 07:57:07` | `cowrie.client.kex` |
| `2026-06-27 07:57:08` | `cowrie.login.success` |
| `2026-06-27 07:57:08` | `cowrie.session.params` |
| `2026-06-27 07:57:08` | `cowrie.command.input` |
| `2026-06-27 07:57:09` | `cowrie.log.closed` |
| `2026-06-27 07:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c504d1db044b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:58 |
| **Last Seen** | 2026-06-27 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:58:14` | `cowrie.session.connect` |
| `2026-06-27 07:58:14` | `cowrie.client.version` |
| `2026-06-27 07:58:14` | `cowrie.client.kex` |
| `2026-06-27 07:58:14` | `cowrie.login.success` |
| `2026-06-27 07:58:15` | `cowrie.session.params` |
| `2026-06-27 07:58:15` | `cowrie.command.input` |
| `2026-06-27 07:58:15` | `cowrie.log.closed` |
| `2026-06-27 07:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3159885b2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 07:59 |
| **Last Seen** | 2026-06-27 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:59:20` | `cowrie.session.connect` |
| `2026-06-27 07:59:20` | `cowrie.client.version` |
| `2026-06-27 07:59:20` | `cowrie.client.kex` |
| `2026-06-27 07:59:21` | `cowrie.login.success` |
| `2026-06-27 07:59:22` | `cowrie.session.params` |
| `2026-06-27 07:59:22` | `cowrie.command.input` |
| `2026-06-27 07:59:22` | `cowrie.log.closed` |
| `2026-06-27 07:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13707a51d9a8

| Field | Detail |
|---|---|
| **Source IP** | `149.118.135[.]252` |
| **First Seen** | 2026-06-27 07:59 |
| **Last Seen** | 2026-06-27 07:59 |
| **Session Duration** | 35s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 07:59:22` | `cowrie.session.connect` |
| `2026-06-27 07:59:22` | `cowrie.client.version` |
| `2026-06-27 07:59:22` | `cowrie.client.kex` |
| `2026-06-27 07:59:24` | `cowrie.login.failed` |
| `2026-06-27 07:59:25` | `cowrie.login.success` |
| `2026-06-27 07:59:26` | `cowrie.session.params` |
| `2026-06-27 07:59:26` | `cowrie.command.input` |
| `2026-06-27 07:59:26` | `cowrie.command.failed` |
| `2026-06-27 07:59:26` | `cowrie.log.closed` |
| `2026-06-27 07:59:27` | `cowrie.session.params` |
| `2026-06-27 07:59:27` | `cowrie.command.input` |
| `2026-06-27 07:59:27` | `cowrie.log.closed` |
| `2026-06-27 07:59:29` | `cowrie.session.params` |
| `2026-06-27 07:59:29` | `cowrie.command.input` |
| `2026-06-27 07:59:29` | `cowrie.log.closed` |
| `2026-06-27 07:59:30` | `cowrie.session.params` |
| `2026-06-27 07:59:30` | `cowrie.command.input` |
| `2026-06-27 07:59:30` | `cowrie.log.closed` |
| `2026-06-27 07:59:31` | `cowrie.session.params` |
| `2026-06-27 07:59:31` | `cowrie.command.input` |
| `2026-06-27 07:59:31` | `cowrie.log.closed` |
| `2026-06-27 07:59:33` | `cowrie.session.params` |
| `2026-06-27 07:59:33` | `cowrie.command.input` |
| `2026-06-27 07:59:33` | `cowrie.log.closed` |
| `2026-06-27 07:59:34` | `cowrie.session.params` |
| `2026-06-27 07:59:34` | `cowrie.command.input` |
| `2026-06-27 07:59:34` | `cowrie.log.closed` |
| `2026-06-27 07:59:35` | `cowrie.session.params` |
| `2026-06-27 07:59:35` | `cowrie.command.input` |
| `2026-06-27 07:59:35` | `cowrie.log.closed` |
| `2026-06-27 07:59:36` | `cowrie.session.params` |
| `2026-06-27 07:59:36` | `cowrie.command.input` |
| `2026-06-27 07:59:37` | `cowrie.log.closed` |
| `2026-06-27 07:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.118.135[.]252` to AbuseIPDB if not already reported
- [ ] Block `149.118.135[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0d56a19908

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:00 |
| **Last Seen** | 2026-06-27 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:00:25` | `cowrie.session.connect` |
| `2026-06-27 08:00:25` | `cowrie.client.version` |
| `2026-06-27 08:00:26` | `cowrie.client.kex` |
| `2026-06-27 08:00:26` | `cowrie.login.success` |
| `2026-06-27 08:00:27` | `cowrie.session.params` |
| `2026-06-27 08:00:27` | `cowrie.command.input` |
| `2026-06-27 08:00:27` | `cowrie.log.closed` |
| `2026-06-27 08:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b53508bd6ef1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:01 |
| **Last Seen** | 2026-06-27 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:01:12` | `cowrie.session.connect` |
| `2026-06-27 08:01:12` | `cowrie.client.version` |
| `2026-06-27 08:01:12` | `cowrie.client.kex` |
| `2026-06-27 08:01:12` | `cowrie.login.success` |
| `2026-06-27 08:01:13` | `cowrie.session.params` |
| `2026-06-27 08:01:13` | `cowrie.command.input` |
| `2026-06-27 08:01:13` | `cowrie.log.closed` |
| `2026-06-27 08:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5654f99f78

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 08:01 |
| **Last Seen** | 2026-06-27 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:01:26` | `cowrie.session.connect` |
| `2026-06-27 08:01:26` | `cowrie.client.version` |
| `2026-06-27 08:01:26` | `cowrie.client.kex` |
| `2026-06-27 08:01:26` | `cowrie.login.success` |
| `2026-06-27 08:01:27` | `cowrie.session.params` |
| `2026-06-27 08:01:27` | `cowrie.command.input` |
| `2026-06-27 08:01:27` | `cowrie.log.closed` |
| `2026-06-27 08:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d4afe234fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:02 |
| **Last Seen** | 2026-06-27 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:02:00` | `cowrie.session.connect` |
| `2026-06-27 08:02:00` | `cowrie.client.version` |
| `2026-06-27 08:02:00` | `cowrie.client.kex` |
| `2026-06-27 08:02:01` | `cowrie.login.success` |
| `2026-06-27 08:02:02` | `cowrie.session.params` |
| `2026-06-27 08:02:02` | `cowrie.command.input` |
| `2026-06-27 08:02:02` | `cowrie.log.closed` |
| `2026-06-27 08:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6fc40817cbf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 08:02 |
| **Last Seen** | 2026-06-27 08:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:02:21` | `cowrie.session.connect` |
| `2026-06-27 08:02:22` | `cowrie.client.version` |
| `2026-06-27 08:02:22` | `cowrie.client.kex` |
| `2026-06-27 08:02:28` | `cowrie.login.success` |
| `2026-06-27 08:02:32` | `cowrie.session.params` |
| `2026-06-27 08:02:32` | `cowrie.command.input` |
| `2026-06-27 08:02:33` | `cowrie.log.closed` |
| `2026-06-27 08:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1419d7090142

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:02 |
| **Last Seen** | 2026-06-27 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:02:49` | `cowrie.session.connect` |
| `2026-06-27 08:02:49` | `cowrie.client.version` |
| `2026-06-27 08:02:49` | `cowrie.client.kex` |
| `2026-06-27 08:02:50` | `cowrie.login.success` |
| `2026-06-27 08:02:51` | `cowrie.session.params` |
| `2026-06-27 08:02:51` | `cowrie.command.input` |
| `2026-06-27 08:02:51` | `cowrie.log.closed` |
| `2026-06-27 08:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36a89c7b40f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:03 |
| **Last Seen** | 2026-06-27 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:03:36` | `cowrie.session.connect` |
| `2026-06-27 08:03:36` | `cowrie.client.version` |
| `2026-06-27 08:03:36` | `cowrie.client.kex` |
| `2026-06-27 08:03:36` | `cowrie.login.success` |
| `2026-06-27 08:03:37` | `cowrie.session.params` |
| `2026-06-27 08:03:37` | `cowrie.command.input` |
| `2026-06-27 08:03:37` | `cowrie.log.closed` |
| `2026-06-27 08:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2397ec3c26f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:04 |
| **Last Seen** | 2026-06-27 08:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:04:20` | `cowrie.session.connect` |
| `2026-06-27 08:04:20` | `cowrie.client.version` |
| `2026-06-27 08:04:20` | `cowrie.client.kex` |
| `2026-06-27 08:04:20` | `cowrie.login.success` |
| `2026-06-27 08:04:21` | `cowrie.session.params` |
| `2026-06-27 08:04:21` | `cowrie.command.input` |
| `2026-06-27 08:04:21` | `cowrie.log.closed` |
| `2026-06-27 08:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c51cd6de2ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:05 |
| **Last Seen** | 2026-06-27 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:05:05` | `cowrie.session.connect` |
| `2026-06-27 08:05:05` | `cowrie.client.version` |
| `2026-06-27 08:05:05` | `cowrie.client.kex` |
| `2026-06-27 08:05:05` | `cowrie.login.success` |
| `2026-06-27 08:05:06` | `cowrie.session.params` |
| `2026-06-27 08:05:06` | `cowrie.command.input` |
| `2026-06-27 08:05:06` | `cowrie.log.closed` |
| `2026-06-27 08:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f0f6c3494d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:05 |
| **Last Seen** | 2026-06-27 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:05:50` | `cowrie.session.connect` |
| `2026-06-27 08:05:50` | `cowrie.client.version` |
| `2026-06-27 08:05:50` | `cowrie.client.kex` |
| `2026-06-27 08:05:51` | `cowrie.login.success` |
| `2026-06-27 08:05:51` | `cowrie.session.params` |
| `2026-06-27 08:05:51` | `cowrie.command.input` |
| `2026-06-27 08:05:51` | `cowrie.log.closed` |
| `2026-06-27 08:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b4b97b25c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:06 |
| **Last Seen** | 2026-06-27 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:06:36` | `cowrie.session.connect` |
| `2026-06-27 08:06:36` | `cowrie.client.version` |
| `2026-06-27 08:06:36` | `cowrie.client.kex` |
| `2026-06-27 08:06:37` | `cowrie.login.success` |
| `2026-06-27 08:06:38` | `cowrie.session.params` |
| `2026-06-27 08:06:38` | `cowrie.command.input` |
| `2026-06-27 08:06:38` | `cowrie.log.closed` |
| `2026-06-27 08:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f64cdb6f27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:07 |
| **Last Seen** | 2026-06-27 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:07:24` | `cowrie.session.connect` |
| `2026-06-27 08:07:24` | `cowrie.client.version` |
| `2026-06-27 08:07:24` | `cowrie.client.kex` |
| `2026-06-27 08:07:24` | `cowrie.login.success` |
| `2026-06-27 08:07:25` | `cowrie.session.params` |
| `2026-06-27 08:07:25` | `cowrie.command.input` |
| `2026-06-27 08:07:25` | `cowrie.log.closed` |
| `2026-06-27 08:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e46079aa92

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 08:07 |
| **Last Seen** | 2026-06-27 08:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:07:55` | `cowrie.session.connect` |
| `2026-06-27 08:07:55` | `cowrie.client.version` |
| `2026-06-27 08:07:55` | `cowrie.client.kex` |
| `2026-06-27 08:07:57` | `cowrie.login.success` |
| `2026-06-27 08:07:59` | `cowrie.session.params` |
| `2026-06-27 08:07:59` | `cowrie.command.input` |
| `2026-06-27 08:07:59` | `cowrie.log.closed` |
| `2026-06-27 08:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c487b78598

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:08 |
| **Last Seen** | 2026-06-27 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:08:12` | `cowrie.session.connect` |
| `2026-06-27 08:08:12` | `cowrie.client.version` |
| `2026-06-27 08:08:12` | `cowrie.client.kex` |
| `2026-06-27 08:08:13` | `cowrie.login.success` |
| `2026-06-27 08:08:13` | `cowrie.session.params` |
| `2026-06-27 08:08:13` | `cowrie.command.input` |
| `2026-06-27 08:08:14` | `cowrie.log.closed` |
| `2026-06-27 08:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c76bd538c68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:09 |
| **Last Seen** | 2026-06-27 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:09:02` | `cowrie.session.connect` |
| `2026-06-27 08:09:02` | `cowrie.client.version` |
| `2026-06-27 08:09:02` | `cowrie.client.kex` |
| `2026-06-27 08:09:03` | `cowrie.login.success` |
| `2026-06-27 08:09:03` | `cowrie.session.params` |
| `2026-06-27 08:09:03` | `cowrie.command.input` |
| `2026-06-27 08:09:03` | `cowrie.log.closed` |
| `2026-06-27 08:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-142eecead2c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:09 |
| **Last Seen** | 2026-06-27 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:09:49` | `cowrie.session.connect` |
| `2026-06-27 08:09:49` | `cowrie.client.version` |
| `2026-06-27 08:09:50` | `cowrie.client.kex` |
| `2026-06-27 08:09:50` | `cowrie.login.success` |
| `2026-06-27 08:09:51` | `cowrie.session.params` |
| `2026-06-27 08:09:51` | `cowrie.command.input` |
| `2026-06-27 08:09:51` | `cowrie.log.closed` |
| `2026-06-27 08:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0cf1c0c3dcb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:10 |
| **Last Seen** | 2026-06-27 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:10:35` | `cowrie.session.connect` |
| `2026-06-27 08:10:35` | `cowrie.client.version` |
| `2026-06-27 08:10:35` | `cowrie.client.kex` |
| `2026-06-27 08:10:36` | `cowrie.login.success` |
| `2026-06-27 08:10:37` | `cowrie.session.params` |
| `2026-06-27 08:10:37` | `cowrie.command.input` |
| `2026-06-27 08:10:37` | `cowrie.log.closed` |
| `2026-06-27 08:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ff9d1b672b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:11 |
| **Last Seen** | 2026-06-27 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:11:22` | `cowrie.session.connect` |
| `2026-06-27 08:11:22` | `cowrie.client.version` |
| `2026-06-27 08:11:22` | `cowrie.client.kex` |
| `2026-06-27 08:11:22` | `cowrie.login.success` |
| `2026-06-27 08:11:23` | `cowrie.session.params` |
| `2026-06-27 08:11:23` | `cowrie.command.input` |
| `2026-06-27 08:11:23` | `cowrie.log.closed` |
| `2026-06-27 08:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d434744919

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:12 |
| **Last Seen** | 2026-06-27 08:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:12:09` | `cowrie.session.connect` |
| `2026-06-27 08:12:09` | `cowrie.client.version` |
| `2026-06-27 08:12:09` | `cowrie.client.kex` |
| `2026-06-27 08:12:10` | `cowrie.login.success` |
| `2026-06-27 08:12:10` | `cowrie.session.params` |
| `2026-06-27 08:12:10` | `cowrie.command.input` |
| `2026-06-27 08:12:11` | `cowrie.log.closed` |
| `2026-06-27 08:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d72f41fd53

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:13 |
| **Last Seen** | 2026-06-27 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:13:01` | `cowrie.session.connect` |
| `2026-06-27 08:13:01` | `cowrie.client.version` |
| `2026-06-27 08:13:01` | `cowrie.client.kex` |
| `2026-06-27 08:13:02` | `cowrie.login.success` |
| `2026-06-27 08:13:03` | `cowrie.session.params` |
| `2026-06-27 08:13:03` | `cowrie.command.input` |
| `2026-06-27 08:13:03` | `cowrie.log.closed` |
| `2026-06-27 08:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1772bf1f02a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:13 |
| **Last Seen** | 2026-06-27 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:13:52` | `cowrie.session.connect` |
| `2026-06-27 08:13:52` | `cowrie.client.version` |
| `2026-06-27 08:13:52` | `cowrie.client.kex` |
| `2026-06-27 08:13:52` | `cowrie.login.success` |
| `2026-06-27 08:13:53` | `cowrie.session.params` |
| `2026-06-27 08:13:53` | `cowrie.command.input` |
| `2026-06-27 08:13:53` | `cowrie.log.closed` |
| `2026-06-27 08:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a637a417183

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 08:14 |
| **Last Seen** | 2026-06-27 08:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:14:03` | `cowrie.session.connect` |
| `2026-06-27 08:14:04` | `cowrie.client.version` |
| `2026-06-27 08:14:04` | `cowrie.client.kex` |
| `2026-06-27 08:14:10` | `cowrie.login.success` |
| `2026-06-27 08:14:13` | `cowrie.session.params` |
| `2026-06-27 08:14:13` | `cowrie.command.input` |
| `2026-06-27 08:14:14` | `cowrie.log.closed` |
| `2026-06-27 08:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad13f1da7ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:14 |
| **Last Seen** | 2026-06-27 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:14:41` | `cowrie.session.connect` |
| `2026-06-27 08:14:41` | `cowrie.client.version` |
| `2026-06-27 08:14:41` | `cowrie.client.kex` |
| `2026-06-27 08:14:41` | `cowrie.login.success` |
| `2026-06-27 08:14:42` | `cowrie.session.params` |
| `2026-06-27 08:14:42` | `cowrie.command.input` |
| `2026-06-27 08:14:42` | `cowrie.log.closed` |
| `2026-06-27 08:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b425e34172

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:15 |
| **Last Seen** | 2026-06-27 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:15:30` | `cowrie.session.connect` |
| `2026-06-27 08:15:30` | `cowrie.client.version` |
| `2026-06-27 08:15:30` | `cowrie.client.kex` |
| `2026-06-27 08:15:30` | `cowrie.login.success` |
| `2026-06-27 08:15:31` | `cowrie.session.params` |
| `2026-06-27 08:15:31` | `cowrie.command.input` |
| `2026-06-27 08:15:31` | `cowrie.log.closed` |
| `2026-06-27 08:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84a7d28039e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:16 |
| **Last Seen** | 2026-06-27 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:16:19` | `cowrie.session.connect` |
| `2026-06-27 08:16:19` | `cowrie.client.version` |
| `2026-06-27 08:16:19` | `cowrie.client.kex` |
| `2026-06-27 08:16:19` | `cowrie.login.success` |
| `2026-06-27 08:16:20` | `cowrie.session.params` |
| `2026-06-27 08:16:20` | `cowrie.command.input` |
| `2026-06-27 08:16:20` | `cowrie.log.closed` |
| `2026-06-27 08:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-930afc803fb0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:17 |
| **Last Seen** | 2026-06-27 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:17:11` | `cowrie.session.connect` |
| `2026-06-27 08:17:11` | `cowrie.client.version` |
| `2026-06-27 08:17:11` | `cowrie.client.kex` |
| `2026-06-27 08:17:12` | `cowrie.login.success` |
| `2026-06-27 08:17:12` | `cowrie.session.params` |
| `2026-06-27 08:17:12` | `cowrie.command.input` |
| `2026-06-27 08:17:12` | `cowrie.log.closed` |
| `2026-06-27 08:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e205679555a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 08:17 |
| **Last Seen** | 2026-06-27 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:17:51` | `cowrie.session.connect` |
| `2026-06-27 08:17:51` | `cowrie.client.version` |
| `2026-06-27 08:17:51` | `cowrie.client.kex` |
| `2026-06-27 08:17:51` | `cowrie.login.success` |
| `2026-06-27 08:17:52` | `cowrie.session.params` |
| `2026-06-27 08:17:52` | `cowrie.command.input` |
| `2026-06-27 08:17:53` | `cowrie.log.closed` |
| `2026-06-27 08:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12fbedbd11a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:18 |
| **Last Seen** | 2026-06-27 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:18:02` | `cowrie.session.connect` |
| `2026-06-27 08:18:02` | `cowrie.client.version` |
| `2026-06-27 08:18:02` | `cowrie.client.kex` |
| `2026-06-27 08:18:02` | `cowrie.login.success` |
| `2026-06-27 08:18:03` | `cowrie.session.params` |
| `2026-06-27 08:18:03` | `cowrie.command.input` |
| `2026-06-27 08:18:03` | `cowrie.log.closed` |
| `2026-06-27 08:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f9e4c146805

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:18 |
| **Last Seen** | 2026-06-27 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:18:51` | `cowrie.session.connect` |
| `2026-06-27 08:18:51` | `cowrie.client.version` |
| `2026-06-27 08:18:52` | `cowrie.client.kex` |
| `2026-06-27 08:18:52` | `cowrie.login.success` |
| `2026-06-27 08:18:53` | `cowrie.session.params` |
| `2026-06-27 08:18:53` | `cowrie.command.input` |
| `2026-06-27 08:18:53` | `cowrie.log.closed` |
| `2026-06-27 08:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f319b5623cc0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:19 |
| **Last Seen** | 2026-06-27 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:19:41` | `cowrie.session.connect` |
| `2026-06-27 08:19:41` | `cowrie.client.version` |
| `2026-06-27 08:19:41` | `cowrie.client.kex` |
| `2026-06-27 08:19:42` | `cowrie.login.success` |
| `2026-06-27 08:19:43` | `cowrie.session.params` |
| `2026-06-27 08:19:43` | `cowrie.command.input` |
| `2026-06-27 08:19:43` | `cowrie.log.closed` |
| `2026-06-27 08:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6dab539f73e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:20 |
| **Last Seen** | 2026-06-27 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:20:31` | `cowrie.session.connect` |
| `2026-06-27 08:20:31` | `cowrie.client.version` |
| `2026-06-27 08:20:31` | `cowrie.client.kex` |
| `2026-06-27 08:20:31` | `cowrie.login.success` |
| `2026-06-27 08:20:32` | `cowrie.session.params` |
| `2026-06-27 08:20:32` | `cowrie.command.input` |
| `2026-06-27 08:20:32` | `cowrie.log.closed` |
| `2026-06-27 08:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35b306925443

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:21 |
| **Last Seen** | 2026-06-27 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:21:20` | `cowrie.session.connect` |
| `2026-06-27 08:21:20` | `cowrie.client.version` |
| `2026-06-27 08:21:20` | `cowrie.client.kex` |
| `2026-06-27 08:21:20` | `cowrie.login.success` |
| `2026-06-27 08:21:21` | `cowrie.session.params` |
| `2026-06-27 08:21:21` | `cowrie.command.input` |
| `2026-06-27 08:21:21` | `cowrie.log.closed` |
| `2026-06-27 08:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26011b4390ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:22 |
| **Last Seen** | 2026-06-27 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:22:08` | `cowrie.session.connect` |
| `2026-06-27 08:22:08` | `cowrie.client.version` |
| `2026-06-27 08:22:08` | `cowrie.client.kex` |
| `2026-06-27 08:22:08` | `cowrie.login.success` |
| `2026-06-27 08:22:09` | `cowrie.session.params` |
| `2026-06-27 08:22:09` | `cowrie.command.input` |
| `2026-06-27 08:22:09` | `cowrie.log.closed` |
| `2026-06-27 08:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f9043262c67

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 08:22 |
| **Last Seen** | 2026-06-27 08:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:22:24` | `cowrie.session.connect` |
| `2026-06-27 08:22:24` | `cowrie.client.version` |
| `2026-06-27 08:22:24` | `cowrie.client.kex` |
| `2026-06-27 08:22:27` | `cowrie.login.success` |
| `2026-06-27 08:22:28` | `cowrie.session.params` |
| `2026-06-27 08:22:28` | `cowrie.command.input` |
| `2026-06-27 08:22:28` | `cowrie.log.closed` |
| `2026-06-27 08:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14fd02f9e464

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:22 |
| **Last Seen** | 2026-06-27 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:22:54` | `cowrie.session.connect` |
| `2026-06-27 08:22:54` | `cowrie.client.version` |
| `2026-06-27 08:22:55` | `cowrie.client.kex` |
| `2026-06-27 08:22:55` | `cowrie.login.success` |
| `2026-06-27 08:22:56` | `cowrie.session.params` |
| `2026-06-27 08:22:56` | `cowrie.command.input` |
| `2026-06-27 08:22:56` | `cowrie.log.closed` |
| `2026-06-27 08:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c64996fca16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:23 |
| **Last Seen** | 2026-06-27 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:23:41` | `cowrie.session.connect` |
| `2026-06-27 08:23:41` | `cowrie.client.version` |
| `2026-06-27 08:23:41` | `cowrie.client.kex` |
| `2026-06-27 08:23:42` | `cowrie.login.success` |
| `2026-06-27 08:23:42` | `cowrie.session.params` |
| `2026-06-27 08:23:42` | `cowrie.command.input` |
| `2026-06-27 08:23:42` | `cowrie.log.closed` |
| `2026-06-27 08:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af575cd8a0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:24 |
| **Last Seen** | 2026-06-27 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:24:31` | `cowrie.session.connect` |
| `2026-06-27 08:24:31` | `cowrie.client.version` |
| `2026-06-27 08:24:31` | `cowrie.client.kex` |
| `2026-06-27 08:24:31` | `cowrie.login.success` |
| `2026-06-27 08:24:32` | `cowrie.session.params` |
| `2026-06-27 08:24:32` | `cowrie.command.input` |
| `2026-06-27 08:24:32` | `cowrie.log.closed` |
| `2026-06-27 08:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9734bee039c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:25 |
| **Last Seen** | 2026-06-27 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:25:20` | `cowrie.session.connect` |
| `2026-06-27 08:25:20` | `cowrie.client.version` |
| `2026-06-27 08:25:20` | `cowrie.client.kex` |
| `2026-06-27 08:25:21` | `cowrie.login.success` |
| `2026-06-27 08:25:21` | `cowrie.session.params` |
| `2026-06-27 08:25:21` | `cowrie.command.input` |
| `2026-06-27 08:25:21` | `cowrie.log.closed` |
| `2026-06-27 08:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215e06b51189

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 08:25 |
| **Last Seen** | 2026-06-27 08:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:25:24` | `cowrie.session.connect` |
| `2026-06-27 08:25:25` | `cowrie.client.version` |
| `2026-06-27 08:25:25` | `cowrie.client.kex` |
| `2026-06-27 08:25:31` | `cowrie.login.success` |
| `2026-06-27 08:25:34` | `cowrie.session.params` |
| `2026-06-27 08:25:34` | `cowrie.command.input` |
| `2026-06-27 08:25:36` | `cowrie.log.closed` |
| `2026-06-27 08:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c2ccb232ed5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:26 |
| **Last Seen** | 2026-06-27 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:26:13` | `cowrie.session.connect` |
| `2026-06-27 08:26:13` | `cowrie.client.version` |
| `2026-06-27 08:26:13` | `cowrie.client.kex` |
| `2026-06-27 08:26:13` | `cowrie.login.success` |
| `2026-06-27 08:26:14` | `cowrie.session.params` |
| `2026-06-27 08:26:14` | `cowrie.command.input` |
| `2026-06-27 08:26:14` | `cowrie.log.closed` |
| `2026-06-27 08:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c710bdceaaed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:27 |
| **Last Seen** | 2026-06-27 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:27:04` | `cowrie.session.connect` |
| `2026-06-27 08:27:04` | `cowrie.client.version` |
| `2026-06-27 08:27:04` | `cowrie.client.kex` |
| `2026-06-27 08:27:05` | `cowrie.login.success` |
| `2026-06-27 08:27:06` | `cowrie.session.params` |
| `2026-06-27 08:27:06` | `cowrie.command.input` |
| `2026-06-27 08:27:06` | `cowrie.log.closed` |
| `2026-06-27 08:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbdf5270a01f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:27 |
| **Last Seen** | 2026-06-27 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:27:53` | `cowrie.session.connect` |
| `2026-06-27 08:27:53` | `cowrie.client.version` |
| `2026-06-27 08:27:53` | `cowrie.client.kex` |
| `2026-06-27 08:27:54` | `cowrie.login.success` |
| `2026-06-27 08:27:54` | `cowrie.session.params` |
| `2026-06-27 08:27:54` | `cowrie.command.input` |
| `2026-06-27 08:27:55` | `cowrie.log.closed` |
| `2026-06-27 08:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13bfc4b1463a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:28 |
| **Last Seen** | 2026-06-27 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:28:42` | `cowrie.session.connect` |
| `2026-06-27 08:28:42` | `cowrie.client.version` |
| `2026-06-27 08:28:42` | `cowrie.client.kex` |
| `2026-06-27 08:28:43` | `cowrie.login.success` |
| `2026-06-27 08:28:44` | `cowrie.session.params` |
| `2026-06-27 08:28:44` | `cowrie.command.input` |
| `2026-06-27 08:28:44` | `cowrie.log.closed` |
| `2026-06-27 08:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ba2468b1d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:29 |
| **Last Seen** | 2026-06-27 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:29:32` | `cowrie.session.connect` |
| `2026-06-27 08:29:32` | `cowrie.client.version` |
| `2026-06-27 08:29:32` | `cowrie.client.kex` |
| `2026-06-27 08:29:32` | `cowrie.login.success` |
| `2026-06-27 08:29:33` | `cowrie.session.params` |
| `2026-06-27 08:29:33` | `cowrie.command.input` |
| `2026-06-27 08:29:33` | `cowrie.log.closed` |
| `2026-06-27 08:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3501d1e6739

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:30 |
| **Last Seen** | 2026-06-27 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:30:21` | `cowrie.session.connect` |
| `2026-06-27 08:30:21` | `cowrie.client.version` |
| `2026-06-27 08:30:21` | `cowrie.client.kex` |
| `2026-06-27 08:30:21` | `cowrie.login.success` |
| `2026-06-27 08:30:22` | `cowrie.session.params` |
| `2026-06-27 08:30:22` | `cowrie.command.input` |
| `2026-06-27 08:30:22` | `cowrie.log.closed` |
| `2026-06-27 08:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2026fb194c46

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:31 |
| **Last Seen** | 2026-06-27 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:31:11` | `cowrie.session.connect` |
| `2026-06-27 08:31:11` | `cowrie.client.version` |
| `2026-06-27 08:31:11` | `cowrie.client.kex` |
| `2026-06-27 08:31:11` | `cowrie.login.success` |
| `2026-06-27 08:31:12` | `cowrie.session.params` |
| `2026-06-27 08:31:12` | `cowrie.command.input` |
| `2026-06-27 08:31:12` | `cowrie.log.closed` |
| `2026-06-27 08:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d22600a021b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:32 |
| **Last Seen** | 2026-06-27 08:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:32:01` | `cowrie.session.connect` |
| `2026-06-27 08:32:01` | `cowrie.client.version` |
| `2026-06-27 08:32:01` | `cowrie.client.kex` |
| `2026-06-27 08:32:01` | `cowrie.login.success` |
| `2026-06-27 08:32:02` | `cowrie.session.params` |
| `2026-06-27 08:32:02` | `cowrie.command.input` |
| `2026-06-27 08:32:02` | `cowrie.log.closed` |
| `2026-06-27 08:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aaab2534886

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:32 |
| **Last Seen** | 2026-06-27 08:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:32:53` | `cowrie.session.connect` |
| `2026-06-27 08:32:53` | `cowrie.client.version` |
| `2026-06-27 08:32:53` | `cowrie.client.kex` |
| `2026-06-27 08:32:53` | `cowrie.login.success` |
| `2026-06-27 08:32:54` | `cowrie.session.params` |
| `2026-06-27 08:32:54` | `cowrie.command.input` |
| `2026-06-27 08:32:54` | `cowrie.log.closed` |
| `2026-06-27 08:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-167f829e1e54

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:33 |
| **Last Seen** | 2026-06-27 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:33:43` | `cowrie.session.connect` |
| `2026-06-27 08:33:43` | `cowrie.client.version` |
| `2026-06-27 08:33:43` | `cowrie.client.kex` |
| `2026-06-27 08:33:44` | `cowrie.login.success` |
| `2026-06-27 08:33:45` | `cowrie.session.params` |
| `2026-06-27 08:33:45` | `cowrie.command.input` |
| `2026-06-27 08:33:45` | `cowrie.log.closed` |
| `2026-06-27 08:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3069bfbedd3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 08:34 |
| **Last Seen** | 2026-06-27 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:34:30` | `cowrie.session.connect` |
| `2026-06-27 08:34:30` | `cowrie.client.version` |
| `2026-06-27 08:34:30` | `cowrie.client.kex` |
| `2026-06-27 08:34:31` | `cowrie.login.success` |
| `2026-06-27 08:34:32` | `cowrie.session.params` |
| `2026-06-27 08:34:32` | `cowrie.command.input` |
| `2026-06-27 08:34:32` | `cowrie.log.closed` |
| `2026-06-27 08:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54d4ff93a96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:34 |
| **Last Seen** | 2026-06-27 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:34:35` | `cowrie.session.connect` |
| `2026-06-27 08:34:35` | `cowrie.client.version` |
| `2026-06-27 08:34:35` | `cowrie.client.kex` |
| `2026-06-27 08:34:36` | `cowrie.login.success` |
| `2026-06-27 08:34:36` | `cowrie.session.params` |
| `2026-06-27 08:34:36` | `cowrie.command.input` |
| `2026-06-27 08:34:37` | `cowrie.log.closed` |
| `2026-06-27 08:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df83c2746bd1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:35 |
| **Last Seen** | 2026-06-27 08:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:35:26` | `cowrie.session.connect` |
| `2026-06-27 08:35:26` | `cowrie.client.version` |
| `2026-06-27 08:35:26` | `cowrie.client.kex` |
| `2026-06-27 08:35:27` | `cowrie.login.success` |
| `2026-06-27 08:35:27` | `cowrie.session.params` |
| `2026-06-27 08:35:27` | `cowrie.command.input` |
| `2026-06-27 08:35:28` | `cowrie.log.closed` |
| `2026-06-27 08:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13aa3cc5fe40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:36 |
| **Last Seen** | 2026-06-27 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:36:15` | `cowrie.session.connect` |
| `2026-06-27 08:36:15` | `cowrie.client.version` |
| `2026-06-27 08:36:15` | `cowrie.client.kex` |
| `2026-06-27 08:36:15` | `cowrie.login.success` |
| `2026-06-27 08:36:16` | `cowrie.session.params` |
| `2026-06-27 08:36:16` | `cowrie.command.input` |
| `2026-06-27 08:36:16` | `cowrie.log.closed` |
| `2026-06-27 08:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e10d239ee10

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 08:36 |
| **Last Seen** | 2026-06-27 08:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:36:40` | `cowrie.session.connect` |
| `2026-06-27 08:36:40` | `cowrie.client.version` |
| `2026-06-27 08:36:40` | `cowrie.client.kex` |
| `2026-06-27 08:36:42` | `cowrie.login.success` |
| `2026-06-27 08:36:43` | `cowrie.session.params` |
| `2026-06-27 08:36:43` | `cowrie.command.input` |
| `2026-06-27 08:36:44` | `cowrie.log.closed` |
| `2026-06-27 08:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a157e667c89a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 08:36 |
| **Last Seen** | 2026-06-27 08:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:36:52` | `cowrie.session.connect` |
| `2026-06-27 08:36:54` | `cowrie.client.version` |
| `2026-06-27 08:36:54` | `cowrie.client.kex` |
| `2026-06-27 08:36:59` | `cowrie.login.success` |
| `2026-06-27 08:37:03` | `cowrie.session.params` |
| `2026-06-27 08:37:03` | `cowrie.command.input` |
| `2026-06-27 08:37:05` | `cowrie.log.closed` |
| `2026-06-27 08:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee003a4c981

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:37 |
| **Last Seen** | 2026-06-27 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:37:06` | `cowrie.session.connect` |
| `2026-06-27 08:37:06` | `cowrie.client.version` |
| `2026-06-27 08:37:06` | `cowrie.client.kex` |
| `2026-06-27 08:37:06` | `cowrie.login.success` |
| `2026-06-27 08:37:07` | `cowrie.session.params` |
| `2026-06-27 08:37:07` | `cowrie.command.input` |
| `2026-06-27 08:37:07` | `cowrie.log.closed` |
| `2026-06-27 08:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435a6a0c6c88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:37 |
| **Last Seen** | 2026-06-27 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:37:58` | `cowrie.session.connect` |
| `2026-06-27 08:37:58` | `cowrie.client.version` |
| `2026-06-27 08:37:58` | `cowrie.client.kex` |
| `2026-06-27 08:37:58` | `cowrie.login.success` |
| `2026-06-27 08:37:59` | `cowrie.session.params` |
| `2026-06-27 08:37:59` | `cowrie.command.input` |
| `2026-06-27 08:37:59` | `cowrie.log.closed` |
| `2026-06-27 08:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ad53d9d56c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:38 |
| **Last Seen** | 2026-06-27 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:38:49` | `cowrie.session.connect` |
| `2026-06-27 08:38:49` | `cowrie.client.version` |
| `2026-06-27 08:38:49` | `cowrie.client.kex` |
| `2026-06-27 08:38:49` | `cowrie.login.success` |
| `2026-06-27 08:38:50` | `cowrie.session.params` |
| `2026-06-27 08:38:50` | `cowrie.command.input` |
| `2026-06-27 08:38:50` | `cowrie.log.closed` |
| `2026-06-27 08:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2137fcc082

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:39 |
| **Last Seen** | 2026-06-27 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:39:41` | `cowrie.session.connect` |
| `2026-06-27 08:39:41` | `cowrie.client.version` |
| `2026-06-27 08:39:41` | `cowrie.client.kex` |
| `2026-06-27 08:39:42` | `cowrie.login.success` |
| `2026-06-27 08:39:42` | `cowrie.session.params` |
| `2026-06-27 08:39:42` | `cowrie.command.input` |
| `2026-06-27 08:39:42` | `cowrie.log.closed` |
| `2026-06-27 08:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d520f293af6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:40 |
| **Last Seen** | 2026-06-27 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:40:33` | `cowrie.session.connect` |
| `2026-06-27 08:40:33` | `cowrie.client.version` |
| `2026-06-27 08:40:33` | `cowrie.client.kex` |
| `2026-06-27 08:40:33` | `cowrie.login.success` |
| `2026-06-27 08:40:34` | `cowrie.session.params` |
| `2026-06-27 08:40:34` | `cowrie.command.input` |
| `2026-06-27 08:40:34` | `cowrie.log.closed` |
| `2026-06-27 08:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b2e4e9f699

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:41 |
| **Last Seen** | 2026-06-27 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:41:24` | `cowrie.session.connect` |
| `2026-06-27 08:41:24` | `cowrie.client.version` |
| `2026-06-27 08:41:24` | `cowrie.client.kex` |
| `2026-06-27 08:41:24` | `cowrie.login.success` |
| `2026-06-27 08:41:25` | `cowrie.session.params` |
| `2026-06-27 08:41:25` | `cowrie.command.input` |
| `2026-06-27 08:41:25` | `cowrie.log.closed` |
| `2026-06-27 08:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1eea0eac897

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:42 |
| **Last Seen** | 2026-06-27 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:42:13` | `cowrie.session.connect` |
| `2026-06-27 08:42:13` | `cowrie.client.version` |
| `2026-06-27 08:42:13` | `cowrie.client.kex` |
| `2026-06-27 08:42:13` | `cowrie.login.success` |
| `2026-06-27 08:42:14` | `cowrie.session.params` |
| `2026-06-27 08:42:14` | `cowrie.command.input` |
| `2026-06-27 08:42:14` | `cowrie.log.closed` |
| `2026-06-27 08:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dcd6a343953

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:43 |
| **Last Seen** | 2026-06-27 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:43:06` | `cowrie.session.connect` |
| `2026-06-27 08:43:06` | `cowrie.client.version` |
| `2026-06-27 08:43:06` | `cowrie.client.kex` |
| `2026-06-27 08:43:07` | `cowrie.login.success` |
| `2026-06-27 08:43:07` | `cowrie.session.params` |
| `2026-06-27 08:43:07` | `cowrie.command.input` |
| `2026-06-27 08:43:08` | `cowrie.log.closed` |
| `2026-06-27 08:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329c20f55337

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:43 |
| **Last Seen** | 2026-06-27 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:43:58` | `cowrie.session.connect` |
| `2026-06-27 08:43:58` | `cowrie.client.version` |
| `2026-06-27 08:43:58` | `cowrie.client.kex` |
| `2026-06-27 08:43:59` | `cowrie.login.success` |
| `2026-06-27 08:43:59` | `cowrie.session.params` |
| `2026-06-27 08:43:59` | `cowrie.command.input` |
| `2026-06-27 08:43:59` | `cowrie.log.closed` |
| `2026-06-27 08:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b14e966b429

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:44 |
| **Last Seen** | 2026-06-27 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:44:50` | `cowrie.session.connect` |
| `2026-06-27 08:44:50` | `cowrie.client.version` |
| `2026-06-27 08:44:51` | `cowrie.client.kex` |
| `2026-06-27 08:44:51` | `cowrie.login.success` |
| `2026-06-27 08:44:52` | `cowrie.session.params` |
| `2026-06-27 08:44:52` | `cowrie.command.input` |
| `2026-06-27 08:44:52` | `cowrie.log.closed` |
| `2026-06-27 08:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2f40b881b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:45 |
| **Last Seen** | 2026-06-27 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:45:44` | `cowrie.session.connect` |
| `2026-06-27 08:45:44` | `cowrie.client.version` |
| `2026-06-27 08:45:44` | `cowrie.client.kex` |
| `2026-06-27 08:45:44` | `cowrie.login.success` |
| `2026-06-27 08:45:45` | `cowrie.session.params` |
| `2026-06-27 08:45:45` | `cowrie.command.input` |
| `2026-06-27 08:45:45` | `cowrie.log.closed` |
| `2026-06-27 08:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c4aaab9dcd7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:46 |
| **Last Seen** | 2026-06-27 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:46:36` | `cowrie.session.connect` |
| `2026-06-27 08:46:36` | `cowrie.client.version` |
| `2026-06-27 08:46:36` | `cowrie.client.kex` |
| `2026-06-27 08:46:36` | `cowrie.login.success` |
| `2026-06-27 08:46:37` | `cowrie.session.params` |
| `2026-06-27 08:46:37` | `cowrie.command.input` |
| `2026-06-27 08:46:37` | `cowrie.log.closed` |
| `2026-06-27 08:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e71cccce2b89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:47 |
| **Last Seen** | 2026-06-27 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:47:29` | `cowrie.session.connect` |
| `2026-06-27 08:47:29` | `cowrie.client.version` |
| `2026-06-27 08:47:29` | `cowrie.client.kex` |
| `2026-06-27 08:47:29` | `cowrie.login.success` |
| `2026-06-27 08:47:30` | `cowrie.session.params` |
| `2026-06-27 08:47:30` | `cowrie.command.input` |
| `2026-06-27 08:47:30` | `cowrie.log.closed` |
| `2026-06-27 08:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d379df558e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:48 |
| **Last Seen** | 2026-06-27 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:48:23` | `cowrie.session.connect` |
| `2026-06-27 08:48:23` | `cowrie.client.version` |
| `2026-06-27 08:48:23` | `cowrie.client.kex` |
| `2026-06-27 08:48:23` | `cowrie.login.success` |
| `2026-06-27 08:48:24` | `cowrie.session.params` |
| `2026-06-27 08:48:24` | `cowrie.command.input` |
| `2026-06-27 08:48:24` | `cowrie.log.closed` |
| `2026-06-27 08:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3b38966cc7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 08:48 |
| **Last Seen** | 2026-06-27 08:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:48:27` | `cowrie.session.connect` |
| `2026-06-27 08:48:28` | `cowrie.client.version` |
| `2026-06-27 08:48:28` | `cowrie.client.kex` |
| `2026-06-27 08:48:34` | `cowrie.login.success` |
| `2026-06-27 08:48:38` | `cowrie.session.params` |
| `2026-06-27 08:48:38` | `cowrie.command.input` |
| `2026-06-27 08:48:40` | `cowrie.log.closed` |
| `2026-06-27 08:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae8f4363d89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:49 |
| **Last Seen** | 2026-06-27 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:49:19` | `cowrie.session.connect` |
| `2026-06-27 08:49:19` | `cowrie.client.version` |
| `2026-06-27 08:49:20` | `cowrie.client.kex` |
| `2026-06-27 08:49:20` | `cowrie.login.success` |
| `2026-06-27 08:49:21` | `cowrie.session.params` |
| `2026-06-27 08:49:21` | `cowrie.command.input` |
| `2026-06-27 08:49:21` | `cowrie.log.closed` |
| `2026-06-27 08:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e551719a7e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:50 |
| **Last Seen** | 2026-06-27 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:50:12` | `cowrie.session.connect` |
| `2026-06-27 08:50:12` | `cowrie.client.version` |
| `2026-06-27 08:50:13` | `cowrie.client.kex` |
| `2026-06-27 08:50:13` | `cowrie.login.success` |
| `2026-06-27 08:50:14` | `cowrie.session.params` |
| `2026-06-27 08:50:14` | `cowrie.command.input` |
| `2026-06-27 08:50:14` | `cowrie.log.closed` |
| `2026-06-27 08:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a6a0f5f882f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 08:50 |
| **Last Seen** | 2026-06-27 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:50:21` | `cowrie.session.connect` |
| `2026-06-27 08:50:21` | `cowrie.client.version` |
| `2026-06-27 08:50:21` | `cowrie.client.kex` |
| `2026-06-27 08:50:22` | `cowrie.login.success` |
| `2026-06-27 08:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d840271087d4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 08:50 |
| **Last Seen** | 2026-06-27 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:50:21` | `cowrie.session.connect` |
| `2026-06-27 08:50:21` | `cowrie.client.version` |
| `2026-06-27 08:50:22` | `cowrie.client.kex` |
| `2026-06-27 08:50:22` | `cowrie.login.success` |
| `2026-06-27 08:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6daecf64588

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 08:50 |
| **Last Seen** | 2026-06-27 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:50:30` | `cowrie.session.connect` |
| `2026-06-27 08:50:30` | `cowrie.client.version` |
| `2026-06-27 08:50:31` | `cowrie.client.kex` |
| `2026-06-27 08:50:31` | `cowrie.login.success` |
| `2026-06-27 08:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3647c370f0b7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 08:50 |
| **Last Seen** | 2026-06-27 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:50:31` | `cowrie.session.connect` |
| `2026-06-27 08:50:31` | `cowrie.client.version` |
| `2026-06-27 08:50:32` | `cowrie.client.kex` |
| `2026-06-27 08:50:32` | `cowrie.login.success` |
| `2026-06-27 08:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bfae1bf6196

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:51 |
| **Last Seen** | 2026-06-27 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:51:07` | `cowrie.session.connect` |
| `2026-06-27 08:51:07` | `cowrie.client.version` |
| `2026-06-27 08:51:07` | `cowrie.client.kex` |
| `2026-06-27 08:51:07` | `cowrie.login.success` |
| `2026-06-27 08:51:08` | `cowrie.session.params` |
| `2026-06-27 08:51:08` | `cowrie.command.input` |
| `2026-06-27 08:51:08` | `cowrie.log.closed` |
| `2026-06-27 08:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73948e404e8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 08:51 |
| **Last Seen** | 2026-06-27 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:51:20` | `cowrie.session.connect` |
| `2026-06-27 08:51:21` | `cowrie.client.version` |
| `2026-06-27 08:51:21` | `cowrie.client.kex` |
| `2026-06-27 08:51:21` | `cowrie.login.success` |
| `2026-06-27 08:51:22` | `cowrie.session.params` |
| `2026-06-27 08:51:22` | `cowrie.command.input` |
| `2026-06-27 08:51:22` | `cowrie.log.closed` |
| `2026-06-27 08:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f0a7f2c285c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 08:51 |
| **Last Seen** | 2026-06-27 08:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:51:24` | `cowrie.session.connect` |
| `2026-06-27 08:51:25` | `cowrie.client.version` |
| `2026-06-27 08:51:25` | `cowrie.client.kex` |
| `2026-06-27 08:51:26` | `cowrie.login.success` |
| `2026-06-27 08:51:27` | `cowrie.session.params` |
| `2026-06-27 08:51:27` | `cowrie.command.input` |
| `2026-06-27 08:51:28` | `cowrie.log.closed` |
| `2026-06-27 08:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19d1d491a183

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:52 |
| **Last Seen** | 2026-06-27 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:52:02` | `cowrie.session.connect` |
| `2026-06-27 08:52:02` | `cowrie.client.version` |
| `2026-06-27 08:52:02` | `cowrie.client.kex` |
| `2026-06-27 08:52:03` | `cowrie.login.success` |
| `2026-06-27 08:52:03` | `cowrie.session.params` |
| `2026-06-27 08:52:03` | `cowrie.command.input` |
| `2026-06-27 08:52:04` | `cowrie.log.closed` |
| `2026-06-27 08:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb4e78ec746

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:52 |
| **Last Seen** | 2026-06-27 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:52:58` | `cowrie.session.connect` |
| `2026-06-27 08:52:58` | `cowrie.client.version` |
| `2026-06-27 08:52:58` | `cowrie.client.kex` |
| `2026-06-27 08:52:58` | `cowrie.login.success` |
| `2026-06-27 08:52:59` | `cowrie.session.params` |
| `2026-06-27 08:52:59` | `cowrie.command.input` |
| `2026-06-27 08:52:59` | `cowrie.log.closed` |
| `2026-06-27 08:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e07b811a82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:53 |
| **Last Seen** | 2026-06-27 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:53:52` | `cowrie.session.connect` |
| `2026-06-27 08:53:52` | `cowrie.client.version` |
| `2026-06-27 08:53:52` | `cowrie.client.kex` |
| `2026-06-27 08:53:52` | `cowrie.login.success` |
| `2026-06-27 08:53:53` | `cowrie.session.params` |
| `2026-06-27 08:53:53` | `cowrie.command.input` |
| `2026-06-27 08:53:53` | `cowrie.log.closed` |
| `2026-06-27 08:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476c8b750d81

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:54 |
| **Last Seen** | 2026-06-27 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:54:44` | `cowrie.session.connect` |
| `2026-06-27 08:54:44` | `cowrie.client.version` |
| `2026-06-27 08:54:44` | `cowrie.client.kex` |
| `2026-06-27 08:54:45` | `cowrie.login.success` |
| `2026-06-27 08:54:45` | `cowrie.session.params` |
| `2026-06-27 08:54:45` | `cowrie.command.input` |
| `2026-06-27 08:54:45` | `cowrie.log.closed` |
| `2026-06-27 08:54:45` | `cowrie.session.closed` |

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
| `157.230.42[.]17` | **226** | 2026-06-27 06:55 | 2026-06-27 08:54 | 151m | 0 | `T1592` | 🟠 MEDIUM |
| `209.99.185[.]59` | **129** | 2026-06-27 06:55 | 2026-06-27 08:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.58[.]196` | **30** | 2026-06-27 07:04 | 2026-06-27 07:05 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `172.236.228[.]38` | **3** | 2026-06-27 08:34 | 2026-06-27 08:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.27.251[.]252` | **2** | 2026-06-27 08:43 | 2026-06-27 08:45 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-27 07:38 | 2026-06-27 08:34 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.55.35[.]217` | **2** | 2026-06-27 07:35 | 2026-06-27 07:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `209.141.46[.]66` | **2** | 2026-06-27 07:02 | 2026-06-27 07:14 | 1m | 0 | `T1592` | 🟢 LOW |
| `3.19.32[.]17` | **2** | 2026-06-27 07:33 | 2026-06-27 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.250.81[.]7` | **2** | 2026-06-27 07:51 | 2026-06-27 07:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.26.6[.]111` | 1 | 2026-06-27 07:06 | 2026-06-27 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `114.35.0[.]177` | 1 | 2026-06-27 08:11 | 2026-06-27 08:12 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]245` | 1 | 2026-06-27 06:57 | 2026-06-27 06:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-06-27 08:06 | 2026-06-27 08:06 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-06-27 07:06 | 2026-06-27 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-27 07:02 | 2026-06-27 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-27 08:33 | 2026-06-27 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-06-27 07:33 | 2026-06-27 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-27 08:07 | 2026-06-27 08:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]132` | 1 | 2026-06-27 08:21 | 2026-06-27 08:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-06-27 07:33 | 2026-06-27 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-06-27 08:33 | 2026-06-27 08:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]26` | 1 | 2026-06-27 08:52 | 2026-06-27 08:52 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 43/100 | 🟡 MEDIUM | **9/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 44/100 | 🟡 MEDIUM | **11/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 83/100 | 🔴 HIGH | **34/75** 🔴 |
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
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 46/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |

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
| `209.141.46[.]66` | US | FranTech Solutions | **100** ⚠️ | 8 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 3 |
| `207.175.58[.]196` | BE | Google LLC | **100** ⚠️ | 0 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `3.19.32[.]17` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `1.27.251[.]252` | CN | China unicom InnerMongolia province network | **100** ⚠️ | 5 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `85.217.149[.]26` | CA | NL MODAT | **100** ⚠️ | 50 |
| `65.49.1[.]132` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 184 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 174 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 595 cases |
| Tool 34  | Credential Extractor        | ✅ 187 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (1.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 42 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 173 priority case(s) shown individually · 23 recon entry/entries in table (10 group(s) consolidating 400 session(s)).

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
_Report time: 2026-06-27T10:13:16Z_

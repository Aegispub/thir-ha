# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-23 |
| **Generated At** | 2026-06-23T23:11:09Z |
| **Shift Time** | 23:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **459** |
| Confirmed Threats | **425** |
| False Positives Filtered | **34** (7.4%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **12** |
| High Severity Cases | **172** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **287** |
| Malware Samples Analyzed | **4** HIGH · **24** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **172** |
| Unique Credential Pairs | **164** |
| Unique Usernames | **95** |
| Unique Passwords | **150** |
| Successful Auth Pairs | **169** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 56 |
| `ubuntu` | 8 |
| `admin` | 4 |
| `GET / HTTP/1.1` | 4 |
| `*1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 9 |
| `admin` | 4 |
| `123` | 4 |
| `Host: 129.80.119.236:23` | 3 |
| `$4` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 4 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 3 |
| `*1` | `$4` | 3 |
| `root` | `smo@@kkklss` | 2 |
| `root` | `xsw21qaz` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `xsw21qaz` | `209.99.185.59` | 2026-06-23T20:55:40 |
| `root` | `Password1234567` | `209.99.185.59` | 2026-06-23T20:56:32 |
| `root` | `ashley` | `45.205.1.42` | 2026-06-23T20:56:47 |
| `fanwenhao` | `fanwenhao` | `209.99.185.59` | 2026-06-23T20:57:23 |
| `vtu` | `123456` | `209.99.185.59` | 2026-06-23T20:58:15 |
| `root` | `1q` | `209.99.185.59` | 2026-06-23T20:59:08 |
| `songjiebo` | `songjiebo` | `209.99.185.59` | 2026-06-23T21:00:01 |
| `duxuan20` | `duxuan20` | `209.99.185.59` | 2026-06-23T21:00:52 |
| `root` | `Passw0rd11` | `209.99.185.59` | 2026-06-23T21:01:42 |
| `root` | `Password12` | `209.99.185.59` | 2026-06-23T21:02:33 |
| `kali` | `kali` | `209.99.185.59` | 2026-06-23T21:03:24 |
| `zhangyanqing` | `zhangyanqing` | `209.99.185.59` | 2026-06-23T21:04:17 |
| `root` | `d` | `209.99.185.59` | 2026-06-23T21:05:10 |
| `root` | `0p!QAZ2wsx#E` | `209.99.185.59` | 2026-06-23T21:06:02 |
| `nagios` | `siogan` | `209.99.185.59` | 2026-06-23T21:06:53 |
| `root` | `0123!@#` | `209.99.185.59` | 2026-06-23T21:07:43 |
| `root` | `root123@` | `209.99.185.59` | 2026-06-23T21:08:33 |
| `kym` | `kym` | `209.99.185.59` | 2026-06-23T21:09:26 |
| `root` | `qwec0bra222` | `209.99.185.59` | 2026-06-23T21:10:20 |
| `root` | `---fuck_you----` | `118.145.151.135` | 2026-06-23T21:10:43 |
| `root` | `Pa18259w0rd` | `45.205.1.42` | 2026-06-23T21:11:09 |
| `huang` | `123456` | `209.99.185.59` | 2026-06-23T21:11:15 |
| `zabbix` | `123456789` | `209.99.185.59` | 2026-06-23T21:12:09 |
| `group_15` | `group_15` | `209.99.185.59` | 2026-06-23T21:13:02 |
| `username` | `password` | `209.99.185.59` | 2026-06-23T21:13:55 |
| `root` | `asdqwe` | `209.99.185.59` | 2026-06-23T21:14:49 |
| `guest` | `q1w2e3` | `209.99.185.59` | 2026-06-23T21:15:43 |
| `root` | `P@$$w0rd!` | `209.99.185.59` | 2026-06-23T21:16:38 |
| `root` | `Passw0rd1111` | `209.99.185.59` | 2026-06-23T21:17:32 |
| `iexcel` | `iexcel111111` | `209.99.185.59` | 2026-06-23T21:18:25 |
| `mysql` | `123321` | `209.99.185.59` | 2026-06-23T21:19:16 |
| `root` | `ZAQ12WSX` | `209.99.185.59` | 2026-06-23T21:20:08 |
| `dawentao` | `dawentao` | `209.99.185.59` | 2026-06-23T21:20:59 |
| `root` | `(*&^%$#@!` | `209.99.185.59` | 2026-06-23T21:21:52 |
| `root` | `QWExsw123!@#` | `209.99.185.59` | 2026-06-23T21:22:45 |
| `june` | `june` | `209.99.185.59` | 2026-06-23T21:23:39 |
| `anonymous` | `anonymous1` | `209.99.185.59` | 2026-06-23T21:24:31 |
| `hqj` | `hqj` | `209.99.185.59` | 2026-06-23T21:25:22 |
| `root` | `123456aA@` | `45.205.1.42` | 2026-06-23T21:25:37 |
| `amandabackup` | `123456` | `209.99.185.59` | 2026-06-23T21:26:13 |
| `user` | `P@ssw0rd` | `209.99.185.59` | 2026-06-23T21:27:04 |
| `dell` | `1234` | `209.99.185.59` | 2026-06-23T21:27:56 |
| `root` | `12345qwert!@#$%` | `209.99.185.59` | 2026-06-23T21:28:48 |
| `root` | `q1w2e3,.` | `209.99.185.59` | 2026-06-23T21:29:39 |
| `yujc` | `jiayu-ch15` | `209.99.185.59` | 2026-06-23T21:30:31 |
| `db2inst` | `db2inst` | `209.99.185.59` | 2026-06-23T21:31:21 |
| `pdu` | `pdu` | `209.99.185.59` | 2026-06-23T21:32:12 |
| `sales` | `password` | `209.99.185.59` | 2026-06-23T21:33:01 |
| `ubuntu` | `12345678` | `209.99.185.59` | 2026-06-23T21:33:51 |
| `zll` | `QWEasdzxc123` | `209.99.185.59` | 2026-06-23T21:34:42 |
| `root` | `passwd123!@#` | `209.99.185.59` | 2026-06-23T21:35:34 |
| `front` | `front` | `209.99.185.59` | 2026-06-23T21:36:27 |
| `yunfei` | `yunfei123` | `209.99.185.59` | 2026-06-23T21:37:21 |
| `testuser` | `q1w2e3` | `209.99.185.59` | 2026-06-23T21:38:14 |
| `user` | `bjtunlp-194` | `209.99.185.59` | 2026-06-23T21:39:07 |
| `lu` | `lu` | `209.99.185.59` | 2026-06-23T21:39:57 |
| `root` | `Pass0wrd` | `45.205.1.42` | 2026-06-23T21:40:09 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-23T21:40:11 |
| `test3` | `123456` | `209.99.185.59` | 2026-06-23T21:40:50 |
| `manager` | `manager` | `209.99.185.59` | 2026-06-23T21:41:42 |
| `zhangsan` | `zhangsan1` | `209.99.185.59` | 2026-06-23T21:42:36 |
| `root` | `628` | `209.99.185.59` | 2026-06-23T21:43:31 |
| `tiany` | `123456` | `209.99.185.59` | 2026-06-23T21:44:25 |
| `gyx` | `gyx` | `209.99.185.59` | 2026-06-23T21:45:19 |
| `xyj` | `123456` | `209.99.185.59` | 2026-06-23T21:46:11 |
| `liuyang` | `liuyang123` | `209.99.185.59` | 2026-06-23T21:47:04 |
| `root` | `private` | `209.99.185.59` | 2026-06-23T21:48:00 |
| `cc` | `cc0118` | `209.99.185.59` | 2026-06-23T21:48:56 |
| `community` | `community` | `209.99.185.59` | 2026-06-23T21:49:51 |
| `dell` | `dell123` | `209.99.185.59` | 2026-06-23T21:50:46 |
| `whh` | `19901213` | `209.99.185.59` | 2026-06-23T21:51:41 |
| `nagios` | `qwerty123` | `209.99.185.59` | 2026-06-23T21:52:36 |
| `gbkim` | `gbkim` | `209.99.185.59` | 2026-06-23T21:53:32 |
| `czy` | `czy` | `209.99.185.59` | 2026-06-23T21:54:29 |
| `root` | `hosting` | `45.205.1.42` | 2026-06-23T21:54:41 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.22.222.217` | 2026-06-23T21:55:12 |
| `*1` | `$4` | `34.22.222.217` | 2026-06-23T21:55:20 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2972` | `34.22.222.217` | 2026-06-23T21:55:22 |
| `ubuntu` | `abc123` | `209.99.185.59` | 2026-06-23T21:55:27 |
| `lbsweb` | `ypfamily608` | `209.99.185.59` | 2026-06-23T21:56:25 |
| `root` | `changeme123` | `209.99.185.59` | 2026-06-23T21:57:22 |
| `root` | `sanhe123` | `209.99.185.59` | 2026-06-23T21:58:16 |
| `ethos` | `ethos` | `209.99.185.59` | 2026-06-23T21:59:09 |
| `root` | `P@ss!@#123` | `209.99.185.59` | 2026-06-23T22:00:03 |
| `ftp` | `123` | `209.99.185.59` | 2026-06-23T22:00:49 |
| `copy` | `copy` | `209.99.185.59` | 2026-06-23T22:01:33 |
| `mobile1` | `mobile1` | `209.99.185.59` | 2026-06-23T22:02:18 |
| `root` | `qazwsx123123` | `209.99.185.59` | 2026-06-23T22:03:02 |
| `huawei` | `huawei@123` | `209.99.185.59` | 2026-06-23T22:03:45 |
| `nx` | `222222` | `209.99.185.59` | 2026-06-23T22:04:27 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-23T22:05:02 |
| `testuser` | `qwerty` | `209.99.185.59` | 2026-06-23T22:05:09 |
| `root` | `0000000000` | `209.99.185.59` | 2026-06-23T22:05:51 |
| `cic` | `cic` | `209.99.185.59` | 2026-06-23T22:06:34 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.187.78.126` | 2026-06-23T22:06:42 |
| `*1` | `$4` | `35.187.78.126` | 2026-06-23T22:06:56 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8217` | `35.187.78.126` | 2026-06-23T22:06:58 |
| `xxy` | `xxy123456` | `209.99.185.59` | 2026-06-23T22:07:19 |
| `chjiang` | `jch19979` | `209.99.185.59` | 2026-06-23T22:08:04 |
| `ubuntu` | `demo123` | `209.99.185.59` | 2026-06-23T22:08:48 |
| `chw` | `chw` | `45.205.1.42` | 2026-06-23T22:08:57 |
| `qinningxin` | `qinningxin` | `209.99.185.59` | 2026-06-23T22:09:32 |
| `lyl` | `lyl123456` | `209.99.185.59` | 2026-06-23T22:10:16 |
| `web1` | `123` | `209.99.185.59` | 2026-06-23T22:10:59 |
| `tom` | `tom123` | `209.99.185.59` | 2026-06-23T22:11:43 |
| `ubuntu` | `admin222` | `209.99.185.59` | 2026-06-23T22:12:27 |
| `casa` | `casa` | `209.99.185.59` | 2026-06-23T22:13:11 |
| `fl` | `fl123456` | `209.99.185.59` | 2026-06-23T22:13:58 |
| `gpu` | `gpu123` | `209.99.185.59` | 2026-06-23T22:14:45 |
| `hh` | `hh1234` | `209.99.185.59` | 2026-06-23T22:15:31 |
| `root` | `QWEasd123!@#` | `209.99.185.59` | 2026-06-23T22:16:18 |
| `pul` | `test321` | `209.99.185.59` | 2026-06-23T22:17:03 |
| `wanzzc` | `wanzzc` | `209.99.185.59` | 2026-06-23T22:17:49 |
| `root` | `Kifa3031!` | `209.99.185.59` | 2026-06-23T22:18:34 |
| `zhanj` | `123` | `209.99.185.59` | 2026-06-23T22:19:20 |
| `hinjonge` | `yunie153` | `209.99.185.59` | 2026-06-23T22:20:06 |
| `root` | `kedacom` | `209.99.185.59` | 2026-06-23T22:20:54 |
| `test` | `test1234` | `209.99.185.59` | 2026-06-23T22:21:42 |
| `root` | `qwerty.` | `209.99.185.59` | 2026-06-23T22:22:31 |
| `root` | `1a2b3c4d5e` | `209.99.185.59` | 2026-06-23T22:23:18 |
| `root` | `Qwe1!234` | `45.205.1.42` | 2026-06-23T22:23:22 |
| `root` | `qwert123` | `209.99.185.59` | 2026-06-23T22:24:06 |
| `usuario` | `111111` | `209.99.185.59` | 2026-06-23T22:24:55 |
| `server` | `1q2w3e4r` | `209.99.185.59` | 2026-06-23T22:25:43 |
| `iot` | `iot` | `209.99.185.59` | 2026-06-23T22:26:32 |
| `root` | `741258` | `209.99.185.59` | 2026-06-23T22:27:24 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.83` | 2026-06-23T22:27:25 |
| `lyj` | `liuyijie` | `209.99.185.59` | 2026-06-23T22:28:14 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.67.56` | 2026-06-23T22:28:28 |
| `*1` | `$4` | `34.62.67.56` | 2026-06-23T22:28:42 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7427` | `34.62.67.56` | 2026-06-23T22:28:44 |
| `bioinfo` | `bioinfo123` | `209.99.185.59` | 2026-06-23T22:29:04 |
| `buero3` | `buero31234` | `209.99.185.59` | 2026-06-23T22:29:53 |
| `fuzz` | `123456` | `209.99.185.59` | 2026-06-23T22:30:42 |
| `zhan` | `ctrl1995mbpy` | `209.99.185.59` | 2026-06-23T22:31:32 |
| `root` | `1q2w3e4R` | `209.99.185.59` | 2026-06-23T22:32:21 |
| `root` | `CoiaPrant#CentOS7` | `209.99.185.59` | 2026-06-23T22:33:12 |
| `root` | `P4ssword` | `209.99.185.59` | 2026-06-23T22:34:02 |
| `fanslau` | `666666` | `209.99.185.59` | 2026-06-23T22:34:53 |
| `root` | `8ik0p;/;QAZ` | `209.99.185.59` | 2026-06-23T22:35:43 |
| `test3` | `123` | `209.99.185.59` | 2026-06-23T22:36:32 |
| `weblogic` | `wasd` | `209.99.185.59` | 2026-06-23T22:37:20 |
| `ubuntu` | `123321123321` | `45.205.1.42` | 2026-06-23T22:37:35 |
| `oracle` | `112uw009e!rR` | `209.99.185.59` | 2026-06-23T22:38:09 |
| `root` | `123456Ab` | `209.99.185.59` | 2026-06-23T22:39:08 |
| `root` | `4r3e2w1q` | `209.99.185.59` | 2026-06-23T22:40:06 |
| `root` | `﻿------fuck------` | `58.210.39.254` | 2026-06-23T22:40:28 |
| `root` | `123456a@` | `209.99.185.59` | 2026-06-23T22:40:57 |
| `nms` | `nms123456` | `209.99.185.59` | 2026-06-23T22:41:46 |
| `test2` | `111111` | `209.99.185.59` | 2026-06-23T22:42:35 |
| `sbs` | `123456` | `209.99.185.59` | 2026-06-23T22:43:23 |
| `swn` | `swn` | `209.99.185.59` | 2026-06-23T22:44:11 |
| `jwoo` | `1111` | `209.99.185.59` | 2026-06-23T22:44:59 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-23T22:45:07 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-23T22:45:08 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-23T22:45:08 |
| `ubuntu` | `Qwer!234` | `209.99.185.59` | 2026-06-23T22:45:49 |
| `sg` | `korea2013` | `209.99.185.59` | 2026-06-23T22:46:38 |
| `root` | `QAZwsxEDCrfv` | `209.99.185.59` | 2026-06-23T22:47:27 |
| `root` | `qwertyasdfgh` | `209.99.185.59` | 2026-06-23T22:48:17 |
| `app` | `app@123` | `209.99.185.59` | 2026-06-23T22:49:06 |
| `root` | `Fedora7` | `209.99.185.59` | 2026-06-23T22:49:53 |
| `root` | `windows200` | `209.99.185.59` | 2026-06-23T22:50:40 |
| `netscreen` | `netscreen` | `209.99.185.59` | 2026-06-23T22:51:28 |
| `ubuntu` | `P@ssw0rd!` | `45.205.1.42` | 2026-06-23T22:51:44 |
| `tkms` | `123456` | `209.99.185.59` | 2026-06-23T22:52:16 |
| `wl` | `wl20020119` | `209.99.185.59` | 2026-06-23T22:53:07 |
| `won` | `won12` | `209.99.185.59` | 2026-06-23T22:53:56 |
| `ubuntu` | `asd12` | `209.99.185.59` | 2026-06-23T22:54:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **459** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 160 |
| libssh | 20 |
| Paramiko (Python) | 4 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 152 | 2 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |
| `e37f354a101a...` | Mirai/variant | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 152 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 17 | 4 | — |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `e37f354a101a...` | libssh | 3 | 3 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Unknown | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **20** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 8 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS10439` | CariNet, Inc. | 1 | HIGH |
| `AS51396` | Pfcloud UG | 1 | MEDIUM |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | MEDIUM |
| `AS215925` | VPSVAULT.HOST LTD | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (169)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-55383c31fb0d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:55 |
| **Last Seen** | 2026-06-23 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:55:40` | `cowrie.session.connect` |
| `2026-06-23 20:55:40` | `cowrie.client.version` |
| `2026-06-23 20:55:40` | `cowrie.client.kex` |
| `2026-06-23 20:55:40` | `cowrie.login.success` |
| `2026-06-23 20:55:41` | `cowrie.session.params` |
| `2026-06-23 20:55:41` | `cowrie.command.input` |
| `2026-06-23 20:55:42` | `cowrie.log.closed` |
| `2026-06-23 20:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d1efcc44b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:56 |
| **Last Seen** | 2026-06-23 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:56:32` | `cowrie.session.connect` |
| `2026-06-23 20:56:32` | `cowrie.client.version` |
| `2026-06-23 20:56:32` | `cowrie.client.kex` |
| `2026-06-23 20:56:32` | `cowrie.login.success` |
| `2026-06-23 20:56:33` | `cowrie.session.params` |
| `2026-06-23 20:56:33` | `cowrie.command.input` |
| `2026-06-23 20:56:33` | `cowrie.log.closed` |
| `2026-06-23 20:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c4eeeb223bb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 20:56 |
| **Last Seen** | 2026-06-23 20:56 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:56:39` | `cowrie.session.connect` |
| `2026-06-23 20:56:40` | `cowrie.client.version` |
| `2026-06-23 20:56:40` | `cowrie.client.kex` |
| `2026-06-23 20:56:47` | `cowrie.login.success` |
| `2026-06-23 20:56:51` | `cowrie.session.params` |
| `2026-06-23 20:56:51` | `cowrie.command.input` |
| `2026-06-23 20:56:53` | `cowrie.log.closed` |
| `2026-06-23 20:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de73ebcb6fbb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:57 |
| **Last Seen** | 2026-06-23 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:57:23` | `cowrie.session.connect` |
| `2026-06-23 20:57:23` | `cowrie.client.version` |
| `2026-06-23 20:57:23` | `cowrie.client.kex` |
| `2026-06-23 20:57:23` | `cowrie.login.success` |
| `2026-06-23 20:57:24` | `cowrie.session.params` |
| `2026-06-23 20:57:24` | `cowrie.command.input` |
| `2026-06-23 20:57:24` | `cowrie.log.closed` |
| `2026-06-23 20:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689c627bc3f5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:58 |
| **Last Seen** | 2026-06-23 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:58:14` | `cowrie.session.connect` |
| `2026-06-23 20:58:14` | `cowrie.client.version` |
| `2026-06-23 20:58:14` | `cowrie.client.kex` |
| `2026-06-23 20:58:15` | `cowrie.login.success` |
| `2026-06-23 20:58:15` | `cowrie.session.params` |
| `2026-06-23 20:58:15` | `cowrie.command.input` |
| `2026-06-23 20:58:16` | `cowrie.log.closed` |
| `2026-06-23 20:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e48ad4d21df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 20:59 |
| **Last Seen** | 2026-06-23 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 20:59:08` | `cowrie.session.connect` |
| `2026-06-23 20:59:08` | `cowrie.client.version` |
| `2026-06-23 20:59:08` | `cowrie.client.kex` |
| `2026-06-23 20:59:08` | `cowrie.login.success` |
| `2026-06-23 20:59:09` | `cowrie.session.params` |
| `2026-06-23 20:59:09` | `cowrie.command.input` |
| `2026-06-23 20:59:09` | `cowrie.log.closed` |
| `2026-06-23 20:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd6b88ee082

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:00 |
| **Last Seen** | 2026-06-23 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:00:01` | `cowrie.session.connect` |
| `2026-06-23 21:00:01` | `cowrie.client.version` |
| `2026-06-23 21:00:01` | `cowrie.client.kex` |
| `2026-06-23 21:00:01` | `cowrie.login.success` |
| `2026-06-23 21:00:02` | `cowrie.session.params` |
| `2026-06-23 21:00:02` | `cowrie.command.input` |
| `2026-06-23 21:00:02` | `cowrie.log.closed` |
| `2026-06-23 21:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de30e418cb7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:00 |
| **Last Seen** | 2026-06-23 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:00:52` | `cowrie.session.connect` |
| `2026-06-23 21:00:52` | `cowrie.client.version` |
| `2026-06-23 21:00:52` | `cowrie.client.kex` |
| `2026-06-23 21:00:52` | `cowrie.login.success` |
| `2026-06-23 21:00:53` | `cowrie.session.params` |
| `2026-06-23 21:00:53` | `cowrie.command.input` |
| `2026-06-23 21:00:53` | `cowrie.log.closed` |
| `2026-06-23 21:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c469cb2b03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:01 |
| **Last Seen** | 2026-06-23 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:01:41` | `cowrie.session.connect` |
| `2026-06-23 21:01:41` | `cowrie.client.version` |
| `2026-06-23 21:01:42` | `cowrie.client.kex` |
| `2026-06-23 21:01:42` | `cowrie.login.success` |
| `2026-06-23 21:01:43` | `cowrie.session.params` |
| `2026-06-23 21:01:43` | `cowrie.command.input` |
| `2026-06-23 21:01:43` | `cowrie.log.closed` |
| `2026-06-23 21:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f288ec47166

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:02 |
| **Last Seen** | 2026-06-23 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:02:33` | `cowrie.session.connect` |
| `2026-06-23 21:02:33` | `cowrie.client.version` |
| `2026-06-23 21:02:33` | `cowrie.client.kex` |
| `2026-06-23 21:02:33` | `cowrie.login.success` |
| `2026-06-23 21:02:34` | `cowrie.session.params` |
| `2026-06-23 21:02:34` | `cowrie.command.input` |
| `2026-06-23 21:02:34` | `cowrie.log.closed` |
| `2026-06-23 21:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d9838cd975

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:03 |
| **Last Seen** | 2026-06-23 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:03:24` | `cowrie.session.connect` |
| `2026-06-23 21:03:24` | `cowrie.client.version` |
| `2026-06-23 21:03:24` | `cowrie.client.kex` |
| `2026-06-23 21:03:24` | `cowrie.login.success` |
| `2026-06-23 21:03:25` | `cowrie.session.params` |
| `2026-06-23 21:03:25` | `cowrie.command.input` |
| `2026-06-23 21:03:25` | `cowrie.log.closed` |
| `2026-06-23 21:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d016fddd3d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:04 |
| **Last Seen** | 2026-06-23 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:04:16` | `cowrie.session.connect` |
| `2026-06-23 21:04:16` | `cowrie.client.version` |
| `2026-06-23 21:04:16` | `cowrie.client.kex` |
| `2026-06-23 21:04:17` | `cowrie.login.success` |
| `2026-06-23 21:04:18` | `cowrie.session.params` |
| `2026-06-23 21:04:18` | `cowrie.command.input` |
| `2026-06-23 21:04:18` | `cowrie.log.closed` |
| `2026-06-23 21:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-befdaecfd472

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:05 |
| **Last Seen** | 2026-06-23 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:05:09` | `cowrie.session.connect` |
| `2026-06-23 21:05:09` | `cowrie.client.version` |
| `2026-06-23 21:05:09` | `cowrie.client.kex` |
| `2026-06-23 21:05:10` | `cowrie.login.success` |
| `2026-06-23 21:05:10` | `cowrie.session.params` |
| `2026-06-23 21:05:10` | `cowrie.command.input` |
| `2026-06-23 21:05:10` | `cowrie.log.closed` |
| `2026-06-23 21:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d043666dba2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:06 |
| **Last Seen** | 2026-06-23 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:06:02` | `cowrie.session.connect` |
| `2026-06-23 21:06:02` | `cowrie.client.version` |
| `2026-06-23 21:06:02` | `cowrie.client.kex` |
| `2026-06-23 21:06:02` | `cowrie.login.success` |
| `2026-06-23 21:06:03` | `cowrie.session.params` |
| `2026-06-23 21:06:03` | `cowrie.command.input` |
| `2026-06-23 21:06:03` | `cowrie.log.closed` |
| `2026-06-23 21:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2070766ee4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:06 |
| **Last Seen** | 2026-06-23 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:06:52` | `cowrie.session.connect` |
| `2026-06-23 21:06:52` | `cowrie.client.version` |
| `2026-06-23 21:06:52` | `cowrie.client.kex` |
| `2026-06-23 21:06:53` | `cowrie.login.success` |
| `2026-06-23 21:06:53` | `cowrie.session.params` |
| `2026-06-23 21:06:53` | `cowrie.command.input` |
| `2026-06-23 21:06:54` | `cowrie.log.closed` |
| `2026-06-23 21:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef383d95b23

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:07 |
| **Last Seen** | 2026-06-23 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:07:42` | `cowrie.session.connect` |
| `2026-06-23 21:07:42` | `cowrie.client.version` |
| `2026-06-23 21:07:43` | `cowrie.client.kex` |
| `2026-06-23 21:07:43` | `cowrie.login.success` |
| `2026-06-23 21:07:44` | `cowrie.session.params` |
| `2026-06-23 21:07:44` | `cowrie.command.input` |
| `2026-06-23 21:07:44` | `cowrie.log.closed` |
| `2026-06-23 21:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5454c8d40e3f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:08 |
| **Last Seen** | 2026-06-23 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:08:33` | `cowrie.session.connect` |
| `2026-06-23 21:08:33` | `cowrie.client.version` |
| `2026-06-23 21:08:33` | `cowrie.client.kex` |
| `2026-06-23 21:08:33` | `cowrie.login.success` |
| `2026-06-23 21:08:34` | `cowrie.session.params` |
| `2026-06-23 21:08:34` | `cowrie.command.input` |
| `2026-06-23 21:08:34` | `cowrie.log.closed` |
| `2026-06-23 21:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3265e65ad8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:09 |
| **Last Seen** | 2026-06-23 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:09:25` | `cowrie.session.connect` |
| `2026-06-23 21:09:25` | `cowrie.client.version` |
| `2026-06-23 21:09:25` | `cowrie.client.kex` |
| `2026-06-23 21:09:26` | `cowrie.login.success` |
| `2026-06-23 21:09:26` | `cowrie.session.params` |
| `2026-06-23 21:09:26` | `cowrie.command.input` |
| `2026-06-23 21:09:27` | `cowrie.log.closed` |
| `2026-06-23 21:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d8a2040c41

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:10 |
| **Last Seen** | 2026-06-23 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:10:19` | `cowrie.session.connect` |
| `2026-06-23 21:10:19` | `cowrie.client.version` |
| `2026-06-23 21:10:19` | `cowrie.client.kex` |
| `2026-06-23 21:10:20` | `cowrie.login.success` |
| `2026-06-23 21:10:21` | `cowrie.session.params` |
| `2026-06-23 21:10:21` | `cowrie.command.input` |
| `2026-06-23 21:10:21` | `cowrie.log.closed` |
| `2026-06-23 21:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954339ebde1a

| Field | Detail |
|---|---|
| **Source IP** | `118.145.151[.]135` |
| **First Seen** | 2026-06-23 21:10 |
| **Last Seen** | 2026-06-23 21:15 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:10:42` | `cowrie.session.connect` |
| `2026-06-23 21:10:42` | `cowrie.client.version` |
| `2026-06-23 21:10:42` | `cowrie.client.kex` |
| `2026-06-23 21:10:43` | `cowrie.login.success` |
| `2026-06-23 21:10:45` | `cowrie.session.params` |
| `2026-06-23 21:10:45` | `cowrie.command.input` |
| `2026-06-23 21:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.151[.]135` to AbuseIPDB if not already reported
- [ ] Block `118.145.151[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ff6f7c7602

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 21:11 |
| **Last Seen** | 2026-06-23 21:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:11:01` | `cowrie.session.connect` |
| `2026-06-23 21:11:02` | `cowrie.client.version` |
| `2026-06-23 21:11:02` | `cowrie.client.kex` |
| `2026-06-23 21:11:09` | `cowrie.login.success` |
| `2026-06-23 21:11:13` | `cowrie.session.params` |
| `2026-06-23 21:11:13` | `cowrie.command.input` |
| `2026-06-23 21:11:15` | `cowrie.log.closed` |
| `2026-06-23 21:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46911895adb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:11 |
| **Last Seen** | 2026-06-23 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:11:14` | `cowrie.session.connect` |
| `2026-06-23 21:11:14` | `cowrie.client.version` |
| `2026-06-23 21:11:15` | `cowrie.client.kex` |
| `2026-06-23 21:11:15` | `cowrie.login.success` |
| `2026-06-23 21:11:16` | `cowrie.session.params` |
| `2026-06-23 21:11:16` | `cowrie.command.input` |
| `2026-06-23 21:11:16` | `cowrie.log.closed` |
| `2026-06-23 21:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d618f9941942

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:12 |
| **Last Seen** | 2026-06-23 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:12:08` | `cowrie.session.connect` |
| `2026-06-23 21:12:08` | `cowrie.client.version` |
| `2026-06-23 21:12:08` | `cowrie.client.kex` |
| `2026-06-23 21:12:09` | `cowrie.login.success` |
| `2026-06-23 21:12:10` | `cowrie.session.params` |
| `2026-06-23 21:12:10` | `cowrie.command.input` |
| `2026-06-23 21:12:10` | `cowrie.log.closed` |
| `2026-06-23 21:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c8c86cba56

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:13 |
| **Last Seen** | 2026-06-23 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:13:02` | `cowrie.session.connect` |
| `2026-06-23 21:13:02` | `cowrie.client.version` |
| `2026-06-23 21:13:02` | `cowrie.client.kex` |
| `2026-06-23 21:13:02` | `cowrie.login.success` |
| `2026-06-23 21:13:03` | `cowrie.session.params` |
| `2026-06-23 21:13:03` | `cowrie.command.input` |
| `2026-06-23 21:13:03` | `cowrie.log.closed` |
| `2026-06-23 21:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d1bd9298fdf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:13 |
| **Last Seen** | 2026-06-23 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:13:55` | `cowrie.session.connect` |
| `2026-06-23 21:13:55` | `cowrie.client.version` |
| `2026-06-23 21:13:55` | `cowrie.client.kex` |
| `2026-06-23 21:13:55` | `cowrie.login.success` |
| `2026-06-23 21:13:56` | `cowrie.session.params` |
| `2026-06-23 21:13:56` | `cowrie.command.input` |
| `2026-06-23 21:13:56` | `cowrie.log.closed` |
| `2026-06-23 21:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f9fcf925a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:14 |
| **Last Seen** | 2026-06-23 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:14:48` | `cowrie.session.connect` |
| `2026-06-23 21:14:48` | `cowrie.client.version` |
| `2026-06-23 21:14:48` | `cowrie.client.kex` |
| `2026-06-23 21:14:49` | `cowrie.login.success` |
| `2026-06-23 21:14:50` | `cowrie.session.params` |
| `2026-06-23 21:14:50` | `cowrie.command.input` |
| `2026-06-23 21:14:50` | `cowrie.log.closed` |
| `2026-06-23 21:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b312d4032230

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:15 |
| **Last Seen** | 2026-06-23 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:15:42` | `cowrie.session.connect` |
| `2026-06-23 21:15:42` | `cowrie.client.version` |
| `2026-06-23 21:15:42` | `cowrie.client.kex` |
| `2026-06-23 21:15:43` | `cowrie.login.success` |
| `2026-06-23 21:15:43` | `cowrie.session.params` |
| `2026-06-23 21:15:43` | `cowrie.command.input` |
| `2026-06-23 21:15:43` | `cowrie.log.closed` |
| `2026-06-23 21:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d00f9b362d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:16 |
| **Last Seen** | 2026-06-23 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:16:37` | `cowrie.session.connect` |
| `2026-06-23 21:16:37` | `cowrie.client.version` |
| `2026-06-23 21:16:37` | `cowrie.client.kex` |
| `2026-06-23 21:16:38` | `cowrie.login.success` |
| `2026-06-23 21:16:39` | `cowrie.session.params` |
| `2026-06-23 21:16:39` | `cowrie.command.input` |
| `2026-06-23 21:16:39` | `cowrie.log.closed` |
| `2026-06-23 21:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4e64f252cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:17 |
| **Last Seen** | 2026-06-23 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:17:31` | `cowrie.session.connect` |
| `2026-06-23 21:17:31` | `cowrie.client.version` |
| `2026-06-23 21:17:31` | `cowrie.client.kex` |
| `2026-06-23 21:17:32` | `cowrie.login.success` |
| `2026-06-23 21:17:32` | `cowrie.session.params` |
| `2026-06-23 21:17:32` | `cowrie.command.input` |
| `2026-06-23 21:17:32` | `cowrie.log.closed` |
| `2026-06-23 21:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736024d6cc10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:18 |
| **Last Seen** | 2026-06-23 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:18:24` | `cowrie.session.connect` |
| `2026-06-23 21:18:24` | `cowrie.client.version` |
| `2026-06-23 21:18:24` | `cowrie.client.kex` |
| `2026-06-23 21:18:25` | `cowrie.login.success` |
| `2026-06-23 21:18:26` | `cowrie.session.params` |
| `2026-06-23 21:18:26` | `cowrie.command.input` |
| `2026-06-23 21:18:26` | `cowrie.log.closed` |
| `2026-06-23 21:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fcbb4da00f5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:19 |
| **Last Seen** | 2026-06-23 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:19:16` | `cowrie.session.connect` |
| `2026-06-23 21:19:16` | `cowrie.client.version` |
| `2026-06-23 21:19:16` | `cowrie.client.kex` |
| `2026-06-23 21:19:16` | `cowrie.login.success` |
| `2026-06-23 21:19:17` | `cowrie.session.params` |
| `2026-06-23 21:19:17` | `cowrie.command.input` |
| `2026-06-23 21:19:17` | `cowrie.log.closed` |
| `2026-06-23 21:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687ad7d3045f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:20 |
| **Last Seen** | 2026-06-23 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:20:08` | `cowrie.session.connect` |
| `2026-06-23 21:20:08` | `cowrie.client.version` |
| `2026-06-23 21:20:08` | `cowrie.client.kex` |
| `2026-06-23 21:20:08` | `cowrie.login.success` |
| `2026-06-23 21:20:09` | `cowrie.session.params` |
| `2026-06-23 21:20:09` | `cowrie.command.input` |
| `2026-06-23 21:20:09` | `cowrie.log.closed` |
| `2026-06-23 21:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd4e0b674d69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:20 |
| **Last Seen** | 2026-06-23 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:20:59` | `cowrie.session.connect` |
| `2026-06-23 21:20:59` | `cowrie.client.version` |
| `2026-06-23 21:20:59` | `cowrie.client.kex` |
| `2026-06-23 21:20:59` | `cowrie.login.success` |
| `2026-06-23 21:21:00` | `cowrie.session.params` |
| `2026-06-23 21:21:00` | `cowrie.command.input` |
| `2026-06-23 21:21:00` | `cowrie.log.closed` |
| `2026-06-23 21:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c314324613

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:21 |
| **Last Seen** | 2026-06-23 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:21:51` | `cowrie.session.connect` |
| `2026-06-23 21:21:51` | `cowrie.client.version` |
| `2026-06-23 21:21:51` | `cowrie.client.kex` |
| `2026-06-23 21:21:52` | `cowrie.login.success` |
| `2026-06-23 21:21:52` | `cowrie.session.params` |
| `2026-06-23 21:21:52` | `cowrie.command.input` |
| `2026-06-23 21:21:52` | `cowrie.log.closed` |
| `2026-06-23 21:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea9884d4929

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:22 |
| **Last Seen** | 2026-06-23 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:22:44` | `cowrie.session.connect` |
| `2026-06-23 21:22:44` | `cowrie.client.version` |
| `2026-06-23 21:22:44` | `cowrie.client.kex` |
| `2026-06-23 21:22:45` | `cowrie.login.success` |
| `2026-06-23 21:22:45` | `cowrie.session.params` |
| `2026-06-23 21:22:45` | `cowrie.command.input` |
| `2026-06-23 21:22:45` | `cowrie.log.closed` |
| `2026-06-23 21:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0484942c46f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:23 |
| **Last Seen** | 2026-06-23 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:23:38` | `cowrie.session.connect` |
| `2026-06-23 21:23:38` | `cowrie.client.version` |
| `2026-06-23 21:23:39` | `cowrie.client.kex` |
| `2026-06-23 21:23:39` | `cowrie.login.success` |
| `2026-06-23 21:23:40` | `cowrie.session.params` |
| `2026-06-23 21:23:40` | `cowrie.command.input` |
| `2026-06-23 21:23:40` | `cowrie.log.closed` |
| `2026-06-23 21:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615d84b98ceb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:24 |
| **Last Seen** | 2026-06-23 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:24:31` | `cowrie.session.connect` |
| `2026-06-23 21:24:31` | `cowrie.client.version` |
| `2026-06-23 21:24:31` | `cowrie.client.kex` |
| `2026-06-23 21:24:31` | `cowrie.login.success` |
| `2026-06-23 21:24:32` | `cowrie.session.params` |
| `2026-06-23 21:24:32` | `cowrie.command.input` |
| `2026-06-23 21:24:32` | `cowrie.log.closed` |
| `2026-06-23 21:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3323d05d7d0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:25 |
| **Last Seen** | 2026-06-23 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:25:21` | `cowrie.session.connect` |
| `2026-06-23 21:25:21` | `cowrie.client.version` |
| `2026-06-23 21:25:21` | `cowrie.client.kex` |
| `2026-06-23 21:25:22` | `cowrie.login.success` |
| `2026-06-23 21:25:22` | `cowrie.session.params` |
| `2026-06-23 21:25:22` | `cowrie.command.input` |
| `2026-06-23 21:25:22` | `cowrie.log.closed` |
| `2026-06-23 21:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639fcd53044c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 21:25 |
| **Last Seen** | 2026-06-23 21:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:25:28` | `cowrie.session.connect` |
| `2026-06-23 21:25:30` | `cowrie.client.version` |
| `2026-06-23 21:25:30` | `cowrie.client.kex` |
| `2026-06-23 21:25:37` | `cowrie.login.success` |
| `2026-06-23 21:25:40` | `cowrie.session.params` |
| `2026-06-23 21:25:40` | `cowrie.command.input` |
| `2026-06-23 21:25:43` | `cowrie.log.closed` |
| `2026-06-23 21:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a160cdf0ce3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:26 |
| **Last Seen** | 2026-06-23 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:26:13` | `cowrie.session.connect` |
| `2026-06-23 21:26:13` | `cowrie.client.version` |
| `2026-06-23 21:26:13` | `cowrie.client.kex` |
| `2026-06-23 21:26:13` | `cowrie.login.success` |
| `2026-06-23 21:26:14` | `cowrie.session.params` |
| `2026-06-23 21:26:14` | `cowrie.command.input` |
| `2026-06-23 21:26:14` | `cowrie.log.closed` |
| `2026-06-23 21:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-522ee28084b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:27 |
| **Last Seen** | 2026-06-23 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:27:03` | `cowrie.session.connect` |
| `2026-06-23 21:27:03` | `cowrie.client.version` |
| `2026-06-23 21:27:04` | `cowrie.client.kex` |
| `2026-06-23 21:27:04` | `cowrie.login.success` |
| `2026-06-23 21:27:05` | `cowrie.session.params` |
| `2026-06-23 21:27:05` | `cowrie.command.input` |
| `2026-06-23 21:27:05` | `cowrie.log.closed` |
| `2026-06-23 21:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669310553ff1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:27 |
| **Last Seen** | 2026-06-23 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:27:55` | `cowrie.session.connect` |
| `2026-06-23 21:27:55` | `cowrie.client.version` |
| `2026-06-23 21:27:55` | `cowrie.client.kex` |
| `2026-06-23 21:27:56` | `cowrie.login.success` |
| `2026-06-23 21:27:57` | `cowrie.session.params` |
| `2026-06-23 21:27:57` | `cowrie.command.input` |
| `2026-06-23 21:27:57` | `cowrie.log.closed` |
| `2026-06-23 21:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb2a1659323

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:28 |
| **Last Seen** | 2026-06-23 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:28:47` | `cowrie.session.connect` |
| `2026-06-23 21:28:47` | `cowrie.client.version` |
| `2026-06-23 21:28:47` | `cowrie.client.kex` |
| `2026-06-23 21:28:48` | `cowrie.login.success` |
| `2026-06-23 21:28:48` | `cowrie.session.params` |
| `2026-06-23 21:28:48` | `cowrie.command.input` |
| `2026-06-23 21:28:48` | `cowrie.log.closed` |
| `2026-06-23 21:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7b8ead3d52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:29 |
| **Last Seen** | 2026-06-23 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:29:39` | `cowrie.session.connect` |
| `2026-06-23 21:29:39` | `cowrie.client.version` |
| `2026-06-23 21:29:39` | `cowrie.client.kex` |
| `2026-06-23 21:29:39` | `cowrie.login.success` |
| `2026-06-23 21:29:40` | `cowrie.session.params` |
| `2026-06-23 21:29:40` | `cowrie.command.input` |
| `2026-06-23 21:29:40` | `cowrie.log.closed` |
| `2026-06-23 21:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb0a35e86e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:30 |
| **Last Seen** | 2026-06-23 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:30:30` | `cowrie.session.connect` |
| `2026-06-23 21:30:30` | `cowrie.client.version` |
| `2026-06-23 21:30:30` | `cowrie.client.kex` |
| `2026-06-23 21:30:31` | `cowrie.login.success` |
| `2026-06-23 21:30:32` | `cowrie.session.params` |
| `2026-06-23 21:30:32` | `cowrie.command.input` |
| `2026-06-23 21:30:32` | `cowrie.log.closed` |
| `2026-06-23 21:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125e72cae7f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:31 |
| **Last Seen** | 2026-06-23 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:31:21` | `cowrie.session.connect` |
| `2026-06-23 21:31:21` | `cowrie.client.version` |
| `2026-06-23 21:31:21` | `cowrie.client.kex` |
| `2026-06-23 21:31:21` | `cowrie.login.success` |
| `2026-06-23 21:31:22` | `cowrie.session.params` |
| `2026-06-23 21:31:22` | `cowrie.command.input` |
| `2026-06-23 21:31:22` | `cowrie.log.closed` |
| `2026-06-23 21:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a178bfa3187f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:32 |
| **Last Seen** | 2026-06-23 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:32:11` | `cowrie.session.connect` |
| `2026-06-23 21:32:11` | `cowrie.client.version` |
| `2026-06-23 21:32:11` | `cowrie.client.kex` |
| `2026-06-23 21:32:12` | `cowrie.login.success` |
| `2026-06-23 21:32:12` | `cowrie.session.params` |
| `2026-06-23 21:32:12` | `cowrie.command.input` |
| `2026-06-23 21:32:13` | `cowrie.log.closed` |
| `2026-06-23 21:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b209d098cb0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:33 |
| **Last Seen** | 2026-06-23 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:33:01` | `cowrie.session.connect` |
| `2026-06-23 21:33:01` | `cowrie.client.version` |
| `2026-06-23 21:33:01` | `cowrie.client.kex` |
| `2026-06-23 21:33:01` | `cowrie.login.success` |
| `2026-06-23 21:33:02` | `cowrie.session.params` |
| `2026-06-23 21:33:02` | `cowrie.command.input` |
| `2026-06-23 21:33:02` | `cowrie.log.closed` |
| `2026-06-23 21:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9462eec1afb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:33 |
| **Last Seen** | 2026-06-23 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:33:51` | `cowrie.session.connect` |
| `2026-06-23 21:33:51` | `cowrie.client.version` |
| `2026-06-23 21:33:51` | `cowrie.client.kex` |
| `2026-06-23 21:33:51` | `cowrie.login.success` |
| `2026-06-23 21:33:52` | `cowrie.session.params` |
| `2026-06-23 21:33:52` | `cowrie.command.input` |
| `2026-06-23 21:33:52` | `cowrie.log.closed` |
| `2026-06-23 21:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be095c4cde46

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:34 |
| **Last Seen** | 2026-06-23 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:34:42` | `cowrie.session.connect` |
| `2026-06-23 21:34:42` | `cowrie.client.version` |
| `2026-06-23 21:34:42` | `cowrie.client.kex` |
| `2026-06-23 21:34:42` | `cowrie.login.success` |
| `2026-06-23 21:34:43` | `cowrie.session.params` |
| `2026-06-23 21:34:43` | `cowrie.command.input` |
| `2026-06-23 21:34:43` | `cowrie.log.closed` |
| `2026-06-23 21:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9415d4f6b3ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:35 |
| **Last Seen** | 2026-06-23 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:35:34` | `cowrie.session.connect` |
| `2026-06-23 21:35:34` | `cowrie.client.version` |
| `2026-06-23 21:35:34` | `cowrie.client.kex` |
| `2026-06-23 21:35:34` | `cowrie.login.success` |
| `2026-06-23 21:35:35` | `cowrie.session.params` |
| `2026-06-23 21:35:35` | `cowrie.command.input` |
| `2026-06-23 21:35:35` | `cowrie.log.closed` |
| `2026-06-23 21:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-408a7e756606

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:36 |
| **Last Seen** | 2026-06-23 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:36:27` | `cowrie.session.connect` |
| `2026-06-23 21:36:27` | `cowrie.client.version` |
| `2026-06-23 21:36:27` | `cowrie.client.kex` |
| `2026-06-23 21:36:27` | `cowrie.login.success` |
| `2026-06-23 21:36:28` | `cowrie.session.params` |
| `2026-06-23 21:36:28` | `cowrie.command.input` |
| `2026-06-23 21:36:28` | `cowrie.log.closed` |
| `2026-06-23 21:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f456620feeb7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:37 |
| **Last Seen** | 2026-06-23 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:37:21` | `cowrie.session.connect` |
| `2026-06-23 21:37:21` | `cowrie.client.version` |
| `2026-06-23 21:37:21` | `cowrie.client.kex` |
| `2026-06-23 21:37:21` | `cowrie.login.success` |
| `2026-06-23 21:37:22` | `cowrie.session.params` |
| `2026-06-23 21:37:22` | `cowrie.command.input` |
| `2026-06-23 21:37:22` | `cowrie.log.closed` |
| `2026-06-23 21:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72b6b3ae620e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:38 |
| **Last Seen** | 2026-06-23 21:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:38:14` | `cowrie.session.connect` |
| `2026-06-23 21:38:14` | `cowrie.client.version` |
| `2026-06-23 21:38:14` | `cowrie.client.kex` |
| `2026-06-23 21:38:14` | `cowrie.login.success` |
| `2026-06-23 21:38:15` | `cowrie.session.params` |
| `2026-06-23 21:38:15` | `cowrie.command.input` |
| `2026-06-23 21:38:15` | `cowrie.log.closed` |
| `2026-06-23 21:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654ff9a39ee4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:39 |
| **Last Seen** | 2026-06-23 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:39:06` | `cowrie.session.connect` |
| `2026-06-23 21:39:06` | `cowrie.client.version` |
| `2026-06-23 21:39:06` | `cowrie.client.kex` |
| `2026-06-23 21:39:07` | `cowrie.login.success` |
| `2026-06-23 21:39:08` | `cowrie.session.params` |
| `2026-06-23 21:39:08` | `cowrie.command.input` |
| `2026-06-23 21:39:08` | `cowrie.log.closed` |
| `2026-06-23 21:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bcabbb621ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:39 |
| **Last Seen** | 2026-06-23 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:39:57` | `cowrie.session.connect` |
| `2026-06-23 21:39:57` | `cowrie.client.version` |
| `2026-06-23 21:39:57` | `cowrie.client.kex` |
| `2026-06-23 21:39:57` | `cowrie.login.success` |
| `2026-06-23 21:39:58` | `cowrie.session.params` |
| `2026-06-23 21:39:58` | `cowrie.command.input` |
| `2026-06-23 21:39:58` | `cowrie.log.closed` |
| `2026-06-23 21:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db5c4589f739

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 21:40 |
| **Last Seen** | 2026-06-23 21:40 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:40:01` | `cowrie.session.connect` |
| `2026-06-23 21:40:02` | `cowrie.client.version` |
| `2026-06-23 21:40:02` | `cowrie.client.kex` |
| `2026-06-23 21:40:09` | `cowrie.login.success` |
| `2026-06-23 21:40:13` | `cowrie.session.params` |
| `2026-06-23 21:40:13` | `cowrie.command.input` |
| `2026-06-23 21:40:14` | `cowrie.log.closed` |
| `2026-06-23 21:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a427934086

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-23 21:40 |
| **Last Seen** | 2026-06-23 21:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:40:11` | `cowrie.session.connect` |
| `2026-06-23 21:40:11` | `cowrie.client.version` |
| `2026-06-23 21:40:11` | `cowrie.client.kex` |
| `2026-06-23 21:40:11` | `cowrie.login.success` |
| `2026-06-23 21:40:11` | `cowrie.direct-tcpip.request` |
| `2026-06-23 21:40:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-23 21:40:11` | `cowrie.direct-tcpip.data` |
| `2026-06-23 21:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb65167b357

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-23 21:40 |
| **Last Seen** | 2026-06-23 21:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:40:11` | `cowrie.session.connect` |
| `2026-06-23 21:40:11` | `cowrie.client.version` |
| `2026-06-23 21:40:12` | `cowrie.client.kex` |
| `2026-06-23 21:40:12` | `cowrie.login.success` |
| `2026-06-23 21:40:12` | `cowrie.direct-tcpip.request` |
| `2026-06-23 21:40:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-23 21:40:12` | `cowrie.direct-tcpip.data` |
| `2026-06-23 21:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b5d93e20d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:40 |
| **Last Seen** | 2026-06-23 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:40:49` | `cowrie.session.connect` |
| `2026-06-23 21:40:49` | `cowrie.client.version` |
| `2026-06-23 21:40:50` | `cowrie.client.kex` |
| `2026-06-23 21:40:50` | `cowrie.login.success` |
| `2026-06-23 21:40:51` | `cowrie.session.params` |
| `2026-06-23 21:40:51` | `cowrie.command.input` |
| `2026-06-23 21:40:51` | `cowrie.log.closed` |
| `2026-06-23 21:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42db9f1045a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:41 |
| **Last Seen** | 2026-06-23 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:41:42` | `cowrie.session.connect` |
| `2026-06-23 21:41:42` | `cowrie.client.version` |
| `2026-06-23 21:41:42` | `cowrie.client.kex` |
| `2026-06-23 21:41:42` | `cowrie.login.success` |
| `2026-06-23 21:41:43` | `cowrie.session.params` |
| `2026-06-23 21:41:43` | `cowrie.command.input` |
| `2026-06-23 21:41:43` | `cowrie.log.closed` |
| `2026-06-23 21:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108de6e45136

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:42 |
| **Last Seen** | 2026-06-23 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:42:36` | `cowrie.session.connect` |
| `2026-06-23 21:42:36` | `cowrie.client.version` |
| `2026-06-23 21:42:36` | `cowrie.client.kex` |
| `2026-06-23 21:42:36` | `cowrie.login.success` |
| `2026-06-23 21:42:37` | `cowrie.session.params` |
| `2026-06-23 21:42:37` | `cowrie.command.input` |
| `2026-06-23 21:42:37` | `cowrie.log.closed` |
| `2026-06-23 21:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3c9de1fe70

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:43 |
| **Last Seen** | 2026-06-23 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:43:30` | `cowrie.session.connect` |
| `2026-06-23 21:43:30` | `cowrie.client.version` |
| `2026-06-23 21:43:30` | `cowrie.client.kex` |
| `2026-06-23 21:43:31` | `cowrie.login.success` |
| `2026-06-23 21:43:32` | `cowrie.session.params` |
| `2026-06-23 21:43:32` | `cowrie.command.input` |
| `2026-06-23 21:43:32` | `cowrie.log.closed` |
| `2026-06-23 21:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eaa1f82e4f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:44 |
| **Last Seen** | 2026-06-23 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:44:25` | `cowrie.session.connect` |
| `2026-06-23 21:44:25` | `cowrie.client.version` |
| `2026-06-23 21:44:25` | `cowrie.client.kex` |
| `2026-06-23 21:44:25` | `cowrie.login.success` |
| `2026-06-23 21:44:26` | `cowrie.session.params` |
| `2026-06-23 21:44:26` | `cowrie.command.input` |
| `2026-06-23 21:44:26` | `cowrie.log.closed` |
| `2026-06-23 21:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4612d94bd8d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:45 |
| **Last Seen** | 2026-06-23 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:45:19` | `cowrie.session.connect` |
| `2026-06-23 21:45:19` | `cowrie.client.version` |
| `2026-06-23 21:45:19` | `cowrie.client.kex` |
| `2026-06-23 21:45:19` | `cowrie.login.success` |
| `2026-06-23 21:45:20` | `cowrie.session.params` |
| `2026-06-23 21:45:20` | `cowrie.command.input` |
| `2026-06-23 21:45:20` | `cowrie.log.closed` |
| `2026-06-23 21:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf8601c4d43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:46 |
| **Last Seen** | 2026-06-23 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:46:11` | `cowrie.session.connect` |
| `2026-06-23 21:46:11` | `cowrie.client.version` |
| `2026-06-23 21:46:11` | `cowrie.client.kex` |
| `2026-06-23 21:46:11` | `cowrie.login.success` |
| `2026-06-23 21:46:12` | `cowrie.session.params` |
| `2026-06-23 21:46:12` | `cowrie.command.input` |
| `2026-06-23 21:46:12` | `cowrie.log.closed` |
| `2026-06-23 21:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1efcf482c81

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:47 |
| **Last Seen** | 2026-06-23 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:47:04` | `cowrie.session.connect` |
| `2026-06-23 21:47:04` | `cowrie.client.version` |
| `2026-06-23 21:47:04` | `cowrie.client.kex` |
| `2026-06-23 21:47:04` | `cowrie.login.success` |
| `2026-06-23 21:47:05` | `cowrie.session.params` |
| `2026-06-23 21:47:05` | `cowrie.command.input` |
| `2026-06-23 21:47:05` | `cowrie.log.closed` |
| `2026-06-23 21:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42f81f21a98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:48 |
| **Last Seen** | 2026-06-23 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:48:00` | `cowrie.session.connect` |
| `2026-06-23 21:48:00` | `cowrie.client.version` |
| `2026-06-23 21:48:00` | `cowrie.client.kex` |
| `2026-06-23 21:48:00` | `cowrie.login.success` |
| `2026-06-23 21:48:01` | `cowrie.session.params` |
| `2026-06-23 21:48:01` | `cowrie.command.input` |
| `2026-06-23 21:48:01` | `cowrie.log.closed` |
| `2026-06-23 21:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f9ded744a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:48 |
| **Last Seen** | 2026-06-23 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:48:55` | `cowrie.session.connect` |
| `2026-06-23 21:48:55` | `cowrie.client.version` |
| `2026-06-23 21:48:55` | `cowrie.client.kex` |
| `2026-06-23 21:48:56` | `cowrie.login.success` |
| `2026-06-23 21:48:56` | `cowrie.session.params` |
| `2026-06-23 21:48:56` | `cowrie.command.input` |
| `2026-06-23 21:48:56` | `cowrie.log.closed` |
| `2026-06-23 21:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55d2df8dfaf5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:49 |
| **Last Seen** | 2026-06-23 21:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:49:51` | `cowrie.session.connect` |
| `2026-06-23 21:49:51` | `cowrie.client.version` |
| `2026-06-23 21:49:51` | `cowrie.client.kex` |
| `2026-06-23 21:49:51` | `cowrie.login.success` |
| `2026-06-23 21:49:52` | `cowrie.session.params` |
| `2026-06-23 21:49:52` | `cowrie.command.input` |
| `2026-06-23 21:49:52` | `cowrie.log.closed` |
| `2026-06-23 21:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d6527e6285

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:50 |
| **Last Seen** | 2026-06-23 21:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:50:46` | `cowrie.session.connect` |
| `2026-06-23 21:50:46` | `cowrie.client.version` |
| `2026-06-23 21:50:46` | `cowrie.client.kex` |
| `2026-06-23 21:50:46` | `cowrie.login.success` |
| `2026-06-23 21:50:47` | `cowrie.session.params` |
| `2026-06-23 21:50:47` | `cowrie.command.input` |
| `2026-06-23 21:50:47` | `cowrie.log.closed` |
| `2026-06-23 21:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cf65d885477

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:51 |
| **Last Seen** | 2026-06-23 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:51:41` | `cowrie.session.connect` |
| `2026-06-23 21:51:41` | `cowrie.client.version` |
| `2026-06-23 21:51:41` | `cowrie.client.kex` |
| `2026-06-23 21:51:41` | `cowrie.login.success` |
| `2026-06-23 21:51:42` | `cowrie.session.params` |
| `2026-06-23 21:51:42` | `cowrie.command.input` |
| `2026-06-23 21:51:42` | `cowrie.log.closed` |
| `2026-06-23 21:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc99136dec1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:52 |
| **Last Seen** | 2026-06-23 21:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:52:36` | `cowrie.session.connect` |
| `2026-06-23 21:52:36` | `cowrie.client.version` |
| `2026-06-23 21:52:36` | `cowrie.client.kex` |
| `2026-06-23 21:52:36` | `cowrie.login.success` |
| `2026-06-23 21:52:37` | `cowrie.session.params` |
| `2026-06-23 21:52:37` | `cowrie.command.input` |
| `2026-06-23 21:52:37` | `cowrie.log.closed` |
| `2026-06-23 21:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044b867f4cf8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:53 |
| **Last Seen** | 2026-06-23 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:53:31` | `cowrie.session.connect` |
| `2026-06-23 21:53:31` | `cowrie.client.version` |
| `2026-06-23 21:53:31` | `cowrie.client.kex` |
| `2026-06-23 21:53:32` | `cowrie.login.success` |
| `2026-06-23 21:53:32` | `cowrie.session.params` |
| `2026-06-23 21:53:32` | `cowrie.command.input` |
| `2026-06-23 21:53:32` | `cowrie.log.closed` |
| `2026-06-23 21:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c585cb08a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:54 |
| **Last Seen** | 2026-06-23 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:54:28` | `cowrie.session.connect` |
| `2026-06-23 21:54:28` | `cowrie.client.version` |
| `2026-06-23 21:54:28` | `cowrie.client.kex` |
| `2026-06-23 21:54:29` | `cowrie.login.success` |
| `2026-06-23 21:54:29` | `cowrie.session.params` |
| `2026-06-23 21:54:29` | `cowrie.command.input` |
| `2026-06-23 21:54:29` | `cowrie.log.closed` |
| `2026-06-23 21:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ebce487ad6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 21:54 |
| **Last Seen** | 2026-06-23 21:54 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:54:33` | `cowrie.session.connect` |
| `2026-06-23 21:54:34` | `cowrie.client.version` |
| `2026-06-23 21:54:34` | `cowrie.client.kex` |
| `2026-06-23 21:54:41` | `cowrie.login.success` |
| `2026-06-23 21:54:45` | `cowrie.session.params` |
| `2026-06-23 21:54:45` | `cowrie.command.input` |
| `2026-06-23 21:54:46` | `cowrie.log.closed` |
| `2026-06-23 21:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a7831f21fd

| Field | Detail |
|---|---|
| **Source IP** | `34.22.222[.]217` |
| **First Seen** | 2026-06-23 21:55 |
| **Last Seen** | 2026-06-23 21:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:55:12` | `cowrie.session.connect` |
| `2026-06-23 21:55:12` | `cowrie.login.success` |
| `2026-06-23 21:55:12` | `cowrie.session.params` |
| `2026-06-23 21:55:12` | `cowrie.command.input` |
| `2026-06-23 21:55:12` | `cowrie.command.input` |
| `2026-06-23 21:55:12` | `cowrie.command.failed` |
| `2026-06-23 21:55:12` | `cowrie.command.input` |
| `2026-06-23 21:55:12` | `cowrie.log.closed` |
| `2026-06-23 21:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.222[.]217` to AbuseIPDB if not already reported
- [ ] Block `34.22.222[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-113398983be1

| Field | Detail |
|---|---|
| **Source IP** | `34.22.222[.]217` |
| **First Seen** | 2026-06-23 21:55 |
| **Last Seen** | 2026-06-23 21:56 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:55:20` | `cowrie.session.connect` |
| `2026-06-23 21:55:20` | `cowrie.login.success` |
| `2026-06-23 21:55:21` | `cowrie.session.params` |
| `2026-06-23 21:55:21` | `cowrie.command.input` |
| `2026-06-23 21:55:21` | `cowrie.command.failed` |
| `2026-06-23 21:56:13` | `cowrie.log.closed` |
| `2026-06-23 21:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.222[.]217` to AbuseIPDB if not already reported
- [ ] Block `34.22.222[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd74c1eb2127

| Field | Detail |
|---|---|
| **Source IP** | `34.22.222[.]217` |
| **First Seen** | 2026-06-23 21:55 |
| **Last Seen** | 2026-06-23 21:56 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:55:22` | `cowrie.session.connect` |
| `2026-06-23 21:55:22` | `cowrie.login.success` |
| `2026-06-23 21:55:23` | `cowrie.session.params` |
| `2026-06-23 21:55:23` | `cowrie.command.input` |
| `2026-06-23 21:56:13` | `cowrie.log.closed` |
| `2026-06-23 21:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.222[.]217` to AbuseIPDB if not already reported
- [ ] Block `34.22.222[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb94f78f2441

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:55 |
| **Last Seen** | 2026-06-23 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:55:27` | `cowrie.session.connect` |
| `2026-06-23 21:55:27` | `cowrie.client.version` |
| `2026-06-23 21:55:27` | `cowrie.client.kex` |
| `2026-06-23 21:55:27` | `cowrie.login.success` |
| `2026-06-23 21:55:28` | `cowrie.session.params` |
| `2026-06-23 21:55:28` | `cowrie.command.input` |
| `2026-06-23 21:55:28` | `cowrie.log.closed` |
| `2026-06-23 21:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360f2a5381fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:56 |
| **Last Seen** | 2026-06-23 21:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:56:25` | `cowrie.session.connect` |
| `2026-06-23 21:56:25` | `cowrie.client.version` |
| `2026-06-23 21:56:25` | `cowrie.client.kex` |
| `2026-06-23 21:56:25` | `cowrie.login.success` |
| `2026-06-23 21:56:26` | `cowrie.session.params` |
| `2026-06-23 21:56:26` | `cowrie.command.input` |
| `2026-06-23 21:56:26` | `cowrie.log.closed` |
| `2026-06-23 21:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff46e6dc2e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:57 |
| **Last Seen** | 2026-06-23 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:57:21` | `cowrie.session.connect` |
| `2026-06-23 21:57:21` | `cowrie.client.version` |
| `2026-06-23 21:57:21` | `cowrie.client.kex` |
| `2026-06-23 21:57:22` | `cowrie.login.success` |
| `2026-06-23 21:57:23` | `cowrie.session.params` |
| `2026-06-23 21:57:23` | `cowrie.command.input` |
| `2026-06-23 21:57:23` | `cowrie.log.closed` |
| `2026-06-23 21:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a163278a7c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:58 |
| **Last Seen** | 2026-06-23 21:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:58:16` | `cowrie.session.connect` |
| `2026-06-23 21:58:16` | `cowrie.client.version` |
| `2026-06-23 21:58:16` | `cowrie.client.kex` |
| `2026-06-23 21:58:16` | `cowrie.login.success` |
| `2026-06-23 21:58:17` | `cowrie.session.params` |
| `2026-06-23 21:58:17` | `cowrie.command.input` |
| `2026-06-23 21:58:17` | `cowrie.log.closed` |
| `2026-06-23 21:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8259ff72e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 21:59 |
| **Last Seen** | 2026-06-23 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 21:59:09` | `cowrie.session.connect` |
| `2026-06-23 21:59:09` | `cowrie.client.version` |
| `2026-06-23 21:59:09` | `cowrie.client.kex` |
| `2026-06-23 21:59:09` | `cowrie.login.success` |
| `2026-06-23 21:59:10` | `cowrie.session.params` |
| `2026-06-23 21:59:10` | `cowrie.command.input` |
| `2026-06-23 21:59:10` | `cowrie.log.closed` |
| `2026-06-23 21:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d882aed6c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:00 |
| **Last Seen** | 2026-06-23 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:00:03` | `cowrie.session.connect` |
| `2026-06-23 22:00:03` | `cowrie.client.version` |
| `2026-06-23 22:00:03` | `cowrie.client.kex` |
| `2026-06-23 22:00:03` | `cowrie.login.success` |
| `2026-06-23 22:00:04` | `cowrie.session.params` |
| `2026-06-23 22:00:04` | `cowrie.command.input` |
| `2026-06-23 22:00:04` | `cowrie.log.closed` |
| `2026-06-23 22:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b875ff7ed8c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:00 |
| **Last Seen** | 2026-06-23 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:00:49` | `cowrie.session.connect` |
| `2026-06-23 22:00:49` | `cowrie.client.version` |
| `2026-06-23 22:00:49` | `cowrie.client.kex` |
| `2026-06-23 22:00:49` | `cowrie.login.success` |
| `2026-06-23 22:00:50` | `cowrie.session.params` |
| `2026-06-23 22:00:50` | `cowrie.command.input` |
| `2026-06-23 22:00:50` | `cowrie.log.closed` |
| `2026-06-23 22:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a28fdbde9a04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:01 |
| **Last Seen** | 2026-06-23 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:01:33` | `cowrie.session.connect` |
| `2026-06-23 22:01:33` | `cowrie.client.version` |
| `2026-06-23 22:01:33` | `cowrie.client.kex` |
| `2026-06-23 22:01:33` | `cowrie.login.success` |
| `2026-06-23 22:01:34` | `cowrie.session.params` |
| `2026-06-23 22:01:34` | `cowrie.command.input` |
| `2026-06-23 22:01:34` | `cowrie.log.closed` |
| `2026-06-23 22:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727eaa3b7426

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:02 |
| **Last Seen** | 2026-06-23 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:02:17` | `cowrie.session.connect` |
| `2026-06-23 22:02:17` | `cowrie.client.version` |
| `2026-06-23 22:02:17` | `cowrie.client.kex` |
| `2026-06-23 22:02:18` | `cowrie.login.success` |
| `2026-06-23 22:02:18` | `cowrie.session.params` |
| `2026-06-23 22:02:18` | `cowrie.command.input` |
| `2026-06-23 22:02:18` | `cowrie.log.closed` |
| `2026-06-23 22:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a103bcc497

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:03 |
| **Last Seen** | 2026-06-23 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:03:01` | `cowrie.session.connect` |
| `2026-06-23 22:03:01` | `cowrie.client.version` |
| `2026-06-23 22:03:02` | `cowrie.client.kex` |
| `2026-06-23 22:03:02` | `cowrie.login.success` |
| `2026-06-23 22:03:03` | `cowrie.session.params` |
| `2026-06-23 22:03:03` | `cowrie.command.input` |
| `2026-06-23 22:03:03` | `cowrie.log.closed` |
| `2026-06-23 22:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a2d799aa24d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:03 |
| **Last Seen** | 2026-06-23 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:03:44` | `cowrie.session.connect` |
| `2026-06-23 22:03:44` | `cowrie.client.version` |
| `2026-06-23 22:03:44` | `cowrie.client.kex` |
| `2026-06-23 22:03:45` | `cowrie.login.success` |
| `2026-06-23 22:03:45` | `cowrie.session.params` |
| `2026-06-23 22:03:45` | `cowrie.command.input` |
| `2026-06-23 22:03:45` | `cowrie.log.closed` |
| `2026-06-23 22:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93afc72641cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:04 |
| **Last Seen** | 2026-06-23 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:04:26` | `cowrie.session.connect` |
| `2026-06-23 22:04:26` | `cowrie.client.version` |
| `2026-06-23 22:04:26` | `cowrie.client.kex` |
| `2026-06-23 22:04:27` | `cowrie.login.success` |
| `2026-06-23 22:04:27` | `cowrie.session.params` |
| `2026-06-23 22:04:27` | `cowrie.command.input` |
| `2026-06-23 22:04:27` | `cowrie.log.closed` |
| `2026-06-23 22:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08c5abf7d27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:05 |
| **Last Seen** | 2026-06-23 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:05:08` | `cowrie.session.connect` |
| `2026-06-23 22:05:08` | `cowrie.client.version` |
| `2026-06-23 22:05:08` | `cowrie.client.kex` |
| `2026-06-23 22:05:09` | `cowrie.login.success` |
| `2026-06-23 22:05:10` | `cowrie.session.params` |
| `2026-06-23 22:05:10` | `cowrie.command.input` |
| `2026-06-23 22:05:10` | `cowrie.log.closed` |
| `2026-06-23 22:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d714773fc938

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:05 |
| **Last Seen** | 2026-06-23 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:05:51` | `cowrie.session.connect` |
| `2026-06-23 22:05:51` | `cowrie.client.version` |
| `2026-06-23 22:05:51` | `cowrie.client.kex` |
| `2026-06-23 22:05:51` | `cowrie.login.success` |
| `2026-06-23 22:05:52` | `cowrie.session.params` |
| `2026-06-23 22:05:52` | `cowrie.command.input` |
| `2026-06-23 22:05:52` | `cowrie.log.closed` |
| `2026-06-23 22:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f6aa8c783e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:06 |
| **Last Seen** | 2026-06-23 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:06:34` | `cowrie.session.connect` |
| `2026-06-23 22:06:34` | `cowrie.client.version` |
| `2026-06-23 22:06:34` | `cowrie.client.kex` |
| `2026-06-23 22:06:34` | `cowrie.login.success` |
| `2026-06-23 22:06:35` | `cowrie.session.params` |
| `2026-06-23 22:06:35` | `cowrie.command.input` |
| `2026-06-23 22:06:35` | `cowrie.log.closed` |
| `2026-06-23 22:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596c1be174a0

| Field | Detail |
|---|---|
| **Source IP** | `35.187.78[.]126` |
| **First Seen** | 2026-06-23 22:06 |
| **Last Seen** | 2026-06-23 22:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:06:42` | `cowrie.session.connect` |
| `2026-06-23 22:06:42` | `cowrie.login.success` |
| `2026-06-23 22:06:43` | `cowrie.session.params` |
| `2026-06-23 22:06:43` | `cowrie.command.input` |
| `2026-06-23 22:06:43` | `cowrie.command.input` |
| `2026-06-23 22:06:43` | `cowrie.command.failed` |
| `2026-06-23 22:06:43` | `cowrie.command.input` |
| `2026-06-23 22:06:43` | `cowrie.log.closed` |
| `2026-06-23 22:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.78[.]126` to AbuseIPDB if not already reported
- [ ] Block `35.187.78[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d6ac1a4252

| Field | Detail |
|---|---|
| **Source IP** | `35.187.78[.]126` |
| **First Seen** | 2026-06-23 22:06 |
| **Last Seen** | 2026-06-23 22:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:06:56` | `cowrie.session.connect` |
| `2026-06-23 22:06:56` | `cowrie.login.success` |
| `2026-06-23 22:06:56` | `cowrie.session.params` |
| `2026-06-23 22:06:56` | `cowrie.command.input` |
| `2026-06-23 22:06:56` | `cowrie.command.failed` |
| `2026-06-23 22:07:02` | `cowrie.log.closed` |
| `2026-06-23 22:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.78[.]126` to AbuseIPDB if not already reported
- [ ] Block `35.187.78[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b69bbbd356d

| Field | Detail |
|---|---|
| **Source IP** | `35.187.78[.]126` |
| **First Seen** | 2026-06-23 22:06 |
| **Last Seen** | 2026-06-23 22:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:06:58` | `cowrie.session.connect` |
| `2026-06-23 22:06:58` | `cowrie.login.success` |
| `2026-06-23 22:06:58` | `cowrie.session.params` |
| `2026-06-23 22:06:58` | `cowrie.command.input` |
| `2026-06-23 22:07:02` | `cowrie.log.closed` |
| `2026-06-23 22:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.187.78[.]126` to AbuseIPDB if not already reported
- [ ] Block `35.187.78[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6550e13ca2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:07 |
| **Last Seen** | 2026-06-23 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:07:19` | `cowrie.session.connect` |
| `2026-06-23 22:07:19` | `cowrie.client.version` |
| `2026-06-23 22:07:19` | `cowrie.client.kex` |
| `2026-06-23 22:07:19` | `cowrie.login.success` |
| `2026-06-23 22:07:20` | `cowrie.session.params` |
| `2026-06-23 22:07:20` | `cowrie.command.input` |
| `2026-06-23 22:07:20` | `cowrie.log.closed` |
| `2026-06-23 22:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d3600e48bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:08 |
| **Last Seen** | 2026-06-23 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:08:03` | `cowrie.session.connect` |
| `2026-06-23 22:08:03` | `cowrie.client.version` |
| `2026-06-23 22:08:03` | `cowrie.client.kex` |
| `2026-06-23 22:08:04` | `cowrie.login.success` |
| `2026-06-23 22:08:04` | `cowrie.session.params` |
| `2026-06-23 22:08:04` | `cowrie.command.input` |
| `2026-06-23 22:08:04` | `cowrie.log.closed` |
| `2026-06-23 22:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00fb6d3c3cf5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:08 |
| **Last Seen** | 2026-06-23 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:08:48` | `cowrie.session.connect` |
| `2026-06-23 22:08:48` | `cowrie.client.version` |
| `2026-06-23 22:08:48` | `cowrie.client.kex` |
| `2026-06-23 22:08:48` | `cowrie.login.success` |
| `2026-06-23 22:08:49` | `cowrie.session.params` |
| `2026-06-23 22:08:49` | `cowrie.command.input` |
| `2026-06-23 22:08:49` | `cowrie.log.closed` |
| `2026-06-23 22:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054f0e82af57

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 22:08 |
| **Last Seen** | 2026-06-23 22:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:08:49` | `cowrie.session.connect` |
| `2026-06-23 22:08:52` | `cowrie.client.version` |
| `2026-06-23 22:08:52` | `cowrie.client.kex` |
| `2026-06-23 22:08:57` | `cowrie.login.success` |
| `2026-06-23 22:09:02` | `cowrie.session.params` |
| `2026-06-23 22:09:02` | `cowrie.command.input` |
| `2026-06-23 22:09:03` | `cowrie.log.closed` |
| `2026-06-23 22:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251946361410

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:09 |
| **Last Seen** | 2026-06-23 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:09:32` | `cowrie.session.connect` |
| `2026-06-23 22:09:32` | `cowrie.client.version` |
| `2026-06-23 22:09:32` | `cowrie.client.kex` |
| `2026-06-23 22:09:32` | `cowrie.login.success` |
| `2026-06-23 22:09:33` | `cowrie.session.params` |
| `2026-06-23 22:09:33` | `cowrie.command.input` |
| `2026-06-23 22:09:33` | `cowrie.log.closed` |
| `2026-06-23 22:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d52c945035a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:10 |
| **Last Seen** | 2026-06-23 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:10:16` | `cowrie.session.connect` |
| `2026-06-23 22:10:16` | `cowrie.client.version` |
| `2026-06-23 22:10:16` | `cowrie.client.kex` |
| `2026-06-23 22:10:16` | `cowrie.login.success` |
| `2026-06-23 22:10:17` | `cowrie.session.params` |
| `2026-06-23 22:10:17` | `cowrie.command.input` |
| `2026-06-23 22:10:17` | `cowrie.log.closed` |
| `2026-06-23 22:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be176ebf0bce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:10 |
| **Last Seen** | 2026-06-23 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:10:59` | `cowrie.session.connect` |
| `2026-06-23 22:10:59` | `cowrie.client.version` |
| `2026-06-23 22:10:59` | `cowrie.client.kex` |
| `2026-06-23 22:10:59` | `cowrie.login.success` |
| `2026-06-23 22:11:00` | `cowrie.session.params` |
| `2026-06-23 22:11:00` | `cowrie.command.input` |
| `2026-06-23 22:11:00` | `cowrie.log.closed` |
| `2026-06-23 22:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a81fe538165

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:11 |
| **Last Seen** | 2026-06-23 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:11:43` | `cowrie.session.connect` |
| `2026-06-23 22:11:43` | `cowrie.client.version` |
| `2026-06-23 22:11:43` | `cowrie.client.kex` |
| `2026-06-23 22:11:43` | `cowrie.login.success` |
| `2026-06-23 22:11:44` | `cowrie.session.params` |
| `2026-06-23 22:11:44` | `cowrie.command.input` |
| `2026-06-23 22:11:44` | `cowrie.log.closed` |
| `2026-06-23 22:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3bdc3e02348

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:12 |
| **Last Seen** | 2026-06-23 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:12:27` | `cowrie.session.connect` |
| `2026-06-23 22:12:27` | `cowrie.client.version` |
| `2026-06-23 22:12:27` | `cowrie.client.kex` |
| `2026-06-23 22:12:27` | `cowrie.login.success` |
| `2026-06-23 22:12:28` | `cowrie.session.params` |
| `2026-06-23 22:12:28` | `cowrie.command.input` |
| `2026-06-23 22:12:28` | `cowrie.log.closed` |
| `2026-06-23 22:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6623fb27f902

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:13 |
| **Last Seen** | 2026-06-23 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:13:11` | `cowrie.session.connect` |
| `2026-06-23 22:13:11` | `cowrie.client.version` |
| `2026-06-23 22:13:11` | `cowrie.client.kex` |
| `2026-06-23 22:13:11` | `cowrie.login.success` |
| `2026-06-23 22:13:12` | `cowrie.session.params` |
| `2026-06-23 22:13:12` | `cowrie.command.input` |
| `2026-06-23 22:13:12` | `cowrie.log.closed` |
| `2026-06-23 22:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77bdc704fc34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:13 |
| **Last Seen** | 2026-06-23 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:13:57` | `cowrie.session.connect` |
| `2026-06-23 22:13:57` | `cowrie.client.version` |
| `2026-06-23 22:13:57` | `cowrie.client.kex` |
| `2026-06-23 22:13:58` | `cowrie.login.success` |
| `2026-06-23 22:13:59` | `cowrie.session.params` |
| `2026-06-23 22:13:59` | `cowrie.command.input` |
| `2026-06-23 22:13:59` | `cowrie.log.closed` |
| `2026-06-23 22:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7123fa662678

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:14 |
| **Last Seen** | 2026-06-23 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:14:44` | `cowrie.session.connect` |
| `2026-06-23 22:14:44` | `cowrie.client.version` |
| `2026-06-23 22:14:44` | `cowrie.client.kex` |
| `2026-06-23 22:14:45` | `cowrie.login.success` |
| `2026-06-23 22:14:45` | `cowrie.session.params` |
| `2026-06-23 22:14:45` | `cowrie.command.input` |
| `2026-06-23 22:14:46` | `cowrie.log.closed` |
| `2026-06-23 22:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f9fa0c449d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:15 |
| **Last Seen** | 2026-06-23 22:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:15:31` | `cowrie.session.connect` |
| `2026-06-23 22:15:31` | `cowrie.client.version` |
| `2026-06-23 22:15:31` | `cowrie.client.kex` |
| `2026-06-23 22:15:31` | `cowrie.login.success` |
| `2026-06-23 22:15:32` | `cowrie.session.params` |
| `2026-06-23 22:15:32` | `cowrie.command.input` |
| `2026-06-23 22:15:32` | `cowrie.log.closed` |
| `2026-06-23 22:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b25130b7f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:16 |
| **Last Seen** | 2026-06-23 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:16:17` | `cowrie.session.connect` |
| `2026-06-23 22:16:17` | `cowrie.client.version` |
| `2026-06-23 22:16:17` | `cowrie.client.kex` |
| `2026-06-23 22:16:18` | `cowrie.login.success` |
| `2026-06-23 22:16:18` | `cowrie.session.params` |
| `2026-06-23 22:16:18` | `cowrie.command.input` |
| `2026-06-23 22:16:19` | `cowrie.log.closed` |
| `2026-06-23 22:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f176fcee035

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:17 |
| **Last Seen** | 2026-06-23 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:17:03` | `cowrie.session.connect` |
| `2026-06-23 22:17:03` | `cowrie.client.version` |
| `2026-06-23 22:17:03` | `cowrie.client.kex` |
| `2026-06-23 22:17:03` | `cowrie.login.success` |
| `2026-06-23 22:17:04` | `cowrie.session.params` |
| `2026-06-23 22:17:04` | `cowrie.command.input` |
| `2026-06-23 22:17:04` | `cowrie.log.closed` |
| `2026-06-23 22:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef142e772d83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:17 |
| **Last Seen** | 2026-06-23 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:17:48` | `cowrie.session.connect` |
| `2026-06-23 22:17:48` | `cowrie.client.version` |
| `2026-06-23 22:17:48` | `cowrie.client.kex` |
| `2026-06-23 22:17:49` | `cowrie.login.success` |
| `2026-06-23 22:17:49` | `cowrie.session.params` |
| `2026-06-23 22:17:49` | `cowrie.command.input` |
| `2026-06-23 22:17:49` | `cowrie.log.closed` |
| `2026-06-23 22:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c47a21bf3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:18 |
| **Last Seen** | 2026-06-23 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:18:33` | `cowrie.session.connect` |
| `2026-06-23 22:18:33` | `cowrie.client.version` |
| `2026-06-23 22:18:33` | `cowrie.client.kex` |
| `2026-06-23 22:18:34` | `cowrie.login.success` |
| `2026-06-23 22:18:35` | `cowrie.session.params` |
| `2026-06-23 22:18:35` | `cowrie.command.input` |
| `2026-06-23 22:18:35` | `cowrie.log.closed` |
| `2026-06-23 22:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53adf63e8e27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:19 |
| **Last Seen** | 2026-06-23 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:19:19` | `cowrie.session.connect` |
| `2026-06-23 22:19:19` | `cowrie.client.version` |
| `2026-06-23 22:19:19` | `cowrie.client.kex` |
| `2026-06-23 22:19:20` | `cowrie.login.success` |
| `2026-06-23 22:19:20` | `cowrie.session.params` |
| `2026-06-23 22:19:20` | `cowrie.command.input` |
| `2026-06-23 22:19:20` | `cowrie.log.closed` |
| `2026-06-23 22:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd60c76e36c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:20 |
| **Last Seen** | 2026-06-23 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:20:06` | `cowrie.session.connect` |
| `2026-06-23 22:20:06` | `cowrie.client.version` |
| `2026-06-23 22:20:06` | `cowrie.client.kex` |
| `2026-06-23 22:20:06` | `cowrie.login.success` |
| `2026-06-23 22:20:07` | `cowrie.session.params` |
| `2026-06-23 22:20:07` | `cowrie.command.input` |
| `2026-06-23 22:20:07` | `cowrie.log.closed` |
| `2026-06-23 22:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21953d6a1ce0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:20 |
| **Last Seen** | 2026-06-23 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:20:54` | `cowrie.session.connect` |
| `2026-06-23 22:20:54` | `cowrie.client.version` |
| `2026-06-23 22:20:54` | `cowrie.client.kex` |
| `2026-06-23 22:20:54` | `cowrie.login.success` |
| `2026-06-23 22:20:55` | `cowrie.session.params` |
| `2026-06-23 22:20:55` | `cowrie.command.input` |
| `2026-06-23 22:20:55` | `cowrie.log.closed` |
| `2026-06-23 22:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f28d8a8296a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:21 |
| **Last Seen** | 2026-06-23 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:21:42` | `cowrie.session.connect` |
| `2026-06-23 22:21:42` | `cowrie.client.version` |
| `2026-06-23 22:21:42` | `cowrie.client.kex` |
| `2026-06-23 22:21:42` | `cowrie.login.success` |
| `2026-06-23 22:21:43` | `cowrie.session.params` |
| `2026-06-23 22:21:43` | `cowrie.command.input` |
| `2026-06-23 22:21:43` | `cowrie.log.closed` |
| `2026-06-23 22:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45392b4c9a87

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:22 |
| **Last Seen** | 2026-06-23 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:22:30` | `cowrie.session.connect` |
| `2026-06-23 22:22:30` | `cowrie.client.version` |
| `2026-06-23 22:22:30` | `cowrie.client.kex` |
| `2026-06-23 22:22:31` | `cowrie.login.success` |
| `2026-06-23 22:22:31` | `cowrie.session.params` |
| `2026-06-23 22:22:31` | `cowrie.command.input` |
| `2026-06-23 22:22:32` | `cowrie.log.closed` |
| `2026-06-23 22:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b046baf2cdb5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 22:23 |
| **Last Seen** | 2026-06-23 22:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:23:14` | `cowrie.session.connect` |
| `2026-06-23 22:23:16` | `cowrie.client.version` |
| `2026-06-23 22:23:16` | `cowrie.client.kex` |
| `2026-06-23 22:23:22` | `cowrie.login.success` |
| `2026-06-23 22:23:26` | `cowrie.session.params` |
| `2026-06-23 22:23:26` | `cowrie.command.input` |
| `2026-06-23 22:23:28` | `cowrie.log.closed` |
| `2026-06-23 22:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568d4ae6bf25

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:23 |
| **Last Seen** | 2026-06-23 22:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:23:18` | `cowrie.session.connect` |
| `2026-06-23 22:23:18` | `cowrie.client.version` |
| `2026-06-23 22:23:18` | `cowrie.client.kex` |
| `2026-06-23 22:23:18` | `cowrie.login.success` |
| `2026-06-23 22:23:19` | `cowrie.session.params` |
| `2026-06-23 22:23:19` | `cowrie.command.input` |
| `2026-06-23 22:23:19` | `cowrie.log.closed` |
| `2026-06-23 22:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f1e43a10e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:24 |
| **Last Seen** | 2026-06-23 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:24:06` | `cowrie.session.connect` |
| `2026-06-23 22:24:06` | `cowrie.client.version` |
| `2026-06-23 22:24:06` | `cowrie.client.kex` |
| `2026-06-23 22:24:06` | `cowrie.login.success` |
| `2026-06-23 22:24:07` | `cowrie.session.params` |
| `2026-06-23 22:24:07` | `cowrie.command.input` |
| `2026-06-23 22:24:07` | `cowrie.log.closed` |
| `2026-06-23 22:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86aaf68e4118

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:24 |
| **Last Seen** | 2026-06-23 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:24:54` | `cowrie.session.connect` |
| `2026-06-23 22:24:54` | `cowrie.client.version` |
| `2026-06-23 22:24:54` | `cowrie.client.kex` |
| `2026-06-23 22:24:55` | `cowrie.login.success` |
| `2026-06-23 22:24:55` | `cowrie.session.params` |
| `2026-06-23 22:24:55` | `cowrie.command.input` |
| `2026-06-23 22:24:55` | `cowrie.log.closed` |
| `2026-06-23 22:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d16d43daf8e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:25 |
| **Last Seen** | 2026-06-23 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:25:42` | `cowrie.session.connect` |
| `2026-06-23 22:25:42` | `cowrie.client.version` |
| `2026-06-23 22:25:42` | `cowrie.client.kex` |
| `2026-06-23 22:25:43` | `cowrie.login.success` |
| `2026-06-23 22:25:44` | `cowrie.session.params` |
| `2026-06-23 22:25:44` | `cowrie.command.input` |
| `2026-06-23 22:25:44` | `cowrie.log.closed` |
| `2026-06-23 22:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f57e8478813

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:26 |
| **Last Seen** | 2026-06-23 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:26:32` | `cowrie.session.connect` |
| `2026-06-23 22:26:32` | `cowrie.client.version` |
| `2026-06-23 22:26:32` | `cowrie.client.kex` |
| `2026-06-23 22:26:32` | `cowrie.login.success` |
| `2026-06-23 22:26:33` | `cowrie.session.params` |
| `2026-06-23 22:26:33` | `cowrie.command.input` |
| `2026-06-23 22:26:33` | `cowrie.log.closed` |
| `2026-06-23 22:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-504da6f98f01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:27 |
| **Last Seen** | 2026-06-23 22:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:27:23` | `cowrie.session.connect` |
| `2026-06-23 22:27:23` | `cowrie.client.version` |
| `2026-06-23 22:27:23` | `cowrie.client.kex` |
| `2026-06-23 22:27:24` | `cowrie.login.success` |
| `2026-06-23 22:27:24` | `cowrie.session.params` |
| `2026-06-23 22:27:24` | `cowrie.command.input` |
| `2026-06-23 22:27:25` | `cowrie.log.closed` |
| `2026-06-23 22:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd28fa3a465

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:28 |
| **Last Seen** | 2026-06-23 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:28:14` | `cowrie.session.connect` |
| `2026-06-23 22:28:14` | `cowrie.client.version` |
| `2026-06-23 22:28:14` | `cowrie.client.kex` |
| `2026-06-23 22:28:14` | `cowrie.login.success` |
| `2026-06-23 22:28:15` | `cowrie.session.params` |
| `2026-06-23 22:28:15` | `cowrie.command.input` |
| `2026-06-23 22:28:15` | `cowrie.log.closed` |
| `2026-06-23 22:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd81102e216

| Field | Detail |
|---|---|
| **Source IP** | `34.62.67[.]56` |
| **First Seen** | 2026-06-23 22:28 |
| **Last Seen** | 2026-06-23 22:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:28:28` | `cowrie.session.connect` |
| `2026-06-23 22:28:28` | `cowrie.login.success` |
| `2026-06-23 22:28:29` | `cowrie.session.params` |
| `2026-06-23 22:28:29` | `cowrie.command.input` |
| `2026-06-23 22:28:29` | `cowrie.command.input` |
| `2026-06-23 22:28:29` | `cowrie.command.failed` |
| `2026-06-23 22:28:29` | `cowrie.command.input` |
| `2026-06-23 22:28:29` | `cowrie.log.closed` |
| `2026-06-23 22:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.67[.]56` to AbuseIPDB if not already reported
- [ ] Block `34.62.67[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3264bf0d06

| Field | Detail |
|---|---|
| **Source IP** | `34.62.67[.]56` |
| **First Seen** | 2026-06-23 22:28 |
| **Last Seen** | 2026-06-23 22:29 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:28:42` | `cowrie.session.connect` |
| `2026-06-23 22:28:42` | `cowrie.login.success` |
| `2026-06-23 22:28:42` | `cowrie.session.params` |
| `2026-06-23 22:28:42` | `cowrie.command.input` |
| `2026-06-23 22:28:42` | `cowrie.command.failed` |
| `2026-06-23 22:29:20` | `cowrie.log.closed` |
| `2026-06-23 22:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.67[.]56` to AbuseIPDB if not already reported
- [ ] Block `34.62.67[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4791d8a0943b

| Field | Detail |
|---|---|
| **Source IP** | `34.62.67[.]56` |
| **First Seen** | 2026-06-23 22:28 |
| **Last Seen** | 2026-06-23 22:29 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:28:44` | `cowrie.session.connect` |
| `2026-06-23 22:28:44` | `cowrie.login.success` |
| `2026-06-23 22:28:44` | `cowrie.session.params` |
| `2026-06-23 22:28:44` | `cowrie.command.input` |
| `2026-06-23 22:29:20` | `cowrie.log.closed` |
| `2026-06-23 22:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.67[.]56` to AbuseIPDB if not already reported
- [ ] Block `34.62.67[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395c3cb8579e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:29 |
| **Last Seen** | 2026-06-23 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:29:04` | `cowrie.session.connect` |
| `2026-06-23 22:29:04` | `cowrie.client.version` |
| `2026-06-23 22:29:04` | `cowrie.client.kex` |
| `2026-06-23 22:29:04` | `cowrie.login.success` |
| `2026-06-23 22:29:05` | `cowrie.session.params` |
| `2026-06-23 22:29:05` | `cowrie.command.input` |
| `2026-06-23 22:29:05` | `cowrie.log.closed` |
| `2026-06-23 22:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e98aae4d397f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:29 |
| **Last Seen** | 2026-06-23 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:29:53` | `cowrie.session.connect` |
| `2026-06-23 22:29:53` | `cowrie.client.version` |
| `2026-06-23 22:29:53` | `cowrie.client.kex` |
| `2026-06-23 22:29:53` | `cowrie.login.success` |
| `2026-06-23 22:29:54` | `cowrie.session.params` |
| `2026-06-23 22:29:54` | `cowrie.command.input` |
| `2026-06-23 22:29:54` | `cowrie.log.closed` |
| `2026-06-23 22:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435b9e9b990a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:30 |
| **Last Seen** | 2026-06-23 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:30:42` | `cowrie.session.connect` |
| `2026-06-23 22:30:42` | `cowrie.client.version` |
| `2026-06-23 22:30:42` | `cowrie.client.kex` |
| `2026-06-23 22:30:42` | `cowrie.login.success` |
| `2026-06-23 22:30:43` | `cowrie.session.params` |
| `2026-06-23 22:30:43` | `cowrie.command.input` |
| `2026-06-23 22:30:43` | `cowrie.log.closed` |
| `2026-06-23 22:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9322b18b537a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:31 |
| **Last Seen** | 2026-06-23 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:31:31` | `cowrie.session.connect` |
| `2026-06-23 22:31:31` | `cowrie.client.version` |
| `2026-06-23 22:31:31` | `cowrie.client.kex` |
| `2026-06-23 22:31:32` | `cowrie.login.success` |
| `2026-06-23 22:31:32` | `cowrie.session.params` |
| `2026-06-23 22:31:32` | `cowrie.command.input` |
| `2026-06-23 22:31:32` | `cowrie.log.closed` |
| `2026-06-23 22:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3600dc91771

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:32 |
| **Last Seen** | 2026-06-23 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:32:21` | `cowrie.session.connect` |
| `2026-06-23 22:32:21` | `cowrie.client.version` |
| `2026-06-23 22:32:21` | `cowrie.client.kex` |
| `2026-06-23 22:32:21` | `cowrie.login.success` |
| `2026-06-23 22:32:22` | `cowrie.session.params` |
| `2026-06-23 22:32:22` | `cowrie.command.input` |
| `2026-06-23 22:32:22` | `cowrie.log.closed` |
| `2026-06-23 22:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30adef853736

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:33 |
| **Last Seen** | 2026-06-23 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:33:11` | `cowrie.session.connect` |
| `2026-06-23 22:33:11` | `cowrie.client.version` |
| `2026-06-23 22:33:11` | `cowrie.client.kex` |
| `2026-06-23 22:33:12` | `cowrie.login.success` |
| `2026-06-23 22:33:12` | `cowrie.session.params` |
| `2026-06-23 22:33:12` | `cowrie.command.input` |
| `2026-06-23 22:33:13` | `cowrie.log.closed` |
| `2026-06-23 22:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eab0494928f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:34 |
| **Last Seen** | 2026-06-23 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:34:02` | `cowrie.session.connect` |
| `2026-06-23 22:34:02` | `cowrie.client.version` |
| `2026-06-23 22:34:02` | `cowrie.client.kex` |
| `2026-06-23 22:34:02` | `cowrie.login.success` |
| `2026-06-23 22:34:03` | `cowrie.session.params` |
| `2026-06-23 22:34:03` | `cowrie.command.input` |
| `2026-06-23 22:34:03` | `cowrie.log.closed` |
| `2026-06-23 22:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43d7d30af51

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:34 |
| **Last Seen** | 2026-06-23 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:34:53` | `cowrie.session.connect` |
| `2026-06-23 22:34:53` | `cowrie.client.version` |
| `2026-06-23 22:34:53` | `cowrie.client.kex` |
| `2026-06-23 22:34:53` | `cowrie.login.success` |
| `2026-06-23 22:34:54` | `cowrie.session.params` |
| `2026-06-23 22:34:54` | `cowrie.command.input` |
| `2026-06-23 22:34:54` | `cowrie.log.closed` |
| `2026-06-23 22:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c104448901c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:35 |
| **Last Seen** | 2026-06-23 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:35:43` | `cowrie.session.connect` |
| `2026-06-23 22:35:43` | `cowrie.client.version` |
| `2026-06-23 22:35:43` | `cowrie.client.kex` |
| `2026-06-23 22:35:43` | `cowrie.login.success` |
| `2026-06-23 22:35:44` | `cowrie.session.params` |
| `2026-06-23 22:35:44` | `cowrie.command.input` |
| `2026-06-23 22:35:44` | `cowrie.log.closed` |
| `2026-06-23 22:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1398039edd87

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:36 |
| **Last Seen** | 2026-06-23 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:36:31` | `cowrie.session.connect` |
| `2026-06-23 22:36:31` | `cowrie.client.version` |
| `2026-06-23 22:36:31` | `cowrie.client.kex` |
| `2026-06-23 22:36:32` | `cowrie.login.success` |
| `2026-06-23 22:36:32` | `cowrie.session.params` |
| `2026-06-23 22:36:32` | `cowrie.command.input` |
| `2026-06-23 22:36:33` | `cowrie.log.closed` |
| `2026-06-23 22:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a93fe7e5f68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:37 |
| **Last Seen** | 2026-06-23 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:37:19` | `cowrie.session.connect` |
| `2026-06-23 22:37:19` | `cowrie.client.version` |
| `2026-06-23 22:37:20` | `cowrie.client.kex` |
| `2026-06-23 22:37:20` | `cowrie.login.success` |
| `2026-06-23 22:37:21` | `cowrie.session.params` |
| `2026-06-23 22:37:21` | `cowrie.command.input` |
| `2026-06-23 22:37:21` | `cowrie.log.closed` |
| `2026-06-23 22:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f8c25e58e8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 22:37 |
| **Last Seen** | 2026-06-23 22:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:37:28` | `cowrie.session.connect` |
| `2026-06-23 22:37:29` | `cowrie.client.version` |
| `2026-06-23 22:37:29` | `cowrie.client.kex` |
| `2026-06-23 22:37:35` | `cowrie.login.success` |
| `2026-06-23 22:37:39` | `cowrie.session.params` |
| `2026-06-23 22:37:39` | `cowrie.command.input` |
| `2026-06-23 22:37:41` | `cowrie.log.closed` |
| `2026-06-23 22:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e611f60104d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:38 |
| **Last Seen** | 2026-06-23 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:38:08` | `cowrie.session.connect` |
| `2026-06-23 22:38:08` | `cowrie.client.version` |
| `2026-06-23 22:38:08` | `cowrie.client.kex` |
| `2026-06-23 22:38:09` | `cowrie.login.success` |
| `2026-06-23 22:38:09` | `cowrie.session.params` |
| `2026-06-23 22:38:09` | `cowrie.command.input` |
| `2026-06-23 22:38:10` | `cowrie.log.closed` |
| `2026-06-23 22:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e2566357fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:39 |
| **Last Seen** | 2026-06-23 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:39:08` | `cowrie.session.connect` |
| `2026-06-23 22:39:08` | `cowrie.client.version` |
| `2026-06-23 22:39:08` | `cowrie.client.kex` |
| `2026-06-23 22:39:08` | `cowrie.login.success` |
| `2026-06-23 22:39:09` | `cowrie.session.params` |
| `2026-06-23 22:39:09` | `cowrie.command.input` |
| `2026-06-23 22:39:09` | `cowrie.log.closed` |
| `2026-06-23 22:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b656e299ed2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:40 |
| **Last Seen** | 2026-06-23 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:40:05` | `cowrie.session.connect` |
| `2026-06-23 22:40:05` | `cowrie.client.version` |
| `2026-06-23 22:40:05` | `cowrie.client.kex` |
| `2026-06-23 22:40:06` | `cowrie.login.success` |
| `2026-06-23 22:40:07` | `cowrie.session.params` |
| `2026-06-23 22:40:07` | `cowrie.command.input` |
| `2026-06-23 22:40:07` | `cowrie.log.closed` |
| `2026-06-23 22:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1d2a9fa60c

| Field | Detail |
|---|---|
| **Source IP** | `58.210.39[.]254` |
| **First Seen** | 2026-06-23 22:40 |
| **Last Seen** | 2026-06-23 22:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:40:27` | `cowrie.session.connect` |
| `2026-06-23 22:40:27` | `cowrie.client.version` |
| `2026-06-23 22:40:27` | `cowrie.client.kex` |
| `2026-06-23 22:40:28` | `cowrie.login.success` |
| `2026-06-23 22:40:29` | `cowrie.session.params` |
| `2026-06-23 22:40:29` | `cowrie.command.input` |
| `2026-06-23 22:40:29` | `cowrie.log.closed` |
| `2026-06-23 22:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.210.39[.]254` to AbuseIPDB if not already reported
- [ ] Block `58.210.39[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f757e1d6767

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:40 |
| **Last Seen** | 2026-06-23 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:40:56` | `cowrie.session.connect` |
| `2026-06-23 22:40:56` | `cowrie.client.version` |
| `2026-06-23 22:40:56` | `cowrie.client.kex` |
| `2026-06-23 22:40:57` | `cowrie.login.success` |
| `2026-06-23 22:40:57` | `cowrie.session.params` |
| `2026-06-23 22:40:57` | `cowrie.command.input` |
| `2026-06-23 22:40:57` | `cowrie.log.closed` |
| `2026-06-23 22:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3248042d16b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:41 |
| **Last Seen** | 2026-06-23 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:41:46` | `cowrie.session.connect` |
| `2026-06-23 22:41:46` | `cowrie.client.version` |
| `2026-06-23 22:41:46` | `cowrie.client.kex` |
| `2026-06-23 22:41:46` | `cowrie.login.success` |
| `2026-06-23 22:41:47` | `cowrie.session.params` |
| `2026-06-23 22:41:47` | `cowrie.command.input` |
| `2026-06-23 22:41:47` | `cowrie.log.closed` |
| `2026-06-23 22:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf632178a8aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:42 |
| **Last Seen** | 2026-06-23 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:42:35` | `cowrie.session.connect` |
| `2026-06-23 22:42:35` | `cowrie.client.version` |
| `2026-06-23 22:42:35` | `cowrie.client.kex` |
| `2026-06-23 22:42:35` | `cowrie.login.success` |
| `2026-06-23 22:42:36` | `cowrie.session.params` |
| `2026-06-23 22:42:36` | `cowrie.command.input` |
| `2026-06-23 22:42:36` | `cowrie.log.closed` |
| `2026-06-23 22:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ebe9bebee5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:43 |
| **Last Seen** | 2026-06-23 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:43:23` | `cowrie.session.connect` |
| `2026-06-23 22:43:23` | `cowrie.client.version` |
| `2026-06-23 22:43:23` | `cowrie.client.kex` |
| `2026-06-23 22:43:23` | `cowrie.login.success` |
| `2026-06-23 22:43:24` | `cowrie.session.params` |
| `2026-06-23 22:43:24` | `cowrie.command.input` |
| `2026-06-23 22:43:24` | `cowrie.log.closed` |
| `2026-06-23 22:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b207b649b890

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:44 |
| **Last Seen** | 2026-06-23 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:44:10` | `cowrie.session.connect` |
| `2026-06-23 22:44:10` | `cowrie.client.version` |
| `2026-06-23 22:44:11` | `cowrie.client.kex` |
| `2026-06-23 22:44:11` | `cowrie.login.success` |
| `2026-06-23 22:44:12` | `cowrie.session.params` |
| `2026-06-23 22:44:12` | `cowrie.command.input` |
| `2026-06-23 22:44:12` | `cowrie.log.closed` |
| `2026-06-23 22:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b63c631bef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:44 |
| **Last Seen** | 2026-06-23 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:44:59` | `cowrie.session.connect` |
| `2026-06-23 22:44:59` | `cowrie.client.version` |
| `2026-06-23 22:44:59` | `cowrie.client.kex` |
| `2026-06-23 22:44:59` | `cowrie.login.success` |
| `2026-06-23 22:45:00` | `cowrie.session.params` |
| `2026-06-23 22:45:00` | `cowrie.command.input` |
| `2026-06-23 22:45:00` | `cowrie.log.closed` |
| `2026-06-23 22:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b47c03edebe

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 22:45 |
| **Last Seen** | 2026-06-23 22:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:45:06` | `cowrie.session.connect` |
| `2026-06-23 22:45:06` | `cowrie.client.version` |
| `2026-06-23 22:45:07` | `cowrie.client.kex` |
| `2026-06-23 22:45:07` | `cowrie.login.success` |
| `2026-06-23 22:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd27901f24e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 22:45 |
| **Last Seen** | 2026-06-23 22:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:45:07` | `cowrie.session.connect` |
| `2026-06-23 22:45:07` | `cowrie.client.version` |
| `2026-06-23 22:45:07` | `cowrie.client.kex` |
| `2026-06-23 22:45:08` | `cowrie.login.success` |
| `2026-06-23 22:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a1960f9ffbf

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 22:45 |
| **Last Seen** | 2026-06-23 22:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:45:07` | `cowrie.session.connect` |
| `2026-06-23 22:45:07` | `cowrie.client.version` |
| `2026-06-23 22:45:08` | `cowrie.client.kex` |
| `2026-06-23 22:45:08` | `cowrie.login.success` |
| `2026-06-23 22:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5b18573d31

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-23 22:45 |
| **Last Seen** | 2026-06-23 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:45:08` | `cowrie.session.connect` |
| `2026-06-23 22:45:08` | `cowrie.client.version` |
| `2026-06-23 22:45:09` | `cowrie.client.kex` |
| `2026-06-23 22:45:09` | `cowrie.login.success` |
| `2026-06-23 22:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-438d3062403f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:45 |
| **Last Seen** | 2026-06-23 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:45:48` | `cowrie.session.connect` |
| `2026-06-23 22:45:48` | `cowrie.client.version` |
| `2026-06-23 22:45:48` | `cowrie.client.kex` |
| `2026-06-23 22:45:49` | `cowrie.login.success` |
| `2026-06-23 22:45:49` | `cowrie.session.params` |
| `2026-06-23 22:45:49` | `cowrie.command.input` |
| `2026-06-23 22:45:50` | `cowrie.log.closed` |
| `2026-06-23 22:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e5445fcd5d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:46 |
| **Last Seen** | 2026-06-23 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:46:38` | `cowrie.session.connect` |
| `2026-06-23 22:46:38` | `cowrie.client.version` |
| `2026-06-23 22:46:38` | `cowrie.client.kex` |
| `2026-06-23 22:46:38` | `cowrie.login.success` |
| `2026-06-23 22:46:39` | `cowrie.session.params` |
| `2026-06-23 22:46:39` | `cowrie.command.input` |
| `2026-06-23 22:46:39` | `cowrie.log.closed` |
| `2026-06-23 22:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7315f667647f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:47 |
| **Last Seen** | 2026-06-23 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:47:27` | `cowrie.session.connect` |
| `2026-06-23 22:47:27` | `cowrie.client.version` |
| `2026-06-23 22:47:27` | `cowrie.client.kex` |
| `2026-06-23 22:47:27` | `cowrie.login.success` |
| `2026-06-23 22:47:28` | `cowrie.session.params` |
| `2026-06-23 22:47:28` | `cowrie.command.input` |
| `2026-06-23 22:47:28` | `cowrie.log.closed` |
| `2026-06-23 22:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1b522b3f88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:48 |
| **Last Seen** | 2026-06-23 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:48:17` | `cowrie.session.connect` |
| `2026-06-23 22:48:17` | `cowrie.client.version` |
| `2026-06-23 22:48:17` | `cowrie.client.kex` |
| `2026-06-23 22:48:17` | `cowrie.login.success` |
| `2026-06-23 22:48:18` | `cowrie.session.params` |
| `2026-06-23 22:48:18` | `cowrie.command.input` |
| `2026-06-23 22:48:18` | `cowrie.log.closed` |
| `2026-06-23 22:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57c0bc6d171

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:49 |
| **Last Seen** | 2026-06-23 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:49:05` | `cowrie.session.connect` |
| `2026-06-23 22:49:05` | `cowrie.client.version` |
| `2026-06-23 22:49:05` | `cowrie.client.kex` |
| `2026-06-23 22:49:06` | `cowrie.login.success` |
| `2026-06-23 22:49:06` | `cowrie.session.params` |
| `2026-06-23 22:49:06` | `cowrie.command.input` |
| `2026-06-23 22:49:07` | `cowrie.log.closed` |
| `2026-06-23 22:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2fb6c053fde

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:49 |
| **Last Seen** | 2026-06-23 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:49:52` | `cowrie.session.connect` |
| `2026-06-23 22:49:52` | `cowrie.client.version` |
| `2026-06-23 22:49:53` | `cowrie.client.kex` |
| `2026-06-23 22:49:53` | `cowrie.login.success` |
| `2026-06-23 22:49:54` | `cowrie.session.params` |
| `2026-06-23 22:49:54` | `cowrie.command.input` |
| `2026-06-23 22:49:54` | `cowrie.log.closed` |
| `2026-06-23 22:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114fba5787a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:50 |
| **Last Seen** | 2026-06-23 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:50:40` | `cowrie.session.connect` |
| `2026-06-23 22:50:40` | `cowrie.client.version` |
| `2026-06-23 22:50:40` | `cowrie.client.kex` |
| `2026-06-23 22:50:40` | `cowrie.login.success` |
| `2026-06-23 22:50:41` | `cowrie.session.params` |
| `2026-06-23 22:50:41` | `cowrie.command.input` |
| `2026-06-23 22:50:41` | `cowrie.log.closed` |
| `2026-06-23 22:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3493689033a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:51 |
| **Last Seen** | 2026-06-23 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:51:27` | `cowrie.session.connect` |
| `2026-06-23 22:51:27` | `cowrie.client.version` |
| `2026-06-23 22:51:27` | `cowrie.client.kex` |
| `2026-06-23 22:51:28` | `cowrie.login.success` |
| `2026-06-23 22:51:28` | `cowrie.session.params` |
| `2026-06-23 22:51:28` | `cowrie.command.input` |
| `2026-06-23 22:51:28` | `cowrie.log.closed` |
| `2026-06-23 22:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93996854c6c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-23 22:51 |
| **Last Seen** | 2026-06-23 22:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:51:36` | `cowrie.session.connect` |
| `2026-06-23 22:51:37` | `cowrie.client.version` |
| `2026-06-23 22:51:37` | `cowrie.client.kex` |
| `2026-06-23 22:51:44` | `cowrie.login.success` |
| `2026-06-23 22:51:48` | `cowrie.session.params` |
| `2026-06-23 22:51:48` | `cowrie.command.input` |
| `2026-06-23 22:51:49` | `cowrie.log.closed` |
| `2026-06-23 22:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e129ad56e78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:52 |
| **Last Seen** | 2026-06-23 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:52:16` | `cowrie.session.connect` |
| `2026-06-23 22:52:16` | `cowrie.client.version` |
| `2026-06-23 22:52:16` | `cowrie.client.kex` |
| `2026-06-23 22:52:16` | `cowrie.login.success` |
| `2026-06-23 22:52:17` | `cowrie.session.params` |
| `2026-06-23 22:52:17` | `cowrie.command.input` |
| `2026-06-23 22:52:17` | `cowrie.log.closed` |
| `2026-06-23 22:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0412d10f20fc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:53 |
| **Last Seen** | 2026-06-23 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:53:06` | `cowrie.session.connect` |
| `2026-06-23 22:53:06` | `cowrie.client.version` |
| `2026-06-23 22:53:06` | `cowrie.client.kex` |
| `2026-06-23 22:53:07` | `cowrie.login.success` |
| `2026-06-23 22:53:07` | `cowrie.session.params` |
| `2026-06-23 22:53:07` | `cowrie.command.input` |
| `2026-06-23 22:53:08` | `cowrie.log.closed` |
| `2026-06-23 22:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04444f2cbf88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:53 |
| **Last Seen** | 2026-06-23 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:53:56` | `cowrie.session.connect` |
| `2026-06-23 22:53:56` | `cowrie.client.version` |
| `2026-06-23 22:53:56` | `cowrie.client.kex` |
| `2026-06-23 22:53:56` | `cowrie.login.success` |
| `2026-06-23 22:53:57` | `cowrie.session.params` |
| `2026-06-23 22:53:57` | `cowrie.command.input` |
| `2026-06-23 22:53:57` | `cowrie.log.closed` |
| `2026-06-23 22:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a2da2d96b59

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-23 22:54 |
| **Last Seen** | 2026-06-23 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-23 22:54:44` | `cowrie.session.connect` |
| `2026-06-23 22:54:44` | `cowrie.client.version` |
| `2026-06-23 22:54:44` | `cowrie.client.kex` |
| `2026-06-23 22:54:45` | `cowrie.login.success` |
| `2026-06-23 22:54:45` | `cowrie.session.params` |
| `2026-06-23 22:54:45` | `cowrie.command.input` |
| `2026-06-23 22:54:46` | `cowrie.log.closed` |
| `2026-06-23 22:54:46` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **143** | 2026-06-23 20:55 | 2026-06-23 22:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `34.22.222[.]217` | **30** | 2026-06-23 21:55 | 2026-06-23 21:55 | 19m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.67[.]56` | **30** | 2026-06-23 22:28 | 2026-06-23 22:28 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `35.187.78[.]126` | **30** | 2026-06-23 22:06 | 2026-06-23 22:06 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `176.65.148[.]25` | **4** | 2026-06-23 21:01 | 2026-06-23 21:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]103` | **3** | 2026-06-23 20:56 | 2026-06-23 20:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.120.30[.]67` | **3** | 2026-06-23 21:44 | 2026-06-23 21:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-23 21:16 | 2026-06-23 21:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `72.167.49[.]132` | **2** | 2026-06-23 22:03 | 2026-06-23 22:53 | 1m | 0 | `T1592` | 🟢 LOW |
| `8.145.55[.]124` | **2** | 2026-06-23 22:44 | 2026-06-23 22:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.145.151[.]135` | 1 | 2026-06-23 21:10 | 2026-06-23 21:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.141.46[.]66` | 1 | 2026-06-23 21:30 | 2026-06-23 21:30 | 37s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-23 22:03 | 2026-06-23 22:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.210.39[.]254` | 1 | 2026-06-23 22:40 | 2026-06-23 22:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-23 21:39 | 2026-06-23 21:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-06-23 22:33 | 2026-06-23 22:34 | 10s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-06-23 20:57 | 2026-06-23 20:57 | 6s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (29 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/73** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/73** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/73** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **37/73** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `118.145.151[.]135` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 6 |
| `47.120.30[.]67` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 4 |
| `72.167.49[.]132` | US | GoDaddy.com, LLC | **100** ⚠️ | 7 |
| `209.141.46[.]66` | US | FranTech Solutions | **100** ⚠️ | 8 |
| `58.210.39[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 1 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `45.148.10[.]121` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `34.22.222[.]217` | BE | Google LLC | **100** ⚠️ | 0 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 189 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 172 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 26 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 459 cases |
| Tool 34  | Credential Extractor        | ✅ 172 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (7.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 29 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 169 priority case(s) shown individually · 17 recon entry/entries in table (10 group(s) consolidating 249 session(s)).

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
_Report time: 2026-06-23T23:11:09Z_

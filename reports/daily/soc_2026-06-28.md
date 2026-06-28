# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-28 |
| **Generated At** | 2026-06-28T13:55:44Z |
| **Shift Time** | 13:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **312** |
| Confirmed Threats | **306** |
| False Positives Filtered | **6** (1.9%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **10** |
| High Severity Cases | **159** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **153** |
| Malware Samples Analyzed | **5** HIGH · **41** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **161** |
| Unique Credential Pairs | **154** |
| Unique Usernames | **89** |
| Unique Passwords | **136** |
| Successful Auth Pairs | **159** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 61 |
| `ubuntu` | 9 |
| `zhangxinkui` | 2 |
| `vps` | 2 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 13 |
| `123` | 3 |
| `Password@12345` | 3 |
| `passwd` | 2 |
| `666666` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `Password@12345` | 3 |
| `admin` | `admin` | 2 |
| `root` | `LeitboGi0ro` | 2 |
| `root` | `123@@@` | 2 |
| `root` | `smo@@kkklss` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `null` | `sd.30df.1s,m1ba*IK<abmuiema` | `209.99.185.59` | 2026-06-28T10:55:44 |
| `mariadb` | `mariadb` | `209.99.185.59` | 2026-06-28T10:56:39 |
| `wartung` | `0` | `209.99.185.59` | 2026-06-28T10:57:40 |
| `web2` | `web2` | `45.198.224.120` | 2026-06-28T10:58:07 |
| `user` | `passwd` | `209.99.185.59` | 2026-06-28T10:58:42 |
| `ltsp157` | `123456` | `209.99.185.59` | 2026-06-28T10:59:43 |
| `root` | `root2009` | `209.99.185.59` | 2026-06-28T11:00:40 |
| `ubuntu` | `qazwsx123` | `209.99.185.59` | 2026-06-28T11:01:36 |
| `root` | `G*t!sgshj@s^56e#5l` | `209.99.185.59` | 2026-06-28T11:02:33 |
| `quadralia` | `666666` | `209.99.185.59` | 2026-06-28T11:03:30 |
| `localadmin` | `localadmin` | `209.99.185.59` | 2026-06-28T11:04:28 |
| `professor` | `professor` | `45.205.1.42` | 2026-06-28T11:04:43 |
| `tbsigdev` | `tbsigdev` | `209.99.185.59` | 2026-06-28T11:05:24 |
| `root` | `P@ssw0rd$$icd` | `209.99.185.59` | 2026-06-28T11:06:19 |
| `zhouh` | `test123` | `209.99.185.59` | 2026-06-28T11:07:13 |
| `fly` | `fly` | `209.99.185.59` | 2026-06-28T11:08:09 |
| `ISTBI_data` | `istbI(*)` | `209.99.185.59` | 2026-06-28T11:09:06 |
| `root` | `raspberry` | `45.198.224.120` | 2026-06-28T11:09:23 |
| `yuehao` | `yuehao` | `209.99.185.59` | 2026-06-28T11:10:04 |
| `ubuntu` | `000000000` | `209.99.185.59` | 2026-06-28T11:11:03 |
| `fuy20` | `8CTVJ//ljPM=` | `209.99.185.59` | 2026-06-28T11:12:01 |
| `zhangxinkui` | `333333` | `209.99.185.59` | 2026-06-28T11:13:00 |
| `cy` | `cy123` | `209.99.185.59` | 2026-06-28T11:14:02 |
| `ubuntu` | `00000` | `209.99.185.59` | 2026-06-28T11:15:01 |
| `suporte` | `123456` | `209.99.185.59` | 2026-06-28T11:16:01 |
| `kezhiying` | `kezhiying112526+1s` | `209.99.185.59` | 2026-06-28T11:17:02 |
| `ubuntu` | `root123456` | `209.99.185.59` | 2026-06-28T11:18:04 |
| `marketing` | `marketing` | `209.99.185.59` | 2026-06-28T11:19:04 |
| `root` | `speakteam` | `45.205.1.42` | 2026-06-28T11:19:24 |
| `root` | `zsexdrcft` | `209.99.185.59` | 2026-06-28T11:20:11 |
| `root` | `super` | `45.198.224.120` | 2026-06-28T11:20:54 |
| `root` | `$$naveen18!!` | `209.99.185.59` | 2026-06-28T11:21:15 |
| `wzy` | `Yeah1432576554` | `209.99.185.59` | 2026-06-28T11:22:17 |
| `vps` | `passwd` | `209.99.185.59` | 2026-06-28T11:23:19 |
| `root` | `P@ssw0rd1!` | `209.99.185.59` | 2026-06-28T11:24:23 |
| `root` | `21` | `209.99.185.59` | 2026-06-28T11:25:25 |
| `vps` | `123` | `209.99.185.59` | 2026-06-28T11:26:25 |
| `root` | `Password@12345` | `10.0.0.73` | 2026-06-28T11:27:13 |
| `root` | `test@1234` | `209.99.185.59` | 2026-06-28T11:27:26 |
| `gentai` | `gentai` | `209.99.185.59` | 2026-06-28T11:28:28 |
| `root` | `Pass12345` | `209.99.185.59` | 2026-06-28T11:29:31 |
| `wq` | `123456` | `209.99.185.59` | 2026-06-28T11:30:32 |
| `root` | `999888777` | `209.99.185.59` | 2026-06-28T11:31:35 |
| `root` | `purple` | `45.198.224.120` | 2026-06-28T11:32:22 |
| `zq` | `123` | `209.99.185.59` | 2026-06-28T11:32:36 |
| `system` | `123456` | `209.99.185.59` | 2026-06-28T11:33:37 |
| `ubuntu` | `asdasd` | `45.205.1.42` | 2026-06-28T11:34:25 |
| `wagner` | `wagner` | `209.99.185.59` | 2026-06-28T11:34:39 |
| `ns` | `ns1234` | `209.99.185.59` | 2026-06-28T11:35:45 |
| `root` | `F1pnA%3W?v` | `209.99.185.59` | 2026-06-28T11:36:51 |
| `Dio` | `Dio` | `209.99.185.59` | 2026-06-28T11:37:54 |
| `root` | `S3cureLinux#Passw0rd!` | `209.99.185.59` | 2026-06-28T11:38:57 |
| `root` | `﻿------fuck------` | `218.203.203.232` | 2026-06-28T11:39:53 |
| `cl` | `123456` | `209.99.185.59` | 2026-06-28T11:39:59 |
| `root` | `3141592` | `209.99.185.59` | 2026-06-28T11:41:04 |
| `zhengchaoxin` | `zhengchaoxin` | `209.99.185.59` | 2026-06-28T11:42:09 |
| `dev` | `123456` | `209.99.185.59` | 2026-06-28T11:43:12 |
| `test3` | `test3` | `45.198.224.120` | 2026-06-28T11:43:38 |
| `ftp_test` | `ftp_test123` | `209.99.185.59` | 2026-06-28T11:44:17 |
| `root` | `qazwsxedcrfvtgb` | `209.99.185.59` | 2026-06-28T11:45:21 |
| `qifenghuang` | `worldpass2808` | `209.99.185.59` | 2026-06-28T11:46:24 |
| `root` | `qwe12#` | `209.99.185.59` | 2026-06-28T11:47:31 |
| `apache` | `test321` | `209.99.185.59` | 2026-06-28T11:48:37 |
| `guest` | `princess` | `45.205.1.42` | 2026-06-28T11:49:22 |
| `root` | `passwd#123` | `209.99.185.59` | 2026-06-28T11:49:44 |
| `yegu` | `yegu` | `209.99.185.59` | 2026-06-28T11:50:49 |
| `root` | `3bb316793206b1ffb1c4499cb167e0fcf69d26a9fcdfd870` | `209.99.185.59` | 2026-06-28T11:51:55 |
| `t` | `t` | `209.99.185.59` | 2026-06-28T11:53:02 |
| `xiaobing` | `123` | `209.99.185.59` | 2026-06-28T11:54:11 |
| `root` | `softball` | `45.198.224.120` | 2026-06-28T11:55:03 |
| `wp` | `wp123` | `209.99.185.59` | 2026-06-28T11:55:21 |
| `root` | `asdf0` | `209.99.185.59` | 2026-06-28T11:56:28 |
| `root` | `Password@12345` | `185.242.3.195` | 2026-06-28T11:56:46 |
| `ubuntu` | `abc123!!` | `209.99.185.59` | 2026-06-28T11:57:33 |
| `joyhan` | `123456` | `209.99.185.59` | 2026-06-28T11:58:38 |
| `test` | `123456qwer!` | `209.99.185.59` | 2026-06-28T11:59:45 |
| `lsw` | `lsw` | `209.99.185.59` | 2026-06-28T12:00:40 |
| `admin` | `admin` | `159.65.91.36` | 2026-06-28T12:00:55 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-28T12:00:55 |
| `root` | `123321123321` | `209.99.185.59` | 2026-06-28T12:01:26 |
| `gyuwon` | `3578` | `209.99.185.59` | 2026-06-28T12:02:10 |
| `root` | `123QWE!@#` | `209.99.185.59` | 2026-06-28T12:02:56 |
| `kipt` | `222222` | `209.99.185.59` | 2026-06-28T12:03:41 |
| `root` | `qweQWE123` | `45.205.1.42` | 2026-06-28T12:03:56 |
| `root` | `Sugon#W0rld` | `209.99.185.59` | 2026-06-28T12:04:27 |
| `zhangxinkui` | `123456` | `209.99.185.59` | 2026-06-28T12:05:13 |
| `tll` | `123456` | `209.99.185.59` | 2026-06-28T12:06:01 |
| `ubuntu` | `P@ssw0rd` | `45.198.224.120` | 2026-06-28T12:06:09 |
| `sander` | `sander111111` | `209.99.185.59` | 2026-06-28T12:06:50 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-28T12:07:36 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-28T12:07:36 |
| `root` | `999` | `209.99.185.59` | 2026-06-28T12:07:39 |
| `nagios` | `1234` | `209.99.185.59` | 2026-06-28T12:08:28 |
| `root` | `14872824` | `209.99.185.59` | 2026-06-28T12:09:16 |
| `LiuMinyue` | `7ZHHIqxiGZ` | `209.99.185.59` | 2026-06-28T12:10:04 |
| `syj` | `syj123456` | `209.99.185.59` | 2026-06-28T12:10:50 |
| `test` | `123654` | `209.99.185.59` | 2026-06-28T12:11:38 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `45.142.154.108` | 2026-06-28T12:11:39 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-28T12:12:24 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-28T12:12:24 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-28T12:12:26 |
| `root` | `76cI&D#^nykNxzf^dnwPjGv&` | `209.99.185.59` | 2026-06-28T12:12:27 |
| `test1` | `pgj-heu05HQM=bMvz` | `209.99.185.59` | 2026-06-28T12:13:16 |
| `Zhanghua` | `666666` | `209.99.185.59` | 2026-06-28T12:14:05 |
| `dell` | `Admin@777` | `209.99.185.59` | 2026-06-28T12:14:57 |
| `root` | `1qaz2wsx3edc` | `209.99.185.59` | 2026-06-28T12:15:47 |
| `baoshaoqi` | `baoshaoqi` | `45.148.10.239` | 2026-06-28T12:16:31 |
| `yubx` | `yubx` | `209.99.185.59` | 2026-06-28T12:16:36 |
| `root` | `zxc` | `209.99.185.59` | 2026-06-28T12:17:24 |
| `camera` | `camera123` | `45.198.224.120` | 2026-06-28T12:17:40 |
| `root` | `qazwsx741` | `10.0.0.73` | 2026-06-28T12:17:40 |
| `root` | `redhat72` | `209.99.185.59` | 2026-06-28T12:18:13 |
| `root` | `linux@123` | `45.205.1.42` | 2026-06-28T12:18:35 |
| `root` | `!@#!@#` | `209.99.185.59` | 2026-06-28T12:19:03 |
| `DingWB` | `DWB39219920914` | `209.99.185.59` | 2026-06-28T12:19:53 |
| `sync` | `sync` | `209.99.185.59` | 2026-06-28T12:20:44 |
| `hadoop` | `pass` | `209.99.185.59` | 2026-06-28T12:21:35 |
| `hdqcd` | `hdqcd2009` | `209.99.185.59` | 2026-06-28T12:22:25 |
| `zcc` | `zcc` | `209.99.185.59` | 2026-06-28T12:23:14 |
| `assha` | `assha` | `209.99.185.59` | 2026-06-28T12:24:04 |
| `linx` | `ysBE93UppC` | `209.99.185.59` | 2026-06-28T12:24:55 |
| `postgre` | `123456` | `209.99.185.59` | 2026-06-28T12:25:47 |
| `root` | `a1s2d3f4g5h6j7k8l9` | `209.99.185.59` | 2026-06-28T12:26:40 |
| `ubuntu` | `qwe` | `209.99.185.59` | 2026-06-28T12:27:33 |
| `miner2` | `miner2` | `209.99.185.59` | 2026-06-28T12:28:24 |
| `root` | `Test@123` | `45.198.224.120` | 2026-06-28T12:29:05 |
| `col` | `1234` | `209.99.185.59` | 2026-06-28T12:29:17 |
| `root` | `outbox` | `209.99.185.59` | 2026-06-28T12:30:09 |
| `root` | `snicker` | `209.99.185.59` | 2026-06-28T12:31:04 |
| `root1` | `1` | `209.99.185.59` | 2026-06-28T12:32:00 |
| `wanzhuo` | `DFZiRan` | `209.99.185.59` | 2026-06-28T12:32:56 |
| `root` | `QWEzaq123!@#` | `45.205.1.42` | 2026-06-28T12:33:03 |
| `ykjung` | `ykjung` | `209.99.185.59` | 2026-06-28T12:33:50 |
| `root` | `root123321` | `209.99.185.59` | 2026-06-28T12:34:43 |
| `ubuntu` | `123qweASD` | `209.99.185.59` | 2026-06-28T12:35:34 |
| `wcr` | `Hydrogen` | `209.99.185.59` | 2026-06-28T12:36:25 |
| `rtx` | `rtx` | `209.99.185.59` | 2026-06-28T12:37:30 |
| `root` | `000000000` | `209.99.185.59` | 2026-06-28T12:38:24 |
| `root` | `password@123456` | `209.99.185.59` | 2026-06-28T12:39:17 |
| `root` | `test1` | `209.99.185.59` | 2026-06-28T12:40:15 |
| `internet` | `internet` | `45.198.224.120` | 2026-06-28T12:40:32 |
| `hugo` | `hugo` | `209.99.185.59` | 2026-06-28T12:41:13 |
| `ruth` | `ruth` | `209.99.185.59` | 2026-06-28T12:42:08 |
| `lilei` | `zly@ll2012.0128` | `209.99.185.59` | 2026-06-28T12:43:05 |
| `root` | `ts` | `209.99.185.59` | 2026-06-28T12:44:00 |
| `steam` | `abc123` | `209.99.185.59` | 2026-06-28T12:44:56 |
| `songyuxiang` | `songyx` | `209.99.185.59` | 2026-06-28T12:45:53 |
| `root` | `qazwsx741` | `185.242.3.195` | 2026-06-28T12:46:28 |
| `root` | `poiuy` | `209.99.185.59` | 2026-06-28T12:46:48 |
| `uas` | `123456` | `209.99.185.59` | 2026-06-28T12:47:42 |
| `root` | `robert` | `45.205.1.42` | 2026-06-28T12:47:53 |
| `yeil` | `123456` | `209.99.185.59` | 2026-06-28T12:48:35 |
| `raomeng` | `raomeng` | `209.99.185.59` | 2026-06-28T12:49:28 |
| `root` | `iptviptv` | `209.99.185.59` | 2026-06-28T12:50:22 |
| `cyf` | `123456` | `209.99.185.59` | 2026-06-28T12:51:18 |
| `root` | `1qw23e` | `45.198.224.120` | 2026-06-28T12:51:51 |
| `peng` | `peng@supper2022` | `209.99.185.59` | 2026-06-28T12:52:15 |
| `sybase` | `sybase` | `209.99.185.59` | 2026-06-28T12:53:11 |
| `wtb` | `wtb` | `209.99.185.59` | 2026-06-28T12:54:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **312** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 152 |
| Paramiko (Python) | 6 |
| libssh | 6 |
| OpenSSH | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 149 | 5 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 149 | 5 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **16** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS215929` | Data Campus Limited | 1 | HIGH |
| `AS202412` | Omegatech LTD | 1 | HIGH |
| `AS9465` | AGOTOZ PTE. LTD. | 1 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (159)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1eee1dae7d18

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:55 |
| **Last Seen** | 2026-06-28 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:55:43` | `cowrie.session.connect` |
| `2026-06-28 10:55:43` | `cowrie.client.version` |
| `2026-06-28 10:55:43` | `cowrie.client.kex` |
| `2026-06-28 10:55:44` | `cowrie.login.success` |
| `2026-06-28 10:55:45` | `cowrie.session.params` |
| `2026-06-28 10:55:45` | `cowrie.command.input` |
| `2026-06-28 10:55:45` | `cowrie.log.closed` |
| `2026-06-28 10:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db72ec4e8f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:56 |
| **Last Seen** | 2026-06-28 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:56:39` | `cowrie.session.connect` |
| `2026-06-28 10:56:39` | `cowrie.client.version` |
| `2026-06-28 10:56:39` | `cowrie.client.kex` |
| `2026-06-28 10:56:39` | `cowrie.login.success` |
| `2026-06-28 10:56:40` | `cowrie.session.params` |
| `2026-06-28 10:56:40` | `cowrie.command.input` |
| `2026-06-28 10:56:40` | `cowrie.log.closed` |
| `2026-06-28 10:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475e63062301

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:57 |
| **Last Seen** | 2026-06-28 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:57:40` | `cowrie.session.connect` |
| `2026-06-28 10:57:40` | `cowrie.client.version` |
| `2026-06-28 10:57:40` | `cowrie.client.kex` |
| `2026-06-28 10:57:40` | `cowrie.login.success` |
| `2026-06-28 10:57:41` | `cowrie.session.params` |
| `2026-06-28 10:57:41` | `cowrie.command.input` |
| `2026-06-28 10:57:41` | `cowrie.log.closed` |
| `2026-06-28 10:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640b06926fb9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 10:57 |
| **Last Seen** | 2026-06-28 10:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:57:59` | `cowrie.session.connect` |
| `2026-06-28 10:58:01` | `cowrie.client.version` |
| `2026-06-28 10:58:01` | `cowrie.client.kex` |
| `2026-06-28 10:58:07` | `cowrie.login.success` |
| `2026-06-28 10:58:11` | `cowrie.session.params` |
| `2026-06-28 10:58:11` | `cowrie.command.input` |
| `2026-06-28 10:58:13` | `cowrie.log.closed` |
| `2026-06-28 10:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714a65afce67

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:58 |
| **Last Seen** | 2026-06-28 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:58:41` | `cowrie.session.connect` |
| `2026-06-28 10:58:41` | `cowrie.client.version` |
| `2026-06-28 10:58:42` | `cowrie.client.kex` |
| `2026-06-28 10:58:42` | `cowrie.login.success` |
| `2026-06-28 10:58:43` | `cowrie.session.params` |
| `2026-06-28 10:58:43` | `cowrie.command.input` |
| `2026-06-28 10:58:43` | `cowrie.log.closed` |
| `2026-06-28 10:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00db88e6f782

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:59 |
| **Last Seen** | 2026-06-28 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:59:43` | `cowrie.session.connect` |
| `2026-06-28 10:59:43` | `cowrie.client.version` |
| `2026-06-28 10:59:43` | `cowrie.client.kex` |
| `2026-06-28 10:59:43` | `cowrie.login.success` |
| `2026-06-28 10:59:44` | `cowrie.session.params` |
| `2026-06-28 10:59:44` | `cowrie.command.input` |
| `2026-06-28 10:59:44` | `cowrie.log.closed` |
| `2026-06-28 10:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8797a75911b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:00 |
| **Last Seen** | 2026-06-28 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:00:40` | `cowrie.session.connect` |
| `2026-06-28 11:00:40` | `cowrie.client.version` |
| `2026-06-28 11:00:40` | `cowrie.client.kex` |
| `2026-06-28 11:00:40` | `cowrie.login.success` |
| `2026-06-28 11:00:41` | `cowrie.session.params` |
| `2026-06-28 11:00:41` | `cowrie.command.input` |
| `2026-06-28 11:00:41` | `cowrie.log.closed` |
| `2026-06-28 11:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92523522834f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:01 |
| **Last Seen** | 2026-06-28 11:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:01:35` | `cowrie.session.connect` |
| `2026-06-28 11:01:35` | `cowrie.client.version` |
| `2026-06-28 11:01:35` | `cowrie.client.kex` |
| `2026-06-28 11:01:36` | `cowrie.login.success` |
| `2026-06-28 11:01:36` | `cowrie.session.params` |
| `2026-06-28 11:01:36` | `cowrie.command.input` |
| `2026-06-28 11:01:36` | `cowrie.log.closed` |
| `2026-06-28 11:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae93a6528d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:02 |
| **Last Seen** | 2026-06-28 11:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:02:32` | `cowrie.session.connect` |
| `2026-06-28 11:02:32` | `cowrie.client.version` |
| `2026-06-28 11:02:32` | `cowrie.client.kex` |
| `2026-06-28 11:02:33` | `cowrie.login.success` |
| `2026-06-28 11:02:33` | `cowrie.session.params` |
| `2026-06-28 11:02:33` | `cowrie.command.input` |
| `2026-06-28 11:02:34` | `cowrie.log.closed` |
| `2026-06-28 11:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7ce6d689c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:03 |
| **Last Seen** | 2026-06-28 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:03:30` | `cowrie.session.connect` |
| `2026-06-28 11:03:30` | `cowrie.client.version` |
| `2026-06-28 11:03:30` | `cowrie.client.kex` |
| `2026-06-28 11:03:30` | `cowrie.login.success` |
| `2026-06-28 11:03:31` | `cowrie.session.params` |
| `2026-06-28 11:03:31` | `cowrie.command.input` |
| `2026-06-28 11:03:31` | `cowrie.log.closed` |
| `2026-06-28 11:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6243b0237074

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:04 |
| **Last Seen** | 2026-06-28 11:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:04:27` | `cowrie.session.connect` |
| `2026-06-28 11:04:27` | `cowrie.client.version` |
| `2026-06-28 11:04:27` | `cowrie.client.kex` |
| `2026-06-28 11:04:28` | `cowrie.login.success` |
| `2026-06-28 11:04:28` | `cowrie.session.params` |
| `2026-06-28 11:04:28` | `cowrie.command.input` |
| `2026-06-28 11:04:29` | `cowrie.log.closed` |
| `2026-06-28 11:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a31e043717

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 11:04 |
| **Last Seen** | 2026-06-28 11:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:04:41` | `cowrie.session.connect` |
| `2026-06-28 11:04:42` | `cowrie.client.version` |
| `2026-06-28 11:04:42` | `cowrie.client.kex` |
| `2026-06-28 11:04:43` | `cowrie.login.success` |
| `2026-06-28 11:04:45` | `cowrie.session.params` |
| `2026-06-28 11:04:45` | `cowrie.command.input` |
| `2026-06-28 11:04:45` | `cowrie.log.closed` |
| `2026-06-28 11:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7328d7f2e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:05 |
| **Last Seen** | 2026-06-28 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:05:24` | `cowrie.session.connect` |
| `2026-06-28 11:05:24` | `cowrie.client.version` |
| `2026-06-28 11:05:24` | `cowrie.client.kex` |
| `2026-06-28 11:05:24` | `cowrie.login.success` |
| `2026-06-28 11:05:25` | `cowrie.session.params` |
| `2026-06-28 11:05:25` | `cowrie.command.input` |
| `2026-06-28 11:05:25` | `cowrie.log.closed` |
| `2026-06-28 11:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a6f073cce6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:06 |
| **Last Seen** | 2026-06-28 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:06:19` | `cowrie.session.connect` |
| `2026-06-28 11:06:19` | `cowrie.client.version` |
| `2026-06-28 11:06:19` | `cowrie.client.kex` |
| `2026-06-28 11:06:19` | `cowrie.login.success` |
| `2026-06-28 11:06:20` | `cowrie.session.params` |
| `2026-06-28 11:06:20` | `cowrie.command.input` |
| `2026-06-28 11:06:20` | `cowrie.log.closed` |
| `2026-06-28 11:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0662ef50858d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:07 |
| **Last Seen** | 2026-06-28 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:07:13` | `cowrie.session.connect` |
| `2026-06-28 11:07:13` | `cowrie.client.version` |
| `2026-06-28 11:07:13` | `cowrie.client.kex` |
| `2026-06-28 11:07:13` | `cowrie.login.success` |
| `2026-06-28 11:07:14` | `cowrie.session.params` |
| `2026-06-28 11:07:14` | `cowrie.command.input` |
| `2026-06-28 11:07:14` | `cowrie.log.closed` |
| `2026-06-28 11:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6503e8b09be2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:08 |
| **Last Seen** | 2026-06-28 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:08:08` | `cowrie.session.connect` |
| `2026-06-28 11:08:08` | `cowrie.client.version` |
| `2026-06-28 11:08:09` | `cowrie.client.kex` |
| `2026-06-28 11:08:09` | `cowrie.login.success` |
| `2026-06-28 11:08:10` | `cowrie.session.params` |
| `2026-06-28 11:08:10` | `cowrie.command.input` |
| `2026-06-28 11:08:10` | `cowrie.log.closed` |
| `2026-06-28 11:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201303c28a0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:09 |
| **Last Seen** | 2026-06-28 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:09:05` | `cowrie.session.connect` |
| `2026-06-28 11:09:05` | `cowrie.client.version` |
| `2026-06-28 11:09:05` | `cowrie.client.kex` |
| `2026-06-28 11:09:06` | `cowrie.login.success` |
| `2026-06-28 11:09:07` | `cowrie.session.params` |
| `2026-06-28 11:09:07` | `cowrie.command.input` |
| `2026-06-28 11:09:07` | `cowrie.log.closed` |
| `2026-06-28 11:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79b31df1abf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 11:09 |
| **Last Seen** | 2026-06-28 11:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:09:16` | `cowrie.session.connect` |
| `2026-06-28 11:09:17` | `cowrie.client.version` |
| `2026-06-28 11:09:17` | `cowrie.client.kex` |
| `2026-06-28 11:09:23` | `cowrie.login.success` |
| `2026-06-28 11:09:26` | `cowrie.session.params` |
| `2026-06-28 11:09:26` | `cowrie.command.input` |
| `2026-06-28 11:09:28` | `cowrie.log.closed` |
| `2026-06-28 11:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801e9be775fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:10 |
| **Last Seen** | 2026-06-28 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:10:04` | `cowrie.session.connect` |
| `2026-06-28 11:10:04` | `cowrie.client.version` |
| `2026-06-28 11:10:04` | `cowrie.client.kex` |
| `2026-06-28 11:10:04` | `cowrie.login.success` |
| `2026-06-28 11:10:05` | `cowrie.session.params` |
| `2026-06-28 11:10:05` | `cowrie.command.input` |
| `2026-06-28 11:10:05` | `cowrie.log.closed` |
| `2026-06-28 11:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3497d0cd2f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:11 |
| **Last Seen** | 2026-06-28 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:11:02` | `cowrie.session.connect` |
| `2026-06-28 11:11:02` | `cowrie.client.version` |
| `2026-06-28 11:11:02` | `cowrie.client.kex` |
| `2026-06-28 11:11:03` | `cowrie.login.success` |
| `2026-06-28 11:11:04` | `cowrie.session.params` |
| `2026-06-28 11:11:04` | `cowrie.command.input` |
| `2026-06-28 11:11:04` | `cowrie.log.closed` |
| `2026-06-28 11:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087d6b3e005e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:12 |
| **Last Seen** | 2026-06-28 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:12:01` | `cowrie.session.connect` |
| `2026-06-28 11:12:01` | `cowrie.client.version` |
| `2026-06-28 11:12:01` | `cowrie.client.kex` |
| `2026-06-28 11:12:01` | `cowrie.login.success` |
| `2026-06-28 11:12:02` | `cowrie.session.params` |
| `2026-06-28 11:12:02` | `cowrie.command.input` |
| `2026-06-28 11:12:02` | `cowrie.log.closed` |
| `2026-06-28 11:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b066aca2d8c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:13 |
| **Last Seen** | 2026-06-28 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:13:00` | `cowrie.session.connect` |
| `2026-06-28 11:13:00` | `cowrie.client.version` |
| `2026-06-28 11:13:00` | `cowrie.client.kex` |
| `2026-06-28 11:13:00` | `cowrie.login.success` |
| `2026-06-28 11:13:01` | `cowrie.session.params` |
| `2026-06-28 11:13:01` | `cowrie.command.input` |
| `2026-06-28 11:13:01` | `cowrie.log.closed` |
| `2026-06-28 11:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e48d087c150

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:14 |
| **Last Seen** | 2026-06-28 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:14:01` | `cowrie.session.connect` |
| `2026-06-28 11:14:01` | `cowrie.client.version` |
| `2026-06-28 11:14:01` | `cowrie.client.kex` |
| `2026-06-28 11:14:02` | `cowrie.login.success` |
| `2026-06-28 11:14:02` | `cowrie.session.params` |
| `2026-06-28 11:14:02` | `cowrie.command.input` |
| `2026-06-28 11:14:03` | `cowrie.log.closed` |
| `2026-06-28 11:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78529178ab11

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:15 |
| **Last Seen** | 2026-06-28 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:15:00` | `cowrie.session.connect` |
| `2026-06-28 11:15:00` | `cowrie.client.version` |
| `2026-06-28 11:15:00` | `cowrie.client.kex` |
| `2026-06-28 11:15:01` | `cowrie.login.success` |
| `2026-06-28 11:15:01` | `cowrie.session.params` |
| `2026-06-28 11:15:01` | `cowrie.command.input` |
| `2026-06-28 11:15:01` | `cowrie.log.closed` |
| `2026-06-28 11:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107696752ee9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:16 |
| **Last Seen** | 2026-06-28 11:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:16:01` | `cowrie.session.connect` |
| `2026-06-28 11:16:01` | `cowrie.client.version` |
| `2026-06-28 11:16:01` | `cowrie.client.kex` |
| `2026-06-28 11:16:01` | `cowrie.login.success` |
| `2026-06-28 11:16:02` | `cowrie.session.params` |
| `2026-06-28 11:16:02` | `cowrie.command.input` |
| `2026-06-28 11:16:02` | `cowrie.log.closed` |
| `2026-06-28 11:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f483aedc9a31

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:17 |
| **Last Seen** | 2026-06-28 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:17:02` | `cowrie.session.connect` |
| `2026-06-28 11:17:02` | `cowrie.client.version` |
| `2026-06-28 11:17:02` | `cowrie.client.kex` |
| `2026-06-28 11:17:02` | `cowrie.login.success` |
| `2026-06-28 11:17:03` | `cowrie.session.params` |
| `2026-06-28 11:17:03` | `cowrie.command.input` |
| `2026-06-28 11:17:03` | `cowrie.log.closed` |
| `2026-06-28 11:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-884e46613bdc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:18 |
| **Last Seen** | 2026-06-28 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:18:03` | `cowrie.session.connect` |
| `2026-06-28 11:18:03` | `cowrie.client.version` |
| `2026-06-28 11:18:04` | `cowrie.client.kex` |
| `2026-06-28 11:18:04` | `cowrie.login.success` |
| `2026-06-28 11:18:05` | `cowrie.session.params` |
| `2026-06-28 11:18:05` | `cowrie.command.input` |
| `2026-06-28 11:18:05` | `cowrie.log.closed` |
| `2026-06-28 11:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7184fec36fe8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:19 |
| **Last Seen** | 2026-06-28 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:19:03` | `cowrie.session.connect` |
| `2026-06-28 11:19:03` | `cowrie.client.version` |
| `2026-06-28 11:19:03` | `cowrie.client.kex` |
| `2026-06-28 11:19:04` | `cowrie.login.success` |
| `2026-06-28 11:19:05` | `cowrie.session.params` |
| `2026-06-28 11:19:05` | `cowrie.command.input` |
| `2026-06-28 11:19:05` | `cowrie.log.closed` |
| `2026-06-28 11:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e9c7799289

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 11:19 |
| **Last Seen** | 2026-06-28 11:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:19:22` | `cowrie.session.connect` |
| `2026-06-28 11:19:23` | `cowrie.client.version` |
| `2026-06-28 11:19:23` | `cowrie.client.kex` |
| `2026-06-28 11:19:24` | `cowrie.login.success` |
| `2026-06-28 11:19:25` | `cowrie.session.params` |
| `2026-06-28 11:19:25` | `cowrie.command.input` |
| `2026-06-28 11:19:26` | `cowrie.log.closed` |
| `2026-06-28 11:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe465956511f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:20 |
| **Last Seen** | 2026-06-28 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:20:11` | `cowrie.session.connect` |
| `2026-06-28 11:20:11` | `cowrie.client.version` |
| `2026-06-28 11:20:11` | `cowrie.client.kex` |
| `2026-06-28 11:20:11` | `cowrie.login.success` |
| `2026-06-28 11:20:12` | `cowrie.session.params` |
| `2026-06-28 11:20:12` | `cowrie.command.input` |
| `2026-06-28 11:20:12` | `cowrie.log.closed` |
| `2026-06-28 11:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9211f05e1b76

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 11:20 |
| **Last Seen** | 2026-06-28 11:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:20:47` | `cowrie.session.connect` |
| `2026-06-28 11:20:48` | `cowrie.client.version` |
| `2026-06-28 11:20:48` | `cowrie.client.kex` |
| `2026-06-28 11:20:54` | `cowrie.login.success` |
| `2026-06-28 11:20:57` | `cowrie.session.params` |
| `2026-06-28 11:20:57` | `cowrie.command.input` |
| `2026-06-28 11:21:00` | `cowrie.log.closed` |
| `2026-06-28 11:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c274e87ed87

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:21 |
| **Last Seen** | 2026-06-28 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:21:15` | `cowrie.session.connect` |
| `2026-06-28 11:21:15` | `cowrie.client.version` |
| `2026-06-28 11:21:15` | `cowrie.client.kex` |
| `2026-06-28 11:21:15` | `cowrie.login.success` |
| `2026-06-28 11:21:16` | `cowrie.session.params` |
| `2026-06-28 11:21:16` | `cowrie.command.input` |
| `2026-06-28 11:21:16` | `cowrie.log.closed` |
| `2026-06-28 11:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2de937a7f29

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:22 |
| **Last Seen** | 2026-06-28 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:22:16` | `cowrie.session.connect` |
| `2026-06-28 11:22:16` | `cowrie.client.version` |
| `2026-06-28 11:22:16` | `cowrie.client.kex` |
| `2026-06-28 11:22:17` | `cowrie.login.success` |
| `2026-06-28 11:22:17` | `cowrie.session.params` |
| `2026-06-28 11:22:17` | `cowrie.command.input` |
| `2026-06-28 11:22:18` | `cowrie.log.closed` |
| `2026-06-28 11:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8bc7a98e819

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:23 |
| **Last Seen** | 2026-06-28 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:23:19` | `cowrie.session.connect` |
| `2026-06-28 11:23:19` | `cowrie.client.version` |
| `2026-06-28 11:23:19` | `cowrie.client.kex` |
| `2026-06-28 11:23:19` | `cowrie.login.success` |
| `2026-06-28 11:23:20` | `cowrie.session.params` |
| `2026-06-28 11:23:20` | `cowrie.command.input` |
| `2026-06-28 11:23:20` | `cowrie.log.closed` |
| `2026-06-28 11:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9cd283ef0fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:24 |
| **Last Seen** | 2026-06-28 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:24:23` | `cowrie.session.connect` |
| `2026-06-28 11:24:23` | `cowrie.client.version` |
| `2026-06-28 11:24:23` | `cowrie.client.kex` |
| `2026-06-28 11:24:23` | `cowrie.login.success` |
| `2026-06-28 11:24:24` | `cowrie.session.params` |
| `2026-06-28 11:24:24` | `cowrie.command.input` |
| `2026-06-28 11:24:24` | `cowrie.log.closed` |
| `2026-06-28 11:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae36073f96b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:25 |
| **Last Seen** | 2026-06-28 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:25:24` | `cowrie.session.connect` |
| `2026-06-28 11:25:24` | `cowrie.client.version` |
| `2026-06-28 11:25:24` | `cowrie.client.kex` |
| `2026-06-28 11:25:25` | `cowrie.login.success` |
| `2026-06-28 11:25:26` | `cowrie.session.params` |
| `2026-06-28 11:25:26` | `cowrie.command.input` |
| `2026-06-28 11:25:26` | `cowrie.log.closed` |
| `2026-06-28 11:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c34ffcb760

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:26 |
| **Last Seen** | 2026-06-28 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:26:25` | `cowrie.session.connect` |
| `2026-06-28 11:26:25` | `cowrie.client.version` |
| `2026-06-28 11:26:25` | `cowrie.client.kex` |
| `2026-06-28 11:26:25` | `cowrie.login.success` |
| `2026-06-28 11:26:26` | `cowrie.session.params` |
| `2026-06-28 11:26:26` | `cowrie.command.input` |
| `2026-06-28 11:26:26` | `cowrie.log.closed` |
| `2026-06-28 11:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2b19e9c7b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:27 |
| **Last Seen** | 2026-06-28 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:27:26` | `cowrie.session.connect` |
| `2026-06-28 11:27:26` | `cowrie.client.version` |
| `2026-06-28 11:27:26` | `cowrie.client.kex` |
| `2026-06-28 11:27:26` | `cowrie.login.success` |
| `2026-06-28 11:27:27` | `cowrie.session.params` |
| `2026-06-28 11:27:27` | `cowrie.command.input` |
| `2026-06-28 11:27:27` | `cowrie.log.closed` |
| `2026-06-28 11:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f2f51ba840

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:28 |
| **Last Seen** | 2026-06-28 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:28:28` | `cowrie.session.connect` |
| `2026-06-28 11:28:28` | `cowrie.client.version` |
| `2026-06-28 11:28:28` | `cowrie.client.kex` |
| `2026-06-28 11:28:28` | `cowrie.login.success` |
| `2026-06-28 11:28:29` | `cowrie.session.params` |
| `2026-06-28 11:28:29` | `cowrie.command.input` |
| `2026-06-28 11:28:29` | `cowrie.log.closed` |
| `2026-06-28 11:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e5bfc7ca8f5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:29 |
| **Last Seen** | 2026-06-28 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:29:31` | `cowrie.session.connect` |
| `2026-06-28 11:29:31` | `cowrie.client.version` |
| `2026-06-28 11:29:31` | `cowrie.client.kex` |
| `2026-06-28 11:29:31` | `cowrie.login.success` |
| `2026-06-28 11:29:32` | `cowrie.session.params` |
| `2026-06-28 11:29:32` | `cowrie.command.input` |
| `2026-06-28 11:29:32` | `cowrie.log.closed` |
| `2026-06-28 11:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c26bc49d9884

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:30 |
| **Last Seen** | 2026-06-28 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:30:32` | `cowrie.session.connect` |
| `2026-06-28 11:30:32` | `cowrie.client.version` |
| `2026-06-28 11:30:32` | `cowrie.client.kex` |
| `2026-06-28 11:30:32` | `cowrie.login.success` |
| `2026-06-28 11:30:33` | `cowrie.session.params` |
| `2026-06-28 11:30:33` | `cowrie.command.input` |
| `2026-06-28 11:30:33` | `cowrie.log.closed` |
| `2026-06-28 11:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb8399bde15

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:31 |
| **Last Seen** | 2026-06-28 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:31:35` | `cowrie.session.connect` |
| `2026-06-28 11:31:35` | `cowrie.client.version` |
| `2026-06-28 11:31:35` | `cowrie.client.kex` |
| `2026-06-28 11:31:35` | `cowrie.login.success` |
| `2026-06-28 11:31:36` | `cowrie.session.params` |
| `2026-06-28 11:31:36` | `cowrie.command.input` |
| `2026-06-28 11:31:36` | `cowrie.log.closed` |
| `2026-06-28 11:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c7c355f758

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 11:32 |
| **Last Seen** | 2026-06-28 11:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:32:14` | `cowrie.session.connect` |
| `2026-06-28 11:32:16` | `cowrie.client.version` |
| `2026-06-28 11:32:16` | `cowrie.client.kex` |
| `2026-06-28 11:32:22` | `cowrie.login.success` |
| `2026-06-28 11:32:26` | `cowrie.session.params` |
| `2026-06-28 11:32:26` | `cowrie.command.input` |
| `2026-06-28 11:32:28` | `cowrie.log.closed` |
| `2026-06-28 11:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fba13e934a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:32 |
| **Last Seen** | 2026-06-28 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:32:35` | `cowrie.session.connect` |
| `2026-06-28 11:32:35` | `cowrie.client.version` |
| `2026-06-28 11:32:35` | `cowrie.client.kex` |
| `2026-06-28 11:32:36` | `cowrie.login.success` |
| `2026-06-28 11:32:36` | `cowrie.session.params` |
| `2026-06-28 11:32:36` | `cowrie.command.input` |
| `2026-06-28 11:32:37` | `cowrie.log.closed` |
| `2026-06-28 11:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d353389d6e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:33 |
| **Last Seen** | 2026-06-28 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:33:36` | `cowrie.session.connect` |
| `2026-06-28 11:33:36` | `cowrie.client.version` |
| `2026-06-28 11:33:36` | `cowrie.client.kex` |
| `2026-06-28 11:33:37` | `cowrie.login.success` |
| `2026-06-28 11:33:37` | `cowrie.session.params` |
| `2026-06-28 11:33:37` | `cowrie.command.input` |
| `2026-06-28 11:33:37` | `cowrie.log.closed` |
| `2026-06-28 11:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326a333ef561

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 11:34 |
| **Last Seen** | 2026-06-28 11:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:34:23` | `cowrie.session.connect` |
| `2026-06-28 11:34:24` | `cowrie.client.version` |
| `2026-06-28 11:34:24` | `cowrie.client.kex` |
| `2026-06-28 11:34:25` | `cowrie.login.success` |
| `2026-06-28 11:34:27` | `cowrie.session.params` |
| `2026-06-28 11:34:27` | `cowrie.command.input` |
| `2026-06-28 11:34:28` | `cowrie.log.closed` |
| `2026-06-28 11:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9bb104fbd2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:34 |
| **Last Seen** | 2026-06-28 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:34:39` | `cowrie.session.connect` |
| `2026-06-28 11:34:39` | `cowrie.client.version` |
| `2026-06-28 11:34:39` | `cowrie.client.kex` |
| `2026-06-28 11:34:39` | `cowrie.login.success` |
| `2026-06-28 11:34:40` | `cowrie.session.params` |
| `2026-06-28 11:34:40` | `cowrie.command.input` |
| `2026-06-28 11:34:40` | `cowrie.log.closed` |
| `2026-06-28 11:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0541d7bb61e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:35 |
| **Last Seen** | 2026-06-28 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:35:44` | `cowrie.session.connect` |
| `2026-06-28 11:35:44` | `cowrie.client.version` |
| `2026-06-28 11:35:44` | `cowrie.client.kex` |
| `2026-06-28 11:35:45` | `cowrie.login.success` |
| `2026-06-28 11:35:45` | `cowrie.session.params` |
| `2026-06-28 11:35:45` | `cowrie.command.input` |
| `2026-06-28 11:35:46` | `cowrie.log.closed` |
| `2026-06-28 11:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-746c692b16c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:36 |
| **Last Seen** | 2026-06-28 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:36:51` | `cowrie.session.connect` |
| `2026-06-28 11:36:51` | `cowrie.client.version` |
| `2026-06-28 11:36:51` | `cowrie.client.kex` |
| `2026-06-28 11:36:51` | `cowrie.login.success` |
| `2026-06-28 11:36:52` | `cowrie.session.params` |
| `2026-06-28 11:36:52` | `cowrie.command.input` |
| `2026-06-28 11:36:52` | `cowrie.log.closed` |
| `2026-06-28 11:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885a6118dd77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:37 |
| **Last Seen** | 2026-06-28 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:37:54` | `cowrie.session.connect` |
| `2026-06-28 11:37:54` | `cowrie.client.version` |
| `2026-06-28 11:37:54` | `cowrie.client.kex` |
| `2026-06-28 11:37:54` | `cowrie.login.success` |
| `2026-06-28 11:37:55` | `cowrie.session.params` |
| `2026-06-28 11:37:55` | `cowrie.command.input` |
| `2026-06-28 11:37:55` | `cowrie.log.closed` |
| `2026-06-28 11:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ecf927347d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:38 |
| **Last Seen** | 2026-06-28 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:38:56` | `cowrie.session.connect` |
| `2026-06-28 11:38:56` | `cowrie.client.version` |
| `2026-06-28 11:38:56` | `cowrie.client.kex` |
| `2026-06-28 11:38:57` | `cowrie.login.success` |
| `2026-06-28 11:38:57` | `cowrie.session.params` |
| `2026-06-28 11:38:57` | `cowrie.command.input` |
| `2026-06-28 11:38:58` | `cowrie.log.closed` |
| `2026-06-28 11:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986c879b507b

| Field | Detail |
|---|---|
| **Source IP** | `218.203.203[.]232` |
| **First Seen** | 2026-06-28 11:39 |
| **Last Seen** | 2026-06-28 11:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:39:50` | `cowrie.session.connect` |
| `2026-06-28 11:39:51` | `cowrie.client.version` |
| `2026-06-28 11:39:51` | `cowrie.client.kex` |
| `2026-06-28 11:39:53` | `cowrie.login.success` |
| `2026-06-28 11:39:55` | `cowrie.session.params` |
| `2026-06-28 11:39:55` | `cowrie.command.input` |
| `2026-06-28 11:39:56` | `cowrie.log.closed` |
| `2026-06-28 11:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.203.203[.]232` to AbuseIPDB if not already reported
- [ ] Block `218.203.203[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1390f77467

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:39 |
| **Last Seen** | 2026-06-28 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:39:59` | `cowrie.session.connect` |
| `2026-06-28 11:39:59` | `cowrie.client.version` |
| `2026-06-28 11:39:59` | `cowrie.client.kex` |
| `2026-06-28 11:39:59` | `cowrie.login.success` |
| `2026-06-28 11:40:00` | `cowrie.session.params` |
| `2026-06-28 11:40:00` | `cowrie.command.input` |
| `2026-06-28 11:40:00` | `cowrie.log.closed` |
| `2026-06-28 11:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f21a96bcea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:41 |
| **Last Seen** | 2026-06-28 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:41:03` | `cowrie.session.connect` |
| `2026-06-28 11:41:03` | `cowrie.client.version` |
| `2026-06-28 11:41:03` | `cowrie.client.kex` |
| `2026-06-28 11:41:04` | `cowrie.login.success` |
| `2026-06-28 11:41:05` | `cowrie.session.params` |
| `2026-06-28 11:41:05` | `cowrie.command.input` |
| `2026-06-28 11:41:05` | `cowrie.log.closed` |
| `2026-06-28 11:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e39945470a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:42 |
| **Last Seen** | 2026-06-28 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:42:08` | `cowrie.session.connect` |
| `2026-06-28 11:42:08` | `cowrie.client.version` |
| `2026-06-28 11:42:08` | `cowrie.client.kex` |
| `2026-06-28 11:42:09` | `cowrie.login.success` |
| `2026-06-28 11:42:09` | `cowrie.session.params` |
| `2026-06-28 11:42:09` | `cowrie.command.input` |
| `2026-06-28 11:42:10` | `cowrie.log.closed` |
| `2026-06-28 11:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a904c443828

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:43 |
| **Last Seen** | 2026-06-28 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:43:12` | `cowrie.session.connect` |
| `2026-06-28 11:43:12` | `cowrie.client.version` |
| `2026-06-28 11:43:12` | `cowrie.client.kex` |
| `2026-06-28 11:43:12` | `cowrie.login.success` |
| `2026-06-28 11:43:13` | `cowrie.session.params` |
| `2026-06-28 11:43:13` | `cowrie.command.input` |
| `2026-06-28 11:43:13` | `cowrie.log.closed` |
| `2026-06-28 11:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a25258db4c5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 11:43 |
| **Last Seen** | 2026-06-28 11:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:43:30` | `cowrie.session.connect` |
| `2026-06-28 11:43:33` | `cowrie.client.version` |
| `2026-06-28 11:43:33` | `cowrie.client.kex` |
| `2026-06-28 11:43:38` | `cowrie.login.success` |
| `2026-06-28 11:43:42` | `cowrie.session.params` |
| `2026-06-28 11:43:42` | `cowrie.command.input` |
| `2026-06-28 11:43:43` | `cowrie.log.closed` |
| `2026-06-28 11:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87942d2c2f2c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:44 |
| **Last Seen** | 2026-06-28 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:44:16` | `cowrie.session.connect` |
| `2026-06-28 11:44:16` | `cowrie.client.version` |
| `2026-06-28 11:44:16` | `cowrie.client.kex` |
| `2026-06-28 11:44:17` | `cowrie.login.success` |
| `2026-06-28 11:44:17` | `cowrie.session.params` |
| `2026-06-28 11:44:17` | `cowrie.command.input` |
| `2026-06-28 11:44:17` | `cowrie.log.closed` |
| `2026-06-28 11:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18cf52b5c34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:45 |
| **Last Seen** | 2026-06-28 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:45:21` | `cowrie.session.connect` |
| `2026-06-28 11:45:21` | `cowrie.client.version` |
| `2026-06-28 11:45:21` | `cowrie.client.kex` |
| `2026-06-28 11:45:21` | `cowrie.login.success` |
| `2026-06-28 11:45:22` | `cowrie.session.params` |
| `2026-06-28 11:45:22` | `cowrie.command.input` |
| `2026-06-28 11:45:22` | `cowrie.log.closed` |
| `2026-06-28 11:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02d11f0e50d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:46 |
| **Last Seen** | 2026-06-28 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:46:24` | `cowrie.session.connect` |
| `2026-06-28 11:46:24` | `cowrie.client.version` |
| `2026-06-28 11:46:24` | `cowrie.client.kex` |
| `2026-06-28 11:46:24` | `cowrie.login.success` |
| `2026-06-28 11:46:25` | `cowrie.session.params` |
| `2026-06-28 11:46:25` | `cowrie.command.input` |
| `2026-06-28 11:46:25` | `cowrie.log.closed` |
| `2026-06-28 11:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7bd505ce2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:47 |
| **Last Seen** | 2026-06-28 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:47:31` | `cowrie.session.connect` |
| `2026-06-28 11:47:31` | `cowrie.client.version` |
| `2026-06-28 11:47:31` | `cowrie.client.kex` |
| `2026-06-28 11:47:31` | `cowrie.login.success` |
| `2026-06-28 11:47:32` | `cowrie.session.params` |
| `2026-06-28 11:47:32` | `cowrie.command.input` |
| `2026-06-28 11:47:32` | `cowrie.log.closed` |
| `2026-06-28 11:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40fd68f773c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:48 |
| **Last Seen** | 2026-06-28 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:48:37` | `cowrie.session.connect` |
| `2026-06-28 11:48:37` | `cowrie.client.version` |
| `2026-06-28 11:48:37` | `cowrie.client.kex` |
| `2026-06-28 11:48:37` | `cowrie.login.success` |
| `2026-06-28 11:48:38` | `cowrie.session.params` |
| `2026-06-28 11:48:38` | `cowrie.command.input` |
| `2026-06-28 11:48:38` | `cowrie.log.closed` |
| `2026-06-28 11:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02c55e2a10c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 11:49 |
| **Last Seen** | 2026-06-28 11:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:49:19` | `cowrie.session.connect` |
| `2026-06-28 11:49:19` | `cowrie.client.version` |
| `2026-06-28 11:49:19` | `cowrie.client.kex` |
| `2026-06-28 11:49:22` | `cowrie.login.success` |
| `2026-06-28 11:49:23` | `cowrie.session.params` |
| `2026-06-28 11:49:23` | `cowrie.command.input` |
| `2026-06-28 11:49:23` | `cowrie.log.closed` |
| `2026-06-28 11:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-430701aa19b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:49 |
| **Last Seen** | 2026-06-28 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:49:43` | `cowrie.session.connect` |
| `2026-06-28 11:49:43` | `cowrie.client.version` |
| `2026-06-28 11:49:43` | `cowrie.client.kex` |
| `2026-06-28 11:49:44` | `cowrie.login.success` |
| `2026-06-28 11:49:44` | `cowrie.session.params` |
| `2026-06-28 11:49:44` | `cowrie.command.input` |
| `2026-06-28 11:49:45` | `cowrie.log.closed` |
| `2026-06-28 11:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da66104821d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:50 |
| **Last Seen** | 2026-06-28 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:50:48` | `cowrie.session.connect` |
| `2026-06-28 11:50:48` | `cowrie.client.version` |
| `2026-06-28 11:50:49` | `cowrie.client.kex` |
| `2026-06-28 11:50:49` | `cowrie.login.success` |
| `2026-06-28 11:50:50` | `cowrie.session.params` |
| `2026-06-28 11:50:50` | `cowrie.command.input` |
| `2026-06-28 11:50:50` | `cowrie.log.closed` |
| `2026-06-28 11:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e8df8c5a53

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:51 |
| **Last Seen** | 2026-06-28 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:51:54` | `cowrie.session.connect` |
| `2026-06-28 11:51:54` | `cowrie.client.version` |
| `2026-06-28 11:51:54` | `cowrie.client.kex` |
| `2026-06-28 11:51:55` | `cowrie.login.success` |
| `2026-06-28 11:51:55` | `cowrie.session.params` |
| `2026-06-28 11:51:55` | `cowrie.command.input` |
| `2026-06-28 11:51:55` | `cowrie.log.closed` |
| `2026-06-28 11:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7752e8b968c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:53 |
| **Last Seen** | 2026-06-28 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:53:01` | `cowrie.session.connect` |
| `2026-06-28 11:53:01` | `cowrie.client.version` |
| `2026-06-28 11:53:01` | `cowrie.client.kex` |
| `2026-06-28 11:53:02` | `cowrie.login.success` |
| `2026-06-28 11:53:02` | `cowrie.session.params` |
| `2026-06-28 11:53:02` | `cowrie.command.input` |
| `2026-06-28 11:53:03` | `cowrie.log.closed` |
| `2026-06-28 11:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bafb78bce22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:54 |
| **Last Seen** | 2026-06-28 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:54:10` | `cowrie.session.connect` |
| `2026-06-28 11:54:10` | `cowrie.client.version` |
| `2026-06-28 11:54:10` | `cowrie.client.kex` |
| `2026-06-28 11:54:11` | `cowrie.login.success` |
| `2026-06-28 11:54:12` | `cowrie.session.params` |
| `2026-06-28 11:54:12` | `cowrie.command.input` |
| `2026-06-28 11:54:12` | `cowrie.log.closed` |
| `2026-06-28 11:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6bcff4acc78

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 11:54 |
| **Last Seen** | 2026-06-28 11:55 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:54:56` | `cowrie.session.connect` |
| `2026-06-28 11:54:57` | `cowrie.client.version` |
| `2026-06-28 11:54:57` | `cowrie.client.kex` |
| `2026-06-28 11:55:03` | `cowrie.login.success` |
| `2026-06-28 11:55:06` | `cowrie.session.params` |
| `2026-06-28 11:55:06` | `cowrie.command.input` |
| `2026-06-28 11:55:07` | `cowrie.log.closed` |
| `2026-06-28 11:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb955aaea207

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:55 |
| **Last Seen** | 2026-06-28 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:55:21` | `cowrie.session.connect` |
| `2026-06-28 11:55:21` | `cowrie.client.version` |
| `2026-06-28 11:55:21` | `cowrie.client.kex` |
| `2026-06-28 11:55:21` | `cowrie.login.success` |
| `2026-06-28 11:55:22` | `cowrie.session.params` |
| `2026-06-28 11:55:22` | `cowrie.command.input` |
| `2026-06-28 11:55:22` | `cowrie.log.closed` |
| `2026-06-28 11:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf612fcd3c4b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:56 |
| **Last Seen** | 2026-06-28 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:56:28` | `cowrie.session.connect` |
| `2026-06-28 11:56:28` | `cowrie.client.version` |
| `2026-06-28 11:56:28` | `cowrie.client.kex` |
| `2026-06-28 11:56:28` | `cowrie.login.success` |
| `2026-06-28 11:56:29` | `cowrie.session.params` |
| `2026-06-28 11:56:29` | `cowrie.command.input` |
| `2026-06-28 11:56:29` | `cowrie.log.closed` |
| `2026-06-28 11:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f9472354620

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-28 11:56 |
| **Last Seen** | 2026-06-28 11:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:56:44` | `cowrie.session.connect` |
| `2026-06-28 11:56:45` | `cowrie.client.version` |
| `2026-06-28 11:56:45` | `cowrie.client.kex` |
| `2026-06-28 11:56:46` | `cowrie.login.success` |
| `2026-06-28 11:56:47` | `cowrie.session.params` |
| `2026-06-28 11:56:47` | `cowrie.command.input` |
| `2026-06-28 11:56:47` | `cowrie.log.closed` |
| `2026-06-28 11:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b610c6f7351

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:57 |
| **Last Seen** | 2026-06-28 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:57:33` | `cowrie.session.connect` |
| `2026-06-28 11:57:33` | `cowrie.client.version` |
| `2026-06-28 11:57:33` | `cowrie.client.kex` |
| `2026-06-28 11:57:33` | `cowrie.login.success` |
| `2026-06-28 11:57:34` | `cowrie.session.params` |
| `2026-06-28 11:57:34` | `cowrie.command.input` |
| `2026-06-28 11:57:34` | `cowrie.log.closed` |
| `2026-06-28 11:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30005b578bdc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:58 |
| **Last Seen** | 2026-06-28 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:58:38` | `cowrie.session.connect` |
| `2026-06-28 11:58:38` | `cowrie.client.version` |
| `2026-06-28 11:58:38` | `cowrie.client.kex` |
| `2026-06-28 11:58:38` | `cowrie.login.success` |
| `2026-06-28 11:58:39` | `cowrie.session.params` |
| `2026-06-28 11:58:39` | `cowrie.command.input` |
| `2026-06-28 11:58:39` | `cowrie.log.closed` |
| `2026-06-28 11:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbfd3bda70b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 11:59 |
| **Last Seen** | 2026-06-28 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 11:59:44` | `cowrie.session.connect` |
| `2026-06-28 11:59:44` | `cowrie.client.version` |
| `2026-06-28 11:59:45` | `cowrie.client.kex` |
| `2026-06-28 11:59:45` | `cowrie.login.success` |
| `2026-06-28 11:59:46` | `cowrie.session.params` |
| `2026-06-28 11:59:46` | `cowrie.command.input` |
| `2026-06-28 11:59:46` | `cowrie.log.closed` |
| `2026-06-28 11:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4885bb4caaf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:00 |
| **Last Seen** | 2026-06-28 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:00:40` | `cowrie.session.connect` |
| `2026-06-28 12:00:40` | `cowrie.client.version` |
| `2026-06-28 12:00:40` | `cowrie.client.kex` |
| `2026-06-28 12:00:40` | `cowrie.login.success` |
| `2026-06-28 12:00:41` | `cowrie.session.params` |
| `2026-06-28 12:00:41` | `cowrie.command.input` |
| `2026-06-28 12:00:41` | `cowrie.log.closed` |
| `2026-06-28 12:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-302e07374783

| Field | Detail |
|---|---|
| **Source IP** | `159.65.91[.]36` |
| **First Seen** | 2026-06-28 12:00 |
| **Last Seen** | 2026-06-28 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:00:54` | `cowrie.session.connect` |
| `2026-06-28 12:00:54` | `cowrie.client.version` |
| `2026-06-28 12:00:54` | `cowrie.client.kex` |
| `2026-06-28 12:00:55` | `cowrie.login.success` |
| `2026-06-28 12:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.91[.]36` to AbuseIPDB if not already reported
- [ ] Block `159.65.91[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-959836890e8a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-28 12:00 |
| **Last Seen** | 2026-06-28 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:00:55` | `cowrie.session.connect` |
| `2026-06-28 12:00:55` | `cowrie.client.version` |
| `2026-06-28 12:00:55` | `cowrie.client.kex` |
| `2026-06-28 12:00:55` | `cowrie.login.success` |
| `2026-06-28 12:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d17ad47a576

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:01 |
| **Last Seen** | 2026-06-28 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:01:25` | `cowrie.session.connect` |
| `2026-06-28 12:01:25` | `cowrie.client.version` |
| `2026-06-28 12:01:25` | `cowrie.client.kex` |
| `2026-06-28 12:01:26` | `cowrie.login.success` |
| `2026-06-28 12:01:27` | `cowrie.session.params` |
| `2026-06-28 12:01:27` | `cowrie.command.input` |
| `2026-06-28 12:01:27` | `cowrie.log.closed` |
| `2026-06-28 12:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40042fdf31fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:02 |
| **Last Seen** | 2026-06-28 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:02:10` | `cowrie.session.connect` |
| `2026-06-28 12:02:10` | `cowrie.client.version` |
| `2026-06-28 12:02:10` | `cowrie.client.kex` |
| `2026-06-28 12:02:10` | `cowrie.login.success` |
| `2026-06-28 12:02:11` | `cowrie.session.params` |
| `2026-06-28 12:02:11` | `cowrie.command.input` |
| `2026-06-28 12:02:11` | `cowrie.log.closed` |
| `2026-06-28 12:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b9c0817d84

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:02 |
| **Last Seen** | 2026-06-28 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:02:55` | `cowrie.session.connect` |
| `2026-06-28 12:02:55` | `cowrie.client.version` |
| `2026-06-28 12:02:55` | `cowrie.client.kex` |
| `2026-06-28 12:02:56` | `cowrie.login.success` |
| `2026-06-28 12:02:56` | `cowrie.session.params` |
| `2026-06-28 12:02:56` | `cowrie.command.input` |
| `2026-06-28 12:02:56` | `cowrie.log.closed` |
| `2026-06-28 12:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec58205de0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:03 |
| **Last Seen** | 2026-06-28 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:03:41` | `cowrie.session.connect` |
| `2026-06-28 12:03:41` | `cowrie.client.version` |
| `2026-06-28 12:03:41` | `cowrie.client.kex` |
| `2026-06-28 12:03:41` | `cowrie.login.success` |
| `2026-06-28 12:03:42` | `cowrie.session.params` |
| `2026-06-28 12:03:42` | `cowrie.command.input` |
| `2026-06-28 12:03:42` | `cowrie.log.closed` |
| `2026-06-28 12:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81cf35c74bf

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 12:03 |
| **Last Seen** | 2026-06-28 12:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:03:54` | `cowrie.session.connect` |
| `2026-06-28 12:03:54` | `cowrie.client.version` |
| `2026-06-28 12:03:54` | `cowrie.client.kex` |
| `2026-06-28 12:03:56` | `cowrie.login.success` |
| `2026-06-28 12:03:57` | `cowrie.session.params` |
| `2026-06-28 12:03:57` | `cowrie.command.input` |
| `2026-06-28 12:03:57` | `cowrie.log.closed` |
| `2026-06-28 12:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a2c65f5c55

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:04 |
| **Last Seen** | 2026-06-28 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:04:26` | `cowrie.session.connect` |
| `2026-06-28 12:04:26` | `cowrie.client.version` |
| `2026-06-28 12:04:27` | `cowrie.client.kex` |
| `2026-06-28 12:04:27` | `cowrie.login.success` |
| `2026-06-28 12:04:28` | `cowrie.session.params` |
| `2026-06-28 12:04:28` | `cowrie.command.input` |
| `2026-06-28 12:04:28` | `cowrie.log.closed` |
| `2026-06-28 12:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530834ff9fa1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:05 |
| **Last Seen** | 2026-06-28 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:05:13` | `cowrie.session.connect` |
| `2026-06-28 12:05:13` | `cowrie.client.version` |
| `2026-06-28 12:05:13` | `cowrie.client.kex` |
| `2026-06-28 12:05:13` | `cowrie.login.success` |
| `2026-06-28 12:05:14` | `cowrie.session.params` |
| `2026-06-28 12:05:14` | `cowrie.command.input` |
| `2026-06-28 12:05:14` | `cowrie.log.closed` |
| `2026-06-28 12:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46cc2e012f96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:06 |
| **Last Seen** | 2026-06-28 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:06:01` | `cowrie.session.connect` |
| `2026-06-28 12:06:01` | `cowrie.client.version` |
| `2026-06-28 12:06:01` | `cowrie.client.kex` |
| `2026-06-28 12:06:01` | `cowrie.login.success` |
| `2026-06-28 12:06:02` | `cowrie.session.params` |
| `2026-06-28 12:06:02` | `cowrie.command.input` |
| `2026-06-28 12:06:02` | `cowrie.log.closed` |
| `2026-06-28 12:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd66efb4d6e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 12:06 |
| **Last Seen** | 2026-06-28 12:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:06:01` | `cowrie.session.connect` |
| `2026-06-28 12:06:03` | `cowrie.client.version` |
| `2026-06-28 12:06:03` | `cowrie.client.kex` |
| `2026-06-28 12:06:09` | `cowrie.login.success` |
| `2026-06-28 12:06:13` | `cowrie.session.params` |
| `2026-06-28 12:06:13` | `cowrie.command.input` |
| `2026-06-28 12:06:14` | `cowrie.log.closed` |
| `2026-06-28 12:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3f9131e803

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:06 |
| **Last Seen** | 2026-06-28 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:06:49` | `cowrie.session.connect` |
| `2026-06-28 12:06:49` | `cowrie.client.version` |
| `2026-06-28 12:06:49` | `cowrie.client.kex` |
| `2026-06-28 12:06:50` | `cowrie.login.success` |
| `2026-06-28 12:06:50` | `cowrie.session.params` |
| `2026-06-28 12:06:50` | `cowrie.command.input` |
| `2026-06-28 12:06:51` | `cowrie.log.closed` |
| `2026-06-28 12:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334fc9723577

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-28 12:07 |
| **Last Seen** | 2026-06-28 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:07:35` | `cowrie.session.connect` |
| `2026-06-28 12:07:35` | `cowrie.client.version` |
| `2026-06-28 12:07:35` | `cowrie.client.kex` |
| `2026-06-28 12:07:36` | `cowrie.login.success` |
| `2026-06-28 12:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0c6a985ef8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-28 12:07 |
| **Last Seen** | 2026-06-28 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:07:35` | `cowrie.session.connect` |
| `2026-06-28 12:07:35` | `cowrie.client.version` |
| `2026-06-28 12:07:35` | `cowrie.client.kex` |
| `2026-06-28 12:07:36` | `cowrie.login.success` |
| `2026-06-28 12:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad2830f07fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:07 |
| **Last Seen** | 2026-06-28 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:07:38` | `cowrie.session.connect` |
| `2026-06-28 12:07:38` | `cowrie.client.version` |
| `2026-06-28 12:07:38` | `cowrie.client.kex` |
| `2026-06-28 12:07:39` | `cowrie.login.success` |
| `2026-06-28 12:07:39` | `cowrie.session.params` |
| `2026-06-28 12:07:39` | `cowrie.command.input` |
| `2026-06-28 12:07:39` | `cowrie.log.closed` |
| `2026-06-28 12:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1c7e6c28a91

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:08 |
| **Last Seen** | 2026-06-28 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:08:28` | `cowrie.session.connect` |
| `2026-06-28 12:08:28` | `cowrie.client.version` |
| `2026-06-28 12:08:28` | `cowrie.client.kex` |
| `2026-06-28 12:08:28` | `cowrie.login.success` |
| `2026-06-28 12:08:29` | `cowrie.session.params` |
| `2026-06-28 12:08:29` | `cowrie.command.input` |
| `2026-06-28 12:08:29` | `cowrie.log.closed` |
| `2026-06-28 12:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720f3cd00869

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:09 |
| **Last Seen** | 2026-06-28 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:09:16` | `cowrie.session.connect` |
| `2026-06-28 12:09:16` | `cowrie.client.version` |
| `2026-06-28 12:09:16` | `cowrie.client.kex` |
| `2026-06-28 12:09:16` | `cowrie.login.success` |
| `2026-06-28 12:09:17` | `cowrie.session.params` |
| `2026-06-28 12:09:17` | `cowrie.command.input` |
| `2026-06-28 12:09:17` | `cowrie.log.closed` |
| `2026-06-28 12:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f002bc4f066

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:10 |
| **Last Seen** | 2026-06-28 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:10:03` | `cowrie.session.connect` |
| `2026-06-28 12:10:03` | `cowrie.client.version` |
| `2026-06-28 12:10:03` | `cowrie.client.kex` |
| `2026-06-28 12:10:04` | `cowrie.login.success` |
| `2026-06-28 12:10:04` | `cowrie.session.params` |
| `2026-06-28 12:10:04` | `cowrie.command.input` |
| `2026-06-28 12:10:05` | `cowrie.log.closed` |
| `2026-06-28 12:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ddc03b8acc9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:10 |
| **Last Seen** | 2026-06-28 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:10:50` | `cowrie.session.connect` |
| `2026-06-28 12:10:50` | `cowrie.client.version` |
| `2026-06-28 12:10:50` | `cowrie.client.kex` |
| `2026-06-28 12:10:50` | `cowrie.login.success` |
| `2026-06-28 12:10:51` | `cowrie.session.params` |
| `2026-06-28 12:10:51` | `cowrie.command.input` |
| `2026-06-28 12:10:51` | `cowrie.log.closed` |
| `2026-06-28 12:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77009c2a77c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:11 |
| **Last Seen** | 2026-06-28 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:11:37` | `cowrie.session.connect` |
| `2026-06-28 12:11:37` | `cowrie.client.version` |
| `2026-06-28 12:11:38` | `cowrie.client.kex` |
| `2026-06-28 12:11:38` | `cowrie.login.success` |
| `2026-06-28 12:11:39` | `cowrie.session.params` |
| `2026-06-28 12:11:39` | `cowrie.command.input` |
| `2026-06-28 12:11:39` | `cowrie.log.closed` |
| `2026-06-28 12:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d956de118da

| Field | Detail |
|---|---|
| **Source IP** | `45.142.154[.]108` |
| **First Seen** | 2026-06-28 12:11 |
| **Last Seen** | 2026-06-28 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:11:39` | `cowrie.session.connect` |
| `2026-06-28 12:11:39` | `cowrie.login.success` |
| `2026-06-28 12:11:40` | `cowrie.session.params` |
| `2026-06-28 12:11:40` | `cowrie.command.input` |
| `2026-06-28 12:11:40` | `cowrie.command.failed` |
| `2026-06-28 12:11:40` | `cowrie.command.input` |
| `2026-06-28 12:11:40` | `cowrie.log.closed` |
| `2026-06-28 12:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.154[.]108` to AbuseIPDB if not already reported
- [ ] Block `45.142.154[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5823a6176a27

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-28 12:11 |
| **Last Seen** | 2026-06-28 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:11:47` | `cowrie.session.connect` |
| `2026-06-28 12:11:47` | `cowrie.client.version` |
| `2026-06-28 12:11:47` | `cowrie.client.kex` |
| `2026-06-28 12:11:47` | `cowrie.login.success` |
| `2026-06-28 12:11:48` | `cowrie.session.params` |
| `2026-06-28 12:11:48` | `cowrie.command.input` |
| `2026-06-28 12:11:48` | `cowrie.log.closed` |
| `2026-06-28 12:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e040944038

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-28 12:12 |
| **Last Seen** | 2026-06-28 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:12:23` | `cowrie.session.connect` |
| `2026-06-28 12:12:23` | `cowrie.client.version` |
| `2026-06-28 12:12:23` | `cowrie.client.kex` |
| `2026-06-28 12:12:24` | `cowrie.login.success` |
| `2026-06-28 12:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b62cedfc4f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-28 12:12 |
| **Last Seen** | 2026-06-28 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:12:24` | `cowrie.session.connect` |
| `2026-06-28 12:12:24` | `cowrie.client.version` |
| `2026-06-28 12:12:24` | `cowrie.client.kex` |
| `2026-06-28 12:12:24` | `cowrie.login.success` |
| `2026-06-28 12:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d2839d1ad3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-28 12:12 |
| **Last Seen** | 2026-06-28 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:12:25` | `cowrie.session.connect` |
| `2026-06-28 12:12:25` | `cowrie.client.version` |
| `2026-06-28 12:12:25` | `cowrie.client.kex` |
| `2026-06-28 12:12:26` | `cowrie.login.success` |
| `2026-06-28 12:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d078014ebfb2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-28 12:12 |
| **Last Seen** | 2026-06-28 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:12:26` | `cowrie.session.connect` |
| `2026-06-28 12:12:26` | `cowrie.client.version` |
| `2026-06-28 12:12:26` | `cowrie.client.kex` |
| `2026-06-28 12:12:26` | `cowrie.login.success` |
| `2026-06-28 12:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11123a843be3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:12 |
| **Last Seen** | 2026-06-28 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:12:27` | `cowrie.session.connect` |
| `2026-06-28 12:12:27` | `cowrie.client.version` |
| `2026-06-28 12:12:27` | `cowrie.client.kex` |
| `2026-06-28 12:12:27` | `cowrie.login.success` |
| `2026-06-28 12:12:28` | `cowrie.session.params` |
| `2026-06-28 12:12:28` | `cowrie.command.input` |
| `2026-06-28 12:12:28` | `cowrie.log.closed` |
| `2026-06-28 12:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490a85be7f80

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:13 |
| **Last Seen** | 2026-06-28 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:13:15` | `cowrie.session.connect` |
| `2026-06-28 12:13:15` | `cowrie.client.version` |
| `2026-06-28 12:13:16` | `cowrie.client.kex` |
| `2026-06-28 12:13:16` | `cowrie.login.success` |
| `2026-06-28 12:13:17` | `cowrie.session.params` |
| `2026-06-28 12:13:17` | `cowrie.command.input` |
| `2026-06-28 12:13:17` | `cowrie.log.closed` |
| `2026-06-28 12:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0aeb09b124

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:14 |
| **Last Seen** | 2026-06-28 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:14:05` | `cowrie.session.connect` |
| `2026-06-28 12:14:05` | `cowrie.client.version` |
| `2026-06-28 12:14:05` | `cowrie.client.kex` |
| `2026-06-28 12:14:05` | `cowrie.login.success` |
| `2026-06-28 12:14:06` | `cowrie.session.params` |
| `2026-06-28 12:14:06` | `cowrie.command.input` |
| `2026-06-28 12:14:06` | `cowrie.log.closed` |
| `2026-06-28 12:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e099a48d581

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:14 |
| **Last Seen** | 2026-06-28 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:14:56` | `cowrie.session.connect` |
| `2026-06-28 12:14:56` | `cowrie.client.version` |
| `2026-06-28 12:14:56` | `cowrie.client.kex` |
| `2026-06-28 12:14:57` | `cowrie.login.success` |
| `2026-06-28 12:14:57` | `cowrie.session.params` |
| `2026-06-28 12:14:57` | `cowrie.command.input` |
| `2026-06-28 12:14:57` | `cowrie.log.closed` |
| `2026-06-28 12:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f94d2831150

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:15 |
| **Last Seen** | 2026-06-28 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:15:47` | `cowrie.session.connect` |
| `2026-06-28 12:15:47` | `cowrie.client.version` |
| `2026-06-28 12:15:47` | `cowrie.client.kex` |
| `2026-06-28 12:15:47` | `cowrie.login.success` |
| `2026-06-28 12:15:48` | `cowrie.session.params` |
| `2026-06-28 12:15:48` | `cowrie.command.input` |
| `2026-06-28 12:15:48` | `cowrie.log.closed` |
| `2026-06-28 12:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-136dc18e1aae

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-28 12:16 |
| **Last Seen** | 2026-06-28 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:16:30` | `cowrie.session.connect` |
| `2026-06-28 12:16:30` | `cowrie.client.version` |
| `2026-06-28 12:16:31` | `cowrie.client.kex` |
| `2026-06-28 12:16:31` | `cowrie.login.success` |
| `2026-06-28 12:16:32` | `cowrie.session.params` |
| `2026-06-28 12:16:32` | `cowrie.command.input` |
| `2026-06-28 12:16:32` | `cowrie.log.closed` |
| `2026-06-28 12:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d0fb862ef5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:16 |
| **Last Seen** | 2026-06-28 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:16:36` | `cowrie.session.connect` |
| `2026-06-28 12:16:36` | `cowrie.client.version` |
| `2026-06-28 12:16:36` | `cowrie.client.kex` |
| `2026-06-28 12:16:36` | `cowrie.login.success` |
| `2026-06-28 12:16:37` | `cowrie.session.params` |
| `2026-06-28 12:16:37` | `cowrie.command.input` |
| `2026-06-28 12:16:37` | `cowrie.log.closed` |
| `2026-06-28 12:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88166857b96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:17 |
| **Last Seen** | 2026-06-28 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:17:24` | `cowrie.session.connect` |
| `2026-06-28 12:17:24` | `cowrie.client.version` |
| `2026-06-28 12:17:24` | `cowrie.client.kex` |
| `2026-06-28 12:17:24` | `cowrie.login.success` |
| `2026-06-28 12:17:25` | `cowrie.session.params` |
| `2026-06-28 12:17:25` | `cowrie.command.input` |
| `2026-06-28 12:17:25` | `cowrie.log.closed` |
| `2026-06-28 12:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3a23d1ab53

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 12:17 |
| **Last Seen** | 2026-06-28 12:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:17:33` | `cowrie.session.connect` |
| `2026-06-28 12:17:34` | `cowrie.client.version` |
| `2026-06-28 12:17:34` | `cowrie.client.kex` |
| `2026-06-28 12:17:40` | `cowrie.login.success` |
| `2026-06-28 12:17:43` | `cowrie.session.params` |
| `2026-06-28 12:17:43` | `cowrie.command.input` |
| `2026-06-28 12:17:45` | `cowrie.log.closed` |
| `2026-06-28 12:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee2f74244f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:18 |
| **Last Seen** | 2026-06-28 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:18:13` | `cowrie.session.connect` |
| `2026-06-28 12:18:13` | `cowrie.client.version` |
| `2026-06-28 12:18:13` | `cowrie.client.kex` |
| `2026-06-28 12:18:13` | `cowrie.login.success` |
| `2026-06-28 12:18:14` | `cowrie.session.params` |
| `2026-06-28 12:18:14` | `cowrie.command.input` |
| `2026-06-28 12:18:14` | `cowrie.log.closed` |
| `2026-06-28 12:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b2f0a97d6ea

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 12:18 |
| **Last Seen** | 2026-06-28 12:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:18:33` | `cowrie.session.connect` |
| `2026-06-28 12:18:33` | `cowrie.client.version` |
| `2026-06-28 12:18:33` | `cowrie.client.kex` |
| `2026-06-28 12:18:35` | `cowrie.login.success` |
| `2026-06-28 12:18:36` | `cowrie.session.params` |
| `2026-06-28 12:18:36` | `cowrie.command.input` |
| `2026-06-28 12:18:38` | `cowrie.log.closed` |
| `2026-06-28 12:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc826391f18

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:19 |
| **Last Seen** | 2026-06-28 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:19:02` | `cowrie.session.connect` |
| `2026-06-28 12:19:02` | `cowrie.client.version` |
| `2026-06-28 12:19:02` | `cowrie.client.kex` |
| `2026-06-28 12:19:03` | `cowrie.login.success` |
| `2026-06-28 12:19:04` | `cowrie.session.params` |
| `2026-06-28 12:19:04` | `cowrie.command.input` |
| `2026-06-28 12:19:04` | `cowrie.log.closed` |
| `2026-06-28 12:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52da2b481eb4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:19 |
| **Last Seen** | 2026-06-28 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:19:53` | `cowrie.session.connect` |
| `2026-06-28 12:19:53` | `cowrie.client.version` |
| `2026-06-28 12:19:53` | `cowrie.client.kex` |
| `2026-06-28 12:19:53` | `cowrie.login.success` |
| `2026-06-28 12:19:54` | `cowrie.session.params` |
| `2026-06-28 12:19:54` | `cowrie.command.input` |
| `2026-06-28 12:19:54` | `cowrie.log.closed` |
| `2026-06-28 12:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba3340a7e72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:20 |
| **Last Seen** | 2026-06-28 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:20:44` | `cowrie.session.connect` |
| `2026-06-28 12:20:44` | `cowrie.client.version` |
| `2026-06-28 12:20:44` | `cowrie.client.kex` |
| `2026-06-28 12:20:44` | `cowrie.login.success` |
| `2026-06-28 12:20:45` | `cowrie.session.params` |
| `2026-06-28 12:20:45` | `cowrie.command.input` |
| `2026-06-28 12:20:45` | `cowrie.log.closed` |
| `2026-06-28 12:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3178856a2b17

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:21 |
| **Last Seen** | 2026-06-28 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:21:35` | `cowrie.session.connect` |
| `2026-06-28 12:21:35` | `cowrie.client.version` |
| `2026-06-28 12:21:35` | `cowrie.client.kex` |
| `2026-06-28 12:21:35` | `cowrie.login.success` |
| `2026-06-28 12:21:36` | `cowrie.session.params` |
| `2026-06-28 12:21:36` | `cowrie.command.input` |
| `2026-06-28 12:21:36` | `cowrie.log.closed` |
| `2026-06-28 12:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917c947075ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:22 |
| **Last Seen** | 2026-06-28 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:22:24` | `cowrie.session.connect` |
| `2026-06-28 12:22:24` | `cowrie.client.version` |
| `2026-06-28 12:22:24` | `cowrie.client.kex` |
| `2026-06-28 12:22:25` | `cowrie.login.success` |
| `2026-06-28 12:22:25` | `cowrie.session.params` |
| `2026-06-28 12:22:25` | `cowrie.command.input` |
| `2026-06-28 12:22:26` | `cowrie.log.closed` |
| `2026-06-28 12:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd48a16d3728

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:23 |
| **Last Seen** | 2026-06-28 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:23:13` | `cowrie.session.connect` |
| `2026-06-28 12:23:13` | `cowrie.client.version` |
| `2026-06-28 12:23:14` | `cowrie.client.kex` |
| `2026-06-28 12:23:14` | `cowrie.login.success` |
| `2026-06-28 12:23:15` | `cowrie.session.params` |
| `2026-06-28 12:23:15` | `cowrie.command.input` |
| `2026-06-28 12:23:15` | `cowrie.log.closed` |
| `2026-06-28 12:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef24a6ba583b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:24 |
| **Last Seen** | 2026-06-28 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:24:04` | `cowrie.session.connect` |
| `2026-06-28 12:24:04` | `cowrie.client.version` |
| `2026-06-28 12:24:04` | `cowrie.client.kex` |
| `2026-06-28 12:24:04` | `cowrie.login.success` |
| `2026-06-28 12:24:05` | `cowrie.session.params` |
| `2026-06-28 12:24:05` | `cowrie.command.input` |
| `2026-06-28 12:24:05` | `cowrie.log.closed` |
| `2026-06-28 12:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa561a2558d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:24 |
| **Last Seen** | 2026-06-28 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:24:54` | `cowrie.session.connect` |
| `2026-06-28 12:24:54` | `cowrie.client.version` |
| `2026-06-28 12:24:54` | `cowrie.client.kex` |
| `2026-06-28 12:24:55` | `cowrie.login.success` |
| `2026-06-28 12:24:55` | `cowrie.session.params` |
| `2026-06-28 12:24:55` | `cowrie.command.input` |
| `2026-06-28 12:24:55` | `cowrie.log.closed` |
| `2026-06-28 12:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-322de85a1834

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:25 |
| **Last Seen** | 2026-06-28 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:25:46` | `cowrie.session.connect` |
| `2026-06-28 12:25:46` | `cowrie.client.version` |
| `2026-06-28 12:25:46` | `cowrie.client.kex` |
| `2026-06-28 12:25:47` | `cowrie.login.success` |
| `2026-06-28 12:25:48` | `cowrie.session.params` |
| `2026-06-28 12:25:48` | `cowrie.command.input` |
| `2026-06-28 12:25:48` | `cowrie.log.closed` |
| `2026-06-28 12:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-203162d5bedd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:26 |
| **Last Seen** | 2026-06-28 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:26:39` | `cowrie.session.connect` |
| `2026-06-28 12:26:39` | `cowrie.client.version` |
| `2026-06-28 12:26:39` | `cowrie.client.kex` |
| `2026-06-28 12:26:40` | `cowrie.login.success` |
| `2026-06-28 12:26:41` | `cowrie.session.params` |
| `2026-06-28 12:26:41` | `cowrie.command.input` |
| `2026-06-28 12:26:41` | `cowrie.log.closed` |
| `2026-06-28 12:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ea3f7e8522

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:27 |
| **Last Seen** | 2026-06-28 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:27:32` | `cowrie.session.connect` |
| `2026-06-28 12:27:32` | `cowrie.client.version` |
| `2026-06-28 12:27:33` | `cowrie.client.kex` |
| `2026-06-28 12:27:33` | `cowrie.login.success` |
| `2026-06-28 12:27:34` | `cowrie.session.params` |
| `2026-06-28 12:27:34` | `cowrie.command.input` |
| `2026-06-28 12:27:34` | `cowrie.log.closed` |
| `2026-06-28 12:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9cfdd795cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:28 |
| **Last Seen** | 2026-06-28 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:28:24` | `cowrie.session.connect` |
| `2026-06-28 12:28:24` | `cowrie.client.version` |
| `2026-06-28 12:28:24` | `cowrie.client.kex` |
| `2026-06-28 12:28:24` | `cowrie.login.success` |
| `2026-06-28 12:28:25` | `cowrie.session.params` |
| `2026-06-28 12:28:25` | `cowrie.command.input` |
| `2026-06-28 12:28:25` | `cowrie.log.closed` |
| `2026-06-28 12:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dcef5629882

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 12:28 |
| **Last Seen** | 2026-06-28 12:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:28:58` | `cowrie.session.connect` |
| `2026-06-28 12:28:59` | `cowrie.client.version` |
| `2026-06-28 12:28:59` | `cowrie.client.kex` |
| `2026-06-28 12:29:05` | `cowrie.login.success` |
| `2026-06-28 12:29:08` | `cowrie.session.params` |
| `2026-06-28 12:29:08` | `cowrie.command.input` |
| `2026-06-28 12:29:11` | `cowrie.log.closed` |
| `2026-06-28 12:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409886204d80

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:29 |
| **Last Seen** | 2026-06-28 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:29:16` | `cowrie.session.connect` |
| `2026-06-28 12:29:16` | `cowrie.client.version` |
| `2026-06-28 12:29:16` | `cowrie.client.kex` |
| `2026-06-28 12:29:17` | `cowrie.login.success` |
| `2026-06-28 12:29:17` | `cowrie.session.params` |
| `2026-06-28 12:29:17` | `cowrie.command.input` |
| `2026-06-28 12:29:18` | `cowrie.log.closed` |
| `2026-06-28 12:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-840b5d46f576

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:30 |
| **Last Seen** | 2026-06-28 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:30:09` | `cowrie.session.connect` |
| `2026-06-28 12:30:09` | `cowrie.client.version` |
| `2026-06-28 12:30:09` | `cowrie.client.kex` |
| `2026-06-28 12:30:09` | `cowrie.login.success` |
| `2026-06-28 12:30:10` | `cowrie.session.params` |
| `2026-06-28 12:30:10` | `cowrie.command.input` |
| `2026-06-28 12:30:10` | `cowrie.log.closed` |
| `2026-06-28 12:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d75e0a21d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:31 |
| **Last Seen** | 2026-06-28 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:31:04` | `cowrie.session.connect` |
| `2026-06-28 12:31:04` | `cowrie.client.version` |
| `2026-06-28 12:31:04` | `cowrie.client.kex` |
| `2026-06-28 12:31:04` | `cowrie.login.success` |
| `2026-06-28 12:31:05` | `cowrie.session.params` |
| `2026-06-28 12:31:05` | `cowrie.command.input` |
| `2026-06-28 12:31:05` | `cowrie.log.closed` |
| `2026-06-28 12:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e7585a36f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:32 |
| **Last Seen** | 2026-06-28 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:32:00` | `cowrie.session.connect` |
| `2026-06-28 12:32:00` | `cowrie.client.version` |
| `2026-06-28 12:32:00` | `cowrie.client.kex` |
| `2026-06-28 12:32:00` | `cowrie.login.success` |
| `2026-06-28 12:32:01` | `cowrie.session.params` |
| `2026-06-28 12:32:01` | `cowrie.command.input` |
| `2026-06-28 12:32:01` | `cowrie.log.closed` |
| `2026-06-28 12:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff5de7f4965e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:32 |
| **Last Seen** | 2026-06-28 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:32:56` | `cowrie.session.connect` |
| `2026-06-28 12:32:56` | `cowrie.client.version` |
| `2026-06-28 12:32:56` | `cowrie.client.kex` |
| `2026-06-28 12:32:56` | `cowrie.login.success` |
| `2026-06-28 12:32:57` | `cowrie.session.params` |
| `2026-06-28 12:32:57` | `cowrie.command.input` |
| `2026-06-28 12:32:57` | `cowrie.log.closed` |
| `2026-06-28 12:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f03e3ab17a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 12:33 |
| **Last Seen** | 2026-06-28 12:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:33:01` | `cowrie.session.connect` |
| `2026-06-28 12:33:01` | `cowrie.client.version` |
| `2026-06-28 12:33:01` | `cowrie.client.kex` |
| `2026-06-28 12:33:03` | `cowrie.login.success` |
| `2026-06-28 12:33:05` | `cowrie.session.params` |
| `2026-06-28 12:33:05` | `cowrie.command.input` |
| `2026-06-28 12:33:05` | `cowrie.log.closed` |
| `2026-06-28 12:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad4b7bf330e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:33 |
| **Last Seen** | 2026-06-28 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:33:50` | `cowrie.session.connect` |
| `2026-06-28 12:33:50` | `cowrie.client.version` |
| `2026-06-28 12:33:50` | `cowrie.client.kex` |
| `2026-06-28 12:33:50` | `cowrie.login.success` |
| `2026-06-28 12:33:51` | `cowrie.session.params` |
| `2026-06-28 12:33:51` | `cowrie.command.input` |
| `2026-06-28 12:33:51` | `cowrie.log.closed` |
| `2026-06-28 12:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35236205b88d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:34 |
| **Last Seen** | 2026-06-28 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:34:43` | `cowrie.session.connect` |
| `2026-06-28 12:34:43` | `cowrie.client.version` |
| `2026-06-28 12:34:43` | `cowrie.client.kex` |
| `2026-06-28 12:34:43` | `cowrie.login.success` |
| `2026-06-28 12:34:44` | `cowrie.session.params` |
| `2026-06-28 12:34:44` | `cowrie.command.input` |
| `2026-06-28 12:34:44` | `cowrie.log.closed` |
| `2026-06-28 12:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8297c461d3b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:35 |
| **Last Seen** | 2026-06-28 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:35:34` | `cowrie.session.connect` |
| `2026-06-28 12:35:34` | `cowrie.client.version` |
| `2026-06-28 12:35:34` | `cowrie.client.kex` |
| `2026-06-28 12:35:34` | `cowrie.login.success` |
| `2026-06-28 12:35:35` | `cowrie.session.params` |
| `2026-06-28 12:35:35` | `cowrie.command.input` |
| `2026-06-28 12:35:35` | `cowrie.log.closed` |
| `2026-06-28 12:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e248133a56af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:36 |
| **Last Seen** | 2026-06-28 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:36:25` | `cowrie.session.connect` |
| `2026-06-28 12:36:25` | `cowrie.client.version` |
| `2026-06-28 12:36:25` | `cowrie.client.kex` |
| `2026-06-28 12:36:25` | `cowrie.login.success` |
| `2026-06-28 12:36:26` | `cowrie.session.params` |
| `2026-06-28 12:36:26` | `cowrie.command.input` |
| `2026-06-28 12:36:26` | `cowrie.log.closed` |
| `2026-06-28 12:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8989f6ccf00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:37 |
| **Last Seen** | 2026-06-28 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:37:30` | `cowrie.session.connect` |
| `2026-06-28 12:37:30` | `cowrie.client.version` |
| `2026-06-28 12:37:30` | `cowrie.client.kex` |
| `2026-06-28 12:37:30` | `cowrie.login.success` |
| `2026-06-28 12:37:31` | `cowrie.session.params` |
| `2026-06-28 12:37:31` | `cowrie.command.input` |
| `2026-06-28 12:37:31` | `cowrie.log.closed` |
| `2026-06-28 12:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62db287006e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:38 |
| **Last Seen** | 2026-06-28 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:38:23` | `cowrie.session.connect` |
| `2026-06-28 12:38:23` | `cowrie.client.version` |
| `2026-06-28 12:38:23` | `cowrie.client.kex` |
| `2026-06-28 12:38:24` | `cowrie.login.success` |
| `2026-06-28 12:38:25` | `cowrie.session.params` |
| `2026-06-28 12:38:25` | `cowrie.command.input` |
| `2026-06-28 12:38:25` | `cowrie.log.closed` |
| `2026-06-28 12:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90511c30f29e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:39 |
| **Last Seen** | 2026-06-28 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:39:17` | `cowrie.session.connect` |
| `2026-06-28 12:39:17` | `cowrie.client.version` |
| `2026-06-28 12:39:17` | `cowrie.client.kex` |
| `2026-06-28 12:39:17` | `cowrie.login.success` |
| `2026-06-28 12:39:18` | `cowrie.session.params` |
| `2026-06-28 12:39:18` | `cowrie.command.input` |
| `2026-06-28 12:39:18` | `cowrie.log.closed` |
| `2026-06-28 12:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3fa04fcb06

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:40 |
| **Last Seen** | 2026-06-28 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:40:15` | `cowrie.session.connect` |
| `2026-06-28 12:40:15` | `cowrie.client.version` |
| `2026-06-28 12:40:15` | `cowrie.client.kex` |
| `2026-06-28 12:40:15` | `cowrie.login.success` |
| `2026-06-28 12:40:16` | `cowrie.session.params` |
| `2026-06-28 12:40:16` | `cowrie.command.input` |
| `2026-06-28 12:40:16` | `cowrie.log.closed` |
| `2026-06-28 12:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64fe2ef7a617

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 12:40 |
| **Last Seen** | 2026-06-28 12:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:40:25` | `cowrie.session.connect` |
| `2026-06-28 12:40:26` | `cowrie.client.version` |
| `2026-06-28 12:40:26` | `cowrie.client.kex` |
| `2026-06-28 12:40:32` | `cowrie.login.success` |
| `2026-06-28 12:40:35` | `cowrie.session.params` |
| `2026-06-28 12:40:35` | `cowrie.command.input` |
| `2026-06-28 12:40:37` | `cowrie.log.closed` |
| `2026-06-28 12:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1e109780a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:41 |
| **Last Seen** | 2026-06-28 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:41:12` | `cowrie.session.connect` |
| `2026-06-28 12:41:12` | `cowrie.client.version` |
| `2026-06-28 12:41:13` | `cowrie.client.kex` |
| `2026-06-28 12:41:13` | `cowrie.login.success` |
| `2026-06-28 12:41:14` | `cowrie.session.params` |
| `2026-06-28 12:41:14` | `cowrie.command.input` |
| `2026-06-28 12:41:14` | `cowrie.log.closed` |
| `2026-06-28 12:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4075d16aaf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:42 |
| **Last Seen** | 2026-06-28 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:42:07` | `cowrie.session.connect` |
| `2026-06-28 12:42:07` | `cowrie.client.version` |
| `2026-06-28 12:42:07` | `cowrie.client.kex` |
| `2026-06-28 12:42:08` | `cowrie.login.success` |
| `2026-06-28 12:42:09` | `cowrie.session.params` |
| `2026-06-28 12:42:09` | `cowrie.command.input` |
| `2026-06-28 12:42:09` | `cowrie.log.closed` |
| `2026-06-28 12:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d419d2c6cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:43 |
| **Last Seen** | 2026-06-28 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:43:05` | `cowrie.session.connect` |
| `2026-06-28 12:43:05` | `cowrie.client.version` |
| `2026-06-28 12:43:05` | `cowrie.client.kex` |
| `2026-06-28 12:43:05` | `cowrie.login.success` |
| `2026-06-28 12:43:06` | `cowrie.session.params` |
| `2026-06-28 12:43:06` | `cowrie.command.input` |
| `2026-06-28 12:43:06` | `cowrie.log.closed` |
| `2026-06-28 12:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b126a76e78e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:43 |
| **Last Seen** | 2026-06-28 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:43:59` | `cowrie.session.connect` |
| `2026-06-28 12:43:59` | `cowrie.client.version` |
| `2026-06-28 12:43:59` | `cowrie.client.kex` |
| `2026-06-28 12:44:00` | `cowrie.login.success` |
| `2026-06-28 12:44:00` | `cowrie.session.params` |
| `2026-06-28 12:44:00` | `cowrie.command.input` |
| `2026-06-28 12:44:00` | `cowrie.log.closed` |
| `2026-06-28 12:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-907b09deb7f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:44 |
| **Last Seen** | 2026-06-28 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:44:56` | `cowrie.session.connect` |
| `2026-06-28 12:44:56` | `cowrie.client.version` |
| `2026-06-28 12:44:56` | `cowrie.client.kex` |
| `2026-06-28 12:44:56` | `cowrie.login.success` |
| `2026-06-28 12:44:57` | `cowrie.session.params` |
| `2026-06-28 12:44:57` | `cowrie.command.input` |
| `2026-06-28 12:44:57` | `cowrie.log.closed` |
| `2026-06-28 12:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac06ff21649e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:45 |
| **Last Seen** | 2026-06-28 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:45:52` | `cowrie.session.connect` |
| `2026-06-28 12:45:52` | `cowrie.client.version` |
| `2026-06-28 12:45:52` | `cowrie.client.kex` |
| `2026-06-28 12:45:53` | `cowrie.login.success` |
| `2026-06-28 12:45:53` | `cowrie.session.params` |
| `2026-06-28 12:45:53` | `cowrie.command.input` |
| `2026-06-28 12:45:54` | `cowrie.log.closed` |
| `2026-06-28 12:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc25b0eb0ecf

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-28 12:46 |
| **Last Seen** | 2026-06-28 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:46:28` | `cowrie.session.connect` |
| `2026-06-28 12:46:28` | `cowrie.client.version` |
| `2026-06-28 12:46:28` | `cowrie.client.kex` |
| `2026-06-28 12:46:28` | `cowrie.login.success` |
| `2026-06-28 12:46:29` | `cowrie.session.params` |
| `2026-06-28 12:46:29` | `cowrie.command.input` |
| `2026-06-28 12:46:29` | `cowrie.log.closed` |
| `2026-06-28 12:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6da74dd839b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:46 |
| **Last Seen** | 2026-06-28 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:46:47` | `cowrie.session.connect` |
| `2026-06-28 12:46:47` | `cowrie.client.version` |
| `2026-06-28 12:46:47` | `cowrie.client.kex` |
| `2026-06-28 12:46:48` | `cowrie.login.success` |
| `2026-06-28 12:46:49` | `cowrie.session.params` |
| `2026-06-28 12:46:49` | `cowrie.command.input` |
| `2026-06-28 12:46:49` | `cowrie.log.closed` |
| `2026-06-28 12:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728b827cfb57

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:47 |
| **Last Seen** | 2026-06-28 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:47:42` | `cowrie.session.connect` |
| `2026-06-28 12:47:42` | `cowrie.client.version` |
| `2026-06-28 12:47:42` | `cowrie.client.kex` |
| `2026-06-28 12:47:42` | `cowrie.login.success` |
| `2026-06-28 12:47:43` | `cowrie.session.params` |
| `2026-06-28 12:47:43` | `cowrie.command.input` |
| `2026-06-28 12:47:43` | `cowrie.log.closed` |
| `2026-06-28 12:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b333ec631447

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 12:47 |
| **Last Seen** | 2026-06-28 12:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:47:50` | `cowrie.session.connect` |
| `2026-06-28 12:47:51` | `cowrie.client.version` |
| `2026-06-28 12:47:51` | `cowrie.client.kex` |
| `2026-06-28 12:47:53` | `cowrie.login.success` |
| `2026-06-28 12:47:55` | `cowrie.session.params` |
| `2026-06-28 12:47:55` | `cowrie.command.input` |
| `2026-06-28 12:47:55` | `cowrie.log.closed` |
| `2026-06-28 12:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73966b4bd87

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:48 |
| **Last Seen** | 2026-06-28 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:48:35` | `cowrie.session.connect` |
| `2026-06-28 12:48:35` | `cowrie.client.version` |
| `2026-06-28 12:48:35` | `cowrie.client.kex` |
| `2026-06-28 12:48:35` | `cowrie.login.success` |
| `2026-06-28 12:48:36` | `cowrie.session.params` |
| `2026-06-28 12:48:36` | `cowrie.command.input` |
| `2026-06-28 12:48:36` | `cowrie.log.closed` |
| `2026-06-28 12:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bea001b43ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:49 |
| **Last Seen** | 2026-06-28 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:49:27` | `cowrie.session.connect` |
| `2026-06-28 12:49:27` | `cowrie.client.version` |
| `2026-06-28 12:49:27` | `cowrie.client.kex` |
| `2026-06-28 12:49:28` | `cowrie.login.success` |
| `2026-06-28 12:49:28` | `cowrie.session.params` |
| `2026-06-28 12:49:28` | `cowrie.command.input` |
| `2026-06-28 12:49:29` | `cowrie.log.closed` |
| `2026-06-28 12:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8646f2367d24

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:50 |
| **Last Seen** | 2026-06-28 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:50:22` | `cowrie.session.connect` |
| `2026-06-28 12:50:22` | `cowrie.client.version` |
| `2026-06-28 12:50:22` | `cowrie.client.kex` |
| `2026-06-28 12:50:22` | `cowrie.login.success` |
| `2026-06-28 12:50:23` | `cowrie.session.params` |
| `2026-06-28 12:50:23` | `cowrie.command.input` |
| `2026-06-28 12:50:23` | `cowrie.log.closed` |
| `2026-06-28 12:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce16efb2d221

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:51 |
| **Last Seen** | 2026-06-28 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:51:18` | `cowrie.session.connect` |
| `2026-06-28 12:51:18` | `cowrie.client.version` |
| `2026-06-28 12:51:18` | `cowrie.client.kex` |
| `2026-06-28 12:51:18` | `cowrie.login.success` |
| `2026-06-28 12:51:19` | `cowrie.session.params` |
| `2026-06-28 12:51:19` | `cowrie.command.input` |
| `2026-06-28 12:51:19` | `cowrie.log.closed` |
| `2026-06-28 12:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22dc975a8ae

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 12:51 |
| **Last Seen** | 2026-06-28 12:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:51:43` | `cowrie.session.connect` |
| `2026-06-28 12:51:45` | `cowrie.client.version` |
| `2026-06-28 12:51:45` | `cowrie.client.kex` |
| `2026-06-28 12:51:51` | `cowrie.login.success` |
| `2026-06-28 12:51:54` | `cowrie.session.params` |
| `2026-06-28 12:51:54` | `cowrie.command.input` |
| `2026-06-28 12:51:55` | `cowrie.log.closed` |
| `2026-06-28 12:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b090ceb61484

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:52 |
| **Last Seen** | 2026-06-28 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:52:15` | `cowrie.session.connect` |
| `2026-06-28 12:52:15` | `cowrie.client.version` |
| `2026-06-28 12:52:15` | `cowrie.client.kex` |
| `2026-06-28 12:52:15` | `cowrie.login.success` |
| `2026-06-28 12:52:16` | `cowrie.session.params` |
| `2026-06-28 12:52:16` | `cowrie.command.input` |
| `2026-06-28 12:52:16` | `cowrie.log.closed` |
| `2026-06-28 12:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf71b4663853

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:53 |
| **Last Seen** | 2026-06-28 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:53:11` | `cowrie.session.connect` |
| `2026-06-28 12:53:11` | `cowrie.client.version` |
| `2026-06-28 12:53:11` | `cowrie.client.kex` |
| `2026-06-28 12:53:11` | `cowrie.login.success` |
| `2026-06-28 12:53:12` | `cowrie.session.params` |
| `2026-06-28 12:53:12` | `cowrie.command.input` |
| `2026-06-28 12:53:12` | `cowrie.log.closed` |
| `2026-06-28 12:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e958be82380

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 12:54 |
| **Last Seen** | 2026-06-28 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 12:54:07` | `cowrie.session.connect` |
| `2026-06-28 12:54:07` | `cowrie.client.version` |
| `2026-06-28 12:54:08` | `cowrie.client.kex` |
| `2026-06-28 12:54:08` | `cowrie.login.success` |
| `2026-06-28 12:54:09` | `cowrie.session.params` |
| `2026-06-28 12:54:09` | `cowrie.command.input` |
| `2026-06-28 12:54:09` | `cowrie.log.closed` |
| `2026-06-28 12:54:09` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **126** | 2026-06-28 10:55 | 2026-06-28 12:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `45.142.154[.]108` | **8** | 2026-06-28 12:11 | 2026-06-28 12:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-06-28 12:49 | 2026-06-28 12:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.176[.]104` | **2** | 2026-06-28 11:51 | 2026-06-28 11:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `157.230.42[.]17` | 1 | 2026-06-28 11:39 | 2026-06-28 11:40 | 41s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-28 11:00 | 2026-06-28 11:01 | 75s | 0 | `T1592` | 🟢 LOW |
| `218.203.203[.]232` | 1 | 2026-06-28 11:39 | 2026-06-28 11:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.164.177[.]41` | 1 | 2026-06-28 11:40 | 2026-06-28 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]179` | 1 | 2026-06-28 11:32 | 2026-06-28 11:32 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **5/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 50/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `62.164.177[.]41` | NL | Layer7 Networks GmbH | **100** ⚠️ | 24 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `159.65.91[.]36` | GB | DigitalOcean, LLC | **100** ⚠️ | 15 |
| `45.142.154[.]108` | HK | HDTIDC LIMITED | **100** ⚠️ | 50 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `66.132.186[.]179` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 169 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 159 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 312 cases |
| Tool 34  | Credential Extractor        | ✅ 161 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (1.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 41 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 159 priority case(s) shown individually · 9 recon entry/entries in table (4 group(s) consolidating 142 session(s)).

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
_Report time: 2026-06-28T13:55:44Z_

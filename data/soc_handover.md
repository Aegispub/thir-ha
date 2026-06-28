# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-28 |
| **Generated At** | 2026-06-28T11:48:50Z |
| **Shift Time** | 11:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **326** |
| Confirmed Threats | **317** |
| False Positives Filtered | **9** (2.8%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **11** |
| High Severity Cases | **163** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **163** |
| Malware Samples Analyzed | **5** HIGH · **41** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **164** |
| Unique Credential Pairs | **159** |
| Unique Usernames | **85** |
| Unique Passwords | **140** |
| Successful Auth Pairs | **158** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 69 |
| `ubuntu` | 4 |
| `nagios` | 3 |
| `zhouh` | 3 |
| `git` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `smo@@kkklss` | 4 |
| `123` | 3 |
| `qwe123` | 3 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 4 |
| `root` | `123@@@` | 2 |
| `root` | `LeitboGi0ro` | 2 |
| `zabbix` | `123` | 1 |
| `root` | `bgt5VFR$cde3` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `zabbix` | `123` | `209.99.185.59` | 2026-06-28T08:55:21 |
| `root` | `bgt5VFR$cde3` | `209.99.185.59` | 2026-06-28T08:56:16 |
| `root` | `123passwd` | `209.99.185.59` | 2026-06-28T08:57:12 |
| `admin2` | `123456` | `209.99.185.59` | 2026-06-28T08:58:07 |
| `ftp` | `ftp` | `27.79.2.107` | 2026-06-28T08:58:29 |
| `ltfeng` | `ltfeng` | `209.99.185.59` | 2026-06-28T08:59:01 |
| `nagios` | `q1w2e3` | `209.99.185.59` | 2026-06-28T08:59:55 |
| `kt` | `123456` | `209.99.185.59` | 2026-06-28T09:00:51 |
| `operator` | `operator` | `27.79.2.107` | 2026-06-28T09:00:54 |
| `openlava` | `openlava` | `209.99.185.59` | 2026-06-28T09:01:49 |
| `support` | `admin` | `27.79.2.107` | 2026-06-28T09:02:48 |
| `tomcat` | `^%$#@!` | `209.99.185.59` | 2026-06-28T09:02:48 |
| `root` | `P@ssw0rd#123` | `45.198.224.120` | 2026-06-28T09:03:22 |
| `root` | `qwe123!@#QWE` | `209.99.185.59` | 2026-06-28T09:03:47 |
| `zk` | `123456` | `209.99.185.59` | 2026-06-28T09:04:46 |
| `root` | `1111` | `209.99.185.59` | 2026-06-28T09:05:43 |
| `hyun` | `hyun` | `209.99.185.59` | 2026-06-28T09:06:41 |
| `oracle` | `oracleoracle` | `45.205.1.42` | 2026-06-28T09:06:52 |
| `bhm` | `bhm` | `209.99.185.59` | 2026-06-28T09:07:39 |
| `root` | `QWEQWE!@#!@#` | `209.99.185.59` | 2026-06-28T09:08:38 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.232` | 2026-06-28T09:09:10 |
| `Adam` | `123456` | `209.99.185.59` | 2026-06-28T09:09:38 |
| `root` | `azerty` | `209.99.185.59` | 2026-06-28T09:10:37 |
| `zhixinwang` | `qwe123` | `209.99.185.59` | 2026-06-28T09:11:35 |
| `root` | `sqlpass` | `209.99.185.59` | 2026-06-28T09:12:34 |
| `root` | `amazon` | `209.99.185.59` | 2026-06-28T09:13:33 |
| `root` | `kingofking` | `209.99.185.59` | 2026-06-28T09:14:33 |
| `ubuntu` | `root` | `45.198.224.120` | 2026-06-28T09:14:47 |
| `root` | `Cdntest!@#$` | `209.99.185.59` | 2026-06-28T09:15:35 |
| `centos7` | `123` | `209.99.185.59` | 2026-06-28T09:16:38 |
| `root` | `management` | `209.99.185.59` | 2026-06-28T09:17:40 |
| `root` | `bobo123` | `209.99.185.59` | 2026-06-28T09:18:40 |
| `r00t` | `qweasd123` | `209.99.185.59` | 2026-06-28T09:19:40 |
| `root` | `P4ssw0rd123` | `209.99.185.59` | 2026-06-28T09:20:42 |
| `root` | `Root@1234` | `45.205.1.42` | 2026-06-28T09:21:37 |
| `root` | `999999` | `209.99.185.59` | 2026-06-28T09:21:44 |
| `wangyinan` | `wangyinan` | `209.99.185.59` | 2026-06-28T09:22:47 |
| `apache` | `123qwe` | `209.99.185.59` | 2026-06-28T09:23:48 |
| `sync` | `123abc` | `209.99.185.59` | 2026-06-28T09:24:49 |
| `jsh` | `jsh` | `209.99.185.59` | 2026-06-28T09:25:49 |
| `root` | `12345678901` | `45.198.224.120` | 2026-06-28T09:26:23 |
| `zzk` | `zzk` | `209.99.185.59` | 2026-06-28T09:26:51 |
| `root` | `pppppp` | `209.99.185.59` | 2026-06-28T09:27:54 |
| `ghb` | `123456` | `209.99.185.59` | 2026-06-28T09:28:57 |
| `zhouh` | `qwerty123456` | `209.99.185.59` | 2026-06-28T09:29:58 |
| `zhouh` | `password` | `209.99.185.59` | 2026-06-28T09:30:58 |
| `sy_hs` | `84NPSH7u9U` | `209.99.185.59` | 2026-06-28T09:31:58 |
| `zero` | `zero123` | `209.99.185.59` | 2026-06-28T09:33:01 |
| `root` | `Root.123` | `209.99.185.59` | 2026-06-28T09:34:04 |
| `metadata` | `metadata0` | `209.99.185.59` | 2026-06-28T09:35:07 |
| `sales` | `sales123` | `209.99.185.59` | 2026-06-28T09:36:14 |
| `root` | `Passw0rd11` | `45.205.1.42` | 2026-06-28T09:36:22 |
| `john` | `password` | `45.148.10.239` | 2026-06-28T09:37:20 |
| `user` | `123321` | `209.99.185.59` | 2026-06-28T09:37:26 |
| `root` | `!QAZ2wsx3edc` | `45.198.224.120` | 2026-06-28T09:37:34 |
| `root` | `t3cn0l0g!` | `209.99.185.59` | 2026-06-28T09:38:28 |
| `root` | `---fuck_you----` | `14.169.72.130` | 2026-06-28T09:39:20 |
| `zhangfan` | `zhangfan` | `209.99.185.59` | 2026-06-28T09:39:32 |
| `jiyuan` | `jiyuan` | `209.99.185.59` | 2026-06-28T09:40:38 |
| `dpessoal1` | `dpessoal1` | `209.99.185.59` | 2026-06-28T09:41:43 |
| `ghost` | `222222` | `209.99.185.59` | 2026-06-28T09:42:49 |
| `root` | `1233218613` | `209.99.185.59` | 2026-06-28T09:43:52 |
| `sc` | `123456` | `209.99.185.59` | 2026-06-28T09:44:55 |
| `root` | `SMS,Shenshoubibeizhuo233` | `209.99.185.59` | 2026-06-28T09:46:00 |
| `test02` | `Test@cii` | `209.99.185.59` | 2026-06-28T09:47:06 |
| `root` | `P4SSWORD` | `209.99.185.59` | 2026-06-28T09:48:12 |
| `ubuntu` | `a1a1a1` | `45.198.224.120` | 2026-06-28T09:49:12 |
| `ejlee` | `111111` | `209.99.185.59` | 2026-06-28T09:49:17 |
| `shutinggu3` | `shutinggu3` | `209.99.185.59` | 2026-06-28T09:50:22 |
| `fernando` | `fernando` | `45.205.1.42` | 2026-06-28T09:51:05 |
| `root` | `0000` | `209.99.185.59` | 2026-06-28T09:51:26 |
| `yan` | `yan` | `209.99.185.59` | 2026-06-28T09:52:32 |
| `superuser` | `passw0rd` | `209.99.185.59` | 2026-06-28T09:53:40 |
| `root` | `qwerty` | `209.99.185.59` | 2026-06-28T09:54:47 |
| `postgres` | `qwe123` | `209.99.185.59` | 2026-06-28T09:55:52 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-28T09:56:22 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-28T09:56:22 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-28T09:56:28 |
| `root` | `git123` | `209.99.185.59` | 2026-06-28T09:56:57 |
| `root` | `qaz123!@#` | `209.99.185.59` | 2026-06-28T09:58:02 |
| `git` | `Admin@123!` | `209.99.185.59` | 2026-06-28T09:59:08 |
| `linj` | `3291087lj` | `209.99.185.59` | 2026-06-28T10:00:15 |
| `xiazehong` | `xiazehong` | `45.198.224.120` | 2026-06-28T10:00:41 |
| `root` | `qwe123321` | `209.99.185.59` | 2026-06-28T10:01:00 |
| `centos` | `123456` | `209.99.185.59` | 2026-06-28T10:01:46 |
| `git` | `qwe123` | `209.99.185.59` | 2026-06-28T10:02:30 |
| `sander` | `sander123` | `209.99.185.59` | 2026-06-28T10:03:14 |
| `postgres` | `postgres123` | `209.99.185.59` | 2026-06-28T10:03:58 |
| `caja25` | `caja25` | `209.99.185.59` | 2026-06-28T10:04:42 |
| `adt` | `123456` | `209.99.185.59` | 2026-06-28T10:05:28 |
| `root` | `qwerty12` | `45.205.1.42` | 2026-06-28T10:05:46 |
| `lkw91` | `0104151511lkw` | `209.99.185.59` | 2026-06-28T10:06:14 |
| `nagios` | `qwerty` | `209.99.185.59` | 2026-06-28T10:07:02 |
| `root` | `lorenzo` | `209.99.185.59` | 2026-06-28T10:07:49 |
| `devops` | `1234567` | `209.99.185.59` | 2026-06-28T10:08:36 |
| `ubuntu` | `qmfltmqjs!@#$` | `209.99.185.59` | 2026-06-28T10:09:22 |
| `nagios` | `nag10s` | `209.99.185.59` | 2026-06-28T10:10:08 |
| `yangliusha16` | `yangliusha16` | `209.99.185.59` | 2026-06-28T10:10:56 |
| `zsn` | `zsn` | `209.99.185.59` | 2026-06-28T10:11:44 |
| `ubuntu` | `passw0rd1` | `45.198.224.120` | 2026-06-28T10:12:10 |
| `qfhuang` | `qfhuang0616` | `209.99.185.59` | 2026-06-28T10:12:32 |
| `root` | `9ol#EDC4rfv` | `209.99.185.59` | 2026-06-28T10:13:21 |
| `yangliusha4` | `yangliusha4` | `209.99.185.59` | 2026-06-28T10:14:57 |
| `root` | `server2010` | `209.99.185.59` | 2026-06-28T10:15:44 |
| `root` | `4X+9zXs3k6%1` | `209.99.185.59` | 2026-06-28T10:16:31 |
| `root` | `Wolong@2022` | `209.99.185.59` | 2026-06-28T10:17:19 |
| `pi` | `123456` | `209.99.185.59` | 2026-06-28T10:18:07 |
| `test2` | `123456` | `209.99.185.59` | 2026-06-28T10:18:58 |
| `ecnu` | `1` | `209.99.185.59` | 2026-06-28T10:19:47 |
| `root` | `Password@12345` | `45.205.1.42` | 2026-06-28T10:20:32 |
| `yhchoi` | `yhchoi` | `209.99.185.59` | 2026-06-28T10:20:38 |
| `angel` | `angel1234` | `209.99.185.59` | 2026-06-28T10:21:26 |
| `root` | `Password12#$` | `209.99.185.59` | 2026-06-28T10:22:15 |
| `root` | `tequila` | `209.99.185.59` | 2026-06-28T10:23:02 |
| `info` | `info123` | `45.198.224.120` | 2026-06-28T10:23:48 |
| `chris` | `chris` | `209.99.185.59` | 2026-06-28T10:23:51 |
| `device` | `qazwsx` | `209.99.185.59` | 2026-06-28T10:24:42 |
| `chuhaoyu` | `chuhaoyu` | `209.99.185.59` | 2026-06-28T10:25:34 |
| `iexcel` | `0` | `209.99.185.59` | 2026-06-28T10:26:25 |
| `build` | `123456` | `209.99.185.59` | 2026-06-28T10:27:16 |
| `quadralia` | `quadralia123` | `209.99.185.59` | 2026-06-28T10:28:06 |
| `spark` | `spark` | `209.99.185.59` | 2026-06-28T10:28:56 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.236.228.229` | 2026-06-28T10:29:16 |
| `fjs` | `Fjs41956946` | `209.99.185.59` | 2026-06-28T10:29:46 |
| `root` | `hack` | `209.99.185.59` | 2026-06-28T10:30:38 |
| `git` | `654321` | `209.99.185.59` | 2026-06-28T10:31:30 |
| `root` | `Master` | `209.99.185.59` | 2026-06-28T10:32:24 |
| `root` | `750323` | `209.99.185.59` | 2026-06-28T10:33:17 |
| `lyp` | `111111` | `209.99.185.59` | 2026-06-28T10:34:10 |
| `root` | `Pass@word#123` | `209.99.185.59` | 2026-06-28T10:35:02 |
| `jack` | `test123` | `45.198.224.120` | 2026-06-28T10:35:14 |
| `root` | `qwe#@!` | `45.205.1.42` | 2026-06-28T10:35:20 |
| `root` | `admin@1234` | `209.99.185.59` | 2026-06-28T10:35:54 |
| `share` | `share123` | `209.99.185.59` | 2026-06-28T10:36:47 |
| `root` | `qweasdqwe` | `209.99.185.59` | 2026-06-28T10:37:39 |
| `root` | `Admin@2018` | `209.99.185.59` | 2026-06-28T10:38:32 |
| `huangxingnan` | `huangxingnan123` | `209.99.185.59` | 2026-06-28T10:39:25 |
| `root` | `﻿------fuck------` | `219.138.78.67` | 2026-06-28T10:39:49 |
| `root` | `iloveyou` | `209.99.185.59` | 2026-06-28T10:40:18 |
| `root` | `Baidu@123` | `209.99.185.59` | 2026-06-28T10:41:10 |
| `root` | `ohmnamah23` | `209.99.185.59` | 2026-06-28T10:42:01 |
| `acs` | `acs` | `209.99.185.59` | 2026-06-28T10:42:53 |
| `caoyang` | `caoyang` | `209.99.185.59` | 2026-06-28T10:43:46 |
| `www-data` | `www-data!@#123` | `209.99.185.59` | 2026-06-28T10:44:41 |
| `zhouh` | `test321` | `209.99.185.59` | 2026-06-28T10:45:38 |
| `root` | `Passwd12345` | `45.198.224.120` | 2026-06-28T10:46:31 |
| `root` | `europa` | `209.99.185.59` | 2026-06-28T10:46:33 |
| `buero3` | `buero3123` | `209.99.185.59` | 2026-06-28T10:47:27 |
| `yunjun` | `yunjun` | `209.99.185.59` | 2026-06-28T10:48:20 |
| `tianjun` | `:tianjun` | `209.99.185.59` | 2026-06-28T10:49:15 |
| `root` | `jimjim30` | `45.205.1.42` | 2026-06-28T10:49:59 |
| `fcx` | `123` | `209.99.185.59` | 2026-06-28T10:50:11 |
| `root` | `computer` | `209.99.185.59` | 2026-06-28T10:51:09 |
| `root` | `admin` | `95.220.204.16` | 2026-06-28T10:51:37 |
| `root` | `linux@123` | `209.99.185.59` | 2026-06-28T10:52:05 |
| `root` | `descan` | `209.99.185.59` | 2026-06-28T10:53:02 |
| `root` | `aA11.22` | `209.99.185.59` | 2026-06-28T10:53:56 |
| `jira` | `q1w2e3r4` | `209.99.185.59` | 2026-06-28T10:54:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **326** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 150 |
| Paramiko (Python) | 9 |
| libssh | 6 |
| AsyncSSH (Python) | 3 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 147 | 4 |
| `a2de0f306611...` | Mirai/variant | 8 | 1 |
| `fda360b1b4f4...` | Mirai/variant | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 147 | 4 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 3 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **21** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS6866` | Cyprus Telecommunications Authority | 1 | HIGH |
| `AS49981` | WorldStream B.V. | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (162)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9465f17a9914

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 08:55 |
| **Last Seen** | 2026-06-28 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 08:55:21` | `cowrie.session.connect` |
| `2026-06-28 08:55:21` | `cowrie.client.version` |
| `2026-06-28 08:55:21` | `cowrie.client.kex` |
| `2026-06-28 08:55:21` | `cowrie.login.success` |
| `2026-06-28 08:55:22` | `cowrie.session.params` |
| `2026-06-28 08:55:22` | `cowrie.command.input` |
| `2026-06-28 08:55:22` | `cowrie.log.closed` |
| `2026-06-28 08:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f87581f04c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 08:56 |
| **Last Seen** | 2026-06-28 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 08:56:16` | `cowrie.session.connect` |
| `2026-06-28 08:56:16` | `cowrie.client.version` |
| `2026-06-28 08:56:16` | `cowrie.client.kex` |
| `2026-06-28 08:56:16` | `cowrie.login.success` |
| `2026-06-28 08:56:17` | `cowrie.session.params` |
| `2026-06-28 08:56:17` | `cowrie.command.input` |
| `2026-06-28 08:56:17` | `cowrie.log.closed` |
| `2026-06-28 08:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8c34c5d150

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 08:57 |
| **Last Seen** | 2026-06-28 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 08:57:12` | `cowrie.session.connect` |
| `2026-06-28 08:57:12` | `cowrie.client.version` |
| `2026-06-28 08:57:12` | `cowrie.client.kex` |
| `2026-06-28 08:57:12` | `cowrie.login.success` |
| `2026-06-28 08:57:13` | `cowrie.session.params` |
| `2026-06-28 08:57:13` | `cowrie.command.input` |
| `2026-06-28 08:57:13` | `cowrie.log.closed` |
| `2026-06-28 08:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd5c4dc10ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 08:58 |
| **Last Seen** | 2026-06-28 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 08:58:07` | `cowrie.session.connect` |
| `2026-06-28 08:58:07` | `cowrie.client.version` |
| `2026-06-28 08:58:07` | `cowrie.client.kex` |
| `2026-06-28 08:58:07` | `cowrie.login.success` |
| `2026-06-28 08:58:08` | `cowrie.session.params` |
| `2026-06-28 08:58:08` | `cowrie.command.input` |
| `2026-06-28 08:58:08` | `cowrie.log.closed` |
| `2026-06-28 08:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e048d1e41181

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]107` |
| **First Seen** | 2026-06-28 08:58 |
| **Last Seen** | 2026-06-28 08:59 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 08:58:08` | `cowrie.session.connect` |
| `2026-06-28 08:58:08` | `cowrie.client.version` |
| `2026-06-28 08:58:21` | `cowrie.client.kex` |
| `2026-06-28 08:58:29` | `cowrie.login.success` |
| `2026-06-28 08:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]107` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e19424401ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 08:59 |
| **Last Seen** | 2026-06-28 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 08:59:01` | `cowrie.session.connect` |
| `2026-06-28 08:59:01` | `cowrie.client.version` |
| `2026-06-28 08:59:01` | `cowrie.client.kex` |
| `2026-06-28 08:59:01` | `cowrie.login.success` |
| `2026-06-28 08:59:02` | `cowrie.session.params` |
| `2026-06-28 08:59:02` | `cowrie.command.input` |
| `2026-06-28 08:59:02` | `cowrie.log.closed` |
| `2026-06-28 08:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa54726f8351

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 08:59 |
| **Last Seen** | 2026-06-28 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 08:59:55` | `cowrie.session.connect` |
| `2026-06-28 08:59:55` | `cowrie.client.version` |
| `2026-06-28 08:59:55` | `cowrie.client.kex` |
| `2026-06-28 08:59:55` | `cowrie.login.success` |
| `2026-06-28 08:59:56` | `cowrie.session.params` |
| `2026-06-28 08:59:56` | `cowrie.command.input` |
| `2026-06-28 08:59:56` | `cowrie.log.closed` |
| `2026-06-28 08:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6318e18b15

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]107` |
| **First Seen** | 2026-06-28 09:00 |
| **Last Seen** | 2026-06-28 09:01 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:00:26` | `cowrie.session.connect` |
| `2026-06-28 09:00:26` | `cowrie.client.version` |
| `2026-06-28 09:00:28` | `cowrie.client.kex` |
| `2026-06-28 09:00:54` | `cowrie.login.success` |
| `2026-06-28 09:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]107` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e000b62b80b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:00 |
| **Last Seen** | 2026-06-28 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:00:51` | `cowrie.session.connect` |
| `2026-06-28 09:00:51` | `cowrie.client.version` |
| `2026-06-28 09:00:51` | `cowrie.client.kex` |
| `2026-06-28 09:00:51` | `cowrie.login.success` |
| `2026-06-28 09:00:52` | `cowrie.session.params` |
| `2026-06-28 09:00:52` | `cowrie.command.input` |
| `2026-06-28 09:00:52` | `cowrie.log.closed` |
| `2026-06-28 09:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955bff6b85ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:01 |
| **Last Seen** | 2026-06-28 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:01:49` | `cowrie.session.connect` |
| `2026-06-28 09:01:49` | `cowrie.client.version` |
| `2026-06-28 09:01:49` | `cowrie.client.kex` |
| `2026-06-28 09:01:49` | `cowrie.login.success` |
| `2026-06-28 09:01:50` | `cowrie.session.params` |
| `2026-06-28 09:01:50` | `cowrie.command.input` |
| `2026-06-28 09:01:50` | `cowrie.log.closed` |
| `2026-06-28 09:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0b0cb9c17d

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]107` |
| **First Seen** | 2026-06-28 09:02 |
| **Last Seen** | 2026-06-28 09:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:02:47` | `cowrie.session.connect` |
| `2026-06-28 09:02:47` | `cowrie.client.version` |
| `2026-06-28 09:02:47` | `cowrie.client.kex` |
| `2026-06-28 09:02:48` | `cowrie.login.success` |
| `2026-06-28 09:02:50` | `cowrie.direct-tcpip.request` |
| `2026-06-28 09:02:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-28 09:02:52` | `cowrie.direct-tcpip.data` |
| `2026-06-28 09:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]107` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a4cde099aa4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:02 |
| **Last Seen** | 2026-06-28 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:02:48` | `cowrie.session.connect` |
| `2026-06-28 09:02:48` | `cowrie.client.version` |
| `2026-06-28 09:02:48` | `cowrie.client.kex` |
| `2026-06-28 09:02:48` | `cowrie.login.success` |
| `2026-06-28 09:02:49` | `cowrie.session.params` |
| `2026-06-28 09:02:49` | `cowrie.command.input` |
| `2026-06-28 09:02:49` | `cowrie.log.closed` |
| `2026-06-28 09:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68aac21a6f9c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 09:03 |
| **Last Seen** | 2026-06-28 09:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:03:15` | `cowrie.session.connect` |
| `2026-06-28 09:03:17` | `cowrie.client.version` |
| `2026-06-28 09:03:17` | `cowrie.client.kex` |
| `2026-06-28 09:03:22` | `cowrie.login.success` |
| `2026-06-28 09:03:26` | `cowrie.session.params` |
| `2026-06-28 09:03:26` | `cowrie.command.input` |
| `2026-06-28 09:03:27` | `cowrie.log.closed` |
| `2026-06-28 09:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c7f11124f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:03 |
| **Last Seen** | 2026-06-28 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:03:47` | `cowrie.session.connect` |
| `2026-06-28 09:03:47` | `cowrie.client.version` |
| `2026-06-28 09:03:47` | `cowrie.client.kex` |
| `2026-06-28 09:03:47` | `cowrie.login.success` |
| `2026-06-28 09:03:48` | `cowrie.session.params` |
| `2026-06-28 09:03:48` | `cowrie.command.input` |
| `2026-06-28 09:03:48` | `cowrie.log.closed` |
| `2026-06-28 09:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3b22429853

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:04 |
| **Last Seen** | 2026-06-28 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:04:45` | `cowrie.session.connect` |
| `2026-06-28 09:04:45` | `cowrie.client.version` |
| `2026-06-28 09:04:45` | `cowrie.client.kex` |
| `2026-06-28 09:04:46` | `cowrie.login.success` |
| `2026-06-28 09:04:46` | `cowrie.session.params` |
| `2026-06-28 09:04:46` | `cowrie.command.input` |
| `2026-06-28 09:04:47` | `cowrie.log.closed` |
| `2026-06-28 09:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88cd7de1bc8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:05 |
| **Last Seen** | 2026-06-28 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:05:43` | `cowrie.session.connect` |
| `2026-06-28 09:05:43` | `cowrie.client.version` |
| `2026-06-28 09:05:43` | `cowrie.client.kex` |
| `2026-06-28 09:05:43` | `cowrie.login.success` |
| `2026-06-28 09:05:44` | `cowrie.session.params` |
| `2026-06-28 09:05:44` | `cowrie.command.input` |
| `2026-06-28 09:05:44` | `cowrie.log.closed` |
| `2026-06-28 09:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d02a972dc35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:06 |
| **Last Seen** | 2026-06-28 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:06:40` | `cowrie.session.connect` |
| `2026-06-28 09:06:40` | `cowrie.client.version` |
| `2026-06-28 09:06:40` | `cowrie.client.kex` |
| `2026-06-28 09:06:41` | `cowrie.login.success` |
| `2026-06-28 09:06:41` | `cowrie.session.params` |
| `2026-06-28 09:06:41` | `cowrie.command.input` |
| `2026-06-28 09:06:41` | `cowrie.log.closed` |
| `2026-06-28 09:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55847930068c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 09:06 |
| **Last Seen** | 2026-06-28 09:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:06:50` | `cowrie.session.connect` |
| `2026-06-28 09:06:51` | `cowrie.client.version` |
| `2026-06-28 09:06:51` | `cowrie.client.kex` |
| `2026-06-28 09:06:52` | `cowrie.login.success` |
| `2026-06-28 09:06:54` | `cowrie.session.params` |
| `2026-06-28 09:06:54` | `cowrie.command.input` |
| `2026-06-28 09:06:54` | `cowrie.log.closed` |
| `2026-06-28 09:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8442ad0f2b82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:07 |
| **Last Seen** | 2026-06-28 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:07:38` | `cowrie.session.connect` |
| `2026-06-28 09:07:38` | `cowrie.client.version` |
| `2026-06-28 09:07:38` | `cowrie.client.kex` |
| `2026-06-28 09:07:39` | `cowrie.login.success` |
| `2026-06-28 09:07:39` | `cowrie.session.params` |
| `2026-06-28 09:07:39` | `cowrie.command.input` |
| `2026-06-28 09:07:40` | `cowrie.log.closed` |
| `2026-06-28 09:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73550ffbef67

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:08 |
| **Last Seen** | 2026-06-28 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:08:38` | `cowrie.session.connect` |
| `2026-06-28 09:08:38` | `cowrie.client.version` |
| `2026-06-28 09:08:38` | `cowrie.client.kex` |
| `2026-06-28 09:08:38` | `cowrie.login.success` |
| `2026-06-28 09:08:39` | `cowrie.session.params` |
| `2026-06-28 09:08:39` | `cowrie.command.input` |
| `2026-06-28 09:08:39` | `cowrie.log.closed` |
| `2026-06-28 09:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188b2f1919dc

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]232` |
| **First Seen** | 2026-06-28 09:09 |
| **Last Seen** | 2026-06-28 09:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:09:10` | `cowrie.session.connect` |
| `2026-06-28 09:09:10` | `cowrie.login.success` |
| `2026-06-28 09:09:10` | `cowrie.session.params` |
| `2026-06-28 09:09:10` | `cowrie.command.input` |
| `2026-06-28 09:09:10` | `cowrie.command.input` |
| `2026-06-28 09:09:10` | `cowrie.command.failed` |
| `2026-06-28 09:09:10` | `cowrie.command.input` |
| `2026-06-28 09:09:10` | `cowrie.command.failed` |
| `2026-06-28 09:09:10` | `cowrie.command.input` |
| `2026-06-28 09:09:10` | `cowrie.log.closed` |
| `2026-06-28 09:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]232` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfcb091712cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:09 |
| **Last Seen** | 2026-06-28 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:09:37` | `cowrie.session.connect` |
| `2026-06-28 09:09:37` | `cowrie.client.version` |
| `2026-06-28 09:09:38` | `cowrie.client.kex` |
| `2026-06-28 09:09:38` | `cowrie.login.success` |
| `2026-06-28 09:09:39` | `cowrie.session.params` |
| `2026-06-28 09:09:39` | `cowrie.command.input` |
| `2026-06-28 09:09:39` | `cowrie.log.closed` |
| `2026-06-28 09:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1cdba050d1e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:10 |
| **Last Seen** | 2026-06-28 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:10:36` | `cowrie.session.connect` |
| `2026-06-28 09:10:36` | `cowrie.client.version` |
| `2026-06-28 09:10:36` | `cowrie.client.kex` |
| `2026-06-28 09:10:37` | `cowrie.login.success` |
| `2026-06-28 09:10:37` | `cowrie.session.params` |
| `2026-06-28 09:10:37` | `cowrie.command.input` |
| `2026-06-28 09:10:38` | `cowrie.log.closed` |
| `2026-06-28 09:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb71f0eca7ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:11 |
| **Last Seen** | 2026-06-28 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:11:35` | `cowrie.session.connect` |
| `2026-06-28 09:11:35` | `cowrie.client.version` |
| `2026-06-28 09:11:35` | `cowrie.client.kex` |
| `2026-06-28 09:11:35` | `cowrie.login.success` |
| `2026-06-28 09:11:36` | `cowrie.session.params` |
| `2026-06-28 09:11:36` | `cowrie.command.input` |
| `2026-06-28 09:11:36` | `cowrie.log.closed` |
| `2026-06-28 09:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4ccb183904

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:12 |
| **Last Seen** | 2026-06-28 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:12:34` | `cowrie.session.connect` |
| `2026-06-28 09:12:34` | `cowrie.client.version` |
| `2026-06-28 09:12:34` | `cowrie.client.kex` |
| `2026-06-28 09:12:34` | `cowrie.login.success` |
| `2026-06-28 09:12:35` | `cowrie.session.params` |
| `2026-06-28 09:12:35` | `cowrie.command.input` |
| `2026-06-28 09:12:35` | `cowrie.log.closed` |
| `2026-06-28 09:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0250449d0142

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:13 |
| **Last Seen** | 2026-06-28 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:13:33` | `cowrie.session.connect` |
| `2026-06-28 09:13:33` | `cowrie.client.version` |
| `2026-06-28 09:13:33` | `cowrie.client.kex` |
| `2026-06-28 09:13:33` | `cowrie.login.success` |
| `2026-06-28 09:13:34` | `cowrie.session.params` |
| `2026-06-28 09:13:34` | `cowrie.command.input` |
| `2026-06-28 09:13:34` | `cowrie.log.closed` |
| `2026-06-28 09:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b485584d0b46

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:14 |
| **Last Seen** | 2026-06-28 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:14:32` | `cowrie.session.connect` |
| `2026-06-28 09:14:32` | `cowrie.client.version` |
| `2026-06-28 09:14:32` | `cowrie.client.kex` |
| `2026-06-28 09:14:33` | `cowrie.login.success` |
| `2026-06-28 09:14:33` | `cowrie.session.params` |
| `2026-06-28 09:14:33` | `cowrie.command.input` |
| `2026-06-28 09:14:34` | `cowrie.log.closed` |
| `2026-06-28 09:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d58399cbe249

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 09:14 |
| **Last Seen** | 2026-06-28 09:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:14:41` | `cowrie.session.connect` |
| `2026-06-28 09:14:42` | `cowrie.client.version` |
| `2026-06-28 09:14:42` | `cowrie.client.kex` |
| `2026-06-28 09:14:47` | `cowrie.login.success` |
| `2026-06-28 09:14:51` | `cowrie.session.params` |
| `2026-06-28 09:14:51` | `cowrie.command.input` |
| `2026-06-28 09:14:52` | `cowrie.log.closed` |
| `2026-06-28 09:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b101e16b140

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:15 |
| **Last Seen** | 2026-06-28 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:15:34` | `cowrie.session.connect` |
| `2026-06-28 09:15:34` | `cowrie.client.version` |
| `2026-06-28 09:15:34` | `cowrie.client.kex` |
| `2026-06-28 09:15:35` | `cowrie.login.success` |
| `2026-06-28 09:15:35` | `cowrie.session.params` |
| `2026-06-28 09:15:35` | `cowrie.command.input` |
| `2026-06-28 09:15:36` | `cowrie.log.closed` |
| `2026-06-28 09:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15fcbe29fde9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:16 |
| **Last Seen** | 2026-06-28 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:16:37` | `cowrie.session.connect` |
| `2026-06-28 09:16:37` | `cowrie.client.version` |
| `2026-06-28 09:16:37` | `cowrie.client.kex` |
| `2026-06-28 09:16:38` | `cowrie.login.success` |
| `2026-06-28 09:16:38` | `cowrie.session.params` |
| `2026-06-28 09:16:38` | `cowrie.command.input` |
| `2026-06-28 09:16:38` | `cowrie.log.closed` |
| `2026-06-28 09:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56def5234909

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:17 |
| **Last Seen** | 2026-06-28 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:17:39` | `cowrie.session.connect` |
| `2026-06-28 09:17:39` | `cowrie.client.version` |
| `2026-06-28 09:17:39` | `cowrie.client.kex` |
| `2026-06-28 09:17:40` | `cowrie.login.success` |
| `2026-06-28 09:17:40` | `cowrie.session.params` |
| `2026-06-28 09:17:40` | `cowrie.command.input` |
| `2026-06-28 09:17:41` | `cowrie.log.closed` |
| `2026-06-28 09:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3c25be407f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:18 |
| **Last Seen** | 2026-06-28 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:18:40` | `cowrie.session.connect` |
| `2026-06-28 09:18:40` | `cowrie.client.version` |
| `2026-06-28 09:18:40` | `cowrie.client.kex` |
| `2026-06-28 09:18:40` | `cowrie.login.success` |
| `2026-06-28 09:18:41` | `cowrie.session.params` |
| `2026-06-28 09:18:41` | `cowrie.command.input` |
| `2026-06-28 09:18:41` | `cowrie.log.closed` |
| `2026-06-28 09:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ac9d6faecd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:19 |
| **Last Seen** | 2026-06-28 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:19:40` | `cowrie.session.connect` |
| `2026-06-28 09:19:40` | `cowrie.client.version` |
| `2026-06-28 09:19:40` | `cowrie.client.kex` |
| `2026-06-28 09:19:40` | `cowrie.login.success` |
| `2026-06-28 09:19:41` | `cowrie.session.params` |
| `2026-06-28 09:19:41` | `cowrie.command.input` |
| `2026-06-28 09:19:41` | `cowrie.log.closed` |
| `2026-06-28 09:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85661f5825a6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:20 |
| **Last Seen** | 2026-06-28 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:20:41` | `cowrie.session.connect` |
| `2026-06-28 09:20:41` | `cowrie.client.version` |
| `2026-06-28 09:20:41` | `cowrie.client.kex` |
| `2026-06-28 09:20:42` | `cowrie.login.success` |
| `2026-06-28 09:20:42` | `cowrie.session.params` |
| `2026-06-28 09:20:42` | `cowrie.command.input` |
| `2026-06-28 09:20:43` | `cowrie.log.closed` |
| `2026-06-28 09:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e89acac5c5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 09:21 |
| **Last Seen** | 2026-06-28 09:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:21:35` | `cowrie.session.connect` |
| `2026-06-28 09:21:35` | `cowrie.client.version` |
| `2026-06-28 09:21:35` | `cowrie.client.kex` |
| `2026-06-28 09:21:37` | `cowrie.login.success` |
| `2026-06-28 09:21:38` | `cowrie.session.params` |
| `2026-06-28 09:21:38` | `cowrie.command.input` |
| `2026-06-28 09:21:39` | `cowrie.log.closed` |
| `2026-06-28 09:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a01ad3dd949c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:21 |
| **Last Seen** | 2026-06-28 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:21:44` | `cowrie.session.connect` |
| `2026-06-28 09:21:44` | `cowrie.client.version` |
| `2026-06-28 09:21:44` | `cowrie.client.kex` |
| `2026-06-28 09:21:44` | `cowrie.login.success` |
| `2026-06-28 09:21:45` | `cowrie.session.params` |
| `2026-06-28 09:21:45` | `cowrie.command.input` |
| `2026-06-28 09:21:45` | `cowrie.log.closed` |
| `2026-06-28 09:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3063c5a541

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:22 |
| **Last Seen** | 2026-06-28 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:22:47` | `cowrie.session.connect` |
| `2026-06-28 09:22:47` | `cowrie.client.version` |
| `2026-06-28 09:22:47` | `cowrie.client.kex` |
| `2026-06-28 09:22:47` | `cowrie.login.success` |
| `2026-06-28 09:22:48` | `cowrie.session.params` |
| `2026-06-28 09:22:48` | `cowrie.command.input` |
| `2026-06-28 09:22:48` | `cowrie.log.closed` |
| `2026-06-28 09:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce6b76e026b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:23 |
| **Last Seen** | 2026-06-28 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:23:48` | `cowrie.session.connect` |
| `2026-06-28 09:23:48` | `cowrie.client.version` |
| `2026-06-28 09:23:48` | `cowrie.client.kex` |
| `2026-06-28 09:23:48` | `cowrie.login.success` |
| `2026-06-28 09:23:49` | `cowrie.session.params` |
| `2026-06-28 09:23:49` | `cowrie.command.input` |
| `2026-06-28 09:23:49` | `cowrie.log.closed` |
| `2026-06-28 09:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2720a7019e43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:24 |
| **Last Seen** | 2026-06-28 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:24:48` | `cowrie.session.connect` |
| `2026-06-28 09:24:48` | `cowrie.client.version` |
| `2026-06-28 09:24:49` | `cowrie.client.kex` |
| `2026-06-28 09:24:49` | `cowrie.login.success` |
| `2026-06-28 09:24:50` | `cowrie.session.params` |
| `2026-06-28 09:24:50` | `cowrie.command.input` |
| `2026-06-28 09:24:50` | `cowrie.log.closed` |
| `2026-06-28 09:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe12c5362295

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:25 |
| **Last Seen** | 2026-06-28 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:25:48` | `cowrie.session.connect` |
| `2026-06-28 09:25:48` | `cowrie.client.version` |
| `2026-06-28 09:25:48` | `cowrie.client.kex` |
| `2026-06-28 09:25:49` | `cowrie.login.success` |
| `2026-06-28 09:25:50` | `cowrie.session.params` |
| `2026-06-28 09:25:50` | `cowrie.command.input` |
| `2026-06-28 09:25:50` | `cowrie.log.closed` |
| `2026-06-28 09:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff6b9432ec3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 09:26 |
| **Last Seen** | 2026-06-28 09:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:26:15` | `cowrie.session.connect` |
| `2026-06-28 09:26:16` | `cowrie.client.version` |
| `2026-06-28 09:26:16` | `cowrie.client.kex` |
| `2026-06-28 09:26:23` | `cowrie.login.success` |
| `2026-06-28 09:26:25` | `cowrie.session.params` |
| `2026-06-28 09:26:25` | `cowrie.command.input` |
| `2026-06-28 09:26:27` | `cowrie.log.closed` |
| `2026-06-28 09:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19786121da8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:26 |
| **Last Seen** | 2026-06-28 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:26:51` | `cowrie.session.connect` |
| `2026-06-28 09:26:51` | `cowrie.client.version` |
| `2026-06-28 09:26:51` | `cowrie.client.kex` |
| `2026-06-28 09:26:51` | `cowrie.login.success` |
| `2026-06-28 09:26:52` | `cowrie.session.params` |
| `2026-06-28 09:26:52` | `cowrie.command.input` |
| `2026-06-28 09:26:52` | `cowrie.log.closed` |
| `2026-06-28 09:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e975fb5f6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:27 |
| **Last Seen** | 2026-06-28 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:27:53` | `cowrie.session.connect` |
| `2026-06-28 09:27:53` | `cowrie.client.version` |
| `2026-06-28 09:27:53` | `cowrie.client.kex` |
| `2026-06-28 09:27:54` | `cowrie.login.success` |
| `2026-06-28 09:27:55` | `cowrie.session.params` |
| `2026-06-28 09:27:55` | `cowrie.command.input` |
| `2026-06-28 09:27:55` | `cowrie.log.closed` |
| `2026-06-28 09:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a909cf5cc43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:28 |
| **Last Seen** | 2026-06-28 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:28:56` | `cowrie.session.connect` |
| `2026-06-28 09:28:56` | `cowrie.client.version` |
| `2026-06-28 09:28:56` | `cowrie.client.kex` |
| `2026-06-28 09:28:57` | `cowrie.login.success` |
| `2026-06-28 09:28:57` | `cowrie.session.params` |
| `2026-06-28 09:28:57` | `cowrie.command.input` |
| `2026-06-28 09:28:57` | `cowrie.log.closed` |
| `2026-06-28 09:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b92efd97e4c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:29 |
| **Last Seen** | 2026-06-28 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:29:57` | `cowrie.session.connect` |
| `2026-06-28 09:29:57` | `cowrie.client.version` |
| `2026-06-28 09:29:57` | `cowrie.client.kex` |
| `2026-06-28 09:29:58` | `cowrie.login.success` |
| `2026-06-28 09:29:58` | `cowrie.session.params` |
| `2026-06-28 09:29:58` | `cowrie.command.input` |
| `2026-06-28 09:29:59` | `cowrie.log.closed` |
| `2026-06-28 09:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a622e3dd44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:30 |
| **Last Seen** | 2026-06-28 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:30:58` | `cowrie.session.connect` |
| `2026-06-28 09:30:58` | `cowrie.client.version` |
| `2026-06-28 09:30:58` | `cowrie.client.kex` |
| `2026-06-28 09:30:58` | `cowrie.login.success` |
| `2026-06-28 09:30:59` | `cowrie.session.params` |
| `2026-06-28 09:30:59` | `cowrie.command.input` |
| `2026-06-28 09:30:59` | `cowrie.log.closed` |
| `2026-06-28 09:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a15be8fcf95

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:31 |
| **Last Seen** | 2026-06-28 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:31:58` | `cowrie.session.connect` |
| `2026-06-28 09:31:58` | `cowrie.client.version` |
| `2026-06-28 09:31:58` | `cowrie.client.kex` |
| `2026-06-28 09:31:58` | `cowrie.login.success` |
| `2026-06-28 09:31:59` | `cowrie.session.params` |
| `2026-06-28 09:31:59` | `cowrie.command.input` |
| `2026-06-28 09:31:59` | `cowrie.log.closed` |
| `2026-06-28 09:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7c25259b2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:33 |
| **Last Seen** | 2026-06-28 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:33:00` | `cowrie.session.connect` |
| `2026-06-28 09:33:00` | `cowrie.client.version` |
| `2026-06-28 09:33:00` | `cowrie.client.kex` |
| `2026-06-28 09:33:01` | `cowrie.login.success` |
| `2026-06-28 09:33:01` | `cowrie.session.params` |
| `2026-06-28 09:33:01` | `cowrie.command.input` |
| `2026-06-28 09:33:02` | `cowrie.log.closed` |
| `2026-06-28 09:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2864145094

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:34 |
| **Last Seen** | 2026-06-28 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:34:04` | `cowrie.session.connect` |
| `2026-06-28 09:34:04` | `cowrie.client.version` |
| `2026-06-28 09:34:04` | `cowrie.client.kex` |
| `2026-06-28 09:34:04` | `cowrie.login.success` |
| `2026-06-28 09:34:05` | `cowrie.session.params` |
| `2026-06-28 09:34:05` | `cowrie.command.input` |
| `2026-06-28 09:34:05` | `cowrie.log.closed` |
| `2026-06-28 09:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52a9c0e107b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:35 |
| **Last Seen** | 2026-06-28 09:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:35:07` | `cowrie.session.connect` |
| `2026-06-28 09:35:07` | `cowrie.client.version` |
| `2026-06-28 09:35:07` | `cowrie.client.kex` |
| `2026-06-28 09:35:07` | `cowrie.login.success` |
| `2026-06-28 09:35:08` | `cowrie.session.params` |
| `2026-06-28 09:35:08` | `cowrie.command.input` |
| `2026-06-28 09:35:08` | `cowrie.log.closed` |
| `2026-06-28 09:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfac3c957ef8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:36 |
| **Last Seen** | 2026-06-28 09:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:36:13` | `cowrie.session.connect` |
| `2026-06-28 09:36:13` | `cowrie.client.version` |
| `2026-06-28 09:36:13` | `cowrie.client.kex` |
| `2026-06-28 09:36:14` | `cowrie.login.success` |
| `2026-06-28 09:36:16` | `cowrie.session.params` |
| `2026-06-28 09:36:16` | `cowrie.command.input` |
| `2026-06-28 09:36:16` | `cowrie.log.closed` |
| `2026-06-28 09:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef2ccb86d0f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 09:36 |
| **Last Seen** | 2026-06-28 09:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:36:19` | `cowrie.session.connect` |
| `2026-06-28 09:36:19` | `cowrie.client.version` |
| `2026-06-28 09:36:19` | `cowrie.client.kex` |
| `2026-06-28 09:36:22` | `cowrie.login.success` |
| `2026-06-28 09:36:23` | `cowrie.session.params` |
| `2026-06-28 09:36:23` | `cowrie.command.input` |
| `2026-06-28 09:36:24` | `cowrie.log.closed` |
| `2026-06-28 09:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33d2777eec5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-28 09:37 |
| **Last Seen** | 2026-06-28 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:37:20` | `cowrie.session.connect` |
| `2026-06-28 09:37:20` | `cowrie.client.version` |
| `2026-06-28 09:37:20` | `cowrie.client.kex` |
| `2026-06-28 09:37:20` | `cowrie.login.success` |
| `2026-06-28 09:37:21` | `cowrie.session.params` |
| `2026-06-28 09:37:21` | `cowrie.command.input` |
| `2026-06-28 09:37:21` | `cowrie.log.closed` |
| `2026-06-28 09:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d909dfb4e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:37 |
| **Last Seen** | 2026-06-28 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:37:26` | `cowrie.session.connect` |
| `2026-06-28 09:37:26` | `cowrie.client.version` |
| `2026-06-28 09:37:26` | `cowrie.client.kex` |
| `2026-06-28 09:37:26` | `cowrie.login.success` |
| `2026-06-28 09:37:27` | `cowrie.session.params` |
| `2026-06-28 09:37:27` | `cowrie.command.input` |
| `2026-06-28 09:37:27` | `cowrie.log.closed` |
| `2026-06-28 09:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d81d5fdb88

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 09:37 |
| **Last Seen** | 2026-06-28 09:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:37:27` | `cowrie.session.connect` |
| `2026-06-28 09:37:28` | `cowrie.client.version` |
| `2026-06-28 09:37:28` | `cowrie.client.kex` |
| `2026-06-28 09:37:34` | `cowrie.login.success` |
| `2026-06-28 09:37:37` | `cowrie.session.params` |
| `2026-06-28 09:37:37` | `cowrie.command.input` |
| `2026-06-28 09:37:38` | `cowrie.log.closed` |
| `2026-06-28 09:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2137caf0e11

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:38 |
| **Last Seen** | 2026-06-28 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:38:28` | `cowrie.session.connect` |
| `2026-06-28 09:38:28` | `cowrie.client.version` |
| `2026-06-28 09:38:28` | `cowrie.client.kex` |
| `2026-06-28 09:38:28` | `cowrie.login.success` |
| `2026-06-28 09:38:29` | `cowrie.session.params` |
| `2026-06-28 09:38:29` | `cowrie.command.input` |
| `2026-06-28 09:38:29` | `cowrie.log.closed` |
| `2026-06-28 09:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4502fe48c04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:39 |
| **Last Seen** | 2026-06-28 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:39:32` | `cowrie.session.connect` |
| `2026-06-28 09:39:32` | `cowrie.client.version` |
| `2026-06-28 09:39:32` | `cowrie.client.kex` |
| `2026-06-28 09:39:32` | `cowrie.login.success` |
| `2026-06-28 09:39:33` | `cowrie.session.params` |
| `2026-06-28 09:39:33` | `cowrie.command.input` |
| `2026-06-28 09:39:33` | `cowrie.log.closed` |
| `2026-06-28 09:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d87a78322ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:40 |
| **Last Seen** | 2026-06-28 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:40:37` | `cowrie.session.connect` |
| `2026-06-28 09:40:37` | `cowrie.client.version` |
| `2026-06-28 09:40:38` | `cowrie.client.kex` |
| `2026-06-28 09:40:38` | `cowrie.login.success` |
| `2026-06-28 09:40:39` | `cowrie.session.params` |
| `2026-06-28 09:40:39` | `cowrie.command.input` |
| `2026-06-28 09:40:39` | `cowrie.log.closed` |
| `2026-06-28 09:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f6c70f86029

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:41 |
| **Last Seen** | 2026-06-28 09:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:41:43` | `cowrie.session.connect` |
| `2026-06-28 09:41:43` | `cowrie.client.version` |
| `2026-06-28 09:41:43` | `cowrie.client.kex` |
| `2026-06-28 09:41:43` | `cowrie.login.success` |
| `2026-06-28 09:41:44` | `cowrie.session.params` |
| `2026-06-28 09:41:44` | `cowrie.command.input` |
| `2026-06-28 09:41:44` | `cowrie.log.closed` |
| `2026-06-28 09:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c4908f7b47d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:42 |
| **Last Seen** | 2026-06-28 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:42:49` | `cowrie.session.connect` |
| `2026-06-28 09:42:49` | `cowrie.client.version` |
| `2026-06-28 09:42:49` | `cowrie.client.kex` |
| `2026-06-28 09:42:49` | `cowrie.login.success` |
| `2026-06-28 09:42:50` | `cowrie.session.params` |
| `2026-06-28 09:42:50` | `cowrie.command.input` |
| `2026-06-28 09:42:50` | `cowrie.log.closed` |
| `2026-06-28 09:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a83a394ab3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:43 |
| **Last Seen** | 2026-06-28 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:43:52` | `cowrie.session.connect` |
| `2026-06-28 09:43:52` | `cowrie.client.version` |
| `2026-06-28 09:43:52` | `cowrie.client.kex` |
| `2026-06-28 09:43:52` | `cowrie.login.success` |
| `2026-06-28 09:43:53` | `cowrie.session.params` |
| `2026-06-28 09:43:53` | `cowrie.command.input` |
| `2026-06-28 09:43:53` | `cowrie.log.closed` |
| `2026-06-28 09:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52b75fde030

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:44 |
| **Last Seen** | 2026-06-28 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:44:55` | `cowrie.session.connect` |
| `2026-06-28 09:44:55` | `cowrie.client.version` |
| `2026-06-28 09:44:55` | `cowrie.client.kex` |
| `2026-06-28 09:44:55` | `cowrie.login.success` |
| `2026-06-28 09:44:56` | `cowrie.session.params` |
| `2026-06-28 09:44:56` | `cowrie.command.input` |
| `2026-06-28 09:44:56` | `cowrie.log.closed` |
| `2026-06-28 09:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5506c913a46f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:45 |
| **Last Seen** | 2026-06-28 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:45:59` | `cowrie.session.connect` |
| `2026-06-28 09:45:59` | `cowrie.client.version` |
| `2026-06-28 09:45:59` | `cowrie.client.kex` |
| `2026-06-28 09:46:00` | `cowrie.login.success` |
| `2026-06-28 09:46:01` | `cowrie.session.params` |
| `2026-06-28 09:46:01` | `cowrie.command.input` |
| `2026-06-28 09:46:01` | `cowrie.log.closed` |
| `2026-06-28 09:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2a10561a44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:47 |
| **Last Seen** | 2026-06-28 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:47:05` | `cowrie.session.connect` |
| `2026-06-28 09:47:05` | `cowrie.client.version` |
| `2026-06-28 09:47:06` | `cowrie.client.kex` |
| `2026-06-28 09:47:06` | `cowrie.login.success` |
| `2026-06-28 09:47:07` | `cowrie.session.params` |
| `2026-06-28 09:47:07` | `cowrie.command.input` |
| `2026-06-28 09:47:07` | `cowrie.log.closed` |
| `2026-06-28 09:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa856f2edb51

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:48 |
| **Last Seen** | 2026-06-28 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:48:12` | `cowrie.session.connect` |
| `2026-06-28 09:48:12` | `cowrie.client.version` |
| `2026-06-28 09:48:12` | `cowrie.client.kex` |
| `2026-06-28 09:48:12` | `cowrie.login.success` |
| `2026-06-28 09:48:13` | `cowrie.session.params` |
| `2026-06-28 09:48:13` | `cowrie.command.input` |
| `2026-06-28 09:48:13` | `cowrie.log.closed` |
| `2026-06-28 09:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5e0bbf2a3b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 09:49 |
| **Last Seen** | 2026-06-28 09:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:49:04` | `cowrie.session.connect` |
| `2026-06-28 09:49:05` | `cowrie.client.version` |
| `2026-06-28 09:49:05` | `cowrie.client.kex` |
| `2026-06-28 09:49:12` | `cowrie.login.success` |
| `2026-06-28 09:49:15` | `cowrie.session.params` |
| `2026-06-28 09:49:15` | `cowrie.command.input` |
| `2026-06-28 09:49:17` | `cowrie.log.closed` |
| `2026-06-28 09:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e9a2ae2510

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:49 |
| **Last Seen** | 2026-06-28 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:49:17` | `cowrie.session.connect` |
| `2026-06-28 09:49:17` | `cowrie.client.version` |
| `2026-06-28 09:49:17` | `cowrie.client.kex` |
| `2026-06-28 09:49:17` | `cowrie.login.success` |
| `2026-06-28 09:49:18` | `cowrie.session.params` |
| `2026-06-28 09:49:18` | `cowrie.command.input` |
| `2026-06-28 09:49:18` | `cowrie.log.closed` |
| `2026-06-28 09:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a639ae7019e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:50 |
| **Last Seen** | 2026-06-28 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:50:22` | `cowrie.session.connect` |
| `2026-06-28 09:50:22` | `cowrie.client.version` |
| `2026-06-28 09:50:22` | `cowrie.client.kex` |
| `2026-06-28 09:50:22` | `cowrie.login.success` |
| `2026-06-28 09:50:23` | `cowrie.session.params` |
| `2026-06-28 09:50:23` | `cowrie.command.input` |
| `2026-06-28 09:50:23` | `cowrie.log.closed` |
| `2026-06-28 09:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69da7dd6e6e9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 09:51 |
| **Last Seen** | 2026-06-28 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:51:03` | `cowrie.session.connect` |
| `2026-06-28 09:51:03` | `cowrie.client.version` |
| `2026-06-28 09:51:03` | `cowrie.client.kex` |
| `2026-06-28 09:51:05` | `cowrie.login.success` |
| `2026-06-28 09:51:06` | `cowrie.session.params` |
| `2026-06-28 09:51:06` | `cowrie.command.input` |
| `2026-06-28 09:51:07` | `cowrie.log.closed` |
| `2026-06-28 09:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0e7a6d1d69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:51 |
| **Last Seen** | 2026-06-28 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:51:26` | `cowrie.session.connect` |
| `2026-06-28 09:51:26` | `cowrie.client.version` |
| `2026-06-28 09:51:26` | `cowrie.client.kex` |
| `2026-06-28 09:51:26` | `cowrie.login.success` |
| `2026-06-28 09:51:27` | `cowrie.session.params` |
| `2026-06-28 09:51:27` | `cowrie.command.input` |
| `2026-06-28 09:51:27` | `cowrie.log.closed` |
| `2026-06-28 09:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-682b99e4cac7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:52 |
| **Last Seen** | 2026-06-28 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:52:32` | `cowrie.session.connect` |
| `2026-06-28 09:52:32` | `cowrie.client.version` |
| `2026-06-28 09:52:32` | `cowrie.client.kex` |
| `2026-06-28 09:52:32` | `cowrie.login.success` |
| `2026-06-28 09:52:33` | `cowrie.session.params` |
| `2026-06-28 09:52:33` | `cowrie.command.input` |
| `2026-06-28 09:52:33` | `cowrie.log.closed` |
| `2026-06-28 09:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e368342f91b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:53 |
| **Last Seen** | 2026-06-28 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:53:39` | `cowrie.session.connect` |
| `2026-06-28 09:53:39` | `cowrie.client.version` |
| `2026-06-28 09:53:39` | `cowrie.client.kex` |
| `2026-06-28 09:53:40` | `cowrie.login.success` |
| `2026-06-28 09:53:41` | `cowrie.session.params` |
| `2026-06-28 09:53:41` | `cowrie.command.input` |
| `2026-06-28 09:53:41` | `cowrie.log.closed` |
| `2026-06-28 09:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9423f2fe103a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:54 |
| **Last Seen** | 2026-06-28 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:54:46` | `cowrie.session.connect` |
| `2026-06-28 09:54:46` | `cowrie.client.version` |
| `2026-06-28 09:54:46` | `cowrie.client.kex` |
| `2026-06-28 09:54:47` | `cowrie.login.success` |
| `2026-06-28 09:54:48` | `cowrie.session.params` |
| `2026-06-28 09:54:48` | `cowrie.command.input` |
| `2026-06-28 09:54:48` | `cowrie.log.closed` |
| `2026-06-28 09:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c873b77a034

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:55 |
| **Last Seen** | 2026-06-28 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:55:52` | `cowrie.session.connect` |
| `2026-06-28 09:55:52` | `cowrie.client.version` |
| `2026-06-28 09:55:52` | `cowrie.client.kex` |
| `2026-06-28 09:55:52` | `cowrie.login.success` |
| `2026-06-28 09:55:53` | `cowrie.session.params` |
| `2026-06-28 09:55:53` | `cowrie.command.input` |
| `2026-06-28 09:55:53` | `cowrie.log.closed` |
| `2026-06-28 09:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72127526c80b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 09:56 |
| **Last Seen** | 2026-06-28 09:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:56:22` | `cowrie.session.connect` |
| `2026-06-28 09:56:22` | `cowrie.client.version` |
| `2026-06-28 09:56:22` | `cowrie.client.kex` |
| `2026-06-28 09:56:22` | `cowrie.login.success` |
| `2026-06-28 09:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99dede714492

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 09:56 |
| **Last Seen** | 2026-06-28 09:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:56:22` | `cowrie.session.connect` |
| `2026-06-28 09:56:22` | `cowrie.client.version` |
| `2026-06-28 09:56:22` | `cowrie.client.kex` |
| `2026-06-28 09:56:22` | `cowrie.login.success` |
| `2026-06-28 09:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5977353c951a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 09:56 |
| **Last Seen** | 2026-06-28 09:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:56:28` | `cowrie.session.connect` |
| `2026-06-28 09:56:28` | `cowrie.client.version` |
| `2026-06-28 09:56:28` | `cowrie.client.kex` |
| `2026-06-28 09:56:28` | `cowrie.login.success` |
| `2026-06-28 09:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3382750fd255

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 09:56 |
| **Last Seen** | 2026-06-28 09:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:56:28` | `cowrie.session.connect` |
| `2026-06-28 09:56:28` | `cowrie.client.version` |
| `2026-06-28 09:56:28` | `cowrie.client.kex` |
| `2026-06-28 09:56:28` | `cowrie.login.success` |
| `2026-06-28 09:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1bd0e654c7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:56 |
| **Last Seen** | 2026-06-28 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:56:56` | `cowrie.session.connect` |
| `2026-06-28 09:56:56` | `cowrie.client.version` |
| `2026-06-28 09:56:56` | `cowrie.client.kex` |
| `2026-06-28 09:56:57` | `cowrie.login.success` |
| `2026-06-28 09:56:57` | `cowrie.session.params` |
| `2026-06-28 09:56:57` | `cowrie.command.input` |
| `2026-06-28 09:56:58` | `cowrie.log.closed` |
| `2026-06-28 09:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26d87e88443

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:58 |
| **Last Seen** | 2026-06-28 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:58:01` | `cowrie.session.connect` |
| `2026-06-28 09:58:01` | `cowrie.client.version` |
| `2026-06-28 09:58:01` | `cowrie.client.kex` |
| `2026-06-28 09:58:02` | `cowrie.login.success` |
| `2026-06-28 09:58:03` | `cowrie.session.params` |
| `2026-06-28 09:58:03` | `cowrie.command.input` |
| `2026-06-28 09:58:03` | `cowrie.log.closed` |
| `2026-06-28 09:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb80320cf58e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 09:59 |
| **Last Seen** | 2026-06-28 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 09:59:07` | `cowrie.session.connect` |
| `2026-06-28 09:59:07` | `cowrie.client.version` |
| `2026-06-28 09:59:07` | `cowrie.client.kex` |
| `2026-06-28 09:59:08` | `cowrie.login.success` |
| `2026-06-28 09:59:08` | `cowrie.session.params` |
| `2026-06-28 09:59:08` | `cowrie.command.input` |
| `2026-06-28 09:59:08` | `cowrie.log.closed` |
| `2026-06-28 09:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-818e7258124d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:00 |
| **Last Seen** | 2026-06-28 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:00:15` | `cowrie.session.connect` |
| `2026-06-28 10:00:15` | `cowrie.client.version` |
| `2026-06-28 10:00:15` | `cowrie.client.kex` |
| `2026-06-28 10:00:15` | `cowrie.login.success` |
| `2026-06-28 10:00:16` | `cowrie.session.params` |
| `2026-06-28 10:00:16` | `cowrie.command.input` |
| `2026-06-28 10:00:16` | `cowrie.log.closed` |
| `2026-06-28 10:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b1fe0b41c4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 10:00 |
| **Last Seen** | 2026-06-28 10:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:00:34` | `cowrie.session.connect` |
| `2026-06-28 10:00:36` | `cowrie.client.version` |
| `2026-06-28 10:00:36` | `cowrie.client.kex` |
| `2026-06-28 10:00:41` | `cowrie.login.success` |
| `2026-06-28 10:00:45` | `cowrie.session.params` |
| `2026-06-28 10:00:45` | `cowrie.command.input` |
| `2026-06-28 10:00:47` | `cowrie.log.closed` |
| `2026-06-28 10:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ea327475dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:01 |
| **Last Seen** | 2026-06-28 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:01:00` | `cowrie.session.connect` |
| `2026-06-28 10:01:00` | `cowrie.client.version` |
| `2026-06-28 10:01:00` | `cowrie.client.kex` |
| `2026-06-28 10:01:00` | `cowrie.login.success` |
| `2026-06-28 10:01:01` | `cowrie.session.params` |
| `2026-06-28 10:01:01` | `cowrie.command.input` |
| `2026-06-28 10:01:01` | `cowrie.log.closed` |
| `2026-06-28 10:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47ce82e4b8a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:01 |
| **Last Seen** | 2026-06-28 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:01:45` | `cowrie.session.connect` |
| `2026-06-28 10:01:45` | `cowrie.client.version` |
| `2026-06-28 10:01:45` | `cowrie.client.kex` |
| `2026-06-28 10:01:46` | `cowrie.login.success` |
| `2026-06-28 10:01:46` | `cowrie.session.params` |
| `2026-06-28 10:01:46` | `cowrie.command.input` |
| `2026-06-28 10:01:47` | `cowrie.log.closed` |
| `2026-06-28 10:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4517908298

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:02 |
| **Last Seen** | 2026-06-28 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:02:30` | `cowrie.session.connect` |
| `2026-06-28 10:02:30` | `cowrie.client.version` |
| `2026-06-28 10:02:30` | `cowrie.client.kex` |
| `2026-06-28 10:02:30` | `cowrie.login.success` |
| `2026-06-28 10:02:31` | `cowrie.session.params` |
| `2026-06-28 10:02:31` | `cowrie.command.input` |
| `2026-06-28 10:02:31` | `cowrie.log.closed` |
| `2026-06-28 10:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5619bb82672b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:03 |
| **Last Seen** | 2026-06-28 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:03:14` | `cowrie.session.connect` |
| `2026-06-28 10:03:14` | `cowrie.client.version` |
| `2026-06-28 10:03:14` | `cowrie.client.kex` |
| `2026-06-28 10:03:14` | `cowrie.login.success` |
| `2026-06-28 10:03:15` | `cowrie.session.params` |
| `2026-06-28 10:03:15` | `cowrie.command.input` |
| `2026-06-28 10:03:15` | `cowrie.log.closed` |
| `2026-06-28 10:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66bd22b9d02e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:03 |
| **Last Seen** | 2026-06-28 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:03:58` | `cowrie.session.connect` |
| `2026-06-28 10:03:58` | `cowrie.client.version` |
| `2026-06-28 10:03:58` | `cowrie.client.kex` |
| `2026-06-28 10:03:58` | `cowrie.login.success` |
| `2026-06-28 10:03:59` | `cowrie.session.params` |
| `2026-06-28 10:03:59` | `cowrie.command.input` |
| `2026-06-28 10:03:59` | `cowrie.log.closed` |
| `2026-06-28 10:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55be91b67bb3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:04 |
| **Last Seen** | 2026-06-28 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:04:42` | `cowrie.session.connect` |
| `2026-06-28 10:04:42` | `cowrie.client.version` |
| `2026-06-28 10:04:42` | `cowrie.client.kex` |
| `2026-06-28 10:04:42` | `cowrie.login.success` |
| `2026-06-28 10:04:43` | `cowrie.session.params` |
| `2026-06-28 10:04:43` | `cowrie.command.input` |
| `2026-06-28 10:04:43` | `cowrie.log.closed` |
| `2026-06-28 10:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abbbb30041b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:05 |
| **Last Seen** | 2026-06-28 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:05:27` | `cowrie.session.connect` |
| `2026-06-28 10:05:27` | `cowrie.client.version` |
| `2026-06-28 10:05:28` | `cowrie.client.kex` |
| `2026-06-28 10:05:28` | `cowrie.login.success` |
| `2026-06-28 10:05:29` | `cowrie.session.params` |
| `2026-06-28 10:05:29` | `cowrie.command.input` |
| `2026-06-28 10:05:29` | `cowrie.log.closed` |
| `2026-06-28 10:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2de18ff17a2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 10:05 |
| **Last Seen** | 2026-06-28 10:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:05:44` | `cowrie.session.connect` |
| `2026-06-28 10:05:44` | `cowrie.client.version` |
| `2026-06-28 10:05:44` | `cowrie.client.kex` |
| `2026-06-28 10:05:46` | `cowrie.login.success` |
| `2026-06-28 10:05:47` | `cowrie.session.params` |
| `2026-06-28 10:05:47` | `cowrie.command.input` |
| `2026-06-28 10:05:48` | `cowrie.log.closed` |
| `2026-06-28 10:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b368bd4dab5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:06 |
| **Last Seen** | 2026-06-28 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:06:14` | `cowrie.session.connect` |
| `2026-06-28 10:06:14` | `cowrie.client.version` |
| `2026-06-28 10:06:14` | `cowrie.client.kex` |
| `2026-06-28 10:06:14` | `cowrie.login.success` |
| `2026-06-28 10:06:15` | `cowrie.session.params` |
| `2026-06-28 10:06:15` | `cowrie.command.input` |
| `2026-06-28 10:06:15` | `cowrie.log.closed` |
| `2026-06-28 10:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e817e9cfe9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:07 |
| **Last Seen** | 2026-06-28 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:07:01` | `cowrie.session.connect` |
| `2026-06-28 10:07:01` | `cowrie.client.version` |
| `2026-06-28 10:07:01` | `cowrie.client.kex` |
| `2026-06-28 10:07:02` | `cowrie.login.success` |
| `2026-06-28 10:07:02` | `cowrie.session.params` |
| `2026-06-28 10:07:02` | `cowrie.command.input` |
| `2026-06-28 10:07:02` | `cowrie.log.closed` |
| `2026-06-28 10:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179345c47af0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:07 |
| **Last Seen** | 2026-06-28 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:07:49` | `cowrie.session.connect` |
| `2026-06-28 10:07:49` | `cowrie.client.version` |
| `2026-06-28 10:07:49` | `cowrie.client.kex` |
| `2026-06-28 10:07:49` | `cowrie.login.success` |
| `2026-06-28 10:07:50` | `cowrie.session.params` |
| `2026-06-28 10:07:50` | `cowrie.command.input` |
| `2026-06-28 10:07:50` | `cowrie.log.closed` |
| `2026-06-28 10:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70360ce160df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:08 |
| **Last Seen** | 2026-06-28 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:08:35` | `cowrie.session.connect` |
| `2026-06-28 10:08:35` | `cowrie.client.version` |
| `2026-06-28 10:08:35` | `cowrie.client.kex` |
| `2026-06-28 10:08:36` | `cowrie.login.success` |
| `2026-06-28 10:08:36` | `cowrie.session.params` |
| `2026-06-28 10:08:36` | `cowrie.command.input` |
| `2026-06-28 10:08:36` | `cowrie.log.closed` |
| `2026-06-28 10:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42713d93f576

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:09 |
| **Last Seen** | 2026-06-28 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:09:21` | `cowrie.session.connect` |
| `2026-06-28 10:09:21` | `cowrie.client.version` |
| `2026-06-28 10:09:21` | `cowrie.client.kex` |
| `2026-06-28 10:09:22` | `cowrie.login.success` |
| `2026-06-28 10:09:23` | `cowrie.session.params` |
| `2026-06-28 10:09:23` | `cowrie.command.input` |
| `2026-06-28 10:09:23` | `cowrie.log.closed` |
| `2026-06-28 10:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da48181ae124

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:10 |
| **Last Seen** | 2026-06-28 10:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:10:08` | `cowrie.session.connect` |
| `2026-06-28 10:10:08` | `cowrie.client.version` |
| `2026-06-28 10:10:08` | `cowrie.client.kex` |
| `2026-06-28 10:10:08` | `cowrie.login.success` |
| `2026-06-28 10:10:09` | `cowrie.session.params` |
| `2026-06-28 10:10:09` | `cowrie.command.input` |
| `2026-06-28 10:10:09` | `cowrie.log.closed` |
| `2026-06-28 10:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500544f3eb05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:10 |
| **Last Seen** | 2026-06-28 10:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:10:55` | `cowrie.session.connect` |
| `2026-06-28 10:10:55` | `cowrie.client.version` |
| `2026-06-28 10:10:55` | `cowrie.client.kex` |
| `2026-06-28 10:10:56` | `cowrie.login.success` |
| `2026-06-28 10:10:56` | `cowrie.session.params` |
| `2026-06-28 10:10:56` | `cowrie.command.input` |
| `2026-06-28 10:10:56` | `cowrie.log.closed` |
| `2026-06-28 10:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-345e5e9fda35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:11 |
| **Last Seen** | 2026-06-28 10:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:11:43` | `cowrie.session.connect` |
| `2026-06-28 10:11:43` | `cowrie.client.version` |
| `2026-06-28 10:11:43` | `cowrie.client.kex` |
| `2026-06-28 10:11:44` | `cowrie.login.success` |
| `2026-06-28 10:11:45` | `cowrie.session.params` |
| `2026-06-28 10:11:45` | `cowrie.command.input` |
| `2026-06-28 10:11:45` | `cowrie.log.closed` |
| `2026-06-28 10:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbaff88038ca

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 10:12 |
| **Last Seen** | 2026-06-28 10:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:12:02` | `cowrie.session.connect` |
| `2026-06-28 10:12:04` | `cowrie.client.version` |
| `2026-06-28 10:12:04` | `cowrie.client.kex` |
| `2026-06-28 10:12:10` | `cowrie.login.success` |
| `2026-06-28 10:12:13` | `cowrie.session.params` |
| `2026-06-28 10:12:13` | `cowrie.command.input` |
| `2026-06-28 10:12:15` | `cowrie.log.closed` |
| `2026-06-28 10:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a5356ccd41

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:12 |
| **Last Seen** | 2026-06-28 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:12:32` | `cowrie.session.connect` |
| `2026-06-28 10:12:32` | `cowrie.client.version` |
| `2026-06-28 10:12:32` | `cowrie.client.kex` |
| `2026-06-28 10:12:32` | `cowrie.login.success` |
| `2026-06-28 10:12:33` | `cowrie.session.params` |
| `2026-06-28 10:12:33` | `cowrie.command.input` |
| `2026-06-28 10:12:33` | `cowrie.log.closed` |
| `2026-06-28 10:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10887b2aa4e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:13 |
| **Last Seen** | 2026-06-28 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:13:20` | `cowrie.session.connect` |
| `2026-06-28 10:13:20` | `cowrie.client.version` |
| `2026-06-28 10:13:20` | `cowrie.client.kex` |
| `2026-06-28 10:13:21` | `cowrie.login.success` |
| `2026-06-28 10:13:22` | `cowrie.session.params` |
| `2026-06-28 10:13:22` | `cowrie.command.input` |
| `2026-06-28 10:13:22` | `cowrie.log.closed` |
| `2026-06-28 10:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f10ed70b52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:14 |
| **Last Seen** | 2026-06-28 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:14:56` | `cowrie.session.connect` |
| `2026-06-28 10:14:56` | `cowrie.client.version` |
| `2026-06-28 10:14:57` | `cowrie.client.kex` |
| `2026-06-28 10:14:57` | `cowrie.login.success` |
| `2026-06-28 10:14:58` | `cowrie.session.params` |
| `2026-06-28 10:14:58` | `cowrie.command.input` |
| `2026-06-28 10:14:58` | `cowrie.log.closed` |
| `2026-06-28 10:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7177bf0792

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:15 |
| **Last Seen** | 2026-06-28 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:15:43` | `cowrie.session.connect` |
| `2026-06-28 10:15:43` | `cowrie.client.version` |
| `2026-06-28 10:15:43` | `cowrie.client.kex` |
| `2026-06-28 10:15:44` | `cowrie.login.success` |
| `2026-06-28 10:15:44` | `cowrie.session.params` |
| `2026-06-28 10:15:44` | `cowrie.command.input` |
| `2026-06-28 10:15:44` | `cowrie.log.closed` |
| `2026-06-28 10:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-735d571e4c9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:16 |
| **Last Seen** | 2026-06-28 10:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:16:31` | `cowrie.session.connect` |
| `2026-06-28 10:16:31` | `cowrie.client.version` |
| `2026-06-28 10:16:31` | `cowrie.client.kex` |
| `2026-06-28 10:16:31` | `cowrie.login.success` |
| `2026-06-28 10:16:32` | `cowrie.session.params` |
| `2026-06-28 10:16:32` | `cowrie.command.input` |
| `2026-06-28 10:16:32` | `cowrie.log.closed` |
| `2026-06-28 10:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1080882b68e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:17 |
| **Last Seen** | 2026-06-28 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:17:18` | `cowrie.session.connect` |
| `2026-06-28 10:17:18` | `cowrie.client.version` |
| `2026-06-28 10:17:18` | `cowrie.client.kex` |
| `2026-06-28 10:17:19` | `cowrie.login.success` |
| `2026-06-28 10:17:20` | `cowrie.session.params` |
| `2026-06-28 10:17:20` | `cowrie.command.input` |
| `2026-06-28 10:17:20` | `cowrie.log.closed` |
| `2026-06-28 10:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff2dea994368

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:18 |
| **Last Seen** | 2026-06-28 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:18:07` | `cowrie.session.connect` |
| `2026-06-28 10:18:07` | `cowrie.client.version` |
| `2026-06-28 10:18:07` | `cowrie.client.kex` |
| `2026-06-28 10:18:07` | `cowrie.login.success` |
| `2026-06-28 10:18:08` | `cowrie.session.params` |
| `2026-06-28 10:18:08` | `cowrie.command.input` |
| `2026-06-28 10:18:08` | `cowrie.log.closed` |
| `2026-06-28 10:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39288428ce35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:18 |
| **Last Seen** | 2026-06-28 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:18:57` | `cowrie.session.connect` |
| `2026-06-28 10:18:57` | `cowrie.client.version` |
| `2026-06-28 10:18:57` | `cowrie.client.kex` |
| `2026-06-28 10:18:58` | `cowrie.login.success` |
| `2026-06-28 10:18:58` | `cowrie.session.params` |
| `2026-06-28 10:18:58` | `cowrie.command.input` |
| `2026-06-28 10:18:59` | `cowrie.log.closed` |
| `2026-06-28 10:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49d6cc6b3096

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:19 |
| **Last Seen** | 2026-06-28 10:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:19:47` | `cowrie.session.connect` |
| `2026-06-28 10:19:47` | `cowrie.client.version` |
| `2026-06-28 10:19:47` | `cowrie.client.kex` |
| `2026-06-28 10:19:47` | `cowrie.login.success` |
| `2026-06-28 10:19:48` | `cowrie.session.params` |
| `2026-06-28 10:19:48` | `cowrie.command.input` |
| `2026-06-28 10:19:48` | `cowrie.log.closed` |
| `2026-06-28 10:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368254c16ea9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 10:20 |
| **Last Seen** | 2026-06-28 10:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:20:30` | `cowrie.session.connect` |
| `2026-06-28 10:20:31` | `cowrie.client.version` |
| `2026-06-28 10:20:31` | `cowrie.client.kex` |
| `2026-06-28 10:20:32` | `cowrie.login.success` |
| `2026-06-28 10:20:34` | `cowrie.session.params` |
| `2026-06-28 10:20:34` | `cowrie.command.input` |
| `2026-06-28 10:20:35` | `cowrie.log.closed` |
| `2026-06-28 10:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b08ee1aa61e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:20 |
| **Last Seen** | 2026-06-28 10:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:20:37` | `cowrie.session.connect` |
| `2026-06-28 10:20:37` | `cowrie.client.version` |
| `2026-06-28 10:20:37` | `cowrie.client.kex` |
| `2026-06-28 10:20:38` | `cowrie.login.success` |
| `2026-06-28 10:20:38` | `cowrie.session.params` |
| `2026-06-28 10:20:38` | `cowrie.command.input` |
| `2026-06-28 10:20:38` | `cowrie.log.closed` |
| `2026-06-28 10:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a01c9eb9d2c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:21 |
| **Last Seen** | 2026-06-28 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:21:26` | `cowrie.session.connect` |
| `2026-06-28 10:21:26` | `cowrie.client.version` |
| `2026-06-28 10:21:26` | `cowrie.client.kex` |
| `2026-06-28 10:21:26` | `cowrie.login.success` |
| `2026-06-28 10:21:27` | `cowrie.session.params` |
| `2026-06-28 10:21:27` | `cowrie.command.input` |
| `2026-06-28 10:21:27` | `cowrie.log.closed` |
| `2026-06-28 10:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e723240eccf6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:22 |
| **Last Seen** | 2026-06-28 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:22:14` | `cowrie.session.connect` |
| `2026-06-28 10:22:14` | `cowrie.client.version` |
| `2026-06-28 10:22:14` | `cowrie.client.kex` |
| `2026-06-28 10:22:15` | `cowrie.login.success` |
| `2026-06-28 10:22:16` | `cowrie.session.params` |
| `2026-06-28 10:22:16` | `cowrie.command.input` |
| `2026-06-28 10:22:16` | `cowrie.log.closed` |
| `2026-06-28 10:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0bb4c596be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:23 |
| **Last Seen** | 2026-06-28 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:23:02` | `cowrie.session.connect` |
| `2026-06-28 10:23:02` | `cowrie.client.version` |
| `2026-06-28 10:23:02` | `cowrie.client.kex` |
| `2026-06-28 10:23:02` | `cowrie.login.success` |
| `2026-06-28 10:23:03` | `cowrie.session.params` |
| `2026-06-28 10:23:03` | `cowrie.command.input` |
| `2026-06-28 10:23:03` | `cowrie.log.closed` |
| `2026-06-28 10:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed4ad3ee64ea

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 10:23 |
| **Last Seen** | 2026-06-28 10:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:23:41` | `cowrie.session.connect` |
| `2026-06-28 10:23:42` | `cowrie.client.version` |
| `2026-06-28 10:23:42` | `cowrie.client.kex` |
| `2026-06-28 10:23:48` | `cowrie.login.success` |
| `2026-06-28 10:23:53` | `cowrie.session.params` |
| `2026-06-28 10:23:53` | `cowrie.command.input` |
| `2026-06-28 10:23:54` | `cowrie.log.closed` |
| `2026-06-28 10:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-062b144d8036

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:23 |
| **Last Seen** | 2026-06-28 10:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:23:51` | `cowrie.session.connect` |
| `2026-06-28 10:23:51` | `cowrie.client.version` |
| `2026-06-28 10:23:51` | `cowrie.client.kex` |
| `2026-06-28 10:23:51` | `cowrie.login.success` |
| `2026-06-28 10:23:52` | `cowrie.session.params` |
| `2026-06-28 10:23:52` | `cowrie.command.input` |
| `2026-06-28 10:23:53` | `cowrie.log.closed` |
| `2026-06-28 10:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d1bc144df5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:24 |
| **Last Seen** | 2026-06-28 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:24:41` | `cowrie.session.connect` |
| `2026-06-28 10:24:41` | `cowrie.client.version` |
| `2026-06-28 10:24:41` | `cowrie.client.kex` |
| `2026-06-28 10:24:42` | `cowrie.login.success` |
| `2026-06-28 10:24:42` | `cowrie.session.params` |
| `2026-06-28 10:24:42` | `cowrie.command.input` |
| `2026-06-28 10:24:42` | `cowrie.log.closed` |
| `2026-06-28 10:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fa5e6753bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:25 |
| **Last Seen** | 2026-06-28 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:25:33` | `cowrie.session.connect` |
| `2026-06-28 10:25:33` | `cowrie.client.version` |
| `2026-06-28 10:25:33` | `cowrie.client.kex` |
| `2026-06-28 10:25:34` | `cowrie.login.success` |
| `2026-06-28 10:25:35` | `cowrie.session.params` |
| `2026-06-28 10:25:35` | `cowrie.command.input` |
| `2026-06-28 10:25:35` | `cowrie.log.closed` |
| `2026-06-28 10:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680010a7ccaa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:26 |
| **Last Seen** | 2026-06-28 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:26:25` | `cowrie.session.connect` |
| `2026-06-28 10:26:25` | `cowrie.client.version` |
| `2026-06-28 10:26:25` | `cowrie.client.kex` |
| `2026-06-28 10:26:25` | `cowrie.login.success` |
| `2026-06-28 10:26:26` | `cowrie.session.params` |
| `2026-06-28 10:26:26` | `cowrie.command.input` |
| `2026-06-28 10:26:26` | `cowrie.log.closed` |
| `2026-06-28 10:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe97e5381c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:27 |
| **Last Seen** | 2026-06-28 10:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:27:16` | `cowrie.session.connect` |
| `2026-06-28 10:27:16` | `cowrie.client.version` |
| `2026-06-28 10:27:16` | `cowrie.client.kex` |
| `2026-06-28 10:27:16` | `cowrie.login.success` |
| `2026-06-28 10:27:17` | `cowrie.session.params` |
| `2026-06-28 10:27:17` | `cowrie.command.input` |
| `2026-06-28 10:27:17` | `cowrie.log.closed` |
| `2026-06-28 10:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49359856ef9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:28 |
| **Last Seen** | 2026-06-28 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:28:06` | `cowrie.session.connect` |
| `2026-06-28 10:28:06` | `cowrie.client.version` |
| `2026-06-28 10:28:06` | `cowrie.client.kex` |
| `2026-06-28 10:28:06` | `cowrie.login.success` |
| `2026-06-28 10:28:07` | `cowrie.session.params` |
| `2026-06-28 10:28:07` | `cowrie.command.input` |
| `2026-06-28 10:28:07` | `cowrie.log.closed` |
| `2026-06-28 10:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7999c005153e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:28 |
| **Last Seen** | 2026-06-28 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:28:56` | `cowrie.session.connect` |
| `2026-06-28 10:28:56` | `cowrie.client.version` |
| `2026-06-28 10:28:56` | `cowrie.client.kex` |
| `2026-06-28 10:28:56` | `cowrie.login.success` |
| `2026-06-28 10:28:57` | `cowrie.session.params` |
| `2026-06-28 10:28:57` | `cowrie.command.input` |
| `2026-06-28 10:28:57` | `cowrie.log.closed` |
| `2026-06-28 10:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f28ec1a32f

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]229` |
| **First Seen** | 2026-06-28 10:29 |
| **Last Seen** | 2026-06-28 10:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:29:16` | `cowrie.session.connect` |
| `2026-06-28 10:29:16` | `cowrie.login.success` |
| `2026-06-28 10:29:17` | `cowrie.session.params` |
| `2026-06-28 10:29:17` | `cowrie.command.input` |
| `2026-06-28 10:29:17` | `cowrie.command.input` |
| `2026-06-28 10:29:17` | `cowrie.command.failed` |
| `2026-06-28 10:29:17` | `cowrie.command.input` |
| `2026-06-28 10:29:17` | `cowrie.command.failed` |
| `2026-06-28 10:29:17` | `cowrie.command.input` |
| `2026-06-28 10:29:17` | `cowrie.log.closed` |
| `2026-06-28 10:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]229` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bdb8b3b41a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:29 |
| **Last Seen** | 2026-06-28 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:29:46` | `cowrie.session.connect` |
| `2026-06-28 10:29:46` | `cowrie.client.version` |
| `2026-06-28 10:29:46` | `cowrie.client.kex` |
| `2026-06-28 10:29:46` | `cowrie.login.success` |
| `2026-06-28 10:29:47` | `cowrie.session.params` |
| `2026-06-28 10:29:47` | `cowrie.command.input` |
| `2026-06-28 10:29:47` | `cowrie.log.closed` |
| `2026-06-28 10:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9729071483

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:30 |
| **Last Seen** | 2026-06-28 10:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:30:37` | `cowrie.session.connect` |
| `2026-06-28 10:30:37` | `cowrie.client.version` |
| `2026-06-28 10:30:37` | `cowrie.client.kex` |
| `2026-06-28 10:30:38` | `cowrie.login.success` |
| `2026-06-28 10:30:38` | `cowrie.session.params` |
| `2026-06-28 10:30:38` | `cowrie.command.input` |
| `2026-06-28 10:30:39` | `cowrie.log.closed` |
| `2026-06-28 10:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9385ac53c502

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:31 |
| **Last Seen** | 2026-06-28 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:31:30` | `cowrie.session.connect` |
| `2026-06-28 10:31:30` | `cowrie.client.version` |
| `2026-06-28 10:31:30` | `cowrie.client.kex` |
| `2026-06-28 10:31:30` | `cowrie.login.success` |
| `2026-06-28 10:31:31` | `cowrie.session.params` |
| `2026-06-28 10:31:31` | `cowrie.command.input` |
| `2026-06-28 10:31:31` | `cowrie.log.closed` |
| `2026-06-28 10:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b7736e9a32a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:32 |
| **Last Seen** | 2026-06-28 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:32:23` | `cowrie.session.connect` |
| `2026-06-28 10:32:23` | `cowrie.client.version` |
| `2026-06-28 10:32:23` | `cowrie.client.kex` |
| `2026-06-28 10:32:24` | `cowrie.login.success` |
| `2026-06-28 10:32:25` | `cowrie.session.params` |
| `2026-06-28 10:32:25` | `cowrie.command.input` |
| `2026-06-28 10:32:25` | `cowrie.log.closed` |
| `2026-06-28 10:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37cf3a57ceb8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:33 |
| **Last Seen** | 2026-06-28 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:33:16` | `cowrie.session.connect` |
| `2026-06-28 10:33:16` | `cowrie.client.version` |
| `2026-06-28 10:33:16` | `cowrie.client.kex` |
| `2026-06-28 10:33:17` | `cowrie.login.success` |
| `2026-06-28 10:33:17` | `cowrie.session.params` |
| `2026-06-28 10:33:17` | `cowrie.command.input` |
| `2026-06-28 10:33:18` | `cowrie.log.closed` |
| `2026-06-28 10:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6d5c502e2e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:34 |
| **Last Seen** | 2026-06-28 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:34:09` | `cowrie.session.connect` |
| `2026-06-28 10:34:09` | `cowrie.client.version` |
| `2026-06-28 10:34:09` | `cowrie.client.kex` |
| `2026-06-28 10:34:10` | `cowrie.login.success` |
| `2026-06-28 10:34:11` | `cowrie.session.params` |
| `2026-06-28 10:34:11` | `cowrie.command.input` |
| `2026-06-28 10:34:11` | `cowrie.log.closed` |
| `2026-06-28 10:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3464fd1a66

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:35 |
| **Last Seen** | 2026-06-28 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:35:01` | `cowrie.session.connect` |
| `2026-06-28 10:35:01` | `cowrie.client.version` |
| `2026-06-28 10:35:01` | `cowrie.client.kex` |
| `2026-06-28 10:35:02` | `cowrie.login.success` |
| `2026-06-28 10:35:02` | `cowrie.session.params` |
| `2026-06-28 10:35:02` | `cowrie.command.input` |
| `2026-06-28 10:35:03` | `cowrie.log.closed` |
| `2026-06-28 10:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbce9d83c799

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 10:35 |
| **Last Seen** | 2026-06-28 10:35 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:35:06` | `cowrie.session.connect` |
| `2026-06-28 10:35:07` | `cowrie.client.version` |
| `2026-06-28 10:35:07` | `cowrie.client.kex` |
| `2026-06-28 10:35:14` | `cowrie.login.success` |
| `2026-06-28 10:35:17` | `cowrie.session.params` |
| `2026-06-28 10:35:17` | `cowrie.command.input` |
| `2026-06-28 10:35:20` | `cowrie.log.closed` |
| `2026-06-28 10:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f15aa0b4c9d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 10:35 |
| **Last Seen** | 2026-06-28 10:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:35:18` | `cowrie.session.connect` |
| `2026-06-28 10:35:18` | `cowrie.client.version` |
| `2026-06-28 10:35:18` | `cowrie.client.kex` |
| `2026-06-28 10:35:20` | `cowrie.login.success` |
| `2026-06-28 10:35:22` | `cowrie.session.params` |
| `2026-06-28 10:35:22` | `cowrie.command.input` |
| `2026-06-28 10:35:23` | `cowrie.log.closed` |
| `2026-06-28 10:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c059596f4f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:35 |
| **Last Seen** | 2026-06-28 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:35:54` | `cowrie.session.connect` |
| `2026-06-28 10:35:54` | `cowrie.client.version` |
| `2026-06-28 10:35:54` | `cowrie.client.kex` |
| `2026-06-28 10:35:54` | `cowrie.login.success` |
| `2026-06-28 10:35:55` | `cowrie.session.params` |
| `2026-06-28 10:35:55` | `cowrie.command.input` |
| `2026-06-28 10:35:55` | `cowrie.log.closed` |
| `2026-06-28 10:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a844aefd82

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 10:36 |
| **Last Seen** | 2026-06-28 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:36:00` | `cowrie.session.connect` |
| `2026-06-28 10:36:00` | `cowrie.client.version` |
| `2026-06-28 10:36:00` | `cowrie.client.kex` |
| `2026-06-28 10:36:00` | `cowrie.login.success` |
| `2026-06-28 10:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99a596eece51

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 10:36 |
| **Last Seen** | 2026-06-28 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:36:00` | `cowrie.session.connect` |
| `2026-06-28 10:36:00` | `cowrie.client.version` |
| `2026-06-28 10:36:00` | `cowrie.client.kex` |
| `2026-06-28 10:36:00` | `cowrie.login.success` |
| `2026-06-28 10:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1290696f5954

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 10:36 |
| **Last Seen** | 2026-06-28 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:36:10` | `cowrie.session.connect` |
| `2026-06-28 10:36:10` | `cowrie.client.version` |
| `2026-06-28 10:36:10` | `cowrie.client.kex` |
| `2026-06-28 10:36:10` | `cowrie.login.success` |
| `2026-06-28 10:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca29502838e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 10:36 |
| **Last Seen** | 2026-06-28 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:36:10` | `cowrie.session.connect` |
| `2026-06-28 10:36:10` | `cowrie.client.version` |
| `2026-06-28 10:36:10` | `cowrie.client.kex` |
| `2026-06-28 10:36:10` | `cowrie.login.success` |
| `2026-06-28 10:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7248130341

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:36 |
| **Last Seen** | 2026-06-28 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:36:46` | `cowrie.session.connect` |
| `2026-06-28 10:36:46` | `cowrie.client.version` |
| `2026-06-28 10:36:46` | `cowrie.client.kex` |
| `2026-06-28 10:36:47` | `cowrie.login.success` |
| `2026-06-28 10:36:47` | `cowrie.session.params` |
| `2026-06-28 10:36:47` | `cowrie.command.input` |
| `2026-06-28 10:36:48` | `cowrie.log.closed` |
| `2026-06-28 10:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eeb57a262d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:37 |
| **Last Seen** | 2026-06-28 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:37:38` | `cowrie.session.connect` |
| `2026-06-28 10:37:38` | `cowrie.client.version` |
| `2026-06-28 10:37:38` | `cowrie.client.kex` |
| `2026-06-28 10:37:39` | `cowrie.login.success` |
| `2026-06-28 10:37:40` | `cowrie.session.params` |
| `2026-06-28 10:37:40` | `cowrie.command.input` |
| `2026-06-28 10:37:40` | `cowrie.log.closed` |
| `2026-06-28 10:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb48cbb808b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:38 |
| **Last Seen** | 2026-06-28 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:38:32` | `cowrie.session.connect` |
| `2026-06-28 10:38:32` | `cowrie.client.version` |
| `2026-06-28 10:38:32` | `cowrie.client.kex` |
| `2026-06-28 10:38:32` | `cowrie.login.success` |
| `2026-06-28 10:38:33` | `cowrie.session.params` |
| `2026-06-28 10:38:33` | `cowrie.command.input` |
| `2026-06-28 10:38:33` | `cowrie.log.closed` |
| `2026-06-28 10:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6eb2d8acbf

| Field | Detail |
|---|---|
| **Source IP** | `219.138.78[.]67` |
| **First Seen** | 2026-06-28 10:39 |
| **Last Seen** | 2026-06-28 10:39 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:39:01` | `cowrie.session.connect` |
| `2026-06-28 10:39:02` | `cowrie.client.version` |
| `2026-06-28 10:39:49` | `cowrie.client.kex` |
| `2026-06-28 10:39:49` | `cowrie.login.success` |
| `2026-06-28 10:39:50` | `cowrie.session.params` |
| `2026-06-28 10:39:50` | `cowrie.command.input` |
| `2026-06-28 10:39:51` | `cowrie.log.closed` |
| `2026-06-28 10:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.138.78[.]67` to AbuseIPDB if not already reported
- [ ] Block `219.138.78[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0447d2c1dc33

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:39 |
| **Last Seen** | 2026-06-28 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:39:25` | `cowrie.session.connect` |
| `2026-06-28 10:39:25` | `cowrie.client.version` |
| `2026-06-28 10:39:25` | `cowrie.client.kex` |
| `2026-06-28 10:39:25` | `cowrie.login.success` |
| `2026-06-28 10:39:26` | `cowrie.session.params` |
| `2026-06-28 10:39:26` | `cowrie.command.input` |
| `2026-06-28 10:39:26` | `cowrie.log.closed` |
| `2026-06-28 10:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6526a33ee4b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:40 |
| **Last Seen** | 2026-06-28 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:40:17` | `cowrie.session.connect` |
| `2026-06-28 10:40:17` | `cowrie.client.version` |
| `2026-06-28 10:40:17` | `cowrie.client.kex` |
| `2026-06-28 10:40:18` | `cowrie.login.success` |
| `2026-06-28 10:40:18` | `cowrie.session.params` |
| `2026-06-28 10:40:18` | `cowrie.command.input` |
| `2026-06-28 10:40:18` | `cowrie.log.closed` |
| `2026-06-28 10:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260ab218c6a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:41 |
| **Last Seen** | 2026-06-28 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:41:09` | `cowrie.session.connect` |
| `2026-06-28 10:41:09` | `cowrie.client.version` |
| `2026-06-28 10:41:09` | `cowrie.client.kex` |
| `2026-06-28 10:41:10` | `cowrie.login.success` |
| `2026-06-28 10:41:11` | `cowrie.session.params` |
| `2026-06-28 10:41:11` | `cowrie.command.input` |
| `2026-06-28 10:41:11` | `cowrie.log.closed` |
| `2026-06-28 10:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c417df99e619

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:42 |
| **Last Seen** | 2026-06-28 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:42:01` | `cowrie.session.connect` |
| `2026-06-28 10:42:01` | `cowrie.client.version` |
| `2026-06-28 10:42:01` | `cowrie.client.kex` |
| `2026-06-28 10:42:01` | `cowrie.login.success` |
| `2026-06-28 10:42:02` | `cowrie.session.params` |
| `2026-06-28 10:42:02` | `cowrie.command.input` |
| `2026-06-28 10:42:02` | `cowrie.log.closed` |
| `2026-06-28 10:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac112edb392c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:42 |
| **Last Seen** | 2026-06-28 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:42:52` | `cowrie.session.connect` |
| `2026-06-28 10:42:52` | `cowrie.client.version` |
| `2026-06-28 10:42:52` | `cowrie.client.kex` |
| `2026-06-28 10:42:53` | `cowrie.login.success` |
| `2026-06-28 10:42:54` | `cowrie.session.params` |
| `2026-06-28 10:42:54` | `cowrie.command.input` |
| `2026-06-28 10:42:54` | `cowrie.log.closed` |
| `2026-06-28 10:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c94a447cd07

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:43 |
| **Last Seen** | 2026-06-28 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:43:46` | `cowrie.session.connect` |
| `2026-06-28 10:43:46` | `cowrie.client.version` |
| `2026-06-28 10:43:46` | `cowrie.client.kex` |
| `2026-06-28 10:43:46` | `cowrie.login.success` |
| `2026-06-28 10:43:47` | `cowrie.session.params` |
| `2026-06-28 10:43:47` | `cowrie.command.input` |
| `2026-06-28 10:43:47` | `cowrie.log.closed` |
| `2026-06-28 10:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10c363895516

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:44 |
| **Last Seen** | 2026-06-28 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:44:41` | `cowrie.session.connect` |
| `2026-06-28 10:44:41` | `cowrie.client.version` |
| `2026-06-28 10:44:41` | `cowrie.client.kex` |
| `2026-06-28 10:44:41` | `cowrie.login.success` |
| `2026-06-28 10:44:42` | `cowrie.session.params` |
| `2026-06-28 10:44:42` | `cowrie.command.input` |
| `2026-06-28 10:44:42` | `cowrie.log.closed` |
| `2026-06-28 10:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8965bad2129

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:45 |
| **Last Seen** | 2026-06-28 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:45:37` | `cowrie.session.connect` |
| `2026-06-28 10:45:37` | `cowrie.client.version` |
| `2026-06-28 10:45:37` | `cowrie.client.kex` |
| `2026-06-28 10:45:38` | `cowrie.login.success` |
| `2026-06-28 10:45:38` | `cowrie.session.params` |
| `2026-06-28 10:45:38` | `cowrie.command.input` |
| `2026-06-28 10:45:39` | `cowrie.log.closed` |
| `2026-06-28 10:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940e9698e50e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 10:46 |
| **Last Seen** | 2026-06-28 10:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:46:24` | `cowrie.session.connect` |
| `2026-06-28 10:46:26` | `cowrie.client.version` |
| `2026-06-28 10:46:26` | `cowrie.client.kex` |
| `2026-06-28 10:46:31` | `cowrie.login.success` |
| `2026-06-28 10:46:35` | `cowrie.session.params` |
| `2026-06-28 10:46:35` | `cowrie.command.input` |
| `2026-06-28 10:46:36` | `cowrie.log.closed` |
| `2026-06-28 10:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cc5d036ea91

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:46 |
| **Last Seen** | 2026-06-28 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:46:33` | `cowrie.session.connect` |
| `2026-06-28 10:46:33` | `cowrie.client.version` |
| `2026-06-28 10:46:33` | `cowrie.client.kex` |
| `2026-06-28 10:46:33` | `cowrie.login.success` |
| `2026-06-28 10:46:34` | `cowrie.session.params` |
| `2026-06-28 10:46:34` | `cowrie.command.input` |
| `2026-06-28 10:46:34` | `cowrie.log.closed` |
| `2026-06-28 10:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab45ab63254

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:47 |
| **Last Seen** | 2026-06-28 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:47:26` | `cowrie.session.connect` |
| `2026-06-28 10:47:26` | `cowrie.client.version` |
| `2026-06-28 10:47:26` | `cowrie.client.kex` |
| `2026-06-28 10:47:27` | `cowrie.login.success` |
| `2026-06-28 10:47:28` | `cowrie.session.params` |
| `2026-06-28 10:47:28` | `cowrie.command.input` |
| `2026-06-28 10:47:28` | `cowrie.log.closed` |
| `2026-06-28 10:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7607292d5db0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:48 |
| **Last Seen** | 2026-06-28 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:48:20` | `cowrie.session.connect` |
| `2026-06-28 10:48:20` | `cowrie.client.version` |
| `2026-06-28 10:48:20` | `cowrie.client.kex` |
| `2026-06-28 10:48:20` | `cowrie.login.success` |
| `2026-06-28 10:48:21` | `cowrie.session.params` |
| `2026-06-28 10:48:21` | `cowrie.command.input` |
| `2026-06-28 10:48:21` | `cowrie.log.closed` |
| `2026-06-28 10:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cbedd356973

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:49 |
| **Last Seen** | 2026-06-28 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:49:15` | `cowrie.session.connect` |
| `2026-06-28 10:49:15` | `cowrie.client.version` |
| `2026-06-28 10:49:15` | `cowrie.client.kex` |
| `2026-06-28 10:49:15` | `cowrie.login.success` |
| `2026-06-28 10:49:16` | `cowrie.session.params` |
| `2026-06-28 10:49:16` | `cowrie.command.input` |
| `2026-06-28 10:49:16` | `cowrie.log.closed` |
| `2026-06-28 10:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69670c54549

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 10:49 |
| **Last Seen** | 2026-06-28 10:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:49:57` | `cowrie.session.connect` |
| `2026-06-28 10:49:58` | `cowrie.client.version` |
| `2026-06-28 10:49:58` | `cowrie.client.kex` |
| `2026-06-28 10:49:59` | `cowrie.login.success` |
| `2026-06-28 10:50:01` | `cowrie.session.params` |
| `2026-06-28 10:50:01` | `cowrie.command.input` |
| `2026-06-28 10:50:01` | `cowrie.log.closed` |
| `2026-06-28 10:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191b13245192

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:50 |
| **Last Seen** | 2026-06-28 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:50:10` | `cowrie.session.connect` |
| `2026-06-28 10:50:10` | `cowrie.client.version` |
| `2026-06-28 10:50:11` | `cowrie.client.kex` |
| `2026-06-28 10:50:11` | `cowrie.login.success` |
| `2026-06-28 10:50:12` | `cowrie.session.params` |
| `2026-06-28 10:50:12` | `cowrie.command.input` |
| `2026-06-28 10:50:12` | `cowrie.log.closed` |
| `2026-06-28 10:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe74d59c8f06

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:51 |
| **Last Seen** | 2026-06-28 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:51:08` | `cowrie.session.connect` |
| `2026-06-28 10:51:08` | `cowrie.client.version` |
| `2026-06-28 10:51:08` | `cowrie.client.kex` |
| `2026-06-28 10:51:09` | `cowrie.login.success` |
| `2026-06-28 10:51:10` | `cowrie.session.params` |
| `2026-06-28 10:51:10` | `cowrie.command.input` |
| `2026-06-28 10:51:10` | `cowrie.log.closed` |
| `2026-06-28 10:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d663a8ae7f07

| Field | Detail |
|---|---|
| **Source IP** | `95.220.204[.]16` |
| **First Seen** | 2026-06-28 10:51 |
| **Last Seen** | 2026-06-28 10:53 |
| **Session Duration** | 108s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:51:32` | `cowrie.session.connect` |
| `2026-06-28 10:51:32` | `cowrie.client.version` |
| `2026-06-28 10:51:32` | `cowrie.client.kex` |
| `2026-06-28 10:51:36` | `cowrie.login.failed` |
| `2026-06-28 10:51:37` | `cowrie.login.success` |
| `2026-06-28 10:51:38` | `cowrie.session.params` |
| `2026-06-28 10:51:38` | `cowrie.command.input` |
| `2026-06-28 10:51:38` | `cowrie.command.failed` |
| `2026-06-28 10:51:38` | `cowrie.log.closed` |
| `2026-06-28 10:51:39` | `cowrie.session.params` |
| `2026-06-28 10:51:39` | `cowrie.command.input` |
| `2026-06-28 10:51:39` | `cowrie.log.closed` |
| `2026-06-28 10:51:40` | `cowrie.session.params` |
| `2026-06-28 10:51:40` | `cowrie.command.input` |
| `2026-06-28 10:51:40` | `cowrie.log.closed` |
| `2026-06-28 10:51:41` | `cowrie.session.params` |
| `2026-06-28 10:51:41` | `cowrie.command.input` |
| `2026-06-28 10:51:42` | `cowrie.log.closed` |
| `2026-06-28 10:51:42` | `cowrie.session.params` |
| `2026-06-28 10:51:42` | `cowrie.command.input` |
| `2026-06-28 10:51:42` | `cowrie.log.closed` |
| `2026-06-28 10:51:43` | `cowrie.session.params` |
| `2026-06-28 10:51:43` | `cowrie.command.input` |
| `2026-06-28 10:51:43` | `cowrie.log.closed` |
| `2026-06-28 10:51:44` | `cowrie.session.params` |
| `2026-06-28 10:51:44` | `cowrie.command.input` |
| `2026-06-28 10:51:44` | `cowrie.log.closed` |
| `2026-06-28 10:51:45` | `cowrie.session.params` |
| `2026-06-28 10:51:45` | `cowrie.command.input` |
| `2026-06-28 10:51:46` | `cowrie.log.closed` |
| `2026-06-28 10:51:47` | `cowrie.session.params` |
| `2026-06-28 10:51:47` | `cowrie.command.input` |
| `2026-06-28 10:51:47` | `cowrie.log.closed` |
| `2026-06-28 10:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.220.204[.]16` to AbuseIPDB if not already reported
- [ ] Block `95.220.204[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a256b3ee5c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:52 |
| **Last Seen** | 2026-06-28 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:52:05` | `cowrie.session.connect` |
| `2026-06-28 10:52:05` | `cowrie.client.version` |
| `2026-06-28 10:52:05` | `cowrie.client.kex` |
| `2026-06-28 10:52:05` | `cowrie.login.success` |
| `2026-06-28 10:52:06` | `cowrie.session.params` |
| `2026-06-28 10:52:06` | `cowrie.command.input` |
| `2026-06-28 10:52:06` | `cowrie.log.closed` |
| `2026-06-28 10:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-300d53a756e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:53 |
| **Last Seen** | 2026-06-28 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:53:01` | `cowrie.session.connect` |
| `2026-06-28 10:53:01` | `cowrie.client.version` |
| `2026-06-28 10:53:01` | `cowrie.client.kex` |
| `2026-06-28 10:53:02` | `cowrie.login.success` |
| `2026-06-28 10:53:02` | `cowrie.session.params` |
| `2026-06-28 10:53:02` | `cowrie.command.input` |
| `2026-06-28 10:53:03` | `cowrie.log.closed` |
| `2026-06-28 10:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cf3a7c65d54

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:53 |
| **Last Seen** | 2026-06-28 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:53:55` | `cowrie.session.connect` |
| `2026-06-28 10:53:55` | `cowrie.client.version` |
| `2026-06-28 10:53:55` | `cowrie.client.kex` |
| `2026-06-28 10:53:56` | `cowrie.login.success` |
| `2026-06-28 10:53:57` | `cowrie.session.params` |
| `2026-06-28 10:53:57` | `cowrie.command.input` |
| `2026-06-28 10:53:57` | `cowrie.log.closed` |
| `2026-06-28 10:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ec4679a7af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 10:54 |
| **Last Seen** | 2026-06-28 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 10:54:49` | `cowrie.session.connect` |
| `2026-06-28 10:54:49` | `cowrie.client.version` |
| `2026-06-28 10:54:49` | `cowrie.client.kex` |
| `2026-06-28 10:54:49` | `cowrie.login.success` |
| `2026-06-28 10:54:50` | `cowrie.session.params` |
| `2026-06-28 10:54:50` | `cowrie.command.input` |
| `2026-06-28 10:54:50` | `cowrie.log.closed` |
| `2026-06-28 10:54:50` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **129** | 2026-06-28 08:55 | 2026-06-28 10:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **3** | 2026-06-28 09:59 | 2026-06-28 10:44 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]32` | **3** | 2026-06-28 09:36 | 2026-06-28 09:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]42` | **3** | 2026-06-28 09:36 | 2026-06-28 09:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]48` | **3** | 2026-06-28 09:35 | 2026-06-28 09:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | **2** | 2026-06-28 10:03 | 2026-06-28 10:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `36.140.29[.]110` | **2** | 2026-06-28 09:56 | 2026-06-28 09:58 | 2m | 0 | `T1592` | 🟢 LOW |
| `157.230.42[.]17` | 1 | 2026-06-28 09:15 | 2026-06-28 09:16 | 50s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | 1 | 2026-06-28 10:29 | 2026-06-28 10:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-06-28 09:33 | 2026-06-28 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.26.252[.]153` | 1 | 2026-06-28 09:05 | 2026-06-28 09:05 | 4s | 0 | `T1592` | 🟢 LOW |
| `213.149.181[.]32` | 1 | 2026-06-28 09:43 | 2026-06-28 09:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `219.138.78[.]67` | 1 | 2026-06-28 10:39 | 2026-06-28 10:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.134.216[.]108` | 1 | 2026-06-28 10:25 | 2026-06-28 10:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-06-28 10:06 | 2026-06-28 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-06-28 10:32 | 2026-06-28 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.131.166[.]119` | 1 | 2026-06-28 10:28 | 2026-06-28 10:28 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `3.134.216[.]108` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `172.236.228[.]229` | US | Linode | **100** ⚠️ | 50 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `45.79.5[.]11` | US | Linode | **100** ⚠️ | 50 |
| `157.230.42[.]17` | SG | DigitalOcean, LLC | **100** ⚠️ | 11 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `213.149.181[.]32` | CY | Cyprus Telecommuncations Authority | **100** ⚠️ | 50 |
| `219.138.78[.]67` | CN | CHINANET hubei province network | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 171 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 163 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 326 cases |
| Tool 34  | Credential Extractor        | ✅ 164 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (2.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 41 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 162 priority case(s) shown individually · 17 recon entry/entries in table (7 group(s) consolidating 145 session(s)).

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
_Report time: 2026-06-28T11:48:50Z_

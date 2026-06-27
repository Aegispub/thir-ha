# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-27 |
| **Generated At** | 2026-06-27T23:07:10Z |
| **Shift Time** | 23:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **392** |
| Confirmed Threats | **385** |
| False Positives Filtered | **7** (1.8%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **10** |
| High Severity Cases | **153** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **239** |
| Malware Samples Analyzed | **5** HIGH · **41** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **154** |
| Unique Credential Pairs | **150** |
| Unique Usernames | **78** |
| Unique Passwords | **142** |
| Successful Auth Pairs | **153** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 57 |
| `ubuntu` | 13 |
| `user` | 5 |
| `web1` | 2 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 4 |
| `1234` | 4 |
| `pass` | 2 |
| `scan` | 2 |
| `peixuanli` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `peixuanli` | `peixuanli` | 2 |
| `root` | `LeitboGi0ro` | 2 |
| `root` | `123@@@` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `root` | `qweasd12` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qweasd12` | `209.99.185.59` | 2026-06-27T20:55:04 |
| `root` | `L1nuxAdmin#Secure` | `209.99.185.59` | 2026-06-27T20:55:59 |
| `hotel` | `123456` | `209.99.185.59` | 2026-06-27T20:56:55 |
| `ubuntu` | `1234567890` | `209.99.185.59` | 2026-06-27T20:57:52 |
| `root` | `Password0` | `45.205.1.42` | 2026-06-27T20:58:09 |
| `gpu` | `000000` | `209.99.185.59` | 2026-06-27T20:58:48 |
| `hanx` | `hanx` | `209.99.185.59` | 2026-06-27T20:59:44 |
| `root` | `huawei12#$` | `209.99.185.59` | 2026-06-27T21:00:39 |
| `chaoxi.xu` | `Chaoxi2020` | `209.99.185.59` | 2026-06-27T21:01:34 |
| `temp` | `temp` | `209.99.185.59` | 2026-06-27T21:02:29 |
| `root` | `123zxc!@#` | `209.99.185.59` | 2026-06-27T21:03:28 |
| `ubuntu` | `qwert12345` | `45.198.224.120` | 2026-06-27T21:04:23 |
| `DingWubin` | `DWB39219920914` | `209.99.185.59` | 2026-06-27T21:04:27 |
| `chiye` | `chiye` | `209.99.185.59` | 2026-06-27T21:05:24 |
| `db2inst1` | `db2pw` | `209.99.185.59` | 2026-06-27T21:06:20 |
| `root` | `abc123B` | `209.99.185.59` | 2026-06-27T21:07:16 |
| `ubuntu` | `1z2x3c` | `209.99.185.59` | 2026-06-27T21:08:13 |
| `root` | `pxf123` | `209.99.185.59` | 2026-06-27T21:09:11 |
| `elk` | `elk666` | `209.99.185.59` | 2026-06-27T21:10:10 |
| `ubuntu` | `123root321` | `209.99.185.59` | 2026-06-27T21:11:09 |
| `user` | `pass` | `209.99.185.59` | 2026-06-27T21:12:10 |
| `root` | `qwert` | `45.205.1.42` | 2026-06-27T21:12:42 |
| `yunwei` | `123456` | `209.99.185.59` | 2026-06-27T21:13:07 |
| `aidana` | `aidana` | `209.99.185.59` | 2026-06-27T21:14:03 |
| `m` | `123` | `209.99.185.59` | 2026-06-27T21:15:01 |
| `root` | `QAZwsxedc123` | `45.198.224.120` | 2026-06-27T21:15:59 |
| `web1` | `web123` | `209.99.185.59` | 2026-06-27T21:16:00 |
| `root` | `Pa22word` | `209.99.185.59` | 2026-06-27T21:17:00 |
| `root` | `adminadmin` | `209.99.185.59` | 2026-06-27T21:18:00 |
| `kdp` | `kdp123` | `209.99.185.59` | 2026-06-27T21:18:59 |
| `user` | `654321` | `209.99.185.59` | 2026-06-27T21:19:57 |
| `kxw` | `kxw123` | `209.99.185.59` | 2026-06-27T21:21:00 |
| `root` | `oliver` | `209.99.185.59` | 2026-06-27T21:22:03 |
| `wahid` | `wahid123!` | `209.99.185.59` | 2026-06-27T21:23:06 |
| `ubuntu` | `ubuntuserver` | `209.99.185.59` | 2026-06-27T21:24:08 |
| `root` | `a1s2d3f4g5h6j7` | `209.99.185.59` | 2026-06-27T21:25:10 |
| `universe` | `universe` | `209.99.185.59` | 2026-06-27T21:26:11 |
| `fengyingchao` | `fengyingchao` | `209.99.185.59` | 2026-06-27T21:27:13 |
| `ubuntu` | `P4ssw0rd` | `45.205.1.42` | 2026-06-27T21:27:22 |
| `ubuntu` | `demo` | `45.198.224.120` | 2026-06-27T21:27:42 |
| `root` | `123server` | `209.99.185.59` | 2026-06-27T21:28:20 |
| `guest` | `11111111` | `209.99.185.59` | 2026-06-27T21:29:25 |
| `develop` | `develop@123` | `209.99.185.59` | 2026-06-27T21:30:30 |
| `root` | `zxqqy` | `209.99.185.59` | 2026-06-27T21:31:34 |
| `cgx` | `cgx12345` | `209.99.185.59` | 2026-06-27T21:32:37 |
| `root` | `asd1234567` | `209.99.185.59` | 2026-06-27T21:33:40 |
| `zhangby` | `zhangby` | `209.99.185.59` | 2026-06-27T21:34:46 |
| `lhy` | `lhy` | `209.99.185.59` | 2026-06-27T21:35:53 |
| `redsun2k` | `P@ssword1!` | `209.99.185.59` | 2026-06-27T21:36:58 |
| `lyy` | `123456` | `209.99.185.59` | 2026-06-27T21:38:03 |
| `user` | `wasd` | `209.99.185.59` | 2026-06-27T21:39:07 |
| `test` | `1234` | `45.198.224.120` | 2026-06-27T21:39:54 |
| `admin` | `admin123!@#` | `209.99.185.59` | 2026-06-27T21:40:13 |
| `root` | `i-0f00f0e4433858245` | `209.99.185.59` | 2026-06-27T21:41:20 |
| `root` | `qweasdzxc` | `45.205.1.42` | 2026-06-27T21:41:52 |
| `centos` | `password` | `209.99.185.59` | 2026-06-27T21:42:28 |
| `root` | `a1b2c3d4e5` | `209.99.185.59` | 2026-06-27T21:43:35 |
| `LouisSu123` | `MercedesAMG2014` | `209.99.185.59` | 2026-06-27T21:44:40 |
| `root` | `!QAZ2wsx` | `209.99.185.59` | 2026-06-27T21:45:45 |
| `prova` | `prova123` | `209.99.185.59` | 2026-06-27T21:46:51 |
| `sjb` | `korea2013` | `209.99.185.59` | 2026-06-27T21:47:59 |
| `jiadayu` | `jiadayu123` | `209.99.185.59` | 2026-06-27T21:49:09 |
| `root` | `qwerty0` | `209.99.185.59` | 2026-06-27T21:50:19 |
| `batman` | `batman` | `209.99.185.59` | 2026-06-27T21:51:27 |
| `root` | `Pass@word123!` | `45.198.224.120` | 2026-06-27T21:51:39 |
| `root` | `root@222` | `209.99.185.59` | 2026-06-27T21:52:33 |
| `root` | `pass12345` | `209.99.185.59` | 2026-06-27T21:53:41 |
| `lasha` | `lasha` | `209.99.185.59` | 2026-06-27T21:54:50 |
| `bio3` | `1234` | `209.99.185.59` | 2026-06-27T21:56:01 |
| `root` | `scan` | `45.205.1.42` | 2026-06-27T21:56:26 |
| `jayce` | `!Jayce1228` | `209.99.185.59` | 2026-06-27T21:57:11 |
| `ubuntu` | `hduser` | `209.99.185.59` | 2026-06-27T21:58:18 |
| `root` | `postgres123` | `209.99.185.59` | 2026-06-27T21:59:27 |
| `gosh2` | `#new0211` | `209.99.185.59` | 2026-06-27T22:00:29 |
| `root` | `0147` | `209.99.185.59` | 2026-06-27T22:01:15 |
| `rashid` | `rashid` | `209.99.185.59` | 2026-06-27T22:02:01 |
| `jira` | `123321` | `209.99.185.59` | 2026-06-27T22:02:46 |
| `ubuntu` | `123qwer` | `45.198.224.120` | 2026-06-27T22:03:29 |
| `liyang` | `liyang` | `209.99.185.59` | 2026-06-27T22:03:31 |
| `oracle` | `pass` | `209.99.185.59` | 2026-06-27T22:04:14 |
| `test2` | `test2` | `209.99.185.59` | 2026-06-27T22:04:59 |
| `dolphin` | `Drag1823hcacatcuciocolata` | `209.99.185.59` | 2026-06-27T22:05:44 |
| `root` | `qazwsxedc18` | `209.99.185.59` | 2026-06-27T22:06:30 |
| `backup` | `backup123` | `209.99.185.59` | 2026-06-27T22:07:17 |
| `root` | `cccccc` | `209.99.185.59` | 2026-06-27T22:08:04 |
| `gitlab` | `gitlab123` | `209.99.185.59` | 2026-06-27T22:08:50 |
| `root` | `buzhidao` | `209.99.185.59` | 2026-06-27T22:09:37 |
| `zqding` | `zqding` | `209.99.185.59` | 2026-06-27T22:10:24 |
| `ubuntu` | `admin1121` | `45.205.1.42` | 2026-06-27T22:10:58 |
| `root` | `wuning@2020` | `209.99.185.59` | 2026-06-27T22:11:10 |
| `yu` | `wafxp110` | `209.99.185.59` | 2026-06-27T22:11:57 |
| `dell` | `ABCabc123` | `209.99.185.59` | 2026-06-27T22:12:45 |
| `root` | `'2+3z!![WSVGvw%-*'` | `209.99.185.59` | 2026-06-27T22:13:35 |
| `vmadmin` | `vmadmin` | `209.99.185.59` | 2026-06-27T22:14:24 |
| `root` | `777777` | `209.99.185.59` | 2026-06-27T22:15:12 |
| `peixuanli` | `peixuanli` | `45.198.224.120` | 2026-06-27T22:15:43 |
| `root` | `w79w9riq` | `209.99.185.59` | 2026-06-27T22:16:00 |
| `ubuntu` | `Admin` | `209.99.185.59` | 2026-06-27T22:16:47 |
| `root` | `aptx4869` | `209.99.185.59` | 2026-06-27T22:17:34 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-27T22:17:48 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-27T22:17:48 |
| `cmaq` | `korea2021` | `209.99.185.59` | 2026-06-27T22:18:21 |
| `ylj` | `jingyunliang` | `209.99.185.59` | 2026-06-27T22:19:10 |
| `ex` | `ex` | `209.99.185.59` | 2026-06-27T22:19:59 |
| `root` | `inspur@123` | `209.99.185.59` | 2026-06-27T22:20:50 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-27T22:21:32 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-27T22:21:33 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-27T22:21:34 |
| `tomcat` | `Tomcat@2022` | `209.99.185.59` | 2026-06-27T22:21:41 |
| `user5` | `user5` | `209.99.185.59` | 2026-06-27T22:22:31 |
| `shizhan` | `shizhan123` | `209.99.185.59` | 2026-06-27T22:23:21 |
| `edna` | `edna` | `209.99.185.59` | 2026-06-27T22:24:11 |
| `wujinxia` | `wujinxia` | `209.99.185.59` | 2026-06-27T22:25:03 |
| `peixuanli` | `peixuanli` | `45.205.1.42` | 2026-06-27T22:25:47 |
| `es` | `changeme123` | `209.99.185.59` | 2026-06-27T22:25:56 |
| `root` | `dangerous@123` | `209.99.185.59` | 2026-06-27T22:26:49 |
| `user` | `abc@123` | `209.99.185.59` | 2026-06-27T22:27:41 |
| `root` | `Passwd!` | `45.198.224.120` | 2026-06-27T22:28:06 |
| `huangQiFeng` | `worldpass2808` | `209.99.185.59` | 2026-06-27T22:28:31 |
| `hadoop` | `Hadoop123!` | `209.99.185.59` | 2026-06-27T22:29:22 |
| `root` | `asdf1234567890` | `209.99.185.59` | 2026-06-27T22:30:12 |
| `tunel` | `tunel` | `209.99.185.59` | 2026-06-27T22:31:03 |
| `root` | `qwer` | `209.99.185.59` | 2026-06-27T22:31:55 |
| `site` | `site` | `209.99.185.59` | 2026-06-27T22:32:48 |
| `dzr` | `drz` | `209.99.185.59` | 2026-06-27T22:33:43 |
| `web1` | `newtest` | `209.99.185.59` | 2026-06-27T22:34:40 |
| `oracle` | `12345678` | `209.99.185.59` | 2026-06-27T22:35:34 |
| `ubuntu` | `password1234567` | `209.99.185.59` | 2026-06-27T22:36:27 |
| `gituser` | `gituser` | `209.99.185.59` | 2026-06-27T22:37:21 |
| `test` | `1qaz2wsx3edc` | `209.99.185.59` | 2026-06-27T22:38:15 |
| `user` | `q1w2e3r4` | `209.99.185.59` | 2026-06-27T22:39:13 |
| `root` | `security` | `45.198.224.120` | 2026-06-27T22:39:46 |
| `liwp` | `liwp` | `209.99.185.59` | 2026-06-27T22:40:06 |
| `scan` | `scan` | `45.205.1.42` | 2026-06-27T22:40:19 |
| `root` | `iexcel` | `209.99.185.59` | 2026-06-27T22:41:01 |
| `root` | `hesoyam2005` | `209.99.185.59` | 2026-06-27T22:41:55 |
| `zhang` | `123456` | `209.99.185.59` | 2026-06-27T22:42:48 |
| `devuser` | `1234` | `209.99.185.59` | 2026-06-27T22:43:41 |
| `root` | `POIUYT#@!2017` | `209.99.185.59` | 2026-06-27T22:44:38 |
| `liujy` | `X6228102` | `209.99.185.59` | 2026-06-27T22:45:34 |
| `nfe` | `nfe` | `209.99.185.59` | 2026-06-27T22:46:29 |
| `zhouh` | `1234qwer` | `209.99.185.59` | 2026-06-27T22:47:23 |
| `root` | `123456Abc` | `209.99.185.59` | 2026-06-27T22:48:17 |
| `root` | `daniel` | `209.99.185.59` | 2026-06-27T22:49:09 |
| `root` | `123012` | `209.99.185.59` | 2026-06-27T22:50:03 |
| `panziyi` | `panziyi` | `209.99.185.59` | 2026-06-27T22:50:59 |
| `root` | `dVrI4vTcir` | `10.0.0.73` | 2026-06-27T22:51:00 |
| `root` | `qwer123456` | `45.198.224.120` | 2026-06-27T22:51:10 |
| `root` | `aA123456!` | `209.99.185.59` | 2026-06-27T22:51:54 |
| `jangkyu` | `1234` | `209.99.185.59` | 2026-06-27T22:52:50 |
| `root` | `mnh@2020` | `209.99.185.59` | 2026-06-27T22:53:45 |
| `tacuser` | `acceler8` | `209.99.185.59` | 2026-06-27T22:54:40 |
| `ubuntu` | `debian123456789` | `45.205.1.42` | 2026-06-27T22:54:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **392** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 148 |
| Paramiko (Python) | 6 |
| libssh | 5 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 148 | 4 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 148 | 4 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **12** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS402253` | SKN Subnet & Telecom Ltd | 1 | HIGH |
| `AS267784` | Flyservers S.A. | 1 | HIGH |
| `AS49981` | WorldStream B.V. | 1 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (153)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-44522c40a351

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:55 |
| **Last Seen** | 2026-06-27 20:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:55:03` | `cowrie.session.connect` |
| `2026-06-27 20:55:03` | `cowrie.client.version` |
| `2026-06-27 20:55:03` | `cowrie.client.kex` |
| `2026-06-27 20:55:04` | `cowrie.login.success` |
| `2026-06-27 20:55:05` | `cowrie.session.params` |
| `2026-06-27 20:55:05` | `cowrie.command.input` |
| `2026-06-27 20:55:05` | `cowrie.log.closed` |
| `2026-06-27 20:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b3810883a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:55 |
| **Last Seen** | 2026-06-27 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:55:59` | `cowrie.session.connect` |
| `2026-06-27 20:55:59` | `cowrie.client.version` |
| `2026-06-27 20:55:59` | `cowrie.client.kex` |
| `2026-06-27 20:55:59` | `cowrie.login.success` |
| `2026-06-27 20:56:00` | `cowrie.session.params` |
| `2026-06-27 20:56:00` | `cowrie.command.input` |
| `2026-06-27 20:56:00` | `cowrie.log.closed` |
| `2026-06-27 20:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ddfc30f251

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:56 |
| **Last Seen** | 2026-06-27 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:56:55` | `cowrie.session.connect` |
| `2026-06-27 20:56:55` | `cowrie.client.version` |
| `2026-06-27 20:56:55` | `cowrie.client.kex` |
| `2026-06-27 20:56:55` | `cowrie.login.success` |
| `2026-06-27 20:56:56` | `cowrie.session.params` |
| `2026-06-27 20:56:56` | `cowrie.command.input` |
| `2026-06-27 20:56:56` | `cowrie.log.closed` |
| `2026-06-27 20:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03976b03b444

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:57 |
| **Last Seen** | 2026-06-27 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:57:52` | `cowrie.session.connect` |
| `2026-06-27 20:57:52` | `cowrie.client.version` |
| `2026-06-27 20:57:52` | `cowrie.client.kex` |
| `2026-06-27 20:57:52` | `cowrie.login.success` |
| `2026-06-27 20:57:53` | `cowrie.session.params` |
| `2026-06-27 20:57:53` | `cowrie.command.input` |
| `2026-06-27 20:57:53` | `cowrie.log.closed` |
| `2026-06-27 20:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52bc8f7da78

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 20:58 |
| **Last Seen** | 2026-06-27 20:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:58:07` | `cowrie.session.connect` |
| `2026-06-27 20:58:07` | `cowrie.client.version` |
| `2026-06-27 20:58:07` | `cowrie.client.kex` |
| `2026-06-27 20:58:09` | `cowrie.login.success` |
| `2026-06-27 20:58:10` | `cowrie.session.params` |
| `2026-06-27 20:58:10` | `cowrie.command.input` |
| `2026-06-27 20:58:10` | `cowrie.log.closed` |
| `2026-06-27 20:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e52acaa0023

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:58 |
| **Last Seen** | 2026-06-27 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:58:48` | `cowrie.session.connect` |
| `2026-06-27 20:58:48` | `cowrie.client.version` |
| `2026-06-27 20:58:48` | `cowrie.client.kex` |
| `2026-06-27 20:58:48` | `cowrie.login.success` |
| `2026-06-27 20:58:49` | `cowrie.session.params` |
| `2026-06-27 20:58:49` | `cowrie.command.input` |
| `2026-06-27 20:58:49` | `cowrie.log.closed` |
| `2026-06-27 20:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883b88a0fc9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:59 |
| **Last Seen** | 2026-06-27 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:59:44` | `cowrie.session.connect` |
| `2026-06-27 20:59:44` | `cowrie.client.version` |
| `2026-06-27 20:59:44` | `cowrie.client.kex` |
| `2026-06-27 20:59:44` | `cowrie.login.success` |
| `2026-06-27 20:59:45` | `cowrie.session.params` |
| `2026-06-27 20:59:45` | `cowrie.command.input` |
| `2026-06-27 20:59:45` | `cowrie.log.closed` |
| `2026-06-27 20:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff4a796bfa4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:00 |
| **Last Seen** | 2026-06-27 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:00:39` | `cowrie.session.connect` |
| `2026-06-27 21:00:39` | `cowrie.client.version` |
| `2026-06-27 21:00:39` | `cowrie.client.kex` |
| `2026-06-27 21:00:39` | `cowrie.login.success` |
| `2026-06-27 21:00:40` | `cowrie.session.params` |
| `2026-06-27 21:00:40` | `cowrie.command.input` |
| `2026-06-27 21:00:40` | `cowrie.log.closed` |
| `2026-06-27 21:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b071aeafa82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:01 |
| **Last Seen** | 2026-06-27 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:01:33` | `cowrie.session.connect` |
| `2026-06-27 21:01:33` | `cowrie.client.version` |
| `2026-06-27 21:01:33` | `cowrie.client.kex` |
| `2026-06-27 21:01:34` | `cowrie.login.success` |
| `2026-06-27 21:01:34` | `cowrie.session.params` |
| `2026-06-27 21:01:34` | `cowrie.command.input` |
| `2026-06-27 21:01:35` | `cowrie.log.closed` |
| `2026-06-27 21:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae341aeb1e01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:02 |
| **Last Seen** | 2026-06-27 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:02:29` | `cowrie.session.connect` |
| `2026-06-27 21:02:29` | `cowrie.client.version` |
| `2026-06-27 21:02:29` | `cowrie.client.kex` |
| `2026-06-27 21:02:29` | `cowrie.login.success` |
| `2026-06-27 21:02:30` | `cowrie.session.params` |
| `2026-06-27 21:02:30` | `cowrie.command.input` |
| `2026-06-27 21:02:30` | `cowrie.log.closed` |
| `2026-06-27 21:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c6c6219457

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:03 |
| **Last Seen** | 2026-06-27 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:03:27` | `cowrie.session.connect` |
| `2026-06-27 21:03:27` | `cowrie.client.version` |
| `2026-06-27 21:03:27` | `cowrie.client.kex` |
| `2026-06-27 21:03:28` | `cowrie.login.success` |
| `2026-06-27 21:03:28` | `cowrie.session.params` |
| `2026-06-27 21:03:28` | `cowrie.command.input` |
| `2026-06-27 21:03:28` | `cowrie.log.closed` |
| `2026-06-27 21:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf86f3e468fc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 21:04 |
| **Last Seen** | 2026-06-27 21:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:04:16` | `cowrie.session.connect` |
| `2026-06-27 21:04:18` | `cowrie.client.version` |
| `2026-06-27 21:04:18` | `cowrie.client.kex` |
| `2026-06-27 21:04:23` | `cowrie.login.success` |
| `2026-06-27 21:04:27` | `cowrie.session.params` |
| `2026-06-27 21:04:27` | `cowrie.command.input` |
| `2026-06-27 21:04:28` | `cowrie.log.closed` |
| `2026-06-27 21:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c5388d4c45b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:04 |
| **Last Seen** | 2026-06-27 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:04:27` | `cowrie.session.connect` |
| `2026-06-27 21:04:27` | `cowrie.client.version` |
| `2026-06-27 21:04:27` | `cowrie.client.kex` |
| `2026-06-27 21:04:27` | `cowrie.login.success` |
| `2026-06-27 21:04:28` | `cowrie.session.params` |
| `2026-06-27 21:04:28` | `cowrie.command.input` |
| `2026-06-27 21:04:28` | `cowrie.log.closed` |
| `2026-06-27 21:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e381ea0fc13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:05 |
| **Last Seen** | 2026-06-27 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:05:24` | `cowrie.session.connect` |
| `2026-06-27 21:05:24` | `cowrie.client.version` |
| `2026-06-27 21:05:24` | `cowrie.client.kex` |
| `2026-06-27 21:05:24` | `cowrie.login.success` |
| `2026-06-27 21:05:25` | `cowrie.session.params` |
| `2026-06-27 21:05:25` | `cowrie.command.input` |
| `2026-06-27 21:05:25` | `cowrie.log.closed` |
| `2026-06-27 21:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62c35f376c51

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:06 |
| **Last Seen** | 2026-06-27 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:06:20` | `cowrie.session.connect` |
| `2026-06-27 21:06:20` | `cowrie.client.version` |
| `2026-06-27 21:06:20` | `cowrie.client.kex` |
| `2026-06-27 21:06:20` | `cowrie.login.success` |
| `2026-06-27 21:06:21` | `cowrie.session.params` |
| `2026-06-27 21:06:21` | `cowrie.command.input` |
| `2026-06-27 21:06:21` | `cowrie.log.closed` |
| `2026-06-27 21:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3663d8f501

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:07 |
| **Last Seen** | 2026-06-27 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:07:16` | `cowrie.session.connect` |
| `2026-06-27 21:07:16` | `cowrie.client.version` |
| `2026-06-27 21:07:16` | `cowrie.client.kex` |
| `2026-06-27 21:07:16` | `cowrie.login.success` |
| `2026-06-27 21:07:17` | `cowrie.session.params` |
| `2026-06-27 21:07:17` | `cowrie.command.input` |
| `2026-06-27 21:07:17` | `cowrie.log.closed` |
| `2026-06-27 21:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d08e9b3c5b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:08 |
| **Last Seen** | 2026-06-27 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:08:13` | `cowrie.session.connect` |
| `2026-06-27 21:08:13` | `cowrie.client.version` |
| `2026-06-27 21:08:13` | `cowrie.client.kex` |
| `2026-06-27 21:08:13` | `cowrie.login.success` |
| `2026-06-27 21:08:14` | `cowrie.session.params` |
| `2026-06-27 21:08:14` | `cowrie.command.input` |
| `2026-06-27 21:08:14` | `cowrie.log.closed` |
| `2026-06-27 21:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f3cbd52db9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:09 |
| **Last Seen** | 2026-06-27 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:09:11` | `cowrie.session.connect` |
| `2026-06-27 21:09:11` | `cowrie.client.version` |
| `2026-06-27 21:09:11` | `cowrie.client.kex` |
| `2026-06-27 21:09:11` | `cowrie.login.success` |
| `2026-06-27 21:09:12` | `cowrie.session.params` |
| `2026-06-27 21:09:12` | `cowrie.command.input` |
| `2026-06-27 21:09:12` | `cowrie.log.closed` |
| `2026-06-27 21:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1da35f5db99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:10 |
| **Last Seen** | 2026-06-27 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:10:10` | `cowrie.session.connect` |
| `2026-06-27 21:10:10` | `cowrie.client.version` |
| `2026-06-27 21:10:10` | `cowrie.client.kex` |
| `2026-06-27 21:10:10` | `cowrie.login.success` |
| `2026-06-27 21:10:11` | `cowrie.session.params` |
| `2026-06-27 21:10:11` | `cowrie.command.input` |
| `2026-06-27 21:10:11` | `cowrie.log.closed` |
| `2026-06-27 21:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1675d689fba1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:11 |
| **Last Seen** | 2026-06-27 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:11:08` | `cowrie.session.connect` |
| `2026-06-27 21:11:08` | `cowrie.client.version` |
| `2026-06-27 21:11:08` | `cowrie.client.kex` |
| `2026-06-27 21:11:09` | `cowrie.login.success` |
| `2026-06-27 21:11:10` | `cowrie.session.params` |
| `2026-06-27 21:11:10` | `cowrie.command.input` |
| `2026-06-27 21:11:10` | `cowrie.log.closed` |
| `2026-06-27 21:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ef8f035afb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:12 |
| **Last Seen** | 2026-06-27 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:12:09` | `cowrie.session.connect` |
| `2026-06-27 21:12:09` | `cowrie.client.version` |
| `2026-06-27 21:12:09` | `cowrie.client.kex` |
| `2026-06-27 21:12:10` | `cowrie.login.success` |
| `2026-06-27 21:12:10` | `cowrie.session.params` |
| `2026-06-27 21:12:10` | `cowrie.command.input` |
| `2026-06-27 21:12:10` | `cowrie.log.closed` |
| `2026-06-27 21:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ee25b5cdfe

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 21:12 |
| **Last Seen** | 2026-06-27 21:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:12:40` | `cowrie.session.connect` |
| `2026-06-27 21:12:40` | `cowrie.client.version` |
| `2026-06-27 21:12:40` | `cowrie.client.kex` |
| `2026-06-27 21:12:42` | `cowrie.login.success` |
| `2026-06-27 21:12:44` | `cowrie.session.params` |
| `2026-06-27 21:12:44` | `cowrie.command.input` |
| `2026-06-27 21:12:44` | `cowrie.log.closed` |
| `2026-06-27 21:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022c715c2931

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:13 |
| **Last Seen** | 2026-06-27 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:13:06` | `cowrie.session.connect` |
| `2026-06-27 21:13:06` | `cowrie.client.version` |
| `2026-06-27 21:13:06` | `cowrie.client.kex` |
| `2026-06-27 21:13:07` | `cowrie.login.success` |
| `2026-06-27 21:13:07` | `cowrie.session.params` |
| `2026-06-27 21:13:07` | `cowrie.command.input` |
| `2026-06-27 21:13:08` | `cowrie.log.closed` |
| `2026-06-27 21:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e22aade4aa6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:14 |
| **Last Seen** | 2026-06-27 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:14:03` | `cowrie.session.connect` |
| `2026-06-27 21:14:03` | `cowrie.client.version` |
| `2026-06-27 21:14:03` | `cowrie.client.kex` |
| `2026-06-27 21:14:03` | `cowrie.login.success` |
| `2026-06-27 21:14:04` | `cowrie.session.params` |
| `2026-06-27 21:14:04` | `cowrie.command.input` |
| `2026-06-27 21:14:04` | `cowrie.log.closed` |
| `2026-06-27 21:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35c8244b8063

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:15 |
| **Last Seen** | 2026-06-27 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:15:00` | `cowrie.session.connect` |
| `2026-06-27 21:15:00` | `cowrie.client.version` |
| `2026-06-27 21:15:01` | `cowrie.client.kex` |
| `2026-06-27 21:15:01` | `cowrie.login.success` |
| `2026-06-27 21:15:02` | `cowrie.session.params` |
| `2026-06-27 21:15:02` | `cowrie.command.input` |
| `2026-06-27 21:15:02` | `cowrie.log.closed` |
| `2026-06-27 21:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b7e75062f19

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 21:15 |
| **Last Seen** | 2026-06-27 21:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:15:51` | `cowrie.session.connect` |
| `2026-06-27 21:15:53` | `cowrie.client.version` |
| `2026-06-27 21:15:53` | `cowrie.client.kex` |
| `2026-06-27 21:15:59` | `cowrie.login.success` |
| `2026-06-27 21:16:02` | `cowrie.session.params` |
| `2026-06-27 21:16:02` | `cowrie.command.input` |
| `2026-06-27 21:16:04` | `cowrie.log.closed` |
| `2026-06-27 21:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b26e5448161

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:15 |
| **Last Seen** | 2026-06-27 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:15:59` | `cowrie.session.connect` |
| `2026-06-27 21:15:59` | `cowrie.client.version` |
| `2026-06-27 21:15:59` | `cowrie.client.kex` |
| `2026-06-27 21:16:00` | `cowrie.login.success` |
| `2026-06-27 21:16:00` | `cowrie.session.params` |
| `2026-06-27 21:16:00` | `cowrie.command.input` |
| `2026-06-27 21:16:00` | `cowrie.log.closed` |
| `2026-06-27 21:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f01eae42bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:17 |
| **Last Seen** | 2026-06-27 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:17:00` | `cowrie.session.connect` |
| `2026-06-27 21:17:00` | `cowrie.client.version` |
| `2026-06-27 21:17:00` | `cowrie.client.kex` |
| `2026-06-27 21:17:00` | `cowrie.login.success` |
| `2026-06-27 21:17:01` | `cowrie.session.params` |
| `2026-06-27 21:17:01` | `cowrie.command.input` |
| `2026-06-27 21:17:01` | `cowrie.log.closed` |
| `2026-06-27 21:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca8fb224e50

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:18 |
| **Last Seen** | 2026-06-27 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:18:00` | `cowrie.session.connect` |
| `2026-06-27 21:18:00` | `cowrie.client.version` |
| `2026-06-27 21:18:00` | `cowrie.client.kex` |
| `2026-06-27 21:18:00` | `cowrie.login.success` |
| `2026-06-27 21:18:01` | `cowrie.session.params` |
| `2026-06-27 21:18:01` | `cowrie.command.input` |
| `2026-06-27 21:18:01` | `cowrie.log.closed` |
| `2026-06-27 21:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3bfe0e5f60c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:18 |
| **Last Seen** | 2026-06-27 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:18:58` | `cowrie.session.connect` |
| `2026-06-27 21:18:58` | `cowrie.client.version` |
| `2026-06-27 21:18:58` | `cowrie.client.kex` |
| `2026-06-27 21:18:59` | `cowrie.login.success` |
| `2026-06-27 21:18:59` | `cowrie.session.params` |
| `2026-06-27 21:18:59` | `cowrie.command.input` |
| `2026-06-27 21:19:00` | `cowrie.log.closed` |
| `2026-06-27 21:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849898afbdf1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:19 |
| **Last Seen** | 2026-06-27 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:19:56` | `cowrie.session.connect` |
| `2026-06-27 21:19:56` | `cowrie.client.version` |
| `2026-06-27 21:19:56` | `cowrie.client.kex` |
| `2026-06-27 21:19:57` | `cowrie.login.success` |
| `2026-06-27 21:19:57` | `cowrie.session.params` |
| `2026-06-27 21:19:57` | `cowrie.command.input` |
| `2026-06-27 21:19:58` | `cowrie.log.closed` |
| `2026-06-27 21:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4adf8dac5fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:20 |
| **Last Seen** | 2026-06-27 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:20:59` | `cowrie.session.connect` |
| `2026-06-27 21:20:59` | `cowrie.client.version` |
| `2026-06-27 21:21:00` | `cowrie.client.kex` |
| `2026-06-27 21:21:00` | `cowrie.login.success` |
| `2026-06-27 21:21:00` | `cowrie.session.params` |
| `2026-06-27 21:21:00` | `cowrie.command.input` |
| `2026-06-27 21:21:01` | `cowrie.log.closed` |
| `2026-06-27 21:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c444aabaa486

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:22 |
| **Last Seen** | 2026-06-27 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:22:02` | `cowrie.session.connect` |
| `2026-06-27 21:22:02` | `cowrie.client.version` |
| `2026-06-27 21:22:03` | `cowrie.client.kex` |
| `2026-06-27 21:22:03` | `cowrie.login.success` |
| `2026-06-27 21:22:04` | `cowrie.session.params` |
| `2026-06-27 21:22:04` | `cowrie.command.input` |
| `2026-06-27 21:22:04` | `cowrie.log.closed` |
| `2026-06-27 21:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828765a53b0d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:23 |
| **Last Seen** | 2026-06-27 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:23:05` | `cowrie.session.connect` |
| `2026-06-27 21:23:05` | `cowrie.client.version` |
| `2026-06-27 21:23:05` | `cowrie.client.kex` |
| `2026-06-27 21:23:06` | `cowrie.login.success` |
| `2026-06-27 21:23:06` | `cowrie.session.params` |
| `2026-06-27 21:23:06` | `cowrie.command.input` |
| `2026-06-27 21:23:07` | `cowrie.log.closed` |
| `2026-06-27 21:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-631264ed9808

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:24 |
| **Last Seen** | 2026-06-27 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:24:08` | `cowrie.session.connect` |
| `2026-06-27 21:24:08` | `cowrie.client.version` |
| `2026-06-27 21:24:08` | `cowrie.client.kex` |
| `2026-06-27 21:24:08` | `cowrie.login.success` |
| `2026-06-27 21:24:09` | `cowrie.session.params` |
| `2026-06-27 21:24:09` | `cowrie.command.input` |
| `2026-06-27 21:24:09` | `cowrie.log.closed` |
| `2026-06-27 21:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a99b618171

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:25 |
| **Last Seen** | 2026-06-27 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:25:10` | `cowrie.session.connect` |
| `2026-06-27 21:25:10` | `cowrie.client.version` |
| `2026-06-27 21:25:10` | `cowrie.client.kex` |
| `2026-06-27 21:25:10` | `cowrie.login.success` |
| `2026-06-27 21:25:11` | `cowrie.session.params` |
| `2026-06-27 21:25:11` | `cowrie.command.input` |
| `2026-06-27 21:25:11` | `cowrie.log.closed` |
| `2026-06-27 21:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eed0a5dce98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:26 |
| **Last Seen** | 2026-06-27 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:26:11` | `cowrie.session.connect` |
| `2026-06-27 21:26:11` | `cowrie.client.version` |
| `2026-06-27 21:26:11` | `cowrie.client.kex` |
| `2026-06-27 21:26:11` | `cowrie.login.success` |
| `2026-06-27 21:26:12` | `cowrie.session.params` |
| `2026-06-27 21:26:12` | `cowrie.command.input` |
| `2026-06-27 21:26:12` | `cowrie.log.closed` |
| `2026-06-27 21:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5172d0720cd3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:27 |
| **Last Seen** | 2026-06-27 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:27:12` | `cowrie.session.connect` |
| `2026-06-27 21:27:12` | `cowrie.client.version` |
| `2026-06-27 21:27:12` | `cowrie.client.kex` |
| `2026-06-27 21:27:13` | `cowrie.login.success` |
| `2026-06-27 21:27:14` | `cowrie.session.params` |
| `2026-06-27 21:27:14` | `cowrie.command.input` |
| `2026-06-27 21:27:14` | `cowrie.log.closed` |
| `2026-06-27 21:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5757449fe9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 21:27 |
| **Last Seen** | 2026-06-27 21:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:27:20` | `cowrie.session.connect` |
| `2026-06-27 21:27:20` | `cowrie.client.version` |
| `2026-06-27 21:27:20` | `cowrie.client.kex` |
| `2026-06-27 21:27:22` | `cowrie.login.success` |
| `2026-06-27 21:27:24` | `cowrie.session.params` |
| `2026-06-27 21:27:24` | `cowrie.command.input` |
| `2026-06-27 21:27:25` | `cowrie.log.closed` |
| `2026-06-27 21:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bdd772096e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 21:27 |
| **Last Seen** | 2026-06-27 21:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:27:35` | `cowrie.session.connect` |
| `2026-06-27 21:27:36` | `cowrie.client.version` |
| `2026-06-27 21:27:36` | `cowrie.client.kex` |
| `2026-06-27 21:27:42` | `cowrie.login.success` |
| `2026-06-27 21:27:45` | `cowrie.session.params` |
| `2026-06-27 21:27:45` | `cowrie.command.input` |
| `2026-06-27 21:27:47` | `cowrie.log.closed` |
| `2026-06-27 21:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871fbbafd585

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:28 |
| **Last Seen** | 2026-06-27 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:28:19` | `cowrie.session.connect` |
| `2026-06-27 21:28:19` | `cowrie.client.version` |
| `2026-06-27 21:28:19` | `cowrie.client.kex` |
| `2026-06-27 21:28:20` | `cowrie.login.success` |
| `2026-06-27 21:28:20` | `cowrie.session.params` |
| `2026-06-27 21:28:20` | `cowrie.command.input` |
| `2026-06-27 21:28:20` | `cowrie.log.closed` |
| `2026-06-27 21:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ece9b9faef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:29 |
| **Last Seen** | 2026-06-27 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:29:24` | `cowrie.session.connect` |
| `2026-06-27 21:29:24` | `cowrie.client.version` |
| `2026-06-27 21:29:25` | `cowrie.client.kex` |
| `2026-06-27 21:29:25` | `cowrie.login.success` |
| `2026-06-27 21:29:26` | `cowrie.session.params` |
| `2026-06-27 21:29:26` | `cowrie.command.input` |
| `2026-06-27 21:29:26` | `cowrie.log.closed` |
| `2026-06-27 21:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3b89ed548a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:30 |
| **Last Seen** | 2026-06-27 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:30:29` | `cowrie.session.connect` |
| `2026-06-27 21:30:29` | `cowrie.client.version` |
| `2026-06-27 21:30:29` | `cowrie.client.kex` |
| `2026-06-27 21:30:30` | `cowrie.login.success` |
| `2026-06-27 21:30:30` | `cowrie.session.params` |
| `2026-06-27 21:30:30` | `cowrie.command.input` |
| `2026-06-27 21:30:30` | `cowrie.log.closed` |
| `2026-06-27 21:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db99b460028e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:31 |
| **Last Seen** | 2026-06-27 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:31:33` | `cowrie.session.connect` |
| `2026-06-27 21:31:33` | `cowrie.client.version` |
| `2026-06-27 21:31:33` | `cowrie.client.kex` |
| `2026-06-27 21:31:34` | `cowrie.login.success` |
| `2026-06-27 21:31:35` | `cowrie.session.params` |
| `2026-06-27 21:31:35` | `cowrie.command.input` |
| `2026-06-27 21:31:35` | `cowrie.log.closed` |
| `2026-06-27 21:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f029c96f9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:32 |
| **Last Seen** | 2026-06-27 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:32:37` | `cowrie.session.connect` |
| `2026-06-27 21:32:37` | `cowrie.client.version` |
| `2026-06-27 21:32:37` | `cowrie.client.kex` |
| `2026-06-27 21:32:37` | `cowrie.login.success` |
| `2026-06-27 21:32:38` | `cowrie.session.params` |
| `2026-06-27 21:32:38` | `cowrie.command.input` |
| `2026-06-27 21:32:38` | `cowrie.log.closed` |
| `2026-06-27 21:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5ba1a1f315

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:33 |
| **Last Seen** | 2026-06-27 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:33:40` | `cowrie.session.connect` |
| `2026-06-27 21:33:40` | `cowrie.client.version` |
| `2026-06-27 21:33:40` | `cowrie.client.kex` |
| `2026-06-27 21:33:40` | `cowrie.login.success` |
| `2026-06-27 21:33:41` | `cowrie.session.params` |
| `2026-06-27 21:33:41` | `cowrie.command.input` |
| `2026-06-27 21:33:41` | `cowrie.log.closed` |
| `2026-06-27 21:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b278e17da2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:34 |
| **Last Seen** | 2026-06-27 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:34:45` | `cowrie.session.connect` |
| `2026-06-27 21:34:45` | `cowrie.client.version` |
| `2026-06-27 21:34:45` | `cowrie.client.kex` |
| `2026-06-27 21:34:46` | `cowrie.login.success` |
| `2026-06-27 21:34:46` | `cowrie.session.params` |
| `2026-06-27 21:34:46` | `cowrie.command.input` |
| `2026-06-27 21:34:47` | `cowrie.log.closed` |
| `2026-06-27 21:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4889897f4c6c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:35 |
| **Last Seen** | 2026-06-27 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:35:52` | `cowrie.session.connect` |
| `2026-06-27 21:35:52` | `cowrie.client.version` |
| `2026-06-27 21:35:52` | `cowrie.client.kex` |
| `2026-06-27 21:35:53` | `cowrie.login.success` |
| `2026-06-27 21:35:53` | `cowrie.session.params` |
| `2026-06-27 21:35:53` | `cowrie.command.input` |
| `2026-06-27 21:35:53` | `cowrie.log.closed` |
| `2026-06-27 21:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e295919191

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:36 |
| **Last Seen** | 2026-06-27 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:36:58` | `cowrie.session.connect` |
| `2026-06-27 21:36:58` | `cowrie.client.version` |
| `2026-06-27 21:36:58` | `cowrie.client.kex` |
| `2026-06-27 21:36:58` | `cowrie.login.success` |
| `2026-06-27 21:36:59` | `cowrie.session.params` |
| `2026-06-27 21:36:59` | `cowrie.command.input` |
| `2026-06-27 21:36:59` | `cowrie.log.closed` |
| `2026-06-27 21:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63171d79b970

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:38 |
| **Last Seen** | 2026-06-27 21:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:38:03` | `cowrie.session.connect` |
| `2026-06-27 21:38:03` | `cowrie.client.version` |
| `2026-06-27 21:38:03` | `cowrie.client.kex` |
| `2026-06-27 21:38:03` | `cowrie.login.success` |
| `2026-06-27 21:38:04` | `cowrie.session.params` |
| `2026-06-27 21:38:04` | `cowrie.command.input` |
| `2026-06-27 21:38:04` | `cowrie.log.closed` |
| `2026-06-27 21:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81da57d7dd5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:39 |
| **Last Seen** | 2026-06-27 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:39:07` | `cowrie.session.connect` |
| `2026-06-27 21:39:07` | `cowrie.client.version` |
| `2026-06-27 21:39:07` | `cowrie.client.kex` |
| `2026-06-27 21:39:07` | `cowrie.login.success` |
| `2026-06-27 21:39:08` | `cowrie.session.params` |
| `2026-06-27 21:39:08` | `cowrie.command.input` |
| `2026-06-27 21:39:08` | `cowrie.log.closed` |
| `2026-06-27 21:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7da2523845

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 21:39 |
| **Last Seen** | 2026-06-27 21:39 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:39:46` | `cowrie.session.connect` |
| `2026-06-27 21:39:48` | `cowrie.client.version` |
| `2026-06-27 21:39:48` | `cowrie.client.kex` |
| `2026-06-27 21:39:54` | `cowrie.login.success` |
| `2026-06-27 21:39:58` | `cowrie.session.params` |
| `2026-06-27 21:39:58` | `cowrie.command.input` |
| `2026-06-27 21:39:59` | `cowrie.log.closed` |
| `2026-06-27 21:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20715b5f54ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:40 |
| **Last Seen** | 2026-06-27 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:40:13` | `cowrie.session.connect` |
| `2026-06-27 21:40:13` | `cowrie.client.version` |
| `2026-06-27 21:40:13` | `cowrie.client.kex` |
| `2026-06-27 21:40:13` | `cowrie.login.success` |
| `2026-06-27 21:40:14` | `cowrie.session.params` |
| `2026-06-27 21:40:14` | `cowrie.command.input` |
| `2026-06-27 21:40:14` | `cowrie.log.closed` |
| `2026-06-27 21:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09debbe48479

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:41 |
| **Last Seen** | 2026-06-27 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:41:20` | `cowrie.session.connect` |
| `2026-06-27 21:41:20` | `cowrie.client.version` |
| `2026-06-27 21:41:20` | `cowrie.client.kex` |
| `2026-06-27 21:41:20` | `cowrie.login.success` |
| `2026-06-27 21:41:21` | `cowrie.session.params` |
| `2026-06-27 21:41:21` | `cowrie.command.input` |
| `2026-06-27 21:41:21` | `cowrie.log.closed` |
| `2026-06-27 21:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2117fbff67

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 21:41 |
| **Last Seen** | 2026-06-27 21:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:41:51` | `cowrie.session.connect` |
| `2026-06-27 21:41:51` | `cowrie.client.version` |
| `2026-06-27 21:41:51` | `cowrie.client.kex` |
| `2026-06-27 21:41:52` | `cowrie.login.success` |
| `2026-06-27 21:41:54` | `cowrie.session.params` |
| `2026-06-27 21:41:54` | `cowrie.command.input` |
| `2026-06-27 21:41:54` | `cowrie.log.closed` |
| `2026-06-27 21:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d01e2e8db46

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:42 |
| **Last Seen** | 2026-06-27 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:42:28` | `cowrie.session.connect` |
| `2026-06-27 21:42:28` | `cowrie.client.version` |
| `2026-06-27 21:42:28` | `cowrie.client.kex` |
| `2026-06-27 21:42:28` | `cowrie.login.success` |
| `2026-06-27 21:42:29` | `cowrie.session.params` |
| `2026-06-27 21:42:29` | `cowrie.command.input` |
| `2026-06-27 21:42:29` | `cowrie.log.closed` |
| `2026-06-27 21:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac704fcca4ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:43 |
| **Last Seen** | 2026-06-27 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:43:34` | `cowrie.session.connect` |
| `2026-06-27 21:43:34` | `cowrie.client.version` |
| `2026-06-27 21:43:34` | `cowrie.client.kex` |
| `2026-06-27 21:43:35` | `cowrie.login.success` |
| `2026-06-27 21:43:35` | `cowrie.session.params` |
| `2026-06-27 21:43:35` | `cowrie.command.input` |
| `2026-06-27 21:43:36` | `cowrie.log.closed` |
| `2026-06-27 21:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643f62e51d6e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:44 |
| **Last Seen** | 2026-06-27 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:44:39` | `cowrie.session.connect` |
| `2026-06-27 21:44:39` | `cowrie.client.version` |
| `2026-06-27 21:44:39` | `cowrie.client.kex` |
| `2026-06-27 21:44:40` | `cowrie.login.success` |
| `2026-06-27 21:44:40` | `cowrie.session.params` |
| `2026-06-27 21:44:40` | `cowrie.command.input` |
| `2026-06-27 21:44:40` | `cowrie.log.closed` |
| `2026-06-27 21:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cb24bedfa1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:45 |
| **Last Seen** | 2026-06-27 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:45:45` | `cowrie.session.connect` |
| `2026-06-27 21:45:45` | `cowrie.client.version` |
| `2026-06-27 21:45:45` | `cowrie.client.kex` |
| `2026-06-27 21:45:45` | `cowrie.login.success` |
| `2026-06-27 21:45:46` | `cowrie.session.params` |
| `2026-06-27 21:45:46` | `cowrie.command.input` |
| `2026-06-27 21:45:46` | `cowrie.log.closed` |
| `2026-06-27 21:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-968c70d09353

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:46 |
| **Last Seen** | 2026-06-27 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:46:51` | `cowrie.session.connect` |
| `2026-06-27 21:46:51` | `cowrie.client.version` |
| `2026-06-27 21:46:51` | `cowrie.client.kex` |
| `2026-06-27 21:46:51` | `cowrie.login.success` |
| `2026-06-27 21:46:52` | `cowrie.session.params` |
| `2026-06-27 21:46:52` | `cowrie.command.input` |
| `2026-06-27 21:46:52` | `cowrie.log.closed` |
| `2026-06-27 21:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37d00db4bcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:47 |
| **Last Seen** | 2026-06-27 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:47:59` | `cowrie.session.connect` |
| `2026-06-27 21:47:59` | `cowrie.client.version` |
| `2026-06-27 21:47:59` | `cowrie.client.kex` |
| `2026-06-27 21:47:59` | `cowrie.login.success` |
| `2026-06-27 21:48:00` | `cowrie.session.params` |
| `2026-06-27 21:48:00` | `cowrie.command.input` |
| `2026-06-27 21:48:00` | `cowrie.log.closed` |
| `2026-06-27 21:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda01e29b57d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:49 |
| **Last Seen** | 2026-06-27 21:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:49:09` | `cowrie.session.connect` |
| `2026-06-27 21:49:09` | `cowrie.client.version` |
| `2026-06-27 21:49:09` | `cowrie.client.kex` |
| `2026-06-27 21:49:09` | `cowrie.login.success` |
| `2026-06-27 21:49:10` | `cowrie.session.params` |
| `2026-06-27 21:49:10` | `cowrie.command.input` |
| `2026-06-27 21:49:10` | `cowrie.log.closed` |
| `2026-06-27 21:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9707f74ab840

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:50 |
| **Last Seen** | 2026-06-27 21:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:50:18` | `cowrie.session.connect` |
| `2026-06-27 21:50:18` | `cowrie.client.version` |
| `2026-06-27 21:50:19` | `cowrie.client.kex` |
| `2026-06-27 21:50:19` | `cowrie.login.success` |
| `2026-06-27 21:50:20` | `cowrie.session.params` |
| `2026-06-27 21:50:20` | `cowrie.command.input` |
| `2026-06-27 21:50:20` | `cowrie.log.closed` |
| `2026-06-27 21:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a8cfc39718

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:51 |
| **Last Seen** | 2026-06-27 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:51:26` | `cowrie.session.connect` |
| `2026-06-27 21:51:26` | `cowrie.client.version` |
| `2026-06-27 21:51:27` | `cowrie.client.kex` |
| `2026-06-27 21:51:27` | `cowrie.login.success` |
| `2026-06-27 21:51:28` | `cowrie.session.params` |
| `2026-06-27 21:51:28` | `cowrie.command.input` |
| `2026-06-27 21:51:28` | `cowrie.log.closed` |
| `2026-06-27 21:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8782dab25279

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 21:51 |
| **Last Seen** | 2026-06-27 21:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:51:32` | `cowrie.session.connect` |
| `2026-06-27 21:51:33` | `cowrie.client.version` |
| `2026-06-27 21:51:33` | `cowrie.client.kex` |
| `2026-06-27 21:51:39` | `cowrie.login.success` |
| `2026-06-27 21:51:42` | `cowrie.session.params` |
| `2026-06-27 21:51:42` | `cowrie.command.input` |
| `2026-06-27 21:51:43` | `cowrie.log.closed` |
| `2026-06-27 21:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-417702316c62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:52 |
| **Last Seen** | 2026-06-27 21:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:52:33` | `cowrie.session.connect` |
| `2026-06-27 21:52:33` | `cowrie.client.version` |
| `2026-06-27 21:52:33` | `cowrie.client.kex` |
| `2026-06-27 21:52:33` | `cowrie.login.success` |
| `2026-06-27 21:52:34` | `cowrie.session.params` |
| `2026-06-27 21:52:34` | `cowrie.command.input` |
| `2026-06-27 21:52:34` | `cowrie.log.closed` |
| `2026-06-27 21:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ef2dbdce59

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:53 |
| **Last Seen** | 2026-06-27 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:53:40` | `cowrie.session.connect` |
| `2026-06-27 21:53:40` | `cowrie.client.version` |
| `2026-06-27 21:53:40` | `cowrie.client.kex` |
| `2026-06-27 21:53:41` | `cowrie.login.success` |
| `2026-06-27 21:53:42` | `cowrie.session.params` |
| `2026-06-27 21:53:42` | `cowrie.command.input` |
| `2026-06-27 21:53:42` | `cowrie.log.closed` |
| `2026-06-27 21:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd6ae73dc47

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:54 |
| **Last Seen** | 2026-06-27 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:54:50` | `cowrie.session.connect` |
| `2026-06-27 21:54:50` | `cowrie.client.version` |
| `2026-06-27 21:54:50` | `cowrie.client.kex` |
| `2026-06-27 21:54:50` | `cowrie.login.success` |
| `2026-06-27 21:54:51` | `cowrie.session.params` |
| `2026-06-27 21:54:51` | `cowrie.command.input` |
| `2026-06-27 21:54:51` | `cowrie.log.closed` |
| `2026-06-27 21:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee024ad1f05d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:56 |
| **Last Seen** | 2026-06-27 21:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:56:00` | `cowrie.session.connect` |
| `2026-06-27 21:56:00` | `cowrie.client.version` |
| `2026-06-27 21:56:00` | `cowrie.client.kex` |
| `2026-06-27 21:56:01` | `cowrie.login.success` |
| `2026-06-27 21:56:02` | `cowrie.session.params` |
| `2026-06-27 21:56:02` | `cowrie.command.input` |
| `2026-06-27 21:56:02` | `cowrie.log.closed` |
| `2026-06-27 21:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7a2d87f908

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 21:56 |
| **Last Seen** | 2026-06-27 21:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:56:24` | `cowrie.session.connect` |
| `2026-06-27 21:56:24` | `cowrie.client.version` |
| `2026-06-27 21:56:24` | `cowrie.client.kex` |
| `2026-06-27 21:56:26` | `cowrie.login.success` |
| `2026-06-27 21:56:27` | `cowrie.session.params` |
| `2026-06-27 21:56:27` | `cowrie.command.input` |
| `2026-06-27 21:56:27` | `cowrie.log.closed` |
| `2026-06-27 21:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7229c49053ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:57 |
| **Last Seen** | 2026-06-27 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:57:10` | `cowrie.session.connect` |
| `2026-06-27 21:57:10` | `cowrie.client.version` |
| `2026-06-27 21:57:10` | `cowrie.client.kex` |
| `2026-06-27 21:57:11` | `cowrie.login.success` |
| `2026-06-27 21:57:12` | `cowrie.session.params` |
| `2026-06-27 21:57:12` | `cowrie.command.input` |
| `2026-06-27 21:57:12` | `cowrie.log.closed` |
| `2026-06-27 21:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0d8c171863

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:58 |
| **Last Seen** | 2026-06-27 21:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:58:17` | `cowrie.session.connect` |
| `2026-06-27 21:58:17` | `cowrie.client.version` |
| `2026-06-27 21:58:18` | `cowrie.client.kex` |
| `2026-06-27 21:58:18` | `cowrie.login.success` |
| `2026-06-27 21:58:19` | `cowrie.session.params` |
| `2026-06-27 21:58:19` | `cowrie.command.input` |
| `2026-06-27 21:58:19` | `cowrie.log.closed` |
| `2026-06-27 21:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e925ecd1f308

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 21:59 |
| **Last Seen** | 2026-06-27 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 21:59:26` | `cowrie.session.connect` |
| `2026-06-27 21:59:26` | `cowrie.client.version` |
| `2026-06-27 21:59:26` | `cowrie.client.kex` |
| `2026-06-27 21:59:27` | `cowrie.login.success` |
| `2026-06-27 21:59:28` | `cowrie.session.params` |
| `2026-06-27 21:59:28` | `cowrie.command.input` |
| `2026-06-27 21:59:28` | `cowrie.log.closed` |
| `2026-06-27 21:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f3c06c6b94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:00 |
| **Last Seen** | 2026-06-27 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:00:29` | `cowrie.session.connect` |
| `2026-06-27 22:00:29` | `cowrie.client.version` |
| `2026-06-27 22:00:29` | `cowrie.client.kex` |
| `2026-06-27 22:00:29` | `cowrie.login.success` |
| `2026-06-27 22:00:30` | `cowrie.session.params` |
| `2026-06-27 22:00:30` | `cowrie.command.input` |
| `2026-06-27 22:00:30` | `cowrie.log.closed` |
| `2026-06-27 22:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab02261cc9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:01 |
| **Last Seen** | 2026-06-27 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:01:15` | `cowrie.session.connect` |
| `2026-06-27 22:01:15` | `cowrie.client.version` |
| `2026-06-27 22:01:15` | `cowrie.client.kex` |
| `2026-06-27 22:01:15` | `cowrie.login.success` |
| `2026-06-27 22:01:16` | `cowrie.session.params` |
| `2026-06-27 22:01:16` | `cowrie.command.input` |
| `2026-06-27 22:01:16` | `cowrie.log.closed` |
| `2026-06-27 22:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18b02fab0f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:02 |
| **Last Seen** | 2026-06-27 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:02:00` | `cowrie.session.connect` |
| `2026-06-27 22:02:00` | `cowrie.client.version` |
| `2026-06-27 22:02:00` | `cowrie.client.kex` |
| `2026-06-27 22:02:01` | `cowrie.login.success` |
| `2026-06-27 22:02:02` | `cowrie.session.params` |
| `2026-06-27 22:02:02` | `cowrie.command.input` |
| `2026-06-27 22:02:02` | `cowrie.log.closed` |
| `2026-06-27 22:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6a4253637b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:02 |
| **Last Seen** | 2026-06-27 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:02:45` | `cowrie.session.connect` |
| `2026-06-27 22:02:45` | `cowrie.client.version` |
| `2026-06-27 22:02:46` | `cowrie.client.kex` |
| `2026-06-27 22:02:46` | `cowrie.login.success` |
| `2026-06-27 22:02:47` | `cowrie.session.params` |
| `2026-06-27 22:02:47` | `cowrie.command.input` |
| `2026-06-27 22:02:47` | `cowrie.log.closed` |
| `2026-06-27 22:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee84cf42fd3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 22:03 |
| **Last Seen** | 2026-06-27 22:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:03:21` | `cowrie.session.connect` |
| `2026-06-27 22:03:22` | `cowrie.client.version` |
| `2026-06-27 22:03:22` | `cowrie.client.kex` |
| `2026-06-27 22:03:29` | `cowrie.login.success` |
| `2026-06-27 22:03:32` | `cowrie.session.params` |
| `2026-06-27 22:03:32` | `cowrie.command.input` |
| `2026-06-27 22:03:33` | `cowrie.log.closed` |
| `2026-06-27 22:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0da5d2038821

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:03 |
| **Last Seen** | 2026-06-27 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:03:30` | `cowrie.session.connect` |
| `2026-06-27 22:03:30` | `cowrie.client.version` |
| `2026-06-27 22:03:30` | `cowrie.client.kex` |
| `2026-06-27 22:03:31` | `cowrie.login.success` |
| `2026-06-27 22:03:31` | `cowrie.session.params` |
| `2026-06-27 22:03:31` | `cowrie.command.input` |
| `2026-06-27 22:03:32` | `cowrie.log.closed` |
| `2026-06-27 22:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e6ae8541f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:04 |
| **Last Seen** | 2026-06-27 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:04:14` | `cowrie.session.connect` |
| `2026-06-27 22:04:14` | `cowrie.client.version` |
| `2026-06-27 22:04:14` | `cowrie.client.kex` |
| `2026-06-27 22:04:14` | `cowrie.login.success` |
| `2026-06-27 22:04:15` | `cowrie.session.params` |
| `2026-06-27 22:04:15` | `cowrie.command.input` |
| `2026-06-27 22:04:15` | `cowrie.log.closed` |
| `2026-06-27 22:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c35aa6ae8e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:04 |
| **Last Seen** | 2026-06-27 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:04:58` | `cowrie.session.connect` |
| `2026-06-27 22:04:58` | `cowrie.client.version` |
| `2026-06-27 22:04:58` | `cowrie.client.kex` |
| `2026-06-27 22:04:59` | `cowrie.login.success` |
| `2026-06-27 22:04:59` | `cowrie.session.params` |
| `2026-06-27 22:04:59` | `cowrie.command.input` |
| `2026-06-27 22:04:59` | `cowrie.log.closed` |
| `2026-06-27 22:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e08c96a44a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:05 |
| **Last Seen** | 2026-06-27 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:05:43` | `cowrie.session.connect` |
| `2026-06-27 22:05:43` | `cowrie.client.version` |
| `2026-06-27 22:05:43` | `cowrie.client.kex` |
| `2026-06-27 22:05:44` | `cowrie.login.success` |
| `2026-06-27 22:05:45` | `cowrie.session.params` |
| `2026-06-27 22:05:45` | `cowrie.command.input` |
| `2026-06-27 22:05:45` | `cowrie.log.closed` |
| `2026-06-27 22:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256f37b0f5a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:06 |
| **Last Seen** | 2026-06-27 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:06:30` | `cowrie.session.connect` |
| `2026-06-27 22:06:30` | `cowrie.client.version` |
| `2026-06-27 22:06:30` | `cowrie.client.kex` |
| `2026-06-27 22:06:30` | `cowrie.login.success` |
| `2026-06-27 22:06:31` | `cowrie.session.params` |
| `2026-06-27 22:06:31` | `cowrie.command.input` |
| `2026-06-27 22:06:31` | `cowrie.log.closed` |
| `2026-06-27 22:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34bb4268e2fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:07 |
| **Last Seen** | 2026-06-27 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:07:16` | `cowrie.session.connect` |
| `2026-06-27 22:07:16` | `cowrie.client.version` |
| `2026-06-27 22:07:16` | `cowrie.client.kex` |
| `2026-06-27 22:07:17` | `cowrie.login.success` |
| `2026-06-27 22:07:18` | `cowrie.session.params` |
| `2026-06-27 22:07:18` | `cowrie.command.input` |
| `2026-06-27 22:07:18` | `cowrie.log.closed` |
| `2026-06-27 22:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57bfa9c836e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:08 |
| **Last Seen** | 2026-06-27 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:08:03` | `cowrie.session.connect` |
| `2026-06-27 22:08:03` | `cowrie.client.version` |
| `2026-06-27 22:08:03` | `cowrie.client.kex` |
| `2026-06-27 22:08:04` | `cowrie.login.success` |
| `2026-06-27 22:08:05` | `cowrie.session.params` |
| `2026-06-27 22:08:05` | `cowrie.command.input` |
| `2026-06-27 22:08:05` | `cowrie.log.closed` |
| `2026-06-27 22:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0986e4588a4b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:08 |
| **Last Seen** | 2026-06-27 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:08:50` | `cowrie.session.connect` |
| `2026-06-27 22:08:50` | `cowrie.client.version` |
| `2026-06-27 22:08:50` | `cowrie.client.kex` |
| `2026-06-27 22:08:50` | `cowrie.login.success` |
| `2026-06-27 22:08:51` | `cowrie.session.params` |
| `2026-06-27 22:08:51` | `cowrie.command.input` |
| `2026-06-27 22:08:51` | `cowrie.log.closed` |
| `2026-06-27 22:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bddd983b009

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:09 |
| **Last Seen** | 2026-06-27 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:09:37` | `cowrie.session.connect` |
| `2026-06-27 22:09:37` | `cowrie.client.version` |
| `2026-06-27 22:09:37` | `cowrie.client.kex` |
| `2026-06-27 22:09:37` | `cowrie.login.success` |
| `2026-06-27 22:09:38` | `cowrie.session.params` |
| `2026-06-27 22:09:38` | `cowrie.command.input` |
| `2026-06-27 22:09:38` | `cowrie.log.closed` |
| `2026-06-27 22:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dbfa183e24e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:10 |
| **Last Seen** | 2026-06-27 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:10:23` | `cowrie.session.connect` |
| `2026-06-27 22:10:23` | `cowrie.client.version` |
| `2026-06-27 22:10:23` | `cowrie.client.kex` |
| `2026-06-27 22:10:24` | `cowrie.login.success` |
| `2026-06-27 22:10:25` | `cowrie.session.params` |
| `2026-06-27 22:10:25` | `cowrie.command.input` |
| `2026-06-27 22:10:25` | `cowrie.log.closed` |
| `2026-06-27 22:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6993f8675fbd

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 22:10 |
| **Last Seen** | 2026-06-27 22:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:10:55` | `cowrie.session.connect` |
| `2026-06-27 22:10:57` | `cowrie.client.version` |
| `2026-06-27 22:10:57` | `cowrie.client.kex` |
| `2026-06-27 22:10:58` | `cowrie.login.success` |
| `2026-06-27 22:11:00` | `cowrie.session.params` |
| `2026-06-27 22:11:00` | `cowrie.command.input` |
| `2026-06-27 22:11:00` | `cowrie.log.closed` |
| `2026-06-27 22:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef1100982e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:11 |
| **Last Seen** | 2026-06-27 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:11:09` | `cowrie.session.connect` |
| `2026-06-27 22:11:09` | `cowrie.client.version` |
| `2026-06-27 22:11:10` | `cowrie.client.kex` |
| `2026-06-27 22:11:10` | `cowrie.login.success` |
| `2026-06-27 22:11:11` | `cowrie.session.params` |
| `2026-06-27 22:11:11` | `cowrie.command.input` |
| `2026-06-27 22:11:11` | `cowrie.log.closed` |
| `2026-06-27 22:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c007e1e72e45

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:11 |
| **Last Seen** | 2026-06-27 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:11:57` | `cowrie.session.connect` |
| `2026-06-27 22:11:57` | `cowrie.client.version` |
| `2026-06-27 22:11:57` | `cowrie.client.kex` |
| `2026-06-27 22:11:57` | `cowrie.login.success` |
| `2026-06-27 22:11:58` | `cowrie.session.params` |
| `2026-06-27 22:11:58` | `cowrie.command.input` |
| `2026-06-27 22:11:58` | `cowrie.log.closed` |
| `2026-06-27 22:11:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5d16b220b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:12 |
| **Last Seen** | 2026-06-27 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:12:45` | `cowrie.session.connect` |
| `2026-06-27 22:12:45` | `cowrie.client.version` |
| `2026-06-27 22:12:45` | `cowrie.client.kex` |
| `2026-06-27 22:12:45` | `cowrie.login.success` |
| `2026-06-27 22:12:46` | `cowrie.session.params` |
| `2026-06-27 22:12:46` | `cowrie.command.input` |
| `2026-06-27 22:12:46` | `cowrie.log.closed` |
| `2026-06-27 22:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d61ea773a9ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:13 |
| **Last Seen** | 2026-06-27 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:13:34` | `cowrie.session.connect` |
| `2026-06-27 22:13:34` | `cowrie.client.version` |
| `2026-06-27 22:13:34` | `cowrie.client.kex` |
| `2026-06-27 22:13:35` | `cowrie.login.success` |
| `2026-06-27 22:13:35` | `cowrie.session.params` |
| `2026-06-27 22:13:35` | `cowrie.command.input` |
| `2026-06-27 22:13:36` | `cowrie.log.closed` |
| `2026-06-27 22:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c19ff144e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:14 |
| **Last Seen** | 2026-06-27 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:14:23` | `cowrie.session.connect` |
| `2026-06-27 22:14:23` | `cowrie.client.version` |
| `2026-06-27 22:14:23` | `cowrie.client.kex` |
| `2026-06-27 22:14:24` | `cowrie.login.success` |
| `2026-06-27 22:14:24` | `cowrie.session.params` |
| `2026-06-27 22:14:24` | `cowrie.command.input` |
| `2026-06-27 22:14:24` | `cowrie.log.closed` |
| `2026-06-27 22:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f44082fb465

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:15 |
| **Last Seen** | 2026-06-27 22:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:15:12` | `cowrie.session.connect` |
| `2026-06-27 22:15:12` | `cowrie.client.version` |
| `2026-06-27 22:15:12` | `cowrie.client.kex` |
| `2026-06-27 22:15:12` | `cowrie.login.success` |
| `2026-06-27 22:15:13` | `cowrie.session.params` |
| `2026-06-27 22:15:13` | `cowrie.command.input` |
| `2026-06-27 22:15:13` | `cowrie.log.closed` |
| `2026-06-27 22:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af354cac7d14

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 22:15 |
| **Last Seen** | 2026-06-27 22:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:15:36` | `cowrie.session.connect` |
| `2026-06-27 22:15:38` | `cowrie.client.version` |
| `2026-06-27 22:15:38` | `cowrie.client.kex` |
| `2026-06-27 22:15:43` | `cowrie.login.success` |
| `2026-06-27 22:15:47` | `cowrie.session.params` |
| `2026-06-27 22:15:47` | `cowrie.command.input` |
| `2026-06-27 22:15:49` | `cowrie.log.closed` |
| `2026-06-27 22:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201b923d952b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:16 |
| **Last Seen** | 2026-06-27 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:16:00` | `cowrie.session.connect` |
| `2026-06-27 22:16:00` | `cowrie.client.version` |
| `2026-06-27 22:16:00` | `cowrie.client.kex` |
| `2026-06-27 22:16:00` | `cowrie.login.success` |
| `2026-06-27 22:16:01` | `cowrie.session.params` |
| `2026-06-27 22:16:01` | `cowrie.command.input` |
| `2026-06-27 22:16:01` | `cowrie.log.closed` |
| `2026-06-27 22:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca60dcd1c787

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:16 |
| **Last Seen** | 2026-06-27 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:16:47` | `cowrie.session.connect` |
| `2026-06-27 22:16:47` | `cowrie.client.version` |
| `2026-06-27 22:16:47` | `cowrie.client.kex` |
| `2026-06-27 22:16:47` | `cowrie.login.success` |
| `2026-06-27 22:16:48` | `cowrie.session.params` |
| `2026-06-27 22:16:48` | `cowrie.command.input` |
| `2026-06-27 22:16:48` | `cowrie.log.closed` |
| `2026-06-27 22:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb6f4ddb85c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:17 |
| **Last Seen** | 2026-06-27 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:17:33` | `cowrie.session.connect` |
| `2026-06-27 22:17:33` | `cowrie.client.version` |
| `2026-06-27 22:17:34` | `cowrie.client.kex` |
| `2026-06-27 22:17:34` | `cowrie.login.success` |
| `2026-06-27 22:17:35` | `cowrie.session.params` |
| `2026-06-27 22:17:35` | `cowrie.command.input` |
| `2026-06-27 22:17:35` | `cowrie.log.closed` |
| `2026-06-27 22:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb87c55b2efe

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 22:17 |
| **Last Seen** | 2026-06-27 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:17:47` | `cowrie.session.connect` |
| `2026-06-27 22:17:47` | `cowrie.client.version` |
| `2026-06-27 22:17:47` | `cowrie.client.kex` |
| `2026-06-27 22:17:48` | `cowrie.login.success` |
| `2026-06-27 22:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f25897e8bdc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 22:17 |
| **Last Seen** | 2026-06-27 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:17:47` | `cowrie.session.connect` |
| `2026-06-27 22:17:47` | `cowrie.client.version` |
| `2026-06-27 22:17:48` | `cowrie.client.kex` |
| `2026-06-27 22:17:48` | `cowrie.login.success` |
| `2026-06-27 22:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9d38923d8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:18 |
| **Last Seen** | 2026-06-27 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:18:21` | `cowrie.session.connect` |
| `2026-06-27 22:18:21` | `cowrie.client.version` |
| `2026-06-27 22:18:21` | `cowrie.client.kex` |
| `2026-06-27 22:18:21` | `cowrie.login.success` |
| `2026-06-27 22:18:22` | `cowrie.session.params` |
| `2026-06-27 22:18:22` | `cowrie.command.input` |
| `2026-06-27 22:18:22` | `cowrie.log.closed` |
| `2026-06-27 22:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9df80a9f55c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:19 |
| **Last Seen** | 2026-06-27 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:19:09` | `cowrie.session.connect` |
| `2026-06-27 22:19:09` | `cowrie.client.version` |
| `2026-06-27 22:19:09` | `cowrie.client.kex` |
| `2026-06-27 22:19:10` | `cowrie.login.success` |
| `2026-06-27 22:19:10` | `cowrie.session.params` |
| `2026-06-27 22:19:10` | `cowrie.command.input` |
| `2026-06-27 22:19:11` | `cowrie.log.closed` |
| `2026-06-27 22:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9f23a72cd11

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:19 |
| **Last Seen** | 2026-06-27 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:19:59` | `cowrie.session.connect` |
| `2026-06-27 22:19:59` | `cowrie.client.version` |
| `2026-06-27 22:19:59` | `cowrie.client.kex` |
| `2026-06-27 22:19:59` | `cowrie.login.success` |
| `2026-06-27 22:20:00` | `cowrie.session.params` |
| `2026-06-27 22:20:00` | `cowrie.command.input` |
| `2026-06-27 22:20:00` | `cowrie.log.closed` |
| `2026-06-27 22:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f646e1e25e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:20 |
| **Last Seen** | 2026-06-27 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:20:50` | `cowrie.session.connect` |
| `2026-06-27 22:20:50` | `cowrie.client.version` |
| `2026-06-27 22:20:50` | `cowrie.client.kex` |
| `2026-06-27 22:20:50` | `cowrie.login.success` |
| `2026-06-27 22:20:51` | `cowrie.session.params` |
| `2026-06-27 22:20:51` | `cowrie.command.input` |
| `2026-06-27 22:20:51` | `cowrie.log.closed` |
| `2026-06-27 22:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e39f1dc9bab

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 22:21 |
| **Last Seen** | 2026-06-27 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:21:32` | `cowrie.session.connect` |
| `2026-06-27 22:21:32` | `cowrie.client.version` |
| `2026-06-27 22:21:32` | `cowrie.client.kex` |
| `2026-06-27 22:21:32` | `cowrie.login.success` |
| `2026-06-27 22:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e8987ba27e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 22:21 |
| **Last Seen** | 2026-06-27 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:21:33` | `cowrie.session.connect` |
| `2026-06-27 22:21:33` | `cowrie.client.version` |
| `2026-06-27 22:21:33` | `cowrie.client.kex` |
| `2026-06-27 22:21:33` | `cowrie.login.success` |
| `2026-06-27 22:21:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7b7df10fbf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 22:21 |
| **Last Seen** | 2026-06-27 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:21:34` | `cowrie.session.connect` |
| `2026-06-27 22:21:34` | `cowrie.client.version` |
| `2026-06-27 22:21:34` | `cowrie.client.kex` |
| `2026-06-27 22:21:34` | `cowrie.login.success` |
| `2026-06-27 22:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed44211e01bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:21 |
| **Last Seen** | 2026-06-27 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:21:40` | `cowrie.session.connect` |
| `2026-06-27 22:21:40` | `cowrie.client.version` |
| `2026-06-27 22:21:40` | `cowrie.client.kex` |
| `2026-06-27 22:21:41` | `cowrie.login.success` |
| `2026-06-27 22:21:41` | `cowrie.session.params` |
| `2026-06-27 22:21:41` | `cowrie.command.input` |
| `2026-06-27 22:21:41` | `cowrie.log.closed` |
| `2026-06-27 22:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eab6f0a6e45d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 22:21 |
| **Last Seen** | 2026-06-27 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:21:43` | `cowrie.session.connect` |
| `2026-06-27 22:21:43` | `cowrie.client.version` |
| `2026-06-27 22:21:43` | `cowrie.client.kex` |
| `2026-06-27 22:21:43` | `cowrie.login.success` |
| `2026-06-27 22:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f330ff47c8a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:22 |
| **Last Seen** | 2026-06-27 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:22:30` | `cowrie.session.connect` |
| `2026-06-27 22:22:30` | `cowrie.client.version` |
| `2026-06-27 22:22:30` | `cowrie.client.kex` |
| `2026-06-27 22:22:31` | `cowrie.login.success` |
| `2026-06-27 22:22:31` | `cowrie.session.params` |
| `2026-06-27 22:22:31` | `cowrie.command.input` |
| `2026-06-27 22:22:31` | `cowrie.log.closed` |
| `2026-06-27 22:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b286e829da0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:23 |
| **Last Seen** | 2026-06-27 22:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:23:20` | `cowrie.session.connect` |
| `2026-06-27 22:23:20` | `cowrie.client.version` |
| `2026-06-27 22:23:21` | `cowrie.client.kex` |
| `2026-06-27 22:23:21` | `cowrie.login.success` |
| `2026-06-27 22:23:22` | `cowrie.session.params` |
| `2026-06-27 22:23:22` | `cowrie.command.input` |
| `2026-06-27 22:23:22` | `cowrie.log.closed` |
| `2026-06-27 22:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2cf753df993

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:24 |
| **Last Seen** | 2026-06-27 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:24:11` | `cowrie.session.connect` |
| `2026-06-27 22:24:11` | `cowrie.client.version` |
| `2026-06-27 22:24:11` | `cowrie.client.kex` |
| `2026-06-27 22:24:11` | `cowrie.login.success` |
| `2026-06-27 22:24:12` | `cowrie.session.params` |
| `2026-06-27 22:24:12` | `cowrie.command.input` |
| `2026-06-27 22:24:12` | `cowrie.log.closed` |
| `2026-06-27 22:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eceb21af0d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:25 |
| **Last Seen** | 2026-06-27 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:25:03` | `cowrie.session.connect` |
| `2026-06-27 22:25:03` | `cowrie.client.version` |
| `2026-06-27 22:25:03` | `cowrie.client.kex` |
| `2026-06-27 22:25:03` | `cowrie.login.success` |
| `2026-06-27 22:25:04` | `cowrie.session.params` |
| `2026-06-27 22:25:04` | `cowrie.command.input` |
| `2026-06-27 22:25:04` | `cowrie.log.closed` |
| `2026-06-27 22:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c211afb2ae

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 22:25 |
| **Last Seen** | 2026-06-27 22:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:25:45` | `cowrie.session.connect` |
| `2026-06-27 22:25:45` | `cowrie.client.version` |
| `2026-06-27 22:25:45` | `cowrie.client.kex` |
| `2026-06-27 22:25:47` | `cowrie.login.success` |
| `2026-06-27 22:25:49` | `cowrie.session.params` |
| `2026-06-27 22:25:49` | `cowrie.command.input` |
| `2026-06-27 22:25:49` | `cowrie.log.closed` |
| `2026-06-27 22:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6bf40724e2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:25 |
| **Last Seen** | 2026-06-27 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:25:55` | `cowrie.session.connect` |
| `2026-06-27 22:25:55` | `cowrie.client.version` |
| `2026-06-27 22:25:55` | `cowrie.client.kex` |
| `2026-06-27 22:25:56` | `cowrie.login.success` |
| `2026-06-27 22:25:56` | `cowrie.session.params` |
| `2026-06-27 22:25:56` | `cowrie.command.input` |
| `2026-06-27 22:25:56` | `cowrie.log.closed` |
| `2026-06-27 22:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e7a1164142

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:26 |
| **Last Seen** | 2026-06-27 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:26:49` | `cowrie.session.connect` |
| `2026-06-27 22:26:49` | `cowrie.client.version` |
| `2026-06-27 22:26:49` | `cowrie.client.kex` |
| `2026-06-27 22:26:49` | `cowrie.login.success` |
| `2026-06-27 22:26:50` | `cowrie.session.params` |
| `2026-06-27 22:26:50` | `cowrie.command.input` |
| `2026-06-27 22:26:50` | `cowrie.log.closed` |
| `2026-06-27 22:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b2e1c8eef8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:27 |
| **Last Seen** | 2026-06-27 22:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:27:41` | `cowrie.session.connect` |
| `2026-06-27 22:27:41` | `cowrie.client.version` |
| `2026-06-27 22:27:41` | `cowrie.client.kex` |
| `2026-06-27 22:27:41` | `cowrie.login.success` |
| `2026-06-27 22:27:42` | `cowrie.session.params` |
| `2026-06-27 22:27:42` | `cowrie.command.input` |
| `2026-06-27 22:27:42` | `cowrie.log.closed` |
| `2026-06-27 22:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d40f8fe91f1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 22:27 |
| **Last Seen** | 2026-06-27 22:28 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:27:58` | `cowrie.session.connect` |
| `2026-06-27 22:28:00` | `cowrie.client.version` |
| `2026-06-27 22:28:00` | `cowrie.client.kex` |
| `2026-06-27 22:28:06` | `cowrie.login.success` |
| `2026-06-27 22:28:09` | `cowrie.session.params` |
| `2026-06-27 22:28:09` | `cowrie.command.input` |
| `2026-06-27 22:28:11` | `cowrie.log.closed` |
| `2026-06-27 22:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a237238343

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:28 |
| **Last Seen** | 2026-06-27 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:28:31` | `cowrie.session.connect` |
| `2026-06-27 22:28:31` | `cowrie.client.version` |
| `2026-06-27 22:28:31` | `cowrie.client.kex` |
| `2026-06-27 22:28:31` | `cowrie.login.success` |
| `2026-06-27 22:28:32` | `cowrie.session.params` |
| `2026-06-27 22:28:32` | `cowrie.command.input` |
| `2026-06-27 22:28:32` | `cowrie.log.closed` |
| `2026-06-27 22:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac4cddf85c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:29 |
| **Last Seen** | 2026-06-27 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:29:21` | `cowrie.session.connect` |
| `2026-06-27 22:29:21` | `cowrie.client.version` |
| `2026-06-27 22:29:21` | `cowrie.client.kex` |
| `2026-06-27 22:29:22` | `cowrie.login.success` |
| `2026-06-27 22:29:22` | `cowrie.session.params` |
| `2026-06-27 22:29:22` | `cowrie.command.input` |
| `2026-06-27 22:29:22` | `cowrie.log.closed` |
| `2026-06-27 22:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af50924555de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:30 |
| **Last Seen** | 2026-06-27 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:30:12` | `cowrie.session.connect` |
| `2026-06-27 22:30:12` | `cowrie.client.version` |
| `2026-06-27 22:30:12` | `cowrie.client.kex` |
| `2026-06-27 22:30:12` | `cowrie.login.success` |
| `2026-06-27 22:30:13` | `cowrie.session.params` |
| `2026-06-27 22:30:13` | `cowrie.command.input` |
| `2026-06-27 22:30:13` | `cowrie.log.closed` |
| `2026-06-27 22:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da19a7756131

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:31 |
| **Last Seen** | 2026-06-27 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:31:02` | `cowrie.session.connect` |
| `2026-06-27 22:31:02` | `cowrie.client.version` |
| `2026-06-27 22:31:03` | `cowrie.client.kex` |
| `2026-06-27 22:31:03` | `cowrie.login.success` |
| `2026-06-27 22:31:04` | `cowrie.session.params` |
| `2026-06-27 22:31:04` | `cowrie.command.input` |
| `2026-06-27 22:31:04` | `cowrie.log.closed` |
| `2026-06-27 22:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d3614afa052

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:31 |
| **Last Seen** | 2026-06-27 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:31:55` | `cowrie.session.connect` |
| `2026-06-27 22:31:55` | `cowrie.client.version` |
| `2026-06-27 22:31:55` | `cowrie.client.kex` |
| `2026-06-27 22:31:55` | `cowrie.login.success` |
| `2026-06-27 22:31:56` | `cowrie.session.params` |
| `2026-06-27 22:31:56` | `cowrie.command.input` |
| `2026-06-27 22:31:56` | `cowrie.log.closed` |
| `2026-06-27 22:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2321b20884

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:32 |
| **Last Seen** | 2026-06-27 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:32:48` | `cowrie.session.connect` |
| `2026-06-27 22:32:48` | `cowrie.client.version` |
| `2026-06-27 22:32:48` | `cowrie.client.kex` |
| `2026-06-27 22:32:48` | `cowrie.login.success` |
| `2026-06-27 22:32:49` | `cowrie.session.params` |
| `2026-06-27 22:32:49` | `cowrie.command.input` |
| `2026-06-27 22:32:49` | `cowrie.log.closed` |
| `2026-06-27 22:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b495543db579

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:33 |
| **Last Seen** | 2026-06-27 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:33:42` | `cowrie.session.connect` |
| `2026-06-27 22:33:42` | `cowrie.client.version` |
| `2026-06-27 22:33:42` | `cowrie.client.kex` |
| `2026-06-27 22:33:43` | `cowrie.login.success` |
| `2026-06-27 22:33:44` | `cowrie.session.params` |
| `2026-06-27 22:33:44` | `cowrie.command.input` |
| `2026-06-27 22:33:44` | `cowrie.log.closed` |
| `2026-06-27 22:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031742578e9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:34 |
| **Last Seen** | 2026-06-27 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:34:39` | `cowrie.session.connect` |
| `2026-06-27 22:34:39` | `cowrie.client.version` |
| `2026-06-27 22:34:40` | `cowrie.client.kex` |
| `2026-06-27 22:34:40` | `cowrie.login.success` |
| `2026-06-27 22:34:41` | `cowrie.session.params` |
| `2026-06-27 22:34:41` | `cowrie.command.input` |
| `2026-06-27 22:34:41` | `cowrie.log.closed` |
| `2026-06-27 22:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7e2e6987bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:35 |
| **Last Seen** | 2026-06-27 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:35:34` | `cowrie.session.connect` |
| `2026-06-27 22:35:34` | `cowrie.client.version` |
| `2026-06-27 22:35:34` | `cowrie.client.kex` |
| `2026-06-27 22:35:34` | `cowrie.login.success` |
| `2026-06-27 22:35:35` | `cowrie.session.params` |
| `2026-06-27 22:35:35` | `cowrie.command.input` |
| `2026-06-27 22:35:35` | `cowrie.log.closed` |
| `2026-06-27 22:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f127c4eb426

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:36 |
| **Last Seen** | 2026-06-27 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:36:27` | `cowrie.session.connect` |
| `2026-06-27 22:36:27` | `cowrie.client.version` |
| `2026-06-27 22:36:27` | `cowrie.client.kex` |
| `2026-06-27 22:36:27` | `cowrie.login.success` |
| `2026-06-27 22:36:28` | `cowrie.session.params` |
| `2026-06-27 22:36:28` | `cowrie.command.input` |
| `2026-06-27 22:36:28` | `cowrie.log.closed` |
| `2026-06-27 22:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee7d86c2eba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:37 |
| **Last Seen** | 2026-06-27 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:37:21` | `cowrie.session.connect` |
| `2026-06-27 22:37:21` | `cowrie.client.version` |
| `2026-06-27 22:37:21` | `cowrie.client.kex` |
| `2026-06-27 22:37:21` | `cowrie.login.success` |
| `2026-06-27 22:37:22` | `cowrie.session.params` |
| `2026-06-27 22:37:22` | `cowrie.command.input` |
| `2026-06-27 22:37:22` | `cowrie.log.closed` |
| `2026-06-27 22:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4291e7d13b64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:38 |
| **Last Seen** | 2026-06-27 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:38:15` | `cowrie.session.connect` |
| `2026-06-27 22:38:15` | `cowrie.client.version` |
| `2026-06-27 22:38:15` | `cowrie.client.kex` |
| `2026-06-27 22:38:15` | `cowrie.login.success` |
| `2026-06-27 22:38:16` | `cowrie.session.params` |
| `2026-06-27 22:38:16` | `cowrie.command.input` |
| `2026-06-27 22:38:16` | `cowrie.log.closed` |
| `2026-06-27 22:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ae64e9556b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:39 |
| **Last Seen** | 2026-06-27 22:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:39:12` | `cowrie.session.connect` |
| `2026-06-27 22:39:12` | `cowrie.client.version` |
| `2026-06-27 22:39:12` | `cowrie.client.kex` |
| `2026-06-27 22:39:13` | `cowrie.login.success` |
| `2026-06-27 22:39:13` | `cowrie.session.params` |
| `2026-06-27 22:39:13` | `cowrie.command.input` |
| `2026-06-27 22:39:20` | `cowrie.log.closed` |
| `2026-06-27 22:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69815bf8c3d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 22:39 |
| **Last Seen** | 2026-06-27 22:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:39:39` | `cowrie.session.connect` |
| `2026-06-27 22:39:40` | `cowrie.client.version` |
| `2026-06-27 22:39:40` | `cowrie.client.kex` |
| `2026-06-27 22:39:46` | `cowrie.login.success` |
| `2026-06-27 22:39:49` | `cowrie.session.params` |
| `2026-06-27 22:39:49` | `cowrie.command.input` |
| `2026-06-27 22:39:51` | `cowrie.log.closed` |
| `2026-06-27 22:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce663ebab781

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:40 |
| **Last Seen** | 2026-06-27 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:40:05` | `cowrie.session.connect` |
| `2026-06-27 22:40:05` | `cowrie.client.version` |
| `2026-06-27 22:40:05` | `cowrie.client.kex` |
| `2026-06-27 22:40:06` | `cowrie.login.success` |
| `2026-06-27 22:40:06` | `cowrie.session.params` |
| `2026-06-27 22:40:06` | `cowrie.command.input` |
| `2026-06-27 22:40:07` | `cowrie.log.closed` |
| `2026-06-27 22:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1bc631c948a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 22:40 |
| **Last Seen** | 2026-06-27 22:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:40:17` | `cowrie.session.connect` |
| `2026-06-27 22:40:17` | `cowrie.client.version` |
| `2026-06-27 22:40:17` | `cowrie.client.kex` |
| `2026-06-27 22:40:19` | `cowrie.login.success` |
| `2026-06-27 22:40:20` | `cowrie.session.params` |
| `2026-06-27 22:40:20` | `cowrie.command.input` |
| `2026-06-27 22:40:21` | `cowrie.log.closed` |
| `2026-06-27 22:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e373a7c1118c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:41 |
| **Last Seen** | 2026-06-27 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:41:01` | `cowrie.session.connect` |
| `2026-06-27 22:41:01` | `cowrie.client.version` |
| `2026-06-27 22:41:01` | `cowrie.client.kex` |
| `2026-06-27 22:41:01` | `cowrie.login.success` |
| `2026-06-27 22:41:02` | `cowrie.session.params` |
| `2026-06-27 22:41:02` | `cowrie.command.input` |
| `2026-06-27 22:41:02` | `cowrie.log.closed` |
| `2026-06-27 22:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791ec3d966e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:41 |
| **Last Seen** | 2026-06-27 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:41:55` | `cowrie.session.connect` |
| `2026-06-27 22:41:55` | `cowrie.client.version` |
| `2026-06-27 22:41:55` | `cowrie.client.kex` |
| `2026-06-27 22:41:55` | `cowrie.login.success` |
| `2026-06-27 22:41:56` | `cowrie.session.params` |
| `2026-06-27 22:41:56` | `cowrie.command.input` |
| `2026-06-27 22:41:56` | `cowrie.log.closed` |
| `2026-06-27 22:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7665b556e8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:42 |
| **Last Seen** | 2026-06-27 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:42:48` | `cowrie.session.connect` |
| `2026-06-27 22:42:48` | `cowrie.client.version` |
| `2026-06-27 22:42:48` | `cowrie.client.kex` |
| `2026-06-27 22:42:48` | `cowrie.login.success` |
| `2026-06-27 22:42:49` | `cowrie.session.params` |
| `2026-06-27 22:42:49` | `cowrie.command.input` |
| `2026-06-27 22:42:49` | `cowrie.log.closed` |
| `2026-06-27 22:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0382fd45543

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:43 |
| **Last Seen** | 2026-06-27 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:43:41` | `cowrie.session.connect` |
| `2026-06-27 22:43:41` | `cowrie.client.version` |
| `2026-06-27 22:43:41` | `cowrie.client.kex` |
| `2026-06-27 22:43:41` | `cowrie.login.success` |
| `2026-06-27 22:43:42` | `cowrie.session.params` |
| `2026-06-27 22:43:42` | `cowrie.command.input` |
| `2026-06-27 22:43:42` | `cowrie.log.closed` |
| `2026-06-27 22:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f389940ffb5b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:44 |
| **Last Seen** | 2026-06-27 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:44:38` | `cowrie.session.connect` |
| `2026-06-27 22:44:38` | `cowrie.client.version` |
| `2026-06-27 22:44:38` | `cowrie.client.kex` |
| `2026-06-27 22:44:38` | `cowrie.login.success` |
| `2026-06-27 22:44:39` | `cowrie.session.params` |
| `2026-06-27 22:44:39` | `cowrie.command.input` |
| `2026-06-27 22:44:39` | `cowrie.log.closed` |
| `2026-06-27 22:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c788a7d44ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:45 |
| **Last Seen** | 2026-06-27 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:45:34` | `cowrie.session.connect` |
| `2026-06-27 22:45:34` | `cowrie.client.version` |
| `2026-06-27 22:45:34` | `cowrie.client.kex` |
| `2026-06-27 22:45:34` | `cowrie.login.success` |
| `2026-06-27 22:45:35` | `cowrie.session.params` |
| `2026-06-27 22:45:35` | `cowrie.command.input` |
| `2026-06-27 22:45:35` | `cowrie.log.closed` |
| `2026-06-27 22:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-575097318c01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:46 |
| **Last Seen** | 2026-06-27 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:46:28` | `cowrie.session.connect` |
| `2026-06-27 22:46:28` | `cowrie.client.version` |
| `2026-06-27 22:46:28` | `cowrie.client.kex` |
| `2026-06-27 22:46:29` | `cowrie.login.success` |
| `2026-06-27 22:46:29` | `cowrie.session.params` |
| `2026-06-27 22:46:29` | `cowrie.command.input` |
| `2026-06-27 22:46:30` | `cowrie.log.closed` |
| `2026-06-27 22:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf5b8e1362b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:47 |
| **Last Seen** | 2026-06-27 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:47:23` | `cowrie.session.connect` |
| `2026-06-27 22:47:23` | `cowrie.client.version` |
| `2026-06-27 22:47:23` | `cowrie.client.kex` |
| `2026-06-27 22:47:23` | `cowrie.login.success` |
| `2026-06-27 22:47:24` | `cowrie.session.params` |
| `2026-06-27 22:47:24` | `cowrie.command.input` |
| `2026-06-27 22:47:24` | `cowrie.log.closed` |
| `2026-06-27 22:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0882f5337c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:48 |
| **Last Seen** | 2026-06-27 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:48:16` | `cowrie.session.connect` |
| `2026-06-27 22:48:16` | `cowrie.client.version` |
| `2026-06-27 22:48:16` | `cowrie.client.kex` |
| `2026-06-27 22:48:17` | `cowrie.login.success` |
| `2026-06-27 22:48:18` | `cowrie.session.params` |
| `2026-06-27 22:48:18` | `cowrie.command.input` |
| `2026-06-27 22:48:18` | `cowrie.log.closed` |
| `2026-06-27 22:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1747a034cb64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:49 |
| **Last Seen** | 2026-06-27 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:49:09` | `cowrie.session.connect` |
| `2026-06-27 22:49:09` | `cowrie.client.version` |
| `2026-06-27 22:49:09` | `cowrie.client.kex` |
| `2026-06-27 22:49:09` | `cowrie.login.success` |
| `2026-06-27 22:49:10` | `cowrie.session.params` |
| `2026-06-27 22:49:10` | `cowrie.command.input` |
| `2026-06-27 22:49:10` | `cowrie.log.closed` |
| `2026-06-27 22:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169a513d9bd1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:50 |
| **Last Seen** | 2026-06-27 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:50:03` | `cowrie.session.connect` |
| `2026-06-27 22:50:03` | `cowrie.client.version` |
| `2026-06-27 22:50:03` | `cowrie.client.kex` |
| `2026-06-27 22:50:03` | `cowrie.login.success` |
| `2026-06-27 22:50:04` | `cowrie.session.params` |
| `2026-06-27 22:50:04` | `cowrie.command.input` |
| `2026-06-27 22:50:04` | `cowrie.log.closed` |
| `2026-06-27 22:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed3546550ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:50 |
| **Last Seen** | 2026-06-27 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:50:58` | `cowrie.session.connect` |
| `2026-06-27 22:50:58` | `cowrie.client.version` |
| `2026-06-27 22:50:58` | `cowrie.client.kex` |
| `2026-06-27 22:50:59` | `cowrie.login.success` |
| `2026-06-27 22:51:00` | `cowrie.session.params` |
| `2026-06-27 22:51:00` | `cowrie.command.input` |
| `2026-06-27 22:51:00` | `cowrie.log.closed` |
| `2026-06-27 22:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981d0d1aadb4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 22:51 |
| **Last Seen** | 2026-06-27 22:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:51:03` | `cowrie.session.connect` |
| `2026-06-27 22:51:05` | `cowrie.client.version` |
| `2026-06-27 22:51:05` | `cowrie.client.kex` |
| `2026-06-27 22:51:10` | `cowrie.login.success` |
| `2026-06-27 22:51:14` | `cowrie.session.params` |
| `2026-06-27 22:51:14` | `cowrie.command.input` |
| `2026-06-27 22:51:16` | `cowrie.log.closed` |
| `2026-06-27 22:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7a8b9a7257

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:51 |
| **Last Seen** | 2026-06-27 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:51:54` | `cowrie.session.connect` |
| `2026-06-27 22:51:54` | `cowrie.client.version` |
| `2026-06-27 22:51:54` | `cowrie.client.kex` |
| `2026-06-27 22:51:54` | `cowrie.login.success` |
| `2026-06-27 22:51:55` | `cowrie.session.params` |
| `2026-06-27 22:51:55` | `cowrie.command.input` |
| `2026-06-27 22:51:55` | `cowrie.log.closed` |
| `2026-06-27 22:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aebd14d2953d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:52 |
| **Last Seen** | 2026-06-27 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:52:50` | `cowrie.session.connect` |
| `2026-06-27 22:52:50` | `cowrie.client.version` |
| `2026-06-27 22:52:50` | `cowrie.client.kex` |
| `2026-06-27 22:52:50` | `cowrie.login.success` |
| `2026-06-27 22:52:51` | `cowrie.session.params` |
| `2026-06-27 22:52:51` | `cowrie.command.input` |
| `2026-06-27 22:52:51` | `cowrie.log.closed` |
| `2026-06-27 22:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665da6e6ce4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:53 |
| **Last Seen** | 2026-06-27 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:53:45` | `cowrie.session.connect` |
| `2026-06-27 22:53:45` | `cowrie.client.version` |
| `2026-06-27 22:53:45` | `cowrie.client.kex` |
| `2026-06-27 22:53:45` | `cowrie.login.success` |
| `2026-06-27 22:53:46` | `cowrie.session.params` |
| `2026-06-27 22:53:46` | `cowrie.command.input` |
| `2026-06-27 22:53:46` | `cowrie.log.closed` |
| `2026-06-27 22:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9919fe0dfd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 22:54 |
| **Last Seen** | 2026-06-27 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:54:40` | `cowrie.session.connect` |
| `2026-06-27 22:54:40` | `cowrie.client.version` |
| `2026-06-27 22:54:40` | `cowrie.client.kex` |
| `2026-06-27 22:54:40` | `cowrie.login.success` |
| `2026-06-27 22:54:41` | `cowrie.session.params` |
| `2026-06-27 22:54:41` | `cowrie.command.input` |
| `2026-06-27 22:54:41` | `cowrie.log.closed` |
| `2026-06-27 22:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f954296e9b7b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 22:54 |
| **Last Seen** | 2026-06-27 22:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 22:54:54` | `cowrie.session.connect` |
| `2026-06-27 22:54:54` | `cowrie.client.version` |
| `2026-06-27 22:54:54` | `cowrie.client.kex` |
| `2026-06-27 22:54:56` | `cowrie.login.success` |
| `2026-06-27 22:54:58` | `cowrie.session.params` |
| `2026-06-27 22:54:58` | `cowrie.command.input` |
| `2026-06-27 22:54:58` | `cowrie.log.closed` |
| `2026-06-27 22:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `209.99.185[.]59` | **128** | 2026-06-27 20:55 | 2026-06-27 22:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `157.230.42[.]17` | **92** | 2026-06-27 20:55 | 2026-06-27 22:52 | 62m | 0 | `T1592` | 🟠 MEDIUM |
| `212.8.242[.]38` | **3** | 2026-06-27 22:25 | 2026-06-27 22:44 | 1m | 0 | `T1592` | 🟢 LOW |
| `132.148.29[.]10` | **2** | 2026-06-27 20:59 | 2026-06-27 21:03 | 1m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-27 22:00 | 2026-06-27 22:29 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]162` | **2** | 2026-06-27 21:08 | 2026-06-27 21:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-06-27 22:25 | 2026-06-27 22:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.115.99[.]68` | 1 | 2026-06-27 22:28 | 2026-06-27 22:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-06-27 22:08 | 2026-06-27 22:08 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `157.230.42[.]17` | SG | DigitalOcean, LLC | **100** ⚠️ | 11 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `20.115.99[.]68` | US | Microsoft Corporation | **100** ⚠️ | 36 |
| `45.227.254[.]170` | LT | XWIN UNIVERSAL LTD | **100** ⚠️ | 50 |
| `195.96.139[.]162` | GB | Driftnet Ltd | **100** ⚠️ | 4 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 15 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 161 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 153 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 392 cases |
| Tool 34  | Credential Extractor        | ✅ 154 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 41 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 153 priority case(s) shown individually · 9 recon entry/entries in table (6 group(s) consolidating 229 session(s)).

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
_Report time: 2026-06-27T23:07:10Z_

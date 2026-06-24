# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-24 |
| **Generated At** | 2026-06-24T17:59:26Z |
| **Shift Time** | 17:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **651** |
| Confirmed Threats | **636** |
| False Positives Filtered | **15** (2.3%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **13** |
| High Severity Cases | **320** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **331** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **326** |
| Unique Credential Pairs | **298** |
| Unique Usernames | **154** |
| Unique Passwords | **266** |
| Successful Auth Pairs | **312** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 126 |
| `ubuntu` | 15 |
| `admin` | 11 |
| `hadoop` | 5 |
| `user` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 14 |
| `LeitboGi0ro` | 9 |
| `admin` | 8 |
| `123@@@` | 6 |
| `smo@@kkklss` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 9 |
| `admin` | `admin` | 7 |
| `root` | `123@@@` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `admin` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `B884033f9748a5b3b39C` | `209.99.185.59` | 2026-06-24T12:55:17 |
| `dydrkfl0608` | `dydrkfl0608` | `209.99.185.59` | 2026-06-24T12:56:07 |
| `tianyi` | `tianyi` | `209.99.185.59` | 2026-06-24T12:56:59 |
| `master` | `master` | `209.99.185.59` | 2026-06-24T12:57:51 |
| `ul` | `ul1234` | `209.99.185.59` | 2026-06-24T12:58:44 |
| `datacenter` | `123qwe` | `209.99.185.59` | 2026-06-24T12:59:38 |
| `Data` | `korea2012` | `209.99.185.59` | 2026-06-24T13:00:31 |
| `xzxhaha` | `xzxhaha` | `209.99.185.59` | 2026-06-24T13:01:23 |
| `atlbitbucket` | `atlbitbucket` | `209.99.185.59` | 2026-06-24T13:02:15 |
| `git` | `12345678` | `209.99.185.59` | 2026-06-24T13:03:08 |
| `root` | `quS7bw8a` | `45.205.1.42` | 2026-06-24T13:03:41 |
| `ubuntu` | `debian1234567` | `209.99.185.59` | 2026-06-24T13:04:01 |
| `root` | `123qwezxc` | `209.99.185.59` | 2026-06-24T13:04:56 |
| `root` | `P@sswd12` | `209.99.185.59` | 2026-06-24T13:05:51 |
| `timesten` | `timesten` | `209.99.185.59` | 2026-06-24T13:06:45 |
| `root` | `salisbury` | `209.99.185.59` | 2026-06-24T13:07:38 |
| `root` | `q1w2e3r4t5y` | `209.99.185.59` | 2026-06-24T13:08:31 |
| `ubuntu` | `123qwe` | `209.99.185.59` | 2026-06-24T13:09:24 |
| `root` | `dbwhdgml9090` | `209.99.185.59` | 2026-06-24T13:10:17 |
| `yudongyong` | `yudongyong` | `209.99.185.59` | 2026-06-24T13:11:12 |
| `root` | `RD6NJLFkExgi` | `209.99.185.59` | 2026-06-24T13:12:08 |
| `sup` | `sup` | `209.99.185.59` | 2026-06-24T13:13:03 |
| `dell` | `admin@6666` | `209.99.185.59` | 2026-06-24T13:13:57 |
| `iexcel_wuhan` | `iexcel_wuhan1` | `209.99.185.59` | 2026-06-24T13:14:51 |
| `root` | `123mobile` | `209.99.185.59` | 2026-06-24T13:15:45 |
| `cm` | `123456` | `209.99.185.59` | 2026-06-24T13:16:41 |
| `zhangning` | `zhangning` | `209.99.185.59` | 2026-06-24T13:17:37 |
| `ubuntu` | `18atcskd2w` | `45.205.1.42` | 2026-06-24T13:17:54 |
| `testing` | `babygirl1` | `209.99.185.59` | 2026-06-24T13:18:35 |
| `root` | `demo12345678` | `209.99.185.59` | 2026-06-24T13:19:32 |
| `root` | `primo` | `209.99.185.59` | 2026-06-24T13:20:28 |
| `www-data` | `p@ssw0rd` | `209.99.185.59` | 2026-06-24T13:21:24 |
| `root` | `Zhidan@123` | `209.99.185.59` | 2026-06-24T13:22:19 |
| `root` | `11111` | `209.99.185.59` | 2026-06-24T13:23:16 |
| `ubuntu` | `redhat` | `209.99.185.59` | 2026-06-24T13:24:13 |
| `root` | `12345.com` | `209.99.185.59` | 2026-06-24T13:25:10 |
| `fengfan` | `fengfan` | `209.99.185.59` | 2026-06-24T13:26:07 |
| `manish` | `manish123` | `209.99.185.59` | 2026-06-24T13:27:04 |
| `liuchangle` | `Tab.l@639` | `209.99.185.59` | 2026-06-24T13:28:00 |
| `cyrus` | `0` | `209.99.185.59` | 2026-06-24T13:28:56 |
| `root` | `maintenance` | `209.99.185.59` | 2026-06-24T13:29:53 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-24T13:30:02 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-24T13:30:03 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-24T13:30:08 |
| `hadoop` | `1` | `209.99.185.59` | 2026-06-24T13:30:51 |
| `root` | `root123456` | `209.99.185.59` | 2026-06-24T13:31:50 |
| `root` | `loveme` | `45.205.1.42` | 2026-06-24T13:32:13 |
| `root` | `jasmine` | `209.99.185.59` | 2026-06-24T13:32:50 |
| `zxy` | `123456` | `209.99.185.59` | 2026-06-24T13:33:46 |
| `dbuser` | `dbuser@123` | `209.99.185.59` | 2026-06-24T13:34:43 |
| `db2inst1` | `111111` | `209.99.185.59` | 2026-06-24T13:35:40 |
| `root` | `1qazwsx2` | `209.99.185.59` | 2026-06-24T13:36:38 |
| `root` | `1a2s3d4f5g6h7j8k` | `209.99.185.59` | 2026-06-24T13:37:37 |
| `hadoop` | `q1w2e3r4` | `209.99.185.59` | 2026-06-24T13:38:35 |
| `usuario` | `222222` | `209.99.185.59` | 2026-06-24T13:39:33 |
| `root` | `jimjim30` | `209.99.185.59` | 2026-06-24T13:40:32 |
| `root` | `Qwerty@1232wsx` | `209.99.185.59` | 2026-06-24T13:41:31 |
| `root` | `Admin@777` | `209.99.185.59` | 2026-06-24T13:42:30 |
| `root` | `v` | `209.99.185.59` | 2026-06-24T13:43:29 |
| `root` | `1qa2ws#ED` | `209.99.185.59` | 2026-06-24T13:44:32 |
| `iexcel001` | `222222` | `209.99.185.59` | 2026-06-24T13:45:30 |
| `root` | `P@ssword1!` | `45.205.1.42` | 2026-06-24T13:46:13 |
| `root` | `upload0` | `209.99.185.59` | 2026-06-24T13:46:28 |
| `lyj` | `lyj123` | `209.99.185.59` | 2026-06-24T13:47:26 |
| `root` | `Pass123123!@#` | `209.99.185.59` | 2026-06-24T13:48:27 |
| `hsj` | `korea2014` | `209.99.185.59` | 2026-06-24T13:49:28 |
| `hongchen` | `20171224` | `209.99.185.59` | 2026-06-24T13:50:31 |
| `root` | `anta` | `209.99.185.59` | 2026-06-24T13:51:32 |
| `root` | `Pa$$s0rd12` | `209.99.185.59` | 2026-06-24T13:52:32 |
| `operator` | `0` | `209.99.185.59` | 2026-06-24T13:53:28 |
| `root` | `admin123#` | `209.99.185.59` | 2026-06-24T13:54:27 |
| `hadoop` | `haddop123` | `209.99.185.59` | 2026-06-24T13:55:25 |
| `root` | `jobandtalent` | `209.99.185.59` | 2026-06-24T13:56:25 |
| `root` | `********` | `209.99.185.59` | 2026-06-24T13:57:29 |
| `caja01` | `caja01` | `209.99.185.59` | 2026-06-24T13:58:30 |
| `book` | `123456` | `209.99.185.59` | 2026-06-24T13:59:29 |
| `root` | `a123456` | `45.205.1.42` | 2026-06-24T14:00:20 |
| `xian1` | `xian1` | `209.99.185.59` | 2026-06-24T14:00:26 |
| `mjdeff` | `7890uiop` | `209.99.185.59` | 2026-06-24T14:01:14 |
| `root` | `qiugaoqs123` | `209.99.185.59` | 2026-06-24T14:02:01 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-24T14:02:17 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-24T14:02:18 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-24T14:02:19 |
| `ubuntu` | `qazwsxedc` | `209.99.185.59` | 2026-06-24T14:02:49 |
| `root` | `codyy@1215` | `209.99.185.59` | 2026-06-24T14:03:38 |
| `test` | `tset` | `209.99.185.59` | 2026-06-24T14:04:27 |
| `buero3` | `333333` | `209.99.185.59` | 2026-06-24T14:05:15 |
| `user` | `qwerty123` | `209.99.185.59` | 2026-06-24T14:06:02 |
| `oracle` | `101010` | `209.99.185.59` | 2026-06-24T14:06:48 |
| `test` | `1234` | `209.99.185.59` | 2026-06-24T14:07:36 |
| `root` | `korea2019` | `209.99.185.59` | 2026-06-24T14:08:27 |
| `traffic` | `traffic` | `209.99.185.59` | 2026-06-24T14:09:19 |
| `root` | `Flores123` | `209.99.185.59` | 2026-06-24T14:10:13 |
| `root` | `abc123!` | `209.99.185.59` | 2026-06-24T14:11:02 |
| `root` | `Ceckspamroot87?` | `209.99.185.59` | 2026-06-24T14:11:48 |
| `hmkim` | `7890uiop` | `209.99.185.59` | 2026-06-24T14:12:35 |
| `zou` | `zou` | `209.99.185.59` | 2026-06-24T14:13:23 |
| `root` | `---fuck_you----` | `171.111.218.2` | 2026-06-24T14:13:50 |
| `root` | `0p9o8i7u6y5t4r` | `209.99.185.59` | 2026-06-24T14:14:10 |
| `root` | `0123` | `45.205.1.42` | 2026-06-24T14:14:42 |
| `yxt` | `1` | `209.99.185.59` | 2026-06-24T14:14:59 |
| `root` | `www.sina.com.cn` | `209.99.185.59` | 2026-06-24T14:15:53 |
| `root` | `1234abcd!@#$` | `209.99.185.59` | 2026-06-24T14:16:41 |
| `professor` | `professor` | `209.99.185.59` | 2026-06-24T14:17:28 |
| `root` | `Pa55w0rD!` | `209.99.185.59` | 2026-06-24T14:18:15 |
| `xuzhenjing` | `xuzhenjing` | `209.99.185.59` | 2026-06-24T14:19:01 |
| `root` | `qaz!@#321` | `209.99.185.59` | 2026-06-24T14:19:50 |
| `postgres` | `admin1234` | `209.99.185.59` | 2026-06-24T14:20:39 |
| `chenzheng` | `chenzheng` | `209.99.185.59` | 2026-06-24T14:21:29 |
| `rizhiyi` | `rizhiyi&2014` | `209.99.185.59` | 2026-06-24T14:22:19 |
| `oryun4912` | `1` | `209.99.185.59` | 2026-06-24T14:23:10 |
| `deploy` | `deploy123` | `209.99.185.59` | 2026-06-24T14:24:00 |
| `ubuntu` | `123321` | `209.99.185.59` | 2026-06-24T14:24:49 |
| `sunzheng` | `dul_sbl2021` | `209.99.185.59` | 2026-06-24T14:25:40 |
| `root` | `Passwd@1234` | `209.99.185.59` | 2026-06-24T14:26:29 |
| `ocean` | `ocean` | `209.99.185.59` | 2026-06-24T14:27:18 |
| `node` | `changeme123` | `209.99.185.59` | 2026-06-24T14:28:08 |
| `ubuntu` | `1qazcde3` | `45.205.1.42` | 2026-06-24T14:28:48 |
| `root` | `Mypassw0rdischengu.com` | `209.99.185.59` | 2026-06-24T14:28:58 |
| `root` | `linux1` | `209.99.185.59` | 2026-06-24T14:29:48 |
| `user` | `rl_3367ye` | `209.99.185.59` | 2026-06-24T14:30:37 |
| `yuanenming` | `123456` | `209.99.185.59` | 2026-06-24T14:31:29 |
| `yt` | `yt@asc` | `209.99.185.59` | 2026-06-24T14:32:18 |
| `tcc` | `tcc123.com` | `209.99.185.59` | 2026-06-24T14:33:09 |
| `liy` | `liy123` | `209.99.185.59` | 2026-06-24T14:34:02 |
| `cajr` | `cajr` | `209.99.185.59` | 2026-06-24T14:34:55 |
| `zc` | `zc` | `209.99.185.59` | 2026-06-24T14:35:46 |
| `root` | `webalizer` | `209.99.185.59` | 2026-06-24T14:36:38 |
| `oracle` | `oracle!@#` | `209.99.185.59` | 2026-06-24T14:37:28 |
| `root` | `2222` | `209.99.185.59` | 2026-06-24T14:38:19 |
| `ftp` | `1234` | `209.99.185.59` | 2026-06-24T14:39:11 |
| `root` | `﻿------fuck------` | `106.12.127.43` | 2026-06-24T14:39:48 |
| `geou02` | `geou02` | `209.99.185.59` | 2026-06-24T14:40:02 |
| `zhuang` | `zhuang1997` | `209.99.185.59` | 2026-06-24T14:40:54 |
| `xmetasr` | `xmetar` | `209.99.185.59` | 2026-06-24T14:41:47 |
| `iptv2` | `123456` | `209.99.185.59` | 2026-06-24T14:42:37 |
| `file` | `file` | `45.205.1.42` | 2026-06-24T14:43:01 |
| `root` | `1qaz2wsx1qaz` | `209.99.185.59` | 2026-06-24T14:43:27 |
| `root` | `tribal` | `209.99.185.59` | 2026-06-24T14:44:16 |
| `zk` | `keyanzhongkai` | `209.99.185.59` | 2026-06-24T14:45:07 |
| `wps` | `wps` | `209.99.185.59` | 2026-06-24T14:45:59 |
| `iskw1114` | `031320lxc` | `209.99.185.59` | 2026-06-24T14:46:51 |
| `root` | `beautiful` | `209.99.185.59` | 2026-06-24T14:47:44 |
| `user` | `sitonholy` | `209.99.185.59` | 2026-06-24T14:48:38 |
| `yangliusha3` | `yangliusha3` | `209.99.185.59` | 2026-06-24T14:49:29 |
| `airchem` | `korea2015` | `209.99.185.59` | 2026-06-24T14:50:22 |
| `root` | `@Bismillah123` | `209.99.185.59` | 2026-06-24T14:51:19 |
| `et21-haojx` | `Hjx123` | `209.99.185.59` | 2026-06-24T14:52:13 |
| `new` | `password` | `209.99.185.59` | 2026-06-24T14:53:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `184.105.139.70` | 2026-06-24T14:53:48 |
| `root` | `root.2020` | `209.99.185.59` | 2026-06-24T14:53:59 |
| `cs` | `123456` | `209.99.185.59` | 2026-06-24T14:54:52 |
| `root` | `compromised` | `209.99.185.59` | 2026-06-24T14:55:48 |
| `root` | `password#123` | `209.99.185.59` | 2026-06-24T14:56:44 |
| `ubuntu` | `1qaz321x` | `45.205.1.42` | 2026-06-24T14:57:14 |
| `wwwdata` | `wwwdata` | `209.99.185.59` | 2026-06-24T14:57:37 |
| `root` | `123456789a` | `209.99.185.59` | 2026-06-24T14:58:31 |
| `root` | `Pa$$w0rd01` | `209.99.185.59` | 2026-06-24T14:59:26 |
| `odoo12` | `admin` | `209.99.185.59` | 2026-06-24T15:00:26 |
| `zl` | `123` | `209.99.185.59` | 2026-06-24T15:01:24 |
| `root` | `password!` | `209.99.185.59` | 2026-06-24T15:02:17 |
| `jaeeun` | `jaeeun` | `209.99.185.59` | 2026-06-24T15:03:09 |
| `postgres` | `123` | `209.99.185.59` | 2026-06-24T15:04:01 |
| `root` | `1a2s3d` | `209.99.185.59` | 2026-06-24T15:04:56 |
| `zhuyz` | `zhuyz` | `209.99.185.59` | 2026-06-24T15:05:54 |
| `root` | `root@444` | `209.99.185.59` | 2026-06-24T15:06:51 |
| `es` | `es@321` | `209.99.185.59` | 2026-06-24T15:07:49 |
| `caoke` | `caoke` | `209.99.185.59` | 2026-06-24T15:08:47 |
| `server` | `password123` | `209.99.185.59` | 2026-06-24T15:09:40 |
| `czfy` | `czfy1028` | `209.99.185.59` | 2026-06-24T15:10:37 |
| `root` | `aaa123` | `45.205.1.42` | 2026-06-24T15:11:34 |
| `steam` | `1234` | `209.99.185.59` | 2026-06-24T15:11:39 |
| `sjb` | `korea2020` | `209.99.185.59` | 2026-06-24T15:12:38 |
| `deploy` | `1q2w3e` | `209.99.185.59` | 2026-06-24T15:13:35 |
| `dell` | `dell@3000` | `209.99.185.59` | 2026-06-24T15:14:31 |
| `root` | `admin2019` | `209.99.185.59` | 2026-06-24T15:15:26 |
| `mysql` | `321` | `209.99.185.59` | 2026-06-24T15:16:25 |
| `oracle` | `1234567` | `209.99.185.59` | 2026-06-24T15:17:19 |
| `root` | `r3dh4at` | `209.99.185.59` | 2026-06-24T15:18:14 |
| `ee17041` | `1234` | `209.99.185.59` | 2026-06-24T15:19:09 |
| `oracle` | `zaq12wsx` | `209.99.185.59` | 2026-06-24T15:20:07 |
| `root` | `seekyou` | `209.99.185.59` | 2026-06-24T15:21:03 |
| `hadoop` | `qwerty123456` | `209.99.185.59` | 2026-06-24T15:21:57 |
| `nelson` | `nelson` | `209.99.185.59` | 2026-06-24T15:22:50 |
| `henrique` | `henrique` | `209.99.185.59` | 2026-06-24T15:23:45 |
| `mysql` | `mysql1123` | `209.99.185.59` | 2026-06-24T15:24:42 |
| `root` | `unknown` | `45.205.1.42` | 2026-06-24T15:25:38 |
| `renjie` | `renjie` | `209.99.185.59` | 2026-06-24T15:25:40 |
| `root` | `esqooel.com` | `209.99.185.59` | 2026-06-24T15:26:37 |
| `root` | `danielle` | `209.99.185.59` | 2026-06-24T15:27:36 |
| `iexcel001` | `333333` | `209.99.185.59` | 2026-06-24T15:28:36 |
| `jxye` | `Yjx19990621` | `209.99.185.59` | 2026-06-24T15:29:33 |
| `root` | `vmw@re` | `209.99.185.59` | 2026-06-24T15:30:30 |
| `a` | `111111` | `209.99.185.59` | 2026-06-24T15:31:27 |
| `ubuntu` | `abc123d4` | `209.99.185.59` | 2026-06-24T15:32:24 |
| `star` | `star` | `209.99.185.59` | 2026-06-24T15:33:20 |
| `james` | `james123` | `209.99.185.59` | 2026-06-24T15:34:15 |
| `john` | `123456` | `209.99.185.59` | 2026-06-24T15:35:13 |
| `yuanwd` | `passpass` | `209.99.185.59` | 2026-06-24T15:36:10 |
| `root` | `p@ssw0rd` | `209.99.185.59` | 2026-06-24T15:37:09 |
| `nas` | `nas` | `209.99.185.59` | 2026-06-24T15:38:11 |
| `shenleqi` | `shenleqi` | `209.99.185.59` | 2026-06-24T15:39:11 |
| `oscar` | `oscar` | `45.205.1.42` | 2026-06-24T15:39:40 |
| `root` | `passwdroot` | `209.99.185.59` | 2026-06-24T15:40:09 |
| `gpuadmin` | `Itmaya2009!` | `209.99.185.59` | 2026-06-24T15:41:06 |
| `sslee` | `sslee` | `209.99.185.59` | 2026-06-24T15:42:02 |
| `anna` | `anna` | `209.99.185.59` | 2026-06-24T15:43:00 |
| `ubnt` | `default` | `209.99.185.59` | 2026-06-24T15:43:58 |
| `nasa123` | `nasa123` | `209.99.185.59` | 2026-06-24T15:44:57 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-24T15:44:57 |
| `root` | `pwd@123` | `209.99.185.59` | 2026-06-24T15:45:55 |
| `root` | `AA@123456` | `209.99.185.59` | 2026-06-24T15:46:52 |
| `root` | `8larry8` | `209.99.185.59` | 2026-06-24T15:47:46 |
| `dc` | `123456` | `209.99.185.59` | 2026-06-24T15:48:42 |
| `root` | `LeitboGi0ro` | `161.118.237.181` | 2026-06-24T15:49:20 |
| `root` | `123@@@` | `161.118.237.181` | 2026-06-24T15:49:20 |
| `root` | `1a2s3d4f5g6` | `209.99.185.59` | 2026-06-24T15:49:39 |
| `vps` | `111111` | `209.99.185.59` | 2026-06-24T15:50:37 |
| `bailey` | `bailey` | `209.99.185.59` | 2026-06-24T15:51:36 |
| `root` | `P455word` | `209.99.185.59` | 2026-06-24T15:52:35 |
| `a1` | `a1` | `45.205.1.42` | 2026-06-24T15:53:31 |
| `ubuntu` | `password209` | `209.99.185.59` | 2026-06-24T15:53:32 |
| `lcy` | `lcy` | `209.99.185.59` | 2026-06-24T15:54:26 |
| `root` | `Aa112233` | `209.99.185.59` | 2026-06-24T15:55:20 |
| `root` | `abc12` | `209.99.185.59` | 2026-06-24T15:56:17 |
| `wx` | `wx` | `209.99.185.59` | 2026-06-24T15:57:13 |
| `admin` | `admin` | `143.20.49.38` | 2026-06-24T15:57:58 |
| `admin` | `admin` | `168.144.45.211` | 2026-06-24T15:58:01 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-24T15:58:02 |
| `git` | `git` | `209.99.185.59` | 2026-06-24T15:58:10 |
| `hadoop` | `hadoop!` | `209.99.185.59` | 2026-06-24T15:59:06 |
| `root` | `unknown` | `209.99.185.59` | 2026-06-24T16:00:05 |
| `root` | `` | `141.11.88.100` | 2026-06-24T16:00:41 |
| `root` | `pa$$w0rd123` | `209.99.185.59` | 2026-06-24T16:00:51 |
| `xzh` | `xzhuai` | `209.99.185.59` | 2026-06-24T16:01:36 |
| `pepper` | `pepper` | `209.99.185.59` | 2026-06-24T16:02:20 |
| `pul` | `q1w2e3r4` | `209.99.185.59` | 2026-06-24T16:03:05 |
| `ceshi2` | `111111` | `209.99.185.59` | 2026-06-24T16:03:50 |
| `ubuntu` | `asd1` | `209.99.185.59` | 2026-06-24T16:04:36 |
| `ubuntu` | `admin!@#` | `209.99.185.59` | 2026-06-24T16:05:24 |
| `djy` | `123456` | `209.99.185.59` | 2026-06-24T16:06:06 |
| `koreagift` | `koreagift` | `209.99.185.59` | 2026-06-24T16:06:51 |
| `root` | `Qwert!@#$%` | `209.99.185.59` | 2026-06-24T16:07:36 |
| `ubuntu` | `test123` | `45.205.1.42` | 2026-06-24T16:07:40 |
| `root` | `Pass@word12345` | `209.99.185.59` | 2026-06-24T16:08:20 |
| `ubuntu` | `password1234` | `209.99.185.59` | 2026-06-24T16:09:04 |
| `bin` | `iohd9fewifi89ew66` | `209.99.185.59` | 2026-06-24T16:09:50 |
| `root` | `2wsxzaq1` | `209.99.185.59` | 2026-06-24T16:10:37 |
| `mytest` | `mytest` | `209.99.185.59` | 2026-06-24T16:11:23 |
| `dell` | `dell@2222` | `209.99.185.59` | 2026-06-24T16:12:10 |
| `deploy` | `321123` | `209.99.185.59` | 2026-06-24T16:12:57 |
| `test` | `test11` | `209.99.185.59` | 2026-06-24T16:13:43 |
| `ubuntu` | `P@ssword1` | `209.99.185.59` | 2026-06-24T16:14:30 |
| `ftpuser` | `qwer1234` | `209.99.185.59` | 2026-06-24T16:15:18 |
| `admin1` | `admin1321` | `209.99.185.59` | 2026-06-24T16:16:07 |
| `a` | `a` | `165.232.61.133` | 2026-06-24T16:16:56 |
| `gaurav` | `gaurav` | `209.99.185.59` | 2026-06-24T16:16:57 |
| `root` | `qwe.123` | `209.99.185.59` | 2026-06-24T16:17:46 |
| `rootroot` | `rootroot` | `209.99.185.59` | 2026-06-24T16:18:34 |
| `root` | `Ubuntu$Root1234!` | `209.99.185.59` | 2026-06-24T16:19:21 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-24T16:20:05 |
| `mediazen` | `1234` | `209.99.185.59` | 2026-06-24T16:20:07 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-24T16:20:07 |
| `tomcat1` | `123456` | `209.99.185.59` | 2026-06-24T16:20:56 |
| `zouzhenhong` | `cluster.208008` | `209.99.185.59` | 2026-06-24T16:21:46 |
| `root` | `P@$w0rd` | `45.205.1.42` | 2026-06-24T16:21:52 |
| `install` | `install` | `209.99.185.59` | 2026-06-24T16:22:35 |
| `zhangxinkui` | `zhangxinkui` | `209.99.185.59` | 2026-06-24T16:23:24 |
| `sujin` | `sujin` | `209.99.185.59` | 2026-06-24T16:24:13 |
| `ruili` | `ruili` | `209.99.185.59` | 2026-06-24T16:25:00 |
| `gabriel` | `gabriel` | `209.99.185.59` | 2026-06-24T16:25:48 |
| `root` | `p0o9` | `209.99.185.59` | 2026-06-24T16:26:35 |
| `lyl` | `123456` | `209.99.185.59` | 2026-06-24T16:27:23 |
| `zouzhenhong` | `linka84521` | `209.99.185.59` | 2026-06-24T16:28:12 |
| `root` | `QWEasd@123` | `209.99.185.59` | 2026-06-24T16:29:01 |
| `root` | `s123456` | `209.99.185.59` | 2026-06-24T16:29:51 |
| `root` | `123@@@` | `163.192.13.135` | 2026-06-24T16:30:19 |
| `root` | `LeitboGi0ro` | `163.192.13.135` | 2026-06-24T16:30:19 |
| `nvidia` | `gputest` | `209.99.185.59` | 2026-06-24T16:30:40 |
| `zhangsan` | `zhangsan1234` | `209.99.185.59` | 2026-06-24T16:31:30 |
| `root` | `0p2wsx#EDC4` | `209.99.185.59` | 2026-06-24T16:32:18 |
| `amandabackup` | `amandabackup123` | `209.99.185.59` | 2026-06-24T16:33:08 |
| `root` | `qwe123@qwe` | `209.99.185.59` | 2026-06-24T16:33:55 |
| `ksy` | `ksy` | `209.99.185.59` | 2026-06-24T16:34:45 |
| `yangquan` | `yangquan` | `209.99.185.59` | 2026-06-24T16:35:34 |
| `root` | `P@ssword@123` | `45.205.1.42` | 2026-06-24T16:36:01 |
| `root` | `omgpop` | `209.99.185.59` | 2026-06-24T16:36:25 |
| `bxw` | `bxw` | `209.99.185.59` | 2026-06-24T16:37:15 |
| `root` | `plm54321` | `209.99.185.59` | 2026-06-24T16:38:05 |
| `papeleria` | `papeleria` | `209.99.185.59` | 2026-06-24T16:38:52 |
| `zhangyubo` | `zhangyubo` | `209.99.185.59` | 2026-06-24T16:39:39 |
| `root` | `Aa@112233` | `209.99.185.59` | 2026-06-24T16:40:27 |
| `admin` | `admin` | `34.62.138.158` | 2026-06-24T16:40:42 |
| `downloader` | `downloader321` | `209.99.185.59` | 2026-06-24T16:41:17 |
| `lml` | `123456` | `209.99.185.59` | 2026-06-24T16:42:08 |
| `info` | `info` | `209.99.185.59` | 2026-06-24T16:42:59 |
| `admin` | `admin` | `47.253.245.52` | 2026-06-24T16:43:29 |
| `jtang` | `123456` | `209.99.185.59` | 2026-06-24T16:43:49 |
| `iexcel001` | `iexcel001123` | `209.99.185.59` | 2026-06-24T16:44:39 |
| `rep_ve2` | `rep_ve2` | `209.99.185.59` | 2026-06-24T16:45:28 |
| `root` | `xsc` | `209.99.185.59` | 2026-06-24T16:46:19 |
| `localadmin` | `123456` | `209.99.185.59` | 2026-06-24T16:47:08 |
| `kelly` | `kelly` | `209.99.185.59` | 2026-06-24T16:47:59 |
| `root` | `qazxcv!@#` | `209.99.185.59` | 2026-06-24T16:48:51 |
| `centos` | `changeme` | `209.99.185.59` | 2026-06-24T16:49:41 |
| `root` | `qweASDqwe123` | `45.205.1.42` | 2026-06-24T16:50:21 |
| `root` | `Cernet@2020` | `209.99.185.59` | 2026-06-24T16:50:33 |
| `root` | `6666` | `209.99.185.59` | 2026-06-24T16:51:23 |
| `zwrao` | `10624170` | `209.99.185.59` | 2026-06-24T16:52:14 |
| `root` | `P@ssw0rd0` | `209.99.185.59` | 2026-06-24T16:53:05 |
| `zxf` | `zxf123456` | `209.99.185.59` | 2026-06-24T16:53:58 |
| `zy` | `zy` | `209.99.185.59` | 2026-06-24T16:54:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **651** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 300 |
| Paramiko (Python) | 21 |
| libssh | 20 |
| Nmap scanner | 7 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 289 | 2 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `6372ee695756...` | Modern SSH client | 7 | 2 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `bc3aee897af7...` | Mirai/variant | 3 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 289 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 18 | 8 | — |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 7 | 2 | Modern SSH client |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `bc3aee897af7...` | Go SSH scanner | 3 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

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
Source IPs: `141.11.88.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **24** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS3320` | Deutsche Telekom AG | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (320)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3b72b1eef08e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 12:55 |
| **Last Seen** | 2026-06-24 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 12:55:16` | `cowrie.session.connect` |
| `2026-06-24 12:55:16` | `cowrie.client.version` |
| `2026-06-24 12:55:16` | `cowrie.client.kex` |
| `2026-06-24 12:55:17` | `cowrie.login.success` |
| `2026-06-24 12:55:17` | `cowrie.session.params` |
| `2026-06-24 12:55:17` | `cowrie.command.input` |
| `2026-06-24 12:55:18` | `cowrie.log.closed` |
| `2026-06-24 12:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9147576799cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 12:56 |
| **Last Seen** | 2026-06-24 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 12:56:07` | `cowrie.session.connect` |
| `2026-06-24 12:56:07` | `cowrie.client.version` |
| `2026-06-24 12:56:07` | `cowrie.client.kex` |
| `2026-06-24 12:56:07` | `cowrie.login.success` |
| `2026-06-24 12:56:08` | `cowrie.session.params` |
| `2026-06-24 12:56:08` | `cowrie.command.input` |
| `2026-06-24 12:56:08` | `cowrie.log.closed` |
| `2026-06-24 12:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd11950a5cf9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 12:56 |
| **Last Seen** | 2026-06-24 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 12:56:58` | `cowrie.session.connect` |
| `2026-06-24 12:56:58` | `cowrie.client.version` |
| `2026-06-24 12:56:58` | `cowrie.client.kex` |
| `2026-06-24 12:56:59` | `cowrie.login.success` |
| `2026-06-24 12:57:00` | `cowrie.session.params` |
| `2026-06-24 12:57:00` | `cowrie.command.input` |
| `2026-06-24 12:57:00` | `cowrie.log.closed` |
| `2026-06-24 12:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9d6c7d962fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 12:57 |
| **Last Seen** | 2026-06-24 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 12:57:50` | `cowrie.session.connect` |
| `2026-06-24 12:57:50` | `cowrie.client.version` |
| `2026-06-24 12:57:50` | `cowrie.client.kex` |
| `2026-06-24 12:57:51` | `cowrie.login.success` |
| `2026-06-24 12:57:51` | `cowrie.session.params` |
| `2026-06-24 12:57:51` | `cowrie.command.input` |
| `2026-06-24 12:57:52` | `cowrie.log.closed` |
| `2026-06-24 12:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2586e76e31b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 12:58 |
| **Last Seen** | 2026-06-24 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 12:58:43` | `cowrie.session.connect` |
| `2026-06-24 12:58:43` | `cowrie.client.version` |
| `2026-06-24 12:58:43` | `cowrie.client.kex` |
| `2026-06-24 12:58:44` | `cowrie.login.success` |
| `2026-06-24 12:58:44` | `cowrie.session.params` |
| `2026-06-24 12:58:44` | `cowrie.command.input` |
| `2026-06-24 12:58:44` | `cowrie.log.closed` |
| `2026-06-24 12:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46aed1c73974

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 12:59 |
| **Last Seen** | 2026-06-24 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 12:59:37` | `cowrie.session.connect` |
| `2026-06-24 12:59:37` | `cowrie.client.version` |
| `2026-06-24 12:59:38` | `cowrie.client.kex` |
| `2026-06-24 12:59:38` | `cowrie.login.success` |
| `2026-06-24 12:59:39` | `cowrie.session.params` |
| `2026-06-24 12:59:39` | `cowrie.command.input` |
| `2026-06-24 12:59:39` | `cowrie.log.closed` |
| `2026-06-24 12:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9c72b634f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:00 |
| **Last Seen** | 2026-06-24 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:00:30` | `cowrie.session.connect` |
| `2026-06-24 13:00:30` | `cowrie.client.version` |
| `2026-06-24 13:00:30` | `cowrie.client.kex` |
| `2026-06-24 13:00:31` | `cowrie.login.success` |
| `2026-06-24 13:00:32` | `cowrie.session.params` |
| `2026-06-24 13:00:32` | `cowrie.command.input` |
| `2026-06-24 13:00:32` | `cowrie.log.closed` |
| `2026-06-24 13:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f475b34a8315

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:01 |
| **Last Seen** | 2026-06-24 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:01:23` | `cowrie.session.connect` |
| `2026-06-24 13:01:23` | `cowrie.client.version` |
| `2026-06-24 13:01:23` | `cowrie.client.kex` |
| `2026-06-24 13:01:23` | `cowrie.login.success` |
| `2026-06-24 13:01:24` | `cowrie.session.params` |
| `2026-06-24 13:01:24` | `cowrie.command.input` |
| `2026-06-24 13:01:24` | `cowrie.log.closed` |
| `2026-06-24 13:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fbb239307c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:02 |
| **Last Seen** | 2026-06-24 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:02:15` | `cowrie.session.connect` |
| `2026-06-24 13:02:15` | `cowrie.client.version` |
| `2026-06-24 13:02:15` | `cowrie.client.kex` |
| `2026-06-24 13:02:15` | `cowrie.login.success` |
| `2026-06-24 13:02:16` | `cowrie.session.params` |
| `2026-06-24 13:02:16` | `cowrie.command.input` |
| `2026-06-24 13:02:16` | `cowrie.log.closed` |
| `2026-06-24 13:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07766fe79117

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:03 |
| **Last Seen** | 2026-06-24 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:03:07` | `cowrie.session.connect` |
| `2026-06-24 13:03:07` | `cowrie.client.version` |
| `2026-06-24 13:03:07` | `cowrie.client.kex` |
| `2026-06-24 13:03:08` | `cowrie.login.success` |
| `2026-06-24 13:03:09` | `cowrie.session.params` |
| `2026-06-24 13:03:09` | `cowrie.command.input` |
| `2026-06-24 13:03:09` | `cowrie.log.closed` |
| `2026-06-24 13:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7d00cf26e4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 13:03 |
| **Last Seen** | 2026-06-24 13:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:03:33` | `cowrie.session.connect` |
| `2026-06-24 13:03:35` | `cowrie.client.version` |
| `2026-06-24 13:03:35` | `cowrie.client.kex` |
| `2026-06-24 13:03:41` | `cowrie.login.success` |
| `2026-06-24 13:03:45` | `cowrie.session.params` |
| `2026-06-24 13:03:45` | `cowrie.command.input` |
| `2026-06-24 13:03:46` | `cowrie.log.closed` |
| `2026-06-24 13:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e1571348862

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:04 |
| **Last Seen** | 2026-06-24 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:04:01` | `cowrie.session.connect` |
| `2026-06-24 13:04:01` | `cowrie.client.version` |
| `2026-06-24 13:04:01` | `cowrie.client.kex` |
| `2026-06-24 13:04:01` | `cowrie.login.success` |
| `2026-06-24 13:04:02` | `cowrie.session.params` |
| `2026-06-24 13:04:02` | `cowrie.command.input` |
| `2026-06-24 13:04:02` | `cowrie.log.closed` |
| `2026-06-24 13:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d927695cab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:04 |
| **Last Seen** | 2026-06-24 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:04:55` | `cowrie.session.connect` |
| `2026-06-24 13:04:55` | `cowrie.client.version` |
| `2026-06-24 13:04:56` | `cowrie.client.kex` |
| `2026-06-24 13:04:56` | `cowrie.login.success` |
| `2026-06-24 13:04:57` | `cowrie.session.params` |
| `2026-06-24 13:04:57` | `cowrie.command.input` |
| `2026-06-24 13:04:57` | `cowrie.log.closed` |
| `2026-06-24 13:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03f6d9303c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:05 |
| **Last Seen** | 2026-06-24 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:05:51` | `cowrie.session.connect` |
| `2026-06-24 13:05:51` | `cowrie.client.version` |
| `2026-06-24 13:05:51` | `cowrie.client.kex` |
| `2026-06-24 13:05:51` | `cowrie.login.success` |
| `2026-06-24 13:05:52` | `cowrie.session.params` |
| `2026-06-24 13:05:52` | `cowrie.command.input` |
| `2026-06-24 13:05:52` | `cowrie.log.closed` |
| `2026-06-24 13:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da370555f9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:06 |
| **Last Seen** | 2026-06-24 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:06:44` | `cowrie.session.connect` |
| `2026-06-24 13:06:44` | `cowrie.client.version` |
| `2026-06-24 13:06:44` | `cowrie.client.kex` |
| `2026-06-24 13:06:45` | `cowrie.login.success` |
| `2026-06-24 13:06:46` | `cowrie.session.params` |
| `2026-06-24 13:06:46` | `cowrie.command.input` |
| `2026-06-24 13:06:46` | `cowrie.log.closed` |
| `2026-06-24 13:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6bc2e735ffd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:07 |
| **Last Seen** | 2026-06-24 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:07:37` | `cowrie.session.connect` |
| `2026-06-24 13:07:37` | `cowrie.client.version` |
| `2026-06-24 13:07:37` | `cowrie.client.kex` |
| `2026-06-24 13:07:38` | `cowrie.login.success` |
| `2026-06-24 13:07:38` | `cowrie.session.params` |
| `2026-06-24 13:07:38` | `cowrie.command.input` |
| `2026-06-24 13:07:38` | `cowrie.log.closed` |
| `2026-06-24 13:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a9e59eed52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:08 |
| **Last Seen** | 2026-06-24 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:08:31` | `cowrie.session.connect` |
| `2026-06-24 13:08:31` | `cowrie.client.version` |
| `2026-06-24 13:08:31` | `cowrie.client.kex` |
| `2026-06-24 13:08:31` | `cowrie.login.success` |
| `2026-06-24 13:08:32` | `cowrie.session.params` |
| `2026-06-24 13:08:32` | `cowrie.command.input` |
| `2026-06-24 13:08:32` | `cowrie.log.closed` |
| `2026-06-24 13:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610a127b458a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:09 |
| **Last Seen** | 2026-06-24 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:09:23` | `cowrie.session.connect` |
| `2026-06-24 13:09:23` | `cowrie.client.version` |
| `2026-06-24 13:09:23` | `cowrie.client.kex` |
| `2026-06-24 13:09:24` | `cowrie.login.success` |
| `2026-06-24 13:09:25` | `cowrie.session.params` |
| `2026-06-24 13:09:25` | `cowrie.command.input` |
| `2026-06-24 13:09:25` | `cowrie.log.closed` |
| `2026-06-24 13:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868a74a3c339

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:10 |
| **Last Seen** | 2026-06-24 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:10:17` | `cowrie.session.connect` |
| `2026-06-24 13:10:17` | `cowrie.client.version` |
| `2026-06-24 13:10:17` | `cowrie.client.kex` |
| `2026-06-24 13:10:17` | `cowrie.login.success` |
| `2026-06-24 13:10:18` | `cowrie.session.params` |
| `2026-06-24 13:10:18` | `cowrie.command.input` |
| `2026-06-24 13:10:18` | `cowrie.log.closed` |
| `2026-06-24 13:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a77a6ca13a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:11 |
| **Last Seen** | 2026-06-24 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:11:12` | `cowrie.session.connect` |
| `2026-06-24 13:11:12` | `cowrie.client.version` |
| `2026-06-24 13:11:12` | `cowrie.client.kex` |
| `2026-06-24 13:11:12` | `cowrie.login.success` |
| `2026-06-24 13:11:13` | `cowrie.session.params` |
| `2026-06-24 13:11:13` | `cowrie.command.input` |
| `2026-06-24 13:11:13` | `cowrie.log.closed` |
| `2026-06-24 13:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e173e79b71

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:12 |
| **Last Seen** | 2026-06-24 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:12:07` | `cowrie.session.connect` |
| `2026-06-24 13:12:07` | `cowrie.client.version` |
| `2026-06-24 13:12:07` | `cowrie.client.kex` |
| `2026-06-24 13:12:08` | `cowrie.login.success` |
| `2026-06-24 13:12:08` | `cowrie.session.params` |
| `2026-06-24 13:12:08` | `cowrie.command.input` |
| `2026-06-24 13:12:09` | `cowrie.log.closed` |
| `2026-06-24 13:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc186c3cfabf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:13 |
| **Last Seen** | 2026-06-24 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:13:02` | `cowrie.session.connect` |
| `2026-06-24 13:13:02` | `cowrie.client.version` |
| `2026-06-24 13:13:02` | `cowrie.client.kex` |
| `2026-06-24 13:13:03` | `cowrie.login.success` |
| `2026-06-24 13:13:03` | `cowrie.session.params` |
| `2026-06-24 13:13:03` | `cowrie.command.input` |
| `2026-06-24 13:13:04` | `cowrie.log.closed` |
| `2026-06-24 13:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3dae3538c90

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:13 |
| **Last Seen** | 2026-06-24 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:13:56` | `cowrie.session.connect` |
| `2026-06-24 13:13:56` | `cowrie.client.version` |
| `2026-06-24 13:13:56` | `cowrie.client.kex` |
| `2026-06-24 13:13:57` | `cowrie.login.success` |
| `2026-06-24 13:13:57` | `cowrie.session.params` |
| `2026-06-24 13:13:57` | `cowrie.command.input` |
| `2026-06-24 13:13:57` | `cowrie.log.closed` |
| `2026-06-24 13:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5750423947c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:14 |
| **Last Seen** | 2026-06-24 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:14:50` | `cowrie.session.connect` |
| `2026-06-24 13:14:50` | `cowrie.client.version` |
| `2026-06-24 13:14:50` | `cowrie.client.kex` |
| `2026-06-24 13:14:51` | `cowrie.login.success` |
| `2026-06-24 13:14:51` | `cowrie.session.params` |
| `2026-06-24 13:14:51` | `cowrie.command.input` |
| `2026-06-24 13:14:51` | `cowrie.log.closed` |
| `2026-06-24 13:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3f5f99ffe0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:15 |
| **Last Seen** | 2026-06-24 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:15:45` | `cowrie.session.connect` |
| `2026-06-24 13:15:45` | `cowrie.client.version` |
| `2026-06-24 13:15:45` | `cowrie.client.kex` |
| `2026-06-24 13:15:45` | `cowrie.login.success` |
| `2026-06-24 13:15:46` | `cowrie.session.params` |
| `2026-06-24 13:15:46` | `cowrie.command.input` |
| `2026-06-24 13:15:46` | `cowrie.log.closed` |
| `2026-06-24 13:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9176997b68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:16 |
| **Last Seen** | 2026-06-24 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:16:40` | `cowrie.session.connect` |
| `2026-06-24 13:16:40` | `cowrie.client.version` |
| `2026-06-24 13:16:40` | `cowrie.client.kex` |
| `2026-06-24 13:16:41` | `cowrie.login.success` |
| `2026-06-24 13:16:42` | `cowrie.session.params` |
| `2026-06-24 13:16:42` | `cowrie.command.input` |
| `2026-06-24 13:16:42` | `cowrie.log.closed` |
| `2026-06-24 13:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0fed91924d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:17 |
| **Last Seen** | 2026-06-24 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:17:36` | `cowrie.session.connect` |
| `2026-06-24 13:17:36` | `cowrie.client.version` |
| `2026-06-24 13:17:36` | `cowrie.client.kex` |
| `2026-06-24 13:17:37` | `cowrie.login.success` |
| `2026-06-24 13:17:37` | `cowrie.session.params` |
| `2026-06-24 13:17:37` | `cowrie.command.input` |
| `2026-06-24 13:17:37` | `cowrie.log.closed` |
| `2026-06-24 13:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8f01f488731

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 13:17 |
| **Last Seen** | 2026-06-24 13:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:17:46` | `cowrie.session.connect` |
| `2026-06-24 13:17:47` | `cowrie.client.version` |
| `2026-06-24 13:17:47` | `cowrie.client.kex` |
| `2026-06-24 13:17:54` | `cowrie.login.success` |
| `2026-06-24 13:17:57` | `cowrie.session.params` |
| `2026-06-24 13:17:57` | `cowrie.command.input` |
| `2026-06-24 13:17:59` | `cowrie.log.closed` |
| `2026-06-24 13:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1fca70bf5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:18 |
| **Last Seen** | 2026-06-24 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:18:34` | `cowrie.session.connect` |
| `2026-06-24 13:18:34` | `cowrie.client.version` |
| `2026-06-24 13:18:34` | `cowrie.client.kex` |
| `2026-06-24 13:18:35` | `cowrie.login.success` |
| `2026-06-24 13:18:35` | `cowrie.session.params` |
| `2026-06-24 13:18:35` | `cowrie.command.input` |
| `2026-06-24 13:18:35` | `cowrie.log.closed` |
| `2026-06-24 13:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-992230479214

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:19 |
| **Last Seen** | 2026-06-24 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:19:31` | `cowrie.session.connect` |
| `2026-06-24 13:19:31` | `cowrie.client.version` |
| `2026-06-24 13:19:31` | `cowrie.client.kex` |
| `2026-06-24 13:19:32` | `cowrie.login.success` |
| `2026-06-24 13:19:32` | `cowrie.session.params` |
| `2026-06-24 13:19:32` | `cowrie.command.input` |
| `2026-06-24 13:19:32` | `cowrie.log.closed` |
| `2026-06-24 13:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b4de593142b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:20 |
| **Last Seen** | 2026-06-24 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:20:28` | `cowrie.session.connect` |
| `2026-06-24 13:20:28` | `cowrie.client.version` |
| `2026-06-24 13:20:28` | `cowrie.client.kex` |
| `2026-06-24 13:20:28` | `cowrie.login.success` |
| `2026-06-24 13:20:29` | `cowrie.session.params` |
| `2026-06-24 13:20:29` | `cowrie.command.input` |
| `2026-06-24 13:20:29` | `cowrie.log.closed` |
| `2026-06-24 13:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465980127ed0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:21 |
| **Last Seen** | 2026-06-24 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:21:24` | `cowrie.session.connect` |
| `2026-06-24 13:21:24` | `cowrie.client.version` |
| `2026-06-24 13:21:24` | `cowrie.client.kex` |
| `2026-06-24 13:21:24` | `cowrie.login.success` |
| `2026-06-24 13:21:25` | `cowrie.session.params` |
| `2026-06-24 13:21:25` | `cowrie.command.input` |
| `2026-06-24 13:21:25` | `cowrie.log.closed` |
| `2026-06-24 13:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b5a5bf6bdf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:22 |
| **Last Seen** | 2026-06-24 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:22:19` | `cowrie.session.connect` |
| `2026-06-24 13:22:19` | `cowrie.client.version` |
| `2026-06-24 13:22:19` | `cowrie.client.kex` |
| `2026-06-24 13:22:19` | `cowrie.login.success` |
| `2026-06-24 13:22:20` | `cowrie.session.params` |
| `2026-06-24 13:22:20` | `cowrie.command.input` |
| `2026-06-24 13:22:20` | `cowrie.log.closed` |
| `2026-06-24 13:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7f13ad5a77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:23 |
| **Last Seen** | 2026-06-24 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:23:15` | `cowrie.session.connect` |
| `2026-06-24 13:23:15` | `cowrie.client.version` |
| `2026-06-24 13:23:16` | `cowrie.client.kex` |
| `2026-06-24 13:23:16` | `cowrie.login.success` |
| `2026-06-24 13:23:17` | `cowrie.session.params` |
| `2026-06-24 13:23:17` | `cowrie.command.input` |
| `2026-06-24 13:23:17` | `cowrie.log.closed` |
| `2026-06-24 13:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00adaae76429

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:24 |
| **Last Seen** | 2026-06-24 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:24:12` | `cowrie.session.connect` |
| `2026-06-24 13:24:12` | `cowrie.client.version` |
| `2026-06-24 13:24:12` | `cowrie.client.kex` |
| `2026-06-24 13:24:13` | `cowrie.login.success` |
| `2026-06-24 13:24:13` | `cowrie.session.params` |
| `2026-06-24 13:24:13` | `cowrie.command.input` |
| `2026-06-24 13:24:13` | `cowrie.log.closed` |
| `2026-06-24 13:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a9338dc30d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:25 |
| **Last Seen** | 2026-06-24 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:25:10` | `cowrie.session.connect` |
| `2026-06-24 13:25:10` | `cowrie.client.version` |
| `2026-06-24 13:25:10` | `cowrie.client.kex` |
| `2026-06-24 13:25:10` | `cowrie.login.success` |
| `2026-06-24 13:25:11` | `cowrie.session.params` |
| `2026-06-24 13:25:11` | `cowrie.command.input` |
| `2026-06-24 13:25:11` | `cowrie.log.closed` |
| `2026-06-24 13:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0f184d3467

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:26 |
| **Last Seen** | 2026-06-24 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:26:07` | `cowrie.session.connect` |
| `2026-06-24 13:26:07` | `cowrie.client.version` |
| `2026-06-24 13:26:07` | `cowrie.client.kex` |
| `2026-06-24 13:26:07` | `cowrie.login.success` |
| `2026-06-24 13:26:08` | `cowrie.session.params` |
| `2026-06-24 13:26:08` | `cowrie.command.input` |
| `2026-06-24 13:26:08` | `cowrie.log.closed` |
| `2026-06-24 13:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2681c8f08f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:27 |
| **Last Seen** | 2026-06-24 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:27:04` | `cowrie.session.connect` |
| `2026-06-24 13:27:04` | `cowrie.client.version` |
| `2026-06-24 13:27:04` | `cowrie.client.kex` |
| `2026-06-24 13:27:04` | `cowrie.login.success` |
| `2026-06-24 13:27:05` | `cowrie.session.params` |
| `2026-06-24 13:27:05` | `cowrie.command.input` |
| `2026-06-24 13:27:05` | `cowrie.log.closed` |
| `2026-06-24 13:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ddf12fe72f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:27 |
| **Last Seen** | 2026-06-24 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:27:59` | `cowrie.session.connect` |
| `2026-06-24 13:27:59` | `cowrie.client.version` |
| `2026-06-24 13:27:59` | `cowrie.client.kex` |
| `2026-06-24 13:28:00` | `cowrie.login.success` |
| `2026-06-24 13:28:01` | `cowrie.session.params` |
| `2026-06-24 13:28:01` | `cowrie.command.input` |
| `2026-06-24 13:28:01` | `cowrie.log.closed` |
| `2026-06-24 13:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d474edbcbf73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:28 |
| **Last Seen** | 2026-06-24 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:28:56` | `cowrie.session.connect` |
| `2026-06-24 13:28:56` | `cowrie.client.version` |
| `2026-06-24 13:28:56` | `cowrie.client.kex` |
| `2026-06-24 13:28:56` | `cowrie.login.success` |
| `2026-06-24 13:28:57` | `cowrie.session.params` |
| `2026-06-24 13:28:57` | `cowrie.command.input` |
| `2026-06-24 13:28:57` | `cowrie.log.closed` |
| `2026-06-24 13:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-276b6f67d272

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:29 |
| **Last Seen** | 2026-06-24 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:29:53` | `cowrie.session.connect` |
| `2026-06-24 13:29:53` | `cowrie.client.version` |
| `2026-06-24 13:29:53` | `cowrie.client.kex` |
| `2026-06-24 13:29:53` | `cowrie.login.success` |
| `2026-06-24 13:29:54` | `cowrie.session.params` |
| `2026-06-24 13:29:54` | `cowrie.command.input` |
| `2026-06-24 13:29:54` | `cowrie.log.closed` |
| `2026-06-24 13:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2a9496829d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 13:30 |
| **Last Seen** | 2026-06-24 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:30:02` | `cowrie.session.connect` |
| `2026-06-24 13:30:02` | `cowrie.client.version` |
| `2026-06-24 13:30:02` | `cowrie.client.kex` |
| `2026-06-24 13:30:02` | `cowrie.login.success` |
| `2026-06-24 13:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395cbcef4633

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 13:30 |
| **Last Seen** | 2026-06-24 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:30:03` | `cowrie.session.connect` |
| `2026-06-24 13:30:03` | `cowrie.client.version` |
| `2026-06-24 13:30:03` | `cowrie.client.kex` |
| `2026-06-24 13:30:03` | `cowrie.login.success` |
| `2026-06-24 13:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-653cd324fb32

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 13:30 |
| **Last Seen** | 2026-06-24 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:30:08` | `cowrie.session.connect` |
| `2026-06-24 13:30:08` | `cowrie.client.version` |
| `2026-06-24 13:30:08` | `cowrie.client.kex` |
| `2026-06-24 13:30:08` | `cowrie.login.success` |
| `2026-06-24 13:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4d79ec752d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 13:30 |
| **Last Seen** | 2026-06-24 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:30:08` | `cowrie.session.connect` |
| `2026-06-24 13:30:08` | `cowrie.client.version` |
| `2026-06-24 13:30:08` | `cowrie.client.kex` |
| `2026-06-24 13:30:08` | `cowrie.login.success` |
| `2026-06-24 13:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfb94c96f4a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:30 |
| **Last Seen** | 2026-06-24 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:30:51` | `cowrie.session.connect` |
| `2026-06-24 13:30:51` | `cowrie.client.version` |
| `2026-06-24 13:30:51` | `cowrie.client.kex` |
| `2026-06-24 13:30:51` | `cowrie.login.success` |
| `2026-06-24 13:30:52` | `cowrie.session.params` |
| `2026-06-24 13:30:52` | `cowrie.command.input` |
| `2026-06-24 13:30:52` | `cowrie.log.closed` |
| `2026-06-24 13:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd30f3d72fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:31 |
| **Last Seen** | 2026-06-24 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:31:50` | `cowrie.session.connect` |
| `2026-06-24 13:31:50` | `cowrie.client.version` |
| `2026-06-24 13:31:50` | `cowrie.client.kex` |
| `2026-06-24 13:31:50` | `cowrie.login.success` |
| `2026-06-24 13:31:51` | `cowrie.session.params` |
| `2026-06-24 13:31:51` | `cowrie.command.input` |
| `2026-06-24 13:31:51` | `cowrie.log.closed` |
| `2026-06-24 13:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765f958b6640

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 13:32 |
| **Last Seen** | 2026-06-24 13:32 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:32:05` | `cowrie.session.connect` |
| `2026-06-24 13:32:07` | `cowrie.client.version` |
| `2026-06-24 13:32:07` | `cowrie.client.kex` |
| `2026-06-24 13:32:13` | `cowrie.login.success` |
| `2026-06-24 13:32:18` | `cowrie.session.params` |
| `2026-06-24 13:32:18` | `cowrie.command.input` |
| `2026-06-24 13:32:19` | `cowrie.log.closed` |
| `2026-06-24 13:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeebb3bd33d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:32 |
| **Last Seen** | 2026-06-24 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:32:50` | `cowrie.session.connect` |
| `2026-06-24 13:32:50` | `cowrie.client.version` |
| `2026-06-24 13:32:50` | `cowrie.client.kex` |
| `2026-06-24 13:32:50` | `cowrie.login.success` |
| `2026-06-24 13:32:51` | `cowrie.session.params` |
| `2026-06-24 13:32:51` | `cowrie.command.input` |
| `2026-06-24 13:32:51` | `cowrie.log.closed` |
| `2026-06-24 13:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f9ff2031de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:33 |
| **Last Seen** | 2026-06-24 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:33:46` | `cowrie.session.connect` |
| `2026-06-24 13:33:46` | `cowrie.client.version` |
| `2026-06-24 13:33:46` | `cowrie.client.kex` |
| `2026-06-24 13:33:46` | `cowrie.login.success` |
| `2026-06-24 13:33:47` | `cowrie.session.params` |
| `2026-06-24 13:33:47` | `cowrie.command.input` |
| `2026-06-24 13:33:47` | `cowrie.log.closed` |
| `2026-06-24 13:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b158c2e5b46e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:34 |
| **Last Seen** | 2026-06-24 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:34:42` | `cowrie.session.connect` |
| `2026-06-24 13:34:42` | `cowrie.client.version` |
| `2026-06-24 13:34:43` | `cowrie.client.kex` |
| `2026-06-24 13:34:43` | `cowrie.login.success` |
| `2026-06-24 13:34:44` | `cowrie.session.params` |
| `2026-06-24 13:34:44` | `cowrie.command.input` |
| `2026-06-24 13:34:44` | `cowrie.log.closed` |
| `2026-06-24 13:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db5ede656130

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:35 |
| **Last Seen** | 2026-06-24 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:35:39` | `cowrie.session.connect` |
| `2026-06-24 13:35:39` | `cowrie.client.version` |
| `2026-06-24 13:35:39` | `cowrie.client.kex` |
| `2026-06-24 13:35:40` | `cowrie.login.success` |
| `2026-06-24 13:35:40` | `cowrie.session.params` |
| `2026-06-24 13:35:40` | `cowrie.command.input` |
| `2026-06-24 13:35:40` | `cowrie.log.closed` |
| `2026-06-24 13:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeeca58bf12c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:36 |
| **Last Seen** | 2026-06-24 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:36:37` | `cowrie.session.connect` |
| `2026-06-24 13:36:37` | `cowrie.client.version` |
| `2026-06-24 13:36:37` | `cowrie.client.kex` |
| `2026-06-24 13:36:38` | `cowrie.login.success` |
| `2026-06-24 13:36:38` | `cowrie.session.params` |
| `2026-06-24 13:36:38` | `cowrie.command.input` |
| `2026-06-24 13:36:39` | `cowrie.log.closed` |
| `2026-06-24 13:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a48a12f5c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:37 |
| **Last Seen** | 2026-06-24 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:37:36` | `cowrie.session.connect` |
| `2026-06-24 13:37:36` | `cowrie.client.version` |
| `2026-06-24 13:37:36` | `cowrie.client.kex` |
| `2026-06-24 13:37:37` | `cowrie.login.success` |
| `2026-06-24 13:37:37` | `cowrie.session.params` |
| `2026-06-24 13:37:37` | `cowrie.command.input` |
| `2026-06-24 13:37:38` | `cowrie.log.closed` |
| `2026-06-24 13:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0837c7ccbc0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:38 |
| **Last Seen** | 2026-06-24 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:38:35` | `cowrie.session.connect` |
| `2026-06-24 13:38:35` | `cowrie.client.version` |
| `2026-06-24 13:38:35` | `cowrie.client.kex` |
| `2026-06-24 13:38:35` | `cowrie.login.success` |
| `2026-06-24 13:38:36` | `cowrie.session.params` |
| `2026-06-24 13:38:36` | `cowrie.command.input` |
| `2026-06-24 13:38:36` | `cowrie.log.closed` |
| `2026-06-24 13:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db3f55f0fb1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:39 |
| **Last Seen** | 2026-06-24 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:39:33` | `cowrie.session.connect` |
| `2026-06-24 13:39:33` | `cowrie.client.version` |
| `2026-06-24 13:39:33` | `cowrie.client.kex` |
| `2026-06-24 13:39:33` | `cowrie.login.success` |
| `2026-06-24 13:39:34` | `cowrie.session.params` |
| `2026-06-24 13:39:34` | `cowrie.command.input` |
| `2026-06-24 13:39:34` | `cowrie.log.closed` |
| `2026-06-24 13:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec0d8643577f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:40 |
| **Last Seen** | 2026-06-24 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:40:32` | `cowrie.session.connect` |
| `2026-06-24 13:40:32` | `cowrie.client.version` |
| `2026-06-24 13:40:32` | `cowrie.client.kex` |
| `2026-06-24 13:40:32` | `cowrie.login.success` |
| `2026-06-24 13:40:33` | `cowrie.session.params` |
| `2026-06-24 13:40:33` | `cowrie.command.input` |
| `2026-06-24 13:40:33` | `cowrie.log.closed` |
| `2026-06-24 13:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5bbe09d299c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:41 |
| **Last Seen** | 2026-06-24 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:41:30` | `cowrie.session.connect` |
| `2026-06-24 13:41:30` | `cowrie.client.version` |
| `2026-06-24 13:41:30` | `cowrie.client.kex` |
| `2026-06-24 13:41:31` | `cowrie.login.success` |
| `2026-06-24 13:41:31` | `cowrie.session.params` |
| `2026-06-24 13:41:31` | `cowrie.command.input` |
| `2026-06-24 13:41:32` | `cowrie.log.closed` |
| `2026-06-24 13:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c51cba37bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:42 |
| **Last Seen** | 2026-06-24 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:42:30` | `cowrie.session.connect` |
| `2026-06-24 13:42:30` | `cowrie.client.version` |
| `2026-06-24 13:42:30` | `cowrie.client.kex` |
| `2026-06-24 13:42:30` | `cowrie.login.success` |
| `2026-06-24 13:42:31` | `cowrie.session.params` |
| `2026-06-24 13:42:31` | `cowrie.command.input` |
| `2026-06-24 13:42:31` | `cowrie.log.closed` |
| `2026-06-24 13:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951622fba9ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:43 |
| **Last Seen** | 2026-06-24 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:43:29` | `cowrie.session.connect` |
| `2026-06-24 13:43:29` | `cowrie.client.version` |
| `2026-06-24 13:43:29` | `cowrie.client.kex` |
| `2026-06-24 13:43:29` | `cowrie.login.success` |
| `2026-06-24 13:43:30` | `cowrie.session.params` |
| `2026-06-24 13:43:30` | `cowrie.command.input` |
| `2026-06-24 13:43:30` | `cowrie.log.closed` |
| `2026-06-24 13:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db5b897afd8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:44 |
| **Last Seen** | 2026-06-24 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:44:31` | `cowrie.session.connect` |
| `2026-06-24 13:44:31` | `cowrie.client.version` |
| `2026-06-24 13:44:31` | `cowrie.client.kex` |
| `2026-06-24 13:44:32` | `cowrie.login.success` |
| `2026-06-24 13:44:32` | `cowrie.session.params` |
| `2026-06-24 13:44:32` | `cowrie.command.input` |
| `2026-06-24 13:44:33` | `cowrie.log.closed` |
| `2026-06-24 13:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22e9e95b4d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:45 |
| **Last Seen** | 2026-06-24 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:45:29` | `cowrie.session.connect` |
| `2026-06-24 13:45:29` | `cowrie.client.version` |
| `2026-06-24 13:45:29` | `cowrie.client.kex` |
| `2026-06-24 13:45:30` | `cowrie.login.success` |
| `2026-06-24 13:45:31` | `cowrie.session.params` |
| `2026-06-24 13:45:31` | `cowrie.command.input` |
| `2026-06-24 13:45:31` | `cowrie.log.closed` |
| `2026-06-24 13:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0edb96174388

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 13:46 |
| **Last Seen** | 2026-06-24 13:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:46:06` | `cowrie.session.connect` |
| `2026-06-24 13:46:07` | `cowrie.client.version` |
| `2026-06-24 13:46:07` | `cowrie.client.kex` |
| `2026-06-24 13:46:13` | `cowrie.login.success` |
| `2026-06-24 13:46:17` | `cowrie.session.params` |
| `2026-06-24 13:46:17` | `cowrie.command.input` |
| `2026-06-24 13:46:19` | `cowrie.log.closed` |
| `2026-06-24 13:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21d55df49eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:46 |
| **Last Seen** | 2026-06-24 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:46:28` | `cowrie.session.connect` |
| `2026-06-24 13:46:28` | `cowrie.client.version` |
| `2026-06-24 13:46:28` | `cowrie.client.kex` |
| `2026-06-24 13:46:28` | `cowrie.login.success` |
| `2026-06-24 13:46:29` | `cowrie.session.params` |
| `2026-06-24 13:46:29` | `cowrie.command.input` |
| `2026-06-24 13:46:29` | `cowrie.log.closed` |
| `2026-06-24 13:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d30a3be5df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:47 |
| **Last Seen** | 2026-06-24 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:47:26` | `cowrie.session.connect` |
| `2026-06-24 13:47:26` | `cowrie.client.version` |
| `2026-06-24 13:47:26` | `cowrie.client.kex` |
| `2026-06-24 13:47:26` | `cowrie.login.success` |
| `2026-06-24 13:47:27` | `cowrie.session.params` |
| `2026-06-24 13:47:27` | `cowrie.command.input` |
| `2026-06-24 13:47:27` | `cowrie.log.closed` |
| `2026-06-24 13:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4a65e165fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:48 |
| **Last Seen** | 2026-06-24 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:48:27` | `cowrie.session.connect` |
| `2026-06-24 13:48:27` | `cowrie.client.version` |
| `2026-06-24 13:48:27` | `cowrie.client.kex` |
| `2026-06-24 13:48:27` | `cowrie.login.success` |
| `2026-06-24 13:48:28` | `cowrie.session.params` |
| `2026-06-24 13:48:28` | `cowrie.command.input` |
| `2026-06-24 13:48:28` | `cowrie.log.closed` |
| `2026-06-24 13:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3c1b4f4479

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:49 |
| **Last Seen** | 2026-06-24 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:49:28` | `cowrie.session.connect` |
| `2026-06-24 13:49:28` | `cowrie.client.version` |
| `2026-06-24 13:49:28` | `cowrie.client.kex` |
| `2026-06-24 13:49:28` | `cowrie.login.success` |
| `2026-06-24 13:49:29` | `cowrie.session.params` |
| `2026-06-24 13:49:29` | `cowrie.command.input` |
| `2026-06-24 13:49:29` | `cowrie.log.closed` |
| `2026-06-24 13:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6e4e544dad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:50 |
| **Last Seen** | 2026-06-24 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:50:31` | `cowrie.session.connect` |
| `2026-06-24 13:50:31` | `cowrie.client.version` |
| `2026-06-24 13:50:31` | `cowrie.client.kex` |
| `2026-06-24 13:50:31` | `cowrie.login.success` |
| `2026-06-24 13:50:32` | `cowrie.session.params` |
| `2026-06-24 13:50:32` | `cowrie.command.input` |
| `2026-06-24 13:50:32` | `cowrie.log.closed` |
| `2026-06-24 13:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dbfec6fee36

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:51 |
| **Last Seen** | 2026-06-24 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:51:31` | `cowrie.session.connect` |
| `2026-06-24 13:51:31` | `cowrie.client.version` |
| `2026-06-24 13:51:31` | `cowrie.client.kex` |
| `2026-06-24 13:51:32` | `cowrie.login.success` |
| `2026-06-24 13:51:33` | `cowrie.session.params` |
| `2026-06-24 13:51:33` | `cowrie.command.input` |
| `2026-06-24 13:51:33` | `cowrie.log.closed` |
| `2026-06-24 13:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef3a0b216750

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:52 |
| **Last Seen** | 2026-06-24 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:52:31` | `cowrie.session.connect` |
| `2026-06-24 13:52:31` | `cowrie.client.version` |
| `2026-06-24 13:52:31` | `cowrie.client.kex` |
| `2026-06-24 13:52:32` | `cowrie.login.success` |
| `2026-06-24 13:52:33` | `cowrie.session.params` |
| `2026-06-24 13:52:33` | `cowrie.command.input` |
| `2026-06-24 13:52:33` | `cowrie.log.closed` |
| `2026-06-24 13:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc79cae6cbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:53 |
| **Last Seen** | 2026-06-24 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:53:28` | `cowrie.session.connect` |
| `2026-06-24 13:53:28` | `cowrie.client.version` |
| `2026-06-24 13:53:28` | `cowrie.client.kex` |
| `2026-06-24 13:53:28` | `cowrie.login.success` |
| `2026-06-24 13:53:29` | `cowrie.session.params` |
| `2026-06-24 13:53:29` | `cowrie.command.input` |
| `2026-06-24 13:53:29` | `cowrie.log.closed` |
| `2026-06-24 13:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f0373512dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:54 |
| **Last Seen** | 2026-06-24 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:54:26` | `cowrie.session.connect` |
| `2026-06-24 13:54:26` | `cowrie.client.version` |
| `2026-06-24 13:54:26` | `cowrie.client.kex` |
| `2026-06-24 13:54:27` | `cowrie.login.success` |
| `2026-06-24 13:54:27` | `cowrie.session.params` |
| `2026-06-24 13:54:27` | `cowrie.command.input` |
| `2026-06-24 13:54:28` | `cowrie.log.closed` |
| `2026-06-24 13:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eee9219656a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:55 |
| **Last Seen** | 2026-06-24 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:55:25` | `cowrie.session.connect` |
| `2026-06-24 13:55:25` | `cowrie.client.version` |
| `2026-06-24 13:55:25` | `cowrie.client.kex` |
| `2026-06-24 13:55:25` | `cowrie.login.success` |
| `2026-06-24 13:55:26` | `cowrie.session.params` |
| `2026-06-24 13:55:26` | `cowrie.command.input` |
| `2026-06-24 13:55:26` | `cowrie.log.closed` |
| `2026-06-24 13:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b522e57576

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:56 |
| **Last Seen** | 2026-06-24 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:56:25` | `cowrie.session.connect` |
| `2026-06-24 13:56:25` | `cowrie.client.version` |
| `2026-06-24 13:56:25` | `cowrie.client.kex` |
| `2026-06-24 13:56:25` | `cowrie.login.success` |
| `2026-06-24 13:56:26` | `cowrie.session.params` |
| `2026-06-24 13:56:26` | `cowrie.command.input` |
| `2026-06-24 13:56:26` | `cowrie.log.closed` |
| `2026-06-24 13:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd146c63758d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:57 |
| **Last Seen** | 2026-06-24 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:57:29` | `cowrie.session.connect` |
| `2026-06-24 13:57:29` | `cowrie.client.version` |
| `2026-06-24 13:57:29` | `cowrie.client.kex` |
| `2026-06-24 13:57:29` | `cowrie.login.success` |
| `2026-06-24 13:57:30` | `cowrie.session.params` |
| `2026-06-24 13:57:30` | `cowrie.command.input` |
| `2026-06-24 13:57:30` | `cowrie.log.closed` |
| `2026-06-24 13:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896aaf185734

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:58 |
| **Last Seen** | 2026-06-24 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:58:29` | `cowrie.session.connect` |
| `2026-06-24 13:58:29` | `cowrie.client.version` |
| `2026-06-24 13:58:30` | `cowrie.client.kex` |
| `2026-06-24 13:58:30` | `cowrie.login.success` |
| `2026-06-24 13:58:31` | `cowrie.session.params` |
| `2026-06-24 13:58:31` | `cowrie.command.input` |
| `2026-06-24 13:58:31` | `cowrie.log.closed` |
| `2026-06-24 13:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885aabc9df3a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 13:59 |
| **Last Seen** | 2026-06-24 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 13:59:29` | `cowrie.session.connect` |
| `2026-06-24 13:59:29` | `cowrie.client.version` |
| `2026-06-24 13:59:29` | `cowrie.client.kex` |
| `2026-06-24 13:59:29` | `cowrie.login.success` |
| `2026-06-24 13:59:30` | `cowrie.session.params` |
| `2026-06-24 13:59:30` | `cowrie.command.input` |
| `2026-06-24 13:59:30` | `cowrie.log.closed` |
| `2026-06-24 13:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd868daa6600

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 14:00 |
| **Last Seen** | 2026-06-24 14:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:00:12` | `cowrie.session.connect` |
| `2026-06-24 14:00:14` | `cowrie.client.version` |
| `2026-06-24 14:00:14` | `cowrie.client.kex` |
| `2026-06-24 14:00:20` | `cowrie.login.success` |
| `2026-06-24 14:00:24` | `cowrie.session.params` |
| `2026-06-24 14:00:24` | `cowrie.command.input` |
| `2026-06-24 14:00:26` | `cowrie.log.closed` |
| `2026-06-24 14:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9928c1abd5c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:00 |
| **Last Seen** | 2026-06-24 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:00:26` | `cowrie.session.connect` |
| `2026-06-24 14:00:26` | `cowrie.client.version` |
| `2026-06-24 14:00:26` | `cowrie.client.kex` |
| `2026-06-24 14:00:26` | `cowrie.login.success` |
| `2026-06-24 14:00:27` | `cowrie.session.params` |
| `2026-06-24 14:00:27` | `cowrie.command.input` |
| `2026-06-24 14:00:27` | `cowrie.log.closed` |
| `2026-06-24 14:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e831b0a1a429

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:01 |
| **Last Seen** | 2026-06-24 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:01:14` | `cowrie.session.connect` |
| `2026-06-24 14:01:14` | `cowrie.client.version` |
| `2026-06-24 14:01:14` | `cowrie.client.kex` |
| `2026-06-24 14:01:14` | `cowrie.login.success` |
| `2026-06-24 14:01:15` | `cowrie.session.params` |
| `2026-06-24 14:01:15` | `cowrie.command.input` |
| `2026-06-24 14:01:15` | `cowrie.log.closed` |
| `2026-06-24 14:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394530ba7786

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:02 |
| **Last Seen** | 2026-06-24 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:02:01` | `cowrie.session.connect` |
| `2026-06-24 14:02:01` | `cowrie.client.version` |
| `2026-06-24 14:02:01` | `cowrie.client.kex` |
| `2026-06-24 14:02:01` | `cowrie.login.success` |
| `2026-06-24 14:02:02` | `cowrie.session.params` |
| `2026-06-24 14:02:02` | `cowrie.command.input` |
| `2026-06-24 14:02:02` | `cowrie.log.closed` |
| `2026-06-24 14:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09c93d6071b5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 14:02 |
| **Last Seen** | 2026-06-24 14:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:02:17` | `cowrie.session.connect` |
| `2026-06-24 14:02:17` | `cowrie.client.version` |
| `2026-06-24 14:02:17` | `cowrie.client.kex` |
| `2026-06-24 14:02:17` | `cowrie.login.success` |
| `2026-06-24 14:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59d44bc6fd6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 14:02 |
| **Last Seen** | 2026-06-24 14:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:02:17` | `cowrie.session.connect` |
| `2026-06-24 14:02:17` | `cowrie.client.version` |
| `2026-06-24 14:02:17` | `cowrie.client.kex` |
| `2026-06-24 14:02:18` | `cowrie.login.success` |
| `2026-06-24 14:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ac8b074f6d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 14:02 |
| **Last Seen** | 2026-06-24 14:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:02:18` | `cowrie.session.connect` |
| `2026-06-24 14:02:18` | `cowrie.client.version` |
| `2026-06-24 14:02:19` | `cowrie.client.kex` |
| `2026-06-24 14:02:19` | `cowrie.login.success` |
| `2026-06-24 14:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92277bfa2df4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 14:02 |
| **Last Seen** | 2026-06-24 14:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:02:19` | `cowrie.session.connect` |
| `2026-06-24 14:02:19` | `cowrie.client.version` |
| `2026-06-24 14:02:19` | `cowrie.client.kex` |
| `2026-06-24 14:02:20` | `cowrie.login.success` |
| `2026-06-24 14:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1d7cba1cfb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:02 |
| **Last Seen** | 2026-06-24 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:02:49` | `cowrie.session.connect` |
| `2026-06-24 14:02:49` | `cowrie.client.version` |
| `2026-06-24 14:02:49` | `cowrie.client.kex` |
| `2026-06-24 14:02:49` | `cowrie.login.success` |
| `2026-06-24 14:02:50` | `cowrie.session.params` |
| `2026-06-24 14:02:50` | `cowrie.command.input` |
| `2026-06-24 14:02:50` | `cowrie.log.closed` |
| `2026-06-24 14:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0073002b4049

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:03 |
| **Last Seen** | 2026-06-24 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:03:37` | `cowrie.session.connect` |
| `2026-06-24 14:03:37` | `cowrie.client.version` |
| `2026-06-24 14:03:37` | `cowrie.client.kex` |
| `2026-06-24 14:03:38` | `cowrie.login.success` |
| `2026-06-24 14:03:39` | `cowrie.session.params` |
| `2026-06-24 14:03:39` | `cowrie.command.input` |
| `2026-06-24 14:03:39` | `cowrie.log.closed` |
| `2026-06-24 14:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512fd37f9bac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:04 |
| **Last Seen** | 2026-06-24 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:04:27` | `cowrie.session.connect` |
| `2026-06-24 14:04:27` | `cowrie.client.version` |
| `2026-06-24 14:04:27` | `cowrie.client.kex` |
| `2026-06-24 14:04:27` | `cowrie.login.success` |
| `2026-06-24 14:04:28` | `cowrie.session.params` |
| `2026-06-24 14:04:28` | `cowrie.command.input` |
| `2026-06-24 14:04:28` | `cowrie.log.closed` |
| `2026-06-24 14:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e633c575f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:05 |
| **Last Seen** | 2026-06-24 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:05:14` | `cowrie.session.connect` |
| `2026-06-24 14:05:14` | `cowrie.client.version` |
| `2026-06-24 14:05:15` | `cowrie.client.kex` |
| `2026-06-24 14:05:15` | `cowrie.login.success` |
| `2026-06-24 14:05:16` | `cowrie.session.params` |
| `2026-06-24 14:05:16` | `cowrie.command.input` |
| `2026-06-24 14:05:16` | `cowrie.log.closed` |
| `2026-06-24 14:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33ad038c923

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:06 |
| **Last Seen** | 2026-06-24 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:06:01` | `cowrie.session.connect` |
| `2026-06-24 14:06:01` | `cowrie.client.version` |
| `2026-06-24 14:06:01` | `cowrie.client.kex` |
| `2026-06-24 14:06:02` | `cowrie.login.success` |
| `2026-06-24 14:06:02` | `cowrie.session.params` |
| `2026-06-24 14:06:02` | `cowrie.command.input` |
| `2026-06-24 14:06:03` | `cowrie.log.closed` |
| `2026-06-24 14:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-324ec40218a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:06 |
| **Last Seen** | 2026-06-24 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:06:48` | `cowrie.session.connect` |
| `2026-06-24 14:06:48` | `cowrie.client.version` |
| `2026-06-24 14:06:48` | `cowrie.client.kex` |
| `2026-06-24 14:06:48` | `cowrie.login.success` |
| `2026-06-24 14:06:49` | `cowrie.session.params` |
| `2026-06-24 14:06:49` | `cowrie.command.input` |
| `2026-06-24 14:06:49` | `cowrie.log.closed` |
| `2026-06-24 14:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa12d802cc8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:07 |
| **Last Seen** | 2026-06-24 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:07:35` | `cowrie.session.connect` |
| `2026-06-24 14:07:35` | `cowrie.client.version` |
| `2026-06-24 14:07:36` | `cowrie.client.kex` |
| `2026-06-24 14:07:36` | `cowrie.login.success` |
| `2026-06-24 14:07:37` | `cowrie.session.params` |
| `2026-06-24 14:07:37` | `cowrie.command.input` |
| `2026-06-24 14:07:37` | `cowrie.log.closed` |
| `2026-06-24 14:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb4c98dfa57c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:08 |
| **Last Seen** | 2026-06-24 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:08:26` | `cowrie.session.connect` |
| `2026-06-24 14:08:26` | `cowrie.client.version` |
| `2026-06-24 14:08:26` | `cowrie.client.kex` |
| `2026-06-24 14:08:27` | `cowrie.login.success` |
| `2026-06-24 14:08:28` | `cowrie.session.params` |
| `2026-06-24 14:08:28` | `cowrie.command.input` |
| `2026-06-24 14:08:28` | `cowrie.log.closed` |
| `2026-06-24 14:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b42666d0412

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:09 |
| **Last Seen** | 2026-06-24 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:09:19` | `cowrie.session.connect` |
| `2026-06-24 14:09:19` | `cowrie.client.version` |
| `2026-06-24 14:09:19` | `cowrie.client.kex` |
| `2026-06-24 14:09:19` | `cowrie.login.success` |
| `2026-06-24 14:09:20` | `cowrie.session.params` |
| `2026-06-24 14:09:20` | `cowrie.command.input` |
| `2026-06-24 14:09:20` | `cowrie.log.closed` |
| `2026-06-24 14:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba251b5fb0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:10 |
| **Last Seen** | 2026-06-24 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:10:12` | `cowrie.session.connect` |
| `2026-06-24 14:10:12` | `cowrie.client.version` |
| `2026-06-24 14:10:12` | `cowrie.client.kex` |
| `2026-06-24 14:10:13` | `cowrie.login.success` |
| `2026-06-24 14:10:13` | `cowrie.session.params` |
| `2026-06-24 14:10:13` | `cowrie.command.input` |
| `2026-06-24 14:10:14` | `cowrie.log.closed` |
| `2026-06-24 14:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae31b44848b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:11 |
| **Last Seen** | 2026-06-24 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:11:01` | `cowrie.session.connect` |
| `2026-06-24 14:11:01` | `cowrie.client.version` |
| `2026-06-24 14:11:01` | `cowrie.client.kex` |
| `2026-06-24 14:11:02` | `cowrie.login.success` |
| `2026-06-24 14:11:03` | `cowrie.session.params` |
| `2026-06-24 14:11:03` | `cowrie.command.input` |
| `2026-06-24 14:11:03` | `cowrie.log.closed` |
| `2026-06-24 14:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13fd30544d5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:11 |
| **Last Seen** | 2026-06-24 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:11:47` | `cowrie.session.connect` |
| `2026-06-24 14:11:47` | `cowrie.client.version` |
| `2026-06-24 14:11:47` | `cowrie.client.kex` |
| `2026-06-24 14:11:48` | `cowrie.login.success` |
| `2026-06-24 14:11:48` | `cowrie.session.params` |
| `2026-06-24 14:11:48` | `cowrie.command.input` |
| `2026-06-24 14:11:49` | `cowrie.log.closed` |
| `2026-06-24 14:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d3aea3a76e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:12 |
| **Last Seen** | 2026-06-24 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:12:35` | `cowrie.session.connect` |
| `2026-06-24 14:12:35` | `cowrie.client.version` |
| `2026-06-24 14:12:35` | `cowrie.client.kex` |
| `2026-06-24 14:12:35` | `cowrie.login.success` |
| `2026-06-24 14:12:36` | `cowrie.session.params` |
| `2026-06-24 14:12:36` | `cowrie.command.input` |
| `2026-06-24 14:12:36` | `cowrie.log.closed` |
| `2026-06-24 14:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484e06a011c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:13 |
| **Last Seen** | 2026-06-24 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:13:22` | `cowrie.session.connect` |
| `2026-06-24 14:13:22` | `cowrie.client.version` |
| `2026-06-24 14:13:22` | `cowrie.client.kex` |
| `2026-06-24 14:13:23` | `cowrie.login.success` |
| `2026-06-24 14:13:23` | `cowrie.session.params` |
| `2026-06-24 14:13:23` | `cowrie.command.input` |
| `2026-06-24 14:13:24` | `cowrie.log.closed` |
| `2026-06-24 14:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16448fcd7a74

| Field | Detail |
|---|---|
| **Source IP** | `171.111.218[.]2` |
| **First Seen** | 2026-06-24 14:13 |
| **Last Seen** | 2026-06-24 14:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:13:48` | `cowrie.session.connect` |
| `2026-06-24 14:13:48` | `cowrie.client.version` |
| `2026-06-24 14:13:48` | `cowrie.client.kex` |
| `2026-06-24 14:13:50` | `cowrie.login.success` |
| `2026-06-24 14:13:53` | `cowrie.session.params` |
| `2026-06-24 14:13:53` | `cowrie.command.input` |
| `2026-06-24 14:13:53` | `cowrie.log.closed` |
| `2026-06-24 14:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.111.218[.]2` to AbuseIPDB if not already reported
- [ ] Block `171.111.218[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6523e9b1a1f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:14 |
| **Last Seen** | 2026-06-24 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:14:10` | `cowrie.session.connect` |
| `2026-06-24 14:14:10` | `cowrie.client.version` |
| `2026-06-24 14:14:10` | `cowrie.client.kex` |
| `2026-06-24 14:14:10` | `cowrie.login.success` |
| `2026-06-24 14:14:11` | `cowrie.session.params` |
| `2026-06-24 14:14:11` | `cowrie.command.input` |
| `2026-06-24 14:14:11` | `cowrie.log.closed` |
| `2026-06-24 14:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2231a68840cc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 14:14 |
| **Last Seen** | 2026-06-24 14:14 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:14:33` | `cowrie.session.connect` |
| `2026-06-24 14:14:35` | `cowrie.client.version` |
| `2026-06-24 14:14:35` | `cowrie.client.kex` |
| `2026-06-24 14:14:42` | `cowrie.login.success` |
| `2026-06-24 14:14:46` | `cowrie.session.params` |
| `2026-06-24 14:14:46` | `cowrie.command.input` |
| `2026-06-24 14:14:48` | `cowrie.log.closed` |
| `2026-06-24 14:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ccc42bd957

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:14 |
| **Last Seen** | 2026-06-24 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:14:59` | `cowrie.session.connect` |
| `2026-06-24 14:14:59` | `cowrie.client.version` |
| `2026-06-24 14:14:59` | `cowrie.client.kex` |
| `2026-06-24 14:14:59` | `cowrie.login.success` |
| `2026-06-24 14:15:00` | `cowrie.session.params` |
| `2026-06-24 14:15:00` | `cowrie.command.input` |
| `2026-06-24 14:15:00` | `cowrie.log.closed` |
| `2026-06-24 14:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd13484ccc9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:15 |
| **Last Seen** | 2026-06-24 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:15:52` | `cowrie.session.connect` |
| `2026-06-24 14:15:52` | `cowrie.client.version` |
| `2026-06-24 14:15:52` | `cowrie.client.kex` |
| `2026-06-24 14:15:53` | `cowrie.login.success` |
| `2026-06-24 14:15:53` | `cowrie.session.params` |
| `2026-06-24 14:15:53` | `cowrie.command.input` |
| `2026-06-24 14:15:54` | `cowrie.log.closed` |
| `2026-06-24 14:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3da77be53a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:16 |
| **Last Seen** | 2026-06-24 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:16:41` | `cowrie.session.connect` |
| `2026-06-24 14:16:41` | `cowrie.client.version` |
| `2026-06-24 14:16:41` | `cowrie.client.kex` |
| `2026-06-24 14:16:41` | `cowrie.login.success` |
| `2026-06-24 14:16:42` | `cowrie.session.params` |
| `2026-06-24 14:16:42` | `cowrie.command.input` |
| `2026-06-24 14:16:42` | `cowrie.log.closed` |
| `2026-06-24 14:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4700265361e2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:17 |
| **Last Seen** | 2026-06-24 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:17:28` | `cowrie.session.connect` |
| `2026-06-24 14:17:28` | `cowrie.client.version` |
| `2026-06-24 14:17:28` | `cowrie.client.kex` |
| `2026-06-24 14:17:28` | `cowrie.login.success` |
| `2026-06-24 14:17:29` | `cowrie.session.params` |
| `2026-06-24 14:17:29` | `cowrie.command.input` |
| `2026-06-24 14:17:29` | `cowrie.log.closed` |
| `2026-06-24 14:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be02f14f635

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:18 |
| **Last Seen** | 2026-06-24 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:18:14` | `cowrie.session.connect` |
| `2026-06-24 14:18:14` | `cowrie.client.version` |
| `2026-06-24 14:18:14` | `cowrie.client.kex` |
| `2026-06-24 14:18:15` | `cowrie.login.success` |
| `2026-06-24 14:18:16` | `cowrie.session.params` |
| `2026-06-24 14:18:16` | `cowrie.command.input` |
| `2026-06-24 14:18:16` | `cowrie.log.closed` |
| `2026-06-24 14:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba41d3f271d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:19 |
| **Last Seen** | 2026-06-24 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:19:01` | `cowrie.session.connect` |
| `2026-06-24 14:19:01` | `cowrie.client.version` |
| `2026-06-24 14:19:01` | `cowrie.client.kex` |
| `2026-06-24 14:19:01` | `cowrie.login.success` |
| `2026-06-24 14:19:02` | `cowrie.session.params` |
| `2026-06-24 14:19:02` | `cowrie.command.input` |
| `2026-06-24 14:19:02` | `cowrie.log.closed` |
| `2026-06-24 14:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-240743ba53e2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:19 |
| **Last Seen** | 2026-06-24 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:19:49` | `cowrie.session.connect` |
| `2026-06-24 14:19:49` | `cowrie.client.version` |
| `2026-06-24 14:19:50` | `cowrie.client.kex` |
| `2026-06-24 14:19:50` | `cowrie.login.success` |
| `2026-06-24 14:19:51` | `cowrie.session.params` |
| `2026-06-24 14:19:51` | `cowrie.command.input` |
| `2026-06-24 14:19:51` | `cowrie.log.closed` |
| `2026-06-24 14:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad00e17eb30

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:20 |
| **Last Seen** | 2026-06-24 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:20:38` | `cowrie.session.connect` |
| `2026-06-24 14:20:38` | `cowrie.client.version` |
| `2026-06-24 14:20:38` | `cowrie.client.kex` |
| `2026-06-24 14:20:39` | `cowrie.login.success` |
| `2026-06-24 14:20:40` | `cowrie.session.params` |
| `2026-06-24 14:20:40` | `cowrie.command.input` |
| `2026-06-24 14:20:40` | `cowrie.log.closed` |
| `2026-06-24 14:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18d79d608a6c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:21 |
| **Last Seen** | 2026-06-24 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:21:28` | `cowrie.session.connect` |
| `2026-06-24 14:21:28` | `cowrie.client.version` |
| `2026-06-24 14:21:29` | `cowrie.client.kex` |
| `2026-06-24 14:21:29` | `cowrie.login.success` |
| `2026-06-24 14:21:29` | `cowrie.session.params` |
| `2026-06-24 14:21:29` | `cowrie.command.input` |
| `2026-06-24 14:21:30` | `cowrie.log.closed` |
| `2026-06-24 14:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff89abb661f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:22 |
| **Last Seen** | 2026-06-24 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:22:18` | `cowrie.session.connect` |
| `2026-06-24 14:22:18` | `cowrie.client.version` |
| `2026-06-24 14:22:18` | `cowrie.client.kex` |
| `2026-06-24 14:22:19` | `cowrie.login.success` |
| `2026-06-24 14:22:20` | `cowrie.session.params` |
| `2026-06-24 14:22:20` | `cowrie.command.input` |
| `2026-06-24 14:22:20` | `cowrie.log.closed` |
| `2026-06-24 14:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47aa6daacbae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:23 |
| **Last Seen** | 2026-06-24 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:23:10` | `cowrie.session.connect` |
| `2026-06-24 14:23:10` | `cowrie.client.version` |
| `2026-06-24 14:23:10` | `cowrie.client.kex` |
| `2026-06-24 14:23:10` | `cowrie.login.success` |
| `2026-06-24 14:23:11` | `cowrie.session.params` |
| `2026-06-24 14:23:11` | `cowrie.command.input` |
| `2026-06-24 14:23:11` | `cowrie.log.closed` |
| `2026-06-24 14:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf815605d2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:23 |
| **Last Seen** | 2026-06-24 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:23:59` | `cowrie.session.connect` |
| `2026-06-24 14:23:59` | `cowrie.client.version` |
| `2026-06-24 14:24:00` | `cowrie.client.kex` |
| `2026-06-24 14:24:00` | `cowrie.login.success` |
| `2026-06-24 14:24:01` | `cowrie.session.params` |
| `2026-06-24 14:24:01` | `cowrie.command.input` |
| `2026-06-24 14:24:01` | `cowrie.log.closed` |
| `2026-06-24 14:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3efdaa61dc43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:24 |
| **Last Seen** | 2026-06-24 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:24:49` | `cowrie.session.connect` |
| `2026-06-24 14:24:49` | `cowrie.client.version` |
| `2026-06-24 14:24:49` | `cowrie.client.kex` |
| `2026-06-24 14:24:49` | `cowrie.login.success` |
| `2026-06-24 14:24:50` | `cowrie.session.params` |
| `2026-06-24 14:24:50` | `cowrie.command.input` |
| `2026-06-24 14:24:50` | `cowrie.log.closed` |
| `2026-06-24 14:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6843a4b4ee94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:25 |
| **Last Seen** | 2026-06-24 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:25:40` | `cowrie.session.connect` |
| `2026-06-24 14:25:40` | `cowrie.client.version` |
| `2026-06-24 14:25:40` | `cowrie.client.kex` |
| `2026-06-24 14:25:40` | `cowrie.login.success` |
| `2026-06-24 14:25:41` | `cowrie.session.params` |
| `2026-06-24 14:25:41` | `cowrie.command.input` |
| `2026-06-24 14:25:41` | `cowrie.log.closed` |
| `2026-06-24 14:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8f7803dd21

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:26 |
| **Last Seen** | 2026-06-24 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:26:29` | `cowrie.session.connect` |
| `2026-06-24 14:26:29` | `cowrie.client.version` |
| `2026-06-24 14:26:29` | `cowrie.client.kex` |
| `2026-06-24 14:26:29` | `cowrie.login.success` |
| `2026-06-24 14:26:30` | `cowrie.session.params` |
| `2026-06-24 14:26:30` | `cowrie.command.input` |
| `2026-06-24 14:26:30` | `cowrie.log.closed` |
| `2026-06-24 14:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c960ea2f8933

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:27 |
| **Last Seen** | 2026-06-24 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:27:18` | `cowrie.session.connect` |
| `2026-06-24 14:27:18` | `cowrie.client.version` |
| `2026-06-24 14:27:18` | `cowrie.client.kex` |
| `2026-06-24 14:27:18` | `cowrie.login.success` |
| `2026-06-24 14:27:19` | `cowrie.session.params` |
| `2026-06-24 14:27:19` | `cowrie.command.input` |
| `2026-06-24 14:27:19` | `cowrie.log.closed` |
| `2026-06-24 14:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5802663837a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:28 |
| **Last Seen** | 2026-06-24 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:28:08` | `cowrie.session.connect` |
| `2026-06-24 14:28:08` | `cowrie.client.version` |
| `2026-06-24 14:28:08` | `cowrie.client.kex` |
| `2026-06-24 14:28:08` | `cowrie.login.success` |
| `2026-06-24 14:28:09` | `cowrie.session.params` |
| `2026-06-24 14:28:09` | `cowrie.command.input` |
| `2026-06-24 14:28:09` | `cowrie.log.closed` |
| `2026-06-24 14:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc00b6178e7a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 14:28 |
| **Last Seen** | 2026-06-24 14:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:28:41` | `cowrie.session.connect` |
| `2026-06-24 14:28:42` | `cowrie.client.version` |
| `2026-06-24 14:28:42` | `cowrie.client.kex` |
| `2026-06-24 14:28:48` | `cowrie.login.success` |
| `2026-06-24 14:28:53` | `cowrie.session.params` |
| `2026-06-24 14:28:53` | `cowrie.command.input` |
| `2026-06-24 14:28:54` | `cowrie.log.closed` |
| `2026-06-24 14:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa515d794fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:28 |
| **Last Seen** | 2026-06-24 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:28:58` | `cowrie.session.connect` |
| `2026-06-24 14:28:58` | `cowrie.client.version` |
| `2026-06-24 14:28:58` | `cowrie.client.kex` |
| `2026-06-24 14:28:58` | `cowrie.login.success` |
| `2026-06-24 14:28:59` | `cowrie.session.params` |
| `2026-06-24 14:28:59` | `cowrie.command.input` |
| `2026-06-24 14:28:59` | `cowrie.log.closed` |
| `2026-06-24 14:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21048f15d5fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:29 |
| **Last Seen** | 2026-06-24 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:29:47` | `cowrie.session.connect` |
| `2026-06-24 14:29:47` | `cowrie.client.version` |
| `2026-06-24 14:29:47` | `cowrie.client.kex` |
| `2026-06-24 14:29:48` | `cowrie.login.success` |
| `2026-06-24 14:29:49` | `cowrie.session.params` |
| `2026-06-24 14:29:49` | `cowrie.command.input` |
| `2026-06-24 14:29:49` | `cowrie.log.closed` |
| `2026-06-24 14:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d09e08cf1c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:30 |
| **Last Seen** | 2026-06-24 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:30:37` | `cowrie.session.connect` |
| `2026-06-24 14:30:37` | `cowrie.client.version` |
| `2026-06-24 14:30:37` | `cowrie.client.kex` |
| `2026-06-24 14:30:37` | `cowrie.login.success` |
| `2026-06-24 14:30:38` | `cowrie.session.params` |
| `2026-06-24 14:30:38` | `cowrie.command.input` |
| `2026-06-24 14:30:38` | `cowrie.log.closed` |
| `2026-06-24 14:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cba21aa3f7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:31 |
| **Last Seen** | 2026-06-24 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:31:29` | `cowrie.session.connect` |
| `2026-06-24 14:31:29` | `cowrie.client.version` |
| `2026-06-24 14:31:29` | `cowrie.client.kex` |
| `2026-06-24 14:31:29` | `cowrie.login.success` |
| `2026-06-24 14:31:30` | `cowrie.session.params` |
| `2026-06-24 14:31:30` | `cowrie.command.input` |
| `2026-06-24 14:31:30` | `cowrie.log.closed` |
| `2026-06-24 14:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a8923542c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:32 |
| **Last Seen** | 2026-06-24 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:32:18` | `cowrie.session.connect` |
| `2026-06-24 14:32:18` | `cowrie.client.version` |
| `2026-06-24 14:32:18` | `cowrie.client.kex` |
| `2026-06-24 14:32:18` | `cowrie.login.success` |
| `2026-06-24 14:32:19` | `cowrie.session.params` |
| `2026-06-24 14:32:19` | `cowrie.command.input` |
| `2026-06-24 14:32:19` | `cowrie.log.closed` |
| `2026-06-24 14:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc134075e1df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:33 |
| **Last Seen** | 2026-06-24 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:33:09` | `cowrie.session.connect` |
| `2026-06-24 14:33:09` | `cowrie.client.version` |
| `2026-06-24 14:33:09` | `cowrie.client.kex` |
| `2026-06-24 14:33:09` | `cowrie.login.success` |
| `2026-06-24 14:33:10` | `cowrie.session.params` |
| `2026-06-24 14:33:10` | `cowrie.command.input` |
| `2026-06-24 14:33:10` | `cowrie.log.closed` |
| `2026-06-24 14:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b6a833ad72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:34 |
| **Last Seen** | 2026-06-24 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:34:01` | `cowrie.session.connect` |
| `2026-06-24 14:34:01` | `cowrie.client.version` |
| `2026-06-24 14:34:01` | `cowrie.client.kex` |
| `2026-06-24 14:34:02` | `cowrie.login.success` |
| `2026-06-24 14:34:02` | `cowrie.session.params` |
| `2026-06-24 14:34:02` | `cowrie.command.input` |
| `2026-06-24 14:34:02` | `cowrie.log.closed` |
| `2026-06-24 14:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3146fef37acc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:34 |
| **Last Seen** | 2026-06-24 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:34:54` | `cowrie.session.connect` |
| `2026-06-24 14:34:54` | `cowrie.client.version` |
| `2026-06-24 14:34:54` | `cowrie.client.kex` |
| `2026-06-24 14:34:55` | `cowrie.login.success` |
| `2026-06-24 14:34:55` | `cowrie.session.params` |
| `2026-06-24 14:34:55` | `cowrie.command.input` |
| `2026-06-24 14:34:56` | `cowrie.log.closed` |
| `2026-06-24 14:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1344b69c49

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:35 |
| **Last Seen** | 2026-06-24 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:35:46` | `cowrie.session.connect` |
| `2026-06-24 14:35:46` | `cowrie.client.version` |
| `2026-06-24 14:35:46` | `cowrie.client.kex` |
| `2026-06-24 14:35:46` | `cowrie.login.success` |
| `2026-06-24 14:35:47` | `cowrie.session.params` |
| `2026-06-24 14:35:47` | `cowrie.command.input` |
| `2026-06-24 14:35:47` | `cowrie.log.closed` |
| `2026-06-24 14:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8b4d2c58c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:36 |
| **Last Seen** | 2026-06-24 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:36:38` | `cowrie.session.connect` |
| `2026-06-24 14:36:38` | `cowrie.client.version` |
| `2026-06-24 14:36:38` | `cowrie.client.kex` |
| `2026-06-24 14:36:38` | `cowrie.login.success` |
| `2026-06-24 14:36:39` | `cowrie.session.params` |
| `2026-06-24 14:36:39` | `cowrie.command.input` |
| `2026-06-24 14:36:39` | `cowrie.log.closed` |
| `2026-06-24 14:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b4bb604888

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:37 |
| **Last Seen** | 2026-06-24 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:37:27` | `cowrie.session.connect` |
| `2026-06-24 14:37:27` | `cowrie.client.version` |
| `2026-06-24 14:37:28` | `cowrie.client.kex` |
| `2026-06-24 14:37:28` | `cowrie.login.success` |
| `2026-06-24 14:37:29` | `cowrie.session.params` |
| `2026-06-24 14:37:29` | `cowrie.command.input` |
| `2026-06-24 14:37:29` | `cowrie.log.closed` |
| `2026-06-24 14:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16846af842b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:38 |
| **Last Seen** | 2026-06-24 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:38:19` | `cowrie.session.connect` |
| `2026-06-24 14:38:19` | `cowrie.client.version` |
| `2026-06-24 14:38:19` | `cowrie.client.kex` |
| `2026-06-24 14:38:19` | `cowrie.login.success` |
| `2026-06-24 14:38:20` | `cowrie.session.params` |
| `2026-06-24 14:38:20` | `cowrie.command.input` |
| `2026-06-24 14:38:20` | `cowrie.log.closed` |
| `2026-06-24 14:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d348d6e26c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:39 |
| **Last Seen** | 2026-06-24 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:39:11` | `cowrie.session.connect` |
| `2026-06-24 14:39:11` | `cowrie.client.version` |
| `2026-06-24 14:39:11` | `cowrie.client.kex` |
| `2026-06-24 14:39:11` | `cowrie.login.success` |
| `2026-06-24 14:39:12` | `cowrie.session.params` |
| `2026-06-24 14:39:12` | `cowrie.command.input` |
| `2026-06-24 14:39:12` | `cowrie.log.closed` |
| `2026-06-24 14:39:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0401a447589

| Field | Detail |
|---|---|
| **Source IP** | `106.12.127[.]43` |
| **First Seen** | 2026-06-24 14:39 |
| **Last Seen** | 2026-06-24 14:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:39:43` | `cowrie.session.connect` |
| `2026-06-24 14:39:43` | `cowrie.client.version` |
| `2026-06-24 14:39:45` | `cowrie.client.kex` |
| `2026-06-24 14:39:48` | `cowrie.login.success` |
| `2026-06-24 14:39:54` | `cowrie.session.params` |
| `2026-06-24 14:39:54` | `cowrie.command.input` |
| `2026-06-24 14:39:54` | `cowrie.log.closed` |
| `2026-06-24 14:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.127[.]43` to AbuseIPDB if not already reported
- [ ] Block `106.12.127[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62611db2e060

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:40 |
| **Last Seen** | 2026-06-24 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:40:01` | `cowrie.session.connect` |
| `2026-06-24 14:40:01` | `cowrie.client.version` |
| `2026-06-24 14:40:01` | `cowrie.client.kex` |
| `2026-06-24 14:40:02` | `cowrie.login.success` |
| `2026-06-24 14:40:02` | `cowrie.session.params` |
| `2026-06-24 14:40:02` | `cowrie.command.input` |
| `2026-06-24 14:40:02` | `cowrie.log.closed` |
| `2026-06-24 14:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba33d1488eaf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:40 |
| **Last Seen** | 2026-06-24 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:40:53` | `cowrie.session.connect` |
| `2026-06-24 14:40:53` | `cowrie.client.version` |
| `2026-06-24 14:40:53` | `cowrie.client.kex` |
| `2026-06-24 14:40:54` | `cowrie.login.success` |
| `2026-06-24 14:40:54` | `cowrie.session.params` |
| `2026-06-24 14:40:54` | `cowrie.command.input` |
| `2026-06-24 14:40:55` | `cowrie.log.closed` |
| `2026-06-24 14:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c08136debc00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:41 |
| **Last Seen** | 2026-06-24 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:41:47` | `cowrie.session.connect` |
| `2026-06-24 14:41:47` | `cowrie.client.version` |
| `2026-06-24 14:41:47` | `cowrie.client.kex` |
| `2026-06-24 14:41:47` | `cowrie.login.success` |
| `2026-06-24 14:41:48` | `cowrie.session.params` |
| `2026-06-24 14:41:48` | `cowrie.command.input` |
| `2026-06-24 14:41:48` | `cowrie.log.closed` |
| `2026-06-24 14:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b6f4e7a108

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:42 |
| **Last Seen** | 2026-06-24 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:42:37` | `cowrie.session.connect` |
| `2026-06-24 14:42:37` | `cowrie.client.version` |
| `2026-06-24 14:42:37` | `cowrie.client.kex` |
| `2026-06-24 14:42:37` | `cowrie.login.success` |
| `2026-06-24 14:42:38` | `cowrie.session.params` |
| `2026-06-24 14:42:38` | `cowrie.command.input` |
| `2026-06-24 14:42:38` | `cowrie.log.closed` |
| `2026-06-24 14:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5371fe555d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 14:42 |
| **Last Seen** | 2026-06-24 14:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:42:53` | `cowrie.session.connect` |
| `2026-06-24 14:42:55` | `cowrie.client.version` |
| `2026-06-24 14:42:55` | `cowrie.client.kex` |
| `2026-06-24 14:43:01` | `cowrie.login.success` |
| `2026-06-24 14:43:05` | `cowrie.session.params` |
| `2026-06-24 14:43:05` | `cowrie.command.input` |
| `2026-06-24 14:43:07` | `cowrie.log.closed` |
| `2026-06-24 14:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4746030a5ca4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:43 |
| **Last Seen** | 2026-06-24 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:43:27` | `cowrie.session.connect` |
| `2026-06-24 14:43:27` | `cowrie.client.version` |
| `2026-06-24 14:43:27` | `cowrie.client.kex` |
| `2026-06-24 14:43:27` | `cowrie.login.success` |
| `2026-06-24 14:43:28` | `cowrie.session.params` |
| `2026-06-24 14:43:28` | `cowrie.command.input` |
| `2026-06-24 14:43:28` | `cowrie.log.closed` |
| `2026-06-24 14:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fb97260960

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:44 |
| **Last Seen** | 2026-06-24 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:44:16` | `cowrie.session.connect` |
| `2026-06-24 14:44:16` | `cowrie.client.version` |
| `2026-06-24 14:44:16` | `cowrie.client.kex` |
| `2026-06-24 14:44:16` | `cowrie.login.success` |
| `2026-06-24 14:44:17` | `cowrie.session.params` |
| `2026-06-24 14:44:17` | `cowrie.command.input` |
| `2026-06-24 14:44:17` | `cowrie.log.closed` |
| `2026-06-24 14:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01534a5f1f7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:45 |
| **Last Seen** | 2026-06-24 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:45:07` | `cowrie.session.connect` |
| `2026-06-24 14:45:07` | `cowrie.client.version` |
| `2026-06-24 14:45:07` | `cowrie.client.kex` |
| `2026-06-24 14:45:07` | `cowrie.login.success` |
| `2026-06-24 14:45:08` | `cowrie.session.params` |
| `2026-06-24 14:45:08` | `cowrie.command.input` |
| `2026-06-24 14:45:08` | `cowrie.log.closed` |
| `2026-06-24 14:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d689d9b346

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:45 |
| **Last Seen** | 2026-06-24 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:45:59` | `cowrie.session.connect` |
| `2026-06-24 14:45:59` | `cowrie.client.version` |
| `2026-06-24 14:45:59` | `cowrie.client.kex` |
| `2026-06-24 14:45:59` | `cowrie.login.success` |
| `2026-06-24 14:46:00` | `cowrie.session.params` |
| `2026-06-24 14:46:00` | `cowrie.command.input` |
| `2026-06-24 14:46:00` | `cowrie.log.closed` |
| `2026-06-24 14:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7e6471e853

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:46 |
| **Last Seen** | 2026-06-24 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:46:51` | `cowrie.session.connect` |
| `2026-06-24 14:46:51` | `cowrie.client.version` |
| `2026-06-24 14:46:51` | `cowrie.client.kex` |
| `2026-06-24 14:46:51` | `cowrie.login.success` |
| `2026-06-24 14:46:52` | `cowrie.session.params` |
| `2026-06-24 14:46:52` | `cowrie.command.input` |
| `2026-06-24 14:46:52` | `cowrie.log.closed` |
| `2026-06-24 14:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5bf563d9b6b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:47 |
| **Last Seen** | 2026-06-24 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:47:44` | `cowrie.session.connect` |
| `2026-06-24 14:47:44` | `cowrie.client.version` |
| `2026-06-24 14:47:44` | `cowrie.client.kex` |
| `2026-06-24 14:47:44` | `cowrie.login.success` |
| `2026-06-24 14:47:45` | `cowrie.session.params` |
| `2026-06-24 14:47:45` | `cowrie.command.input` |
| `2026-06-24 14:47:45` | `cowrie.log.closed` |
| `2026-06-24 14:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7520a7b7e1aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:48 |
| **Last Seen** | 2026-06-24 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:48:38` | `cowrie.session.connect` |
| `2026-06-24 14:48:38` | `cowrie.client.version` |
| `2026-06-24 14:48:38` | `cowrie.client.kex` |
| `2026-06-24 14:48:38` | `cowrie.login.success` |
| `2026-06-24 14:48:39` | `cowrie.session.params` |
| `2026-06-24 14:48:39` | `cowrie.command.input` |
| `2026-06-24 14:48:39` | `cowrie.log.closed` |
| `2026-06-24 14:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6c273243f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:49 |
| **Last Seen** | 2026-06-24 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:49:29` | `cowrie.session.connect` |
| `2026-06-24 14:49:29` | `cowrie.client.version` |
| `2026-06-24 14:49:29` | `cowrie.client.kex` |
| `2026-06-24 14:49:29` | `cowrie.login.success` |
| `2026-06-24 14:49:30` | `cowrie.session.params` |
| `2026-06-24 14:49:30` | `cowrie.command.input` |
| `2026-06-24 14:49:30` | `cowrie.log.closed` |
| `2026-06-24 14:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6808afdea8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:50 |
| **Last Seen** | 2026-06-24 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:50:22` | `cowrie.session.connect` |
| `2026-06-24 14:50:22` | `cowrie.client.version` |
| `2026-06-24 14:50:22` | `cowrie.client.kex` |
| `2026-06-24 14:50:22` | `cowrie.login.success` |
| `2026-06-24 14:50:23` | `cowrie.session.params` |
| `2026-06-24 14:50:23` | `cowrie.command.input` |
| `2026-06-24 14:50:23` | `cowrie.log.closed` |
| `2026-06-24 14:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ca115d81492

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:51 |
| **Last Seen** | 2026-06-24 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:51:19` | `cowrie.session.connect` |
| `2026-06-24 14:51:19` | `cowrie.client.version` |
| `2026-06-24 14:51:19` | `cowrie.client.kex` |
| `2026-06-24 14:51:19` | `cowrie.login.success` |
| `2026-06-24 14:51:20` | `cowrie.session.params` |
| `2026-06-24 14:51:20` | `cowrie.command.input` |
| `2026-06-24 14:51:20` | `cowrie.log.closed` |
| `2026-06-24 14:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80b1131dce2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:52 |
| **Last Seen** | 2026-06-24 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:52:13` | `cowrie.session.connect` |
| `2026-06-24 14:52:13` | `cowrie.client.version` |
| `2026-06-24 14:52:13` | `cowrie.client.kex` |
| `2026-06-24 14:52:13` | `cowrie.login.success` |
| `2026-06-24 14:52:14` | `cowrie.session.params` |
| `2026-06-24 14:52:14` | `cowrie.command.input` |
| `2026-06-24 14:52:14` | `cowrie.log.closed` |
| `2026-06-24 14:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f3c4e697db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:53 |
| **Last Seen** | 2026-06-24 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:53:05` | `cowrie.session.connect` |
| `2026-06-24 14:53:05` | `cowrie.client.version` |
| `2026-06-24 14:53:05` | `cowrie.client.kex` |
| `2026-06-24 14:53:05` | `cowrie.login.success` |
| `2026-06-24 14:53:06` | `cowrie.session.params` |
| `2026-06-24 14:53:06` | `cowrie.command.input` |
| `2026-06-24 14:53:06` | `cowrie.log.closed` |
| `2026-06-24 14:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33889f305992

| Field | Detail |
|---|---|
| **Source IP** | `184.105.139[.]70` |
| **First Seen** | 2026-06-24 14:53 |
| **Last Seen** | 2026-06-24 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:53:48` | `cowrie.session.connect` |
| `2026-06-24 14:53:48` | `cowrie.login.success` |
| `2026-06-24 14:53:49` | `cowrie.session.params` |
| `2026-06-24 14:53:49` | `cowrie.command.input` |
| `2026-06-24 14:53:49` | `cowrie.command.input` |
| `2026-06-24 14:53:49` | `cowrie.command.failed` |
| `2026-06-24 14:53:49` | `cowrie.command.input` |
| `2026-06-24 14:53:49` | `cowrie.command.failed` |
| `2026-06-24 14:53:49` | `cowrie.command.input` |
| `2026-06-24 14:53:49` | `cowrie.log.closed` |
| `2026-06-24 14:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.105.139[.]70` to AbuseIPDB if not already reported
- [ ] Block `184.105.139[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b0a9cc51d5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:53 |
| **Last Seen** | 2026-06-24 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:53:58` | `cowrie.session.connect` |
| `2026-06-24 14:53:58` | `cowrie.client.version` |
| `2026-06-24 14:53:58` | `cowrie.client.kex` |
| `2026-06-24 14:53:59` | `cowrie.login.success` |
| `2026-06-24 14:53:59` | `cowrie.session.params` |
| `2026-06-24 14:53:59` | `cowrie.command.input` |
| `2026-06-24 14:54:00` | `cowrie.log.closed` |
| `2026-06-24 14:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506e6f9de331

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:54 |
| **Last Seen** | 2026-06-24 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:54:52` | `cowrie.session.connect` |
| `2026-06-24 14:54:52` | `cowrie.client.version` |
| `2026-06-24 14:54:52` | `cowrie.client.kex` |
| `2026-06-24 14:54:52` | `cowrie.login.success` |
| `2026-06-24 14:54:53` | `cowrie.session.params` |
| `2026-06-24 14:54:53` | `cowrie.command.input` |
| `2026-06-24 14:54:53` | `cowrie.log.closed` |
| `2026-06-24 14:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c15537c4b8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:55 |
| **Last Seen** | 2026-06-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:55:47` | `cowrie.session.connect` |
| `2026-06-24 14:55:47` | `cowrie.client.version` |
| `2026-06-24 14:55:48` | `cowrie.client.kex` |
| `2026-06-24 14:55:48` | `cowrie.login.success` |
| `2026-06-24 14:55:49` | `cowrie.session.params` |
| `2026-06-24 14:55:49` | `cowrie.command.input` |
| `2026-06-24 14:55:49` | `cowrie.log.closed` |
| `2026-06-24 14:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09dc615104b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:56 |
| **Last Seen** | 2026-06-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:56:43` | `cowrie.session.connect` |
| `2026-06-24 14:56:43` | `cowrie.client.version` |
| `2026-06-24 14:56:43` | `cowrie.client.kex` |
| `2026-06-24 14:56:44` | `cowrie.login.success` |
| `2026-06-24 14:56:44` | `cowrie.session.params` |
| `2026-06-24 14:56:44` | `cowrie.command.input` |
| `2026-06-24 14:56:45` | `cowrie.log.closed` |
| `2026-06-24 14:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf70e9c6f909

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 14:57 |
| **Last Seen** | 2026-06-24 14:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:57:07` | `cowrie.session.connect` |
| `2026-06-24 14:57:08` | `cowrie.client.version` |
| `2026-06-24 14:57:08` | `cowrie.client.kex` |
| `2026-06-24 14:57:14` | `cowrie.login.success` |
| `2026-06-24 14:57:18` | `cowrie.session.params` |
| `2026-06-24 14:57:18` | `cowrie.command.input` |
| `2026-06-24 14:57:19` | `cowrie.log.closed` |
| `2026-06-24 14:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ece2b73f11dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:57 |
| **Last Seen** | 2026-06-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:57:37` | `cowrie.session.connect` |
| `2026-06-24 14:57:37` | `cowrie.client.version` |
| `2026-06-24 14:57:37` | `cowrie.client.kex` |
| `2026-06-24 14:57:37` | `cowrie.login.success` |
| `2026-06-24 14:57:38` | `cowrie.session.params` |
| `2026-06-24 14:57:38` | `cowrie.command.input` |
| `2026-06-24 14:57:38` | `cowrie.log.closed` |
| `2026-06-24 14:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b921a6318e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:58 |
| **Last Seen** | 2026-06-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:58:30` | `cowrie.session.connect` |
| `2026-06-24 14:58:30` | `cowrie.client.version` |
| `2026-06-24 14:58:30` | `cowrie.client.kex` |
| `2026-06-24 14:58:31` | `cowrie.login.success` |
| `2026-06-24 14:58:31` | `cowrie.session.params` |
| `2026-06-24 14:58:31` | `cowrie.command.input` |
| `2026-06-24 14:58:31` | `cowrie.log.closed` |
| `2026-06-24 14:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e846485294f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 14:59 |
| **Last Seen** | 2026-06-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 14:59:25` | `cowrie.session.connect` |
| `2026-06-24 14:59:25` | `cowrie.client.version` |
| `2026-06-24 14:59:25` | `cowrie.client.kex` |
| `2026-06-24 14:59:26` | `cowrie.login.success` |
| `2026-06-24 14:59:27` | `cowrie.session.params` |
| `2026-06-24 14:59:27` | `cowrie.command.input` |
| `2026-06-24 14:59:27` | `cowrie.log.closed` |
| `2026-06-24 14:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adbbeea88339

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:00 |
| **Last Seen** | 2026-06-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:00:25` | `cowrie.session.connect` |
| `2026-06-24 15:00:25` | `cowrie.client.version` |
| `2026-06-24 15:00:25` | `cowrie.client.kex` |
| `2026-06-24 15:00:26` | `cowrie.login.success` |
| `2026-06-24 15:00:27` | `cowrie.session.params` |
| `2026-06-24 15:00:27` | `cowrie.command.input` |
| `2026-06-24 15:00:27` | `cowrie.log.closed` |
| `2026-06-24 15:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-234b00158845

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:01 |
| **Last Seen** | 2026-06-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:01:24` | `cowrie.session.connect` |
| `2026-06-24 15:01:24` | `cowrie.client.version` |
| `2026-06-24 15:01:24` | `cowrie.client.kex` |
| `2026-06-24 15:01:24` | `cowrie.login.success` |
| `2026-06-24 15:01:25` | `cowrie.session.params` |
| `2026-06-24 15:01:25` | `cowrie.command.input` |
| `2026-06-24 15:01:25` | `cowrie.log.closed` |
| `2026-06-24 15:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53bfd1cf2bfc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:02 |
| **Last Seen** | 2026-06-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:02:17` | `cowrie.session.connect` |
| `2026-06-24 15:02:17` | `cowrie.client.version` |
| `2026-06-24 15:02:17` | `cowrie.client.kex` |
| `2026-06-24 15:02:17` | `cowrie.login.success` |
| `2026-06-24 15:02:18` | `cowrie.session.params` |
| `2026-06-24 15:02:18` | `cowrie.command.input` |
| `2026-06-24 15:02:18` | `cowrie.log.closed` |
| `2026-06-24 15:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48ac90213e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:03 |
| **Last Seen** | 2026-06-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:03:09` | `cowrie.session.connect` |
| `2026-06-24 15:03:09` | `cowrie.client.version` |
| `2026-06-24 15:03:09` | `cowrie.client.kex` |
| `2026-06-24 15:03:09` | `cowrie.login.success` |
| `2026-06-24 15:03:10` | `cowrie.session.params` |
| `2026-06-24 15:03:10` | `cowrie.command.input` |
| `2026-06-24 15:03:10` | `cowrie.log.closed` |
| `2026-06-24 15:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a795289549

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:04 |
| **Last Seen** | 2026-06-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:04:01` | `cowrie.session.connect` |
| `2026-06-24 15:04:01` | `cowrie.client.version` |
| `2026-06-24 15:04:01` | `cowrie.client.kex` |
| `2026-06-24 15:04:01` | `cowrie.login.success` |
| `2026-06-24 15:04:02` | `cowrie.session.params` |
| `2026-06-24 15:04:02` | `cowrie.command.input` |
| `2026-06-24 15:04:02` | `cowrie.log.closed` |
| `2026-06-24 15:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b24f9e6685f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:04 |
| **Last Seen** | 2026-06-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:04:56` | `cowrie.session.connect` |
| `2026-06-24 15:04:56` | `cowrie.client.version` |
| `2026-06-24 15:04:56` | `cowrie.client.kex` |
| `2026-06-24 15:04:56` | `cowrie.login.success` |
| `2026-06-24 15:04:57` | `cowrie.session.params` |
| `2026-06-24 15:04:57` | `cowrie.command.input` |
| `2026-06-24 15:04:57` | `cowrie.log.closed` |
| `2026-06-24 15:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b7e897e063e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:05 |
| **Last Seen** | 2026-06-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:05:54` | `cowrie.session.connect` |
| `2026-06-24 15:05:54` | `cowrie.client.version` |
| `2026-06-24 15:05:54` | `cowrie.client.kex` |
| `2026-06-24 15:05:54` | `cowrie.login.success` |
| `2026-06-24 15:05:55` | `cowrie.session.params` |
| `2026-06-24 15:05:55` | `cowrie.command.input` |
| `2026-06-24 15:05:55` | `cowrie.log.closed` |
| `2026-06-24 15:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbc3693c39e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:06 |
| **Last Seen** | 2026-06-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:06:51` | `cowrie.session.connect` |
| `2026-06-24 15:06:51` | `cowrie.client.version` |
| `2026-06-24 15:06:51` | `cowrie.client.kex` |
| `2026-06-24 15:06:51` | `cowrie.login.success` |
| `2026-06-24 15:06:52` | `cowrie.session.params` |
| `2026-06-24 15:06:52` | `cowrie.command.input` |
| `2026-06-24 15:06:52` | `cowrie.log.closed` |
| `2026-06-24 15:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6bb3cc17926

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:07 |
| **Last Seen** | 2026-06-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:07:49` | `cowrie.session.connect` |
| `2026-06-24 15:07:49` | `cowrie.client.version` |
| `2026-06-24 15:07:49` | `cowrie.client.kex` |
| `2026-06-24 15:07:49` | `cowrie.login.success` |
| `2026-06-24 15:07:50` | `cowrie.session.params` |
| `2026-06-24 15:07:50` | `cowrie.command.input` |
| `2026-06-24 15:07:50` | `cowrie.log.closed` |
| `2026-06-24 15:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b089ae3beabe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:08 |
| **Last Seen** | 2026-06-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:08:46` | `cowrie.session.connect` |
| `2026-06-24 15:08:46` | `cowrie.client.version` |
| `2026-06-24 15:08:46` | `cowrie.client.kex` |
| `2026-06-24 15:08:47` | `cowrie.login.success` |
| `2026-06-24 15:08:47` | `cowrie.session.params` |
| `2026-06-24 15:08:47` | `cowrie.command.input` |
| `2026-06-24 15:08:48` | `cowrie.log.closed` |
| `2026-06-24 15:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db13b0a3d3f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:09 |
| **Last Seen** | 2026-06-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:09:40` | `cowrie.session.connect` |
| `2026-06-24 15:09:40` | `cowrie.client.version` |
| `2026-06-24 15:09:40` | `cowrie.client.kex` |
| `2026-06-24 15:09:40` | `cowrie.login.success` |
| `2026-06-24 15:09:41` | `cowrie.session.params` |
| `2026-06-24 15:09:41` | `cowrie.command.input` |
| `2026-06-24 15:09:41` | `cowrie.log.closed` |
| `2026-06-24 15:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a18b5cbb33d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:10 |
| **Last Seen** | 2026-06-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:10:36` | `cowrie.session.connect` |
| `2026-06-24 15:10:36` | `cowrie.client.version` |
| `2026-06-24 15:10:36` | `cowrie.client.kex` |
| `2026-06-24 15:10:37` | `cowrie.login.success` |
| `2026-06-24 15:10:38` | `cowrie.session.params` |
| `2026-06-24 15:10:38` | `cowrie.command.input` |
| `2026-06-24 15:10:38` | `cowrie.log.closed` |
| `2026-06-24 15:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de99ac70e111

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 15:11 |
| **Last Seen** | 2026-06-24 15:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:11:26` | `cowrie.session.connect` |
| `2026-06-24 15:11:28` | `cowrie.client.version` |
| `2026-06-24 15:11:28` | `cowrie.client.kex` |
| `2026-06-24 15:11:34` | `cowrie.login.success` |
| `2026-06-24 15:11:38` | `cowrie.session.params` |
| `2026-06-24 15:11:38` | `cowrie.command.input` |
| `2026-06-24 15:11:40` | `cowrie.log.closed` |
| `2026-06-24 15:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db423c574dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:11 |
| **Last Seen** | 2026-06-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:11:38` | `cowrie.session.connect` |
| `2026-06-24 15:11:38` | `cowrie.client.version` |
| `2026-06-24 15:11:38` | `cowrie.client.kex` |
| `2026-06-24 15:11:39` | `cowrie.login.success` |
| `2026-06-24 15:11:40` | `cowrie.session.params` |
| `2026-06-24 15:11:40` | `cowrie.command.input` |
| `2026-06-24 15:11:40` | `cowrie.log.closed` |
| `2026-06-24 15:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352542988025

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:12 |
| **Last Seen** | 2026-06-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:12:38` | `cowrie.session.connect` |
| `2026-06-24 15:12:38` | `cowrie.client.version` |
| `2026-06-24 15:12:38` | `cowrie.client.kex` |
| `2026-06-24 15:12:38` | `cowrie.login.success` |
| `2026-06-24 15:12:39` | `cowrie.session.params` |
| `2026-06-24 15:12:39` | `cowrie.command.input` |
| `2026-06-24 15:12:39` | `cowrie.log.closed` |
| `2026-06-24 15:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a93d0e480fb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 15:13 |
| **Last Seen** | 2026-06-24 15:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:13:01` | `cowrie.session.connect` |
| `2026-06-24 15:13:01` | `cowrie.client.version` |
| `2026-06-24 15:13:01` | `cowrie.client.kex` |
| `2026-06-24 15:13:01` | `cowrie.login.success` |
| `2026-06-24 15:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6264a94051

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 15:13 |
| **Last Seen** | 2026-06-24 15:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:13:01` | `cowrie.session.connect` |
| `2026-06-24 15:13:01` | `cowrie.client.version` |
| `2026-06-24 15:13:01` | `cowrie.client.kex` |
| `2026-06-24 15:13:01` | `cowrie.login.success` |
| `2026-06-24 15:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15072ea5ca09

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 15:13 |
| **Last Seen** | 2026-06-24 15:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:13:03` | `cowrie.session.connect` |
| `2026-06-24 15:13:03` | `cowrie.client.version` |
| `2026-06-24 15:13:03` | `cowrie.client.kex` |
| `2026-06-24 15:13:03` | `cowrie.login.success` |
| `2026-06-24 15:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525d0cf3e3b0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 15:13 |
| **Last Seen** | 2026-06-24 15:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:13:03` | `cowrie.session.connect` |
| `2026-06-24 15:13:03` | `cowrie.client.version` |
| `2026-06-24 15:13:03` | `cowrie.client.kex` |
| `2026-06-24 15:13:03` | `cowrie.login.success` |
| `2026-06-24 15:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97488c8d0d34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:13 |
| **Last Seen** | 2026-06-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:13:35` | `cowrie.session.connect` |
| `2026-06-24 15:13:35` | `cowrie.client.version` |
| `2026-06-24 15:13:35` | `cowrie.client.kex` |
| `2026-06-24 15:13:35` | `cowrie.login.success` |
| `2026-06-24 15:13:36` | `cowrie.session.params` |
| `2026-06-24 15:13:36` | `cowrie.command.input` |
| `2026-06-24 15:13:36` | `cowrie.log.closed` |
| `2026-06-24 15:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffd51b553c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:14 |
| **Last Seen** | 2026-06-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:14:30` | `cowrie.session.connect` |
| `2026-06-24 15:14:30` | `cowrie.client.version` |
| `2026-06-24 15:14:30` | `cowrie.client.kex` |
| `2026-06-24 15:14:31` | `cowrie.login.success` |
| `2026-06-24 15:14:32` | `cowrie.session.params` |
| `2026-06-24 15:14:32` | `cowrie.command.input` |
| `2026-06-24 15:14:32` | `cowrie.log.closed` |
| `2026-06-24 15:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a96774cdcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:15 |
| **Last Seen** | 2026-06-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:15:26` | `cowrie.session.connect` |
| `2026-06-24 15:15:26` | `cowrie.client.version` |
| `2026-06-24 15:15:26` | `cowrie.client.kex` |
| `2026-06-24 15:15:26` | `cowrie.login.success` |
| `2026-06-24 15:15:27` | `cowrie.session.params` |
| `2026-06-24 15:15:27` | `cowrie.command.input` |
| `2026-06-24 15:15:27` | `cowrie.log.closed` |
| `2026-06-24 15:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81986613aa42

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:16 |
| **Last Seen** | 2026-06-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:16:24` | `cowrie.session.connect` |
| `2026-06-24 15:16:24` | `cowrie.client.version` |
| `2026-06-24 15:16:24` | `cowrie.client.kex` |
| `2026-06-24 15:16:25` | `cowrie.login.success` |
| `2026-06-24 15:16:25` | `cowrie.session.params` |
| `2026-06-24 15:16:25` | `cowrie.command.input` |
| `2026-06-24 15:16:26` | `cowrie.log.closed` |
| `2026-06-24 15:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd593ba1884

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:17 |
| **Last Seen** | 2026-06-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:17:19` | `cowrie.session.connect` |
| `2026-06-24 15:17:19` | `cowrie.client.version` |
| `2026-06-24 15:17:19` | `cowrie.client.kex` |
| `2026-06-24 15:17:19` | `cowrie.login.success` |
| `2026-06-24 15:17:20` | `cowrie.session.params` |
| `2026-06-24 15:17:20` | `cowrie.command.input` |
| `2026-06-24 15:17:20` | `cowrie.log.closed` |
| `2026-06-24 15:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706f4c3526c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:18 |
| **Last Seen** | 2026-06-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:18:13` | `cowrie.session.connect` |
| `2026-06-24 15:18:13` | `cowrie.client.version` |
| `2026-06-24 15:18:13` | `cowrie.client.kex` |
| `2026-06-24 15:18:14` | `cowrie.login.success` |
| `2026-06-24 15:18:14` | `cowrie.session.params` |
| `2026-06-24 15:18:14` | `cowrie.command.input` |
| `2026-06-24 15:18:14` | `cowrie.log.closed` |
| `2026-06-24 15:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc76161edf26

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:19 |
| **Last Seen** | 2026-06-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:19:08` | `cowrie.session.connect` |
| `2026-06-24 15:19:08` | `cowrie.client.version` |
| `2026-06-24 15:19:08` | `cowrie.client.kex` |
| `2026-06-24 15:19:09` | `cowrie.login.success` |
| `2026-06-24 15:19:10` | `cowrie.session.params` |
| `2026-06-24 15:19:10` | `cowrie.command.input` |
| `2026-06-24 15:19:10` | `cowrie.log.closed` |
| `2026-06-24 15:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819edf9ce054

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:20 |
| **Last Seen** | 2026-06-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:20:06` | `cowrie.session.connect` |
| `2026-06-24 15:20:06` | `cowrie.client.version` |
| `2026-06-24 15:20:07` | `cowrie.client.kex` |
| `2026-06-24 15:20:07` | `cowrie.login.success` |
| `2026-06-24 15:20:08` | `cowrie.session.params` |
| `2026-06-24 15:20:08` | `cowrie.command.input` |
| `2026-06-24 15:20:08` | `cowrie.log.closed` |
| `2026-06-24 15:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7294e8f33aea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:21 |
| **Last Seen** | 2026-06-24 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:21:02` | `cowrie.session.connect` |
| `2026-06-24 15:21:02` | `cowrie.client.version` |
| `2026-06-24 15:21:02` | `cowrie.client.kex` |
| `2026-06-24 15:21:03` | `cowrie.login.success` |
| `2026-06-24 15:21:03` | `cowrie.session.params` |
| `2026-06-24 15:21:03` | `cowrie.command.input` |
| `2026-06-24 15:21:04` | `cowrie.log.closed` |
| `2026-06-24 15:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1fdc8481d10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:21 |
| **Last Seen** | 2026-06-24 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:21:57` | `cowrie.session.connect` |
| `2026-06-24 15:21:57` | `cowrie.client.version` |
| `2026-06-24 15:21:57` | `cowrie.client.kex` |
| `2026-06-24 15:21:57` | `cowrie.login.success` |
| `2026-06-24 15:21:58` | `cowrie.session.params` |
| `2026-06-24 15:21:58` | `cowrie.command.input` |
| `2026-06-24 15:21:58` | `cowrie.log.closed` |
| `2026-06-24 15:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc75d543e1ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:22 |
| **Last Seen** | 2026-06-24 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:22:50` | `cowrie.session.connect` |
| `2026-06-24 15:22:50` | `cowrie.client.version` |
| `2026-06-24 15:22:50` | `cowrie.client.kex` |
| `2026-06-24 15:22:50` | `cowrie.login.success` |
| `2026-06-24 15:22:51` | `cowrie.session.params` |
| `2026-06-24 15:22:51` | `cowrie.command.input` |
| `2026-06-24 15:22:51` | `cowrie.log.closed` |
| `2026-06-24 15:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aba96e65e63

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:23 |
| **Last Seen** | 2026-06-24 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:23:45` | `cowrie.session.connect` |
| `2026-06-24 15:23:45` | `cowrie.client.version` |
| `2026-06-24 15:23:45` | `cowrie.client.kex` |
| `2026-06-24 15:23:45` | `cowrie.login.success` |
| `2026-06-24 15:23:46` | `cowrie.session.params` |
| `2026-06-24 15:23:46` | `cowrie.command.input` |
| `2026-06-24 15:23:46` | `cowrie.log.closed` |
| `2026-06-24 15:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169a889e25cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:24 |
| **Last Seen** | 2026-06-24 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:24:41` | `cowrie.session.connect` |
| `2026-06-24 15:24:41` | `cowrie.client.version` |
| `2026-06-24 15:24:42` | `cowrie.client.kex` |
| `2026-06-24 15:24:42` | `cowrie.login.success` |
| `2026-06-24 15:24:43` | `cowrie.session.params` |
| `2026-06-24 15:24:43` | `cowrie.command.input` |
| `2026-06-24 15:24:43` | `cowrie.log.closed` |
| `2026-06-24 15:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2abc8a195f0b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 15:25 |
| **Last Seen** | 2026-06-24 15:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:25:30` | `cowrie.session.connect` |
| `2026-06-24 15:25:31` | `cowrie.client.version` |
| `2026-06-24 15:25:31` | `cowrie.client.kex` |
| `2026-06-24 15:25:38` | `cowrie.login.success` |
| `2026-06-24 15:25:41` | `cowrie.session.params` |
| `2026-06-24 15:25:41` | `cowrie.command.input` |
| `2026-06-24 15:25:43` | `cowrie.log.closed` |
| `2026-06-24 15:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21cdc16f9924

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:25 |
| **Last Seen** | 2026-06-24 15:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:25:39` | `cowrie.session.connect` |
| `2026-06-24 15:25:39` | `cowrie.client.version` |
| `2026-06-24 15:25:39` | `cowrie.client.kex` |
| `2026-06-24 15:25:40` | `cowrie.login.success` |
| `2026-06-24 15:25:40` | `cowrie.session.params` |
| `2026-06-24 15:25:40` | `cowrie.command.input` |
| `2026-06-24 15:25:41` | `cowrie.log.closed` |
| `2026-06-24 15:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d400c1170e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:26 |
| **Last Seen** | 2026-06-24 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:26:37` | `cowrie.session.connect` |
| `2026-06-24 15:26:37` | `cowrie.client.version` |
| `2026-06-24 15:26:37` | `cowrie.client.kex` |
| `2026-06-24 15:26:37` | `cowrie.login.success` |
| `2026-06-24 15:26:38` | `cowrie.session.params` |
| `2026-06-24 15:26:38` | `cowrie.command.input` |
| `2026-06-24 15:26:38` | `cowrie.log.closed` |
| `2026-06-24 15:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6e93b0280b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:27 |
| **Last Seen** | 2026-06-24 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:27:35` | `cowrie.session.connect` |
| `2026-06-24 15:27:35` | `cowrie.client.version` |
| `2026-06-24 15:27:36` | `cowrie.client.kex` |
| `2026-06-24 15:27:36` | `cowrie.login.success` |
| `2026-06-24 15:27:37` | `cowrie.session.params` |
| `2026-06-24 15:27:37` | `cowrie.command.input` |
| `2026-06-24 15:27:37` | `cowrie.log.closed` |
| `2026-06-24 15:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143ecb18c60d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:28 |
| **Last Seen** | 2026-06-24 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:28:36` | `cowrie.session.connect` |
| `2026-06-24 15:28:36` | `cowrie.client.version` |
| `2026-06-24 15:28:36` | `cowrie.client.kex` |
| `2026-06-24 15:28:36` | `cowrie.login.success` |
| `2026-06-24 15:28:37` | `cowrie.session.params` |
| `2026-06-24 15:28:37` | `cowrie.command.input` |
| `2026-06-24 15:28:37` | `cowrie.log.closed` |
| `2026-06-24 15:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da7efc6b3202

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:29 |
| **Last Seen** | 2026-06-24 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:29:33` | `cowrie.session.connect` |
| `2026-06-24 15:29:33` | `cowrie.client.version` |
| `2026-06-24 15:29:33` | `cowrie.client.kex` |
| `2026-06-24 15:29:33` | `cowrie.login.success` |
| `2026-06-24 15:29:34` | `cowrie.session.params` |
| `2026-06-24 15:29:34` | `cowrie.command.input` |
| `2026-06-24 15:29:34` | `cowrie.log.closed` |
| `2026-06-24 15:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ddc56eaf46e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:30 |
| **Last Seen** | 2026-06-24 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:30:29` | `cowrie.session.connect` |
| `2026-06-24 15:30:29` | `cowrie.client.version` |
| `2026-06-24 15:30:29` | `cowrie.client.kex` |
| `2026-06-24 15:30:30` | `cowrie.login.success` |
| `2026-06-24 15:30:31` | `cowrie.session.params` |
| `2026-06-24 15:30:31` | `cowrie.command.input` |
| `2026-06-24 15:30:31` | `cowrie.log.closed` |
| `2026-06-24 15:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc0954f35888

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:31 |
| **Last Seen** | 2026-06-24 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:31:27` | `cowrie.session.connect` |
| `2026-06-24 15:31:27` | `cowrie.client.version` |
| `2026-06-24 15:31:27` | `cowrie.client.kex` |
| `2026-06-24 15:31:27` | `cowrie.login.success` |
| `2026-06-24 15:31:28` | `cowrie.session.params` |
| `2026-06-24 15:31:28` | `cowrie.command.input` |
| `2026-06-24 15:31:28` | `cowrie.log.closed` |
| `2026-06-24 15:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60bb32fc52b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:32 |
| **Last Seen** | 2026-06-24 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:32:23` | `cowrie.session.connect` |
| `2026-06-24 15:32:23` | `cowrie.client.version` |
| `2026-06-24 15:32:23` | `cowrie.client.kex` |
| `2026-06-24 15:32:24` | `cowrie.login.success` |
| `2026-06-24 15:32:24` | `cowrie.session.params` |
| `2026-06-24 15:32:24` | `cowrie.command.input` |
| `2026-06-24 15:32:25` | `cowrie.log.closed` |
| `2026-06-24 15:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0017381494

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:33 |
| **Last Seen** | 2026-06-24 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:33:20` | `cowrie.session.connect` |
| `2026-06-24 15:33:20` | `cowrie.client.version` |
| `2026-06-24 15:33:20` | `cowrie.client.kex` |
| `2026-06-24 15:33:20` | `cowrie.login.success` |
| `2026-06-24 15:33:21` | `cowrie.session.params` |
| `2026-06-24 15:33:21` | `cowrie.command.input` |
| `2026-06-24 15:33:21` | `cowrie.log.closed` |
| `2026-06-24 15:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022a2562a553

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:34 |
| **Last Seen** | 2026-06-24 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:34:14` | `cowrie.session.connect` |
| `2026-06-24 15:34:14` | `cowrie.client.version` |
| `2026-06-24 15:34:14` | `cowrie.client.kex` |
| `2026-06-24 15:34:15` | `cowrie.login.success` |
| `2026-06-24 15:34:15` | `cowrie.session.params` |
| `2026-06-24 15:34:15` | `cowrie.command.input` |
| `2026-06-24 15:34:16` | `cowrie.log.closed` |
| `2026-06-24 15:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1f410663be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:35 |
| **Last Seen** | 2026-06-24 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:35:13` | `cowrie.session.connect` |
| `2026-06-24 15:35:13` | `cowrie.client.version` |
| `2026-06-24 15:35:13` | `cowrie.client.kex` |
| `2026-06-24 15:35:13` | `cowrie.login.success` |
| `2026-06-24 15:35:14` | `cowrie.session.params` |
| `2026-06-24 15:35:14` | `cowrie.command.input` |
| `2026-06-24 15:35:14` | `cowrie.log.closed` |
| `2026-06-24 15:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d2129f3e1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:36 |
| **Last Seen** | 2026-06-24 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:36:09` | `cowrie.session.connect` |
| `2026-06-24 15:36:09` | `cowrie.client.version` |
| `2026-06-24 15:36:09` | `cowrie.client.kex` |
| `2026-06-24 15:36:10` | `cowrie.login.success` |
| `2026-06-24 15:36:10` | `cowrie.session.params` |
| `2026-06-24 15:36:10` | `cowrie.command.input` |
| `2026-06-24 15:36:11` | `cowrie.log.closed` |
| `2026-06-24 15:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b24771d52cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:37 |
| **Last Seen** | 2026-06-24 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:37:09` | `cowrie.session.connect` |
| `2026-06-24 15:37:09` | `cowrie.client.version` |
| `2026-06-24 15:37:09` | `cowrie.client.kex` |
| `2026-06-24 15:37:09` | `cowrie.login.success` |
| `2026-06-24 15:37:10` | `cowrie.session.params` |
| `2026-06-24 15:37:10` | `cowrie.command.input` |
| `2026-06-24 15:37:10` | `cowrie.log.closed` |
| `2026-06-24 15:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427b391f06e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:38 |
| **Last Seen** | 2026-06-24 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:38:10` | `cowrie.session.connect` |
| `2026-06-24 15:38:10` | `cowrie.client.version` |
| `2026-06-24 15:38:11` | `cowrie.client.kex` |
| `2026-06-24 15:38:11` | `cowrie.login.success` |
| `2026-06-24 15:38:12` | `cowrie.session.params` |
| `2026-06-24 15:38:12` | `cowrie.command.input` |
| `2026-06-24 15:38:12` | `cowrie.log.closed` |
| `2026-06-24 15:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd08da57135f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:39 |
| **Last Seen** | 2026-06-24 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:39:11` | `cowrie.session.connect` |
| `2026-06-24 15:39:11` | `cowrie.client.version` |
| `2026-06-24 15:39:11` | `cowrie.client.kex` |
| `2026-06-24 15:39:11` | `cowrie.login.success` |
| `2026-06-24 15:39:12` | `cowrie.session.params` |
| `2026-06-24 15:39:12` | `cowrie.command.input` |
| `2026-06-24 15:39:12` | `cowrie.log.closed` |
| `2026-06-24 15:39:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa9dccf8c37

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 15:39 |
| **Last Seen** | 2026-06-24 15:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:39:32` | `cowrie.session.connect` |
| `2026-06-24 15:39:33` | `cowrie.client.version` |
| `2026-06-24 15:39:33` | `cowrie.client.kex` |
| `2026-06-24 15:39:40` | `cowrie.login.success` |
| `2026-06-24 15:39:43` | `cowrie.session.params` |
| `2026-06-24 15:39:43` | `cowrie.command.input` |
| `2026-06-24 15:39:45` | `cowrie.log.closed` |
| `2026-06-24 15:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf1498f8200

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:40 |
| **Last Seen** | 2026-06-24 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:40:08` | `cowrie.session.connect` |
| `2026-06-24 15:40:08` | `cowrie.client.version` |
| `2026-06-24 15:40:09` | `cowrie.client.kex` |
| `2026-06-24 15:40:09` | `cowrie.login.success` |
| `2026-06-24 15:40:10` | `cowrie.session.params` |
| `2026-06-24 15:40:10` | `cowrie.command.input` |
| `2026-06-24 15:40:10` | `cowrie.log.closed` |
| `2026-06-24 15:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf59cba02ac3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:41 |
| **Last Seen** | 2026-06-24 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:41:05` | `cowrie.session.connect` |
| `2026-06-24 15:41:05` | `cowrie.client.version` |
| `2026-06-24 15:41:05` | `cowrie.client.kex` |
| `2026-06-24 15:41:06` | `cowrie.login.success` |
| `2026-06-24 15:41:06` | `cowrie.session.params` |
| `2026-06-24 15:41:06` | `cowrie.command.input` |
| `2026-06-24 15:41:07` | `cowrie.log.closed` |
| `2026-06-24 15:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941d02463715

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:42 |
| **Last Seen** | 2026-06-24 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:42:02` | `cowrie.session.connect` |
| `2026-06-24 15:42:02` | `cowrie.client.version` |
| `2026-06-24 15:42:02` | `cowrie.client.kex` |
| `2026-06-24 15:42:02` | `cowrie.login.success` |
| `2026-06-24 15:42:03` | `cowrie.session.params` |
| `2026-06-24 15:42:03` | `cowrie.command.input` |
| `2026-06-24 15:42:03` | `cowrie.log.closed` |
| `2026-06-24 15:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06a0cbcf3704

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:42 |
| **Last Seen** | 2026-06-24 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:42:59` | `cowrie.session.connect` |
| `2026-06-24 15:42:59` | `cowrie.client.version` |
| `2026-06-24 15:42:59` | `cowrie.client.kex` |
| `2026-06-24 15:43:00` | `cowrie.login.success` |
| `2026-06-24 15:43:00` | `cowrie.session.params` |
| `2026-06-24 15:43:00` | `cowrie.command.input` |
| `2026-06-24 15:43:01` | `cowrie.log.closed` |
| `2026-06-24 15:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ddc0779531

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:43 |
| **Last Seen** | 2026-06-24 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:43:57` | `cowrie.session.connect` |
| `2026-06-24 15:43:57` | `cowrie.client.version` |
| `2026-06-24 15:43:57` | `cowrie.client.kex` |
| `2026-06-24 15:43:58` | `cowrie.login.success` |
| `2026-06-24 15:43:59` | `cowrie.session.params` |
| `2026-06-24 15:43:59` | `cowrie.command.input` |
| `2026-06-24 15:43:59` | `cowrie.log.closed` |
| `2026-06-24 15:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd693696f045

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:44 |
| **Last Seen** | 2026-06-24 15:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:44:56` | `cowrie.session.connect` |
| `2026-06-24 15:44:56` | `cowrie.client.version` |
| `2026-06-24 15:44:56` | `cowrie.client.kex` |
| `2026-06-24 15:44:57` | `cowrie.login.success` |
| `2026-06-24 15:44:57` | `cowrie.session.params` |
| `2026-06-24 15:44:57` | `cowrie.command.input` |
| `2026-06-24 15:44:57` | `cowrie.log.closed` |
| `2026-06-24 15:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd387b9a7d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:45 |
| **Last Seen** | 2026-06-24 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:45:54` | `cowrie.session.connect` |
| `2026-06-24 15:45:54` | `cowrie.client.version` |
| `2026-06-24 15:45:55` | `cowrie.client.kex` |
| `2026-06-24 15:45:55` | `cowrie.login.success` |
| `2026-06-24 15:45:56` | `cowrie.session.params` |
| `2026-06-24 15:45:56` | `cowrie.command.input` |
| `2026-06-24 15:45:56` | `cowrie.log.closed` |
| `2026-06-24 15:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d595db89cbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:46 |
| **Last Seen** | 2026-06-24 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:46:51` | `cowrie.session.connect` |
| `2026-06-24 15:46:51` | `cowrie.client.version` |
| `2026-06-24 15:46:51` | `cowrie.client.kex` |
| `2026-06-24 15:46:52` | `cowrie.login.success` |
| `2026-06-24 15:46:53` | `cowrie.session.params` |
| `2026-06-24 15:46:53` | `cowrie.command.input` |
| `2026-06-24 15:46:53` | `cowrie.log.closed` |
| `2026-06-24 15:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d07990dc44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:47 |
| **Last Seen** | 2026-06-24 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:47:46` | `cowrie.session.connect` |
| `2026-06-24 15:47:46` | `cowrie.client.version` |
| `2026-06-24 15:47:46` | `cowrie.client.kex` |
| `2026-06-24 15:47:46` | `cowrie.login.success` |
| `2026-06-24 15:47:47` | `cowrie.session.params` |
| `2026-06-24 15:47:47` | `cowrie.command.input` |
| `2026-06-24 15:47:47` | `cowrie.log.closed` |
| `2026-06-24 15:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3b82cd6bb0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:48 |
| **Last Seen** | 2026-06-24 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:48:42` | `cowrie.session.connect` |
| `2026-06-24 15:48:42` | `cowrie.client.version` |
| `2026-06-24 15:48:42` | `cowrie.client.kex` |
| `2026-06-24 15:48:42` | `cowrie.login.success` |
| `2026-06-24 15:48:43` | `cowrie.session.params` |
| `2026-06-24 15:48:43` | `cowrie.command.input` |
| `2026-06-24 15:48:43` | `cowrie.log.closed` |
| `2026-06-24 15:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07600ff27da

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-24 15:49 |
| **Last Seen** | 2026-06-24 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:49:18` | `cowrie.session.connect` |
| `2026-06-24 15:49:18` | `cowrie.client.version` |
| `2026-06-24 15:49:19` | `cowrie.client.kex` |
| `2026-06-24 15:49:20` | `cowrie.login.success` |
| `2026-06-24 15:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd558f94da8f

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-24 15:49 |
| **Last Seen** | 2026-06-24 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:49:19` | `cowrie.session.connect` |
| `2026-06-24 15:49:19` | `cowrie.client.version` |
| `2026-06-24 15:49:19` | `cowrie.client.kex` |
| `2026-06-24 15:49:20` | `cowrie.login.success` |
| `2026-06-24 15:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f71cba1ce451

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:49 |
| **Last Seen** | 2026-06-24 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:49:38` | `cowrie.session.connect` |
| `2026-06-24 15:49:38` | `cowrie.client.version` |
| `2026-06-24 15:49:38` | `cowrie.client.kex` |
| `2026-06-24 15:49:39` | `cowrie.login.success` |
| `2026-06-24 15:49:40` | `cowrie.session.params` |
| `2026-06-24 15:49:40` | `cowrie.command.input` |
| `2026-06-24 15:49:40` | `cowrie.log.closed` |
| `2026-06-24 15:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d54f6e47bdc

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-24 15:49 |
| **Last Seen** | 2026-06-24 15:51 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:49:45` | `cowrie.session.connect` |
| `2026-06-24 15:49:45` | `cowrie.client.version` |
| `2026-06-24 15:49:46` | `cowrie.client.kex` |
| `2026-06-24 15:49:47` | `cowrie.login.success` |
| `2026-06-24 15:49:49` | `cowrie.session.file_upload` |
| `2026-06-24 15:49:50` | `cowrie.session.params` |
| `2026-06-24 15:49:50` | `cowrie.command.input` |
| `2026-06-24 15:49:50` | `cowrie.command.input` |
| `2026-06-24 15:49:50` | `cowrie.command.input` |
| `2026-06-24 15:49:50` | `cowrie.command.failed` |
| `2026-06-24 15:49:50` | `cowrie.log.closed` |
| `2026-06-24 15:49:51` | `cowrie.session.params` |
| `2026-06-24 15:49:51` | `cowrie.command.input` |
| `2026-06-24 15:49:52` | `cowrie.log.closed` |
| `2026-06-24 15:49:53` | `cowrie.session.params` |
| `2026-06-24 15:49:53` | `cowrie.command.input` |
| `2026-06-24 15:49:53` | `cowrie.log.closed` |
| `2026-06-24 15:49:54` | `cowrie.session.params` |
| `2026-06-24 15:49:54` | `cowrie.command.input` |
| `2026-06-24 15:49:54` | `cowrie.command.failed` |
| `2026-06-24 15:49:54` | `cowrie.command.failed` |
| `2026-06-24 15:50:55` | `cowrie.session.params` |
| `2026-06-24 15:50:55` | `cowrie.command.input` |
| `2026-06-24 15:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b069844a462b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:50 |
| **Last Seen** | 2026-06-24 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:50:37` | `cowrie.session.connect` |
| `2026-06-24 15:50:37` | `cowrie.client.version` |
| `2026-06-24 15:50:37` | `cowrie.client.kex` |
| `2026-06-24 15:50:37` | `cowrie.login.success` |
| `2026-06-24 15:50:38` | `cowrie.session.params` |
| `2026-06-24 15:50:38` | `cowrie.command.input` |
| `2026-06-24 15:50:38` | `cowrie.log.closed` |
| `2026-06-24 15:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729173229efb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:51 |
| **Last Seen** | 2026-06-24 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:51:36` | `cowrie.session.connect` |
| `2026-06-24 15:51:36` | `cowrie.client.version` |
| `2026-06-24 15:51:36` | `cowrie.client.kex` |
| `2026-06-24 15:51:36` | `cowrie.login.success` |
| `2026-06-24 15:51:37` | `cowrie.session.params` |
| `2026-06-24 15:51:37` | `cowrie.command.input` |
| `2026-06-24 15:51:37` | `cowrie.log.closed` |
| `2026-06-24 15:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b364c92a48ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:52 |
| **Last Seen** | 2026-06-24 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:52:35` | `cowrie.session.connect` |
| `2026-06-24 15:52:35` | `cowrie.client.version` |
| `2026-06-24 15:52:35` | `cowrie.client.kex` |
| `2026-06-24 15:52:35` | `cowrie.login.success` |
| `2026-06-24 15:52:36` | `cowrie.session.params` |
| `2026-06-24 15:52:36` | `cowrie.command.input` |
| `2026-06-24 15:52:36` | `cowrie.log.closed` |
| `2026-06-24 15:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f49593980dd

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 15:53 |
| **Last Seen** | 2026-06-24 15:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:53:22` | `cowrie.session.connect` |
| `2026-06-24 15:53:24` | `cowrie.client.version` |
| `2026-06-24 15:53:24` | `cowrie.client.kex` |
| `2026-06-24 15:53:31` | `cowrie.login.success` |
| `2026-06-24 15:53:34` | `cowrie.session.params` |
| `2026-06-24 15:53:34` | `cowrie.command.input` |
| `2026-06-24 15:53:37` | `cowrie.log.closed` |
| `2026-06-24 15:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57e275a1e02

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:53 |
| **Last Seen** | 2026-06-24 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:53:31` | `cowrie.session.connect` |
| `2026-06-24 15:53:31` | `cowrie.client.version` |
| `2026-06-24 15:53:31` | `cowrie.client.kex` |
| `2026-06-24 15:53:32` | `cowrie.login.success` |
| `2026-06-24 15:53:32` | `cowrie.session.params` |
| `2026-06-24 15:53:32` | `cowrie.command.input` |
| `2026-06-24 15:53:32` | `cowrie.log.closed` |
| `2026-06-24 15:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fed543e3428

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:54 |
| **Last Seen** | 2026-06-24 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:54:26` | `cowrie.session.connect` |
| `2026-06-24 15:54:26` | `cowrie.client.version` |
| `2026-06-24 15:54:26` | `cowrie.client.kex` |
| `2026-06-24 15:54:26` | `cowrie.login.success` |
| `2026-06-24 15:54:27` | `cowrie.session.params` |
| `2026-06-24 15:54:27` | `cowrie.command.input` |
| `2026-06-24 15:54:27` | `cowrie.log.closed` |
| `2026-06-24 15:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d300d62c55

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:55 |
| **Last Seen** | 2026-06-24 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:55:20` | `cowrie.session.connect` |
| `2026-06-24 15:55:20` | `cowrie.client.version` |
| `2026-06-24 15:55:20` | `cowrie.client.kex` |
| `2026-06-24 15:55:20` | `cowrie.login.success` |
| `2026-06-24 15:55:21` | `cowrie.session.params` |
| `2026-06-24 15:55:21` | `cowrie.command.input` |
| `2026-06-24 15:55:21` | `cowrie.log.closed` |
| `2026-06-24 15:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4756f9ada40a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:56 |
| **Last Seen** | 2026-06-24 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:56:16` | `cowrie.session.connect` |
| `2026-06-24 15:56:16` | `cowrie.client.version` |
| `2026-06-24 15:56:16` | `cowrie.client.kex` |
| `2026-06-24 15:56:17` | `cowrie.login.success` |
| `2026-06-24 15:56:17` | `cowrie.session.params` |
| `2026-06-24 15:56:17` | `cowrie.command.input` |
| `2026-06-24 15:56:17` | `cowrie.log.closed` |
| `2026-06-24 15:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef8d4e30bd14

| Field | Detail |
|---|---|
| **Source IP** | `143.20.49[.]38` |
| **First Seen** | 2026-06-24 15:56 |
| **Last Seen** | 2026-06-24 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:56:55` | `cowrie.session.connect` |
| `2026-06-24 15:56:57` | `cowrie.telnet.option` |
| `2026-06-24 15:56:58` | `cowrie.telnet.option` |
| `2026-06-24 15:57:58` | `cowrie.login.success` |
| `2026-06-24 15:57:59` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `143.20.49[.]38` to AbuseIPDB if not already reported
- [ ] Block `143.20.49[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d8da02376b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:57 |
| **Last Seen** | 2026-06-24 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:57:12` | `cowrie.session.connect` |
| `2026-06-24 15:57:12` | `cowrie.client.version` |
| `2026-06-24 15:57:13` | `cowrie.client.kex` |
| `2026-06-24 15:57:13` | `cowrie.login.success` |
| `2026-06-24 15:57:14` | `cowrie.session.params` |
| `2026-06-24 15:57:14` | `cowrie.command.input` |
| `2026-06-24 15:57:14` | `cowrie.log.closed` |
| `2026-06-24 15:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a01481c444

| Field | Detail |
|---|---|
| **Source IP** | `168.144.45[.]211` |
| **First Seen** | 2026-06-24 15:58 |
| **Last Seen** | 2026-06-24 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:58:00` | `cowrie.session.connect` |
| `2026-06-24 15:58:00` | `cowrie.client.version` |
| `2026-06-24 15:58:00` | `cowrie.client.kex` |
| `2026-06-24 15:58:01` | `cowrie.login.success` |
| `2026-06-24 15:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.45[.]211` to AbuseIPDB if not already reported
- [ ] Block `168.144.45[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de490ed0bda2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-24 15:58 |
| **Last Seen** | 2026-06-24 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:58:02` | `cowrie.session.connect` |
| `2026-06-24 15:58:02` | `cowrie.client.version` |
| `2026-06-24 15:58:02` | `cowrie.client.kex` |
| `2026-06-24 15:58:02` | `cowrie.login.success` |
| `2026-06-24 15:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f45786a616

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:58 |
| **Last Seen** | 2026-06-24 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:58:10` | `cowrie.session.connect` |
| `2026-06-24 15:58:10` | `cowrie.client.version` |
| `2026-06-24 15:58:10` | `cowrie.client.kex` |
| `2026-06-24 15:58:10` | `cowrie.login.success` |
| `2026-06-24 15:58:11` | `cowrie.session.params` |
| `2026-06-24 15:58:11` | `cowrie.command.input` |
| `2026-06-24 15:58:11` | `cowrie.log.closed` |
| `2026-06-24 15:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2051b046b46

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 15:59 |
| **Last Seen** | 2026-06-24 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 15:59:06` | `cowrie.session.connect` |
| `2026-06-24 15:59:06` | `cowrie.client.version` |
| `2026-06-24 15:59:06` | `cowrie.client.kex` |
| `2026-06-24 15:59:06` | `cowrie.login.success` |
| `2026-06-24 15:59:07` | `cowrie.session.params` |
| `2026-06-24 15:59:07` | `cowrie.command.input` |
| `2026-06-24 15:59:07` | `cowrie.log.closed` |
| `2026-06-24 15:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82753cd1a37

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:00 |
| **Last Seen** | 2026-06-24 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:00:05` | `cowrie.session.connect` |
| `2026-06-24 16:00:05` | `cowrie.client.version` |
| `2026-06-24 16:00:05` | `cowrie.client.kex` |
| `2026-06-24 16:00:05` | `cowrie.login.success` |
| `2026-06-24 16:00:06` | `cowrie.session.params` |
| `2026-06-24 16:00:06` | `cowrie.command.input` |
| `2026-06-24 16:00:06` | `cowrie.log.closed` |
| `2026-06-24 16:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1e412a24c51

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]100` |
| **First Seen** | 2026-06-24 16:00 |
| **Last Seen** | 2026-06-24 16:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:00:41` | `cowrie.session.connect` |
| `2026-06-24 16:00:41` | `cowrie.login.success` |
| `2026-06-24 16:00:42` | `cowrie.session.params` |
| `2026-06-24 16:00:42` | `cowrie.command.input` |
| `2026-06-24 16:00:43` | `cowrie.command.input` |
| `2026-06-24 16:00:43` | `cowrie.command.input` |
| `2026-06-24 16:00:44` | `cowrie.command.input` |
| `2026-06-24 16:00:44` | `cowrie.command.failed` |
| `2026-06-24 16:00:45` | `cowrie.log.closed` |
| `2026-06-24 16:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]100` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eaceda7207c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:00 |
| **Last Seen** | 2026-06-24 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:00:50` | `cowrie.session.connect` |
| `2026-06-24 16:00:50` | `cowrie.client.version` |
| `2026-06-24 16:00:51` | `cowrie.client.kex` |
| `2026-06-24 16:00:51` | `cowrie.login.success` |
| `2026-06-24 16:00:52` | `cowrie.session.params` |
| `2026-06-24 16:00:52` | `cowrie.command.input` |
| `2026-06-24 16:00:52` | `cowrie.log.closed` |
| `2026-06-24 16:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2441f03f72f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:01 |
| **Last Seen** | 2026-06-24 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:01:36` | `cowrie.session.connect` |
| `2026-06-24 16:01:36` | `cowrie.client.version` |
| `2026-06-24 16:01:36` | `cowrie.client.kex` |
| `2026-06-24 16:01:36` | `cowrie.login.success` |
| `2026-06-24 16:01:37` | `cowrie.session.params` |
| `2026-06-24 16:01:37` | `cowrie.command.input` |
| `2026-06-24 16:01:37` | `cowrie.log.closed` |
| `2026-06-24 16:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d5bffb9ff9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:02 |
| **Last Seen** | 2026-06-24 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:02:20` | `cowrie.session.connect` |
| `2026-06-24 16:02:20` | `cowrie.client.version` |
| `2026-06-24 16:02:20` | `cowrie.client.kex` |
| `2026-06-24 16:02:20` | `cowrie.login.success` |
| `2026-06-24 16:02:21` | `cowrie.session.params` |
| `2026-06-24 16:02:21` | `cowrie.command.input` |
| `2026-06-24 16:02:21` | `cowrie.log.closed` |
| `2026-06-24 16:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d27031c447a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:03 |
| **Last Seen** | 2026-06-24 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:03:04` | `cowrie.session.connect` |
| `2026-06-24 16:03:04` | `cowrie.client.version` |
| `2026-06-24 16:03:04` | `cowrie.client.kex` |
| `2026-06-24 16:03:05` | `cowrie.login.success` |
| `2026-06-24 16:03:05` | `cowrie.session.params` |
| `2026-06-24 16:03:05` | `cowrie.command.input` |
| `2026-06-24 16:03:06` | `cowrie.log.closed` |
| `2026-06-24 16:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb73f12ffeaf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:03 |
| **Last Seen** | 2026-06-24 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:03:50` | `cowrie.session.connect` |
| `2026-06-24 16:03:50` | `cowrie.client.version` |
| `2026-06-24 16:03:50` | `cowrie.client.kex` |
| `2026-06-24 16:03:50` | `cowrie.login.success` |
| `2026-06-24 16:03:51` | `cowrie.session.params` |
| `2026-06-24 16:03:51` | `cowrie.command.input` |
| `2026-06-24 16:03:51` | `cowrie.log.closed` |
| `2026-06-24 16:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98fe2a2ec210

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:04 |
| **Last Seen** | 2026-06-24 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:04:36` | `cowrie.session.connect` |
| `2026-06-24 16:04:36` | `cowrie.client.version` |
| `2026-06-24 16:04:36` | `cowrie.client.kex` |
| `2026-06-24 16:04:36` | `cowrie.login.success` |
| `2026-06-24 16:04:37` | `cowrie.session.params` |
| `2026-06-24 16:04:37` | `cowrie.command.input` |
| `2026-06-24 16:04:37` | `cowrie.log.closed` |
| `2026-06-24 16:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151f98086d89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:05 |
| **Last Seen** | 2026-06-24 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:05:23` | `cowrie.session.connect` |
| `2026-06-24 16:05:23` | `cowrie.client.version` |
| `2026-06-24 16:05:23` | `cowrie.client.kex` |
| `2026-06-24 16:05:24` | `cowrie.login.success` |
| `2026-06-24 16:05:24` | `cowrie.session.params` |
| `2026-06-24 16:05:24` | `cowrie.command.input` |
| `2026-06-24 16:05:25` | `cowrie.log.closed` |
| `2026-06-24 16:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7206e8f357

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:06 |
| **Last Seen** | 2026-06-24 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:06:06` | `cowrie.session.connect` |
| `2026-06-24 16:06:06` | `cowrie.client.version` |
| `2026-06-24 16:06:06` | `cowrie.client.kex` |
| `2026-06-24 16:06:06` | `cowrie.login.success` |
| `2026-06-24 16:06:07` | `cowrie.session.params` |
| `2026-06-24 16:06:07` | `cowrie.command.input` |
| `2026-06-24 16:06:07` | `cowrie.log.closed` |
| `2026-06-24 16:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a92693c6af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:06 |
| **Last Seen** | 2026-06-24 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:06:51` | `cowrie.session.connect` |
| `2026-06-24 16:06:51` | `cowrie.client.version` |
| `2026-06-24 16:06:51` | `cowrie.client.kex` |
| `2026-06-24 16:06:51` | `cowrie.login.success` |
| `2026-06-24 16:06:52` | `cowrie.session.params` |
| `2026-06-24 16:06:52` | `cowrie.command.input` |
| `2026-06-24 16:06:52` | `cowrie.log.closed` |
| `2026-06-24 16:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3439b480c947

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 16:07 |
| **Last Seen** | 2026-06-24 16:07 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:07:31` | `cowrie.session.connect` |
| `2026-06-24 16:07:33` | `cowrie.client.version` |
| `2026-06-24 16:07:33` | `cowrie.client.kex` |
| `2026-06-24 16:07:40` | `cowrie.login.success` |
| `2026-06-24 16:07:44` | `cowrie.session.params` |
| `2026-06-24 16:07:44` | `cowrie.command.input` |
| `2026-06-24 16:07:46` | `cowrie.log.closed` |
| `2026-06-24 16:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34336e85bbd3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:07 |
| **Last Seen** | 2026-06-24 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:07:35` | `cowrie.session.connect` |
| `2026-06-24 16:07:35` | `cowrie.client.version` |
| `2026-06-24 16:07:36` | `cowrie.client.kex` |
| `2026-06-24 16:07:36` | `cowrie.login.success` |
| `2026-06-24 16:07:37` | `cowrie.session.params` |
| `2026-06-24 16:07:37` | `cowrie.command.input` |
| `2026-06-24 16:07:37` | `cowrie.log.closed` |
| `2026-06-24 16:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56857dd49fd3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:08 |
| **Last Seen** | 2026-06-24 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:08:19` | `cowrie.session.connect` |
| `2026-06-24 16:08:19` | `cowrie.client.version` |
| `2026-06-24 16:08:20` | `cowrie.client.kex` |
| `2026-06-24 16:08:20` | `cowrie.login.success` |
| `2026-06-24 16:08:21` | `cowrie.session.params` |
| `2026-06-24 16:08:21` | `cowrie.command.input` |
| `2026-06-24 16:08:21` | `cowrie.log.closed` |
| `2026-06-24 16:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3734f35dbed5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:09 |
| **Last Seen** | 2026-06-24 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:09:04` | `cowrie.session.connect` |
| `2026-06-24 16:09:04` | `cowrie.client.version` |
| `2026-06-24 16:09:04` | `cowrie.client.kex` |
| `2026-06-24 16:09:04` | `cowrie.login.success` |
| `2026-06-24 16:09:05` | `cowrie.session.params` |
| `2026-06-24 16:09:05` | `cowrie.command.input` |
| `2026-06-24 16:09:05` | `cowrie.log.closed` |
| `2026-06-24 16:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c373c0770da8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:09 |
| **Last Seen** | 2026-06-24 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:09:50` | `cowrie.session.connect` |
| `2026-06-24 16:09:50` | `cowrie.client.version` |
| `2026-06-24 16:09:50` | `cowrie.client.kex` |
| `2026-06-24 16:09:50` | `cowrie.login.success` |
| `2026-06-24 16:09:51` | `cowrie.session.params` |
| `2026-06-24 16:09:51` | `cowrie.command.input` |
| `2026-06-24 16:09:51` | `cowrie.log.closed` |
| `2026-06-24 16:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9183805f79f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:10 |
| **Last Seen** | 2026-06-24 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:10:37` | `cowrie.session.connect` |
| `2026-06-24 16:10:37` | `cowrie.client.version` |
| `2026-06-24 16:10:37` | `cowrie.client.kex` |
| `2026-06-24 16:10:37` | `cowrie.login.success` |
| `2026-06-24 16:10:38` | `cowrie.session.params` |
| `2026-06-24 16:10:38` | `cowrie.command.input` |
| `2026-06-24 16:10:38` | `cowrie.log.closed` |
| `2026-06-24 16:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ab6fac01e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:11 |
| **Last Seen** | 2026-06-24 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:11:23` | `cowrie.session.connect` |
| `2026-06-24 16:11:23` | `cowrie.client.version` |
| `2026-06-24 16:11:23` | `cowrie.client.kex` |
| `2026-06-24 16:11:23` | `cowrie.login.success` |
| `2026-06-24 16:11:24` | `cowrie.session.params` |
| `2026-06-24 16:11:24` | `cowrie.command.input` |
| `2026-06-24 16:11:24` | `cowrie.log.closed` |
| `2026-06-24 16:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abadb39a8f6d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:12 |
| **Last Seen** | 2026-06-24 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:12:10` | `cowrie.session.connect` |
| `2026-06-24 16:12:10` | `cowrie.client.version` |
| `2026-06-24 16:12:10` | `cowrie.client.kex` |
| `2026-06-24 16:12:10` | `cowrie.login.success` |
| `2026-06-24 16:12:11` | `cowrie.session.params` |
| `2026-06-24 16:12:11` | `cowrie.command.input` |
| `2026-06-24 16:12:11` | `cowrie.log.closed` |
| `2026-06-24 16:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09f78567645

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:12 |
| **Last Seen** | 2026-06-24 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:12:56` | `cowrie.session.connect` |
| `2026-06-24 16:12:56` | `cowrie.client.version` |
| `2026-06-24 16:12:56` | `cowrie.client.kex` |
| `2026-06-24 16:12:57` | `cowrie.login.success` |
| `2026-06-24 16:12:57` | `cowrie.session.params` |
| `2026-06-24 16:12:57` | `cowrie.command.input` |
| `2026-06-24 16:12:58` | `cowrie.log.closed` |
| `2026-06-24 16:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2b89f4bcfc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:13 |
| **Last Seen** | 2026-06-24 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:13:42` | `cowrie.session.connect` |
| `2026-06-24 16:13:42` | `cowrie.client.version` |
| `2026-06-24 16:13:43` | `cowrie.client.kex` |
| `2026-06-24 16:13:43` | `cowrie.login.success` |
| `2026-06-24 16:13:44` | `cowrie.session.params` |
| `2026-06-24 16:13:44` | `cowrie.command.input` |
| `2026-06-24 16:13:44` | `cowrie.log.closed` |
| `2026-06-24 16:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b360a1bc62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:14 |
| **Last Seen** | 2026-06-24 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:14:29` | `cowrie.session.connect` |
| `2026-06-24 16:14:29` | `cowrie.client.version` |
| `2026-06-24 16:14:29` | `cowrie.client.kex` |
| `2026-06-24 16:14:30` | `cowrie.login.success` |
| `2026-06-24 16:14:31` | `cowrie.session.params` |
| `2026-06-24 16:14:31` | `cowrie.command.input` |
| `2026-06-24 16:14:31` | `cowrie.log.closed` |
| `2026-06-24 16:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebe66175258

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:15 |
| **Last Seen** | 2026-06-24 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:15:18` | `cowrie.session.connect` |
| `2026-06-24 16:15:18` | `cowrie.client.version` |
| `2026-06-24 16:15:18` | `cowrie.client.kex` |
| `2026-06-24 16:15:18` | `cowrie.login.success` |
| `2026-06-24 16:15:19` | `cowrie.session.params` |
| `2026-06-24 16:15:19` | `cowrie.command.input` |
| `2026-06-24 16:15:19` | `cowrie.log.closed` |
| `2026-06-24 16:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8825cf88a60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:16 |
| **Last Seen** | 2026-06-24 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:16:07` | `cowrie.session.connect` |
| `2026-06-24 16:16:07` | `cowrie.client.version` |
| `2026-06-24 16:16:07` | `cowrie.client.kex` |
| `2026-06-24 16:16:07` | `cowrie.login.success` |
| `2026-06-24 16:16:08` | `cowrie.session.params` |
| `2026-06-24 16:16:08` | `cowrie.command.input` |
| `2026-06-24 16:16:08` | `cowrie.log.closed` |
| `2026-06-24 16:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0acf1e2c7ffa

| Field | Detail |
|---|---|
| **Source IP** | `165.232.61[.]133` |
| **First Seen** | 2026-06-24 16:16 |
| **Last Seen** | 2026-06-24 16:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:16:49` | `cowrie.session.connect` |
| `2026-06-24 16:16:49` | `cowrie.client.version` |
| `2026-06-24 16:16:49` | `cowrie.client.kex` |
| `2026-06-24 16:16:56` | `cowrie.login.success` |
| `2026-06-24 16:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.61[.]133` to AbuseIPDB if not already reported
- [ ] Block `165.232.61[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77776727bbac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:16 |
| **Last Seen** | 2026-06-24 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:16:56` | `cowrie.session.connect` |
| `2026-06-24 16:16:56` | `cowrie.client.version` |
| `2026-06-24 16:16:56` | `cowrie.client.kex` |
| `2026-06-24 16:16:57` | `cowrie.login.success` |
| `2026-06-24 16:16:58` | `cowrie.session.params` |
| `2026-06-24 16:16:58` | `cowrie.command.input` |
| `2026-06-24 16:16:58` | `cowrie.log.closed` |
| `2026-06-24 16:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90eccc861d00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:17 |
| **Last Seen** | 2026-06-24 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:17:46` | `cowrie.session.connect` |
| `2026-06-24 16:17:46` | `cowrie.client.version` |
| `2026-06-24 16:17:46` | `cowrie.client.kex` |
| `2026-06-24 16:17:46` | `cowrie.login.success` |
| `2026-06-24 16:17:47` | `cowrie.session.params` |
| `2026-06-24 16:17:47` | `cowrie.command.input` |
| `2026-06-24 16:17:47` | `cowrie.log.closed` |
| `2026-06-24 16:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6425f0b9b561

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:18 |
| **Last Seen** | 2026-06-24 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:18:34` | `cowrie.session.connect` |
| `2026-06-24 16:18:34` | `cowrie.client.version` |
| `2026-06-24 16:18:34` | `cowrie.client.kex` |
| `2026-06-24 16:18:34` | `cowrie.login.success` |
| `2026-06-24 16:18:35` | `cowrie.session.params` |
| `2026-06-24 16:18:35` | `cowrie.command.input` |
| `2026-06-24 16:18:35` | `cowrie.log.closed` |
| `2026-06-24 16:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f33020eb90f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:19 |
| **Last Seen** | 2026-06-24 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:19:20` | `cowrie.session.connect` |
| `2026-06-24 16:19:20` | `cowrie.client.version` |
| `2026-06-24 16:19:21` | `cowrie.client.kex` |
| `2026-06-24 16:19:21` | `cowrie.login.success` |
| `2026-06-24 16:19:22` | `cowrie.session.params` |
| `2026-06-24 16:19:22` | `cowrie.command.input` |
| `2026-06-24 16:19:22` | `cowrie.log.closed` |
| `2026-06-24 16:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b44bab47b0eb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-24 16:20 |
| **Last Seen** | 2026-06-24 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:20:04` | `cowrie.session.connect` |
| `2026-06-24 16:20:04` | `cowrie.client.version` |
| `2026-06-24 16:20:05` | `cowrie.client.kex` |
| `2026-06-24 16:20:05` | `cowrie.login.success` |
| `2026-06-24 16:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3db50c16df

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-24 16:20 |
| **Last Seen** | 2026-06-24 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:20:06` | `cowrie.session.connect` |
| `2026-06-24 16:20:06` | `cowrie.client.version` |
| `2026-06-24 16:20:07` | `cowrie.client.kex` |
| `2026-06-24 16:20:07` | `cowrie.login.success` |
| `2026-06-24 16:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a89e125252

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:20 |
| **Last Seen** | 2026-06-24 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:20:07` | `cowrie.session.connect` |
| `2026-06-24 16:20:07` | `cowrie.client.version` |
| `2026-06-24 16:20:07` | `cowrie.client.kex` |
| `2026-06-24 16:20:07` | `cowrie.login.success` |
| `2026-06-24 16:20:08` | `cowrie.session.params` |
| `2026-06-24 16:20:08` | `cowrie.command.input` |
| `2026-06-24 16:20:08` | `cowrie.log.closed` |
| `2026-06-24 16:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3887adfd9910

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:20 |
| **Last Seen** | 2026-06-24 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:20:56` | `cowrie.session.connect` |
| `2026-06-24 16:20:56` | `cowrie.client.version` |
| `2026-06-24 16:20:56` | `cowrie.client.kex` |
| `2026-06-24 16:20:56` | `cowrie.login.success` |
| `2026-06-24 16:20:57` | `cowrie.session.params` |
| `2026-06-24 16:20:57` | `cowrie.command.input` |
| `2026-06-24 16:20:57` | `cowrie.log.closed` |
| `2026-06-24 16:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73093bc056d3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 16:21 |
| **Last Seen** | 2026-06-24 16:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:21:44` | `cowrie.session.connect` |
| `2026-06-24 16:21:46` | `cowrie.client.version` |
| `2026-06-24 16:21:46` | `cowrie.client.kex` |
| `2026-06-24 16:21:52` | `cowrie.login.success` |
| `2026-06-24 16:21:56` | `cowrie.session.params` |
| `2026-06-24 16:21:56` | `cowrie.command.input` |
| `2026-06-24 16:21:57` | `cowrie.log.closed` |
| `2026-06-24 16:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1aa2fc2e9f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:21 |
| **Last Seen** | 2026-06-24 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:21:45` | `cowrie.session.connect` |
| `2026-06-24 16:21:45` | `cowrie.client.version` |
| `2026-06-24 16:21:46` | `cowrie.client.kex` |
| `2026-06-24 16:21:46` | `cowrie.login.success` |
| `2026-06-24 16:21:47` | `cowrie.session.params` |
| `2026-06-24 16:21:47` | `cowrie.command.input` |
| `2026-06-24 16:21:47` | `cowrie.log.closed` |
| `2026-06-24 16:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d311728eaa73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:22 |
| **Last Seen** | 2026-06-24 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:22:35` | `cowrie.session.connect` |
| `2026-06-24 16:22:35` | `cowrie.client.version` |
| `2026-06-24 16:22:35` | `cowrie.client.kex` |
| `2026-06-24 16:22:35` | `cowrie.login.success` |
| `2026-06-24 16:22:36` | `cowrie.session.params` |
| `2026-06-24 16:22:36` | `cowrie.command.input` |
| `2026-06-24 16:22:36` | `cowrie.log.closed` |
| `2026-06-24 16:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30acee9f5e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:23 |
| **Last Seen** | 2026-06-24 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:23:24` | `cowrie.session.connect` |
| `2026-06-24 16:23:24` | `cowrie.client.version` |
| `2026-06-24 16:23:24` | `cowrie.client.kex` |
| `2026-06-24 16:23:24` | `cowrie.login.success` |
| `2026-06-24 16:23:25` | `cowrie.session.params` |
| `2026-06-24 16:23:25` | `cowrie.command.input` |
| `2026-06-24 16:23:25` | `cowrie.log.closed` |
| `2026-06-24 16:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb895bd595be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:24 |
| **Last Seen** | 2026-06-24 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:24:12` | `cowrie.session.connect` |
| `2026-06-24 16:24:12` | `cowrie.client.version` |
| `2026-06-24 16:24:12` | `cowrie.client.kex` |
| `2026-06-24 16:24:13` | `cowrie.login.success` |
| `2026-06-24 16:24:14` | `cowrie.session.params` |
| `2026-06-24 16:24:14` | `cowrie.command.input` |
| `2026-06-24 16:24:14` | `cowrie.log.closed` |
| `2026-06-24 16:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6949064f9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:25 |
| **Last Seen** | 2026-06-24 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:25:00` | `cowrie.session.connect` |
| `2026-06-24 16:25:00` | `cowrie.client.version` |
| `2026-06-24 16:25:00` | `cowrie.client.kex` |
| `2026-06-24 16:25:00` | `cowrie.login.success` |
| `2026-06-24 16:25:01` | `cowrie.session.params` |
| `2026-06-24 16:25:01` | `cowrie.command.input` |
| `2026-06-24 16:25:01` | `cowrie.log.closed` |
| `2026-06-24 16:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b6f4f21249

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:25 |
| **Last Seen** | 2026-06-24 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:25:48` | `cowrie.session.connect` |
| `2026-06-24 16:25:48` | `cowrie.client.version` |
| `2026-06-24 16:25:48` | `cowrie.client.kex` |
| `2026-06-24 16:25:48` | `cowrie.login.success` |
| `2026-06-24 16:25:49` | `cowrie.session.params` |
| `2026-06-24 16:25:49` | `cowrie.command.input` |
| `2026-06-24 16:25:49` | `cowrie.log.closed` |
| `2026-06-24 16:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b08ad6224f29

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:26 |
| **Last Seen** | 2026-06-24 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:26:35` | `cowrie.session.connect` |
| `2026-06-24 16:26:35` | `cowrie.client.version` |
| `2026-06-24 16:26:35` | `cowrie.client.kex` |
| `2026-06-24 16:26:35` | `cowrie.login.success` |
| `2026-06-24 16:26:36` | `cowrie.session.params` |
| `2026-06-24 16:26:36` | `cowrie.command.input` |
| `2026-06-24 16:26:36` | `cowrie.log.closed` |
| `2026-06-24 16:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6780b6ad3fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:27 |
| **Last Seen** | 2026-06-24 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:27:23` | `cowrie.session.connect` |
| `2026-06-24 16:27:23` | `cowrie.client.version` |
| `2026-06-24 16:27:23` | `cowrie.client.kex` |
| `2026-06-24 16:27:23` | `cowrie.login.success` |
| `2026-06-24 16:27:24` | `cowrie.session.params` |
| `2026-06-24 16:27:24` | `cowrie.command.input` |
| `2026-06-24 16:27:24` | `cowrie.log.closed` |
| `2026-06-24 16:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47cf08b0c063

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:28 |
| **Last Seen** | 2026-06-24 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:28:11` | `cowrie.session.connect` |
| `2026-06-24 16:28:11` | `cowrie.client.version` |
| `2026-06-24 16:28:11` | `cowrie.client.kex` |
| `2026-06-24 16:28:12` | `cowrie.login.success` |
| `2026-06-24 16:28:13` | `cowrie.session.params` |
| `2026-06-24 16:28:13` | `cowrie.command.input` |
| `2026-06-24 16:28:13` | `cowrie.log.closed` |
| `2026-06-24 16:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b0a33cd343

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:29 |
| **Last Seen** | 2026-06-24 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:29:01` | `cowrie.session.connect` |
| `2026-06-24 16:29:01` | `cowrie.client.version` |
| `2026-06-24 16:29:01` | `cowrie.client.kex` |
| `2026-06-24 16:29:01` | `cowrie.login.success` |
| `2026-06-24 16:29:02` | `cowrie.session.params` |
| `2026-06-24 16:29:02` | `cowrie.command.input` |
| `2026-06-24 16:29:02` | `cowrie.log.closed` |
| `2026-06-24 16:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef6e598d09b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:29 |
| **Last Seen** | 2026-06-24 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:29:50` | `cowrie.session.connect` |
| `2026-06-24 16:29:50` | `cowrie.client.version` |
| `2026-06-24 16:29:51` | `cowrie.client.kex` |
| `2026-06-24 16:29:51` | `cowrie.login.success` |
| `2026-06-24 16:29:52` | `cowrie.session.params` |
| `2026-06-24 16:29:52` | `cowrie.command.input` |
| `2026-06-24 16:29:52` | `cowrie.log.closed` |
| `2026-06-24 16:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5865bdccc573

| Field | Detail |
|---|---|
| **Source IP** | `163.192.13[.]135` |
| **First Seen** | 2026-06-24 16:30 |
| **Last Seen** | 2026-06-24 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:30:19` | `cowrie.session.connect` |
| `2026-06-24 16:30:19` | `cowrie.client.version` |
| `2026-06-24 16:30:19` | `cowrie.client.kex` |
| `2026-06-24 16:30:19` | `cowrie.login.success` |
| `2026-06-24 16:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.192.13[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.192.13[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed85ef075613

| Field | Detail |
|---|---|
| **Source IP** | `163.192.13[.]135` |
| **First Seen** | 2026-06-24 16:30 |
| **Last Seen** | 2026-06-24 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:30:19` | `cowrie.session.connect` |
| `2026-06-24 16:30:19` | `cowrie.client.version` |
| `2026-06-24 16:30:19` | `cowrie.client.kex` |
| `2026-06-24 16:30:19` | `cowrie.login.success` |
| `2026-06-24 16:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.192.13[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.192.13[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b426130113f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:30 |
| **Last Seen** | 2026-06-24 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:30:40` | `cowrie.session.connect` |
| `2026-06-24 16:30:40` | `cowrie.client.version` |
| `2026-06-24 16:30:40` | `cowrie.client.kex` |
| `2026-06-24 16:30:40` | `cowrie.login.success` |
| `2026-06-24 16:30:41` | `cowrie.session.params` |
| `2026-06-24 16:30:41` | `cowrie.command.input` |
| `2026-06-24 16:30:41` | `cowrie.log.closed` |
| `2026-06-24 16:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54a5a1a8499

| Field | Detail |
|---|---|
| **Source IP** | `163.192.13[.]135` |
| **First Seen** | 2026-06-24 16:30 |
| **Last Seen** | 2026-06-24 16:32 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:30:42` | `cowrie.session.connect` |
| `2026-06-24 16:30:42` | `cowrie.client.version` |
| `2026-06-24 16:30:42` | `cowrie.client.kex` |
| `2026-06-24 16:30:43` | `cowrie.login.success` |
| `2026-06-24 16:30:44` | `cowrie.session.file_upload` |
| `2026-06-24 16:30:44` | `cowrie.session.params` |
| `2026-06-24 16:30:44` | `cowrie.command.input` |
| `2026-06-24 16:30:44` | `cowrie.command.input` |
| `2026-06-24 16:30:44` | `cowrie.command.input` |
| `2026-06-24 16:30:44` | `cowrie.command.failed` |
| `2026-06-24 16:30:45` | `cowrie.log.closed` |
| `2026-06-24 16:30:45` | `cowrie.session.params` |
| `2026-06-24 16:30:45` | `cowrie.command.input` |
| `2026-06-24 16:30:45` | `cowrie.log.closed` |
| `2026-06-24 16:30:46` | `cowrie.session.params` |
| `2026-06-24 16:30:46` | `cowrie.command.input` |
| `2026-06-24 16:30:46` | `cowrie.log.closed` |
| `2026-06-24 16:30:47` | `cowrie.session.params` |
| `2026-06-24 16:30:47` | `cowrie.command.input` |
| `2026-06-24 16:30:47` | `cowrie.command.failed` |
| `2026-06-24 16:30:47` | `cowrie.command.failed` |
| `2026-06-24 16:31:48` | `cowrie.session.params` |
| `2026-06-24 16:31:48` | `cowrie.command.input` |
| `2026-06-24 16:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.192.13[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.192.13[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0fabbbda1e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:31 |
| **Last Seen** | 2026-06-24 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:31:29` | `cowrie.session.connect` |
| `2026-06-24 16:31:29` | `cowrie.client.version` |
| `2026-06-24 16:31:29` | `cowrie.client.kex` |
| `2026-06-24 16:31:30` | `cowrie.login.success` |
| `2026-06-24 16:31:30` | `cowrie.session.params` |
| `2026-06-24 16:31:30` | `cowrie.command.input` |
| `2026-06-24 16:31:31` | `cowrie.log.closed` |
| `2026-06-24 16:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c382282e320

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:32 |
| **Last Seen** | 2026-06-24 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:32:18` | `cowrie.session.connect` |
| `2026-06-24 16:32:18` | `cowrie.client.version` |
| `2026-06-24 16:32:18` | `cowrie.client.kex` |
| `2026-06-24 16:32:18` | `cowrie.login.success` |
| `2026-06-24 16:32:19` | `cowrie.session.params` |
| `2026-06-24 16:32:19` | `cowrie.command.input` |
| `2026-06-24 16:32:19` | `cowrie.log.closed` |
| `2026-06-24 16:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25959e6129af

| Field | Detail |
|---|---|
| **Source IP** | `163.192.13[.]135` |
| **First Seen** | 2026-06-24 16:33 |
| **Last Seen** | 2026-06-24 16:35 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:33:03` | `cowrie.session.connect` |
| `2026-06-24 16:33:03` | `cowrie.client.version` |
| `2026-06-24 16:33:03` | `cowrie.client.kex` |
| `2026-06-24 16:33:04` | `cowrie.login.success` |
| `2026-06-24 16:33:05` | `cowrie.session.file_upload` |
| `2026-06-24 16:33:05` | `cowrie.session.params` |
| `2026-06-24 16:33:05` | `cowrie.command.input` |
| `2026-06-24 16:33:06` | `cowrie.command.input` |
| `2026-06-24 16:33:06` | `cowrie.command.input` |
| `2026-06-24 16:33:06` | `cowrie.command.failed` |
| `2026-06-24 16:33:06` | `cowrie.log.closed` |
| `2026-06-24 16:33:06` | `cowrie.session.params` |
| `2026-06-24 16:33:06` | `cowrie.command.input` |
| `2026-06-24 16:33:07` | `cowrie.log.closed` |
| `2026-06-24 16:33:07` | `cowrie.session.params` |
| `2026-06-24 16:33:07` | `cowrie.command.input` |
| `2026-06-24 16:33:07` | `cowrie.log.closed` |
| `2026-06-24 16:33:08` | `cowrie.session.params` |
| `2026-06-24 16:33:08` | `cowrie.command.input` |
| `2026-06-24 16:33:08` | `cowrie.command.failed` |
| `2026-06-24 16:33:08` | `cowrie.command.failed` |
| `2026-06-24 16:34:09` | `cowrie.session.params` |
| `2026-06-24 16:34:09` | `cowrie.command.input` |
| `2026-06-24 16:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.192.13[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.192.13[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-968ae3b34051

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:33 |
| **Last Seen** | 2026-06-24 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:33:07` | `cowrie.session.connect` |
| `2026-06-24 16:33:07` | `cowrie.client.version` |
| `2026-06-24 16:33:08` | `cowrie.client.kex` |
| `2026-06-24 16:33:08` | `cowrie.login.success` |
| `2026-06-24 16:33:09` | `cowrie.session.params` |
| `2026-06-24 16:33:09` | `cowrie.command.input` |
| `2026-06-24 16:33:09` | `cowrie.log.closed` |
| `2026-06-24 16:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9327472b69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:33 |
| **Last Seen** | 2026-06-24 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:33:55` | `cowrie.session.connect` |
| `2026-06-24 16:33:55` | `cowrie.client.version` |
| `2026-06-24 16:33:55` | `cowrie.client.kex` |
| `2026-06-24 16:33:55` | `cowrie.login.success` |
| `2026-06-24 16:33:56` | `cowrie.session.params` |
| `2026-06-24 16:33:56` | `cowrie.command.input` |
| `2026-06-24 16:33:56` | `cowrie.log.closed` |
| `2026-06-24 16:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83ce2d302e96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:34 |
| **Last Seen** | 2026-06-24 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:34:45` | `cowrie.session.connect` |
| `2026-06-24 16:34:45` | `cowrie.client.version` |
| `2026-06-24 16:34:45` | `cowrie.client.kex` |
| `2026-06-24 16:34:45` | `cowrie.login.success` |
| `2026-06-24 16:34:46` | `cowrie.session.params` |
| `2026-06-24 16:34:46` | `cowrie.command.input` |
| `2026-06-24 16:34:46` | `cowrie.log.closed` |
| `2026-06-24 16:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52d54be6233

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:35 |
| **Last Seen** | 2026-06-24 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:35:34` | `cowrie.session.connect` |
| `2026-06-24 16:35:34` | `cowrie.client.version` |
| `2026-06-24 16:35:34` | `cowrie.client.kex` |
| `2026-06-24 16:35:34` | `cowrie.login.success` |
| `2026-06-24 16:35:35` | `cowrie.session.params` |
| `2026-06-24 16:35:35` | `cowrie.command.input` |
| `2026-06-24 16:35:35` | `cowrie.log.closed` |
| `2026-06-24 16:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99559379e57e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 16:35 |
| **Last Seen** | 2026-06-24 16:36 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:35:53` | `cowrie.session.connect` |
| `2026-06-24 16:35:55` | `cowrie.client.version` |
| `2026-06-24 16:35:55` | `cowrie.client.kex` |
| `2026-06-24 16:36:01` | `cowrie.login.success` |
| `2026-06-24 16:36:05` | `cowrie.session.params` |
| `2026-06-24 16:36:05` | `cowrie.command.input` |
| `2026-06-24 16:36:07` | `cowrie.log.closed` |
| `2026-06-24 16:36:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151496cd3031

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:36 |
| **Last Seen** | 2026-06-24 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:36:24` | `cowrie.session.connect` |
| `2026-06-24 16:36:24` | `cowrie.client.version` |
| `2026-06-24 16:36:24` | `cowrie.client.kex` |
| `2026-06-24 16:36:25` | `cowrie.login.success` |
| `2026-06-24 16:36:26` | `cowrie.session.params` |
| `2026-06-24 16:36:26` | `cowrie.command.input` |
| `2026-06-24 16:36:26` | `cowrie.log.closed` |
| `2026-06-24 16:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6e3d8c5f3a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:37 |
| **Last Seen** | 2026-06-24 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:37:14` | `cowrie.session.connect` |
| `2026-06-24 16:37:14` | `cowrie.client.version` |
| `2026-06-24 16:37:14` | `cowrie.client.kex` |
| `2026-06-24 16:37:15` | `cowrie.login.success` |
| `2026-06-24 16:37:15` | `cowrie.session.params` |
| `2026-06-24 16:37:15` | `cowrie.command.input` |
| `2026-06-24 16:37:16` | `cowrie.log.closed` |
| `2026-06-24 16:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e350475a6371

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:38 |
| **Last Seen** | 2026-06-24 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:38:04` | `cowrie.session.connect` |
| `2026-06-24 16:38:04` | `cowrie.client.version` |
| `2026-06-24 16:38:04` | `cowrie.client.kex` |
| `2026-06-24 16:38:05` | `cowrie.login.success` |
| `2026-06-24 16:38:06` | `cowrie.session.params` |
| `2026-06-24 16:38:06` | `cowrie.command.input` |
| `2026-06-24 16:38:06` | `cowrie.log.closed` |
| `2026-06-24 16:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a4a8ffda8e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:38 |
| **Last Seen** | 2026-06-24 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:38:52` | `cowrie.session.connect` |
| `2026-06-24 16:38:52` | `cowrie.client.version` |
| `2026-06-24 16:38:52` | `cowrie.client.kex` |
| `2026-06-24 16:38:52` | `cowrie.login.success` |
| `2026-06-24 16:38:53` | `cowrie.session.params` |
| `2026-06-24 16:38:53` | `cowrie.command.input` |
| `2026-06-24 16:38:53` | `cowrie.log.closed` |
| `2026-06-24 16:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e65137b8ecf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:39 |
| **Last Seen** | 2026-06-24 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:39:39` | `cowrie.session.connect` |
| `2026-06-24 16:39:39` | `cowrie.client.version` |
| `2026-06-24 16:39:39` | `cowrie.client.kex` |
| `2026-06-24 16:39:39` | `cowrie.login.success` |
| `2026-06-24 16:39:40` | `cowrie.session.params` |
| `2026-06-24 16:39:40` | `cowrie.command.input` |
| `2026-06-24 16:39:40` | `cowrie.log.closed` |
| `2026-06-24 16:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8511b8a5ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:40 |
| **Last Seen** | 2026-06-24 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:40:27` | `cowrie.session.connect` |
| `2026-06-24 16:40:27` | `cowrie.client.version` |
| `2026-06-24 16:40:27` | `cowrie.client.kex` |
| `2026-06-24 16:40:27` | `cowrie.login.success` |
| `2026-06-24 16:40:28` | `cowrie.session.params` |
| `2026-06-24 16:40:28` | `cowrie.command.input` |
| `2026-06-24 16:40:28` | `cowrie.log.closed` |
| `2026-06-24 16:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82de556a7968

| Field | Detail |
|---|---|
| **Source IP** | `34.62.138[.]158` |
| **First Seen** | 2026-06-24 16:40 |
| **Last Seen** | 2026-06-24 16:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:40:40` | `cowrie.session.connect` |
| `2026-06-24 16:40:40` | `cowrie.client.version` |
| `2026-06-24 16:40:40` | `cowrie.client.kex` |
| `2026-06-24 16:40:42` | `cowrie.login.success` |
| `2026-06-24 16:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.138[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.62.138[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3890d2ba4cff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:41 |
| **Last Seen** | 2026-06-24 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:41:17` | `cowrie.session.connect` |
| `2026-06-24 16:41:17` | `cowrie.client.version` |
| `2026-06-24 16:41:17` | `cowrie.client.kex` |
| `2026-06-24 16:41:17` | `cowrie.login.success` |
| `2026-06-24 16:41:18` | `cowrie.session.params` |
| `2026-06-24 16:41:18` | `cowrie.command.input` |
| `2026-06-24 16:41:18` | `cowrie.log.closed` |
| `2026-06-24 16:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-888123fb8132

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:42 |
| **Last Seen** | 2026-06-24 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:42:07` | `cowrie.session.connect` |
| `2026-06-24 16:42:07` | `cowrie.client.version` |
| `2026-06-24 16:42:08` | `cowrie.client.kex` |
| `2026-06-24 16:42:08` | `cowrie.login.success` |
| `2026-06-24 16:42:09` | `cowrie.session.params` |
| `2026-06-24 16:42:09` | `cowrie.command.input` |
| `2026-06-24 16:42:09` | `cowrie.log.closed` |
| `2026-06-24 16:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b608d178b01f

| Field | Detail |
|---|---|
| **Source IP** | `47.253.245[.]52` |
| **First Seen** | 2026-06-24 16:42 |
| **Last Seen** | 2026-06-24 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:42:29` | `cowrie.session.connect` |
| `2026-06-24 16:42:29` | `cowrie.telnet.option` |
| `2026-06-24 16:42:29` | `cowrie.telnet.option` |
| `2026-06-24 16:43:29` | `cowrie.login.success` |
| `2026-06-24 16:43:29` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.253.245[.]52` to AbuseIPDB if not already reported
- [ ] Block `47.253.245[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6974e4bccf9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:42 |
| **Last Seen** | 2026-06-24 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:42:58` | `cowrie.session.connect` |
| `2026-06-24 16:42:58` | `cowrie.client.version` |
| `2026-06-24 16:42:58` | `cowrie.client.kex` |
| `2026-06-24 16:42:59` | `cowrie.login.success` |
| `2026-06-24 16:43:00` | `cowrie.session.params` |
| `2026-06-24 16:43:00` | `cowrie.command.input` |
| `2026-06-24 16:43:00` | `cowrie.log.closed` |
| `2026-06-24 16:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c067a6f38b50

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:43 |
| **Last Seen** | 2026-06-24 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:43:49` | `cowrie.session.connect` |
| `2026-06-24 16:43:49` | `cowrie.client.version` |
| `2026-06-24 16:43:49` | `cowrie.client.kex` |
| `2026-06-24 16:43:49` | `cowrie.login.success` |
| `2026-06-24 16:43:50` | `cowrie.session.params` |
| `2026-06-24 16:43:50` | `cowrie.command.input` |
| `2026-06-24 16:43:50` | `cowrie.log.closed` |
| `2026-06-24 16:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dbf69c08e83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:44 |
| **Last Seen** | 2026-06-24 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:44:39` | `cowrie.session.connect` |
| `2026-06-24 16:44:39` | `cowrie.client.version` |
| `2026-06-24 16:44:39` | `cowrie.client.kex` |
| `2026-06-24 16:44:39` | `cowrie.login.success` |
| `2026-06-24 16:44:40` | `cowrie.session.params` |
| `2026-06-24 16:44:40` | `cowrie.command.input` |
| `2026-06-24 16:44:40` | `cowrie.log.closed` |
| `2026-06-24 16:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eab1c3ec8ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:45 |
| **Last Seen** | 2026-06-24 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:45:28` | `cowrie.session.connect` |
| `2026-06-24 16:45:28` | `cowrie.client.version` |
| `2026-06-24 16:45:28` | `cowrie.client.kex` |
| `2026-06-24 16:45:28` | `cowrie.login.success` |
| `2026-06-24 16:45:29` | `cowrie.session.params` |
| `2026-06-24 16:45:29` | `cowrie.command.input` |
| `2026-06-24 16:45:29` | `cowrie.log.closed` |
| `2026-06-24 16:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74a45ac15ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:46 |
| **Last Seen** | 2026-06-24 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:46:18` | `cowrie.session.connect` |
| `2026-06-24 16:46:18` | `cowrie.client.version` |
| `2026-06-24 16:46:18` | `cowrie.client.kex` |
| `2026-06-24 16:46:19` | `cowrie.login.success` |
| `2026-06-24 16:46:19` | `cowrie.session.params` |
| `2026-06-24 16:46:19` | `cowrie.command.input` |
| `2026-06-24 16:46:20` | `cowrie.log.closed` |
| `2026-06-24 16:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc3839755ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:47 |
| **Last Seen** | 2026-06-24 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:47:08` | `cowrie.session.connect` |
| `2026-06-24 16:47:08` | `cowrie.client.version` |
| `2026-06-24 16:47:08` | `cowrie.client.kex` |
| `2026-06-24 16:47:08` | `cowrie.login.success` |
| `2026-06-24 16:47:09` | `cowrie.session.params` |
| `2026-06-24 16:47:09` | `cowrie.command.input` |
| `2026-06-24 16:47:09` | `cowrie.log.closed` |
| `2026-06-24 16:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8018f359e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:47 |
| **Last Seen** | 2026-06-24 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:47:59` | `cowrie.session.connect` |
| `2026-06-24 16:47:59` | `cowrie.client.version` |
| `2026-06-24 16:47:59` | `cowrie.client.kex` |
| `2026-06-24 16:47:59` | `cowrie.login.success` |
| `2026-06-24 16:48:00` | `cowrie.session.params` |
| `2026-06-24 16:48:00` | `cowrie.command.input` |
| `2026-06-24 16:48:00` | `cowrie.log.closed` |
| `2026-06-24 16:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-217be72c450b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:48 |
| **Last Seen** | 2026-06-24 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:48:50` | `cowrie.session.connect` |
| `2026-06-24 16:48:50` | `cowrie.client.version` |
| `2026-06-24 16:48:50` | `cowrie.client.kex` |
| `2026-06-24 16:48:51` | `cowrie.login.success` |
| `2026-06-24 16:48:51` | `cowrie.session.params` |
| `2026-06-24 16:48:51` | `cowrie.command.input` |
| `2026-06-24 16:48:51` | `cowrie.log.closed` |
| `2026-06-24 16:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f040e080a40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:49 |
| **Last Seen** | 2026-06-24 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:49:41` | `cowrie.session.connect` |
| `2026-06-24 16:49:41` | `cowrie.client.version` |
| `2026-06-24 16:49:41` | `cowrie.client.kex` |
| `2026-06-24 16:49:41` | `cowrie.login.success` |
| `2026-06-24 16:49:42` | `cowrie.session.params` |
| `2026-06-24 16:49:42` | `cowrie.command.input` |
| `2026-06-24 16:49:42` | `cowrie.log.closed` |
| `2026-06-24 16:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1fb20dadf51

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 16:50 |
| **Last Seen** | 2026-06-24 16:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:50:13` | `cowrie.session.connect` |
| `2026-06-24 16:50:14` | `cowrie.client.version` |
| `2026-06-24 16:50:14` | `cowrie.client.kex` |
| `2026-06-24 16:50:21` | `cowrie.login.success` |
| `2026-06-24 16:50:25` | `cowrie.session.params` |
| `2026-06-24 16:50:25` | `cowrie.command.input` |
| `2026-06-24 16:50:26` | `cowrie.log.closed` |
| `2026-06-24 16:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336b4b1b4852

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:50 |
| **Last Seen** | 2026-06-24 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:50:32` | `cowrie.session.connect` |
| `2026-06-24 16:50:32` | `cowrie.client.version` |
| `2026-06-24 16:50:32` | `cowrie.client.kex` |
| `2026-06-24 16:50:33` | `cowrie.login.success` |
| `2026-06-24 16:50:33` | `cowrie.session.params` |
| `2026-06-24 16:50:33` | `cowrie.command.input` |
| `2026-06-24 16:50:34` | `cowrie.log.closed` |
| `2026-06-24 16:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65587c19c108

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:51 |
| **Last Seen** | 2026-06-24 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:51:23` | `cowrie.session.connect` |
| `2026-06-24 16:51:23` | `cowrie.client.version` |
| `2026-06-24 16:51:23` | `cowrie.client.kex` |
| `2026-06-24 16:51:23` | `cowrie.login.success` |
| `2026-06-24 16:51:24` | `cowrie.session.params` |
| `2026-06-24 16:51:24` | `cowrie.command.input` |
| `2026-06-24 16:51:24` | `cowrie.log.closed` |
| `2026-06-24 16:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d7f479b9d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:52 |
| **Last Seen** | 2026-06-24 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:52:13` | `cowrie.session.connect` |
| `2026-06-24 16:52:13` | `cowrie.client.version` |
| `2026-06-24 16:52:14` | `cowrie.client.kex` |
| `2026-06-24 16:52:14` | `cowrie.login.success` |
| `2026-06-24 16:52:15` | `cowrie.session.params` |
| `2026-06-24 16:52:15` | `cowrie.command.input` |
| `2026-06-24 16:52:15` | `cowrie.log.closed` |
| `2026-06-24 16:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbaf9d9d4f6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:53 |
| **Last Seen** | 2026-06-24 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:53:05` | `cowrie.session.connect` |
| `2026-06-24 16:53:05` | `cowrie.client.version` |
| `2026-06-24 16:53:05` | `cowrie.client.kex` |
| `2026-06-24 16:53:05` | `cowrie.login.success` |
| `2026-06-24 16:53:06` | `cowrie.session.params` |
| `2026-06-24 16:53:06` | `cowrie.command.input` |
| `2026-06-24 16:53:06` | `cowrie.log.closed` |
| `2026-06-24 16:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00fcd725ab98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:53 |
| **Last Seen** | 2026-06-24 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:53:58` | `cowrie.session.connect` |
| `2026-06-24 16:53:58` | `cowrie.client.version` |
| `2026-06-24 16:53:58` | `cowrie.client.kex` |
| `2026-06-24 16:53:58` | `cowrie.login.success` |
| `2026-06-24 16:53:59` | `cowrie.session.params` |
| `2026-06-24 16:53:59` | `cowrie.command.input` |
| `2026-06-24 16:53:59` | `cowrie.log.closed` |
| `2026-06-24 16:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798e2b9ebea3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:54 |
| **Last Seen** | 2026-06-24 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:54:51` | `cowrie.session.connect` |
| `2026-06-24 16:54:51` | `cowrie.client.version` |
| `2026-06-24 16:54:51` | `cowrie.client.kex` |
| `2026-06-24 16:54:52` | `cowrie.login.success` |
| `2026-06-24 16:54:52` | `cowrie.session.params` |
| `2026-06-24 16:54:52` | `cowrie.command.input` |
| `2026-06-24 16:54:53` | `cowrie.log.closed` |
| `2026-06-24 16:54:53` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **272** | 2026-06-24 12:55 | 2026-06-24 16:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `34.53.157[.]149` | **10** | 2026-06-24 16:40 | 2026-06-24 16:41 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **5** | 2026-06-24 15:23 | 2026-06-24 16:45 | 4m | 0 | `T1592` | 🟢 LOW |
| `111.228.42[.]144` | **3** | 2026-06-24 13:56 | 2026-06-24 14:15 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-24 15:14 | 2026-06-24 16:12 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.11[.]46` | **2** | 2026-06-24 14:38 | 2026-06-24 14:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]79` | **2** | 2026-06-24 14:06 | 2026-06-24 15:41 | 4m | 0 | `T1592` | 🟢 LOW |
| `27.156.98[.]194` | **2** | 2026-06-24 14:09 | 2026-06-24 14:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-06-24 13:26 | 2026-06-24 14:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.151.14[.]195` | **2** | 2026-06-24 12:57 | 2026-06-24 13:18 | 4m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]33` | **2** | 2026-06-24 13:17 | 2026-06-24 13:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]100` | 1 | 2026-06-24 16:00 | 2026-06-24 16:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-24 12:55 | 2026-06-24 12:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `165.232.61[.]133` | 1 | 2026-06-24 16:16 | 2026-06-24 16:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.111.218[.]2` | 1 | 2026-06-24 14:13 | 2026-06-24 14:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `34.62.138[.]158` | 1 | 2026-06-24 16:40 | 2026-06-24 16:40 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-06-24 16:03 | 2026-06-24 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-06-24 14:36 | 2026-06-24 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-06-24 15:36 | 2026-06-24 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-06-24 14:35 | 2026-06-24 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]232` | 1 | 2026-06-24 14:08 | 2026-06-24 14:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]51` | 1 | 2026-06-24 13:35 | 2026-06-24 13:35 | 16s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]8` | 1 | 2026-06-24 13:02 | 2026-06-24 13:02 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (31 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **21/73** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `f11dd1e4a3d27eef85d44154d662ce94234ee71b54468aeb2c23edb30b74a5c5` | ELF Binary (Linux executable) (x86-64 64-bit) | `f11dd1e4a3d27eef...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
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
| `161.118.237[.]181` | SG | 500 Oracle Parkway | **100** ⚠️ | 2 |
| `111.228.42[.]144` | CN | eleven street,No. 18 Institute of Jingdong headquarters | **100** ⚠️ | 4 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `77.90.185[.]16` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `168.144.45[.]211` | SG | DigitalOcean, LLC | **100** ⚠️ | 30 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `66.132.195[.]51` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `27.156.98[.]194` | CN | Broadband network the city | **100** ⚠️ | 3 |
| `171.111.218[.]2` | CN | CHINANET GUANGXI PROVINCE NETWORK | **100** ⚠️ | 13 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 352 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 320 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 651 cases |
| Tool 34  | Credential Extractor        | ✅ 326 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (2.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 31 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 320 priority case(s) shown individually · 23 recon entry/entries in table (11 group(s) consolidating 304 session(s)).

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
_Report time: 2026-06-24T17:59:26Z_

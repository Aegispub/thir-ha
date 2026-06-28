# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-28 |
| **Generated At** | 2026-06-28T23:07:35Z |
| **Shift Time** | 23:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **375** |
| Confirmed Threats | **357** |
| False Positives Filtered | **18** (4.8%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **11** |
| High Severity Cases | **208** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **167** |
| Malware Samples Analyzed | **5** HIGH · **41** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **211** |
| Unique Credential Pairs | **200** |
| Unique Usernames | **93** |
| Unique Passwords | **149** |
| Successful Auth Pairs | **205** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `admin` | 19 |
| `ubuntu` | 8 |
| `apache` | 5 |
| `dell` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 16 |
| `1234` | 7 |
| `LeitboGi0ro` | 6 |
| `111111` | 6 |
| `1qaz@WSX` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `admin` | 2 |
| `ps` | `1` | 2 |
| `root` | `smo@@kkklss` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `1qaz@WSX3edc` | `209.99.185.59` | 2026-06-28T20:55:44 |
| `iexcel_wuhan` | `0` | `209.99.185.59` | 2026-06-28T20:56:34 |
| `test` | `zxcvbnm` | `209.99.185.59` | 2026-06-28T20:57:24 |
| `root` | `P@SVVORD` | `45.198.224.120` | 2026-06-28T20:57:31 |
| `root` | `Toor123` | `209.99.185.59` | 2026-06-28T20:58:14 |
| `root` | `P@ssw0rd$Ubuntu2025` | `209.99.185.59` | 2026-06-28T20:59:03 |
| `pi` | `12345` | `209.99.185.59` | 2026-06-28T20:59:53 |
| `root` | `taytay` | `209.99.185.59` | 2026-06-28T21:00:45 |
| `root` | `user123` | `209.99.185.59` | 2026-06-28T21:01:37 |
| `root` | `112233445566` | `209.99.185.59` | 2026-06-28T21:02:29 |
| `install` | `11111111` | `209.99.185.59` | 2026-06-28T21:03:21 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-28T21:04:00 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-28T21:04:01 |
| `rstudio` | `rstudio` | `209.99.185.59` | 2026-06-28T21:04:13 |
| `ftp` | `abc123` | `209.99.185.59` | 2026-06-28T21:05:04 |
| `helga` | `helga` | `209.99.185.59` | 2026-06-28T21:05:56 |
| `deploy` | `qwerty123456` | `209.99.185.59` | 2026-06-28T21:06:49 |
| `xi` | `123456` | `209.99.185.59` | 2026-06-28T21:07:42 |
| `ubuntu` | `hduser12345` | `45.205.1.42` | 2026-06-28T21:08:21 |
| `root` | `manager1` | `209.99.185.59` | 2026-06-28T21:08:36 |
| `ubuntu` | `111111` | `45.198.224.120` | 2026-06-28T21:09:05 |
| `ubuntu` | `qwerty12` | `209.99.185.59` | 2026-06-28T21:09:30 |
| `JiaYuxin` | `JIaYuxin` | `209.99.185.59` | 2026-06-28T21:10:23 |
| `pxy` | `pxy` | `209.99.185.59` | 2026-06-28T21:11:16 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.223` | 2026-06-28T21:12:02 |
| `meklis` | `meklis111111` | `209.99.185.59` | 2026-06-28T21:12:10 |
| `postgres` | `1111` | `209.99.185.59` | 2026-06-28T21:13:05 |
| `admin` | `1234qwer` | `209.99.185.59` | 2026-06-28T21:14:02 |
| `hyj` | `houyujie971022` | `209.99.185.59` | 2026-06-28T21:14:59 |
| `uftp` | `1234qwer` | `209.99.185.59` | 2026-06-28T21:15:55 |
| `cyzhang` | `123456` | `209.99.185.59` | 2026-06-28T21:16:52 |
| `zl` | `zhangliang` | `209.99.185.59` | 2026-06-28T21:17:46 |
| `root` | `111111` | `91.92.40.8` | 2026-06-28T21:17:49 |
| `postgres` | `pass123` | `209.99.185.59` | 2026-06-28T21:18:39 |
| `root` | `123123` | `91.92.40.8` | 2026-06-28T21:19:13 |
| `zlwang` | `123456` | `209.99.185.59` | 2026-06-28T21:19:34 |
| `tyh` | `Tyh@123` | `209.99.185.59` | 2026-06-28T21:20:30 |
| `root` | `ZAQ!xsw2` | `45.198.224.120` | 2026-06-28T21:20:35 |
| `root` | `1234` | `91.92.40.8` | 2026-06-28T21:20:40 |
| `wt` | `123456` | `209.99.185.59` | 2026-06-28T21:21:27 |
| `root` | `12345` | `91.92.40.8` | 2026-06-28T21:22:04 |
| `root` | `1234zxcv` | `209.99.185.59` | 2026-06-28T21:22:23 |
| `ubuntu` | `ubuntu@2021` | `45.205.1.42` | 2026-06-28T21:23:09 |
| `huzheng` | `huzheng` | `209.99.185.59` | 2026-06-28T21:23:19 |
| `dongxuewei` | `dongxuewei123` | `209.99.185.59` | 2026-06-28T21:24:14 |
| `root` | `12345678` | `91.92.40.8` | 2026-06-28T21:24:42 |
| `ansible` | `111111` | `209.99.185.59` | 2026-06-28T21:25:10 |
| `root` | `admin` | `185.220.101.188` | 2026-06-28T21:25:45 |
| `root` | `123456789` | `91.92.40.8` | 2026-06-28T21:25:57 |
| `root` | `administrator123` | `209.99.185.59` | 2026-06-28T21:26:07 |
| `user` | `1234567890` | `209.99.185.59` | 2026-06-28T21:27:05 |
| `root` | `Password1` | `91.92.40.8` | 2026-06-28T21:27:14 |
| `WuJun` | `wujun123` | `209.99.185.59` | 2026-06-28T21:28:02 |
| `root` | `admin` | `91.92.40.8` | 2026-06-28T21:28:34 |
| `root` | `fergus` | `209.99.185.59` | 2026-06-28T21:29:00 |
| `root` | `admin123` | `91.92.40.8` | 2026-06-28T21:29:52 |
| `gas` | `123456` | `209.99.185.59` | 2026-06-28T21:29:56 |
| `hui` | `1234` | `209.99.185.59` | 2026-06-28T21:30:52 |
| `root` | `default` | `91.92.40.8` | 2026-06-28T21:31:09 |
| `user` | `pokemon` | `209.99.185.59` | 2026-06-28T21:31:50 |
| `kelly` | `kelly` | `45.198.224.120` | 2026-06-28T21:32:05 |
| `root` | `letmein` | `91.92.40.8` | 2026-06-28T21:32:30 |
| `sftpuser` | `sftpuser` | `209.99.185.59` | 2026-06-28T21:32:47 |
| `zyc` | `123456` | `209.99.185.59` | 2026-06-28T21:33:46 |
| `root` | `passw0rd` | `91.92.40.8` | 2026-06-28T21:34:00 |
| `root` | `1qaz#EDC5tgb` | `209.99.185.59` | 2026-06-28T21:34:46 |
| `root` | `password` | `91.92.40.8` | 2026-06-28T21:35:29 |
| `www2` | `www2` | `209.99.185.59` | 2026-06-28T21:35:45 |
| `max` | `max2021` | `209.99.185.59` | 2026-06-28T21:36:42 |
| `root` | `qwerty` | `91.92.40.8` | 2026-06-28T21:36:58 |
| `oryun4877` | `oryun4877` | `209.99.185.59` | 2026-06-28T21:37:40 |
| `root` | `ubuntu123` | `45.205.1.42` | 2026-06-28T21:38:02 |
| `jira` | `p@ssw0rd` | `209.99.185.59` | 2026-06-28T21:38:39 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-28T21:39:17 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-28T21:39:21 |
| `root` | `Admin@2017` | `209.99.185.59` | 2026-06-28T21:39:40 |
| `root` | `system` | `91.92.40.8` | 2026-06-28T21:40:09 |
| `es` | `1qaz@WSX` | `209.99.185.59` | 2026-06-28T21:40:41 |
| `root` | `toor` | `91.92.40.8` | 2026-06-28T21:41:41 |
| `baotruongvn` | `baotruongvn` | `209.99.185.59` | 2026-06-28T21:41:43 |
| `ubuntu` | `user123` | `209.99.185.59` | 2026-06-28T21:42:42 |
| `admin` | `111111` | `91.92.40.8` | 2026-06-28T21:43:15 |
| `root` | `P@ssword!@#` | `45.198.224.120` | 2026-06-28T21:43:41 |
| `ptj` | `pengtaojiang` | `209.99.185.59` | 2026-06-28T21:43:42 |
| `app1` | `1qaz@WSX` | `209.99.185.59` | 2026-06-28T21:44:43 |
| `admin` | `123123` | `91.92.40.8` | 2026-06-28T21:44:53 |
| `project` | `123456` | `209.99.185.59` | 2026-06-28T21:45:44 |
| `admin` | `1234` | `91.92.40.8` | 2026-06-28T21:46:39 |
| `siyuan` | `siyuan` | `209.99.185.59` | 2026-06-28T21:46:47 |
| `kdcproxy` | `1` | `209.99.185.59` | 2026-06-28T21:47:49 |
| `admin` | `12345` | `91.92.40.8` | 2026-06-28T21:48:30 |
| `conda` | `conda` | `209.99.185.59` | 2026-06-28T21:48:50 |
| `root` | `Password#123456` | `209.99.185.59` | 2026-06-28T21:49:51 |
| `admin` | `123456` | `91.92.40.8` | 2026-06-28T21:50:30 |
| `pathak` | `1` | `209.99.185.59` | 2026-06-28T21:50:52 |
| `tianhao` | `111111` | `209.99.185.59` | 2026-06-28T21:51:55 |
| `admin` | `12345678` | `91.92.40.8` | 2026-06-28T21:52:42 |
| `root` | `gwerty` | `45.205.1.42` | 2026-06-28T21:52:46 |
| `vnc` | `123` | `209.99.185.59` | 2026-06-28T21:53:00 |
| `root` | `3344520` | `209.99.185.59` | 2026-06-28T21:54:06 |
| `admin` | `123456789` | `91.92.40.8` | 2026-06-28T21:55:00 |
| `root` | `43e75233` | `45.198.224.120` | 2026-06-28T21:55:07 |
| `tmax8` | `tmax8` | `209.99.185.59` | 2026-06-28T21:55:10 |
| `root` | `qwe!!` | `209.99.185.59` | 2026-06-28T21:56:15 |
| `admin` | `Administrator` | `91.92.40.8` | 2026-06-28T21:57:11 |
| `ubuntu` | `q1q1q1q1` | `209.99.185.59` | 2026-06-28T21:57:21 |
| `root` | `Root2021` | `209.99.185.59` | 2026-06-28T21:58:26 |
| `fairy` | `fairy` | `209.99.185.59` | 2026-06-28T21:59:33 |
| `admin` | `access` | `91.92.40.8` | 2026-06-28T21:59:34 |
| `morut` | `morut1` | `209.99.185.59` | 2026-06-28T22:00:31 |
| `root` | `qwert12345678` | `209.99.185.59` | 2026-06-28T22:01:15 |
| `admin` | `admin` | `91.92.40.8` | 2026-06-28T22:01:52 |
| `root` | `777` | `209.99.185.59` | 2026-06-28T22:01:58 |
| `root` | `5r4e3w2q` | `209.99.185.59` | 2026-06-28T22:02:41 |
| `sangmin` | `sangmin` | `209.99.185.59` | 2026-06-28T22:03:25 |
| `dell` | `09a70b81` | `209.99.185.59` | 2026-06-28T22:04:10 |
| `admin` | `admin123` | `91.92.40.8` | 2026-06-28T22:04:12 |
| `root` | `3edcxzaq1` | `209.99.185.59` | 2026-06-28T22:04:55 |
| `testuser` | `1qaz@WSX` | `209.99.185.59` | 2026-06-28T22:05:42 |
| `dell` | `dell@000` | `209.99.185.59` | 2026-06-28T22:06:27 |
| `ps` | `1` | `45.198.224.120` | 2026-06-28T22:06:32 |
| `admin` | `adminadmin` | `91.92.40.8` | 2026-06-28T22:06:57 |
| `db` | `db!` | `209.99.185.59` | 2026-06-28T22:07:12 |
| `oracle` | `manager` | `45.205.1.42` | 2026-06-28T22:07:30 |
| `oracle` | `test123` | `209.99.185.59` | 2026-06-28T22:07:57 |
| `root` | `Password!!` | `209.99.185.59` | 2026-06-28T22:08:43 |
| `datacenter` | `1qaz@WSX` | `209.99.185.59` | 2026-06-28T22:09:27 |
| `admin` | `letmein` | `91.92.40.8` | 2026-06-28T22:09:32 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-28T22:10:07 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-28T22:10:07 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-28T22:10:11 |
| `root` | `1a2b3c` | `209.99.185.59` | 2026-06-28T22:10:11 |
| `nodeproxy` | `123456` | `209.99.185.59` | 2026-06-28T22:10:56 |
| `root` | `123@@@` | `129.146.97.8` | 2026-06-28T22:11:12 |
| `root` | `LeitboGi0ro` | `129.146.97.8` | 2026-06-28T22:11:12 |
| `testing` | `1qaz@WSX` | `209.99.185.59` | 2026-06-28T22:11:42 |
| `root` | `redhat90` | `209.99.185.59` | 2026-06-28T22:12:28 |
| `admin` | `passw0rd` | `91.92.40.8` | 2026-06-28T22:12:30 |
| `root` | `sl0b0zl4t4v4!` | `209.99.185.59` | 2026-06-28T22:13:14 |
| `root` | `dearbook` | `209.99.185.59` | 2026-06-28T22:14:02 |
| `ftp_test` | `ftp_test` | `209.99.185.59` | 2026-06-28T22:14:47 |
| `admin` | `password` | `91.92.40.8` | 2026-06-28T22:15:11 |
| `devops` | `123456` | `209.99.185.59` | 2026-06-28T22:15:32 |
| `michael` | `12345` | `209.99.185.59` | 2026-06-28T22:16:18 |
| `root` | `matthew` | `209.99.185.59` | 2026-06-28T22:17:06 |
| `root` | `root@4444` | `209.99.185.59` | 2026-06-28T22:17:56 |
| `admin` | `password1` | `91.92.40.8` | 2026-06-28T22:18:02 |
| `root` | `Test!234` | `45.198.224.120` | 2026-06-28T22:18:03 |
| `dell` | `dell@222` | `209.99.185.59` | 2026-06-28T22:18:45 |
| `hxy` | `hxy123` | `209.99.185.59` | 2026-06-28T22:19:33 |
| `zyserver` | `123456` | `209.99.185.59` | 2026-06-28T22:20:22 |
| `admin` | `qwerty` | `91.92.40.8` | 2026-06-28T22:20:56 |
| `zhouh` | `pass1234` | `209.99.185.59` | 2026-06-28T22:21:09 |
| `melon` | `dxg` | `209.99.185.59` | 2026-06-28T22:21:57 |
| `root` | `Password!@#$%` | `45.205.1.42` | 2026-06-28T22:22:04 |
| `houwj` | `TCWjGQdv7W` | `209.99.185.59` | 2026-06-28T22:22:45 |
| `dell` | `admin@2222` | `209.99.185.59` | 2026-06-28T22:23:32 |
| `apache` | `1234` | `91.92.40.8` | 2026-06-28T22:23:54 |
| `root` | `schweb` | `209.99.185.59` | 2026-06-28T22:24:25 |
| `root` | `Root@2014` | `209.99.185.59` | 2026-06-28T22:25:15 |
| `hqzhao` | `945401` | `209.99.185.59` | 2026-06-28T22:26:03 |
| `abms` | `abms` | `209.99.185.59` | 2026-06-28T22:26:53 |
| `apache` | `12345678` | `91.92.40.8` | 2026-06-28T22:26:58 |
| `hanxue` | `hanxue` | `209.99.185.59` | 2026-06-28T22:27:41 |
| `wjx` | `wjx` | `209.99.185.59` | 2026-06-28T22:28:30 |
| `adminuser` | `111111` | `209.99.185.59` | 2026-06-28T22:29:20 |
| `chiye1` | `chiye1` | `45.198.224.120` | 2026-06-28T22:29:22 |
| `apache` | `admin` | `91.92.40.8` | 2026-06-28T22:30:05 |
| `root` | `Zjipst@123456` | `209.99.185.59` | 2026-06-28T22:30:10 |
| `airchem` | `korea2018` | `209.99.185.59` | 2026-06-28T22:31:00 |
| `liyi` | `ly4321348` | `209.99.185.59` | 2026-06-28T22:31:51 |
| `root` | `ubuntu` | `65.181.92.228` | 2026-06-28T22:32:06 |
| `cwh` | `cwhcwh` | `209.99.185.59` | 2026-06-28T22:32:43 |
| `apache` | `apache` | `91.92.40.8` | 2026-06-28T22:33:23 |
| `leizhang` | `leizhang` | `209.99.185.59` | 2026-06-28T22:33:32 |
| `root` | `1122334455` | `209.99.185.59` | 2026-06-28T22:34:22 |
| `root` | `hellokitty` | `209.99.185.59` | 2026-06-28T22:35:11 |
| `wanggp` | `wanggp` | `209.99.185.59` | 2026-06-28T22:36:00 |
| `apache` | `password` | `91.92.40.8` | 2026-06-28T22:36:24 |
| `root` | `nmap` | `45.205.1.42` | 2026-06-28T22:36:26 |
| `cc` | `123` | `209.99.185.59` | 2026-06-28T22:36:50 |
| `root` | `QWEqwe123` | `209.99.185.59` | 2026-06-28T22:37:40 |
| `yanghao` | `yanghao` | `209.99.185.59` | 2026-06-28T22:38:31 |
| `root` | `a123456123456` | `209.99.185.59` | 2026-06-28T22:39:21 |
| `ubuntu` | `!QAZ2wsx` | `209.99.185.59` | 2026-06-28T22:40:10 |
| `root` | `P@sswd@1234` | `45.198.224.120` | 2026-06-28T22:40:33 |
| `root` | `passw0rd12` | `209.99.185.59` | 2026-06-28T22:41:00 |
| `root` | `p0o9i8u7y6` | `209.99.185.59` | 2026-06-28T22:41:51 |
| `ps` | `1` | `209.99.185.59` | 2026-06-28T22:42:42 |
| `lll` | `lll` | `209.99.185.59` | 2026-06-28T22:43:35 |
| `root` | `P@ssw0rd123!@#` | `209.99.185.59` | 2026-06-28T22:44:28 |
| `asd` | `1234` | `209.99.185.59` | 2026-06-28T22:45:19 |
| `lab` | `123456` | `209.99.185.59` | 2026-06-28T22:46:10 |
| `hduser` | `0` | `209.99.185.59` | 2026-06-28T22:47:02 |
| `mysql` | `1234` | `209.99.185.59` | 2026-06-28T22:47:53 |
| `Robert` | `123456` | `209.99.185.59` | 2026-06-28T22:48:45 |
| `root` | `test2011` | `209.99.185.59` | 2026-06-28T22:49:38 |
| `root` | `Root@2023` | `209.99.185.59` | 2026-06-28T22:50:31 |
| `ubuntu` | `deploy12345` | `45.205.1.42` | 2026-06-28T22:50:56 |
| `zhanghua` | `123456` | `209.99.185.59` | 2026-06-28T22:51:24 |
| `root` | `amanda` | `45.198.224.120` | 2026-06-28T22:52:01 |
| `ksh` | `123456` | `209.99.185.59` | 2026-06-28T22:52:16 |
| `jihyun` | `1234` | `209.99.185.59` | 2026-06-28T22:53:10 |
| `www` | `wwwpassword` | `209.99.185.59` | 2026-06-28T22:54:02 |
| `root` | `asdasdpassword` | `209.99.185.59` | 2026-06-28T22:54:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **375** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 198 |
| Paramiko (Python) | 12 |
| libssh | 6 |
| OpenSSH | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 155 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 40 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 3 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `b21d7cdcc813...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 155 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 40 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `b21d7cdcc813...` | OpenSSH | 2 | 1 | Mirai/variant |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 38 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `91.92.40.8`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **17** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS263656` | BRSULNET TELECOM LTDA | 1 | MEDIUM |
| `AS60729` | Stiftung Erneuerbare Freiheit | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS136180` | Beijing Tiantexin Tech. Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (207)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-77051f3031bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:55 |
| **Last Seen** | 2026-06-28 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:55:43` | `cowrie.session.connect` |
| `2026-06-28 20:55:43` | `cowrie.client.version` |
| `2026-06-28 20:55:43` | `cowrie.client.kex` |
| `2026-06-28 20:55:44` | `cowrie.login.success` |
| `2026-06-28 20:55:44` | `cowrie.session.params` |
| `2026-06-28 20:55:44` | `cowrie.command.input` |
| `2026-06-28 20:55:45` | `cowrie.log.closed` |
| `2026-06-28 20:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f196c101125

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:56 |
| **Last Seen** | 2026-06-28 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:56:34` | `cowrie.session.connect` |
| `2026-06-28 20:56:34` | `cowrie.client.version` |
| `2026-06-28 20:56:34` | `cowrie.client.kex` |
| `2026-06-28 20:56:34` | `cowrie.login.success` |
| `2026-06-28 20:56:35` | `cowrie.session.params` |
| `2026-06-28 20:56:35` | `cowrie.command.input` |
| `2026-06-28 20:56:35` | `cowrie.log.closed` |
| `2026-06-28 20:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de9ab02c7440

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:57 |
| **Last Seen** | 2026-06-28 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:57:23` | `cowrie.session.connect` |
| `2026-06-28 20:57:23` | `cowrie.client.version` |
| `2026-06-28 20:57:23` | `cowrie.client.kex` |
| `2026-06-28 20:57:24` | `cowrie.login.success` |
| `2026-06-28 20:57:24` | `cowrie.session.params` |
| `2026-06-28 20:57:24` | `cowrie.command.input` |
| `2026-06-28 20:57:25` | `cowrie.log.closed` |
| `2026-06-28 20:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbed3107e349

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 20:57 |
| **Last Seen** | 2026-06-28 20:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:57:24` | `cowrie.session.connect` |
| `2026-06-28 20:57:26` | `cowrie.client.version` |
| `2026-06-28 20:57:26` | `cowrie.client.kex` |
| `2026-06-28 20:57:31` | `cowrie.login.success` |
| `2026-06-28 20:57:35` | `cowrie.session.params` |
| `2026-06-28 20:57:35` | `cowrie.command.input` |
| `2026-06-28 20:57:37` | `cowrie.log.closed` |
| `2026-06-28 20:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e78dd4b9ef66

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:58 |
| **Last Seen** | 2026-06-28 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:58:13` | `cowrie.session.connect` |
| `2026-06-28 20:58:13` | `cowrie.client.version` |
| `2026-06-28 20:58:14` | `cowrie.client.kex` |
| `2026-06-28 20:58:14` | `cowrie.login.success` |
| `2026-06-28 20:58:15` | `cowrie.session.params` |
| `2026-06-28 20:58:15` | `cowrie.command.input` |
| `2026-06-28 20:58:15` | `cowrie.log.closed` |
| `2026-06-28 20:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413790d4f5ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:59 |
| **Last Seen** | 2026-06-28 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:59:03` | `cowrie.session.connect` |
| `2026-06-28 20:59:03` | `cowrie.client.version` |
| `2026-06-28 20:59:03` | `cowrie.client.kex` |
| `2026-06-28 20:59:03` | `cowrie.login.success` |
| `2026-06-28 20:59:04` | `cowrie.session.params` |
| `2026-06-28 20:59:04` | `cowrie.command.input` |
| `2026-06-28 20:59:04` | `cowrie.log.closed` |
| `2026-06-28 20:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360130bb1212

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:59 |
| **Last Seen** | 2026-06-28 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:59:53` | `cowrie.session.connect` |
| `2026-06-28 20:59:53` | `cowrie.client.version` |
| `2026-06-28 20:59:53` | `cowrie.client.kex` |
| `2026-06-28 20:59:53` | `cowrie.login.success` |
| `2026-06-28 20:59:54` | `cowrie.session.params` |
| `2026-06-28 20:59:54` | `cowrie.command.input` |
| `2026-06-28 20:59:54` | `cowrie.log.closed` |
| `2026-06-28 20:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59d5f1e167e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:00 |
| **Last Seen** | 2026-06-28 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:00:44` | `cowrie.session.connect` |
| `2026-06-28 21:00:44` | `cowrie.client.version` |
| `2026-06-28 21:00:44` | `cowrie.client.kex` |
| `2026-06-28 21:00:45` | `cowrie.login.success` |
| `2026-06-28 21:00:46` | `cowrie.session.params` |
| `2026-06-28 21:00:46` | `cowrie.command.input` |
| `2026-06-28 21:00:46` | `cowrie.log.closed` |
| `2026-06-28 21:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1de948a5849

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:01 |
| **Last Seen** | 2026-06-28 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:01:36` | `cowrie.session.connect` |
| `2026-06-28 21:01:36` | `cowrie.client.version` |
| `2026-06-28 21:01:36` | `cowrie.client.kex` |
| `2026-06-28 21:01:37` | `cowrie.login.success` |
| `2026-06-28 21:01:38` | `cowrie.session.params` |
| `2026-06-28 21:01:38` | `cowrie.command.input` |
| `2026-06-28 21:01:38` | `cowrie.log.closed` |
| `2026-06-28 21:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2326a1f7269b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:02 |
| **Last Seen** | 2026-06-28 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:02:28` | `cowrie.session.connect` |
| `2026-06-28 21:02:28` | `cowrie.client.version` |
| `2026-06-28 21:02:29` | `cowrie.client.kex` |
| `2026-06-28 21:02:29` | `cowrie.login.success` |
| `2026-06-28 21:02:30` | `cowrie.session.params` |
| `2026-06-28 21:02:30` | `cowrie.command.input` |
| `2026-06-28 21:02:30` | `cowrie.log.closed` |
| `2026-06-28 21:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510e604f33ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:03 |
| **Last Seen** | 2026-06-28 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:03:20` | `cowrie.session.connect` |
| `2026-06-28 21:03:20` | `cowrie.client.version` |
| `2026-06-28 21:03:20` | `cowrie.client.kex` |
| `2026-06-28 21:03:21` | `cowrie.login.success` |
| `2026-06-28 21:03:22` | `cowrie.session.params` |
| `2026-06-28 21:03:22` | `cowrie.command.input` |
| `2026-06-28 21:03:22` | `cowrie.log.closed` |
| `2026-06-28 21:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be13c0cfd1f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-28 21:03 |
| **Last Seen** | 2026-06-28 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:03:59` | `cowrie.session.connect` |
| `2026-06-28 21:03:59` | `cowrie.client.version` |
| `2026-06-28 21:04:00` | `cowrie.client.kex` |
| `2026-06-28 21:04:00` | `cowrie.login.success` |
| `2026-06-28 21:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96fba6983a20

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-28 21:04 |
| **Last Seen** | 2026-06-28 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:04:00` | `cowrie.session.connect` |
| `2026-06-28 21:04:00` | `cowrie.client.version` |
| `2026-06-28 21:04:00` | `cowrie.client.kex` |
| `2026-06-28 21:04:01` | `cowrie.login.success` |
| `2026-06-28 21:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566268ff62b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:04 |
| **Last Seen** | 2026-06-28 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:04:12` | `cowrie.session.connect` |
| `2026-06-28 21:04:12` | `cowrie.client.version` |
| `2026-06-28 21:04:13` | `cowrie.client.kex` |
| `2026-06-28 21:04:13` | `cowrie.login.success` |
| `2026-06-28 21:04:13` | `cowrie.session.params` |
| `2026-06-28 21:04:13` | `cowrie.command.input` |
| `2026-06-28 21:04:14` | `cowrie.log.closed` |
| `2026-06-28 21:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de13c6acc04a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:05 |
| **Last Seen** | 2026-06-28 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:05:04` | `cowrie.session.connect` |
| `2026-06-28 21:05:04` | `cowrie.client.version` |
| `2026-06-28 21:05:04` | `cowrie.client.kex` |
| `2026-06-28 21:05:04` | `cowrie.login.success` |
| `2026-06-28 21:05:05` | `cowrie.session.params` |
| `2026-06-28 21:05:05` | `cowrie.command.input` |
| `2026-06-28 21:05:05` | `cowrie.log.closed` |
| `2026-06-28 21:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be74b301ff83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:05 |
| **Last Seen** | 2026-06-28 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:05:56` | `cowrie.session.connect` |
| `2026-06-28 21:05:56` | `cowrie.client.version` |
| `2026-06-28 21:05:56` | `cowrie.client.kex` |
| `2026-06-28 21:05:56` | `cowrie.login.success` |
| `2026-06-28 21:05:57` | `cowrie.session.params` |
| `2026-06-28 21:05:57` | `cowrie.command.input` |
| `2026-06-28 21:05:57` | `cowrie.log.closed` |
| `2026-06-28 21:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e55e1c5ef2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:06 |
| **Last Seen** | 2026-06-28 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:06:49` | `cowrie.session.connect` |
| `2026-06-28 21:06:49` | `cowrie.client.version` |
| `2026-06-28 21:06:49` | `cowrie.client.kex` |
| `2026-06-28 21:06:49` | `cowrie.login.success` |
| `2026-06-28 21:06:50` | `cowrie.session.params` |
| `2026-06-28 21:06:50` | `cowrie.command.input` |
| `2026-06-28 21:06:50` | `cowrie.log.closed` |
| `2026-06-28 21:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5642f8e1bd7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:07 |
| **Last Seen** | 2026-06-28 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:07:42` | `cowrie.session.connect` |
| `2026-06-28 21:07:42` | `cowrie.client.version` |
| `2026-06-28 21:07:42` | `cowrie.client.kex` |
| `2026-06-28 21:07:42` | `cowrie.login.success` |
| `2026-06-28 21:07:43` | `cowrie.session.params` |
| `2026-06-28 21:07:43` | `cowrie.command.input` |
| `2026-06-28 21:07:43` | `cowrie.log.closed` |
| `2026-06-28 21:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db64d3d4a33

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 21:08 |
| **Last Seen** | 2026-06-28 21:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:08:18` | `cowrie.session.connect` |
| `2026-06-28 21:08:18` | `cowrie.client.version` |
| `2026-06-28 21:08:18` | `cowrie.client.kex` |
| `2026-06-28 21:08:21` | `cowrie.login.success` |
| `2026-06-28 21:08:22` | `cowrie.session.params` |
| `2026-06-28 21:08:22` | `cowrie.command.input` |
| `2026-06-28 21:08:22` | `cowrie.log.closed` |
| `2026-06-28 21:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb731bfcca0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:08 |
| **Last Seen** | 2026-06-28 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:08:36` | `cowrie.session.connect` |
| `2026-06-28 21:08:36` | `cowrie.client.version` |
| `2026-06-28 21:08:36` | `cowrie.client.kex` |
| `2026-06-28 21:08:36` | `cowrie.login.success` |
| `2026-06-28 21:08:37` | `cowrie.session.params` |
| `2026-06-28 21:08:37` | `cowrie.command.input` |
| `2026-06-28 21:08:37` | `cowrie.log.closed` |
| `2026-06-28 21:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fac33b2ec31

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 21:08 |
| **Last Seen** | 2026-06-28 21:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:08:58` | `cowrie.session.connect` |
| `2026-06-28 21:09:00` | `cowrie.client.version` |
| `2026-06-28 21:09:00` | `cowrie.client.kex` |
| `2026-06-28 21:09:05` | `cowrie.login.success` |
| `2026-06-28 21:09:09` | `cowrie.session.params` |
| `2026-06-28 21:09:09` | `cowrie.command.input` |
| `2026-06-28 21:09:10` | `cowrie.log.closed` |
| `2026-06-28 21:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed37fcce8e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:09 |
| **Last Seen** | 2026-06-28 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:09:29` | `cowrie.session.connect` |
| `2026-06-28 21:09:29` | `cowrie.client.version` |
| `2026-06-28 21:09:30` | `cowrie.client.kex` |
| `2026-06-28 21:09:30` | `cowrie.login.success` |
| `2026-06-28 21:09:30` | `cowrie.session.params` |
| `2026-06-28 21:09:30` | `cowrie.command.input` |
| `2026-06-28 21:09:31` | `cowrie.log.closed` |
| `2026-06-28 21:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0912dd060b39

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:10 |
| **Last Seen** | 2026-06-28 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:10:22` | `cowrie.session.connect` |
| `2026-06-28 21:10:22` | `cowrie.client.version` |
| `2026-06-28 21:10:22` | `cowrie.client.kex` |
| `2026-06-28 21:10:23` | `cowrie.login.success` |
| `2026-06-28 21:10:24` | `cowrie.session.params` |
| `2026-06-28 21:10:24` | `cowrie.command.input` |
| `2026-06-28 21:10:24` | `cowrie.log.closed` |
| `2026-06-28 21:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49db9aa9a425

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:11 |
| **Last Seen** | 2026-06-28 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:11:16` | `cowrie.session.connect` |
| `2026-06-28 21:11:16` | `cowrie.client.version` |
| `2026-06-28 21:11:16` | `cowrie.client.kex` |
| `2026-06-28 21:11:16` | `cowrie.login.success` |
| `2026-06-28 21:11:17` | `cowrie.session.params` |
| `2026-06-28 21:11:17` | `cowrie.command.input` |
| `2026-06-28 21:11:17` | `cowrie.log.closed` |
| `2026-06-28 21:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071aa83c06f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:12 |
| **Last Seen** | 2026-06-28 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:12:10` | `cowrie.session.connect` |
| `2026-06-28 21:12:10` | `cowrie.client.version` |
| `2026-06-28 21:12:10` | `cowrie.client.kex` |
| `2026-06-28 21:12:10` | `cowrie.login.success` |
| `2026-06-28 21:12:11` | `cowrie.session.params` |
| `2026-06-28 21:12:11` | `cowrie.command.input` |
| `2026-06-28 21:12:11` | `cowrie.log.closed` |
| `2026-06-28 21:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90245aa8d6ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:13 |
| **Last Seen** | 2026-06-28 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:13:05` | `cowrie.session.connect` |
| `2026-06-28 21:13:05` | `cowrie.client.version` |
| `2026-06-28 21:13:05` | `cowrie.client.kex` |
| `2026-06-28 21:13:05` | `cowrie.login.success` |
| `2026-06-28 21:13:06` | `cowrie.session.params` |
| `2026-06-28 21:13:06` | `cowrie.command.input` |
| `2026-06-28 21:13:06` | `cowrie.log.closed` |
| `2026-06-28 21:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8754d338d6d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:14 |
| **Last Seen** | 2026-06-28 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:14:01` | `cowrie.session.connect` |
| `2026-06-28 21:14:01` | `cowrie.client.version` |
| `2026-06-28 21:14:01` | `cowrie.client.kex` |
| `2026-06-28 21:14:02` | `cowrie.login.success` |
| `2026-06-28 21:14:02` | `cowrie.session.params` |
| `2026-06-28 21:14:02` | `cowrie.command.input` |
| `2026-06-28 21:14:03` | `cowrie.log.closed` |
| `2026-06-28 21:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149ee9d28505

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:14 |
| **Last Seen** | 2026-06-28 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:14:59` | `cowrie.session.connect` |
| `2026-06-28 21:14:59` | `cowrie.client.version` |
| `2026-06-28 21:14:59` | `cowrie.client.kex` |
| `2026-06-28 21:14:59` | `cowrie.login.success` |
| `2026-06-28 21:15:00` | `cowrie.session.params` |
| `2026-06-28 21:15:00` | `cowrie.command.input` |
| `2026-06-28 21:15:00` | `cowrie.log.closed` |
| `2026-06-28 21:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cee8c2054e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:15 |
| **Last Seen** | 2026-06-28 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:15:55` | `cowrie.session.connect` |
| `2026-06-28 21:15:55` | `cowrie.client.version` |
| `2026-06-28 21:15:55` | `cowrie.client.kex` |
| `2026-06-28 21:15:55` | `cowrie.login.success` |
| `2026-06-28 21:15:56` | `cowrie.session.params` |
| `2026-06-28 21:15:56` | `cowrie.command.input` |
| `2026-06-28 21:15:56` | `cowrie.log.closed` |
| `2026-06-28 21:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1cdd382d3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:16 |
| **Last Seen** | 2026-06-28 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:16:52` | `cowrie.session.connect` |
| `2026-06-28 21:16:52` | `cowrie.client.version` |
| `2026-06-28 21:16:52` | `cowrie.client.kex` |
| `2026-06-28 21:16:52` | `cowrie.login.success` |
| `2026-06-28 21:16:53` | `cowrie.session.params` |
| `2026-06-28 21:16:53` | `cowrie.command.input` |
| `2026-06-28 21:16:53` | `cowrie.log.closed` |
| `2026-06-28 21:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54c96020091

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:17 |
| **Last Seen** | 2026-06-28 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:17:45` | `cowrie.session.connect` |
| `2026-06-28 21:17:45` | `cowrie.client.version` |
| `2026-06-28 21:17:46` | `cowrie.client.kex` |
| `2026-06-28 21:17:46` | `cowrie.login.success` |
| `2026-06-28 21:17:47` | `cowrie.session.params` |
| `2026-06-28 21:17:47` | `cowrie.command.input` |
| `2026-06-28 21:17:47` | `cowrie.log.closed` |
| `2026-06-28 21:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bbc30d4ffd9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:17 |
| **Last Seen** | 2026-06-28 21:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:17:46` | `cowrie.session.connect` |
| `2026-06-28 21:17:47` | `cowrie.client.version` |
| `2026-06-28 21:17:47` | `cowrie.client.kex` |
| `2026-06-28 21:17:49` | `cowrie.login.success` |
| `2026-06-28 21:17:49` | `cowrie.session.params` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.success` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:49` | `cowrie.command.input` |
| `2026-06-28 21:17:50` | `cowrie.log.closed` |
| `2026-06-28 21:17:52` | `cowrie.session.params` |
| `2026-06-28 21:17:52` | `cowrie.command.input` |
| `2026-06-28 21:17:52` | `cowrie.command.input` |
| `2026-06-28 21:17:52` | `cowrie.command.success` |
| `2026-06-28 21:17:52` | `cowrie.log.closed` |
| `2026-06-28 21:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d37668881754

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:18 |
| **Last Seen** | 2026-06-28 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:18:39` | `cowrie.session.connect` |
| `2026-06-28 21:18:39` | `cowrie.client.version` |
| `2026-06-28 21:18:39` | `cowrie.client.kex` |
| `2026-06-28 21:18:39` | `cowrie.login.success` |
| `2026-06-28 21:18:40` | `cowrie.session.params` |
| `2026-06-28 21:18:40` | `cowrie.command.input` |
| `2026-06-28 21:18:40` | `cowrie.log.closed` |
| `2026-06-28 21:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dec6c818062

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:19 |
| **Last Seen** | 2026-06-28 21:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:19:11` | `cowrie.session.connect` |
| `2026-06-28 21:19:11` | `cowrie.client.version` |
| `2026-06-28 21:19:11` | `cowrie.client.kex` |
| `2026-06-28 21:19:13` | `cowrie.login.success` |
| `2026-06-28 21:19:14` | `cowrie.session.params` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.success` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.command.input` |
| `2026-06-28 21:19:14` | `cowrie.log.closed` |
| `2026-06-28 21:19:16` | `cowrie.session.params` |
| `2026-06-28 21:19:16` | `cowrie.command.input` |
| `2026-06-28 21:19:16` | `cowrie.command.input` |
| `2026-06-28 21:19:16` | `cowrie.command.success` |
| `2026-06-28 21:19:17` | `cowrie.log.closed` |
| `2026-06-28 21:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab272e9a6a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:19 |
| **Last Seen** | 2026-06-28 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:19:33` | `cowrie.session.connect` |
| `2026-06-28 21:19:34` | `cowrie.client.version` |
| `2026-06-28 21:19:34` | `cowrie.client.kex` |
| `2026-06-28 21:19:34` | `cowrie.login.success` |
| `2026-06-28 21:19:35` | `cowrie.session.params` |
| `2026-06-28 21:19:35` | `cowrie.command.input` |
| `2026-06-28 21:19:35` | `cowrie.log.closed` |
| `2026-06-28 21:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168097c7b158

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 21:20 |
| **Last Seen** | 2026-06-28 21:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:20:27` | `cowrie.session.connect` |
| `2026-06-28 21:20:28` | `cowrie.client.version` |
| `2026-06-28 21:20:28` | `cowrie.client.kex` |
| `2026-06-28 21:20:35` | `cowrie.login.success` |
| `2026-06-28 21:20:39` | `cowrie.session.params` |
| `2026-06-28 21:20:39` | `cowrie.command.input` |
| `2026-06-28 21:20:40` | `cowrie.log.closed` |
| `2026-06-28 21:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f72f61ee6cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:20 |
| **Last Seen** | 2026-06-28 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:20:29` | `cowrie.session.connect` |
| `2026-06-28 21:20:29` | `cowrie.client.version` |
| `2026-06-28 21:20:29` | `cowrie.client.kex` |
| `2026-06-28 21:20:30` | `cowrie.login.success` |
| `2026-06-28 21:20:30` | `cowrie.session.params` |
| `2026-06-28 21:20:30` | `cowrie.command.input` |
| `2026-06-28 21:20:31` | `cowrie.log.closed` |
| `2026-06-28 21:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4ef411dc3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:20 |
| **Last Seen** | 2026-06-28 21:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:20:39` | `cowrie.session.connect` |
| `2026-06-28 21:20:39` | `cowrie.client.version` |
| `2026-06-28 21:20:39` | `cowrie.client.kex` |
| `2026-06-28 21:20:40` | `cowrie.login.success` |
| `2026-06-28 21:20:41` | `cowrie.session.params` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.success` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:41` | `cowrie.command.input` |
| `2026-06-28 21:20:42` | `cowrie.log.closed` |
| `2026-06-28 21:20:43` | `cowrie.session.params` |
| `2026-06-28 21:20:43` | `cowrie.command.input` |
| `2026-06-28 21:20:43` | `cowrie.command.input` |
| `2026-06-28 21:20:43` | `cowrie.command.success` |
| `2026-06-28 21:20:44` | `cowrie.log.closed` |
| `2026-06-28 21:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99c693f8e3f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:21 |
| **Last Seen** | 2026-06-28 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:21:26` | `cowrie.session.connect` |
| `2026-06-28 21:21:26` | `cowrie.client.version` |
| `2026-06-28 21:21:26` | `cowrie.client.kex` |
| `2026-06-28 21:21:27` | `cowrie.login.success` |
| `2026-06-28 21:21:27` | `cowrie.session.params` |
| `2026-06-28 21:21:27` | `cowrie.command.input` |
| `2026-06-28 21:21:28` | `cowrie.log.closed` |
| `2026-06-28 21:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349c63bbc1a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:22 |
| **Last Seen** | 2026-06-28 21:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:22:02` | `cowrie.session.connect` |
| `2026-06-28 21:22:02` | `cowrie.client.version` |
| `2026-06-28 21:22:02` | `cowrie.client.kex` |
| `2026-06-28 21:22:04` | `cowrie.login.success` |
| `2026-06-28 21:22:04` | `cowrie.session.params` |
| `2026-06-28 21:22:04` | `cowrie.command.input` |
| `2026-06-28 21:22:04` | `cowrie.command.input` |
| `2026-06-28 21:22:04` | `cowrie.command.input` |
| `2026-06-28 21:22:04` | `cowrie.command.input` |
| `2026-06-28 21:22:04` | `cowrie.command.input` |
| `2026-06-28 21:22:04` | `cowrie.command.success` |
| `2026-06-28 21:22:04` | `cowrie.command.input` |
| `2026-06-28 21:22:04` | `cowrie.command.input` |
| `2026-06-28 21:22:05` | `cowrie.command.input` |
| `2026-06-28 21:22:05` | `cowrie.command.input` |
| `2026-06-28 21:22:05` | `cowrie.log.closed` |
| `2026-06-28 21:22:07` | `cowrie.session.params` |
| `2026-06-28 21:22:07` | `cowrie.command.input` |
| `2026-06-28 21:22:07` | `cowrie.command.input` |
| `2026-06-28 21:22:07` | `cowrie.command.success` |
| `2026-06-28 21:22:07` | `cowrie.log.closed` |
| `2026-06-28 21:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa8932da37c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:22 |
| **Last Seen** | 2026-06-28 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:22:23` | `cowrie.session.connect` |
| `2026-06-28 21:22:23` | `cowrie.client.version` |
| `2026-06-28 21:22:23` | `cowrie.client.kex` |
| `2026-06-28 21:22:23` | `cowrie.login.success` |
| `2026-06-28 21:22:24` | `cowrie.session.params` |
| `2026-06-28 21:22:24` | `cowrie.command.input` |
| `2026-06-28 21:22:24` | `cowrie.log.closed` |
| `2026-06-28 21:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2817f6d0c74

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 21:23 |
| **Last Seen** | 2026-06-28 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:23:06` | `cowrie.session.connect` |
| `2026-06-28 21:23:07` | `cowrie.client.version` |
| `2026-06-28 21:23:07` | `cowrie.client.kex` |
| `2026-06-28 21:23:09` | `cowrie.login.success` |
| `2026-06-28 21:23:10` | `cowrie.session.params` |
| `2026-06-28 21:23:10` | `cowrie.command.input` |
| `2026-06-28 21:23:11` | `cowrie.log.closed` |
| `2026-06-28 21:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe2098772c5d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:23 |
| **Last Seen** | 2026-06-28 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:23:18` | `cowrie.session.connect` |
| `2026-06-28 21:23:18` | `cowrie.client.version` |
| `2026-06-28 21:23:19` | `cowrie.client.kex` |
| `2026-06-28 21:23:19` | `cowrie.login.success` |
| `2026-06-28 21:23:20` | `cowrie.session.params` |
| `2026-06-28 21:23:20` | `cowrie.command.input` |
| `2026-06-28 21:23:20` | `cowrie.log.closed` |
| `2026-06-28 21:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6306dae37a6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:24 |
| **Last Seen** | 2026-06-28 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:24:13` | `cowrie.session.connect` |
| `2026-06-28 21:24:13` | `cowrie.client.version` |
| `2026-06-28 21:24:14` | `cowrie.client.kex` |
| `2026-06-28 21:24:14` | `cowrie.login.success` |
| `2026-06-28 21:24:14` | `cowrie.session.params` |
| `2026-06-28 21:24:15` | `cowrie.command.input` |
| `2026-06-28 21:24:15` | `cowrie.log.closed` |
| `2026-06-28 21:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4843ca862e54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:24 |
| **Last Seen** | 2026-06-28 21:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:24:40` | `cowrie.session.connect` |
| `2026-06-28 21:24:41` | `cowrie.client.version` |
| `2026-06-28 21:24:41` | `cowrie.client.kex` |
| `2026-06-28 21:24:42` | `cowrie.login.success` |
| `2026-06-28 21:24:43` | `cowrie.session.params` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.success` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:43` | `cowrie.command.input` |
| `2026-06-28 21:24:44` | `cowrie.log.closed` |
| `2026-06-28 21:24:46` | `cowrie.session.params` |
| `2026-06-28 21:24:46` | `cowrie.command.input` |
| `2026-06-28 21:24:46` | `cowrie.command.input` |
| `2026-06-28 21:24:46` | `cowrie.command.success` |
| `2026-06-28 21:24:46` | `cowrie.log.closed` |
| `2026-06-28 21:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e5cdc1ad0e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:25 |
| **Last Seen** | 2026-06-28 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:25:09` | `cowrie.session.connect` |
| `2026-06-28 21:25:09` | `cowrie.client.version` |
| `2026-06-28 21:25:09` | `cowrie.client.kex` |
| `2026-06-28 21:25:10` | `cowrie.login.success` |
| `2026-06-28 21:25:10` | `cowrie.session.params` |
| `2026-06-28 21:25:10` | `cowrie.command.input` |
| `2026-06-28 21:25:11` | `cowrie.log.closed` |
| `2026-06-28 21:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f13dc80dcc2

| Field | Detail |
|---|---|
| **Source IP** | `185.220.101[.]188` |
| **First Seen** | 2026-06-28 21:25 |
| **Last Seen** | 2026-06-28 21:26 |
| **Session Duration** | 20s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:25:44` | `cowrie.session.connect` |
| `2026-06-28 21:25:44` | `cowrie.client.version` |
| `2026-06-28 21:25:44` | `cowrie.client.kex` |
| `2026-06-28 21:25:44` | `cowrie.client.fingerprint` |
| `2026-06-28 21:25:44` | `cowrie.login.failed` |
| `2026-06-28 21:25:45` | `cowrie.login.success` |
| `2026-06-28 21:26:03` | `cowrie.direct-tcpip.request` |
| `2026-06-28 21:26:04` | `cowrie.direct-tcpip.ja4` |
| `2026-06-28 21:26:04` | `cowrie.direct-tcpip.data` |
| `2026-06-28 21:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.101[.]188` to AbuseIPDB if not already reported
- [ ] Block `185.220.101[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5f14fab750f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:25 |
| **Last Seen** | 2026-06-28 21:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:25:56` | `cowrie.session.connect` |
| `2026-06-28 21:25:56` | `cowrie.client.version` |
| `2026-06-28 21:25:56` | `cowrie.client.kex` |
| `2026-06-28 21:25:57` | `cowrie.login.success` |
| `2026-06-28 21:25:58` | `cowrie.session.params` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.success` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:58` | `cowrie.command.input` |
| `2026-06-28 21:25:59` | `cowrie.log.closed` |
| `2026-06-28 21:26:00` | `cowrie.session.params` |
| `2026-06-28 21:26:00` | `cowrie.command.input` |
| `2026-06-28 21:26:00` | `cowrie.command.input` |
| `2026-06-28 21:26:00` | `cowrie.command.success` |
| `2026-06-28 21:26:00` | `cowrie.log.closed` |
| `2026-06-28 21:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf527c8e93b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:26 |
| **Last Seen** | 2026-06-28 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:26:07` | `cowrie.session.connect` |
| `2026-06-28 21:26:07` | `cowrie.client.version` |
| `2026-06-28 21:26:07` | `cowrie.client.kex` |
| `2026-06-28 21:26:07` | `cowrie.login.success` |
| `2026-06-28 21:26:08` | `cowrie.session.params` |
| `2026-06-28 21:26:08` | `cowrie.command.input` |
| `2026-06-28 21:26:08` | `cowrie.log.closed` |
| `2026-06-28 21:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdab31ac1e83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:27 |
| **Last Seen** | 2026-06-28 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:27:04` | `cowrie.session.connect` |
| `2026-06-28 21:27:04` | `cowrie.client.version` |
| `2026-06-28 21:27:04` | `cowrie.client.kex` |
| `2026-06-28 21:27:05` | `cowrie.login.success` |
| `2026-06-28 21:27:05` | `cowrie.session.params` |
| `2026-06-28 21:27:05` | `cowrie.command.input` |
| `2026-06-28 21:27:06` | `cowrie.log.closed` |
| `2026-06-28 21:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66d196580162

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:27 |
| **Last Seen** | 2026-06-28 21:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:27:12` | `cowrie.session.connect` |
| `2026-06-28 21:27:12` | `cowrie.client.version` |
| `2026-06-28 21:27:12` | `cowrie.client.kex` |
| `2026-06-28 21:27:14` | `cowrie.login.success` |
| `2026-06-28 21:27:15` | `cowrie.session.params` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.success` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.command.input` |
| `2026-06-28 21:27:15` | `cowrie.log.closed` |
| `2026-06-28 21:27:17` | `cowrie.session.params` |
| `2026-06-28 21:27:17` | `cowrie.command.input` |
| `2026-06-28 21:27:17` | `cowrie.command.input` |
| `2026-06-28 21:27:17` | `cowrie.command.success` |
| `2026-06-28 21:27:17` | `cowrie.log.closed` |
| `2026-06-28 21:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c296cf586f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:28 |
| **Last Seen** | 2026-06-28 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:28:02` | `cowrie.session.connect` |
| `2026-06-28 21:28:02` | `cowrie.client.version` |
| `2026-06-28 21:28:02` | `cowrie.client.kex` |
| `2026-06-28 21:28:02` | `cowrie.login.success` |
| `2026-06-28 21:28:03` | `cowrie.session.params` |
| `2026-06-28 21:28:03` | `cowrie.command.input` |
| `2026-06-28 21:28:03` | `cowrie.log.closed` |
| `2026-06-28 21:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7944b04b79f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:28 |
| **Last Seen** | 2026-06-28 21:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:28:32` | `cowrie.session.connect` |
| `2026-06-28 21:28:32` | `cowrie.client.version` |
| `2026-06-28 21:28:32` | `cowrie.client.kex` |
| `2026-06-28 21:28:34` | `cowrie.login.success` |
| `2026-06-28 21:28:35` | `cowrie.session.params` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.success` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.command.input` |
| `2026-06-28 21:28:35` | `cowrie.log.closed` |
| `2026-06-28 21:28:36` | `cowrie.session.params` |
| `2026-06-28 21:28:36` | `cowrie.command.input` |
| `2026-06-28 21:28:36` | `cowrie.command.input` |
| `2026-06-28 21:28:36` | `cowrie.command.success` |
| `2026-06-28 21:28:37` | `cowrie.log.closed` |
| `2026-06-28 21:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66fcfbb44f56

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:28 |
| **Last Seen** | 2026-06-28 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:28:59` | `cowrie.session.connect` |
| `2026-06-28 21:28:59` | `cowrie.client.version` |
| `2026-06-28 21:28:59` | `cowrie.client.kex` |
| `2026-06-28 21:29:00` | `cowrie.login.success` |
| `2026-06-28 21:29:01` | `cowrie.session.params` |
| `2026-06-28 21:29:01` | `cowrie.command.input` |
| `2026-06-28 21:29:01` | `cowrie.log.closed` |
| `2026-06-28 21:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5549e5e6646a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:29 |
| **Last Seen** | 2026-06-28 21:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:29:51` | `cowrie.session.connect` |
| `2026-06-28 21:29:51` | `cowrie.client.version` |
| `2026-06-28 21:29:51` | `cowrie.client.kex` |
| `2026-06-28 21:29:52` | `cowrie.login.success` |
| `2026-06-28 21:29:53` | `cowrie.session.params` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.success` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:53` | `cowrie.command.input` |
| `2026-06-28 21:29:54` | `cowrie.log.closed` |
| `2026-06-28 21:29:55` | `cowrie.session.params` |
| `2026-06-28 21:29:55` | `cowrie.command.input` |
| `2026-06-28 21:29:55` | `cowrie.command.input` |
| `2026-06-28 21:29:55` | `cowrie.command.success` |
| `2026-06-28 21:29:56` | `cowrie.log.closed` |
| `2026-06-28 21:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45aa702b9141

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:29 |
| **Last Seen** | 2026-06-28 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:29:56` | `cowrie.session.connect` |
| `2026-06-28 21:29:56` | `cowrie.client.version` |
| `2026-06-28 21:29:56` | `cowrie.client.kex` |
| `2026-06-28 21:29:56` | `cowrie.login.success` |
| `2026-06-28 21:29:57` | `cowrie.session.params` |
| `2026-06-28 21:29:57` | `cowrie.command.input` |
| `2026-06-28 21:29:57` | `cowrie.log.closed` |
| `2026-06-28 21:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb38c598500

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:30 |
| **Last Seen** | 2026-06-28 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:30:52` | `cowrie.session.connect` |
| `2026-06-28 21:30:52` | `cowrie.client.version` |
| `2026-06-28 21:30:52` | `cowrie.client.kex` |
| `2026-06-28 21:30:52` | `cowrie.login.success` |
| `2026-06-28 21:30:53` | `cowrie.session.params` |
| `2026-06-28 21:30:53` | `cowrie.command.input` |
| `2026-06-28 21:30:53` | `cowrie.log.closed` |
| `2026-06-28 21:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c33b074746

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:31 |
| **Last Seen** | 2026-06-28 21:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:31:08` | `cowrie.session.connect` |
| `2026-06-28 21:31:08` | `cowrie.client.version` |
| `2026-06-28 21:31:08` | `cowrie.client.kex` |
| `2026-06-28 21:31:09` | `cowrie.login.success` |
| `2026-06-28 21:31:11` | `cowrie.session.params` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.success` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.command.input` |
| `2026-06-28 21:31:11` | `cowrie.log.closed` |
| `2026-06-28 21:31:12` | `cowrie.session.params` |
| `2026-06-28 21:31:12` | `cowrie.command.input` |
| `2026-06-28 21:31:12` | `cowrie.command.input` |
| `2026-06-28 21:31:12` | `cowrie.command.success` |
| `2026-06-28 21:31:13` | `cowrie.log.closed` |
| `2026-06-28 21:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e11f9dc3306

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:31 |
| **Last Seen** | 2026-06-28 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:31:49` | `cowrie.session.connect` |
| `2026-06-28 21:31:49` | `cowrie.client.version` |
| `2026-06-28 21:31:49` | `cowrie.client.kex` |
| `2026-06-28 21:31:50` | `cowrie.login.success` |
| `2026-06-28 21:31:50` | `cowrie.session.params` |
| `2026-06-28 21:31:50` | `cowrie.command.input` |
| `2026-06-28 21:31:51` | `cowrie.log.closed` |
| `2026-06-28 21:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec2b43d708a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 21:31 |
| **Last Seen** | 2026-06-28 21:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:31:56` | `cowrie.session.connect` |
| `2026-06-28 21:31:58` | `cowrie.client.version` |
| `2026-06-28 21:31:58` | `cowrie.client.kex` |
| `2026-06-28 21:32:05` | `cowrie.login.success` |
| `2026-06-28 21:32:08` | `cowrie.session.params` |
| `2026-06-28 21:32:08` | `cowrie.command.input` |
| `2026-06-28 21:32:10` | `cowrie.log.closed` |
| `2026-06-28 21:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01bf1438baff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:32 |
| **Last Seen** | 2026-06-28 21:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:32:28` | `cowrie.session.connect` |
| `2026-06-28 21:32:28` | `cowrie.client.version` |
| `2026-06-28 21:32:28` | `cowrie.client.kex` |
| `2026-06-28 21:32:30` | `cowrie.login.success` |
| `2026-06-28 21:32:31` | `cowrie.session.params` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.success` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.command.input` |
| `2026-06-28 21:32:31` | `cowrie.log.closed` |
| `2026-06-28 21:32:33` | `cowrie.session.params` |
| `2026-06-28 21:32:33` | `cowrie.command.input` |
| `2026-06-28 21:32:33` | `cowrie.command.input` |
| `2026-06-28 21:32:33` | `cowrie.command.success` |
| `2026-06-28 21:32:33` | `cowrie.log.closed` |
| `2026-06-28 21:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd9747f490f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:32 |
| **Last Seen** | 2026-06-28 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:32:47` | `cowrie.session.connect` |
| `2026-06-28 21:32:47` | `cowrie.client.version` |
| `2026-06-28 21:32:47` | `cowrie.client.kex` |
| `2026-06-28 21:32:47` | `cowrie.login.success` |
| `2026-06-28 21:32:48` | `cowrie.session.params` |
| `2026-06-28 21:32:48` | `cowrie.command.input` |
| `2026-06-28 21:32:48` | `cowrie.log.closed` |
| `2026-06-28 21:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceda7701517a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:33 |
| **Last Seen** | 2026-06-28 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:33:46` | `cowrie.session.connect` |
| `2026-06-28 21:33:46` | `cowrie.client.version` |
| `2026-06-28 21:33:46` | `cowrie.client.kex` |
| `2026-06-28 21:33:46` | `cowrie.login.success` |
| `2026-06-28 21:33:47` | `cowrie.session.params` |
| `2026-06-28 21:33:47` | `cowrie.command.input` |
| `2026-06-28 21:33:47` | `cowrie.log.closed` |
| `2026-06-28 21:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a204ecb062

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:33 |
| **Last Seen** | 2026-06-28 21:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:33:59` | `cowrie.session.connect` |
| `2026-06-28 21:33:59` | `cowrie.client.version` |
| `2026-06-28 21:33:59` | `cowrie.client.kex` |
| `2026-06-28 21:34:00` | `cowrie.login.success` |
| `2026-06-28 21:34:01` | `cowrie.session.params` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.success` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.command.input` |
| `2026-06-28 21:34:01` | `cowrie.log.closed` |
| `2026-06-28 21:34:02` | `cowrie.session.params` |
| `2026-06-28 21:34:02` | `cowrie.command.input` |
| `2026-06-28 21:34:02` | `cowrie.command.input` |
| `2026-06-28 21:34:02` | `cowrie.command.success` |
| `2026-06-28 21:34:02` | `cowrie.log.closed` |
| `2026-06-28 21:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e092a52be8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:34 |
| **Last Seen** | 2026-06-28 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:34:46` | `cowrie.session.connect` |
| `2026-06-28 21:34:46` | `cowrie.client.version` |
| `2026-06-28 21:34:46` | `cowrie.client.kex` |
| `2026-06-28 21:34:46` | `cowrie.login.success` |
| `2026-06-28 21:34:47` | `cowrie.session.params` |
| `2026-06-28 21:34:47` | `cowrie.command.input` |
| `2026-06-28 21:34:47` | `cowrie.log.closed` |
| `2026-06-28 21:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b603e71f4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:35 |
| **Last Seen** | 2026-06-28 21:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:35:28` | `cowrie.session.connect` |
| `2026-06-28 21:35:28` | `cowrie.client.version` |
| `2026-06-28 21:35:28` | `cowrie.client.kex` |
| `2026-06-28 21:35:29` | `cowrie.login.success` |
| `2026-06-28 21:35:30` | `cowrie.session.params` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.success` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.command.input` |
| `2026-06-28 21:35:30` | `cowrie.log.closed` |
| `2026-06-28 21:35:32` | `cowrie.session.params` |
| `2026-06-28 21:35:32` | `cowrie.command.input` |
| `2026-06-28 21:35:32` | `cowrie.command.input` |
| `2026-06-28 21:35:32` | `cowrie.command.success` |
| `2026-06-28 21:35:32` | `cowrie.log.closed` |
| `2026-06-28 21:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e3cb99b3bc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:35 |
| **Last Seen** | 2026-06-28 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:35:45` | `cowrie.session.connect` |
| `2026-06-28 21:35:45` | `cowrie.client.version` |
| `2026-06-28 21:35:45` | `cowrie.client.kex` |
| `2026-06-28 21:35:45` | `cowrie.login.success` |
| `2026-06-28 21:35:46` | `cowrie.session.params` |
| `2026-06-28 21:35:46` | `cowrie.command.input` |
| `2026-06-28 21:35:46` | `cowrie.log.closed` |
| `2026-06-28 21:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e5f67b3b8d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:36 |
| **Last Seen** | 2026-06-28 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:36:42` | `cowrie.session.connect` |
| `2026-06-28 21:36:42` | `cowrie.client.version` |
| `2026-06-28 21:36:42` | `cowrie.client.kex` |
| `2026-06-28 21:36:42` | `cowrie.login.success` |
| `2026-06-28 21:36:43` | `cowrie.session.params` |
| `2026-06-28 21:36:43` | `cowrie.command.input` |
| `2026-06-28 21:36:43` | `cowrie.log.closed` |
| `2026-06-28 21:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861fbc83fc02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:36 |
| **Last Seen** | 2026-06-28 21:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:36:57` | `cowrie.session.connect` |
| `2026-06-28 21:36:57` | `cowrie.client.version` |
| `2026-06-28 21:36:57` | `cowrie.client.kex` |
| `2026-06-28 21:36:58` | `cowrie.login.success` |
| `2026-06-28 21:36:59` | `cowrie.session.params` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.success` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.command.input` |
| `2026-06-28 21:36:59` | `cowrie.log.closed` |
| `2026-06-28 21:37:01` | `cowrie.session.params` |
| `2026-06-28 21:37:01` | `cowrie.command.input` |
| `2026-06-28 21:37:01` | `cowrie.command.input` |
| `2026-06-28 21:37:01` | `cowrie.command.success` |
| `2026-06-28 21:37:01` | `cowrie.log.closed` |
| `2026-06-28 21:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d556f7aaf78e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:37 |
| **Last Seen** | 2026-06-28 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:37:40` | `cowrie.session.connect` |
| `2026-06-28 21:37:40` | `cowrie.client.version` |
| `2026-06-28 21:37:40` | `cowrie.client.kex` |
| `2026-06-28 21:37:40` | `cowrie.login.success` |
| `2026-06-28 21:37:41` | `cowrie.session.params` |
| `2026-06-28 21:37:41` | `cowrie.command.input` |
| `2026-06-28 21:37:41` | `cowrie.log.closed` |
| `2026-06-28 21:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3a5d4702c2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 21:37 |
| **Last Seen** | 2026-06-28 21:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:37:59` | `cowrie.session.connect` |
| `2026-06-28 21:38:00` | `cowrie.client.version` |
| `2026-06-28 21:38:00` | `cowrie.client.kex` |
| `2026-06-28 21:38:02` | `cowrie.login.success` |
| `2026-06-28 21:38:04` | `cowrie.session.params` |
| `2026-06-28 21:38:04` | `cowrie.command.input` |
| `2026-06-28 21:38:05` | `cowrie.log.closed` |
| `2026-06-28 21:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6957895abb03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:38 |
| **Last Seen** | 2026-06-28 21:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:38:39` | `cowrie.session.connect` |
| `2026-06-28 21:38:39` | `cowrie.client.version` |
| `2026-06-28 21:38:39` | `cowrie.client.kex` |
| `2026-06-28 21:38:39` | `cowrie.login.success` |
| `2026-06-28 21:38:40` | `cowrie.session.params` |
| `2026-06-28 21:38:40` | `cowrie.command.input` |
| `2026-06-28 21:38:40` | `cowrie.log.closed` |
| `2026-06-28 21:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbed54c460c9

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-28 21:39 |
| **Last Seen** | 2026-06-28 21:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:39:17` | `cowrie.session.connect` |
| `2026-06-28 21:39:17` | `cowrie.client.version` |
| `2026-06-28 21:39:17` | `cowrie.client.kex` |
| `2026-06-28 21:39:17` | `cowrie.login.success` |
| `2026-06-28 21:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc4209597b6c

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-28 21:39 |
| **Last Seen** | 2026-06-28 21:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:39:21` | `cowrie.session.connect` |
| `2026-06-28 21:39:21` | `cowrie.client.version` |
| `2026-06-28 21:39:21` | `cowrie.client.kex` |
| `2026-06-28 21:39:21` | `cowrie.login.success` |
| `2026-06-28 21:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0a8a755c83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:39 |
| **Last Seen** | 2026-06-28 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:39:39` | `cowrie.session.connect` |
| `2026-06-28 21:39:39` | `cowrie.client.version` |
| `2026-06-28 21:39:39` | `cowrie.client.kex` |
| `2026-06-28 21:39:40` | `cowrie.login.success` |
| `2026-06-28 21:39:40` | `cowrie.session.params` |
| `2026-06-28 21:39:40` | `cowrie.command.input` |
| `2026-06-28 21:39:41` | `cowrie.log.closed` |
| `2026-06-28 21:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1ad2fe204e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:40 |
| **Last Seen** | 2026-06-28 21:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:40:08` | `cowrie.session.connect` |
| `2026-06-28 21:40:08` | `cowrie.client.version` |
| `2026-06-28 21:40:09` | `cowrie.client.kex` |
| `2026-06-28 21:40:09` | `cowrie.login.success` |
| `2026-06-28 21:40:10` | `cowrie.session.params` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.success` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.command.input` |
| `2026-06-28 21:40:10` | `cowrie.log.closed` |
| `2026-06-28 21:40:11` | `cowrie.session.params` |
| `2026-06-28 21:40:11` | `cowrie.command.input` |
| `2026-06-28 21:40:11` | `cowrie.command.input` |
| `2026-06-28 21:40:11` | `cowrie.command.success` |
| `2026-06-28 21:40:12` | `cowrie.log.closed` |
| `2026-06-28 21:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c6317b533c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:40 |
| **Last Seen** | 2026-06-28 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:40:41` | `cowrie.session.connect` |
| `2026-06-28 21:40:41` | `cowrie.client.version` |
| `2026-06-28 21:40:41` | `cowrie.client.kex` |
| `2026-06-28 21:40:41` | `cowrie.login.success` |
| `2026-06-28 21:40:42` | `cowrie.session.params` |
| `2026-06-28 21:40:42` | `cowrie.command.input` |
| `2026-06-28 21:40:42` | `cowrie.log.closed` |
| `2026-06-28 21:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed654c5c493

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:41 |
| **Last Seen** | 2026-06-28 21:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:41:40` | `cowrie.session.connect` |
| `2026-06-28 21:41:41` | `cowrie.client.version` |
| `2026-06-28 21:41:41` | `cowrie.client.kex` |
| `2026-06-28 21:41:41` | `cowrie.login.success` |
| `2026-06-28 21:41:42` | `cowrie.session.params` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.success` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:42` | `cowrie.command.input` |
| `2026-06-28 21:41:43` | `cowrie.log.closed` |
| `2026-06-28 21:41:43` | `cowrie.session.params` |
| `2026-06-28 21:41:43` | `cowrie.command.input` |
| `2026-06-28 21:41:43` | `cowrie.command.input` |
| `2026-06-28 21:41:43` | `cowrie.command.success` |
| `2026-06-28 21:41:44` | `cowrie.log.closed` |
| `2026-06-28 21:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567d31b129b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:41 |
| **Last Seen** | 2026-06-28 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:41:42` | `cowrie.session.connect` |
| `2026-06-28 21:41:42` | `cowrie.client.version` |
| `2026-06-28 21:41:42` | `cowrie.client.kex` |
| `2026-06-28 21:41:43` | `cowrie.login.success` |
| `2026-06-28 21:41:44` | `cowrie.session.params` |
| `2026-06-28 21:41:44` | `cowrie.command.input` |
| `2026-06-28 21:41:44` | `cowrie.log.closed` |
| `2026-06-28 21:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b4ff5d96d62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:42 |
| **Last Seen** | 2026-06-28 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:42:42` | `cowrie.session.connect` |
| `2026-06-28 21:42:42` | `cowrie.client.version` |
| `2026-06-28 21:42:42` | `cowrie.client.kex` |
| `2026-06-28 21:42:42` | `cowrie.login.success` |
| `2026-06-28 21:42:43` | `cowrie.session.params` |
| `2026-06-28 21:42:43` | `cowrie.command.input` |
| `2026-06-28 21:42:43` | `cowrie.log.closed` |
| `2026-06-28 21:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2d17b15ef7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:43 |
| **Last Seen** | 2026-06-28 21:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:43:14` | `cowrie.session.connect` |
| `2026-06-28 21:43:15` | `cowrie.client.version` |
| `2026-06-28 21:43:15` | `cowrie.client.kex` |
| `2026-06-28 21:43:15` | `cowrie.login.success` |
| `2026-06-28 21:43:16` | `cowrie.session.params` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.success` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.command.input` |
| `2026-06-28 21:43:16` | `cowrie.log.closed` |
| `2026-06-28 21:43:18` | `cowrie.session.params` |
| `2026-06-28 21:43:18` | `cowrie.command.input` |
| `2026-06-28 21:43:18` | `cowrie.command.input` |
| `2026-06-28 21:43:18` | `cowrie.command.success` |
| `2026-06-28 21:43:18` | `cowrie.log.closed` |
| `2026-06-28 21:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595492c06637

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 21:43 |
| **Last Seen** | 2026-06-28 21:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:43:32` | `cowrie.session.connect` |
| `2026-06-28 21:43:34` | `cowrie.client.version` |
| `2026-06-28 21:43:34` | `cowrie.client.kex` |
| `2026-06-28 21:43:41` | `cowrie.login.success` |
| `2026-06-28 21:43:45` | `cowrie.session.params` |
| `2026-06-28 21:43:45` | `cowrie.command.input` |
| `2026-06-28 21:43:46` | `cowrie.log.closed` |
| `2026-06-28 21:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f38f9bdefe6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:43 |
| **Last Seen** | 2026-06-28 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:43:42` | `cowrie.session.connect` |
| `2026-06-28 21:43:42` | `cowrie.client.version` |
| `2026-06-28 21:43:42` | `cowrie.client.kex` |
| `2026-06-28 21:43:42` | `cowrie.login.success` |
| `2026-06-28 21:43:43` | `cowrie.session.params` |
| `2026-06-28 21:43:43` | `cowrie.command.input` |
| `2026-06-28 21:43:43` | `cowrie.log.closed` |
| `2026-06-28 21:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9924a1182709

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:44 |
| **Last Seen** | 2026-06-28 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:44:42` | `cowrie.session.connect` |
| `2026-06-28 21:44:42` | `cowrie.client.version` |
| `2026-06-28 21:44:42` | `cowrie.client.kex` |
| `2026-06-28 21:44:43` | `cowrie.login.success` |
| `2026-06-28 21:44:43` | `cowrie.session.params` |
| `2026-06-28 21:44:43` | `cowrie.command.input` |
| `2026-06-28 21:44:44` | `cowrie.log.closed` |
| `2026-06-28 21:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ad1e3c841a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:44 |
| **Last Seen** | 2026-06-28 21:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:44:52` | `cowrie.session.connect` |
| `2026-06-28 21:44:52` | `cowrie.client.version` |
| `2026-06-28 21:44:52` | `cowrie.client.kex` |
| `2026-06-28 21:44:53` | `cowrie.login.success` |
| `2026-06-28 21:44:54` | `cowrie.session.params` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.success` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.command.input` |
| `2026-06-28 21:44:54` | `cowrie.log.closed` |
| `2026-06-28 21:44:55` | `cowrie.session.params` |
| `2026-06-28 21:44:55` | `cowrie.command.input` |
| `2026-06-28 21:44:55` | `cowrie.command.input` |
| `2026-06-28 21:44:55` | `cowrie.command.success` |
| `2026-06-28 21:44:55` | `cowrie.log.closed` |
| `2026-06-28 21:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce71ba7affee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:45 |
| **Last Seen** | 2026-06-28 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:45:44` | `cowrie.session.connect` |
| `2026-06-28 21:45:44` | `cowrie.client.version` |
| `2026-06-28 21:45:44` | `cowrie.client.kex` |
| `2026-06-28 21:45:44` | `cowrie.login.success` |
| `2026-06-28 21:45:45` | `cowrie.session.params` |
| `2026-06-28 21:45:45` | `cowrie.command.input` |
| `2026-06-28 21:45:45` | `cowrie.log.closed` |
| `2026-06-28 21:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce94d2f9376

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:46 |
| **Last Seen** | 2026-06-28 21:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:46:38` | `cowrie.session.connect` |
| `2026-06-28 21:46:39` | `cowrie.client.version` |
| `2026-06-28 21:46:39` | `cowrie.client.kex` |
| `2026-06-28 21:46:39` | `cowrie.login.success` |
| `2026-06-28 21:46:40` | `cowrie.session.params` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.success` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.command.input` |
| `2026-06-28 21:46:40` | `cowrie.log.closed` |
| `2026-06-28 21:46:41` | `cowrie.session.params` |
| `2026-06-28 21:46:41` | `cowrie.command.input` |
| `2026-06-28 21:46:41` | `cowrie.command.input` |
| `2026-06-28 21:46:41` | `cowrie.command.success` |
| `2026-06-28 21:46:41` | `cowrie.log.closed` |
| `2026-06-28 21:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f062ba3da5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:46 |
| **Last Seen** | 2026-06-28 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:46:46` | `cowrie.session.connect` |
| `2026-06-28 21:46:46` | `cowrie.client.version` |
| `2026-06-28 21:46:46` | `cowrie.client.kex` |
| `2026-06-28 21:46:47` | `cowrie.login.success` |
| `2026-06-28 21:46:48` | `cowrie.session.params` |
| `2026-06-28 21:46:48` | `cowrie.command.input` |
| `2026-06-28 21:46:48` | `cowrie.log.closed` |
| `2026-06-28 21:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1348b161e67

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:47 |
| **Last Seen** | 2026-06-28 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:47:48` | `cowrie.session.connect` |
| `2026-06-28 21:47:48` | `cowrie.client.version` |
| `2026-06-28 21:47:48` | `cowrie.client.kex` |
| `2026-06-28 21:47:49` | `cowrie.login.success` |
| `2026-06-28 21:47:49` | `cowrie.session.params` |
| `2026-06-28 21:47:49` | `cowrie.command.input` |
| `2026-06-28 21:47:49` | `cowrie.log.closed` |
| `2026-06-28 21:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6673be110e3b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:48 |
| **Last Seen** | 2026-06-28 21:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:48:30` | `cowrie.session.connect` |
| `2026-06-28 21:48:30` | `cowrie.client.version` |
| `2026-06-28 21:48:30` | `cowrie.client.kex` |
| `2026-06-28 21:48:30` | `cowrie.login.success` |
| `2026-06-28 21:48:31` | `cowrie.session.params` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.success` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.command.input` |
| `2026-06-28 21:48:31` | `cowrie.log.closed` |
| `2026-06-28 21:48:32` | `cowrie.session.params` |
| `2026-06-28 21:48:32` | `cowrie.command.input` |
| `2026-06-28 21:48:32` | `cowrie.command.input` |
| `2026-06-28 21:48:32` | `cowrie.command.success` |
| `2026-06-28 21:48:32` | `cowrie.log.closed` |
| `2026-06-28 21:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b3b0ddb16a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:48 |
| **Last Seen** | 2026-06-28 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:48:49` | `cowrie.session.connect` |
| `2026-06-28 21:48:49` | `cowrie.client.version` |
| `2026-06-28 21:48:50` | `cowrie.client.kex` |
| `2026-06-28 21:48:50` | `cowrie.login.success` |
| `2026-06-28 21:48:51` | `cowrie.session.params` |
| `2026-06-28 21:48:51` | `cowrie.command.input` |
| `2026-06-28 21:48:51` | `cowrie.log.closed` |
| `2026-06-28 21:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0816f60bbe8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:49 |
| **Last Seen** | 2026-06-28 21:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:49:50` | `cowrie.session.connect` |
| `2026-06-28 21:49:50` | `cowrie.client.version` |
| `2026-06-28 21:49:50` | `cowrie.client.kex` |
| `2026-06-28 21:49:51` | `cowrie.login.success` |
| `2026-06-28 21:49:51` | `cowrie.session.params` |
| `2026-06-28 21:49:51` | `cowrie.command.input` |
| `2026-06-28 21:49:52` | `cowrie.log.closed` |
| `2026-06-28 21:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f6159e1587

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:50 |
| **Last Seen** | 2026-06-28 21:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:50:30` | `cowrie.session.connect` |
| `2026-06-28 21:50:30` | `cowrie.client.version` |
| `2026-06-28 21:50:30` | `cowrie.client.kex` |
| `2026-06-28 21:50:30` | `cowrie.login.success` |
| `2026-06-28 21:50:31` | `cowrie.session.params` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.success` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:31` | `cowrie.command.input` |
| `2026-06-28 21:50:32` | `cowrie.log.closed` |
| `2026-06-28 21:50:32` | `cowrie.session.params` |
| `2026-06-28 21:50:32` | `cowrie.command.input` |
| `2026-06-28 21:50:32` | `cowrie.command.input` |
| `2026-06-28 21:50:32` | `cowrie.command.success` |
| `2026-06-28 21:50:33` | `cowrie.log.closed` |
| `2026-06-28 21:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57466a5f2cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:50 |
| **Last Seen** | 2026-06-28 21:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:50:52` | `cowrie.session.connect` |
| `2026-06-28 21:50:52` | `cowrie.client.version` |
| `2026-06-28 21:50:52` | `cowrie.client.kex` |
| `2026-06-28 21:50:52` | `cowrie.login.success` |
| `2026-06-28 21:50:53` | `cowrie.session.params` |
| `2026-06-28 21:50:53` | `cowrie.command.input` |
| `2026-06-28 21:50:53` | `cowrie.log.closed` |
| `2026-06-28 21:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038f329c731c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:51 |
| **Last Seen** | 2026-06-28 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:51:55` | `cowrie.session.connect` |
| `2026-06-28 21:51:55` | `cowrie.client.version` |
| `2026-06-28 21:51:55` | `cowrie.client.kex` |
| `2026-06-28 21:51:55` | `cowrie.login.success` |
| `2026-06-28 21:51:56` | `cowrie.session.params` |
| `2026-06-28 21:51:56` | `cowrie.command.input` |
| `2026-06-28 21:51:56` | `cowrie.log.closed` |
| `2026-06-28 21:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff06e5214be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:52 |
| **Last Seen** | 2026-06-28 21:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:52:41` | `cowrie.session.connect` |
| `2026-06-28 21:52:41` | `cowrie.client.version` |
| `2026-06-28 21:52:41` | `cowrie.client.kex` |
| `2026-06-28 21:52:42` | `cowrie.login.success` |
| `2026-06-28 21:52:43` | `cowrie.session.params` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.success` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.command.input` |
| `2026-06-28 21:52:43` | `cowrie.log.closed` |
| `2026-06-28 21:52:44` | `cowrie.session.params` |
| `2026-06-28 21:52:44` | `cowrie.command.input` |
| `2026-06-28 21:52:44` | `cowrie.command.input` |
| `2026-06-28 21:52:44` | `cowrie.command.success` |
| `2026-06-28 21:52:44` | `cowrie.log.closed` |
| `2026-06-28 21:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d7cc1a973c2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 21:52 |
| **Last Seen** | 2026-06-28 21:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:52:43` | `cowrie.session.connect` |
| `2026-06-28 21:52:44` | `cowrie.client.version` |
| `2026-06-28 21:52:44` | `cowrie.client.kex` |
| `2026-06-28 21:52:46` | `cowrie.login.success` |
| `2026-06-28 21:52:47` | `cowrie.session.params` |
| `2026-06-28 21:52:47` | `cowrie.command.input` |
| `2026-06-28 21:52:47` | `cowrie.log.closed` |
| `2026-06-28 21:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68f4b2d838c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:53 |
| **Last Seen** | 2026-06-28 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:53:00` | `cowrie.session.connect` |
| `2026-06-28 21:53:00` | `cowrie.client.version` |
| `2026-06-28 21:53:00` | `cowrie.client.kex` |
| `2026-06-28 21:53:00` | `cowrie.login.success` |
| `2026-06-28 21:53:01` | `cowrie.session.params` |
| `2026-06-28 21:53:01` | `cowrie.command.input` |
| `2026-06-28 21:53:01` | `cowrie.log.closed` |
| `2026-06-28 21:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9b2dd1f4f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:54 |
| **Last Seen** | 2026-06-28 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:54:05` | `cowrie.session.connect` |
| `2026-06-28 21:54:05` | `cowrie.client.version` |
| `2026-06-28 21:54:05` | `cowrie.client.kex` |
| `2026-06-28 21:54:06` | `cowrie.login.success` |
| `2026-06-28 21:54:06` | `cowrie.session.params` |
| `2026-06-28 21:54:06` | `cowrie.command.input` |
| `2026-06-28 21:54:06` | `cowrie.log.closed` |
| `2026-06-28 21:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e63727af9d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 21:54 |
| **Last Seen** | 2026-06-28 21:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:54:59` | `cowrie.session.connect` |
| `2026-06-28 21:55:01` | `cowrie.client.version` |
| `2026-06-28 21:55:01` | `cowrie.client.kex` |
| `2026-06-28 21:55:07` | `cowrie.login.success` |
| `2026-06-28 21:55:09` | `cowrie.session.params` |
| `2026-06-28 21:55:09` | `cowrie.command.input` |
| `2026-06-28 21:55:12` | `cowrie.log.closed` |
| `2026-06-28 21:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f7091a6392

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:54 |
| **Last Seen** | 2026-06-28 21:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:54:59` | `cowrie.session.connect` |
| `2026-06-28 21:54:59` | `cowrie.client.version` |
| `2026-06-28 21:55:00` | `cowrie.client.kex` |
| `2026-06-28 21:55:00` | `cowrie.login.success` |
| `2026-06-28 21:55:01` | `cowrie.session.params` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.success` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.command.input` |
| `2026-06-28 21:55:01` | `cowrie.log.closed` |
| `2026-06-28 21:55:02` | `cowrie.session.params` |
| `2026-06-28 21:55:02` | `cowrie.command.input` |
| `2026-06-28 21:55:02` | `cowrie.command.input` |
| `2026-06-28 21:55:02` | `cowrie.command.success` |
| `2026-06-28 21:55:02` | `cowrie.log.closed` |
| `2026-06-28 21:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9ed7440e26

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:55 |
| **Last Seen** | 2026-06-28 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:55:09` | `cowrie.session.connect` |
| `2026-06-28 21:55:09` | `cowrie.client.version` |
| `2026-06-28 21:55:09` | `cowrie.client.kex` |
| `2026-06-28 21:55:10` | `cowrie.login.success` |
| `2026-06-28 21:55:11` | `cowrie.session.params` |
| `2026-06-28 21:55:11` | `cowrie.command.input` |
| `2026-06-28 21:55:11` | `cowrie.log.closed` |
| `2026-06-28 21:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844d4c07a63f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:56 |
| **Last Seen** | 2026-06-28 21:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:56:14` | `cowrie.session.connect` |
| `2026-06-28 21:56:14` | `cowrie.client.version` |
| `2026-06-28 21:56:15` | `cowrie.client.kex` |
| `2026-06-28 21:56:15` | `cowrie.login.success` |
| `2026-06-28 21:56:16` | `cowrie.session.params` |
| `2026-06-28 21:56:16` | `cowrie.command.input` |
| `2026-06-28 21:56:16` | `cowrie.log.closed` |
| `2026-06-28 21:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fc11015e20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:57 |
| **Last Seen** | 2026-06-28 21:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:57:10` | `cowrie.session.connect` |
| `2026-06-28 21:57:10` | `cowrie.client.version` |
| `2026-06-28 21:57:11` | `cowrie.client.kex` |
| `2026-06-28 21:57:11` | `cowrie.login.success` |
| `2026-06-28 21:57:12` | `cowrie.session.params` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.success` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.command.input` |
| `2026-06-28 21:57:12` | `cowrie.log.closed` |
| `2026-06-28 21:57:13` | `cowrie.session.params` |
| `2026-06-28 21:57:13` | `cowrie.command.input` |
| `2026-06-28 21:57:13` | `cowrie.command.input` |
| `2026-06-28 21:57:13` | `cowrie.command.success` |
| `2026-06-28 21:57:13` | `cowrie.log.closed` |
| `2026-06-28 21:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106086ff6886

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:57 |
| **Last Seen** | 2026-06-28 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:57:20` | `cowrie.session.connect` |
| `2026-06-28 21:57:20` | `cowrie.client.version` |
| `2026-06-28 21:57:20` | `cowrie.client.kex` |
| `2026-06-28 21:57:21` | `cowrie.login.success` |
| `2026-06-28 21:57:22` | `cowrie.session.params` |
| `2026-06-28 21:57:22` | `cowrie.command.input` |
| `2026-06-28 21:57:22` | `cowrie.log.closed` |
| `2026-06-28 21:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a297a763fca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:58 |
| **Last Seen** | 2026-06-28 21:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:58:26` | `cowrie.session.connect` |
| `2026-06-28 21:58:26` | `cowrie.client.version` |
| `2026-06-28 21:58:26` | `cowrie.client.kex` |
| `2026-06-28 21:58:26` | `cowrie.login.success` |
| `2026-06-28 21:58:27` | `cowrie.session.params` |
| `2026-06-28 21:58:27` | `cowrie.command.input` |
| `2026-06-28 21:58:27` | `cowrie.log.closed` |
| `2026-06-28 21:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d43672234e38

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 21:59 |
| **Last Seen** | 2026-06-28 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:59:32` | `cowrie.session.connect` |
| `2026-06-28 21:59:32` | `cowrie.client.version` |
| `2026-06-28 21:59:32` | `cowrie.client.kex` |
| `2026-06-28 21:59:33` | `cowrie.login.success` |
| `2026-06-28 21:59:33` | `cowrie.session.params` |
| `2026-06-28 21:59:33` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.log.closed` |
| `2026-06-28 21:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567a2a530c0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 21:59 |
| **Last Seen** | 2026-06-28 21:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 21:59:32` | `cowrie.session.connect` |
| `2026-06-28 21:59:32` | `cowrie.client.version` |
| `2026-06-28 21:59:33` | `cowrie.client.kex` |
| `2026-06-28 21:59:34` | `cowrie.login.success` |
| `2026-06-28 21:59:34` | `cowrie.session.params` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.success` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.command.input` |
| `2026-06-28 21:59:34` | `cowrie.log.closed` |
| `2026-06-28 21:59:35` | `cowrie.session.params` |
| `2026-06-28 21:59:35` | `cowrie.command.input` |
| `2026-06-28 21:59:35` | `cowrie.command.input` |
| `2026-06-28 21:59:35` | `cowrie.command.success` |
| `2026-06-28 21:59:36` | `cowrie.log.closed` |
| `2026-06-28 21:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe886c5cc9dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:00 |
| **Last Seen** | 2026-06-28 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:00:30` | `cowrie.session.connect` |
| `2026-06-28 22:00:30` | `cowrie.client.version` |
| `2026-06-28 22:00:30` | `cowrie.client.kex` |
| `2026-06-28 22:00:31` | `cowrie.login.success` |
| `2026-06-28 22:00:32` | `cowrie.session.params` |
| `2026-06-28 22:00:32` | `cowrie.command.input` |
| `2026-06-28 22:00:32` | `cowrie.log.closed` |
| `2026-06-28 22:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50878dd13b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:01 |
| **Last Seen** | 2026-06-28 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:01:14` | `cowrie.session.connect` |
| `2026-06-28 22:01:14` | `cowrie.client.version` |
| `2026-06-28 22:01:14` | `cowrie.client.kex` |
| `2026-06-28 22:01:15` | `cowrie.login.success` |
| `2026-06-28 22:01:15` | `cowrie.session.params` |
| `2026-06-28 22:01:15` | `cowrie.command.input` |
| `2026-06-28 22:01:16` | `cowrie.log.closed` |
| `2026-06-28 22:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3981c19d2a89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:01 |
| **Last Seen** | 2026-06-28 22:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:01:51` | `cowrie.session.connect` |
| `2026-06-28 22:01:51` | `cowrie.client.version` |
| `2026-06-28 22:01:51` | `cowrie.client.kex` |
| `2026-06-28 22:01:52` | `cowrie.login.success` |
| `2026-06-28 22:01:53` | `cowrie.session.params` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.success` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.command.input` |
| `2026-06-28 22:01:53` | `cowrie.log.closed` |
| `2026-06-28 22:01:54` | `cowrie.session.params` |
| `2026-06-28 22:01:54` | `cowrie.command.input` |
| `2026-06-28 22:01:54` | `cowrie.command.input` |
| `2026-06-28 22:01:54` | `cowrie.command.success` |
| `2026-06-28 22:01:54` | `cowrie.log.closed` |
| `2026-06-28 22:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca90d33a646

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:01 |
| **Last Seen** | 2026-06-28 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:01:57` | `cowrie.session.connect` |
| `2026-06-28 22:01:57` | `cowrie.client.version` |
| `2026-06-28 22:01:57` | `cowrie.client.kex` |
| `2026-06-28 22:01:58` | `cowrie.login.success` |
| `2026-06-28 22:01:58` | `cowrie.session.params` |
| `2026-06-28 22:01:58` | `cowrie.command.input` |
| `2026-06-28 22:01:58` | `cowrie.log.closed` |
| `2026-06-28 22:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba727151f7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:02 |
| **Last Seen** | 2026-06-28 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:02:41` | `cowrie.session.connect` |
| `2026-06-28 22:02:41` | `cowrie.client.version` |
| `2026-06-28 22:02:41` | `cowrie.client.kex` |
| `2026-06-28 22:02:41` | `cowrie.login.success` |
| `2026-06-28 22:02:42` | `cowrie.session.params` |
| `2026-06-28 22:02:42` | `cowrie.command.input` |
| `2026-06-28 22:02:42` | `cowrie.log.closed` |
| `2026-06-28 22:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39476cb19be1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:03 |
| **Last Seen** | 2026-06-28 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:03:25` | `cowrie.session.connect` |
| `2026-06-28 22:03:25` | `cowrie.client.version` |
| `2026-06-28 22:03:25` | `cowrie.client.kex` |
| `2026-06-28 22:03:25` | `cowrie.login.success` |
| `2026-06-28 22:03:26` | `cowrie.session.params` |
| `2026-06-28 22:03:26` | `cowrie.command.input` |
| `2026-06-28 22:03:26` | `cowrie.log.closed` |
| `2026-06-28 22:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ed1ba16c4d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:04 |
| **Last Seen** | 2026-06-28 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:04:10` | `cowrie.session.connect` |
| `2026-06-28 22:04:10` | `cowrie.client.version` |
| `2026-06-28 22:04:10` | `cowrie.client.kex` |
| `2026-06-28 22:04:10` | `cowrie.login.success` |
| `2026-06-28 22:04:11` | `cowrie.session.params` |
| `2026-06-28 22:04:11` | `cowrie.command.input` |
| `2026-06-28 22:04:11` | `cowrie.log.closed` |
| `2026-06-28 22:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4ff7868208

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:04 |
| **Last Seen** | 2026-06-28 22:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:04:12` | `cowrie.session.connect` |
| `2026-06-28 22:04:12` | `cowrie.client.version` |
| `2026-06-28 22:04:12` | `cowrie.client.kex` |
| `2026-06-28 22:04:12` | `cowrie.login.success` |
| `2026-06-28 22:04:13` | `cowrie.session.params` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.success` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.command.input` |
| `2026-06-28 22:04:13` | `cowrie.log.closed` |
| `2026-06-28 22:04:14` | `cowrie.session.params` |
| `2026-06-28 22:04:14` | `cowrie.command.input` |
| `2026-06-28 22:04:14` | `cowrie.command.input` |
| `2026-06-28 22:04:14` | `cowrie.command.success` |
| `2026-06-28 22:04:14` | `cowrie.log.closed` |
| `2026-06-28 22:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cfe41a0c4ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:04 |
| **Last Seen** | 2026-06-28 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:04:55` | `cowrie.session.connect` |
| `2026-06-28 22:04:55` | `cowrie.client.version` |
| `2026-06-28 22:04:55` | `cowrie.client.kex` |
| `2026-06-28 22:04:55` | `cowrie.login.success` |
| `2026-06-28 22:04:56` | `cowrie.session.params` |
| `2026-06-28 22:04:56` | `cowrie.command.input` |
| `2026-06-28 22:04:56` | `cowrie.log.closed` |
| `2026-06-28 22:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f45c385920

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:05 |
| **Last Seen** | 2026-06-28 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:05:41` | `cowrie.session.connect` |
| `2026-06-28 22:05:41` | `cowrie.client.version` |
| `2026-06-28 22:05:41` | `cowrie.client.kex` |
| `2026-06-28 22:05:42` | `cowrie.login.success` |
| `2026-06-28 22:05:42` | `cowrie.session.params` |
| `2026-06-28 22:05:42` | `cowrie.command.input` |
| `2026-06-28 22:05:42` | `cowrie.log.closed` |
| `2026-06-28 22:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d4a56d38f4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 22:06 |
| **Last Seen** | 2026-06-28 22:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:06:25` | `cowrie.session.connect` |
| `2026-06-28 22:06:26` | `cowrie.client.version` |
| `2026-06-28 22:06:26` | `cowrie.client.kex` |
| `2026-06-28 22:06:32` | `cowrie.login.success` |
| `2026-06-28 22:06:35` | `cowrie.session.params` |
| `2026-06-28 22:06:35` | `cowrie.command.input` |
| `2026-06-28 22:06:36` | `cowrie.log.closed` |
| `2026-06-28 22:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fececec60654

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:06 |
| **Last Seen** | 2026-06-28 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:06:27` | `cowrie.session.connect` |
| `2026-06-28 22:06:27` | `cowrie.client.version` |
| `2026-06-28 22:06:27` | `cowrie.client.kex` |
| `2026-06-28 22:06:27` | `cowrie.login.success` |
| `2026-06-28 22:06:28` | `cowrie.session.params` |
| `2026-06-28 22:06:28` | `cowrie.command.input` |
| `2026-06-28 22:06:28` | `cowrie.log.closed` |
| `2026-06-28 22:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d243447f275

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:06 |
| **Last Seen** | 2026-06-28 22:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:06:57` | `cowrie.session.connect` |
| `2026-06-28 22:06:57` | `cowrie.client.version` |
| `2026-06-28 22:06:57` | `cowrie.client.kex` |
| `2026-06-28 22:06:57` | `cowrie.login.success` |
| `2026-06-28 22:06:58` | `cowrie.session.params` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.success` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.command.input` |
| `2026-06-28 22:06:58` | `cowrie.log.closed` |
| `2026-06-28 22:06:59` | `cowrie.session.params` |
| `2026-06-28 22:06:59` | `cowrie.command.input` |
| `2026-06-28 22:06:59` | `cowrie.command.input` |
| `2026-06-28 22:06:59` | `cowrie.command.success` |
| `2026-06-28 22:06:59` | `cowrie.log.closed` |
| `2026-06-28 22:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442cd0b28179

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:07 |
| **Last Seen** | 2026-06-28 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:07:11` | `cowrie.session.connect` |
| `2026-06-28 22:07:11` | `cowrie.client.version` |
| `2026-06-28 22:07:11` | `cowrie.client.kex` |
| `2026-06-28 22:07:12` | `cowrie.login.success` |
| `2026-06-28 22:07:13` | `cowrie.session.params` |
| `2026-06-28 22:07:13` | `cowrie.command.input` |
| `2026-06-28 22:07:13` | `cowrie.log.closed` |
| `2026-06-28 22:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16271b51ac1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 22:07 |
| **Last Seen** | 2026-06-28 22:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:07:28` | `cowrie.session.connect` |
| `2026-06-28 22:07:29` | `cowrie.client.version` |
| `2026-06-28 22:07:29` | `cowrie.client.kex` |
| `2026-06-28 22:07:30` | `cowrie.login.success` |
| `2026-06-28 22:07:32` | `cowrie.session.params` |
| `2026-06-28 22:07:32` | `cowrie.command.input` |
| `2026-06-28 22:07:32` | `cowrie.log.closed` |
| `2026-06-28 22:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128c401afb25

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:07 |
| **Last Seen** | 2026-06-28 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:07:57` | `cowrie.session.connect` |
| `2026-06-28 22:07:57` | `cowrie.client.version` |
| `2026-06-28 22:07:57` | `cowrie.client.kex` |
| `2026-06-28 22:07:57` | `cowrie.login.success` |
| `2026-06-28 22:07:58` | `cowrie.session.params` |
| `2026-06-28 22:07:58` | `cowrie.command.input` |
| `2026-06-28 22:07:58` | `cowrie.log.closed` |
| `2026-06-28 22:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e9d9c7e632

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:08 |
| **Last Seen** | 2026-06-28 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:08:42` | `cowrie.session.connect` |
| `2026-06-28 22:08:42` | `cowrie.client.version` |
| `2026-06-28 22:08:42` | `cowrie.client.kex` |
| `2026-06-28 22:08:43` | `cowrie.login.success` |
| `2026-06-28 22:08:44` | `cowrie.session.params` |
| `2026-06-28 22:08:44` | `cowrie.command.input` |
| `2026-06-28 22:08:44` | `cowrie.log.closed` |
| `2026-06-28 22:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731c066a72bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:09 |
| **Last Seen** | 2026-06-28 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:09:27` | `cowrie.session.connect` |
| `2026-06-28 22:09:27` | `cowrie.client.version` |
| `2026-06-28 22:09:27` | `cowrie.client.kex` |
| `2026-06-28 22:09:27` | `cowrie.login.success` |
| `2026-06-28 22:09:28` | `cowrie.session.params` |
| `2026-06-28 22:09:28` | `cowrie.command.input` |
| `2026-06-28 22:09:28` | `cowrie.log.closed` |
| `2026-06-28 22:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ad1319b358

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:09 |
| **Last Seen** | 2026-06-28 22:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:09:31` | `cowrie.session.connect` |
| `2026-06-28 22:09:31` | `cowrie.client.version` |
| `2026-06-28 22:09:31` | `cowrie.client.kex` |
| `2026-06-28 22:09:32` | `cowrie.login.success` |
| `2026-06-28 22:09:33` | `cowrie.session.params` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.success` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.command.input` |
| `2026-06-28 22:09:33` | `cowrie.log.closed` |
| `2026-06-28 22:09:34` | `cowrie.session.params` |
| `2026-06-28 22:09:34` | `cowrie.command.input` |
| `2026-06-28 22:09:34` | `cowrie.command.input` |
| `2026-06-28 22:09:34` | `cowrie.command.success` |
| `2026-06-28 22:09:34` | `cowrie.log.closed` |
| `2026-06-28 22:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f82da3c4c0c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 22:10 |
| **Last Seen** | 2026-06-28 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:10:07` | `cowrie.session.connect` |
| `2026-06-28 22:10:07` | `cowrie.client.version` |
| `2026-06-28 22:10:07` | `cowrie.client.kex` |
| `2026-06-28 22:10:07` | `cowrie.login.success` |
| `2026-06-28 22:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e007520ea5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 22:10 |
| **Last Seen** | 2026-06-28 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:10:07` | `cowrie.session.connect` |
| `2026-06-28 22:10:07` | `cowrie.client.version` |
| `2026-06-28 22:10:07` | `cowrie.client.kex` |
| `2026-06-28 22:10:07` | `cowrie.login.success` |
| `2026-06-28 22:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728f3844d964

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:10 |
| **Last Seen** | 2026-06-28 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:10:11` | `cowrie.session.connect` |
| `2026-06-28 22:10:11` | `cowrie.client.version` |
| `2026-06-28 22:10:11` | `cowrie.client.kex` |
| `2026-06-28 22:10:11` | `cowrie.login.success` |
| `2026-06-28 22:10:12` | `cowrie.session.params` |
| `2026-06-28 22:10:12` | `cowrie.command.input` |
| `2026-06-28 22:10:12` | `cowrie.log.closed` |
| `2026-06-28 22:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4606b24ed219

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 22:10 |
| **Last Seen** | 2026-06-28 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:10:11` | `cowrie.session.connect` |
| `2026-06-28 22:10:11` | `cowrie.client.version` |
| `2026-06-28 22:10:11` | `cowrie.client.kex` |
| `2026-06-28 22:10:11` | `cowrie.login.success` |
| `2026-06-28 22:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bd9a55aa240

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 22:10 |
| **Last Seen** | 2026-06-28 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:10:11` | `cowrie.session.connect` |
| `2026-06-28 22:10:11` | `cowrie.client.version` |
| `2026-06-28 22:10:11` | `cowrie.client.kex` |
| `2026-06-28 22:10:11` | `cowrie.login.success` |
| `2026-06-28 22:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2066478aec4b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:10 |
| **Last Seen** | 2026-06-28 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:10:56` | `cowrie.session.connect` |
| `2026-06-28 22:10:56` | `cowrie.client.version` |
| `2026-06-28 22:10:56` | `cowrie.client.kex` |
| `2026-06-28 22:10:56` | `cowrie.login.success` |
| `2026-06-28 22:10:57` | `cowrie.session.params` |
| `2026-06-28 22:10:57` | `cowrie.command.input` |
| `2026-06-28 22:10:57` | `cowrie.log.closed` |
| `2026-06-28 22:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddab6b5a31d9

| Field | Detail |
|---|---|
| **Source IP** | `129.146.97[.]8` |
| **First Seen** | 2026-06-28 22:11 |
| **Last Seen** | 2026-06-28 22:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:11:12` | `cowrie.session.connect` |
| `2026-06-28 22:11:12` | `cowrie.client.version` |
| `2026-06-28 22:11:12` | `cowrie.client.kex` |
| `2026-06-28 22:11:12` | `cowrie.login.success` |
| `2026-06-28 22:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.146.97[.]8` to AbuseIPDB if not already reported
- [ ] Block `129.146.97[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f4bf8e3f55

| Field | Detail |
|---|---|
| **Source IP** | `129.146.97[.]8` |
| **First Seen** | 2026-06-28 22:11 |
| **Last Seen** | 2026-06-28 22:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:11:12` | `cowrie.session.connect` |
| `2026-06-28 22:11:12` | `cowrie.client.version` |
| `2026-06-28 22:11:12` | `cowrie.client.kex` |
| `2026-06-28 22:11:12` | `cowrie.login.success` |
| `2026-06-28 22:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.146.97[.]8` to AbuseIPDB if not already reported
- [ ] Block `129.146.97[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452973adfb41

| Field | Detail |
|---|---|
| **Source IP** | `129.146.97[.]8` |
| **First Seen** | 2026-06-28 22:11 |
| **Last Seen** | 2026-06-28 22:13 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:11:36` | `cowrie.session.connect` |
| `2026-06-28 22:11:36` | `cowrie.client.version` |
| `2026-06-28 22:11:37` | `cowrie.client.kex` |
| `2026-06-28 22:11:37` | `cowrie.login.success` |
| `2026-06-28 22:11:38` | `cowrie.session.file_upload` |
| `2026-06-28 22:11:38` | `cowrie.session.params` |
| `2026-06-28 22:11:38` | `cowrie.command.input` |
| `2026-06-28 22:11:38` | `cowrie.command.input` |
| `2026-06-28 22:11:38` | `cowrie.command.input` |
| `2026-06-28 22:11:38` | `cowrie.command.failed` |
| `2026-06-28 22:11:38` | `cowrie.log.closed` |
| `2026-06-28 22:11:39` | `cowrie.session.params` |
| `2026-06-28 22:11:39` | `cowrie.command.input` |
| `2026-06-28 22:11:39` | `cowrie.log.closed` |
| `2026-06-28 22:11:40` | `cowrie.session.params` |
| `2026-06-28 22:11:40` | `cowrie.command.input` |
| `2026-06-28 22:11:40` | `cowrie.log.closed` |
| `2026-06-28 22:11:41` | `cowrie.session.params` |
| `2026-06-28 22:11:41` | `cowrie.command.input` |
| `2026-06-28 22:11:41` | `cowrie.command.failed` |
| `2026-06-28 22:11:41` | `cowrie.command.failed` |
| `2026-06-28 22:12:42` | `cowrie.session.params` |
| `2026-06-28 22:12:42` | `cowrie.command.input` |
| `2026-06-28 22:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.146.97[.]8` to AbuseIPDB if not already reported
- [ ] Block `129.146.97[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a657b2c7b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:11 |
| **Last Seen** | 2026-06-28 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:11:42` | `cowrie.session.connect` |
| `2026-06-28 22:11:42` | `cowrie.client.version` |
| `2026-06-28 22:11:42` | `cowrie.client.kex` |
| `2026-06-28 22:11:42` | `cowrie.login.success` |
| `2026-06-28 22:11:43` | `cowrie.session.params` |
| `2026-06-28 22:11:43` | `cowrie.command.input` |
| `2026-06-28 22:11:43` | `cowrie.log.closed` |
| `2026-06-28 22:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b2a86de2e92

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:12 |
| **Last Seen** | 2026-06-28 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:12:28` | `cowrie.session.connect` |
| `2026-06-28 22:12:28` | `cowrie.client.version` |
| `2026-06-28 22:12:28` | `cowrie.client.kex` |
| `2026-06-28 22:12:28` | `cowrie.login.success` |
| `2026-06-28 22:12:29` | `cowrie.session.params` |
| `2026-06-28 22:12:29` | `cowrie.command.input` |
| `2026-06-28 22:12:29` | `cowrie.log.closed` |
| `2026-06-28 22:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ddefb45ed3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:12 |
| **Last Seen** | 2026-06-28 22:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:12:29` | `cowrie.session.connect` |
| `2026-06-28 22:12:29` | `cowrie.client.version` |
| `2026-06-28 22:12:29` | `cowrie.client.kex` |
| `2026-06-28 22:12:30` | `cowrie.login.success` |
| `2026-06-28 22:12:30` | `cowrie.session.params` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.success` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:30` | `cowrie.command.input` |
| `2026-06-28 22:12:31` | `cowrie.log.closed` |
| `2026-06-28 22:12:31` | `cowrie.session.params` |
| `2026-06-28 22:12:31` | `cowrie.command.input` |
| `2026-06-28 22:12:31` | `cowrie.command.input` |
| `2026-06-28 22:12:31` | `cowrie.command.success` |
| `2026-06-28 22:12:31` | `cowrie.log.closed` |
| `2026-06-28 22:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e41cd5a7e05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:13 |
| **Last Seen** | 2026-06-28 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:13:14` | `cowrie.session.connect` |
| `2026-06-28 22:13:14` | `cowrie.client.version` |
| `2026-06-28 22:13:14` | `cowrie.client.kex` |
| `2026-06-28 22:13:14` | `cowrie.login.success` |
| `2026-06-28 22:13:15` | `cowrie.session.params` |
| `2026-06-28 22:13:15` | `cowrie.command.input` |
| `2026-06-28 22:13:15` | `cowrie.log.closed` |
| `2026-06-28 22:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba59d79615f1

| Field | Detail |
|---|---|
| **Source IP** | `129.146.97[.]8` |
| **First Seen** | 2026-06-28 22:13 |
| **Last Seen** | 2026-06-28 22:16 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:13:57` | `cowrie.session.connect` |
| `2026-06-28 22:13:57` | `cowrie.client.version` |
| `2026-06-28 22:13:57` | `cowrie.client.kex` |
| `2026-06-28 22:13:57` | `cowrie.login.success` |
| `2026-06-28 22:13:58` | `cowrie.session.file_upload` |
| `2026-06-28 22:13:59` | `cowrie.session.params` |
| `2026-06-28 22:13:59` | `cowrie.command.input` |
| `2026-06-28 22:13:59` | `cowrie.command.input` |
| `2026-06-28 22:13:59` | `cowrie.command.input` |
| `2026-06-28 22:13:59` | `cowrie.command.failed` |
| `2026-06-28 22:13:59` | `cowrie.log.closed` |
| `2026-06-28 22:14:00` | `cowrie.session.params` |
| `2026-06-28 22:14:00` | `cowrie.command.input` |
| `2026-06-28 22:14:00` | `cowrie.log.closed` |
| `2026-06-28 22:14:01` | `cowrie.session.params` |
| `2026-06-28 22:14:01` | `cowrie.command.input` |
| `2026-06-28 22:14:01` | `cowrie.log.closed` |
| `2026-06-28 22:14:02` | `cowrie.session.params` |
| `2026-06-28 22:14:02` | `cowrie.command.input` |
| `2026-06-28 22:14:02` | `cowrie.command.failed` |
| `2026-06-28 22:14:02` | `cowrie.command.failed` |
| `2026-06-28 22:15:02` | `cowrie.session.params` |
| `2026-06-28 22:15:02` | `cowrie.command.input` |
| `2026-06-28 22:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.146.97[.]8` to AbuseIPDB if not already reported
- [ ] Block `129.146.97[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1875e4ec3bb3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:14 |
| **Last Seen** | 2026-06-28 22:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:14:00` | `cowrie.session.connect` |
| `2026-06-28 22:14:00` | `cowrie.client.version` |
| `2026-06-28 22:14:00` | `cowrie.client.kex` |
| `2026-06-28 22:14:02` | `cowrie.login.success` |
| `2026-06-28 22:14:02` | `cowrie.session.params` |
| `2026-06-28 22:14:02` | `cowrie.command.input` |
| `2026-06-28 22:14:02` | `cowrie.log.closed` |
| `2026-06-28 22:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f0ead73e9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:14 |
| **Last Seen** | 2026-06-28 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:14:46` | `cowrie.session.connect` |
| `2026-06-28 22:14:46` | `cowrie.client.version` |
| `2026-06-28 22:14:46` | `cowrie.client.kex` |
| `2026-06-28 22:14:47` | `cowrie.login.success` |
| `2026-06-28 22:14:47` | `cowrie.session.params` |
| `2026-06-28 22:14:47` | `cowrie.command.input` |
| `2026-06-28 22:14:48` | `cowrie.log.closed` |
| `2026-06-28 22:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ead8bf5ea2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:15 |
| **Last Seen** | 2026-06-28 22:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:15:11` | `cowrie.session.connect` |
| `2026-06-28 22:15:11` | `cowrie.client.version` |
| `2026-06-28 22:15:11` | `cowrie.client.kex` |
| `2026-06-28 22:15:11` | `cowrie.login.success` |
| `2026-06-28 22:15:12` | `cowrie.session.params` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.success` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.command.input` |
| `2026-06-28 22:15:12` | `cowrie.log.closed` |
| `2026-06-28 22:15:13` | `cowrie.session.params` |
| `2026-06-28 22:15:13` | `cowrie.command.input` |
| `2026-06-28 22:15:13` | `cowrie.command.input` |
| `2026-06-28 22:15:13` | `cowrie.command.success` |
| `2026-06-28 22:15:13` | `cowrie.log.closed` |
| `2026-06-28 22:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1c34c73541

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:15 |
| **Last Seen** | 2026-06-28 22:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:15:32` | `cowrie.session.connect` |
| `2026-06-28 22:15:32` | `cowrie.client.version` |
| `2026-06-28 22:15:32` | `cowrie.client.kex` |
| `2026-06-28 22:15:32` | `cowrie.login.success` |
| `2026-06-28 22:15:33` | `cowrie.session.params` |
| `2026-06-28 22:15:33` | `cowrie.command.input` |
| `2026-06-28 22:15:33` | `cowrie.log.closed` |
| `2026-06-28 22:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7cbaa1c521e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:16 |
| **Last Seen** | 2026-06-28 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:16:18` | `cowrie.session.connect` |
| `2026-06-28 22:16:18` | `cowrie.client.version` |
| `2026-06-28 22:16:18` | `cowrie.client.kex` |
| `2026-06-28 22:16:18` | `cowrie.login.success` |
| `2026-06-28 22:16:19` | `cowrie.session.params` |
| `2026-06-28 22:16:19` | `cowrie.command.input` |
| `2026-06-28 22:16:19` | `cowrie.log.closed` |
| `2026-06-28 22:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0e41f1c1bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:17 |
| **Last Seen** | 2026-06-28 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:17:06` | `cowrie.session.connect` |
| `2026-06-28 22:17:06` | `cowrie.client.version` |
| `2026-06-28 22:17:06` | `cowrie.client.kex` |
| `2026-06-28 22:17:06` | `cowrie.login.success` |
| `2026-06-28 22:17:07` | `cowrie.session.params` |
| `2026-06-28 22:17:07` | `cowrie.command.input` |
| `2026-06-28 22:17:07` | `cowrie.log.closed` |
| `2026-06-28 22:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb155b2db6f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 22:17 |
| **Last Seen** | 2026-06-28 22:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:17:56` | `cowrie.session.connect` |
| `2026-06-28 22:17:57` | `cowrie.client.version` |
| `2026-06-28 22:17:57` | `cowrie.client.kex` |
| `2026-06-28 22:18:03` | `cowrie.login.success` |
| `2026-06-28 22:18:05` | `cowrie.session.params` |
| `2026-06-28 22:18:05` | `cowrie.command.input` |
| `2026-06-28 22:18:07` | `cowrie.log.closed` |
| `2026-06-28 22:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd3a87ef718

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:17 |
| **Last Seen** | 2026-06-28 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:17:56` | `cowrie.session.connect` |
| `2026-06-28 22:17:56` | `cowrie.client.version` |
| `2026-06-28 22:17:56` | `cowrie.client.kex` |
| `2026-06-28 22:17:56` | `cowrie.login.success` |
| `2026-06-28 22:17:57` | `cowrie.session.params` |
| `2026-06-28 22:17:57` | `cowrie.command.input` |
| `2026-06-28 22:17:57` | `cowrie.log.closed` |
| `2026-06-28 22:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46dd35e6f04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:18 |
| **Last Seen** | 2026-06-28 22:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:18:02` | `cowrie.session.connect` |
| `2026-06-28 22:18:02` | `cowrie.client.version` |
| `2026-06-28 22:18:02` | `cowrie.client.kex` |
| `2026-06-28 22:18:02` | `cowrie.login.success` |
| `2026-06-28 22:18:03` | `cowrie.session.params` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.success` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.command.input` |
| `2026-06-28 22:18:03` | `cowrie.log.closed` |
| `2026-06-28 22:18:04` | `cowrie.session.params` |
| `2026-06-28 22:18:04` | `cowrie.command.input` |
| `2026-06-28 22:18:04` | `cowrie.command.input` |
| `2026-06-28 22:18:04` | `cowrie.command.success` |
| `2026-06-28 22:18:04` | `cowrie.log.closed` |
| `2026-06-28 22:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-741195b251df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:18 |
| **Last Seen** | 2026-06-28 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:18:45` | `cowrie.session.connect` |
| `2026-06-28 22:18:45` | `cowrie.client.version` |
| `2026-06-28 22:18:45` | `cowrie.client.kex` |
| `2026-06-28 22:18:45` | `cowrie.login.success` |
| `2026-06-28 22:18:46` | `cowrie.session.params` |
| `2026-06-28 22:18:46` | `cowrie.command.input` |
| `2026-06-28 22:18:46` | `cowrie.log.closed` |
| `2026-06-28 22:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788e75c941af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:19 |
| **Last Seen** | 2026-06-28 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:19:33` | `cowrie.session.connect` |
| `2026-06-28 22:19:33` | `cowrie.client.version` |
| `2026-06-28 22:19:33` | `cowrie.client.kex` |
| `2026-06-28 22:19:33` | `cowrie.login.success` |
| `2026-06-28 22:19:34` | `cowrie.session.params` |
| `2026-06-28 22:19:34` | `cowrie.command.input` |
| `2026-06-28 22:19:34` | `cowrie.log.closed` |
| `2026-06-28 22:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa60789306bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:20 |
| **Last Seen** | 2026-06-28 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:20:21` | `cowrie.session.connect` |
| `2026-06-28 22:20:21` | `cowrie.client.version` |
| `2026-06-28 22:20:21` | `cowrie.client.kex` |
| `2026-06-28 22:20:22` | `cowrie.login.success` |
| `2026-06-28 22:20:22` | `cowrie.session.params` |
| `2026-06-28 22:20:22` | `cowrie.command.input` |
| `2026-06-28 22:20:22` | `cowrie.log.closed` |
| `2026-06-28 22:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b44cc891d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:20 |
| **Last Seen** | 2026-06-28 22:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:20:55` | `cowrie.session.connect` |
| `2026-06-28 22:20:55` | `cowrie.client.version` |
| `2026-06-28 22:20:55` | `cowrie.client.kex` |
| `2026-06-28 22:20:56` | `cowrie.login.success` |
| `2026-06-28 22:20:57` | `cowrie.session.params` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.success` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.log.closed` |
| `2026-06-28 22:20:57` | `cowrie.session.params` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.input` |
| `2026-06-28 22:20:57` | `cowrie.command.success` |
| `2026-06-28 22:20:58` | `cowrie.log.closed` |
| `2026-06-28 22:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e17491d975

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:21 |
| **Last Seen** | 2026-06-28 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:21:09` | `cowrie.session.connect` |
| `2026-06-28 22:21:09` | `cowrie.client.version` |
| `2026-06-28 22:21:09` | `cowrie.client.kex` |
| `2026-06-28 22:21:09` | `cowrie.login.success` |
| `2026-06-28 22:21:10` | `cowrie.session.params` |
| `2026-06-28 22:21:10` | `cowrie.command.input` |
| `2026-06-28 22:21:10` | `cowrie.log.closed` |
| `2026-06-28 22:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b62c57ed10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:21 |
| **Last Seen** | 2026-06-28 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:21:57` | `cowrie.session.connect` |
| `2026-06-28 22:21:57` | `cowrie.client.version` |
| `2026-06-28 22:21:57` | `cowrie.client.kex` |
| `2026-06-28 22:21:57` | `cowrie.login.success` |
| `2026-06-28 22:21:58` | `cowrie.session.params` |
| `2026-06-28 22:21:58` | `cowrie.command.input` |
| `2026-06-28 22:21:58` | `cowrie.log.closed` |
| `2026-06-28 22:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415007d86c82

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 22:22 |
| **Last Seen** | 2026-06-28 22:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:22:01` | `cowrie.session.connect` |
| `2026-06-28 22:22:02` | `cowrie.client.version` |
| `2026-06-28 22:22:02` | `cowrie.client.kex` |
| `2026-06-28 22:22:04` | `cowrie.login.success` |
| `2026-06-28 22:22:05` | `cowrie.session.params` |
| `2026-06-28 22:22:05` | `cowrie.command.input` |
| `2026-06-28 22:22:05` | `cowrie.log.closed` |
| `2026-06-28 22:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f50a745a56

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:22 |
| **Last Seen** | 2026-06-28 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:22:44` | `cowrie.session.connect` |
| `2026-06-28 22:22:44` | `cowrie.client.version` |
| `2026-06-28 22:22:44` | `cowrie.client.kex` |
| `2026-06-28 22:22:45` | `cowrie.login.success` |
| `2026-06-28 22:22:46` | `cowrie.session.params` |
| `2026-06-28 22:22:46` | `cowrie.command.input` |
| `2026-06-28 22:22:46` | `cowrie.log.closed` |
| `2026-06-28 22:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd68dfceede

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:23 |
| **Last Seen** | 2026-06-28 22:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:23:32` | `cowrie.session.connect` |
| `2026-06-28 22:23:32` | `cowrie.client.version` |
| `2026-06-28 22:23:32` | `cowrie.client.kex` |
| `2026-06-28 22:23:32` | `cowrie.login.success` |
| `2026-06-28 22:23:33` | `cowrie.session.params` |
| `2026-06-28 22:23:33` | `cowrie.command.input` |
| `2026-06-28 22:23:33` | `cowrie.log.closed` |
| `2026-06-28 22:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba76fd1ae3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:23 |
| **Last Seen** | 2026-06-28 22:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:23:53` | `cowrie.session.connect` |
| `2026-06-28 22:23:53` | `cowrie.client.version` |
| `2026-06-28 22:23:53` | `cowrie.client.kex` |
| `2026-06-28 22:23:54` | `cowrie.login.success` |
| `2026-06-28 22:23:55` | `cowrie.session.params` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.success` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.command.input` |
| `2026-06-28 22:23:55` | `cowrie.log.closed` |
| `2026-06-28 22:23:56` | `cowrie.session.params` |
| `2026-06-28 22:23:56` | `cowrie.command.input` |
| `2026-06-28 22:23:56` | `cowrie.command.input` |
| `2026-06-28 22:23:56` | `cowrie.command.success` |
| `2026-06-28 22:23:56` | `cowrie.log.closed` |
| `2026-06-28 22:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83ced2138076

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:24 |
| **Last Seen** | 2026-06-28 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:24:24` | `cowrie.session.connect` |
| `2026-06-28 22:24:24` | `cowrie.client.version` |
| `2026-06-28 22:24:24` | `cowrie.client.kex` |
| `2026-06-28 22:24:25` | `cowrie.login.success` |
| `2026-06-28 22:24:26` | `cowrie.session.params` |
| `2026-06-28 22:24:26` | `cowrie.command.input` |
| `2026-06-28 22:24:26` | `cowrie.log.closed` |
| `2026-06-28 22:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a2e90f7a74

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:25 |
| **Last Seen** | 2026-06-28 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:25:14` | `cowrie.session.connect` |
| `2026-06-28 22:25:14` | `cowrie.client.version` |
| `2026-06-28 22:25:14` | `cowrie.client.kex` |
| `2026-06-28 22:25:15` | `cowrie.login.success` |
| `2026-06-28 22:25:15` | `cowrie.session.params` |
| `2026-06-28 22:25:15` | `cowrie.command.input` |
| `2026-06-28 22:25:16` | `cowrie.log.closed` |
| `2026-06-28 22:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f6219abdf3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:26 |
| **Last Seen** | 2026-06-28 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:26:03` | `cowrie.session.connect` |
| `2026-06-28 22:26:03` | `cowrie.client.version` |
| `2026-06-28 22:26:03` | `cowrie.client.kex` |
| `2026-06-28 22:26:03` | `cowrie.login.success` |
| `2026-06-28 22:26:04` | `cowrie.session.params` |
| `2026-06-28 22:26:04` | `cowrie.command.input` |
| `2026-06-28 22:26:04` | `cowrie.log.closed` |
| `2026-06-28 22:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082829a761a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:26 |
| **Last Seen** | 2026-06-28 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:26:53` | `cowrie.session.connect` |
| `2026-06-28 22:26:53` | `cowrie.client.version` |
| `2026-06-28 22:26:53` | `cowrie.client.kex` |
| `2026-06-28 22:26:53` | `cowrie.login.success` |
| `2026-06-28 22:26:54` | `cowrie.session.params` |
| `2026-06-28 22:26:54` | `cowrie.command.input` |
| `2026-06-28 22:26:54` | `cowrie.log.closed` |
| `2026-06-28 22:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44325af6a145

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:26 |
| **Last Seen** | 2026-06-28 22:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:26:57` | `cowrie.session.connect` |
| `2026-06-28 22:26:57` | `cowrie.client.version` |
| `2026-06-28 22:26:57` | `cowrie.client.kex` |
| `2026-06-28 22:26:58` | `cowrie.login.success` |
| `2026-06-28 22:26:59` | `cowrie.session.params` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.success` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.command.input` |
| `2026-06-28 22:26:59` | `cowrie.log.closed` |
| `2026-06-28 22:27:00` | `cowrie.session.params` |
| `2026-06-28 22:27:00` | `cowrie.command.input` |
| `2026-06-28 22:27:00` | `cowrie.command.input` |
| `2026-06-28 22:27:00` | `cowrie.command.success` |
| `2026-06-28 22:27:00` | `cowrie.log.closed` |
| `2026-06-28 22:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2e45617b3c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:27 |
| **Last Seen** | 2026-06-28 22:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:27:41` | `cowrie.session.connect` |
| `2026-06-28 22:27:41` | `cowrie.client.version` |
| `2026-06-28 22:27:41` | `cowrie.client.kex` |
| `2026-06-28 22:27:41` | `cowrie.login.success` |
| `2026-06-28 22:27:42` | `cowrie.session.params` |
| `2026-06-28 22:27:42` | `cowrie.command.input` |
| `2026-06-28 22:27:42` | `cowrie.log.closed` |
| `2026-06-28 22:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed5d98ca588

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:28 |
| **Last Seen** | 2026-06-28 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:28:29` | `cowrie.session.connect` |
| `2026-06-28 22:28:29` | `cowrie.client.version` |
| `2026-06-28 22:28:29` | `cowrie.client.kex` |
| `2026-06-28 22:28:30` | `cowrie.login.success` |
| `2026-06-28 22:28:31` | `cowrie.session.params` |
| `2026-06-28 22:28:31` | `cowrie.command.input` |
| `2026-06-28 22:28:31` | `cowrie.log.closed` |
| `2026-06-28 22:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bafaa5dcf2fb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 22:29 |
| **Last Seen** | 2026-06-28 22:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:29:15` | `cowrie.session.connect` |
| `2026-06-28 22:29:17` | `cowrie.client.version` |
| `2026-06-28 22:29:17` | `cowrie.client.kex` |
| `2026-06-28 22:29:22` | `cowrie.login.success` |
| `2026-06-28 22:29:25` | `cowrie.session.params` |
| `2026-06-28 22:29:25` | `cowrie.command.input` |
| `2026-06-28 22:29:27` | `cowrie.log.closed` |
| `2026-06-28 22:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d559e04c9054

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:29 |
| **Last Seen** | 2026-06-28 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:29:19` | `cowrie.session.connect` |
| `2026-06-28 22:29:19` | `cowrie.client.version` |
| `2026-06-28 22:29:19` | `cowrie.client.kex` |
| `2026-06-28 22:29:20` | `cowrie.login.success` |
| `2026-06-28 22:29:21` | `cowrie.session.params` |
| `2026-06-28 22:29:21` | `cowrie.command.input` |
| `2026-06-28 22:29:21` | `cowrie.log.closed` |
| `2026-06-28 22:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc447ecda3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:30 |
| **Last Seen** | 2026-06-28 22:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:30:05` | `cowrie.session.connect` |
| `2026-06-28 22:30:05` | `cowrie.client.version` |
| `2026-06-28 22:30:05` | `cowrie.client.kex` |
| `2026-06-28 22:30:05` | `cowrie.login.success` |
| `2026-06-28 22:30:06` | `cowrie.session.params` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.success` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.command.input` |
| `2026-06-28 22:30:06` | `cowrie.log.closed` |
| `2026-06-28 22:30:07` | `cowrie.session.params` |
| `2026-06-28 22:30:07` | `cowrie.command.input` |
| `2026-06-28 22:30:07` | `cowrie.command.input` |
| `2026-06-28 22:30:07` | `cowrie.command.success` |
| `2026-06-28 22:30:07` | `cowrie.log.closed` |
| `2026-06-28 22:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a972c220c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:30 |
| **Last Seen** | 2026-06-28 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:30:09` | `cowrie.session.connect` |
| `2026-06-28 22:30:09` | `cowrie.client.version` |
| `2026-06-28 22:30:10` | `cowrie.client.kex` |
| `2026-06-28 22:30:10` | `cowrie.login.success` |
| `2026-06-28 22:30:11` | `cowrie.session.params` |
| `2026-06-28 22:30:11` | `cowrie.command.input` |
| `2026-06-28 22:30:11` | `cowrie.log.closed` |
| `2026-06-28 22:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d953583eb241

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:31 |
| **Last Seen** | 2026-06-28 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:31:00` | `cowrie.session.connect` |
| `2026-06-28 22:31:00` | `cowrie.client.version` |
| `2026-06-28 22:31:00` | `cowrie.client.kex` |
| `2026-06-28 22:31:00` | `cowrie.login.success` |
| `2026-06-28 22:31:01` | `cowrie.session.params` |
| `2026-06-28 22:31:01` | `cowrie.command.input` |
| `2026-06-28 22:31:01` | `cowrie.log.closed` |
| `2026-06-28 22:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff66f5241d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:31 |
| **Last Seen** | 2026-06-28 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:31:51` | `cowrie.session.connect` |
| `2026-06-28 22:31:51` | `cowrie.client.version` |
| `2026-06-28 22:31:51` | `cowrie.client.kex` |
| `2026-06-28 22:31:51` | `cowrie.login.success` |
| `2026-06-28 22:31:52` | `cowrie.session.params` |
| `2026-06-28 22:31:52` | `cowrie.command.input` |
| `2026-06-28 22:31:52` | `cowrie.log.closed` |
| `2026-06-28 22:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9418f6ad5954

| Field | Detail |
|---|---|
| **Source IP** | `65.181.92[.]228` |
| **First Seen** | 2026-06-28 22:32 |
| **Last Seen** | 2026-06-28 22:33 |
| **Session Duration** | 114s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:32:05` | `cowrie.session.connect` |
| `2026-06-28 22:32:05` | `cowrie.client.version` |
| `2026-06-28 22:32:05` | `cowrie.client.kex` |
| `2026-06-28 22:32:06` | `cowrie.login.success` |
| `2026-06-28 22:33:58` | `cowrie.session.file_upload` |
| `2026-06-28 22:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.92[.]228` to AbuseIPDB if not already reported
- [ ] Block `65.181.92[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b21993f56d29

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:32 |
| **Last Seen** | 2026-06-28 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:32:42` | `cowrie.session.connect` |
| `2026-06-28 22:32:42` | `cowrie.client.version` |
| `2026-06-28 22:32:42` | `cowrie.client.kex` |
| `2026-06-28 22:32:43` | `cowrie.login.success` |
| `2026-06-28 22:32:43` | `cowrie.session.params` |
| `2026-06-28 22:32:43` | `cowrie.command.input` |
| `2026-06-28 22:32:43` | `cowrie.log.closed` |
| `2026-06-28 22:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320ea2089ee2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:33 |
| **Last Seen** | 2026-06-28 22:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:33:23` | `cowrie.session.connect` |
| `2026-06-28 22:33:23` | `cowrie.client.version` |
| `2026-06-28 22:33:23` | `cowrie.client.kex` |
| `2026-06-28 22:33:23` | `cowrie.login.success` |
| `2026-06-28 22:33:24` | `cowrie.session.params` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.success` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.command.input` |
| `2026-06-28 22:33:24` | `cowrie.log.closed` |
| `2026-06-28 22:33:25` | `cowrie.session.params` |
| `2026-06-28 22:33:25` | `cowrie.command.input` |
| `2026-06-28 22:33:25` | `cowrie.command.input` |
| `2026-06-28 22:33:25` | `cowrie.command.success` |
| `2026-06-28 22:33:25` | `cowrie.log.closed` |
| `2026-06-28 22:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c025711bca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:33 |
| **Last Seen** | 2026-06-28 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:33:32` | `cowrie.session.connect` |
| `2026-06-28 22:33:32` | `cowrie.client.version` |
| `2026-06-28 22:33:32` | `cowrie.client.kex` |
| `2026-06-28 22:33:32` | `cowrie.login.success` |
| `2026-06-28 22:33:33` | `cowrie.session.params` |
| `2026-06-28 22:33:33` | `cowrie.command.input` |
| `2026-06-28 22:33:33` | `cowrie.log.closed` |
| `2026-06-28 22:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b880efaa59

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:34 |
| **Last Seen** | 2026-06-28 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:34:22` | `cowrie.session.connect` |
| `2026-06-28 22:34:22` | `cowrie.client.version` |
| `2026-06-28 22:34:22` | `cowrie.client.kex` |
| `2026-06-28 22:34:22` | `cowrie.login.success` |
| `2026-06-28 22:34:23` | `cowrie.session.params` |
| `2026-06-28 22:34:23` | `cowrie.command.input` |
| `2026-06-28 22:34:23` | `cowrie.log.closed` |
| `2026-06-28 22:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fccfc46d2ac0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:35 |
| **Last Seen** | 2026-06-28 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:35:11` | `cowrie.session.connect` |
| `2026-06-28 22:35:11` | `cowrie.client.version` |
| `2026-06-28 22:35:11` | `cowrie.client.kex` |
| `2026-06-28 22:35:11` | `cowrie.login.success` |
| `2026-06-28 22:35:12` | `cowrie.session.params` |
| `2026-06-28 22:35:12` | `cowrie.command.input` |
| `2026-06-28 22:35:12` | `cowrie.log.closed` |
| `2026-06-28 22:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd2b1f93301

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:36 |
| **Last Seen** | 2026-06-28 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:36:00` | `cowrie.session.connect` |
| `2026-06-28 22:36:00` | `cowrie.client.version` |
| `2026-06-28 22:36:00` | `cowrie.client.kex` |
| `2026-06-28 22:36:00` | `cowrie.login.success` |
| `2026-06-28 22:36:01` | `cowrie.session.params` |
| `2026-06-28 22:36:01` | `cowrie.command.input` |
| `2026-06-28 22:36:01` | `cowrie.log.closed` |
| `2026-06-28 22:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0734dc339d0d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 22:36 |
| **Last Seen** | 2026-06-28 22:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:36:23` | `cowrie.session.connect` |
| `2026-06-28 22:36:23` | `cowrie.client.version` |
| `2026-06-28 22:36:23` | `cowrie.client.kex` |
| `2026-06-28 22:36:26` | `cowrie.login.success` |
| `2026-06-28 22:36:28` | `cowrie.session.params` |
| `2026-06-28 22:36:28` | `cowrie.command.input` |
| `2026-06-28 22:36:28` | `cowrie.log.closed` |
| `2026-06-28 22:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac69c492df8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]8` |
| **First Seen** | 2026-06-28 22:36 |
| **Last Seen** | 2026-06-28 22:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:36:23` | `cowrie.session.connect` |
| `2026-06-28 22:36:23` | `cowrie.client.version` |
| `2026-06-28 22:36:23` | `cowrie.client.kex` |
| `2026-06-28 22:36:24` | `cowrie.login.success` |
| `2026-06-28 22:36:25` | `cowrie.session.params` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.success` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.command.input` |
| `2026-06-28 22:36:25` | `cowrie.log.closed` |
| `2026-06-28 22:36:26` | `cowrie.session.params` |
| `2026-06-28 22:36:26` | `cowrie.command.input` |
| `2026-06-28 22:36:26` | `cowrie.command.input` |
| `2026-06-28 22:36:26` | `cowrie.command.success` |
| `2026-06-28 22:36:26` | `cowrie.log.closed` |
| `2026-06-28 22:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]8` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ae189534da

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:36 |
| **Last Seen** | 2026-06-28 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:36:49` | `cowrie.session.connect` |
| `2026-06-28 22:36:49` | `cowrie.client.version` |
| `2026-06-28 22:36:49` | `cowrie.client.kex` |
| `2026-06-28 22:36:50` | `cowrie.login.success` |
| `2026-06-28 22:36:51` | `cowrie.session.params` |
| `2026-06-28 22:36:51` | `cowrie.command.input` |
| `2026-06-28 22:36:51` | `cowrie.log.closed` |
| `2026-06-28 22:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008e5cb0aaf9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:37 |
| **Last Seen** | 2026-06-28 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:37:40` | `cowrie.session.connect` |
| `2026-06-28 22:37:40` | `cowrie.client.version` |
| `2026-06-28 22:37:40` | `cowrie.client.kex` |
| `2026-06-28 22:37:40` | `cowrie.login.success` |
| `2026-06-28 22:37:41` | `cowrie.session.params` |
| `2026-06-28 22:37:41` | `cowrie.command.input` |
| `2026-06-28 22:37:41` | `cowrie.log.closed` |
| `2026-06-28 22:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0443e5e7d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:38 |
| **Last Seen** | 2026-06-28 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:38:30` | `cowrie.session.connect` |
| `2026-06-28 22:38:30` | `cowrie.client.version` |
| `2026-06-28 22:38:30` | `cowrie.client.kex` |
| `2026-06-28 22:38:31` | `cowrie.login.success` |
| `2026-06-28 22:38:31` | `cowrie.session.params` |
| `2026-06-28 22:38:31` | `cowrie.command.input` |
| `2026-06-28 22:38:31` | `cowrie.log.closed` |
| `2026-06-28 22:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a86f509b59c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:39 |
| **Last Seen** | 2026-06-28 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:39:20` | `cowrie.session.connect` |
| `2026-06-28 22:39:20` | `cowrie.client.version` |
| `2026-06-28 22:39:20` | `cowrie.client.kex` |
| `2026-06-28 22:39:21` | `cowrie.login.success` |
| `2026-06-28 22:39:21` | `cowrie.session.params` |
| `2026-06-28 22:39:21` | `cowrie.command.input` |
| `2026-06-28 22:39:22` | `cowrie.log.closed` |
| `2026-06-28 22:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6092a77a098

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:40 |
| **Last Seen** | 2026-06-28 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:40:10` | `cowrie.session.connect` |
| `2026-06-28 22:40:10` | `cowrie.client.version` |
| `2026-06-28 22:40:10` | `cowrie.client.kex` |
| `2026-06-28 22:40:10` | `cowrie.login.success` |
| `2026-06-28 22:40:11` | `cowrie.session.params` |
| `2026-06-28 22:40:11` | `cowrie.command.input` |
| `2026-06-28 22:40:11` | `cowrie.log.closed` |
| `2026-06-28 22:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c479a902891

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 22:40 |
| **Last Seen** | 2026-06-28 22:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:40:27` | `cowrie.session.connect` |
| `2026-06-28 22:40:29` | `cowrie.client.version` |
| `2026-06-28 22:40:29` | `cowrie.client.kex` |
| `2026-06-28 22:40:33` | `cowrie.login.success` |
| `2026-06-28 22:40:37` | `cowrie.session.params` |
| `2026-06-28 22:40:37` | `cowrie.command.input` |
| `2026-06-28 22:40:38` | `cowrie.log.closed` |
| `2026-06-28 22:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a4814d17f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:41 |
| **Last Seen** | 2026-06-28 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:41:00` | `cowrie.session.connect` |
| `2026-06-28 22:41:00` | `cowrie.client.version` |
| `2026-06-28 22:41:00` | `cowrie.client.kex` |
| `2026-06-28 22:41:00` | `cowrie.login.success` |
| `2026-06-28 22:41:01` | `cowrie.session.params` |
| `2026-06-28 22:41:01` | `cowrie.command.input` |
| `2026-06-28 22:41:01` | `cowrie.log.closed` |
| `2026-06-28 22:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-761a32af96c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:41 |
| **Last Seen** | 2026-06-28 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:41:50` | `cowrie.session.connect` |
| `2026-06-28 22:41:50` | `cowrie.client.version` |
| `2026-06-28 22:41:51` | `cowrie.client.kex` |
| `2026-06-28 22:41:51` | `cowrie.login.success` |
| `2026-06-28 22:41:51` | `cowrie.session.params` |
| `2026-06-28 22:41:51` | `cowrie.command.input` |
| `2026-06-28 22:41:52` | `cowrie.log.closed` |
| `2026-06-28 22:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88870c7917f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:42 |
| **Last Seen** | 2026-06-28 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:42:42` | `cowrie.session.connect` |
| `2026-06-28 22:42:42` | `cowrie.client.version` |
| `2026-06-28 22:42:42` | `cowrie.client.kex` |
| `2026-06-28 22:42:42` | `cowrie.login.success` |
| `2026-06-28 22:42:43` | `cowrie.session.params` |
| `2026-06-28 22:42:43` | `cowrie.command.input` |
| `2026-06-28 22:42:43` | `cowrie.log.closed` |
| `2026-06-28 22:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38f0718ba22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:43 |
| **Last Seen** | 2026-06-28 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:43:35` | `cowrie.session.connect` |
| `2026-06-28 22:43:35` | `cowrie.client.version` |
| `2026-06-28 22:43:35` | `cowrie.client.kex` |
| `2026-06-28 22:43:35` | `cowrie.login.success` |
| `2026-06-28 22:43:36` | `cowrie.session.params` |
| `2026-06-28 22:43:36` | `cowrie.command.input` |
| `2026-06-28 22:43:36` | `cowrie.log.closed` |
| `2026-06-28 22:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8506af1b37

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:44 |
| **Last Seen** | 2026-06-28 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:44:28` | `cowrie.session.connect` |
| `2026-06-28 22:44:28` | `cowrie.client.version` |
| `2026-06-28 22:44:28` | `cowrie.client.kex` |
| `2026-06-28 22:44:28` | `cowrie.login.success` |
| `2026-06-28 22:44:29` | `cowrie.session.params` |
| `2026-06-28 22:44:29` | `cowrie.command.input` |
| `2026-06-28 22:44:29` | `cowrie.log.closed` |
| `2026-06-28 22:44:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17bce1ad559c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:45 |
| **Last Seen** | 2026-06-28 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:45:18` | `cowrie.session.connect` |
| `2026-06-28 22:45:18` | `cowrie.client.version` |
| `2026-06-28 22:45:19` | `cowrie.client.kex` |
| `2026-06-28 22:45:19` | `cowrie.login.success` |
| `2026-06-28 22:45:20` | `cowrie.session.params` |
| `2026-06-28 22:45:20` | `cowrie.command.input` |
| `2026-06-28 22:45:20` | `cowrie.log.closed` |
| `2026-06-28 22:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2ec023fd68e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:46 |
| **Last Seen** | 2026-06-28 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:46:10` | `cowrie.session.connect` |
| `2026-06-28 22:46:10` | `cowrie.client.version` |
| `2026-06-28 22:46:10` | `cowrie.client.kex` |
| `2026-06-28 22:46:10` | `cowrie.login.success` |
| `2026-06-28 22:46:11` | `cowrie.session.params` |
| `2026-06-28 22:46:11` | `cowrie.command.input` |
| `2026-06-28 22:46:11` | `cowrie.log.closed` |
| `2026-06-28 22:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2dc1ac082a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:47 |
| **Last Seen** | 2026-06-28 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:47:01` | `cowrie.session.connect` |
| `2026-06-28 22:47:01` | `cowrie.client.version` |
| `2026-06-28 22:47:01` | `cowrie.client.kex` |
| `2026-06-28 22:47:02` | `cowrie.login.success` |
| `2026-06-28 22:47:03` | `cowrie.session.params` |
| `2026-06-28 22:47:03` | `cowrie.command.input` |
| `2026-06-28 22:47:03` | `cowrie.log.closed` |
| `2026-06-28 22:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f6f80b088d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:47 |
| **Last Seen** | 2026-06-28 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:47:53` | `cowrie.session.connect` |
| `2026-06-28 22:47:53` | `cowrie.client.version` |
| `2026-06-28 22:47:53` | `cowrie.client.kex` |
| `2026-06-28 22:47:53` | `cowrie.login.success` |
| `2026-06-28 22:47:54` | `cowrie.session.params` |
| `2026-06-28 22:47:54` | `cowrie.command.input` |
| `2026-06-28 22:47:54` | `cowrie.log.closed` |
| `2026-06-28 22:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d79126732b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:48 |
| **Last Seen** | 2026-06-28 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:48:44` | `cowrie.session.connect` |
| `2026-06-28 22:48:44` | `cowrie.client.version` |
| `2026-06-28 22:48:45` | `cowrie.client.kex` |
| `2026-06-28 22:48:45` | `cowrie.login.success` |
| `2026-06-28 22:48:46` | `cowrie.session.params` |
| `2026-06-28 22:48:46` | `cowrie.command.input` |
| `2026-06-28 22:48:46` | `cowrie.log.closed` |
| `2026-06-28 22:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66d8ce701d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:49 |
| **Last Seen** | 2026-06-28 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:49:37` | `cowrie.session.connect` |
| `2026-06-28 22:49:37` | `cowrie.client.version` |
| `2026-06-28 22:49:37` | `cowrie.client.kex` |
| `2026-06-28 22:49:38` | `cowrie.login.success` |
| `2026-06-28 22:49:38` | `cowrie.session.params` |
| `2026-06-28 22:49:38` | `cowrie.command.input` |
| `2026-06-28 22:49:39` | `cowrie.log.closed` |
| `2026-06-28 22:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec97656d66a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:50 |
| **Last Seen** | 2026-06-28 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:50:31` | `cowrie.session.connect` |
| `2026-06-28 22:50:31` | `cowrie.client.version` |
| `2026-06-28 22:50:31` | `cowrie.client.kex` |
| `2026-06-28 22:50:31` | `cowrie.login.success` |
| `2026-06-28 22:50:32` | `cowrie.session.params` |
| `2026-06-28 22:50:32` | `cowrie.command.input` |
| `2026-06-28 22:50:32` | `cowrie.log.closed` |
| `2026-06-28 22:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d583aa93dc91

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 22:50 |
| **Last Seen** | 2026-06-28 22:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:50:54` | `cowrie.session.connect` |
| `2026-06-28 22:50:54` | `cowrie.client.version` |
| `2026-06-28 22:50:54` | `cowrie.client.kex` |
| `2026-06-28 22:50:56` | `cowrie.login.success` |
| `2026-06-28 22:50:57` | `cowrie.session.params` |
| `2026-06-28 22:50:57` | `cowrie.command.input` |
| `2026-06-28 22:50:58` | `cowrie.log.closed` |
| `2026-06-28 22:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915d43a7ea5b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:51 |
| **Last Seen** | 2026-06-28 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:51:23` | `cowrie.session.connect` |
| `2026-06-28 22:51:23` | `cowrie.client.version` |
| `2026-06-28 22:51:24` | `cowrie.client.kex` |
| `2026-06-28 22:51:24` | `cowrie.login.success` |
| `2026-06-28 22:51:25` | `cowrie.session.params` |
| `2026-06-28 22:51:25` | `cowrie.command.input` |
| `2026-06-28 22:51:25` | `cowrie.log.closed` |
| `2026-06-28 22:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a10b5fd02fe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 22:51 |
| **Last Seen** | 2026-06-28 22:52 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:51:53` | `cowrie.session.connect` |
| `2026-06-28 22:51:55` | `cowrie.client.version` |
| `2026-06-28 22:51:55` | `cowrie.client.kex` |
| `2026-06-28 22:52:01` | `cowrie.login.success` |
| `2026-06-28 22:52:04` | `cowrie.session.params` |
| `2026-06-28 22:52:04` | `cowrie.command.input` |
| `2026-06-28 22:52:06` | `cowrie.log.closed` |
| `2026-06-28 22:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a366ce49112

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:52 |
| **Last Seen** | 2026-06-28 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:52:16` | `cowrie.session.connect` |
| `2026-06-28 22:52:16` | `cowrie.client.version` |
| `2026-06-28 22:52:16` | `cowrie.client.kex` |
| `2026-06-28 22:52:16` | `cowrie.login.success` |
| `2026-06-28 22:52:17` | `cowrie.session.params` |
| `2026-06-28 22:52:17` | `cowrie.command.input` |
| `2026-06-28 22:52:17` | `cowrie.log.closed` |
| `2026-06-28 22:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37224571440

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:53 |
| **Last Seen** | 2026-06-28 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:53:09` | `cowrie.session.connect` |
| `2026-06-28 22:53:09` | `cowrie.client.version` |
| `2026-06-28 22:53:10` | `cowrie.client.kex` |
| `2026-06-28 22:53:10` | `cowrie.login.success` |
| `2026-06-28 22:53:11` | `cowrie.session.params` |
| `2026-06-28 22:53:11` | `cowrie.command.input` |
| `2026-06-28 22:53:11` | `cowrie.log.closed` |
| `2026-06-28 22:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4c36f3c6ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:54 |
| **Last Seen** | 2026-06-28 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:54:02` | `cowrie.session.connect` |
| `2026-06-28 22:54:02` | `cowrie.client.version` |
| `2026-06-28 22:54:02` | `cowrie.client.kex` |
| `2026-06-28 22:54:02` | `cowrie.login.success` |
| `2026-06-28 22:54:03` | `cowrie.session.params` |
| `2026-06-28 22:54:03` | `cowrie.command.input` |
| `2026-06-28 22:54:03` | `cowrie.log.closed` |
| `2026-06-28 22:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2055b4264323

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 22:54 |
| **Last Seen** | 2026-06-28 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 22:54:54` | `cowrie.session.connect` |
| `2026-06-28 22:54:54` | `cowrie.client.version` |
| `2026-06-28 22:54:54` | `cowrie.client.kex` |
| `2026-06-28 22:54:55` | `cowrie.login.success` |
| `2026-06-28 22:54:55` | `cowrie.session.params` |
| `2026-06-28 22:54:55` | `cowrie.command.input` |
| `2026-06-28 22:54:55` | `cowrie.log.closed` |
| `2026-06-28 22:54:55` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **136** | 2026-06-28 20:55 | 2026-06-28 22:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `91.92.40[.]8` | **3** | 2026-06-28 21:15 | 2026-06-28 21:38 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `106.12.172[.]151` | **2** | 2026-06-28 22:51 | 2026-06-28 22:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-28 21:26 | 2026-06-28 22:28 | 1m | 0 | `T1592` | 🟢 LOW |
| `208.109.39[.]19` | **2** | 2026-06-28 22:34 | 2026-06-28 22:34 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-06-28 21:54 | 2026-06-28 21:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `190.55.18[.]68` | 1 | 2026-06-28 21:33 | 2026-06-28 21:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-06-28 20:58 | 2026-06-28 20:59 | 49s | 0 | `T1592` | 🟢 LOW |
| `218.161.62[.]161` | 1 | 2026-06-28 21:53 | 2026-06-28 21:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.210.197[.]34` | 1 | 2026-06-28 22:40 | 2026-06-28 22:40 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `208.109.39[.]19` | US | GoDaddy.com, LLC | **100** ⚠️ | 12 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `218.161.62[.]161` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 5 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `91.92.40[.]8` | NL | TechTies Inc. | **100** ⚠️ | 37 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 19 |
| `103.203.57[.]2` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 220 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 208 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 40 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 39 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 375 cases |
| Tool 34  | Credential Extractor        | ✅ 211 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (4.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 41 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 207 priority case(s) shown individually · 10 recon entry/entries in table (5 group(s) consolidating 145 session(s)).

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
_Report time: 2026-06-28T23:07:35Z_

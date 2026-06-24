# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-24 |
| **Generated At** | 2026-06-24T07:49:33Z |
| **Shift Time** | 07:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **750** |
| Confirmed Threats | **729** |
| False Positives Filtered | **21** (2.8%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **12** |
| High Severity Cases | **417** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **333** |
| Malware Samples Analyzed | **4** HIGH · **24** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **422** |
| Unique Credential Pairs | **371** |
| Unique Usernames | **170** |
| Unique Passwords | **302** |
| Successful Auth Pairs | **381** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 144 |
| `admin` | 31 |
| `ubuntu` | 13 |
| `debian` | 13 |
| `backup` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 23 |
| `password` | 13 |
| `1234` | 9 |
| `smo@@kkklss` | 8 |
| `admin` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 8 |
| `admin` | `admin` | 6 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 4 |
| `admin` | `admin123` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin12` | `91.92.40.231` | 2026-06-24T02:55:25 |
| `test` | `1qaz2wsx#EDC` | `209.99.185.59` | 2026-06-24T02:55:39 |
| `rv` | `rv` | `209.99.185.59` | 2026-06-24T02:56:28 |
| `root` | `Passwd123` | `209.99.185.59` | 2026-06-24T02:57:18 |
| `root` | `R@@tOra12` | `209.99.185.59` | 2026-06-24T02:58:07 |
| `admin` | `admin123` | `91.92.40.231` | 2026-06-24T02:58:35 |
| `wpyan` | `wasd` | `209.99.185.59` | 2026-06-24T02:59:01 |
| `jiangruiyang` | `jiangruiyang2000` | `209.99.185.59` | 2026-06-24T02:59:52 |
| `a3` | `a3` | `45.205.1.42` | 2026-06-24T03:00:13 |
| `root` | `pa` | `209.99.185.59` | 2026-06-24T03:00:44 |
| `ftpuser` | `test` | `209.99.185.59` | 2026-06-24T03:01:39 |
| `admin` | `admin2026` | `91.92.40.231` | 2026-06-24T03:01:50 |
| `gpu02` | `1234` | `209.99.185.59` | 2026-06-24T03:02:32 |
| `deploy` | `1234qwer` | `209.99.185.59` | 2026-06-24T03:03:23 |
| `root` | `admin888` | `209.99.185.59` | 2026-06-24T03:04:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-24T03:05:05 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-24T03:05:05 |
| `root` | `PASS` | `209.99.185.59` | 2026-06-24T03:05:10 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-24T03:05:11 |
| `admin` | `letmein` | `91.92.40.231` | 2026-06-24T03:05:20 |
| `ceshi1` | `666666` | `209.99.185.59` | 2026-06-24T03:06:02 |
| `oracle` | `q1w2e3r4` | `209.99.185.59` | 2026-06-24T03:06:58 |
| `root` | `qwer1234` | `209.99.185.59` | 2026-06-24T03:07:52 |
| `root` | `Password12345` | `209.99.185.59` | 2026-06-24T03:08:44 |
| `admin` | `pa$w0rd` | `91.92.40.231` | 2026-06-24T03:09:04 |
| `dcmdba` | `123456` | `209.99.185.59` | 2026-06-24T03:09:35 |
| `yuanwd` | `111111` | `209.99.185.59` | 2026-06-24T03:10:25 |
| `root` | `adgjmp96` | `209.99.185.59` | 2026-06-24T03:11:16 |
| `matthew` | `matthew` | `209.99.185.59` | 2026-06-24T03:12:10 |
| `admin` | `passw0rd` | `91.92.40.231` | 2026-06-24T03:12:42 |
| `localadmin` | `password` | `209.99.185.59` | 2026-06-24T03:13:02 |
| `root` | `qwertyuiop[]` | `209.99.185.59` | 2026-06-24T03:13:57 |
| `root` | `1029384756` | `45.205.1.42` | 2026-06-24T03:14:48 |
| `root` | `.,mlkjoiu987` | `209.99.185.59` | 2026-06-24T03:14:52 |
| `root` | `aq1sw2de3` | `209.99.185.59` | 2026-06-24T03:15:45 |
| `admin` | `password` | `91.92.40.231` | 2026-06-24T03:16:25 |
| `wangjy` | `wangjy` | `209.99.185.59` | 2026-06-24T03:16:39 |
| `root` | `12qwaszx!@` | `209.99.185.59` | 2026-06-24T03:17:36 |
| `xinyufeng` | `xinyufeng` | `209.99.185.59` | 2026-06-24T03:18:29 |
| `ubuntu` | `1qaz@wsx` | `209.99.185.59` | 2026-06-24T03:19:24 |
| `admin` | `qwerty` | `91.92.40.231` | 2026-06-24T03:19:56 |
| `datacenter` | `12345` | `209.99.185.59` | 2026-06-24T03:20:20 |
| `mingzhong` | `mingzhong` | `209.99.185.59` | 2026-06-24T03:21:15 |
| `root` | `2004` | `209.99.185.59` | 2026-06-24T03:22:10 |
| `moonseok` | `moonseok` | `209.99.185.59` | 2026-06-24T03:23:03 |
| `administrator` | `123456` | `91.92.40.231` | 2026-06-24T03:23:38 |
| `ubuntu` | `aaaaaa` | `209.99.185.59` | 2026-06-24T03:23:57 |
| `root` | `P4$$w0rd` | `209.99.185.59` | 2026-06-24T03:24:52 |
| `root` | `wwwrun` | `209.99.185.59` | 2026-06-24T03:25:48 |
| `root` | `techsupport` | `209.99.185.59` | 2026-06-24T03:26:45 |
| `administrator` | `P@ssw0rd` | `91.92.40.231` | 2026-06-24T03:27:12 |
| `wangfei` | `wangfei` | `209.99.185.59` | 2026-06-24T03:27:42 |
| `wpyan` | `pass1234` | `209.99.185.59` | 2026-06-24T03:28:38 |
| `ubuntu` | `P@55w0rd!` | `45.205.1.42` | 2026-06-24T03:29:27 |
| `apache` | `1q2w3e` | `209.99.185.59` | 2026-06-24T03:29:33 |
| `root` | `ems` | `209.99.185.59` | 2026-06-24T03:30:28 |
| `administrator` | `administrator` | `91.92.40.231` | 2026-06-24T03:30:50 |
| `kb` | `123456` | `209.99.185.59` | 2026-06-24T03:31:23 |
| `deploy` | `pass` | `209.99.185.59` | 2026-06-24T03:32:20 |
| `root` | `741852` | `209.99.185.59` | 2026-06-24T03:33:16 |
| `liuwc` | `liuweichen1996` | `209.99.185.59` | 2026-06-24T03:34:11 |
| `administrator` | `administrator123` | `91.92.40.231` | 2026-06-24T03:34:24 |
| `miner` | `Eminer` | `209.99.185.59` | 2026-06-24T03:35:05 |
| `yuanwd` | `p@ssw0rd` | `209.99.185.59` | 2026-06-24T03:36:00 |
| `root` | `102030` | `209.99.185.59` | 2026-06-24T03:36:55 |
| `root` | `Pass123456789` | `209.99.185.59` | 2026-06-24T03:37:52 |
| `administrator` | `passw0rd` | `91.92.40.231` | 2026-06-24T03:38:17 |
| `sly` | `123` | `209.99.185.59` | 2026-06-24T03:38:49 |
| `smrtanalysis` | `smrtanalysis` | `209.99.185.59` | 2026-06-24T03:39:48 |
| `lys` | `123` | `209.99.185.59` | 2026-06-24T03:40:47 |
| `sourabh` | `sourabh` | `209.99.185.59` | 2026-06-24T03:41:45 |
| `administrator` | `password` | `91.92.40.231` | 2026-06-24T03:42:10 |
| `wjc` | `wjc123` | `209.99.185.59` | 2026-06-24T03:42:41 |
| `retag` | `123456` | `209.99.185.59` | 2026-06-24T03:43:39 |
| `root` | `administrator` | `45.205.1.42` | 2026-06-24T03:44:29 |
| `root` | `t00r` | `209.99.185.59` | 2026-06-24T03:44:38 |
| `root` | `root@000` | `209.99.185.59` | 2026-06-24T03:45:37 |
| `ansible` | `123456` | `91.92.40.231` | 2026-06-24T03:45:47 |
| `root` | `dahuacloud` | `209.99.185.59` | 2026-06-24T03:46:36 |
| `Royce` | `Lyh3HGuXrB` | `209.99.185.59` | 2026-06-24T03:47:35 |
| `akaluy` | `akaluy` | `209.99.185.59` | 2026-06-24T03:48:32 |
| `ansible` | `ansible` | `91.92.40.231` | 2026-06-24T03:49:20 |
| `shijian` | `986339sj` | `209.99.185.59` | 2026-06-24T03:49:30 |
| `ubuntu` | `hadoop12345` | `209.99.185.59` | 2026-06-24T03:50:29 |
| `root` | `!@#$` | `209.99.185.59` | 2026-06-24T03:51:29 |
| `root` | `1z2x3c4v5b6n7m` | `209.99.185.59` | 2026-06-24T03:52:30 |
| `ansible` | `ansible123` | `91.92.40.231` | 2026-06-24T03:53:01 |
| `root` | `yes` | `209.99.185.59` | 2026-06-24T03:53:30 |
| `root` | `madison` | `209.99.185.59` | 2026-06-24T03:54:30 |
| `guoshufei` | `guoshufei` | `209.99.185.59` | 2026-06-24T03:55:33 |
| `postgres` | `Florinlaur2005` | `209.99.185.59` | 2026-06-24T03:56:33 |
| `ansible` | `passw0rd` | `91.92.40.231` | 2026-06-24T03:56:44 |
| `root` | `Qaz2wsx` | `209.99.185.59` | 2026-06-24T03:57:36 |
| `root` | `sales123` | `209.99.185.59` | 2026-06-24T03:58:39 |
| `nagios` | `123456` | `45.205.1.42` | 2026-06-24T03:59:13 |
| `ubuntu` | `111111` | `209.99.185.59` | 2026-06-24T03:59:39 |
| `ansible` | `password` | `91.92.40.231` | 2026-06-24T04:00:21 |
| `deployer` | `12345678` | `209.99.185.59` | 2026-06-24T04:00:36 |
| `kyw` | `kyw` | `209.99.185.59` | 2026-06-24T04:01:21 |
| `root` | `123meklozed` | `209.99.185.59` | 2026-06-24T04:02:05 |
| `root` | `abc123Z` | `209.99.185.59` | 2026-06-24T04:02:52 |
| `wq` | `wq` | `209.99.185.59` | 2026-06-24T04:03:38 |
| `apache` | `P@ssw0rd` | `91.92.40.231` | 2026-06-24T04:04:03 |
| `shenao` | `shenao123456` | `209.99.185.59` | 2026-06-24T04:04:25 |
| `shkim` | `1234` | `209.99.185.59` | 2026-06-24T04:05:13 |
| `yuanchengbo` | `123456` | `209.99.185.59` | 2026-06-24T04:06:00 |
| `root` | `SUST21@dmission` | `209.99.185.59` | 2026-06-24T04:06:48 |
| `flq20` | `flq294357` | `209.99.185.59` | 2026-06-24T04:07:34 |
| `apache` | `apache` | `91.92.40.231` | 2026-06-24T04:07:37 |
| `root` | `121314` | `209.99.185.59` | 2026-06-24T04:08:19 |
| `root` | `'Re$tSt0rM123#321'` | `209.99.185.59` | 2026-06-24T04:09:06 |
| `whn` | `Whn123456` | `209.99.185.59` | 2026-06-24T04:09:52 |
| `bank` | `bank123` | `209.99.185.59` | 2026-06-24T04:10:40 |
| `apache` | `password` | `91.92.40.231` | 2026-06-24T04:11:12 |
| `root` | `nyh4rfv%TGB6` | `209.99.185.59` | 2026-06-24T04:11:29 |
| `lee` | `lee` | `209.99.185.59` | 2026-06-24T04:12:17 |
| `ZhangZhijian` | `zhangzhijian` | `209.99.185.59` | 2026-06-24T04:13:04 |
| `rudolfxx` | `1212xxxx` | `209.99.185.59` | 2026-06-24T04:13:50 |
| `oracle` | `iloveyou1` | `45.205.1.42` | 2026-06-24T04:13:59 |
| `root` | `P@ssw0rds` | `209.99.185.59` | 2026-06-24T04:14:36 |
| `backup` | `123qwe` | `91.92.40.231` | 2026-06-24T04:14:46 |
| `root` | `Pass0wrd` | `209.99.185.59` | 2026-06-24T04:15:23 |
| `gyf-srt` | `gaoyifan` | `209.99.185.59` | 2026-06-24T04:16:11 |
| `root` | `roots` | `209.99.185.59` | 2026-06-24T04:17:00 |
| `cug` | `123456` | `209.99.185.59` | 2026-06-24T04:17:50 |
| `backup` | `54321` | `91.92.40.231` | 2026-06-24T04:18:27 |
| `root` | `arschloch` | `209.99.185.59` | 2026-06-24T04:18:39 |
| `root` | `tttttt` | `209.99.185.59` | 2026-06-24T04:19:27 |
| `root` | `PasswOrd0` | `209.99.185.59` | 2026-06-24T04:20:16 |
| `root` | `g_czechout` | `209.99.185.59` | 2026-06-24T04:21:02 |
| `flw` | `fulgercsmode123` | `209.99.185.59` | 2026-06-24T04:21:50 |
| `backup` | `backup` | `91.92.40.231` | 2026-06-24T04:22:05 |
| `jchang` | `620655` | `209.99.185.59` | 2026-06-24T04:22:40 |
| `xzy` | `xzy123` | `209.99.185.59` | 2026-06-24T04:23:32 |
| `Wwk` | `111111` | `209.99.185.59` | 2026-06-24T04:24:22 |
| `root` | `qwe123QWE123` | `209.99.185.59` | 2026-06-24T04:25:11 |
| `backup` | `backup12` | `91.92.40.231` | 2026-06-24T04:25:40 |
| `root` | `abcd12345` | `209.99.185.59` | 2026-06-24T04:25:59 |
| `www-data` | `111111` | `209.99.185.59` | 2026-06-24T04:26:46 |
| `lyb` | `lyb` | `209.99.185.59` | 2026-06-24T04:27:32 |
| `zalend` | `zalend12345678` | `209.99.185.59` | 2026-06-24T04:28:19 |
| `root` | `PasswOrd` | `45.205.1.42` | 2026-06-24T04:28:45 |
| `root` | `rasberry` | `209.99.185.59` | 2026-06-24T04:29:07 |
| `backup` | `backup123` | `91.92.40.231` | 2026-06-24T04:29:18 |
| `root` | `zdxfcgvh` | `209.99.185.59` | 2026-06-24T04:29:57 |
| `root` | `Root!23` | `209.99.185.59` | 2026-06-24T04:30:46 |
| `root` | `1qaz2wsx!QAZ@WSX` | `209.99.185.59` | 2026-06-24T04:31:35 |
| `root` | `---fuck_you----` | `5.34.215.6` | 2026-06-24T04:31:36 |
| `lflenguser3` | `LflE202306` | `209.99.185.59` | 2026-06-24T04:32:24 |
| `backup` | `password` | `91.92.40.231` | 2026-06-24T04:32:58 |
| `ubuntu` | `abc1234567` | `209.99.185.59` | 2026-06-24T04:33:14 |
| `admin1` | `admin1123` | `209.99.185.59` | 2026-06-24T04:34:05 |
| `vps` | `passpass` | `209.99.185.59` | 2026-06-24T04:34:55 |
| `pc` | `computer` | `209.99.185.59` | 2026-06-24T04:35:46 |
| `root` | `ubuntu` | `209.99.185.59` | 2026-06-24T04:36:37 |
| `backup` | `wasd` | `91.92.40.231` | 2026-06-24T04:36:40 |
| `public` | `public123` | `209.99.185.59` | 2026-06-24T04:37:28 |
| `root` | `stdadmin@muk` | `209.99.185.59` | 2026-06-24T04:38:17 |
| `debian` | `password` | `209.99.185.59` | 2026-06-24T04:39:05 |
| `root` | `Admin@888` | `209.99.185.59` | 2026-06-24T04:39:54 |
| `centos` | `centos` | `91.92.40.231` | 2026-06-24T04:40:18 |
| `ubuntu` | `pa$$w0rd1` | `209.99.185.59` | 2026-06-24T04:40:42 |
| `zzr` | `123` | `209.99.185.59` | 2026-06-24T04:41:31 |
| `cxs` | `cxs123` | `209.99.185.59` | 2026-06-24T04:42:21 |
| `root` | `Pass@5rdx` | `209.99.185.59` | 2026-06-24T04:43:10 |
| `root` | `cambiami` | `45.205.1.42` | 2026-06-24T04:43:42 |
| `centos` | `centos123` | `91.92.40.231` | 2026-06-24T04:43:50 |
| `cz` | `cz123456` | `209.99.185.59` | 2026-06-24T04:43:59 |
| `xwang` | `xwang` | `209.99.185.59` | 2026-06-24T04:44:48 |
| `root` | `1qaz@WSX3edc` | `209.99.185.59` | 2026-06-24T04:45:38 |
| `admin` | `admin` | `83.136.251.36` | 2026-06-24T04:46:13 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-24T04:46:13 |
| `root` | `rootuser` | `209.99.185.59` | 2026-06-24T04:46:26 |
| `root` | `poiuytrew` | `209.99.185.59` | 2026-06-24T04:47:16 |
| `debian` | `123456` | `91.92.40.231` | 2026-06-24T04:47:32 |
| `chenqian` | `chenqian` | `209.99.185.59` | 2026-06-24T04:48:06 |
| `root` | `PASSWD` | `209.99.185.59` | 2026-06-24T04:48:58 |
| `admin` | `admin` | `34.62.154.45` | 2026-06-24T04:49:46 |
| `tesoreria` | `tesoreria` | `209.99.185.59` | 2026-06-24T04:49:50 |
| `femas` | `femas` | `209.99.185.59` | 2026-06-24T04:50:40 |
| `debian` | `123qwe` | `91.92.40.231` | 2026-06-24T04:51:18 |
| `jhd` | `1993827jhd` | `209.99.185.59` | 2026-06-24T04:51:30 |
| `root` | `sa369` | `209.99.185.59` | 2026-06-24T04:52:19 |
| `root` | `Qazwsxedcrfv` | `209.99.185.59` | 2026-06-24T04:53:09 |
| `rain` | `1234` | `209.99.185.59` | 2026-06-24T04:54:00 |
| `shr` | `shr` | `209.99.185.59` | 2026-06-24T04:54:51 |
| `debian` | `54321` | `91.92.40.231` | 2026-06-24T04:54:58 |
| `mike0295` | `1234` | `209.99.185.59` | 2026-06-24T04:55:45 |
| `web` | `123456` | `209.99.185.59` | 2026-06-24T04:56:37 |
| `root` | `liangliang` | `209.99.185.59` | 2026-06-24T04:57:28 |
| `root` | `traffic` | `209.99.185.59` | 2026-06-24T04:58:18 |
| `ubuntu` | `P@$$W0RD` | `45.205.1.42` | 2026-06-24T04:58:40 |
| `debian` | `654321` | `91.92.40.231` | 2026-06-24T04:58:44 |
| `root` | `WaPBBS` | `209.99.185.59` | 2026-06-24T04:59:09 |
| `oracle` | `!@#$%^` | `209.99.185.59` | 2026-06-24T05:00:03 |
| `root` | `P@ssw0rd#123` | `209.99.185.59` | 2026-06-24T05:00:58 |
| `adm02` | `adm02` | `209.99.185.59` | 2026-06-24T05:01:54 |
| `debian` | `debian` | `91.92.40.231` | 2026-06-24T05:02:27 |
| `root` | `ruijie@123` | `209.99.185.59` | 2026-06-24T05:02:50 |
| `eda_outsource2` | `EDAOutsource123` | `209.99.185.59` | 2026-06-24T05:03:48 |
| `root` | `santiago` | `209.99.185.59` | 2026-06-24T05:04:40 |
| `es` | `password` | `209.99.185.59` | 2026-06-24T05:05:32 |
| `debian` | `debian12` | `91.92.40.231` | 2026-06-24T05:06:11 |
| `testuser` | `654321` | `209.99.185.59` | 2026-06-24T05:06:24 |
| `root` | `P@ssw0rd!@` | `209.99.185.59` | 2026-06-24T05:07:17 |
| `admin` | `admin` | `194.26.101.146` | 2026-06-24T05:08:15 |
| `test10` | `test10` | `209.99.185.59` | 2026-06-24T05:08:15 |
| `admin` | `` | `194.26.101.146` | 2026-06-24T05:08:19 |
| `admin` | `password` | `194.26.101.146` | 2026-06-24T05:08:19 |
| `admin` | `1234` | `194.26.101.146` | 2026-06-24T05:08:21 |
| `admin` | `12345` | `194.26.101.146` | 2026-06-24T05:08:21 |
| `admin` | `123456` | `194.26.101.146` | 2026-06-24T05:08:23 |
| `admin` | `admin123` | `194.26.101.146` | 2026-06-24T05:08:26 |
| `root` | `admin` | `194.26.101.146` | 2026-06-24T05:08:28 |
| `root` | `` | `194.26.101.146` | 2026-06-24T05:08:28 |
| `root` | `1234` | `194.26.101.146` | 2026-06-24T05:08:28 |
| `root` | `toor` | `194.26.101.146` | 2026-06-24T05:08:32 |
| `root` | `12345` | `194.26.101.146` | 2026-06-24T05:08:35 |
| `user` | `user` | `194.26.101.146` | 2026-06-24T05:08:35 |
| `user` | `password` | `194.26.101.146` | 2026-06-24T05:08:36 |
| `guest` | `guest` | `194.26.101.146` | 2026-06-24T05:08:36 |
| `support` | `support` | `194.26.101.146` | 2026-06-24T05:08:39 |
| `tech` | `tech` | `194.26.101.146` | 2026-06-24T05:08:39 |
| `manager` | `manager` | `194.26.101.146` | 2026-06-24T05:08:43 |
| `cisco` | `cisco` | `194.26.101.146` | 2026-06-24T05:08:45 |
| `cisco` | `` | `194.26.101.146` | 2026-06-24T05:08:45 |
| `enable` | `enable` | `194.26.101.146` | 2026-06-24T05:08:46 |
| `kali` | `kali` | `194.26.101.146` | 2026-06-24T05:08:47 |
| `pi` | `raspberry` | `194.26.101.146` | 2026-06-24T05:08:49 |
| `ubnt` | `ubnt` | `194.26.101.146` | 2026-06-24T05:08:53 |
| `admin` | `123` | `194.26.101.146` | 2026-06-24T05:08:53 |
| `bin` | `bin` | `194.26.101.146` | 2026-06-24T05:08:55 |
| `admin` | `0` | `194.26.101.146` | 2026-06-24T05:08:55 |
| `root` | `qwertyasdfghzxcvbn` | `209.99.185.59` | 2026-06-24T05:09:09 |
| `debian` | `debian123` | `91.92.40.231` | 2026-06-24T05:10:00 |
| `root` | `!@#qweASD` | `209.99.185.59` | 2026-06-24T05:10:03 |
| `lihui` | `lihui123456` | `209.99.185.59` | 2026-06-24T05:10:54 |
| `root` | `cambiami` | `209.99.185.59` | 2026-06-24T05:11:46 |
| `ubuntu` | `admin1121` | `209.99.185.59` | 2026-06-24T05:12:40 |
| `jcye` | `yejiachen8` | `209.99.185.59` | 2026-06-24T05:13:36 |
| `ubuntu` | `pa$$w0rd123` | `45.205.1.42` | 2026-06-24T05:13:39 |
| `debian` | `debian2026` | `91.92.40.231` | 2026-06-24T05:13:51 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-24T05:13:55 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-24T05:13:55 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-24T05:13:56 |
| `root` | `0123456` | `209.99.185.59` | 2026-06-24T05:14:35 |
| `hts` | `hts` | `209.99.185.59` | 2026-06-24T05:15:30 |
| `bai` | `bai` | `209.99.185.59` | 2026-06-24T05:16:23 |
| `root` | `Latinexpress123$` | `209.99.185.59` | 2026-06-24T05:17:16 |
| `debian` | `letmein` | `91.92.40.231` | 2026-06-24T05:17:34 |
| `root` | `toor@123` | `209.99.185.59` | 2026-06-24T05:18:10 |
| `localhost` | `123456` | `209.99.185.59` | 2026-06-24T05:19:05 |
| `omnisky` | `med432rt654321` | `209.99.185.59` | 2026-06-24T05:20:01 |
| `nexus` | `123456` | `209.99.185.59` | 2026-06-24T05:21:02 |
| `debian` | `pa55word` | `91.92.40.231` | 2026-06-24T05:21:29 |
| `wechat` | `wechat` | `209.99.185.59` | 2026-06-24T05:21:58 |
| `root` | `1qaz1q` | `209.99.185.59` | 2026-06-24T05:22:59 |
| `root` | `qweASD!@#` | `209.99.185.59` | 2026-06-24T05:23:53 |
| `root` | `JLdsj@123!@#` | `209.99.185.59` | 2026-06-24T05:24:48 |
| `debian` | `password` | `91.92.40.231` | 2026-06-24T05:25:19 |
| `zhonzhou` | `111111` | `209.99.185.59` | 2026-06-24T05:25:43 |
| `databse` | `database` | `209.99.185.59` | 2026-06-24T05:26:44 |
| `monitor` | `1234` | `209.99.185.59` | 2026-06-24T05:27:43 |
| `root` | `qwerzxcv` | `45.205.1.42` | 2026-06-24T05:28:26 |
| `gyl` | `gyl` | `209.99.185.59` | 2026-06-24T05:28:39 |
| `debian` | `qwerty` | `91.92.40.231` | 2026-06-24T05:29:03 |
| `root` | `QAZ@WSX` | `209.99.185.59` | 2026-06-24T05:29:34 |
| `haowl` | `haowl123` | `209.99.185.59` | 2026-06-24T05:30:29 |
| `chentianyang` | `bitcq-cty2022` | `209.99.185.59` | 2026-06-24T05:31:26 |
| `fengyingchao` | `fengyingchao111111` | `209.99.185.59` | 2026-06-24T05:32:24 |
| `dev` | `123qwe` | `91.92.40.231` | 2026-06-24T05:32:45 |
| `aaaaaa` | `222222` | `209.99.185.59` | 2026-06-24T05:33:22 |
| `ubuntu` | `1234qwer`` | `209.99.185.59` | 2026-06-24T05:34:21 |
| `root` | `` | `176.65.139.44` | 2026-06-24T05:34:47 |
| `oracle` | `qazwsxedc` | `209.99.185.59` | 2026-06-24T05:35:18 |
| `root` | `tsserver` | `209.99.185.59` | 2026-06-24T05:36:16 |
| `dev` | `123qwerty` | `91.92.40.231` | 2026-06-24T05:36:30 |
| `scz` | `123456` | `209.99.185.59` | 2026-06-24T05:37:13 |
| `tianxn1` | `XC68elF` | `209.99.185.59` | 2026-06-24T05:38:10 |
| `ecnu` | `ecnu@123` | `209.99.185.59` | 2026-06-24T05:39:08 |
| `dev` | `54321` | `91.92.40.231` | 2026-06-24T05:40:13 |
| `root` | `secure` | `209.99.185.59` | 2026-06-24T05:41:11 |
| `ZXDSL` | `ZXDSL` | `209.99.185.59` | 2026-06-24T05:42:09 |
| `root` | `P@ssword123!` | `45.205.1.42` | 2026-06-24T05:42:50 |
| `root` | `qaz123456` | `209.99.185.59` | 2026-06-24T05:43:06 |
| `lyp` | `123456` | `209.99.185.59` | 2026-06-24T05:44:06 |
| `dev` | `dev` | `91.92.40.231` | 2026-06-24T05:44:09 |
| `linchunli` | `333333` | `209.99.185.59` | 2026-06-24T05:45:05 |
| `cxs` | `cxs` | `209.99.185.59` | 2026-06-24T05:46:03 |
| `xr` | `xr123` | `209.99.185.59` | 2026-06-24T05:47:01 |
| `root` | `qwer!@#123` | `209.99.185.59` | 2026-06-24T05:48:00 |
| `dev` | `dev1` | `91.92.40.231` | 2026-06-24T05:48:05 |
| `localadmin` | `changeme123` | `209.99.185.59` | 2026-06-24T05:48:57 |
| `test1` | `12345` | `209.99.185.59` | 2026-06-24T05:49:52 |
| `zabbix` | `1234567` | `209.99.185.59` | 2026-06-24T05:50:49 |
| `grid` | `grid123` | `209.99.185.59` | 2026-06-24T05:51:47 |
| `dev` | `dev123` | `91.92.40.231` | 2026-06-24T05:51:59 |
| `root` | `!@#qweasd` | `209.99.185.59` | 2026-06-24T05:52:47 |
| `chenzy` | `czy803803` | `209.99.185.59` | 2026-06-24T05:53:46 |
| `ttt` | `ttt` | `209.99.185.59` | 2026-06-24T05:54:45 |
| `dev` | `qwerty` | `91.92.40.231` | 2026-06-24T05:55:43 |
| `testuser` | `pass1234` | `209.99.185.59` | 2026-06-24T05:55:45 |
| `user1` | `User1@123` | `209.99.185.59` | 2026-06-24T05:56:44 |
| `httpd` | `httpd` | `45.205.1.42` | 2026-06-24T05:57:34 |
| `shenlei` | `199625sL` | `209.99.185.59` | 2026-06-24T05:57:41 |
| `root` | `qwertyui` | `209.99.185.59` | 2026-06-24T05:58:39 |
| `developer` | `developer` | `91.92.40.231` | 2026-06-24T05:59:30 |
| `ho` | `0000` | `209.99.185.59` | 2026-06-24T05:59:38 |
| `wf` | `123456` | `209.99.185.59` | 2026-06-24T06:00:31 |
| `root` | `ro!QAZ2wsx` | `209.99.185.59` | 2026-06-24T06:01:16 |
| `xt` | `xt` | `209.99.185.59` | 2026-06-24T06:02:01 |
| `sheepdog` | `111111` | `209.99.185.59` | 2026-06-24T06:02:46 |
| `root` | `2025` | `209.99.185.59` | 2026-06-24T06:03:32 |
| `root` | `123987` | `209.99.185.59` | 2026-06-24T06:04:19 |
| `root` | `hustle2live` | `10.0.0.73` | 2026-06-24T06:04:24 |
| `dws` | `dws` | `209.99.185.59` | 2026-06-24T06:05:06 |
| `mpr` | `mpr` | `209.99.185.59` | 2026-06-24T06:05:54 |
| `csh` | `123456` | `209.99.185.59` | 2026-06-24T06:06:42 |
| `root` | `qwert1234567890` | `209.99.185.59` | 2026-06-24T06:07:29 |
| `zqc` | `zqc2021` | `209.99.185.59` | 2026-06-24T06:08:16 |
| `root` | `router` | `209.99.185.59` | 2026-06-24T06:09:01 |
| `root` | `asdqwe123` | `209.99.185.59` | 2026-06-24T06:09:47 |
| `postgres` | `postgres1` | `209.99.185.59` | 2026-06-24T06:10:34 |
| `root` | `qweqwe!@#` | `209.99.185.59` | 2026-06-24T06:11:21 |
| `ubuntu` | `abcdefg` | `45.205.1.42` | 2026-06-24T06:12:08 |
| `root` | `aqwzsxedc` | `209.99.185.59` | 2026-06-24T06:12:10 |
| `syslog` | `syslog` | `209.99.185.59` | 2026-06-24T06:12:58 |
| `zhanchongming` | `123456` | `209.99.185.59` | 2026-06-24T06:13:45 |
| `dek` | `123456` | `209.99.185.59` | 2026-06-24T06:14:33 |
| `luoyx66` | `wojiaofs.66` | `209.99.185.59` | 2026-06-24T06:15:19 |
| `dell` | `dell321` | `209.99.185.59` | 2026-06-24T06:16:06 |
| `navidad2` | `navidad2` | `209.99.185.59` | 2026-06-24T06:16:54 |
| `szu` | `123456` | `209.99.185.59` | 2026-06-24T06:17:43 |
| `shaoruizhi` | `33txdy` | `209.99.185.59` | 2026-06-24T06:18:34 |
| `local` | `123qwe` | `209.99.185.59` | 2026-06-24T06:19:27 |
| `shutinggu2` | `shutinggu2` | `209.99.185.59` | 2026-06-24T06:20:15 |
| `root` | `P@$$w0rD` | `209.99.185.59` | 2026-06-24T06:21:07 |
| `sysall` | `fuckoff` | `209.99.185.59` | 2026-06-24T06:21:58 |
| `xubangyong` | `xubangyong` | `209.99.185.59` | 2026-06-24T06:22:47 |
| `licong` | `licong` | `209.99.185.59` | 2026-06-24T06:23:36 |
| `potok` | `0` | `209.99.185.59` | 2026-06-24T06:24:27 |
| `quwei` | `220103nimeiaQW` | `209.99.185.59` | 2026-06-24T06:25:17 |
| `root` | `7ujm9ol>.P;/` | `209.99.185.59` | 2026-06-24T06:26:08 |
| `root` | `q1w2e3r4t5y6` | `45.205.1.42` | 2026-06-24T06:26:28 |
| `root` | `missionimposible` | `209.99.185.59` | 2026-06-24T06:26:58 |
| `pxj-huangdawei` | `pxj-huangdawei` | `209.99.185.59` | 2026-06-24T06:27:48 |
| `root` | `!QAZ1qaz1234` | `209.99.185.59` | 2026-06-24T06:28:42 |
| `user` | `0123` | `209.99.185.59` | 2026-06-24T06:29:32 |
| `root` | `123456!Aa` | `209.99.185.59` | 2026-06-24T06:30:26 |
| `root` | `nicolas` | `209.99.185.59` | 2026-06-24T06:31:18 |
| `root` | `root@6000` | `209.99.185.59` | 2026-06-24T06:32:08 |
| `wyt` | `wyt` | `209.99.185.59` | 2026-06-24T06:32:57 |
| `dell` | `admin@4444` | `209.99.185.59` | 2026-06-24T06:33:49 |
| `root` | `﻿------fuck------` | `180.76.61.232` | 2026-06-24T06:34:41 |
| `jiangyue` | `jiangyue` | `209.99.185.59` | 2026-06-24T06:34:44 |
| `lj` | `lj` | `209.99.185.59` | 2026-06-24T06:35:33 |
| `nagios` | `nagiosnagios` | `209.99.185.59` | 2026-06-24T06:36:22 |
| `zhangxinkui` | `0` | `209.99.185.59` | 2026-06-24T06:37:12 |
| `WhiSKy` | `WUUn0hMsLk` | `209.99.185.59` | 2026-06-24T06:38:02 |
| `admin` | `admin` | `85.215.192.100` | 2026-06-24T06:38:23 |
| `root` | `passadmin` | `209.99.185.59` | 2026-06-24T06:38:52 |
| `radu` | `radu123` | `209.99.185.59` | 2026-06-24T06:39:40 |
| `zhaoyu` | `zhaoyu` | `209.99.185.59` | 2026-06-24T06:40:28 |
| `yangliusha9` | `yangliusha9` | `45.205.1.42` | 2026-06-24T06:40:48 |
| `admin` | `Cliri$R00t` | `209.99.185.59` | 2026-06-24T06:41:17 |
| `ubuntu` | `qweasd789` | `209.99.185.59` | 2026-06-24T06:42:05 |
| `root` | `!@#$%^&*` | `209.99.185.59` | 2026-06-24T06:42:55 |
| `root` | `univers` | `209.99.185.59` | 2026-06-24T06:43:46 |
| `peer` | `0` | `209.99.185.59` | 2026-06-24T06:44:36 |
| `fengjuexiao` | `123123123456` | `209.99.185.59` | 2026-06-24T06:45:28 |
| `root` | `P@ssword123` | `209.99.185.59` | 2026-06-24T06:46:23 |
| `root` | `Aa@123` | `209.99.185.59` | 2026-06-24T06:47:13 |
| `hzq` | `hzq` | `209.99.185.59` | 2026-06-24T06:48:06 |
| `zhanghua` | `zhanghua321` | `209.99.185.59` | 2026-06-24T06:48:57 |
| `chenwei` | `123456` | `209.99.185.59` | 2026-06-24T06:49:50 |
| `local` | `12345678` | `209.99.185.59` | 2026-06-24T06:50:43 |
| `root` | `qawzse` | `209.99.185.59` | 2026-06-24T06:51:33 |
| `aaaaaa` | `0` | `209.99.185.59` | 2026-06-24T06:52:21 |
| `root` | `123!@#qweQWE` | `209.99.185.59` | 2026-06-24T06:53:09 |
| `JiaYuxin` | `JiaYuxn` | `209.99.185.59` | 2026-06-24T06:53:57 |
| `fax` | `fax123` | `209.99.185.59` | 2026-06-24T06:54:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **750** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 348 |
| Paramiko (Python) | 44 |
| libssh | 18 |
| Nmap scanner | 4 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 291 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 51 | 1 |
| `6372ee695756...` | Modern SSH client | 28 | 1 |
| `a2de0f306611...` | Mirai/variant | 16 | 2 |
| `e788c657d1a2...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 291 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 51 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 28 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 16 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 16 | 7 | — |
| `e788c657d1a2...` | Nmap scanner | 4 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 51 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

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
echo 'admin12' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `91.92.40.231`

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
Source IPs: `176.65.139.44`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **28** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS56041` | China Mobile communications corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (416)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9201334405f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 02:55 |
| **Last Seen** | 2026-06-24 02:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin12' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:55:20` | `cowrie.session.connect` |
| `2026-06-24 02:55:21` | `cowrie.client.version` |
| `2026-06-24 02:55:21` | `cowrie.client.kex` |
| `2026-06-24 02:55:25` | `cowrie.login.success` |
| `2026-06-24 02:55:27` | `cowrie.session.params` |
| `2026-06-24 02:55:27` | `cowrie.command.input` |
| `2026-06-24 02:55:27` | `cowrie.command.input` |
| `2026-06-24 02:55:27` | `cowrie.command.input` |
| `2026-06-24 02:55:27` | `cowrie.command.input` |
| `2026-06-24 02:55:28` | `cowrie.log.closed` |
| `2026-06-24 02:55:32` | `cowrie.session.params` |
| `2026-06-24 02:55:32` | `cowrie.command.input` |
| `2026-06-24 02:55:32` | `cowrie.command.input` |
| `2026-06-24 02:55:32` | `cowrie.command.failed` |
| `2026-06-24 02:55:32` | `cowrie.command.failed` |
| `2026-06-24 02:55:32` | `cowrie.command.failed` |
| `2026-06-24 02:55:32` | `cowrie.command.failed` |
| `2026-06-24 02:55:33` | `cowrie.log.closed` |
| `2026-06-24 02:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d58ed790e2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 02:55 |
| **Last Seen** | 2026-06-24 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:55:38` | `cowrie.session.connect` |
| `2026-06-24 02:55:38` | `cowrie.client.version` |
| `2026-06-24 02:55:39` | `cowrie.client.kex` |
| `2026-06-24 02:55:39` | `cowrie.login.success` |
| `2026-06-24 02:55:40` | `cowrie.session.params` |
| `2026-06-24 02:55:40` | `cowrie.command.input` |
| `2026-06-24 02:55:40` | `cowrie.log.closed` |
| `2026-06-24 02:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35738cff7c54

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 02:56 |
| **Last Seen** | 2026-06-24 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:56:28` | `cowrie.session.connect` |
| `2026-06-24 02:56:28` | `cowrie.client.version` |
| `2026-06-24 02:56:28` | `cowrie.client.kex` |
| `2026-06-24 02:56:28` | `cowrie.login.success` |
| `2026-06-24 02:56:29` | `cowrie.session.params` |
| `2026-06-24 02:56:29` | `cowrie.command.input` |
| `2026-06-24 02:56:29` | `cowrie.log.closed` |
| `2026-06-24 02:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5272653bdee6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 02:57 |
| **Last Seen** | 2026-06-24 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:57:17` | `cowrie.session.connect` |
| `2026-06-24 02:57:17` | `cowrie.client.version` |
| `2026-06-24 02:57:17` | `cowrie.client.kex` |
| `2026-06-24 02:57:18` | `cowrie.login.success` |
| `2026-06-24 02:57:18` | `cowrie.session.params` |
| `2026-06-24 02:57:18` | `cowrie.command.input` |
| `2026-06-24 02:57:18` | `cowrie.log.closed` |
| `2026-06-24 02:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8469a4abecf3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 02:58 |
| **Last Seen** | 2026-06-24 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:58:07` | `cowrie.session.connect` |
| `2026-06-24 02:58:07` | `cowrie.client.version` |
| `2026-06-24 02:58:07` | `cowrie.client.kex` |
| `2026-06-24 02:58:07` | `cowrie.login.success` |
| `2026-06-24 02:58:08` | `cowrie.session.params` |
| `2026-06-24 02:58:08` | `cowrie.command.input` |
| `2026-06-24 02:58:08` | `cowrie.log.closed` |
| `2026-06-24 02:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9896a7cf94e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 02:58 |
| **Last Seen** | 2026-06-24 02:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:58:31` | `cowrie.session.connect` |
| `2026-06-24 02:58:31` | `cowrie.client.version` |
| `2026-06-24 02:58:31` | `cowrie.client.kex` |
| `2026-06-24 02:58:35` | `cowrie.login.success` |
| `2026-06-24 02:58:37` | `cowrie.session.params` |
| `2026-06-24 02:58:37` | `cowrie.command.input` |
| `2026-06-24 02:58:37` | `cowrie.command.input` |
| `2026-06-24 02:58:37` | `cowrie.command.input` |
| `2026-06-24 02:58:37` | `cowrie.command.input` |
| `2026-06-24 02:58:38` | `cowrie.log.closed` |
| `2026-06-24 02:58:40` | `cowrie.session.params` |
| `2026-06-24 02:58:40` | `cowrie.command.input` |
| `2026-06-24 02:58:40` | `cowrie.command.input` |
| `2026-06-24 02:58:40` | `cowrie.command.failed` |
| `2026-06-24 02:58:40` | `cowrie.command.failed` |
| `2026-06-24 02:58:40` | `cowrie.command.failed` |
| `2026-06-24 02:58:40` | `cowrie.command.failed` |
| `2026-06-24 02:58:41` | `cowrie.log.closed` |
| `2026-06-24 02:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c5653b38c7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 02:59 |
| **Last Seen** | 2026-06-24 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:59:00` | `cowrie.session.connect` |
| `2026-06-24 02:59:00` | `cowrie.client.version` |
| `2026-06-24 02:59:01` | `cowrie.client.kex` |
| `2026-06-24 02:59:01` | `cowrie.login.success` |
| `2026-06-24 02:59:02` | `cowrie.session.params` |
| `2026-06-24 02:59:02` | `cowrie.command.input` |
| `2026-06-24 02:59:02` | `cowrie.log.closed` |
| `2026-06-24 02:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90ec8baa360

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 02:59 |
| **Last Seen** | 2026-06-24 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 02:59:52` | `cowrie.session.connect` |
| `2026-06-24 02:59:52` | `cowrie.client.version` |
| `2026-06-24 02:59:52` | `cowrie.client.kex` |
| `2026-06-24 02:59:52` | `cowrie.login.success` |
| `2026-06-24 02:59:53` | `cowrie.session.params` |
| `2026-06-24 02:59:53` | `cowrie.command.input` |
| `2026-06-24 02:59:53` | `cowrie.log.closed` |
| `2026-06-24 02:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-856fda73bf43

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 03:00 |
| **Last Seen** | 2026-06-24 03:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:00:05` | `cowrie.session.connect` |
| `2026-06-24 03:00:06` | `cowrie.client.version` |
| `2026-06-24 03:00:06` | `cowrie.client.kex` |
| `2026-06-24 03:00:13` | `cowrie.login.success` |
| `2026-06-24 03:00:16` | `cowrie.session.params` |
| `2026-06-24 03:00:16` | `cowrie.command.input` |
| `2026-06-24 03:00:18` | `cowrie.log.closed` |
| `2026-06-24 03:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c6092a0220

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:00 |
| **Last Seen** | 2026-06-24 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:00:44` | `cowrie.session.connect` |
| `2026-06-24 03:00:44` | `cowrie.client.version` |
| `2026-06-24 03:00:44` | `cowrie.client.kex` |
| `2026-06-24 03:00:44` | `cowrie.login.success` |
| `2026-06-24 03:00:45` | `cowrie.session.params` |
| `2026-06-24 03:00:45` | `cowrie.command.input` |
| `2026-06-24 03:00:45` | `cowrie.log.closed` |
| `2026-06-24 03:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae8b9e5029b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:01 |
| **Last Seen** | 2026-06-24 03:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:01:39` | `cowrie.session.connect` |
| `2026-06-24 03:01:39` | `cowrie.client.version` |
| `2026-06-24 03:01:39` | `cowrie.client.kex` |
| `2026-06-24 03:01:39` | `cowrie.login.success` |
| `2026-06-24 03:01:40` | `cowrie.session.params` |
| `2026-06-24 03:01:40` | `cowrie.command.input` |
| `2026-06-24 03:01:40` | `cowrie.log.closed` |
| `2026-06-24 03:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a3405155b1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:01 |
| **Last Seen** | 2026-06-24 03:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin2026' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:01:45` | `cowrie.session.connect` |
| `2026-06-24 03:01:46` | `cowrie.client.version` |
| `2026-06-24 03:01:46` | `cowrie.client.kex` |
| `2026-06-24 03:01:50` | `cowrie.login.success` |
| `2026-06-24 03:01:52` | `cowrie.session.params` |
| `2026-06-24 03:01:52` | `cowrie.command.input` |
| `2026-06-24 03:01:52` | `cowrie.command.input` |
| `2026-06-24 03:01:52` | `cowrie.command.input` |
| `2026-06-24 03:01:52` | `cowrie.command.input` |
| `2026-06-24 03:01:54` | `cowrie.log.closed` |
| `2026-06-24 03:01:56` | `cowrie.session.params` |
| `2026-06-24 03:01:56` | `cowrie.command.input` |
| `2026-06-24 03:01:56` | `cowrie.command.input` |
| `2026-06-24 03:01:56` | `cowrie.command.failed` |
| `2026-06-24 03:01:56` | `cowrie.command.failed` |
| `2026-06-24 03:01:56` | `cowrie.command.failed` |
| `2026-06-24 03:01:56` | `cowrie.command.failed` |
| `2026-06-24 03:01:57` | `cowrie.log.closed` |
| `2026-06-24 03:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8081680d7d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:02 |
| **Last Seen** | 2026-06-24 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:02:32` | `cowrie.session.connect` |
| `2026-06-24 03:02:32` | `cowrie.client.version` |
| `2026-06-24 03:02:32` | `cowrie.client.kex` |
| `2026-06-24 03:02:32` | `cowrie.login.success` |
| `2026-06-24 03:02:33` | `cowrie.session.params` |
| `2026-06-24 03:02:33` | `cowrie.command.input` |
| `2026-06-24 03:02:33` | `cowrie.log.closed` |
| `2026-06-24 03:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb1559c039b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:03 |
| **Last Seen** | 2026-06-24 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:03:23` | `cowrie.session.connect` |
| `2026-06-24 03:03:23` | `cowrie.client.version` |
| `2026-06-24 03:03:23` | `cowrie.client.kex` |
| `2026-06-24 03:03:23` | `cowrie.login.success` |
| `2026-06-24 03:03:24` | `cowrie.session.params` |
| `2026-06-24 03:03:24` | `cowrie.command.input` |
| `2026-06-24 03:03:24` | `cowrie.log.closed` |
| `2026-06-24 03:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa921408c80

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:04 |
| **Last Seen** | 2026-06-24 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:04:18` | `cowrie.session.connect` |
| `2026-06-24 03:04:18` | `cowrie.client.version` |
| `2026-06-24 03:04:18` | `cowrie.client.kex` |
| `2026-06-24 03:04:18` | `cowrie.login.success` |
| `2026-06-24 03:04:19` | `cowrie.session.params` |
| `2026-06-24 03:04:19` | `cowrie.command.input` |
| `2026-06-24 03:04:19` | `cowrie.log.closed` |
| `2026-06-24 03:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30407ff32d07

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 03:05 |
| **Last Seen** | 2026-06-24 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:05:05` | `cowrie.session.connect` |
| `2026-06-24 03:05:05` | `cowrie.client.version` |
| `2026-06-24 03:05:05` | `cowrie.client.kex` |
| `2026-06-24 03:05:05` | `cowrie.login.success` |
| `2026-06-24 03:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa08da4e183

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 03:05 |
| **Last Seen** | 2026-06-24 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:05:05` | `cowrie.session.connect` |
| `2026-06-24 03:05:05` | `cowrie.client.version` |
| `2026-06-24 03:05:05` | `cowrie.client.kex` |
| `2026-06-24 03:05:05` | `cowrie.login.success` |
| `2026-06-24 03:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77feea22d2a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:05 |
| **Last Seen** | 2026-06-24 03:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:05:10` | `cowrie.session.connect` |
| `2026-06-24 03:05:10` | `cowrie.client.version` |
| `2026-06-24 03:05:10` | `cowrie.client.kex` |
| `2026-06-24 03:05:10` | `cowrie.login.success` |
| `2026-06-24 03:05:11` | `cowrie.session.params` |
| `2026-06-24 03:05:11` | `cowrie.command.input` |
| `2026-06-24 03:05:11` | `cowrie.log.closed` |
| `2026-06-24 03:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b6a382c4e13

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 03:05 |
| **Last Seen** | 2026-06-24 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:05:11` | `cowrie.session.connect` |
| `2026-06-24 03:05:11` | `cowrie.client.version` |
| `2026-06-24 03:05:11` | `cowrie.client.kex` |
| `2026-06-24 03:05:11` | `cowrie.login.success` |
| `2026-06-24 03:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffb47068797a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 03:05 |
| **Last Seen** | 2026-06-24 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:05:11` | `cowrie.session.connect` |
| `2026-06-24 03:05:11` | `cowrie.client.version` |
| `2026-06-24 03:05:11` | `cowrie.client.kex` |
| `2026-06-24 03:05:11` | `cowrie.login.success` |
| `2026-06-24 03:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7524b3da05a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:05 |
| **Last Seen** | 2026-06-24 03:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'letmein' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:05:15` | `cowrie.session.connect` |
| `2026-06-24 03:05:16` | `cowrie.client.version` |
| `2026-06-24 03:05:16` | `cowrie.client.kex` |
| `2026-06-24 03:05:20` | `cowrie.login.success` |
| `2026-06-24 03:05:23` | `cowrie.session.params` |
| `2026-06-24 03:05:23` | `cowrie.command.input` |
| `2026-06-24 03:05:23` | `cowrie.command.input` |
| `2026-06-24 03:05:23` | `cowrie.command.input` |
| `2026-06-24 03:05:23` | `cowrie.command.input` |
| `2026-06-24 03:05:24` | `cowrie.log.closed` |
| `2026-06-24 03:05:27` | `cowrie.session.params` |
| `2026-06-24 03:05:27` | `cowrie.command.input` |
| `2026-06-24 03:05:27` | `cowrie.command.input` |
| `2026-06-24 03:05:27` | `cowrie.command.failed` |
| `2026-06-24 03:05:27` | `cowrie.command.failed` |
| `2026-06-24 03:05:27` | `cowrie.command.failed` |
| `2026-06-24 03:05:27` | `cowrie.command.failed` |
| `2026-06-24 03:05:28` | `cowrie.log.closed` |
| `2026-06-24 03:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e377fe13a9f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:06 |
| **Last Seen** | 2026-06-24 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:06:02` | `cowrie.session.connect` |
| `2026-06-24 03:06:02` | `cowrie.client.version` |
| `2026-06-24 03:06:02` | `cowrie.client.kex` |
| `2026-06-24 03:06:02` | `cowrie.login.success` |
| `2026-06-24 03:06:03` | `cowrie.session.params` |
| `2026-06-24 03:06:03` | `cowrie.command.input` |
| `2026-06-24 03:06:03` | `cowrie.log.closed` |
| `2026-06-24 03:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897109a133bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:06 |
| **Last Seen** | 2026-06-24 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:06:58` | `cowrie.session.connect` |
| `2026-06-24 03:06:58` | `cowrie.client.version` |
| `2026-06-24 03:06:58` | `cowrie.client.kex` |
| `2026-06-24 03:06:58` | `cowrie.login.success` |
| `2026-06-24 03:06:59` | `cowrie.session.params` |
| `2026-06-24 03:06:59` | `cowrie.command.input` |
| `2026-06-24 03:06:59` | `cowrie.log.closed` |
| `2026-06-24 03:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2588bc24343d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:07 |
| **Last Seen** | 2026-06-24 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:07:52` | `cowrie.session.connect` |
| `2026-06-24 03:07:52` | `cowrie.client.version` |
| `2026-06-24 03:07:52` | `cowrie.client.kex` |
| `2026-06-24 03:07:52` | `cowrie.login.success` |
| `2026-06-24 03:07:53` | `cowrie.session.params` |
| `2026-06-24 03:07:53` | `cowrie.command.input` |
| `2026-06-24 03:07:53` | `cowrie.log.closed` |
| `2026-06-24 03:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-472181e11c68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:08 |
| **Last Seen** | 2026-06-24 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:08:44` | `cowrie.session.connect` |
| `2026-06-24 03:08:44` | `cowrie.client.version` |
| `2026-06-24 03:08:44` | `cowrie.client.kex` |
| `2026-06-24 03:08:44` | `cowrie.login.success` |
| `2026-06-24 03:08:45` | `cowrie.session.params` |
| `2026-06-24 03:08:45` | `cowrie.command.input` |
| `2026-06-24 03:08:45` | `cowrie.log.closed` |
| `2026-06-24 03:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b97f9eba56a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:08 |
| **Last Seen** | 2026-06-24 03:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'pa$w0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:08:58` | `cowrie.session.connect` |
| `2026-06-24 03:08:59` | `cowrie.client.version` |
| `2026-06-24 03:08:59` | `cowrie.client.kex` |
| `2026-06-24 03:09:04` | `cowrie.login.success` |
| `2026-06-24 03:09:06` | `cowrie.session.params` |
| `2026-06-24 03:09:06` | `cowrie.command.input` |
| `2026-06-24 03:09:06` | `cowrie.command.input` |
| `2026-06-24 03:09:06` | `cowrie.command.input` |
| `2026-06-24 03:09:06` | `cowrie.command.input` |
| `2026-06-24 03:09:08` | `cowrie.log.closed` |
| `2026-06-24 03:09:11` | `cowrie.session.params` |
| `2026-06-24 03:09:11` | `cowrie.command.input` |
| `2026-06-24 03:09:11` | `cowrie.command.input` |
| `2026-06-24 03:09:11` | `cowrie.command.failed` |
| `2026-06-24 03:09:11` | `cowrie.command.failed` |
| `2026-06-24 03:09:11` | `cowrie.command.failed` |
| `2026-06-24 03:09:11` | `cowrie.command.failed` |
| `2026-06-24 03:09:12` | `cowrie.log.closed` |
| `2026-06-24 03:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc47670fd15

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:09 |
| **Last Seen** | 2026-06-24 03:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:09:34` | `cowrie.session.connect` |
| `2026-06-24 03:09:34` | `cowrie.client.version` |
| `2026-06-24 03:09:35` | `cowrie.client.kex` |
| `2026-06-24 03:09:35` | `cowrie.login.success` |
| `2026-06-24 03:09:36` | `cowrie.session.params` |
| `2026-06-24 03:09:36` | `cowrie.command.input` |
| `2026-06-24 03:09:36` | `cowrie.log.closed` |
| `2026-06-24 03:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2457d24712

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:10 |
| **Last Seen** | 2026-06-24 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:10:24` | `cowrie.session.connect` |
| `2026-06-24 03:10:24` | `cowrie.client.version` |
| `2026-06-24 03:10:24` | `cowrie.client.kex` |
| `2026-06-24 03:10:25` | `cowrie.login.success` |
| `2026-06-24 03:10:25` | `cowrie.session.params` |
| `2026-06-24 03:10:25` | `cowrie.command.input` |
| `2026-06-24 03:10:26` | `cowrie.log.closed` |
| `2026-06-24 03:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca8b1d5b7d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:11 |
| **Last Seen** | 2026-06-24 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:11:16` | `cowrie.session.connect` |
| `2026-06-24 03:11:16` | `cowrie.client.version` |
| `2026-06-24 03:11:16` | `cowrie.client.kex` |
| `2026-06-24 03:11:16` | `cowrie.login.success` |
| `2026-06-24 03:11:17` | `cowrie.session.params` |
| `2026-06-24 03:11:17` | `cowrie.command.input` |
| `2026-06-24 03:11:17` | `cowrie.log.closed` |
| `2026-06-24 03:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-080d1bd4958b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:12 |
| **Last Seen** | 2026-06-24 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:12:09` | `cowrie.session.connect` |
| `2026-06-24 03:12:09` | `cowrie.client.version` |
| `2026-06-24 03:12:09` | `cowrie.client.kex` |
| `2026-06-24 03:12:10` | `cowrie.login.success` |
| `2026-06-24 03:12:10` | `cowrie.session.params` |
| `2026-06-24 03:12:10` | `cowrie.command.input` |
| `2026-06-24 03:12:11` | `cowrie.log.closed` |
| `2026-06-24 03:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea04566bd9d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:12 |
| **Last Seen** | 2026-06-24 03:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'passw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:12:36` | `cowrie.session.connect` |
| `2026-06-24 03:12:37` | `cowrie.client.version` |
| `2026-06-24 03:12:37` | `cowrie.client.kex` |
| `2026-06-24 03:12:42` | `cowrie.login.success` |
| `2026-06-24 03:12:44` | `cowrie.session.params` |
| `2026-06-24 03:12:44` | `cowrie.command.input` |
| `2026-06-24 03:12:44` | `cowrie.command.input` |
| `2026-06-24 03:12:44` | `cowrie.command.input` |
| `2026-06-24 03:12:44` | `cowrie.command.input` |
| `2026-06-24 03:12:46` | `cowrie.log.closed` |
| `2026-06-24 03:12:49` | `cowrie.session.params` |
| `2026-06-24 03:12:49` | `cowrie.command.input` |
| `2026-06-24 03:12:49` | `cowrie.command.input` |
| `2026-06-24 03:12:49` | `cowrie.command.failed` |
| `2026-06-24 03:12:49` | `cowrie.command.failed` |
| `2026-06-24 03:12:49` | `cowrie.command.failed` |
| `2026-06-24 03:12:49` | `cowrie.command.failed` |
| `2026-06-24 03:12:50` | `cowrie.log.closed` |
| `2026-06-24 03:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1608ea1ef67

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:13 |
| **Last Seen** | 2026-06-24 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:13:02` | `cowrie.session.connect` |
| `2026-06-24 03:13:02` | `cowrie.client.version` |
| `2026-06-24 03:13:02` | `cowrie.client.kex` |
| `2026-06-24 03:13:02` | `cowrie.login.success` |
| `2026-06-24 03:13:03` | `cowrie.session.params` |
| `2026-06-24 03:13:03` | `cowrie.command.input` |
| `2026-06-24 03:13:03` | `cowrie.log.closed` |
| `2026-06-24 03:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e18f25d2ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:13 |
| **Last Seen** | 2026-06-24 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:13:57` | `cowrie.session.connect` |
| `2026-06-24 03:13:57` | `cowrie.client.version` |
| `2026-06-24 03:13:57` | `cowrie.client.kex` |
| `2026-06-24 03:13:57` | `cowrie.login.success` |
| `2026-06-24 03:13:58` | `cowrie.session.params` |
| `2026-06-24 03:13:58` | `cowrie.command.input` |
| `2026-06-24 03:13:58` | `cowrie.log.closed` |
| `2026-06-24 03:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7abb3db96540

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 03:14 |
| **Last Seen** | 2026-06-24 03:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:14:40` | `cowrie.session.connect` |
| `2026-06-24 03:14:42` | `cowrie.client.version` |
| `2026-06-24 03:14:42` | `cowrie.client.kex` |
| `2026-06-24 03:14:48` | `cowrie.login.success` |
| `2026-06-24 03:14:52` | `cowrie.session.params` |
| `2026-06-24 03:14:52` | `cowrie.command.input` |
| `2026-06-24 03:14:53` | `cowrie.log.closed` |
| `2026-06-24 03:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb625f0b1ec8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:14 |
| **Last Seen** | 2026-06-24 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:14:52` | `cowrie.session.connect` |
| `2026-06-24 03:14:52` | `cowrie.client.version` |
| `2026-06-24 03:14:52` | `cowrie.client.kex` |
| `2026-06-24 03:14:52` | `cowrie.login.success` |
| `2026-06-24 03:14:53` | `cowrie.session.params` |
| `2026-06-24 03:14:53` | `cowrie.command.input` |
| `2026-06-24 03:14:53` | `cowrie.log.closed` |
| `2026-06-24 03:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78118f46625d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:15 |
| **Last Seen** | 2026-06-24 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:15:45` | `cowrie.session.connect` |
| `2026-06-24 03:15:45` | `cowrie.client.version` |
| `2026-06-24 03:15:45` | `cowrie.client.kex` |
| `2026-06-24 03:15:45` | `cowrie.login.success` |
| `2026-06-24 03:15:46` | `cowrie.session.params` |
| `2026-06-24 03:15:46` | `cowrie.command.input` |
| `2026-06-24 03:15:46` | `cowrie.log.closed` |
| `2026-06-24 03:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb7e1a10755

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:16 |
| **Last Seen** | 2026-06-24 03:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:16:20` | `cowrie.session.connect` |
| `2026-06-24 03:16:21` | `cowrie.client.version` |
| `2026-06-24 03:16:21` | `cowrie.client.kex` |
| `2026-06-24 03:16:25` | `cowrie.login.success` |
| `2026-06-24 03:16:27` | `cowrie.session.params` |
| `2026-06-24 03:16:27` | `cowrie.command.input` |
| `2026-06-24 03:16:27` | `cowrie.command.input` |
| `2026-06-24 03:16:27` | `cowrie.command.input` |
| `2026-06-24 03:16:27` | `cowrie.command.input` |
| `2026-06-24 03:16:30` | `cowrie.log.closed` |
| `2026-06-24 03:16:32` | `cowrie.session.params` |
| `2026-06-24 03:16:32` | `cowrie.command.input` |
| `2026-06-24 03:16:32` | `cowrie.command.input` |
| `2026-06-24 03:16:32` | `cowrie.command.failed` |
| `2026-06-24 03:16:32` | `cowrie.command.failed` |
| `2026-06-24 03:16:32` | `cowrie.command.failed` |
| `2026-06-24 03:16:32` | `cowrie.command.failed` |
| `2026-06-24 03:16:33` | `cowrie.log.closed` |
| `2026-06-24 03:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ebe3f4c665

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:16 |
| **Last Seen** | 2026-06-24 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:16:39` | `cowrie.session.connect` |
| `2026-06-24 03:16:39` | `cowrie.client.version` |
| `2026-06-24 03:16:39` | `cowrie.client.kex` |
| `2026-06-24 03:16:39` | `cowrie.login.success` |
| `2026-06-24 03:16:40` | `cowrie.session.params` |
| `2026-06-24 03:16:40` | `cowrie.command.input` |
| `2026-06-24 03:16:40` | `cowrie.log.closed` |
| `2026-06-24 03:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9c664413cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:17 |
| **Last Seen** | 2026-06-24 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:17:35` | `cowrie.session.connect` |
| `2026-06-24 03:17:35` | `cowrie.client.version` |
| `2026-06-24 03:17:35` | `cowrie.client.kex` |
| `2026-06-24 03:17:36` | `cowrie.login.success` |
| `2026-06-24 03:17:36` | `cowrie.session.params` |
| `2026-06-24 03:17:36` | `cowrie.command.input` |
| `2026-06-24 03:17:36` | `cowrie.log.closed` |
| `2026-06-24 03:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641040df152b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:18 |
| **Last Seen** | 2026-06-24 03:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:18:29` | `cowrie.session.connect` |
| `2026-06-24 03:18:29` | `cowrie.client.version` |
| `2026-06-24 03:18:29` | `cowrie.client.kex` |
| `2026-06-24 03:18:29` | `cowrie.login.success` |
| `2026-06-24 03:18:30` | `cowrie.session.params` |
| `2026-06-24 03:18:30` | `cowrie.command.input` |
| `2026-06-24 03:18:30` | `cowrie.log.closed` |
| `2026-06-24 03:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68fbd0fd8e59

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:19 |
| **Last Seen** | 2026-06-24 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:19:24` | `cowrie.session.connect` |
| `2026-06-24 03:19:24` | `cowrie.client.version` |
| `2026-06-24 03:19:24` | `cowrie.client.kex` |
| `2026-06-24 03:19:24` | `cowrie.login.success` |
| `2026-06-24 03:19:25` | `cowrie.session.params` |
| `2026-06-24 03:19:25` | `cowrie.command.input` |
| `2026-06-24 03:19:25` | `cowrie.log.closed` |
| `2026-06-24 03:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74aee60accf1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:19 |
| **Last Seen** | 2026-06-24 03:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:19:51` | `cowrie.session.connect` |
| `2026-06-24 03:19:51` | `cowrie.client.version` |
| `2026-06-24 03:19:51` | `cowrie.client.kex` |
| `2026-06-24 03:19:56` | `cowrie.login.success` |
| `2026-06-24 03:19:58` | `cowrie.session.params` |
| `2026-06-24 03:19:58` | `cowrie.command.input` |
| `2026-06-24 03:19:58` | `cowrie.command.input` |
| `2026-06-24 03:19:58` | `cowrie.command.input` |
| `2026-06-24 03:19:58` | `cowrie.command.input` |
| `2026-06-24 03:19:59` | `cowrie.log.closed` |
| `2026-06-24 03:20:02` | `cowrie.session.params` |
| `2026-06-24 03:20:02` | `cowrie.command.input` |
| `2026-06-24 03:20:02` | `cowrie.command.input` |
| `2026-06-24 03:20:02` | `cowrie.command.failed` |
| `2026-06-24 03:20:02` | `cowrie.command.failed` |
| `2026-06-24 03:20:02` | `cowrie.command.failed` |
| `2026-06-24 03:20:02` | `cowrie.command.failed` |
| `2026-06-24 03:20:02` | `cowrie.log.closed` |
| `2026-06-24 03:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2d4f75daef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:20 |
| **Last Seen** | 2026-06-24 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:20:19` | `cowrie.session.connect` |
| `2026-06-24 03:20:19` | `cowrie.client.version` |
| `2026-06-24 03:20:19` | `cowrie.client.kex` |
| `2026-06-24 03:20:20` | `cowrie.login.success` |
| `2026-06-24 03:20:21` | `cowrie.session.params` |
| `2026-06-24 03:20:21` | `cowrie.command.input` |
| `2026-06-24 03:20:21` | `cowrie.log.closed` |
| `2026-06-24 03:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee15a380035

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:21 |
| **Last Seen** | 2026-06-24 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:21:14` | `cowrie.session.connect` |
| `2026-06-24 03:21:14` | `cowrie.client.version` |
| `2026-06-24 03:21:14` | `cowrie.client.kex` |
| `2026-06-24 03:21:15` | `cowrie.login.success` |
| `2026-06-24 03:21:15` | `cowrie.session.params` |
| `2026-06-24 03:21:15` | `cowrie.command.input` |
| `2026-06-24 03:21:15` | `cowrie.log.closed` |
| `2026-06-24 03:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5371d4b7ea7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:22 |
| **Last Seen** | 2026-06-24 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:22:09` | `cowrie.session.connect` |
| `2026-06-24 03:22:09` | `cowrie.client.version` |
| `2026-06-24 03:22:09` | `cowrie.client.kex` |
| `2026-06-24 03:22:10` | `cowrie.login.success` |
| `2026-06-24 03:22:11` | `cowrie.session.params` |
| `2026-06-24 03:22:11` | `cowrie.command.input` |
| `2026-06-24 03:22:11` | `cowrie.log.closed` |
| `2026-06-24 03:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a01d503a51d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:23 |
| **Last Seen** | 2026-06-24 03:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:23:03` | `cowrie.session.connect` |
| `2026-06-24 03:23:03` | `cowrie.client.version` |
| `2026-06-24 03:23:03` | `cowrie.client.kex` |
| `2026-06-24 03:23:03` | `cowrie.login.success` |
| `2026-06-24 03:23:04` | `cowrie.session.params` |
| `2026-06-24 03:23:04` | `cowrie.command.input` |
| `2026-06-24 03:23:04` | `cowrie.log.closed` |
| `2026-06-24 03:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d0aa1d0f532

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:23 |
| **Last Seen** | 2026-06-24 03:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:23:33` | `cowrie.session.connect` |
| `2026-06-24 03:23:33` | `cowrie.client.version` |
| `2026-06-24 03:23:33` | `cowrie.client.kex` |
| `2026-06-24 03:23:38` | `cowrie.login.success` |
| `2026-06-24 03:23:40` | `cowrie.session.params` |
| `2026-06-24 03:23:40` | `cowrie.command.input` |
| `2026-06-24 03:23:40` | `cowrie.command.input` |
| `2026-06-24 03:23:40` | `cowrie.command.input` |
| `2026-06-24 03:23:40` | `cowrie.command.input` |
| `2026-06-24 03:23:41` | `cowrie.log.closed` |
| `2026-06-24 03:23:44` | `cowrie.session.params` |
| `2026-06-24 03:23:44` | `cowrie.command.input` |
| `2026-06-24 03:23:44` | `cowrie.command.input` |
| `2026-06-24 03:23:44` | `cowrie.command.failed` |
| `2026-06-24 03:23:44` | `cowrie.command.failed` |
| `2026-06-24 03:23:44` | `cowrie.command.failed` |
| `2026-06-24 03:23:44` | `cowrie.command.failed` |
| `2026-06-24 03:23:45` | `cowrie.log.closed` |
| `2026-06-24 03:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d90cdd61acae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:23 |
| **Last Seen** | 2026-06-24 03:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:23:56` | `cowrie.session.connect` |
| `2026-06-24 03:23:56` | `cowrie.client.version` |
| `2026-06-24 03:23:57` | `cowrie.client.kex` |
| `2026-06-24 03:23:57` | `cowrie.login.success` |
| `2026-06-24 03:23:58` | `cowrie.session.params` |
| `2026-06-24 03:23:58` | `cowrie.command.input` |
| `2026-06-24 03:23:58` | `cowrie.log.closed` |
| `2026-06-24 03:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957ac7fa5fe7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:24 |
| **Last Seen** | 2026-06-24 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:24:52` | `cowrie.session.connect` |
| `2026-06-24 03:24:52` | `cowrie.client.version` |
| `2026-06-24 03:24:52` | `cowrie.client.kex` |
| `2026-06-24 03:24:52` | `cowrie.login.success` |
| `2026-06-24 03:24:53` | `cowrie.session.params` |
| `2026-06-24 03:24:53` | `cowrie.command.input` |
| `2026-06-24 03:24:53` | `cowrie.log.closed` |
| `2026-06-24 03:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e24b249de3a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:25 |
| **Last Seen** | 2026-06-24 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:25:48` | `cowrie.session.connect` |
| `2026-06-24 03:25:48` | `cowrie.client.version` |
| `2026-06-24 03:25:48` | `cowrie.client.kex` |
| `2026-06-24 03:25:48` | `cowrie.login.success` |
| `2026-06-24 03:25:49` | `cowrie.session.params` |
| `2026-06-24 03:25:49` | `cowrie.command.input` |
| `2026-06-24 03:25:49` | `cowrie.log.closed` |
| `2026-06-24 03:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d13d2129a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:26 |
| **Last Seen** | 2026-06-24 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:26:45` | `cowrie.session.connect` |
| `2026-06-24 03:26:45` | `cowrie.client.version` |
| `2026-06-24 03:26:45` | `cowrie.client.kex` |
| `2026-06-24 03:26:45` | `cowrie.login.success` |
| `2026-06-24 03:26:46` | `cowrie.session.params` |
| `2026-06-24 03:26:46` | `cowrie.command.input` |
| `2026-06-24 03:26:46` | `cowrie.log.closed` |
| `2026-06-24 03:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb64f22c08d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:27 |
| **Last Seen** | 2026-06-24 03:27 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'P@ssw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:27:07` | `cowrie.session.connect` |
| `2026-06-24 03:27:08` | `cowrie.client.version` |
| `2026-06-24 03:27:08` | `cowrie.client.kex` |
| `2026-06-24 03:27:12` | `cowrie.login.success` |
| `2026-06-24 03:27:15` | `cowrie.session.params` |
| `2026-06-24 03:27:15` | `cowrie.command.input` |
| `2026-06-24 03:27:15` | `cowrie.command.input` |
| `2026-06-24 03:27:15` | `cowrie.command.input` |
| `2026-06-24 03:27:15` | `cowrie.command.input` |
| `2026-06-24 03:27:16` | `cowrie.log.closed` |
| `2026-06-24 03:27:18` | `cowrie.session.params` |
| `2026-06-24 03:27:18` | `cowrie.command.input` |
| `2026-06-24 03:27:18` | `cowrie.command.input` |
| `2026-06-24 03:27:18` | `cowrie.command.failed` |
| `2026-06-24 03:27:18` | `cowrie.command.failed` |
| `2026-06-24 03:27:18` | `cowrie.command.failed` |
| `2026-06-24 03:27:18` | `cowrie.command.failed` |
| `2026-06-24 03:27:20` | `cowrie.log.closed` |
| `2026-06-24 03:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e5b4b900403

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:27 |
| **Last Seen** | 2026-06-24 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:27:42` | `cowrie.session.connect` |
| `2026-06-24 03:27:42` | `cowrie.client.version` |
| `2026-06-24 03:27:42` | `cowrie.client.kex` |
| `2026-06-24 03:27:42` | `cowrie.login.success` |
| `2026-06-24 03:27:43` | `cowrie.session.params` |
| `2026-06-24 03:27:43` | `cowrie.command.input` |
| `2026-06-24 03:27:43` | `cowrie.log.closed` |
| `2026-06-24 03:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1eb569a167c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:28 |
| **Last Seen** | 2026-06-24 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:28:38` | `cowrie.session.connect` |
| `2026-06-24 03:28:38` | `cowrie.client.version` |
| `2026-06-24 03:28:38` | `cowrie.client.kex` |
| `2026-06-24 03:28:38` | `cowrie.login.success` |
| `2026-06-24 03:28:39` | `cowrie.session.params` |
| `2026-06-24 03:28:39` | `cowrie.command.input` |
| `2026-06-24 03:28:39` | `cowrie.log.closed` |
| `2026-06-24 03:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b32ae97f21

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 03:29 |
| **Last Seen** | 2026-06-24 03:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:29:19` | `cowrie.session.connect` |
| `2026-06-24 03:29:20` | `cowrie.client.version` |
| `2026-06-24 03:29:20` | `cowrie.client.kex` |
| `2026-06-24 03:29:27` | `cowrie.login.success` |
| `2026-06-24 03:29:31` | `cowrie.session.params` |
| `2026-06-24 03:29:31` | `cowrie.command.input` |
| `2026-06-24 03:29:33` | `cowrie.log.closed` |
| `2026-06-24 03:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf499e85d1b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:29 |
| **Last Seen** | 2026-06-24 03:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:29:33` | `cowrie.session.connect` |
| `2026-06-24 03:29:33` | `cowrie.client.version` |
| `2026-06-24 03:29:33` | `cowrie.client.kex` |
| `2026-06-24 03:29:33` | `cowrie.login.success` |
| `2026-06-24 03:29:34` | `cowrie.session.params` |
| `2026-06-24 03:29:34` | `cowrie.command.input` |
| `2026-06-24 03:29:34` | `cowrie.log.closed` |
| `2026-06-24 03:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7923a81b00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:30 |
| **Last Seen** | 2026-06-24 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:30:27` | `cowrie.session.connect` |
| `2026-06-24 03:30:27` | `cowrie.client.version` |
| `2026-06-24 03:30:27` | `cowrie.client.kex` |
| `2026-06-24 03:30:28` | `cowrie.login.success` |
| `2026-06-24 03:30:29` | `cowrie.session.params` |
| `2026-06-24 03:30:29` | `cowrie.command.input` |
| `2026-06-24 03:30:29` | `cowrie.log.closed` |
| `2026-06-24 03:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75a87c1d6fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:30 |
| **Last Seen** | 2026-06-24 03:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'administrator' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:30:44` | `cowrie.session.connect` |
| `2026-06-24 03:30:45` | `cowrie.client.version` |
| `2026-06-24 03:30:45` | `cowrie.client.kex` |
| `2026-06-24 03:30:50` | `cowrie.login.success` |
| `2026-06-24 03:30:53` | `cowrie.session.params` |
| `2026-06-24 03:30:53` | `cowrie.command.input` |
| `2026-06-24 03:30:53` | `cowrie.command.input` |
| `2026-06-24 03:30:53` | `cowrie.command.input` |
| `2026-06-24 03:30:53` | `cowrie.command.input` |
| `2026-06-24 03:30:54` | `cowrie.log.closed` |
| `2026-06-24 03:30:57` | `cowrie.session.params` |
| `2026-06-24 03:30:57` | `cowrie.command.input` |
| `2026-06-24 03:30:57` | `cowrie.command.input` |
| `2026-06-24 03:30:57` | `cowrie.command.failed` |
| `2026-06-24 03:30:57` | `cowrie.command.failed` |
| `2026-06-24 03:30:57` | `cowrie.command.failed` |
| `2026-06-24 03:30:57` | `cowrie.command.failed` |
| `2026-06-24 03:30:58` | `cowrie.log.closed` |
| `2026-06-24 03:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d19c9914fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:31 |
| **Last Seen** | 2026-06-24 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:31:23` | `cowrie.session.connect` |
| `2026-06-24 03:31:23` | `cowrie.client.version` |
| `2026-06-24 03:31:23` | `cowrie.client.kex` |
| `2026-06-24 03:31:23` | `cowrie.login.success` |
| `2026-06-24 03:31:24` | `cowrie.session.params` |
| `2026-06-24 03:31:24` | `cowrie.command.input` |
| `2026-06-24 03:31:24` | `cowrie.log.closed` |
| `2026-06-24 03:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abc011f4689

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:32 |
| **Last Seen** | 2026-06-24 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:32:19` | `cowrie.session.connect` |
| `2026-06-24 03:32:19` | `cowrie.client.version` |
| `2026-06-24 03:32:19` | `cowrie.client.kex` |
| `2026-06-24 03:32:20` | `cowrie.login.success` |
| `2026-06-24 03:32:20` | `cowrie.session.params` |
| `2026-06-24 03:32:20` | `cowrie.command.input` |
| `2026-06-24 03:32:20` | `cowrie.log.closed` |
| `2026-06-24 03:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99fb37dedfa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:33 |
| **Last Seen** | 2026-06-24 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:33:16` | `cowrie.session.connect` |
| `2026-06-24 03:33:16` | `cowrie.client.version` |
| `2026-06-24 03:33:16` | `cowrie.client.kex` |
| `2026-06-24 03:33:16` | `cowrie.login.success` |
| `2026-06-24 03:33:17` | `cowrie.session.params` |
| `2026-06-24 03:33:17` | `cowrie.command.input` |
| `2026-06-24 03:33:17` | `cowrie.log.closed` |
| `2026-06-24 03:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214ffbfec01a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:34 |
| **Last Seen** | 2026-06-24 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:34:11` | `cowrie.session.connect` |
| `2026-06-24 03:34:11` | `cowrie.client.version` |
| `2026-06-24 03:34:11` | `cowrie.client.kex` |
| `2026-06-24 03:34:11` | `cowrie.login.success` |
| `2026-06-24 03:34:12` | `cowrie.session.params` |
| `2026-06-24 03:34:12` | `cowrie.command.input` |
| `2026-06-24 03:34:12` | `cowrie.log.closed` |
| `2026-06-24 03:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94fe655c79f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:34 |
| **Last Seen** | 2026-06-24 03:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'administrator123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:34:18` | `cowrie.session.connect` |
| `2026-06-24 03:34:19` | `cowrie.client.version` |
| `2026-06-24 03:34:19` | `cowrie.client.kex` |
| `2026-06-24 03:34:24` | `cowrie.login.success` |
| `2026-06-24 03:34:26` | `cowrie.session.params` |
| `2026-06-24 03:34:26` | `cowrie.command.input` |
| `2026-06-24 03:34:26` | `cowrie.command.input` |
| `2026-06-24 03:34:26` | `cowrie.command.input` |
| `2026-06-24 03:34:26` | `cowrie.command.input` |
| `2026-06-24 03:34:28` | `cowrie.log.closed` |
| `2026-06-24 03:34:31` | `cowrie.session.params` |
| `2026-06-24 03:34:31` | `cowrie.command.input` |
| `2026-06-24 03:34:31` | `cowrie.command.input` |
| `2026-06-24 03:34:31` | `cowrie.command.failed` |
| `2026-06-24 03:34:31` | `cowrie.command.failed` |
| `2026-06-24 03:34:31` | `cowrie.command.failed` |
| `2026-06-24 03:34:31` | `cowrie.command.failed` |
| `2026-06-24 03:34:32` | `cowrie.log.closed` |
| `2026-06-24 03:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3526d864db34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:35 |
| **Last Seen** | 2026-06-24 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:35:05` | `cowrie.session.connect` |
| `2026-06-24 03:35:05` | `cowrie.client.version` |
| `2026-06-24 03:35:05` | `cowrie.client.kex` |
| `2026-06-24 03:35:05` | `cowrie.login.success` |
| `2026-06-24 03:35:06` | `cowrie.session.params` |
| `2026-06-24 03:35:06` | `cowrie.command.input` |
| `2026-06-24 03:35:06` | `cowrie.log.closed` |
| `2026-06-24 03:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331fd88360a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:36 |
| **Last Seen** | 2026-06-24 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:36:00` | `cowrie.session.connect` |
| `2026-06-24 03:36:00` | `cowrie.client.version` |
| `2026-06-24 03:36:00` | `cowrie.client.kex` |
| `2026-06-24 03:36:00` | `cowrie.login.success` |
| `2026-06-24 03:36:01` | `cowrie.session.params` |
| `2026-06-24 03:36:01` | `cowrie.command.input` |
| `2026-06-24 03:36:01` | `cowrie.log.closed` |
| `2026-06-24 03:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90da2989f145

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:36 |
| **Last Seen** | 2026-06-24 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:36:55` | `cowrie.session.connect` |
| `2026-06-24 03:36:55` | `cowrie.client.version` |
| `2026-06-24 03:36:55` | `cowrie.client.kex` |
| `2026-06-24 03:36:55` | `cowrie.login.success` |
| `2026-06-24 03:36:56` | `cowrie.session.params` |
| `2026-06-24 03:36:56` | `cowrie.command.input` |
| `2026-06-24 03:36:56` | `cowrie.log.closed` |
| `2026-06-24 03:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39866bced35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:37 |
| **Last Seen** | 2026-06-24 03:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:37:51` | `cowrie.session.connect` |
| `2026-06-24 03:37:51` | `cowrie.client.version` |
| `2026-06-24 03:37:51` | `cowrie.client.kex` |
| `2026-06-24 03:37:52` | `cowrie.login.success` |
| `2026-06-24 03:37:52` | `cowrie.session.params` |
| `2026-06-24 03:37:52` | `cowrie.command.input` |
| `2026-06-24 03:37:53` | `cowrie.log.closed` |
| `2026-06-24 03:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e3807e3cfae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:38 |
| **Last Seen** | 2026-06-24 03:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'passw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:38:12` | `cowrie.session.connect` |
| `2026-06-24 03:38:13` | `cowrie.client.version` |
| `2026-06-24 03:38:13` | `cowrie.client.kex` |
| `2026-06-24 03:38:17` | `cowrie.login.success` |
| `2026-06-24 03:38:19` | `cowrie.session.params` |
| `2026-06-24 03:38:19` | `cowrie.command.input` |
| `2026-06-24 03:38:19` | `cowrie.command.input` |
| `2026-06-24 03:38:19` | `cowrie.command.input` |
| `2026-06-24 03:38:19` | `cowrie.command.input` |
| `2026-06-24 03:38:20` | `cowrie.log.closed` |
| `2026-06-24 03:38:23` | `cowrie.session.params` |
| `2026-06-24 03:38:23` | `cowrie.command.input` |
| `2026-06-24 03:38:23` | `cowrie.command.input` |
| `2026-06-24 03:38:23` | `cowrie.command.failed` |
| `2026-06-24 03:38:23` | `cowrie.command.failed` |
| `2026-06-24 03:38:23` | `cowrie.command.failed` |
| `2026-06-24 03:38:23` | `cowrie.command.failed` |
| `2026-06-24 03:38:24` | `cowrie.log.closed` |
| `2026-06-24 03:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9396c027c730

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:38 |
| **Last Seen** | 2026-06-24 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:38:49` | `cowrie.session.connect` |
| `2026-06-24 03:38:49` | `cowrie.client.version` |
| `2026-06-24 03:38:49` | `cowrie.client.kex` |
| `2026-06-24 03:38:49` | `cowrie.login.success` |
| `2026-06-24 03:38:50` | `cowrie.session.params` |
| `2026-06-24 03:38:50` | `cowrie.command.input` |
| `2026-06-24 03:38:50` | `cowrie.log.closed` |
| `2026-06-24 03:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505c6bbefa24

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:39 |
| **Last Seen** | 2026-06-24 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:39:47` | `cowrie.session.connect` |
| `2026-06-24 03:39:47` | `cowrie.client.version` |
| `2026-06-24 03:39:48` | `cowrie.client.kex` |
| `2026-06-24 03:39:48` | `cowrie.login.success` |
| `2026-06-24 03:39:49` | `cowrie.session.params` |
| `2026-06-24 03:39:49` | `cowrie.command.input` |
| `2026-06-24 03:39:49` | `cowrie.log.closed` |
| `2026-06-24 03:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b6166f7b43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:40 |
| **Last Seen** | 2026-06-24 03:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:40:46` | `cowrie.session.connect` |
| `2026-06-24 03:40:46` | `cowrie.client.version` |
| `2026-06-24 03:40:46` | `cowrie.client.kex` |
| `2026-06-24 03:40:47` | `cowrie.login.success` |
| `2026-06-24 03:40:47` | `cowrie.session.params` |
| `2026-06-24 03:40:47` | `cowrie.command.input` |
| `2026-06-24 03:40:47` | `cowrie.log.closed` |
| `2026-06-24 03:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8da6dc612b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:41 |
| **Last Seen** | 2026-06-24 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:41:44` | `cowrie.session.connect` |
| `2026-06-24 03:41:44` | `cowrie.client.version` |
| `2026-06-24 03:41:44` | `cowrie.client.kex` |
| `2026-06-24 03:41:45` | `cowrie.login.success` |
| `2026-06-24 03:41:45` | `cowrie.session.params` |
| `2026-06-24 03:41:45` | `cowrie.command.input` |
| `2026-06-24 03:41:45` | `cowrie.log.closed` |
| `2026-06-24 03:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ff041ad2bf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:42 |
| **Last Seen** | 2026-06-24 03:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:42:05` | `cowrie.session.connect` |
| `2026-06-24 03:42:06` | `cowrie.client.version` |
| `2026-06-24 03:42:06` | `cowrie.client.kex` |
| `2026-06-24 03:42:10` | `cowrie.login.success` |
| `2026-06-24 03:42:13` | `cowrie.session.params` |
| `2026-06-24 03:42:13` | `cowrie.command.input` |
| `2026-06-24 03:42:13` | `cowrie.command.input` |
| `2026-06-24 03:42:13` | `cowrie.command.input` |
| `2026-06-24 03:42:13` | `cowrie.command.input` |
| `2026-06-24 03:42:14` | `cowrie.log.closed` |
| `2026-06-24 03:42:17` | `cowrie.session.params` |
| `2026-06-24 03:42:17` | `cowrie.command.input` |
| `2026-06-24 03:42:17` | `cowrie.command.input` |
| `2026-06-24 03:42:17` | `cowrie.command.failed` |
| `2026-06-24 03:42:17` | `cowrie.command.failed` |
| `2026-06-24 03:42:17` | `cowrie.command.failed` |
| `2026-06-24 03:42:17` | `cowrie.command.failed` |
| `2026-06-24 03:42:18` | `cowrie.log.closed` |
| `2026-06-24 03:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62265002a72f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:42 |
| **Last Seen** | 2026-06-24 03:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:42:41` | `cowrie.session.connect` |
| `2026-06-24 03:42:41` | `cowrie.client.version` |
| `2026-06-24 03:42:41` | `cowrie.client.kex` |
| `2026-06-24 03:42:41` | `cowrie.login.success` |
| `2026-06-24 03:42:42` | `cowrie.session.params` |
| `2026-06-24 03:42:42` | `cowrie.command.input` |
| `2026-06-24 03:42:42` | `cowrie.log.closed` |
| `2026-06-24 03:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f82eec3cea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:43 |
| **Last Seen** | 2026-06-24 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:43:39` | `cowrie.session.connect` |
| `2026-06-24 03:43:39` | `cowrie.client.version` |
| `2026-06-24 03:43:39` | `cowrie.client.kex` |
| `2026-06-24 03:43:39` | `cowrie.login.success` |
| `2026-06-24 03:43:40` | `cowrie.session.params` |
| `2026-06-24 03:43:40` | `cowrie.command.input` |
| `2026-06-24 03:43:40` | `cowrie.log.closed` |
| `2026-06-24 03:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ea5aea320d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 03:44 |
| **Last Seen** | 2026-06-24 03:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:44:20` | `cowrie.session.connect` |
| `2026-06-24 03:44:22` | `cowrie.client.version` |
| `2026-06-24 03:44:22` | `cowrie.client.kex` |
| `2026-06-24 03:44:29` | `cowrie.login.success` |
| `2026-06-24 03:44:32` | `cowrie.session.params` |
| `2026-06-24 03:44:32` | `cowrie.command.input` |
| `2026-06-24 03:44:34` | `cowrie.log.closed` |
| `2026-06-24 03:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4fe43670d0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:44 |
| **Last Seen** | 2026-06-24 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:44:37` | `cowrie.session.connect` |
| `2026-06-24 03:44:37` | `cowrie.client.version` |
| `2026-06-24 03:44:37` | `cowrie.client.kex` |
| `2026-06-24 03:44:38` | `cowrie.login.success` |
| `2026-06-24 03:44:39` | `cowrie.session.params` |
| `2026-06-24 03:44:39` | `cowrie.command.input` |
| `2026-06-24 03:44:39` | `cowrie.log.closed` |
| `2026-06-24 03:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffdc1a6fbb75

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:45 |
| **Last Seen** | 2026-06-24 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:45:37` | `cowrie.session.connect` |
| `2026-06-24 03:45:37` | `cowrie.client.version` |
| `2026-06-24 03:45:37` | `cowrie.client.kex` |
| `2026-06-24 03:45:37` | `cowrie.login.success` |
| `2026-06-24 03:45:38` | `cowrie.session.params` |
| `2026-06-24 03:45:38` | `cowrie.command.input` |
| `2026-06-24 03:45:38` | `cowrie.log.closed` |
| `2026-06-24 03:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d81cbffe0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:45 |
| **Last Seen** | 2026-06-24 03:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:45:42` | `cowrie.session.connect` |
| `2026-06-24 03:45:43` | `cowrie.client.version` |
| `2026-06-24 03:45:43` | `cowrie.client.kex` |
| `2026-06-24 03:45:47` | `cowrie.login.success` |
| `2026-06-24 03:45:49` | `cowrie.session.params` |
| `2026-06-24 03:45:49` | `cowrie.command.input` |
| `2026-06-24 03:45:49` | `cowrie.command.input` |
| `2026-06-24 03:45:49` | `cowrie.command.input` |
| `2026-06-24 03:45:49` | `cowrie.command.input` |
| `2026-06-24 03:45:50` | `cowrie.log.closed` |
| `2026-06-24 03:45:53` | `cowrie.session.params` |
| `2026-06-24 03:45:53` | `cowrie.command.input` |
| `2026-06-24 03:45:53` | `cowrie.command.input` |
| `2026-06-24 03:45:53` | `cowrie.command.failed` |
| `2026-06-24 03:45:53` | `cowrie.command.failed` |
| `2026-06-24 03:45:53` | `cowrie.command.failed` |
| `2026-06-24 03:45:53` | `cowrie.command.failed` |
| `2026-06-24 03:45:54` | `cowrie.log.closed` |
| `2026-06-24 03:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb64e729a293

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:46 |
| **Last Seen** | 2026-06-24 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:46:35` | `cowrie.session.connect` |
| `2026-06-24 03:46:35` | `cowrie.client.version` |
| `2026-06-24 03:46:35` | `cowrie.client.kex` |
| `2026-06-24 03:46:36` | `cowrie.login.success` |
| `2026-06-24 03:46:36` | `cowrie.session.params` |
| `2026-06-24 03:46:36` | `cowrie.command.input` |
| `2026-06-24 03:46:37` | `cowrie.log.closed` |
| `2026-06-24 03:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a5d6c75451

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:47 |
| **Last Seen** | 2026-06-24 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:47:34` | `cowrie.session.connect` |
| `2026-06-24 03:47:34` | `cowrie.client.version` |
| `2026-06-24 03:47:34` | `cowrie.client.kex` |
| `2026-06-24 03:47:35` | `cowrie.login.success` |
| `2026-06-24 03:47:35` | `cowrie.session.params` |
| `2026-06-24 03:47:35` | `cowrie.command.input` |
| `2026-06-24 03:47:36` | `cowrie.log.closed` |
| `2026-06-24 03:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe5e3d5d9d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:48 |
| **Last Seen** | 2026-06-24 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:48:32` | `cowrie.session.connect` |
| `2026-06-24 03:48:32` | `cowrie.client.version` |
| `2026-06-24 03:48:32` | `cowrie.client.kex` |
| `2026-06-24 03:48:32` | `cowrie.login.success` |
| `2026-06-24 03:48:33` | `cowrie.session.params` |
| `2026-06-24 03:48:33` | `cowrie.command.input` |
| `2026-06-24 03:48:33` | `cowrie.log.closed` |
| `2026-06-24 03:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc8df303fd6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:49 |
| **Last Seen** | 2026-06-24 03:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'ansible' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:49:15` | `cowrie.session.connect` |
| `2026-06-24 03:49:17` | `cowrie.client.version` |
| `2026-06-24 03:49:17` | `cowrie.client.kex` |
| `2026-06-24 03:49:20` | `cowrie.login.success` |
| `2026-06-24 03:49:22` | `cowrie.session.params` |
| `2026-06-24 03:49:22` | `cowrie.command.input` |
| `2026-06-24 03:49:22` | `cowrie.command.input` |
| `2026-06-24 03:49:22` | `cowrie.command.input` |
| `2026-06-24 03:49:22` | `cowrie.command.input` |
| `2026-06-24 03:49:24` | `cowrie.log.closed` |
| `2026-06-24 03:49:27` | `cowrie.session.params` |
| `2026-06-24 03:49:27` | `cowrie.command.input` |
| `2026-06-24 03:49:27` | `cowrie.command.input` |
| `2026-06-24 03:49:27` | `cowrie.command.failed` |
| `2026-06-24 03:49:27` | `cowrie.command.failed` |
| `2026-06-24 03:49:27` | `cowrie.command.failed` |
| `2026-06-24 03:49:27` | `cowrie.command.failed` |
| `2026-06-24 03:49:28` | `cowrie.log.closed` |
| `2026-06-24 03:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79702af15595

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:49 |
| **Last Seen** | 2026-06-24 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:49:29` | `cowrie.session.connect` |
| `2026-06-24 03:49:29` | `cowrie.client.version` |
| `2026-06-24 03:49:29` | `cowrie.client.kex` |
| `2026-06-24 03:49:30` | `cowrie.login.success` |
| `2026-06-24 03:49:30` | `cowrie.session.params` |
| `2026-06-24 03:49:30` | `cowrie.command.input` |
| `2026-06-24 03:49:31` | `cowrie.log.closed` |
| `2026-06-24 03:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10ad5d349ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:50 |
| **Last Seen** | 2026-06-24 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:50:28` | `cowrie.session.connect` |
| `2026-06-24 03:50:28` | `cowrie.client.version` |
| `2026-06-24 03:50:28` | `cowrie.client.kex` |
| `2026-06-24 03:50:29` | `cowrie.login.success` |
| `2026-06-24 03:50:29` | `cowrie.session.params` |
| `2026-06-24 03:50:29` | `cowrie.command.input` |
| `2026-06-24 03:50:30` | `cowrie.log.closed` |
| `2026-06-24 03:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66589e819fde

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:51 |
| **Last Seen** | 2026-06-24 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:51:29` | `cowrie.session.connect` |
| `2026-06-24 03:51:29` | `cowrie.client.version` |
| `2026-06-24 03:51:29` | `cowrie.client.kex` |
| `2026-06-24 03:51:29` | `cowrie.login.success` |
| `2026-06-24 03:51:30` | `cowrie.session.params` |
| `2026-06-24 03:51:30` | `cowrie.command.input` |
| `2026-06-24 03:51:30` | `cowrie.log.closed` |
| `2026-06-24 03:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f144c30eea99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:52 |
| **Last Seen** | 2026-06-24 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:52:30` | `cowrie.session.connect` |
| `2026-06-24 03:52:30` | `cowrie.client.version` |
| `2026-06-24 03:52:30` | `cowrie.client.kex` |
| `2026-06-24 03:52:30` | `cowrie.login.success` |
| `2026-06-24 03:52:31` | `cowrie.session.params` |
| `2026-06-24 03:52:31` | `cowrie.command.input` |
| `2026-06-24 03:52:31` | `cowrie.log.closed` |
| `2026-06-24 03:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea245ab68559

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:52 |
| **Last Seen** | 2026-06-24 03:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'ansible123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:52:56` | `cowrie.session.connect` |
| `2026-06-24 03:52:57` | `cowrie.client.version` |
| `2026-06-24 03:52:57` | `cowrie.client.kex` |
| `2026-06-24 03:53:01` | `cowrie.login.success` |
| `2026-06-24 03:53:04` | `cowrie.session.params` |
| `2026-06-24 03:53:04` | `cowrie.command.input` |
| `2026-06-24 03:53:04` | `cowrie.command.input` |
| `2026-06-24 03:53:04` | `cowrie.command.input` |
| `2026-06-24 03:53:04` | `cowrie.command.input` |
| `2026-06-24 03:53:05` | `cowrie.log.closed` |
| `2026-06-24 03:53:09` | `cowrie.session.params` |
| `2026-06-24 03:53:09` | `cowrie.command.input` |
| `2026-06-24 03:53:09` | `cowrie.command.input` |
| `2026-06-24 03:53:09` | `cowrie.command.failed` |
| `2026-06-24 03:53:09` | `cowrie.command.failed` |
| `2026-06-24 03:53:09` | `cowrie.command.failed` |
| `2026-06-24 03:53:09` | `cowrie.command.failed` |
| `2026-06-24 03:53:10` | `cowrie.log.closed` |
| `2026-06-24 03:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9da29c2b8e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:53 |
| **Last Seen** | 2026-06-24 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:53:30` | `cowrie.session.connect` |
| `2026-06-24 03:53:30` | `cowrie.client.version` |
| `2026-06-24 03:53:30` | `cowrie.client.kex` |
| `2026-06-24 03:53:30` | `cowrie.login.success` |
| `2026-06-24 03:53:31` | `cowrie.session.params` |
| `2026-06-24 03:53:31` | `cowrie.command.input` |
| `2026-06-24 03:53:31` | `cowrie.log.closed` |
| `2026-06-24 03:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f627a59e44f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:54 |
| **Last Seen** | 2026-06-24 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:54:29` | `cowrie.session.connect` |
| `2026-06-24 03:54:29` | `cowrie.client.version` |
| `2026-06-24 03:54:29` | `cowrie.client.kex` |
| `2026-06-24 03:54:30` | `cowrie.login.success` |
| `2026-06-24 03:54:31` | `cowrie.session.params` |
| `2026-06-24 03:54:31` | `cowrie.command.input` |
| `2026-06-24 03:54:31` | `cowrie.log.closed` |
| `2026-06-24 03:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6777842b79

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:55 |
| **Last Seen** | 2026-06-24 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:55:33` | `cowrie.session.connect` |
| `2026-06-24 03:55:33` | `cowrie.client.version` |
| `2026-06-24 03:55:33` | `cowrie.client.kex` |
| `2026-06-24 03:55:33` | `cowrie.login.success` |
| `2026-06-24 03:55:34` | `cowrie.session.params` |
| `2026-06-24 03:55:34` | `cowrie.command.input` |
| `2026-06-24 03:55:34` | `cowrie.log.closed` |
| `2026-06-24 03:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206f0dfa7429

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:56 |
| **Last Seen** | 2026-06-24 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:56:32` | `cowrie.session.connect` |
| `2026-06-24 03:56:32` | `cowrie.client.version` |
| `2026-06-24 03:56:32` | `cowrie.client.kex` |
| `2026-06-24 03:56:33` | `cowrie.login.success` |
| `2026-06-24 03:56:33` | `cowrie.session.params` |
| `2026-06-24 03:56:33` | `cowrie.command.input` |
| `2026-06-24 03:56:33` | `cowrie.log.closed` |
| `2026-06-24 03:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a67646beee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 03:56 |
| **Last Seen** | 2026-06-24 03:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'passw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:56:39` | `cowrie.session.connect` |
| `2026-06-24 03:56:39` | `cowrie.client.version` |
| `2026-06-24 03:56:39` | `cowrie.client.kex` |
| `2026-06-24 03:56:44` | `cowrie.login.success` |
| `2026-06-24 03:56:46` | `cowrie.session.params` |
| `2026-06-24 03:56:46` | `cowrie.command.input` |
| `2026-06-24 03:56:46` | `cowrie.command.input` |
| `2026-06-24 03:56:46` | `cowrie.command.input` |
| `2026-06-24 03:56:46` | `cowrie.command.input` |
| `2026-06-24 03:56:47` | `cowrie.log.closed` |
| `2026-06-24 03:56:49` | `cowrie.session.params` |
| `2026-06-24 03:56:49` | `cowrie.command.input` |
| `2026-06-24 03:56:49` | `cowrie.command.input` |
| `2026-06-24 03:56:49` | `cowrie.command.failed` |
| `2026-06-24 03:56:49` | `cowrie.command.failed` |
| `2026-06-24 03:56:49` | `cowrie.command.failed` |
| `2026-06-24 03:56:49` | `cowrie.command.failed` |
| `2026-06-24 03:56:50` | `cowrie.log.closed` |
| `2026-06-24 03:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a271ffaa80

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:57 |
| **Last Seen** | 2026-06-24 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:57:35` | `cowrie.session.connect` |
| `2026-06-24 03:57:35` | `cowrie.client.version` |
| `2026-06-24 03:57:35` | `cowrie.client.kex` |
| `2026-06-24 03:57:36` | `cowrie.login.success` |
| `2026-06-24 03:57:36` | `cowrie.session.params` |
| `2026-06-24 03:57:36` | `cowrie.command.input` |
| `2026-06-24 03:57:36` | `cowrie.log.closed` |
| `2026-06-24 03:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d6de5e9000

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:58 |
| **Last Seen** | 2026-06-24 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:58:39` | `cowrie.session.connect` |
| `2026-06-24 03:58:39` | `cowrie.client.version` |
| `2026-06-24 03:58:39` | `cowrie.client.kex` |
| `2026-06-24 03:58:39` | `cowrie.login.success` |
| `2026-06-24 03:58:40` | `cowrie.session.params` |
| `2026-06-24 03:58:40` | `cowrie.command.input` |
| `2026-06-24 03:58:40` | `cowrie.log.closed` |
| `2026-06-24 03:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb3a0adb521

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 03:59 |
| **Last Seen** | 2026-06-24 03:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:59:04` | `cowrie.session.connect` |
| `2026-06-24 03:59:06` | `cowrie.client.version` |
| `2026-06-24 03:59:06` | `cowrie.client.kex` |
| `2026-06-24 03:59:13` | `cowrie.login.success` |
| `2026-06-24 03:59:17` | `cowrie.session.params` |
| `2026-06-24 03:59:17` | `cowrie.command.input` |
| `2026-06-24 03:59:18` | `cowrie.log.closed` |
| `2026-06-24 03:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701c5d705dbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 03:59 |
| **Last Seen** | 2026-06-24 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 03:59:38` | `cowrie.session.connect` |
| `2026-06-24 03:59:38` | `cowrie.client.version` |
| `2026-06-24 03:59:38` | `cowrie.client.kex` |
| `2026-06-24 03:59:39` | `cowrie.login.success` |
| `2026-06-24 03:59:40` | `cowrie.session.params` |
| `2026-06-24 03:59:40` | `cowrie.command.input` |
| `2026-06-24 03:59:40` | `cowrie.log.closed` |
| `2026-06-24 03:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeff3fa24d86

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:00 |
| **Last Seen** | 2026-06-24 04:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:00:16` | `cowrie.session.connect` |
| `2026-06-24 04:00:18` | `cowrie.client.version` |
| `2026-06-24 04:00:18` | `cowrie.client.kex` |
| `2026-06-24 04:00:21` | `cowrie.login.success` |
| `2026-06-24 04:00:25` | `cowrie.session.params` |
| `2026-06-24 04:00:25` | `cowrie.command.input` |
| `2026-06-24 04:00:25` | `cowrie.command.input` |
| `2026-06-24 04:00:25` | `cowrie.command.input` |
| `2026-06-24 04:00:25` | `cowrie.command.input` |
| `2026-06-24 04:00:26` | `cowrie.log.closed` |
| `2026-06-24 04:00:28` | `cowrie.session.params` |
| `2026-06-24 04:00:28` | `cowrie.command.input` |
| `2026-06-24 04:00:28` | `cowrie.command.input` |
| `2026-06-24 04:00:28` | `cowrie.command.failed` |
| `2026-06-24 04:00:28` | `cowrie.command.failed` |
| `2026-06-24 04:00:28` | `cowrie.command.failed` |
| `2026-06-24 04:00:28` | `cowrie.command.failed` |
| `2026-06-24 04:00:29` | `cowrie.log.closed` |
| `2026-06-24 04:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c803a65ade

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:00 |
| **Last Seen** | 2026-06-24 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:00:36` | `cowrie.session.connect` |
| `2026-06-24 04:00:36` | `cowrie.client.version` |
| `2026-06-24 04:00:36` | `cowrie.client.kex` |
| `2026-06-24 04:00:36` | `cowrie.login.success` |
| `2026-06-24 04:00:37` | `cowrie.session.params` |
| `2026-06-24 04:00:37` | `cowrie.command.input` |
| `2026-06-24 04:00:37` | `cowrie.log.closed` |
| `2026-06-24 04:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817d46d6c783

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:01 |
| **Last Seen** | 2026-06-24 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:01:20` | `cowrie.session.connect` |
| `2026-06-24 04:01:20` | `cowrie.client.version` |
| `2026-06-24 04:01:20` | `cowrie.client.kex` |
| `2026-06-24 04:01:21` | `cowrie.login.success` |
| `2026-06-24 04:01:22` | `cowrie.session.params` |
| `2026-06-24 04:01:22` | `cowrie.command.input` |
| `2026-06-24 04:01:22` | `cowrie.log.closed` |
| `2026-06-24 04:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-855c9a95fcc5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:02 |
| **Last Seen** | 2026-06-24 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:02:05` | `cowrie.session.connect` |
| `2026-06-24 04:02:05` | `cowrie.client.version` |
| `2026-06-24 04:02:05` | `cowrie.client.kex` |
| `2026-06-24 04:02:05` | `cowrie.login.success` |
| `2026-06-24 04:02:06` | `cowrie.session.params` |
| `2026-06-24 04:02:06` | `cowrie.command.input` |
| `2026-06-24 04:02:06` | `cowrie.log.closed` |
| `2026-06-24 04:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c0318134ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:02 |
| **Last Seen** | 2026-06-24 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:02:51` | `cowrie.session.connect` |
| `2026-06-24 04:02:51` | `cowrie.client.version` |
| `2026-06-24 04:02:51` | `cowrie.client.kex` |
| `2026-06-24 04:02:52` | `cowrie.login.success` |
| `2026-06-24 04:02:53` | `cowrie.session.params` |
| `2026-06-24 04:02:53` | `cowrie.command.input` |
| `2026-06-24 04:02:53` | `cowrie.log.closed` |
| `2026-06-24 04:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcbac37277b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:03 |
| **Last Seen** | 2026-06-24 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:03:38` | `cowrie.session.connect` |
| `2026-06-24 04:03:38` | `cowrie.client.version` |
| `2026-06-24 04:03:38` | `cowrie.client.kex` |
| `2026-06-24 04:03:38` | `cowrie.login.success` |
| `2026-06-24 04:03:39` | `cowrie.session.params` |
| `2026-06-24 04:03:39` | `cowrie.command.input` |
| `2026-06-24 04:03:39` | `cowrie.log.closed` |
| `2026-06-24 04:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7297d6ab4ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:04 |
| **Last Seen** | 2026-06-24 04:04 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'P@ssw0rd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:04:00` | `cowrie.session.connect` |
| `2026-06-24 04:04:00` | `cowrie.client.version` |
| `2026-06-24 04:04:00` | `cowrie.client.kex` |
| `2026-06-24 04:04:03` | `cowrie.login.success` |
| `2026-06-24 04:04:05` | `cowrie.session.params` |
| `2026-06-24 04:04:05` | `cowrie.command.input` |
| `2026-06-24 04:04:05` | `cowrie.command.input` |
| `2026-06-24 04:04:05` | `cowrie.command.input` |
| `2026-06-24 04:04:05` | `cowrie.command.input` |
| `2026-06-24 04:04:07` | `cowrie.log.closed` |
| `2026-06-24 04:04:10` | `cowrie.session.params` |
| `2026-06-24 04:04:10` | `cowrie.command.input` |
| `2026-06-24 04:04:10` | `cowrie.command.input` |
| `2026-06-24 04:04:10` | `cowrie.command.failed` |
| `2026-06-24 04:04:10` | `cowrie.command.failed` |
| `2026-06-24 04:04:10` | `cowrie.command.failed` |
| `2026-06-24 04:04:10` | `cowrie.command.failed` |
| `2026-06-24 04:04:11` | `cowrie.log.closed` |
| `2026-06-24 04:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0c5c3e4e90

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:04 |
| **Last Seen** | 2026-06-24 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:04:25` | `cowrie.session.connect` |
| `2026-06-24 04:04:25` | `cowrie.client.version` |
| `2026-06-24 04:04:25` | `cowrie.client.kex` |
| `2026-06-24 04:04:25` | `cowrie.login.success` |
| `2026-06-24 04:04:26` | `cowrie.session.params` |
| `2026-06-24 04:04:26` | `cowrie.command.input` |
| `2026-06-24 04:04:26` | `cowrie.log.closed` |
| `2026-06-24 04:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a70e448b0b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:05 |
| **Last Seen** | 2026-06-24 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:05:12` | `cowrie.session.connect` |
| `2026-06-24 04:05:12` | `cowrie.client.version` |
| `2026-06-24 04:05:12` | `cowrie.client.kex` |
| `2026-06-24 04:05:13` | `cowrie.login.success` |
| `2026-06-24 04:05:14` | `cowrie.session.params` |
| `2026-06-24 04:05:14` | `cowrie.command.input` |
| `2026-06-24 04:05:14` | `cowrie.log.closed` |
| `2026-06-24 04:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae9ec1569a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:06 |
| **Last Seen** | 2026-06-24 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:06:00` | `cowrie.session.connect` |
| `2026-06-24 04:06:00` | `cowrie.client.version` |
| `2026-06-24 04:06:00` | `cowrie.client.kex` |
| `2026-06-24 04:06:00` | `cowrie.login.success` |
| `2026-06-24 04:06:01` | `cowrie.session.params` |
| `2026-06-24 04:06:01` | `cowrie.command.input` |
| `2026-06-24 04:06:01` | `cowrie.log.closed` |
| `2026-06-24 04:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7efd283fa3d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:06 |
| **Last Seen** | 2026-06-24 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:06:47` | `cowrie.session.connect` |
| `2026-06-24 04:06:47` | `cowrie.client.version` |
| `2026-06-24 04:06:47` | `cowrie.client.kex` |
| `2026-06-24 04:06:48` | `cowrie.login.success` |
| `2026-06-24 04:06:48` | `cowrie.session.params` |
| `2026-06-24 04:06:48` | `cowrie.command.input` |
| `2026-06-24 04:06:48` | `cowrie.log.closed` |
| `2026-06-24 04:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab6de1f8ff2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:07 |
| **Last Seen** | 2026-06-24 04:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'apache' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:07:31` | `cowrie.session.connect` |
| `2026-06-24 04:07:32` | `cowrie.client.version` |
| `2026-06-24 04:07:32` | `cowrie.client.kex` |
| `2026-06-24 04:07:37` | `cowrie.login.success` |
| `2026-06-24 04:07:39` | `cowrie.session.params` |
| `2026-06-24 04:07:39` | `cowrie.command.input` |
| `2026-06-24 04:07:39` | `cowrie.command.input` |
| `2026-06-24 04:07:39` | `cowrie.command.input` |
| `2026-06-24 04:07:39` | `cowrie.command.input` |
| `2026-06-24 04:07:41` | `cowrie.log.closed` |
| `2026-06-24 04:07:44` | `cowrie.session.params` |
| `2026-06-24 04:07:44` | `cowrie.command.input` |
| `2026-06-24 04:07:44` | `cowrie.command.input` |
| `2026-06-24 04:07:44` | `cowrie.command.failed` |
| `2026-06-24 04:07:44` | `cowrie.command.failed` |
| `2026-06-24 04:07:44` | `cowrie.command.failed` |
| `2026-06-24 04:07:44` | `cowrie.command.failed` |
| `2026-06-24 04:07:45` | `cowrie.log.closed` |
| `2026-06-24 04:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900015223a76

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:07 |
| **Last Seen** | 2026-06-24 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:07:33` | `cowrie.session.connect` |
| `2026-06-24 04:07:33` | `cowrie.client.version` |
| `2026-06-24 04:07:33` | `cowrie.client.kex` |
| `2026-06-24 04:07:34` | `cowrie.login.success` |
| `2026-06-24 04:07:35` | `cowrie.session.params` |
| `2026-06-24 04:07:35` | `cowrie.command.input` |
| `2026-06-24 04:07:35` | `cowrie.log.closed` |
| `2026-06-24 04:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807b53f6c986

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:08 |
| **Last Seen** | 2026-06-24 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:08:19` | `cowrie.session.connect` |
| `2026-06-24 04:08:19` | `cowrie.client.version` |
| `2026-06-24 04:08:19` | `cowrie.client.kex` |
| `2026-06-24 04:08:19` | `cowrie.login.success` |
| `2026-06-24 04:08:20` | `cowrie.session.params` |
| `2026-06-24 04:08:20` | `cowrie.command.input` |
| `2026-06-24 04:08:20` | `cowrie.log.closed` |
| `2026-06-24 04:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a1a4e47c8d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:09 |
| **Last Seen** | 2026-06-24 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:09:05` | `cowrie.session.connect` |
| `2026-06-24 04:09:05` | `cowrie.client.version` |
| `2026-06-24 04:09:05` | `cowrie.client.kex` |
| `2026-06-24 04:09:06` | `cowrie.login.success` |
| `2026-06-24 04:09:06` | `cowrie.session.params` |
| `2026-06-24 04:09:06` | `cowrie.command.input` |
| `2026-06-24 04:09:07` | `cowrie.log.closed` |
| `2026-06-24 04:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b96b55bee9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:09 |
| **Last Seen** | 2026-06-24 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:09:52` | `cowrie.session.connect` |
| `2026-06-24 04:09:52` | `cowrie.client.version` |
| `2026-06-24 04:09:52` | `cowrie.client.kex` |
| `2026-06-24 04:09:52` | `cowrie.login.success` |
| `2026-06-24 04:09:53` | `cowrie.session.params` |
| `2026-06-24 04:09:53` | `cowrie.command.input` |
| `2026-06-24 04:09:53` | `cowrie.log.closed` |
| `2026-06-24 04:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a500781dac8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:10 |
| **Last Seen** | 2026-06-24 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:10:40` | `cowrie.session.connect` |
| `2026-06-24 04:10:40` | `cowrie.client.version` |
| `2026-06-24 04:10:40` | `cowrie.client.kex` |
| `2026-06-24 04:10:40` | `cowrie.login.success` |
| `2026-06-24 04:10:41` | `cowrie.session.params` |
| `2026-06-24 04:10:41` | `cowrie.command.input` |
| `2026-06-24 04:10:41` | `cowrie.log.closed` |
| `2026-06-24 04:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7eef3466e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:11 |
| **Last Seen** | 2026-06-24 04:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:11:08` | `cowrie.session.connect` |
| `2026-06-24 04:11:09` | `cowrie.client.version` |
| `2026-06-24 04:11:09` | `cowrie.client.kex` |
| `2026-06-24 04:11:12` | `cowrie.login.success` |
| `2026-06-24 04:11:16` | `cowrie.session.params` |
| `2026-06-24 04:11:16` | `cowrie.command.input` |
| `2026-06-24 04:11:16` | `cowrie.command.input` |
| `2026-06-24 04:11:16` | `cowrie.command.input` |
| `2026-06-24 04:11:16` | `cowrie.command.input` |
| `2026-06-24 04:11:17` | `cowrie.log.closed` |
| `2026-06-24 04:11:19` | `cowrie.session.params` |
| `2026-06-24 04:11:19` | `cowrie.command.input` |
| `2026-06-24 04:11:19` | `cowrie.command.input` |
| `2026-06-24 04:11:19` | `cowrie.command.failed` |
| `2026-06-24 04:11:19` | `cowrie.command.failed` |
| `2026-06-24 04:11:19` | `cowrie.command.failed` |
| `2026-06-24 04:11:19` | `cowrie.command.failed` |
| `2026-06-24 04:11:20` | `cowrie.log.closed` |
| `2026-06-24 04:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b62ae0403d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:11 |
| **Last Seen** | 2026-06-24 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:11:29` | `cowrie.session.connect` |
| `2026-06-24 04:11:29` | `cowrie.client.version` |
| `2026-06-24 04:11:29` | `cowrie.client.kex` |
| `2026-06-24 04:11:29` | `cowrie.login.success` |
| `2026-06-24 04:11:30` | `cowrie.session.params` |
| `2026-06-24 04:11:30` | `cowrie.command.input` |
| `2026-06-24 04:11:30` | `cowrie.log.closed` |
| `2026-06-24 04:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f293771a5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:12 |
| **Last Seen** | 2026-06-24 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:12:17` | `cowrie.session.connect` |
| `2026-06-24 04:12:17` | `cowrie.client.version` |
| `2026-06-24 04:12:17` | `cowrie.client.kex` |
| `2026-06-24 04:12:17` | `cowrie.login.success` |
| `2026-06-24 04:12:18` | `cowrie.session.params` |
| `2026-06-24 04:12:18` | `cowrie.command.input` |
| `2026-06-24 04:12:18` | `cowrie.log.closed` |
| `2026-06-24 04:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e6b36a5c7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:13 |
| **Last Seen** | 2026-06-24 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:13:04` | `cowrie.session.connect` |
| `2026-06-24 04:13:04` | `cowrie.client.version` |
| `2026-06-24 04:13:04` | `cowrie.client.kex` |
| `2026-06-24 04:13:04` | `cowrie.login.success` |
| `2026-06-24 04:13:05` | `cowrie.session.params` |
| `2026-06-24 04:13:05` | `cowrie.command.input` |
| `2026-06-24 04:13:05` | `cowrie.log.closed` |
| `2026-06-24 04:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43954ebce498

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:13 |
| **Last Seen** | 2026-06-24 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:13:50` | `cowrie.session.connect` |
| `2026-06-24 04:13:50` | `cowrie.client.version` |
| `2026-06-24 04:13:50` | `cowrie.client.kex` |
| `2026-06-24 04:13:50` | `cowrie.login.success` |
| `2026-06-24 04:13:51` | `cowrie.session.params` |
| `2026-06-24 04:13:51` | `cowrie.command.input` |
| `2026-06-24 04:13:51` | `cowrie.log.closed` |
| `2026-06-24 04:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1972aab084ff

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 04:13 |
| **Last Seen** | 2026-06-24 04:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:13:51` | `cowrie.session.connect` |
| `2026-06-24 04:13:53` | `cowrie.client.version` |
| `2026-06-24 04:13:53` | `cowrie.client.kex` |
| `2026-06-24 04:13:59` | `cowrie.login.success` |
| `2026-06-24 04:14:03` | `cowrie.session.params` |
| `2026-06-24 04:14:03` | `cowrie.command.input` |
| `2026-06-24 04:14:05` | `cowrie.log.closed` |
| `2026-06-24 04:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d4bbafd761

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:14 |
| **Last Seen** | 2026-06-24 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:14:36` | `cowrie.session.connect` |
| `2026-06-24 04:14:36` | `cowrie.client.version` |
| `2026-06-24 04:14:36` | `cowrie.client.kex` |
| `2026-06-24 04:14:36` | `cowrie.login.success` |
| `2026-06-24 04:14:37` | `cowrie.session.params` |
| `2026-06-24 04:14:37` | `cowrie.command.input` |
| `2026-06-24 04:14:37` | `cowrie.log.closed` |
| `2026-06-24 04:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96cad04c4d47

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:14 |
| **Last Seen** | 2026-06-24 04:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123qwe' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:14:42` | `cowrie.session.connect` |
| `2026-06-24 04:14:43` | `cowrie.client.version` |
| `2026-06-24 04:14:43` | `cowrie.client.kex` |
| `2026-06-24 04:14:46` | `cowrie.login.success` |
| `2026-06-24 04:14:49` | `cowrie.session.params` |
| `2026-06-24 04:14:49` | `cowrie.command.input` |
| `2026-06-24 04:14:49` | `cowrie.command.input` |
| `2026-06-24 04:14:49` | `cowrie.command.input` |
| `2026-06-24 04:14:49` | `cowrie.command.input` |
| `2026-06-24 04:14:50` | `cowrie.log.closed` |
| `2026-06-24 04:14:53` | `cowrie.session.params` |
| `2026-06-24 04:14:53` | `cowrie.command.input` |
| `2026-06-24 04:14:53` | `cowrie.command.input` |
| `2026-06-24 04:14:53` | `cowrie.command.failed` |
| `2026-06-24 04:14:53` | `cowrie.command.failed` |
| `2026-06-24 04:14:53` | `cowrie.command.failed` |
| `2026-06-24 04:14:53` | `cowrie.command.failed` |
| `2026-06-24 04:14:54` | `cowrie.log.closed` |
| `2026-06-24 04:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1abb24142c25

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:15 |
| **Last Seen** | 2026-06-24 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:15:23` | `cowrie.session.connect` |
| `2026-06-24 04:15:23` | `cowrie.client.version` |
| `2026-06-24 04:15:23` | `cowrie.client.kex` |
| `2026-06-24 04:15:23` | `cowrie.login.success` |
| `2026-06-24 04:15:24` | `cowrie.session.params` |
| `2026-06-24 04:15:24` | `cowrie.command.input` |
| `2026-06-24 04:15:24` | `cowrie.log.closed` |
| `2026-06-24 04:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372bf250aa0d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:16 |
| **Last Seen** | 2026-06-24 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:16:11` | `cowrie.session.connect` |
| `2026-06-24 04:16:11` | `cowrie.client.version` |
| `2026-06-24 04:16:11` | `cowrie.client.kex` |
| `2026-06-24 04:16:11` | `cowrie.login.success` |
| `2026-06-24 04:16:12` | `cowrie.session.params` |
| `2026-06-24 04:16:12` | `cowrie.command.input` |
| `2026-06-24 04:16:12` | `cowrie.log.closed` |
| `2026-06-24 04:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3fee507a9ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:17 |
| **Last Seen** | 2026-06-24 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:17:00` | `cowrie.session.connect` |
| `2026-06-24 04:17:00` | `cowrie.client.version` |
| `2026-06-24 04:17:00` | `cowrie.client.kex` |
| `2026-06-24 04:17:00` | `cowrie.login.success` |
| `2026-06-24 04:17:02` | `cowrie.session.params` |
| `2026-06-24 04:17:02` | `cowrie.command.input` |
| `2026-06-24 04:17:02` | `cowrie.log.closed` |
| `2026-06-24 04:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900996b27b58

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:17 |
| **Last Seen** | 2026-06-24 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:17:49` | `cowrie.session.connect` |
| `2026-06-24 04:17:49` | `cowrie.client.version` |
| `2026-06-24 04:17:49` | `cowrie.client.kex` |
| `2026-06-24 04:17:50` | `cowrie.login.success` |
| `2026-06-24 04:17:50` | `cowrie.session.params` |
| `2026-06-24 04:17:50` | `cowrie.command.input` |
| `2026-06-24 04:17:50` | `cowrie.log.closed` |
| `2026-06-24 04:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd84ecf524cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:18 |
| **Last Seen** | 2026-06-24 04:18 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '54321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:18:21` | `cowrie.session.connect` |
| `2026-06-24 04:18:22` | `cowrie.client.version` |
| `2026-06-24 04:18:22` | `cowrie.client.kex` |
| `2026-06-24 04:18:27` | `cowrie.login.success` |
| `2026-06-24 04:18:30` | `cowrie.session.params` |
| `2026-06-24 04:18:30` | `cowrie.command.input` |
| `2026-06-24 04:18:30` | `cowrie.command.input` |
| `2026-06-24 04:18:30` | `cowrie.command.input` |
| `2026-06-24 04:18:30` | `cowrie.command.input` |
| `2026-06-24 04:18:33` | `cowrie.log.closed` |
| `2026-06-24 04:18:36` | `cowrie.session.params` |
| `2026-06-24 04:18:36` | `cowrie.command.input` |
| `2026-06-24 04:18:36` | `cowrie.command.input` |
| `2026-06-24 04:18:36` | `cowrie.command.failed` |
| `2026-06-24 04:18:36` | `cowrie.command.failed` |
| `2026-06-24 04:18:36` | `cowrie.command.failed` |
| `2026-06-24 04:18:36` | `cowrie.command.failed` |
| `2026-06-24 04:18:37` | `cowrie.log.closed` |
| `2026-06-24 04:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfe6cfae67f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:18 |
| **Last Seen** | 2026-06-24 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:18:38` | `cowrie.session.connect` |
| `2026-06-24 04:18:38` | `cowrie.client.version` |
| `2026-06-24 04:18:38` | `cowrie.client.kex` |
| `2026-06-24 04:18:39` | `cowrie.login.success` |
| `2026-06-24 04:18:39` | `cowrie.session.params` |
| `2026-06-24 04:18:39` | `cowrie.command.input` |
| `2026-06-24 04:18:39` | `cowrie.log.closed` |
| `2026-06-24 04:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1535a65a1a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:19 |
| **Last Seen** | 2026-06-24 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:19:27` | `cowrie.session.connect` |
| `2026-06-24 04:19:27` | `cowrie.client.version` |
| `2026-06-24 04:19:27` | `cowrie.client.kex` |
| `2026-06-24 04:19:27` | `cowrie.login.success` |
| `2026-06-24 04:19:28` | `cowrie.session.params` |
| `2026-06-24 04:19:28` | `cowrie.command.input` |
| `2026-06-24 04:19:28` | `cowrie.log.closed` |
| `2026-06-24 04:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e1948fa8e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:20 |
| **Last Seen** | 2026-06-24 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:20:15` | `cowrie.session.connect` |
| `2026-06-24 04:20:15` | `cowrie.client.version` |
| `2026-06-24 04:20:15` | `cowrie.client.kex` |
| `2026-06-24 04:20:16` | `cowrie.login.success` |
| `2026-06-24 04:20:16` | `cowrie.session.params` |
| `2026-06-24 04:20:16` | `cowrie.command.input` |
| `2026-06-24 04:20:17` | `cowrie.log.closed` |
| `2026-06-24 04:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f46e9781c8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:21 |
| **Last Seen** | 2026-06-24 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:21:02` | `cowrie.session.connect` |
| `2026-06-24 04:21:02` | `cowrie.client.version` |
| `2026-06-24 04:21:02` | `cowrie.client.kex` |
| `2026-06-24 04:21:02` | `cowrie.login.success` |
| `2026-06-24 04:21:03` | `cowrie.session.params` |
| `2026-06-24 04:21:03` | `cowrie.command.input` |
| `2026-06-24 04:21:03` | `cowrie.log.closed` |
| `2026-06-24 04:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-649bf200681b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:21 |
| **Last Seen** | 2026-06-24 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:21:49` | `cowrie.session.connect` |
| `2026-06-24 04:21:49` | `cowrie.client.version` |
| `2026-06-24 04:21:50` | `cowrie.client.kex` |
| `2026-06-24 04:21:50` | `cowrie.login.success` |
| `2026-06-24 04:21:51` | `cowrie.session.params` |
| `2026-06-24 04:21:51` | `cowrie.command.input` |
| `2026-06-24 04:21:51` | `cowrie.log.closed` |
| `2026-06-24 04:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ff9f955643

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:22 |
| **Last Seen** | 2026-06-24 04:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'backup' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:22:00` | `cowrie.session.connect` |
| `2026-06-24 04:22:01` | `cowrie.client.version` |
| `2026-06-24 04:22:01` | `cowrie.client.kex` |
| `2026-06-24 04:22:05` | `cowrie.login.success` |
| `2026-06-24 04:22:07` | `cowrie.session.params` |
| `2026-06-24 04:22:07` | `cowrie.command.input` |
| `2026-06-24 04:22:07` | `cowrie.command.input` |
| `2026-06-24 04:22:07` | `cowrie.command.input` |
| `2026-06-24 04:22:07` | `cowrie.command.input` |
| `2026-06-24 04:22:09` | `cowrie.log.closed` |
| `2026-06-24 04:22:11` | `cowrie.session.params` |
| `2026-06-24 04:22:11` | `cowrie.command.input` |
| `2026-06-24 04:22:11` | `cowrie.command.input` |
| `2026-06-24 04:22:11` | `cowrie.command.failed` |
| `2026-06-24 04:22:11` | `cowrie.command.failed` |
| `2026-06-24 04:22:11` | `cowrie.command.failed` |
| `2026-06-24 04:22:11` | `cowrie.command.failed` |
| `2026-06-24 04:22:12` | `cowrie.log.closed` |
| `2026-06-24 04:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c0e65afa504

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:22 |
| **Last Seen** | 2026-06-24 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:22:40` | `cowrie.session.connect` |
| `2026-06-24 04:22:40` | `cowrie.client.version` |
| `2026-06-24 04:22:40` | `cowrie.client.kex` |
| `2026-06-24 04:22:40` | `cowrie.login.success` |
| `2026-06-24 04:22:41` | `cowrie.session.params` |
| `2026-06-24 04:22:41` | `cowrie.command.input` |
| `2026-06-24 04:22:41` | `cowrie.log.closed` |
| `2026-06-24 04:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3a871d35ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:23 |
| **Last Seen** | 2026-06-24 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:23:32` | `cowrie.session.connect` |
| `2026-06-24 04:23:32` | `cowrie.client.version` |
| `2026-06-24 04:23:32` | `cowrie.client.kex` |
| `2026-06-24 04:23:32` | `cowrie.login.success` |
| `2026-06-24 04:23:33` | `cowrie.session.params` |
| `2026-06-24 04:23:33` | `cowrie.command.input` |
| `2026-06-24 04:23:33` | `cowrie.log.closed` |
| `2026-06-24 04:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3825aca1e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:24 |
| **Last Seen** | 2026-06-24 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:24:21` | `cowrie.session.connect` |
| `2026-06-24 04:24:21` | `cowrie.client.version` |
| `2026-06-24 04:24:22` | `cowrie.client.kex` |
| `2026-06-24 04:24:22` | `cowrie.login.success` |
| `2026-06-24 04:24:23` | `cowrie.session.params` |
| `2026-06-24 04:24:23` | `cowrie.command.input` |
| `2026-06-24 04:24:23` | `cowrie.log.closed` |
| `2026-06-24 04:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49598967a8b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:25 |
| **Last Seen** | 2026-06-24 04:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:25:10` | `cowrie.session.connect` |
| `2026-06-24 04:25:10` | `cowrie.client.version` |
| `2026-06-24 04:25:10` | `cowrie.client.kex` |
| `2026-06-24 04:25:11` | `cowrie.login.success` |
| `2026-06-24 04:25:11` | `cowrie.session.params` |
| `2026-06-24 04:25:11` | `cowrie.command.input` |
| `2026-06-24 04:25:12` | `cowrie.log.closed` |
| `2026-06-24 04:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e11cc334c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:25 |
| **Last Seen** | 2026-06-24 04:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'backup12' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:25:34` | `cowrie.session.connect` |
| `2026-06-24 04:25:36` | `cowrie.client.version` |
| `2026-06-24 04:25:36` | `cowrie.client.kex` |
| `2026-06-24 04:25:40` | `cowrie.login.success` |
| `2026-06-24 04:25:43` | `cowrie.session.params` |
| `2026-06-24 04:25:43` | `cowrie.command.input` |
| `2026-06-24 04:25:43` | `cowrie.command.input` |
| `2026-06-24 04:25:43` | `cowrie.command.input` |
| `2026-06-24 04:25:43` | `cowrie.command.input` |
| `2026-06-24 04:25:44` | `cowrie.log.closed` |
| `2026-06-24 04:25:47` | `cowrie.session.params` |
| `2026-06-24 04:25:47` | `cowrie.command.input` |
| `2026-06-24 04:25:47` | `cowrie.command.input` |
| `2026-06-24 04:25:47` | `cowrie.command.failed` |
| `2026-06-24 04:25:47` | `cowrie.command.failed` |
| `2026-06-24 04:25:47` | `cowrie.command.failed` |
| `2026-06-24 04:25:47` | `cowrie.command.failed` |
| `2026-06-24 04:25:49` | `cowrie.log.closed` |
| `2026-06-24 04:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f1cd549ade

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:25 |
| **Last Seen** | 2026-06-24 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:25:58` | `cowrie.session.connect` |
| `2026-06-24 04:25:58` | `cowrie.client.version` |
| `2026-06-24 04:25:58` | `cowrie.client.kex` |
| `2026-06-24 04:25:59` | `cowrie.login.success` |
| `2026-06-24 04:26:00` | `cowrie.session.params` |
| `2026-06-24 04:26:00` | `cowrie.command.input` |
| `2026-06-24 04:26:00` | `cowrie.log.closed` |
| `2026-06-24 04:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a34b463a72b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:26 |
| **Last Seen** | 2026-06-24 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:26:45` | `cowrie.session.connect` |
| `2026-06-24 04:26:45` | `cowrie.client.version` |
| `2026-06-24 04:26:45` | `cowrie.client.kex` |
| `2026-06-24 04:26:46` | `cowrie.login.success` |
| `2026-06-24 04:26:47` | `cowrie.session.params` |
| `2026-06-24 04:26:47` | `cowrie.command.input` |
| `2026-06-24 04:26:47` | `cowrie.log.closed` |
| `2026-06-24 04:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd255f10c15e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:27 |
| **Last Seen** | 2026-06-24 04:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:27:32` | `cowrie.session.connect` |
| `2026-06-24 04:27:32` | `cowrie.client.version` |
| `2026-06-24 04:27:32` | `cowrie.client.kex` |
| `2026-06-24 04:27:32` | `cowrie.login.success` |
| `2026-06-24 04:27:33` | `cowrie.session.params` |
| `2026-06-24 04:27:33` | `cowrie.command.input` |
| `2026-06-24 04:27:33` | `cowrie.log.closed` |
| `2026-06-24 04:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e9a6cbecf35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:28 |
| **Last Seen** | 2026-06-24 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:28:19` | `cowrie.session.connect` |
| `2026-06-24 04:28:19` | `cowrie.client.version` |
| `2026-06-24 04:28:19` | `cowrie.client.kex` |
| `2026-06-24 04:28:19` | `cowrie.login.success` |
| `2026-06-24 04:28:20` | `cowrie.session.params` |
| `2026-06-24 04:28:20` | `cowrie.command.input` |
| `2026-06-24 04:28:20` | `cowrie.log.closed` |
| `2026-06-24 04:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd5780989ba

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 04:28 |
| **Last Seen** | 2026-06-24 04:28 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:28:37` | `cowrie.session.connect` |
| `2026-06-24 04:28:38` | `cowrie.client.version` |
| `2026-06-24 04:28:38` | `cowrie.client.kex` |
| `2026-06-24 04:28:45` | `cowrie.login.success` |
| `2026-06-24 04:28:49` | `cowrie.session.params` |
| `2026-06-24 04:28:49` | `cowrie.command.input` |
| `2026-06-24 04:28:51` | `cowrie.log.closed` |
| `2026-06-24 04:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43871fc60836

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:29 |
| **Last Seen** | 2026-06-24 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:29:07` | `cowrie.session.connect` |
| `2026-06-24 04:29:07` | `cowrie.client.version` |
| `2026-06-24 04:29:07` | `cowrie.client.kex` |
| `2026-06-24 04:29:07` | `cowrie.login.success` |
| `2026-06-24 04:29:08` | `cowrie.session.params` |
| `2026-06-24 04:29:08` | `cowrie.command.input` |
| `2026-06-24 04:29:08` | `cowrie.log.closed` |
| `2026-06-24 04:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43d8eba07bab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:29 |
| **Last Seen** | 2026-06-24 04:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'backup123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:29:14` | `cowrie.session.connect` |
| `2026-06-24 04:29:15` | `cowrie.client.version` |
| `2026-06-24 04:29:15` | `cowrie.client.kex` |
| `2026-06-24 04:29:18` | `cowrie.login.success` |
| `2026-06-24 04:29:22` | `cowrie.session.params` |
| `2026-06-24 04:29:22` | `cowrie.command.input` |
| `2026-06-24 04:29:22` | `cowrie.command.input` |
| `2026-06-24 04:29:22` | `cowrie.command.input` |
| `2026-06-24 04:29:22` | `cowrie.command.input` |
| `2026-06-24 04:29:23` | `cowrie.log.closed` |
| `2026-06-24 04:29:25` | `cowrie.session.params` |
| `2026-06-24 04:29:26` | `cowrie.command.input` |
| `2026-06-24 04:29:26` | `cowrie.command.input` |
| `2026-06-24 04:29:26` | `cowrie.command.failed` |
| `2026-06-24 04:29:26` | `cowrie.command.failed` |
| `2026-06-24 04:29:26` | `cowrie.command.failed` |
| `2026-06-24 04:29:26` | `cowrie.command.failed` |
| `2026-06-24 04:29:26` | `cowrie.log.closed` |
| `2026-06-24 04:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f9eab6e2fd3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:29 |
| **Last Seen** | 2026-06-24 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:29:56` | `cowrie.session.connect` |
| `2026-06-24 04:29:56` | `cowrie.client.version` |
| `2026-06-24 04:29:56` | `cowrie.client.kex` |
| `2026-06-24 04:29:57` | `cowrie.login.success` |
| `2026-06-24 04:29:58` | `cowrie.session.params` |
| `2026-06-24 04:29:58` | `cowrie.command.input` |
| `2026-06-24 04:29:58` | `cowrie.log.closed` |
| `2026-06-24 04:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d6615fb9d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:30 |
| **Last Seen** | 2026-06-24 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:30:46` | `cowrie.session.connect` |
| `2026-06-24 04:30:46` | `cowrie.client.version` |
| `2026-06-24 04:30:46` | `cowrie.client.kex` |
| `2026-06-24 04:30:46` | `cowrie.login.success` |
| `2026-06-24 04:30:47` | `cowrie.session.params` |
| `2026-06-24 04:30:47` | `cowrie.command.input` |
| `2026-06-24 04:30:47` | `cowrie.log.closed` |
| `2026-06-24 04:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff22dde85edd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:31 |
| **Last Seen** | 2026-06-24 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:31:35` | `cowrie.session.connect` |
| `2026-06-24 04:31:35` | `cowrie.client.version` |
| `2026-06-24 04:31:35` | `cowrie.client.kex` |
| `2026-06-24 04:31:35` | `cowrie.login.success` |
| `2026-06-24 04:31:36` | `cowrie.session.params` |
| `2026-06-24 04:31:36` | `cowrie.command.input` |
| `2026-06-24 04:31:36` | `cowrie.log.closed` |
| `2026-06-24 04:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969bc7e41202

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:32 |
| **Last Seen** | 2026-06-24 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:32:24` | `cowrie.session.connect` |
| `2026-06-24 04:32:24` | `cowrie.client.version` |
| `2026-06-24 04:32:24` | `cowrie.client.kex` |
| `2026-06-24 04:32:24` | `cowrie.login.success` |
| `2026-06-24 04:32:25` | `cowrie.session.params` |
| `2026-06-24 04:32:25` | `cowrie.command.input` |
| `2026-06-24 04:32:25` | `cowrie.log.closed` |
| `2026-06-24 04:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69dec04fc1ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:32 |
| **Last Seen** | 2026-06-24 04:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:32:54` | `cowrie.session.connect` |
| `2026-06-24 04:32:54` | `cowrie.client.version` |
| `2026-06-24 04:32:54` | `cowrie.client.kex` |
| `2026-06-24 04:32:58` | `cowrie.login.success` |
| `2026-06-24 04:33:01` | `cowrie.session.params` |
| `2026-06-24 04:33:01` | `cowrie.command.input` |
| `2026-06-24 04:33:01` | `cowrie.command.input` |
| `2026-06-24 04:33:01` | `cowrie.command.input` |
| `2026-06-24 04:33:01` | `cowrie.command.input` |
| `2026-06-24 04:33:03` | `cowrie.log.closed` |
| `2026-06-24 04:33:05` | `cowrie.session.params` |
| `2026-06-24 04:33:05` | `cowrie.command.input` |
| `2026-06-24 04:33:05` | `cowrie.command.input` |
| `2026-06-24 04:33:05` | `cowrie.command.failed` |
| `2026-06-24 04:33:05` | `cowrie.command.failed` |
| `2026-06-24 04:33:05` | `cowrie.command.failed` |
| `2026-06-24 04:33:05` | `cowrie.command.failed` |
| `2026-06-24 04:33:06` | `cowrie.log.closed` |
| `2026-06-24 04:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35737536b69b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:33 |
| **Last Seen** | 2026-06-24 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:33:14` | `cowrie.session.connect` |
| `2026-06-24 04:33:14` | `cowrie.client.version` |
| `2026-06-24 04:33:14` | `cowrie.client.kex` |
| `2026-06-24 04:33:14` | `cowrie.login.success` |
| `2026-06-24 04:33:15` | `cowrie.session.params` |
| `2026-06-24 04:33:15` | `cowrie.command.input` |
| `2026-06-24 04:33:15` | `cowrie.log.closed` |
| `2026-06-24 04:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd75eaaa3dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:34 |
| **Last Seen** | 2026-06-24 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:34:04` | `cowrie.session.connect` |
| `2026-06-24 04:34:04` | `cowrie.client.version` |
| `2026-06-24 04:34:04` | `cowrie.client.kex` |
| `2026-06-24 04:34:05` | `cowrie.login.success` |
| `2026-06-24 04:34:06` | `cowrie.session.params` |
| `2026-06-24 04:34:06` | `cowrie.command.input` |
| `2026-06-24 04:34:06` | `cowrie.log.closed` |
| `2026-06-24 04:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90199c4a37ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:34 |
| **Last Seen** | 2026-06-24 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:34:55` | `cowrie.session.connect` |
| `2026-06-24 04:34:55` | `cowrie.client.version` |
| `2026-06-24 04:34:55` | `cowrie.client.kex` |
| `2026-06-24 04:34:55` | `cowrie.login.success` |
| `2026-06-24 04:34:56` | `cowrie.session.params` |
| `2026-06-24 04:34:56` | `cowrie.command.input` |
| `2026-06-24 04:34:56` | `cowrie.log.closed` |
| `2026-06-24 04:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24024a1eea99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:35 |
| **Last Seen** | 2026-06-24 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:35:45` | `cowrie.session.connect` |
| `2026-06-24 04:35:45` | `cowrie.client.version` |
| `2026-06-24 04:35:45` | `cowrie.client.kex` |
| `2026-06-24 04:35:46` | `cowrie.login.success` |
| `2026-06-24 04:35:47` | `cowrie.session.params` |
| `2026-06-24 04:35:47` | `cowrie.command.input` |
| `2026-06-24 04:35:47` | `cowrie.log.closed` |
| `2026-06-24 04:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56eef478da9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:36 |
| **Last Seen** | 2026-06-24 04:36 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'wasd' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:36:32` | `cowrie.session.connect` |
| `2026-06-24 04:36:33` | `cowrie.client.version` |
| `2026-06-24 04:36:33` | `cowrie.client.kex` |
| `2026-06-24 04:36:40` | `cowrie.login.success` |
| `2026-06-24 04:36:42` | `cowrie.session.params` |
| `2026-06-24 04:36:42` | `cowrie.command.input` |
| `2026-06-24 04:36:42` | `cowrie.command.input` |
| `2026-06-24 04:36:42` | `cowrie.command.input` |
| `2026-06-24 04:36:42` | `cowrie.command.input` |
| `2026-06-24 04:36:44` | `cowrie.log.closed` |
| `2026-06-24 04:36:46` | `cowrie.session.params` |
| `2026-06-24 04:36:46` | `cowrie.command.input` |
| `2026-06-24 04:36:46` | `cowrie.command.input` |
| `2026-06-24 04:36:46` | `cowrie.command.failed` |
| `2026-06-24 04:36:46` | `cowrie.command.failed` |
| `2026-06-24 04:36:46` | `cowrie.command.failed` |
| `2026-06-24 04:36:46` | `cowrie.command.failed` |
| `2026-06-24 04:36:47` | `cowrie.log.closed` |
| `2026-06-24 04:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea3867332d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:36 |
| **Last Seen** | 2026-06-24 04:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:36:37` | `cowrie.session.connect` |
| `2026-06-24 04:36:37` | `cowrie.client.version` |
| `2026-06-24 04:36:37` | `cowrie.client.kex` |
| `2026-06-24 04:36:37` | `cowrie.login.success` |
| `2026-06-24 04:36:38` | `cowrie.session.params` |
| `2026-06-24 04:36:38` | `cowrie.command.input` |
| `2026-06-24 04:36:38` | `cowrie.log.closed` |
| `2026-06-24 04:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12a079e703c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:37 |
| **Last Seen** | 2026-06-24 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:37:28` | `cowrie.session.connect` |
| `2026-06-24 04:37:28` | `cowrie.client.version` |
| `2026-06-24 04:37:28` | `cowrie.client.kex` |
| `2026-06-24 04:37:28` | `cowrie.login.success` |
| `2026-06-24 04:37:29` | `cowrie.session.params` |
| `2026-06-24 04:37:29` | `cowrie.command.input` |
| `2026-06-24 04:37:29` | `cowrie.log.closed` |
| `2026-06-24 04:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5422be189b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:38 |
| **Last Seen** | 2026-06-24 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:38:17` | `cowrie.session.connect` |
| `2026-06-24 04:38:17` | `cowrie.client.version` |
| `2026-06-24 04:38:17` | `cowrie.client.kex` |
| `2026-06-24 04:38:17` | `cowrie.login.success` |
| `2026-06-24 04:38:18` | `cowrie.session.params` |
| `2026-06-24 04:38:18` | `cowrie.command.input` |
| `2026-06-24 04:38:18` | `cowrie.log.closed` |
| `2026-06-24 04:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7fd75fc7e92

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:39 |
| **Last Seen** | 2026-06-24 04:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:39:05` | `cowrie.session.connect` |
| `2026-06-24 04:39:05` | `cowrie.client.version` |
| `2026-06-24 04:39:05` | `cowrie.client.kex` |
| `2026-06-24 04:39:05` | `cowrie.login.success` |
| `2026-06-24 04:39:06` | `cowrie.session.params` |
| `2026-06-24 04:39:06` | `cowrie.command.input` |
| `2026-06-24 04:39:06` | `cowrie.log.closed` |
| `2026-06-24 04:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3466c48f846

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:39 |
| **Last Seen** | 2026-06-24 04:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:39:53` | `cowrie.session.connect` |
| `2026-06-24 04:39:53` | `cowrie.client.version` |
| `2026-06-24 04:39:53` | `cowrie.client.kex` |
| `2026-06-24 04:39:54` | `cowrie.login.success` |
| `2026-06-24 04:39:54` | `cowrie.session.params` |
| `2026-06-24 04:39:54` | `cowrie.command.input` |
| `2026-06-24 04:39:54` | `cowrie.log.closed` |
| `2026-06-24 04:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03bcfa51dec3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:40 |
| **Last Seen** | 2026-06-24 04:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'centos' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:40:12` | `cowrie.session.connect` |
| `2026-06-24 04:40:14` | `cowrie.client.version` |
| `2026-06-24 04:40:14` | `cowrie.client.kex` |
| `2026-06-24 04:40:18` | `cowrie.login.success` |
| `2026-06-24 04:40:20` | `cowrie.session.params` |
| `2026-06-24 04:40:20` | `cowrie.command.input` |
| `2026-06-24 04:40:20` | `cowrie.command.input` |
| `2026-06-24 04:40:20` | `cowrie.command.input` |
| `2026-06-24 04:40:20` | `cowrie.command.input` |
| `2026-06-24 04:40:21` | `cowrie.log.closed` |
| `2026-06-24 04:40:24` | `cowrie.session.params` |
| `2026-06-24 04:40:24` | `cowrie.command.input` |
| `2026-06-24 04:40:24` | `cowrie.command.input` |
| `2026-06-24 04:40:24` | `cowrie.command.failed` |
| `2026-06-24 04:40:24` | `cowrie.command.failed` |
| `2026-06-24 04:40:24` | `cowrie.command.failed` |
| `2026-06-24 04:40:24` | `cowrie.command.failed` |
| `2026-06-24 04:40:25` | `cowrie.log.closed` |
| `2026-06-24 04:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3424e7e513b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:40 |
| **Last Seen** | 2026-06-24 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:40:41` | `cowrie.session.connect` |
| `2026-06-24 04:40:41` | `cowrie.client.version` |
| `2026-06-24 04:40:42` | `cowrie.client.kex` |
| `2026-06-24 04:40:42` | `cowrie.login.success` |
| `2026-06-24 04:40:43` | `cowrie.session.params` |
| `2026-06-24 04:40:43` | `cowrie.command.input` |
| `2026-06-24 04:40:43` | `cowrie.log.closed` |
| `2026-06-24 04:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0e6aac1ba1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:41 |
| **Last Seen** | 2026-06-24 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:41:30` | `cowrie.session.connect` |
| `2026-06-24 04:41:30` | `cowrie.client.version` |
| `2026-06-24 04:41:30` | `cowrie.client.kex` |
| `2026-06-24 04:41:31` | `cowrie.login.success` |
| `2026-06-24 04:41:31` | `cowrie.session.params` |
| `2026-06-24 04:41:31` | `cowrie.command.input` |
| `2026-06-24 04:41:32` | `cowrie.log.closed` |
| `2026-06-24 04:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1919a4fa251

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:42 |
| **Last Seen** | 2026-06-24 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:42:20` | `cowrie.session.connect` |
| `2026-06-24 04:42:20` | `cowrie.client.version` |
| `2026-06-24 04:42:21` | `cowrie.client.kex` |
| `2026-06-24 04:42:21` | `cowrie.login.success` |
| `2026-06-24 04:42:22` | `cowrie.session.params` |
| `2026-06-24 04:42:22` | `cowrie.command.input` |
| `2026-06-24 04:42:22` | `cowrie.log.closed` |
| `2026-06-24 04:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e54c7d50e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:43 |
| **Last Seen** | 2026-06-24 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:43:10` | `cowrie.session.connect` |
| `2026-06-24 04:43:10` | `cowrie.client.version` |
| `2026-06-24 04:43:10` | `cowrie.client.kex` |
| `2026-06-24 04:43:10` | `cowrie.login.success` |
| `2026-06-24 04:43:11` | `cowrie.session.params` |
| `2026-06-24 04:43:11` | `cowrie.command.input` |
| `2026-06-24 04:43:11` | `cowrie.log.closed` |
| `2026-06-24 04:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739773d2b4e3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 04:43 |
| **Last Seen** | 2026-06-24 04:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:43:34` | `cowrie.session.connect` |
| `2026-06-24 04:43:35` | `cowrie.client.version` |
| `2026-06-24 04:43:35` | `cowrie.client.kex` |
| `2026-06-24 04:43:42` | `cowrie.login.success` |
| `2026-06-24 04:43:46` | `cowrie.session.params` |
| `2026-06-24 04:43:46` | `cowrie.command.input` |
| `2026-06-24 04:43:48` | `cowrie.log.closed` |
| `2026-06-24 04:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b922f160810e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:43 |
| **Last Seen** | 2026-06-24 04:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'centos123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:43:43` | `cowrie.session.connect` |
| `2026-06-24 04:43:44` | `cowrie.client.version` |
| `2026-06-24 04:43:44` | `cowrie.client.kex` |
| `2026-06-24 04:43:50` | `cowrie.login.success` |
| `2026-06-24 04:43:52` | `cowrie.session.params` |
| `2026-06-24 04:43:52` | `cowrie.command.input` |
| `2026-06-24 04:43:52` | `cowrie.command.input` |
| `2026-06-24 04:43:52` | `cowrie.command.input` |
| `2026-06-24 04:43:52` | `cowrie.command.input` |
| `2026-06-24 04:43:53` | `cowrie.log.closed` |
| `2026-06-24 04:43:56` | `cowrie.session.params` |
| `2026-06-24 04:43:56` | `cowrie.command.input` |
| `2026-06-24 04:43:56` | `cowrie.command.input` |
| `2026-06-24 04:43:56` | `cowrie.command.failed` |
| `2026-06-24 04:43:56` | `cowrie.command.failed` |
| `2026-06-24 04:43:56` | `cowrie.command.failed` |
| `2026-06-24 04:43:56` | `cowrie.command.failed` |
| `2026-06-24 04:43:57` | `cowrie.log.closed` |
| `2026-06-24 04:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d442152c300

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:43 |
| **Last Seen** | 2026-06-24 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:43:59` | `cowrie.session.connect` |
| `2026-06-24 04:43:59` | `cowrie.client.version` |
| `2026-06-24 04:43:59` | `cowrie.client.kex` |
| `2026-06-24 04:43:59` | `cowrie.login.success` |
| `2026-06-24 04:44:00` | `cowrie.session.params` |
| `2026-06-24 04:44:00` | `cowrie.command.input` |
| `2026-06-24 04:44:00` | `cowrie.log.closed` |
| `2026-06-24 04:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0378a7d4d32b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:44 |
| **Last Seen** | 2026-06-24 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:44:48` | `cowrie.session.connect` |
| `2026-06-24 04:44:48` | `cowrie.client.version` |
| `2026-06-24 04:44:48` | `cowrie.client.kex` |
| `2026-06-24 04:44:48` | `cowrie.login.success` |
| `2026-06-24 04:44:49` | `cowrie.session.params` |
| `2026-06-24 04:44:49` | `cowrie.command.input` |
| `2026-06-24 04:44:49` | `cowrie.log.closed` |
| `2026-06-24 04:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a52cab7f4e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:45 |
| **Last Seen** | 2026-06-24 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:45:37` | `cowrie.session.connect` |
| `2026-06-24 04:45:37` | `cowrie.client.version` |
| `2026-06-24 04:45:37` | `cowrie.client.kex` |
| `2026-06-24 04:45:38` | `cowrie.login.success` |
| `2026-06-24 04:45:39` | `cowrie.session.params` |
| `2026-06-24 04:45:39` | `cowrie.command.input` |
| `2026-06-24 04:45:39` | `cowrie.log.closed` |
| `2026-06-24 04:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158f69ca1cb5

| Field | Detail |
|---|---|
| **Source IP** | `83.136.251[.]36` |
| **First Seen** | 2026-06-24 04:46 |
| **Last Seen** | 2026-06-24 04:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:46:12` | `cowrie.session.connect` |
| `2026-06-24 04:46:12` | `cowrie.client.version` |
| `2026-06-24 04:46:12` | `cowrie.client.kex` |
| `2026-06-24 04:46:13` | `cowrie.login.success` |
| `2026-06-24 04:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.136.251[.]36` to AbuseIPDB if not already reported
- [ ] Block `83.136.251[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bdbb8cd3673

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-24 04:46 |
| **Last Seen** | 2026-06-24 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:46:13` | `cowrie.session.connect` |
| `2026-06-24 04:46:13` | `cowrie.client.version` |
| `2026-06-24 04:46:13` | `cowrie.client.kex` |
| `2026-06-24 04:46:13` | `cowrie.login.success` |
| `2026-06-24 04:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd7fcbf9863

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:46 |
| **Last Seen** | 2026-06-24 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:46:26` | `cowrie.session.connect` |
| `2026-06-24 04:46:26` | `cowrie.client.version` |
| `2026-06-24 04:46:26` | `cowrie.client.kex` |
| `2026-06-24 04:46:26` | `cowrie.login.success` |
| `2026-06-24 04:46:27` | `cowrie.session.params` |
| `2026-06-24 04:46:27` | `cowrie.command.input` |
| `2026-06-24 04:46:27` | `cowrie.log.closed` |
| `2026-06-24 04:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0c7976e74e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:47 |
| **Last Seen** | 2026-06-24 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:47:16` | `cowrie.session.connect` |
| `2026-06-24 04:47:16` | `cowrie.client.version` |
| `2026-06-24 04:47:16` | `cowrie.client.kex` |
| `2026-06-24 04:47:16` | `cowrie.login.success` |
| `2026-06-24 04:47:17` | `cowrie.session.params` |
| `2026-06-24 04:47:17` | `cowrie.command.input` |
| `2026-06-24 04:47:17` | `cowrie.log.closed` |
| `2026-06-24 04:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49aa7c7e79d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:47 |
| **Last Seen** | 2026-06-24 04:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:47:27` | `cowrie.session.connect` |
| `2026-06-24 04:47:28` | `cowrie.client.version` |
| `2026-06-24 04:47:28` | `cowrie.client.kex` |
| `2026-06-24 04:47:32` | `cowrie.login.success` |
| `2026-06-24 04:47:34` | `cowrie.session.params` |
| `2026-06-24 04:47:34` | `cowrie.command.input` |
| `2026-06-24 04:47:34` | `cowrie.command.input` |
| `2026-06-24 04:47:34` | `cowrie.command.input` |
| `2026-06-24 04:47:34` | `cowrie.command.input` |
| `2026-06-24 04:47:36` | `cowrie.log.closed` |
| `2026-06-24 04:47:39` | `cowrie.session.params` |
| `2026-06-24 04:47:39` | `cowrie.command.input` |
| `2026-06-24 04:47:39` | `cowrie.command.input` |
| `2026-06-24 04:47:39` | `cowrie.command.failed` |
| `2026-06-24 04:47:39` | `cowrie.command.failed` |
| `2026-06-24 04:47:39` | `cowrie.command.failed` |
| `2026-06-24 04:47:39` | `cowrie.command.failed` |
| `2026-06-24 04:47:40` | `cowrie.log.closed` |
| `2026-06-24 04:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c17489bd1f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:48 |
| **Last Seen** | 2026-06-24 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:48:06` | `cowrie.session.connect` |
| `2026-06-24 04:48:06` | `cowrie.client.version` |
| `2026-06-24 04:48:06` | `cowrie.client.kex` |
| `2026-06-24 04:48:06` | `cowrie.login.success` |
| `2026-06-24 04:48:07` | `cowrie.session.params` |
| `2026-06-24 04:48:07` | `cowrie.command.input` |
| `2026-06-24 04:48:07` | `cowrie.log.closed` |
| `2026-06-24 04:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39509751360c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:48 |
| **Last Seen** | 2026-06-24 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:48:58` | `cowrie.session.connect` |
| `2026-06-24 04:48:58` | `cowrie.client.version` |
| `2026-06-24 04:48:58` | `cowrie.client.kex` |
| `2026-06-24 04:48:58` | `cowrie.login.success` |
| `2026-06-24 04:48:59` | `cowrie.session.params` |
| `2026-06-24 04:48:59` | `cowrie.command.input` |
| `2026-06-24 04:48:59` | `cowrie.log.closed` |
| `2026-06-24 04:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63bca4119c21

| Field | Detail |
|---|---|
| **Source IP** | `34.62.154[.]45` |
| **First Seen** | 2026-06-24 04:49 |
| **Last Seen** | 2026-06-24 04:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:49:44` | `cowrie.session.connect` |
| `2026-06-24 04:49:44` | `cowrie.client.version` |
| `2026-06-24 04:49:44` | `cowrie.client.kex` |
| `2026-06-24 04:49:46` | `cowrie.login.success` |
| `2026-06-24 04:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.154[.]45` to AbuseIPDB if not already reported
- [ ] Block `34.62.154[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87cdf37888f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:49 |
| **Last Seen** | 2026-06-24 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:49:50` | `cowrie.session.connect` |
| `2026-06-24 04:49:50` | `cowrie.client.version` |
| `2026-06-24 04:49:50` | `cowrie.client.kex` |
| `2026-06-24 04:49:50` | `cowrie.login.success` |
| `2026-06-24 04:49:51` | `cowrie.session.params` |
| `2026-06-24 04:49:51` | `cowrie.command.input` |
| `2026-06-24 04:49:51` | `cowrie.log.closed` |
| `2026-06-24 04:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6992913238d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:50 |
| **Last Seen** | 2026-06-24 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:50:40` | `cowrie.session.connect` |
| `2026-06-24 04:50:40` | `cowrie.client.version` |
| `2026-06-24 04:50:40` | `cowrie.client.kex` |
| `2026-06-24 04:50:40` | `cowrie.login.success` |
| `2026-06-24 04:50:41` | `cowrie.session.params` |
| `2026-06-24 04:50:41` | `cowrie.command.input` |
| `2026-06-24 04:50:41` | `cowrie.log.closed` |
| `2026-06-24 04:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4915196c6b56

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:51 |
| **Last Seen** | 2026-06-24 04:51 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123qwe' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:51:12` | `cowrie.session.connect` |
| `2026-06-24 04:51:13` | `cowrie.client.version` |
| `2026-06-24 04:51:13` | `cowrie.client.kex` |
| `2026-06-24 04:51:18` | `cowrie.login.success` |
| `2026-06-24 04:51:20` | `cowrie.session.params` |
| `2026-06-24 04:51:20` | `cowrie.command.input` |
| `2026-06-24 04:51:20` | `cowrie.command.input` |
| `2026-06-24 04:51:20` | `cowrie.command.input` |
| `2026-06-24 04:51:20` | `cowrie.command.input` |
| `2026-06-24 04:51:22` | `cowrie.log.closed` |
| `2026-06-24 04:51:25` | `cowrie.session.params` |
| `2026-06-24 04:51:25` | `cowrie.command.input` |
| `2026-06-24 04:51:25` | `cowrie.command.input` |
| `2026-06-24 04:51:25` | `cowrie.command.failed` |
| `2026-06-24 04:51:25` | `cowrie.command.failed` |
| `2026-06-24 04:51:25` | `cowrie.command.failed` |
| `2026-06-24 04:51:25` | `cowrie.command.failed` |
| `2026-06-24 04:51:26` | `cowrie.log.closed` |
| `2026-06-24 04:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1504d386c623

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:51 |
| **Last Seen** | 2026-06-24 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:51:30` | `cowrie.session.connect` |
| `2026-06-24 04:51:30` | `cowrie.client.version` |
| `2026-06-24 04:51:30` | `cowrie.client.kex` |
| `2026-06-24 04:51:30` | `cowrie.login.success` |
| `2026-06-24 04:51:31` | `cowrie.session.params` |
| `2026-06-24 04:51:31` | `cowrie.command.input` |
| `2026-06-24 04:51:31` | `cowrie.log.closed` |
| `2026-06-24 04:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db889bed4c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:52 |
| **Last Seen** | 2026-06-24 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:52:18` | `cowrie.session.connect` |
| `2026-06-24 04:52:18` | `cowrie.client.version` |
| `2026-06-24 04:52:18` | `cowrie.client.kex` |
| `2026-06-24 04:52:19` | `cowrie.login.success` |
| `2026-06-24 04:52:20` | `cowrie.session.params` |
| `2026-06-24 04:52:20` | `cowrie.command.input` |
| `2026-06-24 04:52:20` | `cowrie.log.closed` |
| `2026-06-24 04:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7adfc9ad19

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:53 |
| **Last Seen** | 2026-06-24 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:53:09` | `cowrie.session.connect` |
| `2026-06-24 04:53:09` | `cowrie.client.version` |
| `2026-06-24 04:53:09` | `cowrie.client.kex` |
| `2026-06-24 04:53:09` | `cowrie.login.success` |
| `2026-06-24 04:53:10` | `cowrie.session.params` |
| `2026-06-24 04:53:10` | `cowrie.command.input` |
| `2026-06-24 04:53:10` | `cowrie.log.closed` |
| `2026-06-24 04:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-134af137c8e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:54 |
| **Last Seen** | 2026-06-24 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:54:00` | `cowrie.session.connect` |
| `2026-06-24 04:54:00` | `cowrie.client.version` |
| `2026-06-24 04:54:00` | `cowrie.client.kex` |
| `2026-06-24 04:54:00` | `cowrie.login.success` |
| `2026-06-24 04:54:01` | `cowrie.session.params` |
| `2026-06-24 04:54:01` | `cowrie.command.input` |
| `2026-06-24 04:54:01` | `cowrie.log.closed` |
| `2026-06-24 04:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39bc2690bdb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:54 |
| **Last Seen** | 2026-06-24 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:54:51` | `cowrie.session.connect` |
| `2026-06-24 04:54:51` | `cowrie.client.version` |
| `2026-06-24 04:54:51` | `cowrie.client.kex` |
| `2026-06-24 04:54:51` | `cowrie.login.success` |
| `2026-06-24 04:54:52` | `cowrie.session.params` |
| `2026-06-24 04:54:52` | `cowrie.command.input` |
| `2026-06-24 04:54:52` | `cowrie.log.closed` |
| `2026-06-24 04:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9f523f9dde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:54 |
| **Last Seen** | 2026-06-24 04:55 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '54321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:54:53` | `cowrie.session.connect` |
| `2026-06-24 04:54:54` | `cowrie.client.version` |
| `2026-06-24 04:54:54` | `cowrie.client.kex` |
| `2026-06-24 04:54:58` | `cowrie.login.success` |
| `2026-06-24 04:55:02` | `cowrie.session.params` |
| `2026-06-24 04:55:02` | `cowrie.command.input` |
| `2026-06-24 04:55:02` | `cowrie.command.input` |
| `2026-06-24 04:55:02` | `cowrie.command.input` |
| `2026-06-24 04:55:02` | `cowrie.command.input` |
| `2026-06-24 04:55:03` | `cowrie.log.closed` |
| `2026-06-24 04:55:06` | `cowrie.session.params` |
| `2026-06-24 04:55:06` | `cowrie.command.input` |
| `2026-06-24 04:55:06` | `cowrie.command.input` |
| `2026-06-24 04:55:06` | `cowrie.command.failed` |
| `2026-06-24 04:55:06` | `cowrie.command.failed` |
| `2026-06-24 04:55:06` | `cowrie.command.failed` |
| `2026-06-24 04:55:06` | `cowrie.command.failed` |
| `2026-06-24 04:55:07` | `cowrie.log.closed` |
| `2026-06-24 04:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5bbce3011d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:55 |
| **Last Seen** | 2026-06-24 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:55:45` | `cowrie.session.connect` |
| `2026-06-24 04:55:45` | `cowrie.client.version` |
| `2026-06-24 04:55:45` | `cowrie.client.kex` |
| `2026-06-24 04:55:45` | `cowrie.login.success` |
| `2026-06-24 04:55:46` | `cowrie.session.params` |
| `2026-06-24 04:55:46` | `cowrie.command.input` |
| `2026-06-24 04:55:46` | `cowrie.log.closed` |
| `2026-06-24 04:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338ad55bff52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:56 |
| **Last Seen** | 2026-06-24 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:56:37` | `cowrie.session.connect` |
| `2026-06-24 04:56:37` | `cowrie.client.version` |
| `2026-06-24 04:56:37` | `cowrie.client.kex` |
| `2026-06-24 04:56:37` | `cowrie.login.success` |
| `2026-06-24 04:56:38` | `cowrie.session.params` |
| `2026-06-24 04:56:38` | `cowrie.command.input` |
| `2026-06-24 04:56:38` | `cowrie.log.closed` |
| `2026-06-24 04:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd92bbac1db3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:57 |
| **Last Seen** | 2026-06-24 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:57:28` | `cowrie.session.connect` |
| `2026-06-24 04:57:28` | `cowrie.client.version` |
| `2026-06-24 04:57:28` | `cowrie.client.kex` |
| `2026-06-24 04:57:28` | `cowrie.login.success` |
| `2026-06-24 04:57:29` | `cowrie.session.params` |
| `2026-06-24 04:57:29` | `cowrie.command.input` |
| `2026-06-24 04:57:29` | `cowrie.log.closed` |
| `2026-06-24 04:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51d52a44be6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:58 |
| **Last Seen** | 2026-06-24 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:58:18` | `cowrie.session.connect` |
| `2026-06-24 04:58:18` | `cowrie.client.version` |
| `2026-06-24 04:58:18` | `cowrie.client.kex` |
| `2026-06-24 04:58:18` | `cowrie.login.success` |
| `2026-06-24 04:58:19` | `cowrie.session.params` |
| `2026-06-24 04:58:19` | `cowrie.command.input` |
| `2026-06-24 04:58:19` | `cowrie.log.closed` |
| `2026-06-24 04:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d003a1fddcb8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 04:58 |
| **Last Seen** | 2026-06-24 04:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:58:31` | `cowrie.session.connect` |
| `2026-06-24 04:58:33` | `cowrie.client.version` |
| `2026-06-24 04:58:33` | `cowrie.client.kex` |
| `2026-06-24 04:58:40` | `cowrie.login.success` |
| `2026-06-24 04:58:43` | `cowrie.session.params` |
| `2026-06-24 04:58:43` | `cowrie.command.input` |
| `2026-06-24 04:58:44` | `cowrie.log.closed` |
| `2026-06-24 04:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d74fb916ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 04:58 |
| **Last Seen** | 2026-06-24 04:58 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '654321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:58:38` | `cowrie.session.connect` |
| `2026-06-24 04:58:40` | `cowrie.client.version` |
| `2026-06-24 04:58:40` | `cowrie.client.kex` |
| `2026-06-24 04:58:44` | `cowrie.login.success` |
| `2026-06-24 04:58:46` | `cowrie.session.params` |
| `2026-06-24 04:58:46` | `cowrie.command.input` |
| `2026-06-24 04:58:46` | `cowrie.command.input` |
| `2026-06-24 04:58:46` | `cowrie.command.input` |
| `2026-06-24 04:58:46` | `cowrie.command.input` |
| `2026-06-24 04:58:48` | `cowrie.log.closed` |
| `2026-06-24 04:58:52` | `cowrie.session.params` |
| `2026-06-24 04:58:52` | `cowrie.command.input` |
| `2026-06-24 04:58:52` | `cowrie.command.input` |
| `2026-06-24 04:58:52` | `cowrie.command.failed` |
| `2026-06-24 04:58:52` | `cowrie.command.failed` |
| `2026-06-24 04:58:52` | `cowrie.command.failed` |
| `2026-06-24 04:58:52` | `cowrie.command.failed` |
| `2026-06-24 04:58:53` | `cowrie.log.closed` |
| `2026-06-24 04:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3beffd11cf55

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 04:59 |
| **Last Seen** | 2026-06-24 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 04:59:08` | `cowrie.session.connect` |
| `2026-06-24 04:59:08` | `cowrie.client.version` |
| `2026-06-24 04:59:08` | `cowrie.client.kex` |
| `2026-06-24 04:59:09` | `cowrie.login.success` |
| `2026-06-24 04:59:09` | `cowrie.session.params` |
| `2026-06-24 04:59:09` | `cowrie.command.input` |
| `2026-06-24 04:59:09` | `cowrie.log.closed` |
| `2026-06-24 04:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f84bffe3874

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:00 |
| **Last Seen** | 2026-06-24 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:00:03` | `cowrie.session.connect` |
| `2026-06-24 05:00:03` | `cowrie.client.version` |
| `2026-06-24 05:00:03` | `cowrie.client.kex` |
| `2026-06-24 05:00:03` | `cowrie.login.success` |
| `2026-06-24 05:00:04` | `cowrie.session.params` |
| `2026-06-24 05:00:04` | `cowrie.command.input` |
| `2026-06-24 05:00:04` | `cowrie.log.closed` |
| `2026-06-24 05:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07fe912938e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:00 |
| **Last Seen** | 2026-06-24 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:00:58` | `cowrie.session.connect` |
| `2026-06-24 05:00:58` | `cowrie.client.version` |
| `2026-06-24 05:00:58` | `cowrie.client.kex` |
| `2026-06-24 05:00:58` | `cowrie.login.success` |
| `2026-06-24 05:00:59` | `cowrie.session.params` |
| `2026-06-24 05:00:59` | `cowrie.command.input` |
| `2026-06-24 05:00:59` | `cowrie.log.closed` |
| `2026-06-24 05:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f31d88059a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:01 |
| **Last Seen** | 2026-06-24 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:01:54` | `cowrie.session.connect` |
| `2026-06-24 05:01:54` | `cowrie.client.version` |
| `2026-06-24 05:01:54` | `cowrie.client.kex` |
| `2026-06-24 05:01:54` | `cowrie.login.success` |
| `2026-06-24 05:01:55` | `cowrie.session.params` |
| `2026-06-24 05:01:55` | `cowrie.command.input` |
| `2026-06-24 05:01:55` | `cowrie.log.closed` |
| `2026-06-24 05:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaebfd2f3e88

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:02 |
| **Last Seen** | 2026-06-24 05:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'debian' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:02:22` | `cowrie.session.connect` |
| `2026-06-24 05:02:23` | `cowrie.client.version` |
| `2026-06-24 05:02:23` | `cowrie.client.kex` |
| `2026-06-24 05:02:27` | `cowrie.login.success` |
| `2026-06-24 05:02:30` | `cowrie.session.params` |
| `2026-06-24 05:02:30` | `cowrie.command.input` |
| `2026-06-24 05:02:30` | `cowrie.command.input` |
| `2026-06-24 05:02:30` | `cowrie.command.input` |
| `2026-06-24 05:02:30` | `cowrie.command.input` |
| `2026-06-24 05:02:31` | `cowrie.log.closed` |
| `2026-06-24 05:02:34` | `cowrie.session.params` |
| `2026-06-24 05:02:34` | `cowrie.command.input` |
| `2026-06-24 05:02:34` | `cowrie.command.input` |
| `2026-06-24 05:02:34` | `cowrie.command.failed` |
| `2026-06-24 05:02:34` | `cowrie.command.failed` |
| `2026-06-24 05:02:34` | `cowrie.command.failed` |
| `2026-06-24 05:02:34` | `cowrie.command.failed` |
| `2026-06-24 05:02:35` | `cowrie.log.closed` |
| `2026-06-24 05:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824f53ce7fff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:02 |
| **Last Seen** | 2026-06-24 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:02:50` | `cowrie.session.connect` |
| `2026-06-24 05:02:50` | `cowrie.client.version` |
| `2026-06-24 05:02:50` | `cowrie.client.kex` |
| `2026-06-24 05:02:50` | `cowrie.login.success` |
| `2026-06-24 05:02:51` | `cowrie.session.params` |
| `2026-06-24 05:02:51` | `cowrie.command.input` |
| `2026-06-24 05:02:51` | `cowrie.log.closed` |
| `2026-06-24 05:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9338879e3d7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:03 |
| **Last Seen** | 2026-06-24 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:03:47` | `cowrie.session.connect` |
| `2026-06-24 05:03:47` | `cowrie.client.version` |
| `2026-06-24 05:03:47` | `cowrie.client.kex` |
| `2026-06-24 05:03:48` | `cowrie.login.success` |
| `2026-06-24 05:03:49` | `cowrie.session.params` |
| `2026-06-24 05:03:49` | `cowrie.command.input` |
| `2026-06-24 05:03:49` | `cowrie.log.closed` |
| `2026-06-24 05:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-699eaa782a25

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:04 |
| **Last Seen** | 2026-06-24 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:04:40` | `cowrie.session.connect` |
| `2026-06-24 05:04:40` | `cowrie.client.version` |
| `2026-06-24 05:04:40` | `cowrie.client.kex` |
| `2026-06-24 05:04:40` | `cowrie.login.success` |
| `2026-06-24 05:04:41` | `cowrie.session.params` |
| `2026-06-24 05:04:41` | `cowrie.command.input` |
| `2026-06-24 05:04:41` | `cowrie.log.closed` |
| `2026-06-24 05:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cc67625070b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:05 |
| **Last Seen** | 2026-06-24 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:05:31` | `cowrie.session.connect` |
| `2026-06-24 05:05:31` | `cowrie.client.version` |
| `2026-06-24 05:05:31` | `cowrie.client.kex` |
| `2026-06-24 05:05:32` | `cowrie.login.success` |
| `2026-06-24 05:05:33` | `cowrie.session.params` |
| `2026-06-24 05:05:33` | `cowrie.command.input` |
| `2026-06-24 05:05:33` | `cowrie.log.closed` |
| `2026-06-24 05:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5bad968aa8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:06 |
| **Last Seen** | 2026-06-24 05:06 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'debian12' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:06:05` | `cowrie.session.connect` |
| `2026-06-24 05:06:06` | `cowrie.client.version` |
| `2026-06-24 05:06:06` | `cowrie.client.kex` |
| `2026-06-24 05:06:11` | `cowrie.login.success` |
| `2026-06-24 05:06:14` | `cowrie.session.params` |
| `2026-06-24 05:06:14` | `cowrie.command.input` |
| `2026-06-24 05:06:14` | `cowrie.command.input` |
| `2026-06-24 05:06:14` | `cowrie.command.input` |
| `2026-06-24 05:06:14` | `cowrie.command.input` |
| `2026-06-24 05:06:15` | `cowrie.log.closed` |
| `2026-06-24 05:06:18` | `cowrie.session.params` |
| `2026-06-24 05:06:18` | `cowrie.command.input` |
| `2026-06-24 05:06:18` | `cowrie.command.input` |
| `2026-06-24 05:06:18` | `cowrie.command.failed` |
| `2026-06-24 05:06:18` | `cowrie.command.failed` |
| `2026-06-24 05:06:18` | `cowrie.command.failed` |
| `2026-06-24 05:06:18` | `cowrie.command.failed` |
| `2026-06-24 05:06:19` | `cowrie.log.closed` |
| `2026-06-24 05:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035752d99f21

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:06 |
| **Last Seen** | 2026-06-24 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:06:23` | `cowrie.session.connect` |
| `2026-06-24 05:06:23` | `cowrie.client.version` |
| `2026-06-24 05:06:24` | `cowrie.client.kex` |
| `2026-06-24 05:06:24` | `cowrie.login.success` |
| `2026-06-24 05:06:25` | `cowrie.session.params` |
| `2026-06-24 05:06:25` | `cowrie.command.input` |
| `2026-06-24 05:06:25` | `cowrie.log.closed` |
| `2026-06-24 05:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe6e2d90d45

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:07 |
| **Last Seen** | 2026-06-24 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:07:17` | `cowrie.session.connect` |
| `2026-06-24 05:07:17` | `cowrie.client.version` |
| `2026-06-24 05:07:17` | `cowrie.client.kex` |
| `2026-06-24 05:07:17` | `cowrie.login.success` |
| `2026-06-24 05:07:18` | `cowrie.session.params` |
| `2026-06-24 05:07:18` | `cowrie.command.input` |
| `2026-06-24 05:07:18` | `cowrie.log.closed` |
| `2026-06-24 05:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476f70a43222

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:15` | `cowrie.session.connect` |
| `2026-06-24 05:08:15` | `cowrie.client.version` |
| `2026-06-24 05:08:15` | `cowrie.client.kex` |
| `2026-06-24 05:08:15` | `cowrie.login.success` |
| `2026-06-24 05:08:16` | `cowrie.session.params` |
| `2026-06-24 05:08:16` | `cowrie.command.input` |
| `2026-06-24 05:08:16` | `cowrie.command.failed` |
| `2026-06-24 05:08:17` | `cowrie.log.closed` |
| `2026-06-24 05:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7910c9edde5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:15` | `cowrie.session.connect` |
| `2026-06-24 05:08:15` | `cowrie.client.version` |
| `2026-06-24 05:08:15` | `cowrie.client.kex` |
| `2026-06-24 05:08:15` | `cowrie.login.success` |
| `2026-06-24 05:08:17` | `cowrie.session.params` |
| `2026-06-24 05:08:17` | `cowrie.command.input` |
| `2026-06-24 05:08:17` | `cowrie.log.closed` |
| `2026-06-24 05:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d56039a17a9

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:17` | `cowrie.session.connect` |
| `2026-06-24 05:08:17` | `cowrie.login.success` |
| `2026-06-24 05:08:18` | `cowrie.session.params` |
| `2026-06-24 05:08:18` | `cowrie.command.input` |
| `2026-06-24 05:08:18` | `cowrie.command.input` |
| `2026-06-24 05:08:18` | `cowrie.command.failed` |
| `2026-06-24 05:08:18` | `cowrie.command.input` |
| `2026-06-24 05:08:18` | `cowrie.command.input` |
| `2026-06-24 05:08:18` | `cowrie.command.input` |
| `2026-06-24 05:08:19` | `cowrie.log.closed` |
| `2026-06-24 05:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce052584036

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:18` | `cowrie.session.connect` |
| `2026-06-24 05:08:18` | `cowrie.client.version` |
| `2026-06-24 05:08:18` | `cowrie.client.kex` |
| `2026-06-24 05:08:19` | `cowrie.login.success` |
| `2026-06-24 05:08:20` | `cowrie.session.params` |
| `2026-06-24 05:08:20` | `cowrie.command.input` |
| `2026-06-24 05:08:20` | `cowrie.command.failed` |
| `2026-06-24 05:08:20` | `cowrie.log.closed` |
| `2026-06-24 05:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4bf3d4076ce

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:19` | `cowrie.session.connect` |
| `2026-06-24 05:08:19` | `cowrie.client.version` |
| `2026-06-24 05:08:19` | `cowrie.client.kex` |
| `2026-06-24 05:08:19` | `cowrie.login.success` |
| `2026-06-24 05:08:21` | `cowrie.session.params` |
| `2026-06-24 05:08:21` | `cowrie.command.input` |
| `2026-06-24 05:08:21` | `cowrie.command.failed` |
| `2026-06-24 05:08:21` | `cowrie.log.closed` |
| `2026-06-24 05:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce6f6622f59

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:19` | `cowrie.session.connect` |
| `2026-06-24 05:08:19` | `cowrie.client.version` |
| `2026-06-24 05:08:19` | `cowrie.client.kex` |
| `2026-06-24 05:08:21` | `cowrie.login.success` |
| `2026-06-24 05:08:21` | `cowrie.session.params` |
| `2026-06-24 05:08:21` | `cowrie.command.input` |
| `2026-06-24 05:08:21` | `cowrie.command.failed` |
| `2026-06-24 05:08:23` | `cowrie.log.closed` |
| `2026-06-24 05:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a69e123abc0

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:19` | `cowrie.session.connect` |
| `2026-06-24 05:08:19` | `cowrie.client.version` |
| `2026-06-24 05:08:20` | `cowrie.client.kex` |
| `2026-06-24 05:08:21` | `cowrie.login.success` |
| `2026-06-24 05:08:23` | `cowrie.session.params` |
| `2026-06-24 05:08:23` | `cowrie.command.input` |
| `2026-06-24 05:08:23` | `cowrie.command.failed` |
| `2026-06-24 05:08:23` | `cowrie.log.closed` |
| `2026-06-24 05:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057cbab589c8

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:20` | `cowrie.session.connect` |
| `2026-06-24 05:08:20` | `cowrie.client.version` |
| `2026-06-24 05:08:21` | `cowrie.client.kex` |
| `2026-06-24 05:08:23` | `cowrie.login.success` |
| `2026-06-24 05:08:26` | `cowrie.session.params` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.failed` |
| `2026-06-24 05:08:26` | `cowrie.log.closed` |
| `2026-06-24 05:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde2f26962ab

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:21` | `cowrie.session.connect` |
| `2026-06-24 05:08:21` | `cowrie.login.success` |
| `2026-06-24 05:08:22` | `cowrie.session.params` |
| `2026-06-24 05:08:23` | `cowrie.command.input` |
| `2026-06-24 05:08:23` | `cowrie.command.input` |
| `2026-06-24 05:08:23` | `cowrie.command.failed` |
| `2026-06-24 05:08:23` | `cowrie.command.input` |
| `2026-06-24 05:08:23` | `cowrie.command.input` |
| `2026-06-24 05:08:23` | `cowrie.command.input` |
| `2026-06-24 05:08:24` | `cowrie.log.closed` |
| `2026-06-24 05:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ccf637c334

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:21` | `cowrie.session.connect` |
| `2026-06-24 05:08:23` | `cowrie.login.success` |
| `2026-06-24 05:08:24` | `cowrie.session.params` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.failed` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.log.closed` |
| `2026-06-24 05:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e0527be392f

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:23` | `cowrie.session.connect` |
| `2026-06-24 05:08:24` | `cowrie.login.success` |
| `2026-06-24 05:08:24` | `cowrie.session.params` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.failed` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:27` | `cowrie.log.closed` |
| `2026-06-24 05:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e300a14d37

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:24` | `cowrie.session.connect` |
| `2026-06-24 05:08:24` | `cowrie.login.success` |
| `2026-06-24 05:08:25` | `cowrie.session.params` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.failed` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:26` | `cowrie.command.input` |
| `2026-06-24 05:08:27` | `cowrie.log.closed` |
| `2026-06-24 05:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7903c7c89bd

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:24` | `cowrie.session.connect` |
| `2026-06-24 05:08:24` | `cowrie.client.version` |
| `2026-06-24 05:08:24` | `cowrie.client.kex` |
| `2026-06-24 05:08:26` | `cowrie.login.success` |
| `2026-06-24 05:08:28` | `cowrie.session.params` |
| `2026-06-24 05:08:28` | `cowrie.command.input` |
| `2026-06-24 05:08:28` | `cowrie.command.failed` |
| `2026-06-24 05:08:28` | `cowrie.log.closed` |
| `2026-06-24 05:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225a9921e99f

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:26` | `cowrie.session.connect` |
| `2026-06-24 05:08:26` | `cowrie.login.success` |
| `2026-06-24 05:08:27` | `cowrie.session.params` |
| `2026-06-24 05:08:28` | `cowrie.command.input` |
| `2026-06-24 05:08:28` | `cowrie.command.input` |
| `2026-06-24 05:08:28` | `cowrie.command.failed` |
| `2026-06-24 05:08:28` | `cowrie.command.input` |
| `2026-06-24 05:08:28` | `cowrie.command.input` |
| `2026-06-24 05:08:28` | `cowrie.command.input` |
| `2026-06-24 05:08:28` | `cowrie.log.closed` |
| `2026-06-24 05:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98ed2617005

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:27` | `cowrie.session.connect` |
| `2026-06-24 05:08:27` | `cowrie.client.version` |
| `2026-06-24 05:08:28` | `cowrie.client.kex` |
| `2026-06-24 05:08:28` | `cowrie.login.success` |
| `2026-06-24 05:08:30` | `cowrie.session.params` |
| `2026-06-24 05:08:30` | `cowrie.command.input` |
| `2026-06-24 05:08:30` | `cowrie.command.failed` |
| `2026-06-24 05:08:31` | `cowrie.log.closed` |
| `2026-06-24 05:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66252b43cbbb

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:27` | `cowrie.session.connect` |
| `2026-06-24 05:08:27` | `cowrie.client.version` |
| `2026-06-24 05:08:28` | `cowrie.client.kex` |
| `2026-06-24 05:08:28` | `cowrie.login.success` |
| `2026-06-24 05:08:29` | `cowrie.session.params` |
| `2026-06-24 05:08:29` | `cowrie.command.input` |
| `2026-06-24 05:08:29` | `cowrie.command.failed` |
| `2026-06-24 05:08:31` | `cowrie.log.closed` |
| `2026-06-24 05:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace11b117d1b

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:28` | `cowrie.session.connect` |
| `2026-06-24 05:08:28` | `cowrie.client.version` |
| `2026-06-24 05:08:28` | `cowrie.client.kex` |
| `2026-06-24 05:08:28` | `cowrie.login.success` |
| `2026-06-24 05:08:31` | `cowrie.session.params` |
| `2026-06-24 05:08:31` | `cowrie.command.input` |
| `2026-06-24 05:08:31` | `cowrie.command.failed` |
| `2026-06-24 05:08:31` | `cowrie.log.closed` |
| `2026-06-24 05:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006266f28e10

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:28` | `cowrie.session.connect` |
| `2026-06-24 05:08:28` | `cowrie.login.success` |
| `2026-06-24 05:08:28` | `cowrie.session.params` |
| `2026-06-24 05:08:31` | `cowrie.command.input` |
| `2026-06-24 05:08:31` | `cowrie.command.input` |
| `2026-06-24 05:08:31` | `cowrie.command.failed` |
| `2026-06-24 05:08:31` | `cowrie.command.input` |
| `2026-06-24 05:08:31` | `cowrie.command.input` |
| `2026-06-24 05:08:31` | `cowrie.command.input` |
| `2026-06-24 05:08:31` | `cowrie.log.closed` |
| `2026-06-24 05:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095fed8cfaef

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:28` | `cowrie.session.connect` |
| `2026-06-24 05:08:28` | `cowrie.client.version` |
| `2026-06-24 05:08:29` | `cowrie.client.kex` |
| `2026-06-24 05:08:32` | `cowrie.login.success` |
| `2026-06-24 05:08:33` | `cowrie.session.params` |
| `2026-06-24 05:08:33` | `cowrie.command.input` |
| `2026-06-24 05:08:33` | `cowrie.command.failed` |
| `2026-06-24 05:08:34` | `cowrie.log.closed` |
| `2026-06-24 05:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3aba651bb9

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:31` | `cowrie.session.connect` |
| `2026-06-24 05:08:32` | `cowrie.login.success` |
| `2026-06-24 05:08:32` | `cowrie.session.params` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.failed` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.log.closed` |
| `2026-06-24 05:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eadc4599750

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:31` | `cowrie.session.connect` |
| `2026-06-24 05:08:31` | `cowrie.login.success` |
| `2026-06-24 05:08:32` | `cowrie.session.params` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.failed` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.command.input` |
| `2026-06-24 05:08:34` | `cowrie.log.closed` |
| `2026-06-24 05:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b83882e56c

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:31` | `cowrie.session.connect` |
| `2026-06-24 05:08:33` | `cowrie.login.success` |
| `2026-06-24 05:08:34` | `cowrie.session.params` |
| `2026-06-24 05:08:35` | `cowrie.command.input` |
| `2026-06-24 05:08:35` | `cowrie.command.input` |
| `2026-06-24 05:08:35` | `cowrie.command.failed` |
| `2026-06-24 05:08:35` | `cowrie.command.input` |
| `2026-06-24 05:08:35` | `cowrie.command.input` |
| `2026-06-24 05:08:35` | `cowrie.command.input` |
| `2026-06-24 05:08:35` | `cowrie.log.closed` |
| `2026-06-24 05:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ed14e392c9d

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:31` | `cowrie.session.connect` |
| `2026-06-24 05:08:32` | `cowrie.client.version` |
| `2026-06-24 05:08:33` | `cowrie.client.kex` |
| `2026-06-24 05:08:35` | `cowrie.login.success` |
| `2026-06-24 05:08:36` | `cowrie.session.params` |
| `2026-06-24 05:08:36` | `cowrie.command.input` |
| `2026-06-24 05:08:36` | `cowrie.command.failed` |
| `2026-06-24 05:08:36` | `cowrie.log.closed` |
| `2026-06-24 05:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa112c64942

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:33` | `cowrie.session.connect` |
| `2026-06-24 05:08:34` | `cowrie.client.version` |
| `2026-06-24 05:08:34` | `cowrie.client.kex` |
| `2026-06-24 05:08:35` | `cowrie.login.success` |
| `2026-06-24 05:08:36` | `cowrie.session.params` |
| `2026-06-24 05:08:36` | `cowrie.command.input` |
| `2026-06-24 05:08:36` | `cowrie.command.failed` |
| `2026-06-24 05:08:36` | `cowrie.log.closed` |
| `2026-06-24 05:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23a658552ae

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:34` | `cowrie.session.connect` |
| `2026-06-24 05:08:34` | `cowrie.login.success` |
| `2026-06-24 05:08:35` | `cowrie.session.params` |
| `2026-06-24 05:08:36` | `cowrie.command.input` |
| `2026-06-24 05:08:36` | `cowrie.command.input` |
| `2026-06-24 05:08:36` | `cowrie.command.failed` |
| `2026-06-24 05:08:36` | `cowrie.command.input` |
| `2026-06-24 05:08:36` | `cowrie.command.input` |
| `2026-06-24 05:08:36` | `cowrie.command.input` |
| `2026-06-24 05:08:36` | `cowrie.log.closed` |
| `2026-06-24 05:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261565a0fb19

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:34` | `cowrie.session.connect` |
| `2026-06-24 05:08:34` | `cowrie.client.version` |
| `2026-06-24 05:08:35` | `cowrie.client.kex` |
| `2026-06-24 05:08:36` | `cowrie.login.success` |
| `2026-06-24 05:08:37` | `cowrie.session.params` |
| `2026-06-24 05:08:37` | `cowrie.command.input` |
| `2026-06-24 05:08:37` | `cowrie.command.failed` |
| `2026-06-24 05:08:39` | `cowrie.log.closed` |
| `2026-06-24 05:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340f44e0db99

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:35` | `cowrie.session.connect` |
| `2026-06-24 05:08:35` | `cowrie.client.version` |
| `2026-06-24 05:08:35` | `cowrie.client.kex` |
| `2026-06-24 05:08:36` | `cowrie.login.success` |
| `2026-06-24 05:08:39` | `cowrie.session.params` |
| `2026-06-24 05:08:39` | `cowrie.command.input` |
| `2026-06-24 05:08:39` | `cowrie.command.failed` |
| `2026-06-24 05:08:39` | `cowrie.log.closed` |
| `2026-06-24 05:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612caf4f638a

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:36` | `cowrie.session.connect` |
| `2026-06-24 05:08:36` | `cowrie.client.version` |
| `2026-06-24 05:08:36` | `cowrie.client.kex` |
| `2026-06-24 05:08:39` | `cowrie.login.success` |
| `2026-06-24 05:08:40` | `cowrie.session.params` |
| `2026-06-24 05:08:40` | `cowrie.command.input` |
| `2026-06-24 05:08:40` | `cowrie.command.failed` |
| `2026-06-24 05:08:42` | `cowrie.log.closed` |
| `2026-06-24 05:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c22fa47f12

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:36` | `cowrie.session.connect` |
| `2026-06-24 05:08:37` | `cowrie.login.success` |
| `2026-06-24 05:08:38` | `cowrie.session.params` |
| `2026-06-24 05:08:39` | `cowrie.command.input` |
| `2026-06-24 05:08:39` | `cowrie.command.input` |
| `2026-06-24 05:08:39` | `cowrie.command.failed` |
| `2026-06-24 05:08:39` | `cowrie.command.input` |
| `2026-06-24 05:08:39` | `cowrie.command.input` |
| `2026-06-24 05:08:39` | `cowrie.command.input` |
| `2026-06-24 05:08:41` | `cowrie.log.closed` |
| `2026-06-24 05:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e719d465f40

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:36` | `cowrie.session.connect` |
| `2026-06-24 05:08:36` | `cowrie.client.version` |
| `2026-06-24 05:08:38` | `cowrie.client.kex` |
| `2026-06-24 05:08:39` | `cowrie.login.success` |
| `2026-06-24 05:08:42` | `cowrie.session.params` |
| `2026-06-24 05:08:42` | `cowrie.command.input` |
| `2026-06-24 05:08:42` | `cowrie.command.failed` |
| `2026-06-24 05:08:42` | `cowrie.log.closed` |
| `2026-06-24 05:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd50274c7d2

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:36` | `cowrie.session.connect` |
| `2026-06-24 05:08:39` | `cowrie.login.success` |
| `2026-06-24 05:08:39` | `cowrie.session.params` |
| `2026-06-24 05:08:41` | `cowrie.command.input` |
| `2026-06-24 05:08:41` | `cowrie.command.input` |
| `2026-06-24 05:08:41` | `cowrie.command.failed` |
| `2026-06-24 05:08:41` | `cowrie.command.input` |
| `2026-06-24 05:08:41` | `cowrie.command.input` |
| `2026-06-24 05:08:41` | `cowrie.command.input` |
| `2026-06-24 05:08:42` | `cowrie.log.closed` |
| `2026-06-24 05:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cd82dbab1f8

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:39` | `cowrie.session.connect` |
| `2026-06-24 05:08:40` | `cowrie.login.success` |
| `2026-06-24 05:08:41` | `cowrie.session.params` |
| `2026-06-24 05:08:42` | `cowrie.command.input` |
| `2026-06-24 05:08:42` | `cowrie.command.input` |
| `2026-06-24 05:08:42` | `cowrie.command.failed` |
| `2026-06-24 05:08:42` | `cowrie.command.input` |
| `2026-06-24 05:08:42` | `cowrie.command.input` |
| `2026-06-24 05:08:42` | `cowrie.command.input` |
| `2026-06-24 05:08:43` | `cowrie.log.closed` |
| `2026-06-24 05:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58fcd90e69e3

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:39` | `cowrie.session.connect` |
| `2026-06-24 05:08:41` | `cowrie.login.success` |
| `2026-06-24 05:08:42` | `cowrie.session.params` |
| `2026-06-24 05:08:43` | `cowrie.command.input` |
| `2026-06-24 05:08:43` | `cowrie.command.input` |
| `2026-06-24 05:08:43` | `cowrie.command.failed` |
| `2026-06-24 05:08:43` | `cowrie.command.input` |
| `2026-06-24 05:08:43` | `cowrie.command.input` |
| `2026-06-24 05:08:43` | `cowrie.command.input` |
| `2026-06-24 05:08:45` | `cowrie.log.closed` |
| `2026-06-24 05:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a52c551b8f

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:41` | `cowrie.session.connect` |
| `2026-06-24 05:08:42` | `cowrie.client.version` |
| `2026-06-24 05:08:42` | `cowrie.client.kex` |
| `2026-06-24 05:08:43` | `cowrie.login.success` |
| `2026-06-24 05:08:45` | `cowrie.session.params` |
| `2026-06-24 05:08:45` | `cowrie.command.input` |
| `2026-06-24 05:08:45` | `cowrie.command.failed` |
| `2026-06-24 05:08:45` | `cowrie.log.closed` |
| `2026-06-24 05:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411dddef6813

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:42` | `cowrie.session.connect` |
| `2026-06-24 05:08:42` | `cowrie.login.success` |
| `2026-06-24 05:08:43` | `cowrie.session.params` |
| `2026-06-24 05:08:44` | `cowrie.command.input` |
| `2026-06-24 05:08:44` | `cowrie.command.input` |
| `2026-06-24 05:08:44` | `cowrie.command.failed` |
| `2026-06-24 05:08:44` | `cowrie.command.input` |
| `2026-06-24 05:08:44` | `cowrie.command.input` |
| `2026-06-24 05:08:44` | `cowrie.command.input` |
| `2026-06-24 05:08:45` | `cowrie.log.closed` |
| `2026-06-24 05:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3749752b64c2

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:42` | `cowrie.session.connect` |
| `2026-06-24 05:08:42` | `cowrie.client.version` |
| `2026-06-24 05:08:42` | `cowrie.client.kex` |
| `2026-06-24 05:08:45` | `cowrie.login.success` |
| `2026-06-24 05:08:46` | `cowrie.session.params` |
| `2026-06-24 05:08:46` | `cowrie.command.input` |
| `2026-06-24 05:08:46` | `cowrie.command.failed` |
| `2026-06-24 05:08:46` | `cowrie.log.closed` |
| `2026-06-24 05:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08162882809d

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:43` | `cowrie.session.connect` |
| `2026-06-24 05:08:43` | `cowrie.login.success` |
| `2026-06-24 05:08:44` | `cowrie.session.params` |
| `2026-06-24 05:08:45` | `cowrie.command.input` |
| `2026-06-24 05:08:45` | `cowrie.command.input` |
| `2026-06-24 05:08:45` | `cowrie.command.failed` |
| `2026-06-24 05:08:45` | `cowrie.command.input` |
| `2026-06-24 05:08:45` | `cowrie.command.input` |
| `2026-06-24 05:08:45` | `cowrie.command.input` |
| `2026-06-24 05:08:46` | `cowrie.log.closed` |
| `2026-06-24 05:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7dd97329975

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:43` | `cowrie.session.connect` |
| `2026-06-24 05:08:43` | `cowrie.client.version` |
| `2026-06-24 05:08:43` | `cowrie.client.kex` |
| `2026-06-24 05:08:45` | `cowrie.login.success` |
| `2026-06-24 05:08:46` | `cowrie.session.params` |
| `2026-06-24 05:08:46` | `cowrie.command.input` |
| `2026-06-24 05:08:46` | `cowrie.command.failed` |
| `2026-06-24 05:08:47` | `cowrie.log.closed` |
| `2026-06-24 05:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c512bde58a

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:45` | `cowrie.session.connect` |
| `2026-06-24 05:08:45` | `cowrie.client.version` |
| `2026-06-24 05:08:45` | `cowrie.client.kex` |
| `2026-06-24 05:08:46` | `cowrie.login.success` |
| `2026-06-24 05:08:47` | `cowrie.session.params` |
| `2026-06-24 05:08:47` | `cowrie.command.input` |
| `2026-06-24 05:08:47` | `cowrie.command.failed` |
| `2026-06-24 05:08:49` | `cowrie.log.closed` |
| `2026-06-24 05:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a3c48f904a

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:45` | `cowrie.session.connect` |
| `2026-06-24 05:08:45` | `cowrie.client.version` |
| `2026-06-24 05:08:46` | `cowrie.client.kex` |
| `2026-06-24 05:08:47` | `cowrie.login.success` |
| `2026-06-24 05:08:51` | `cowrie.session.params` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.failed` |
| `2026-06-24 05:08:51` | `cowrie.log.closed` |
| `2026-06-24 05:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f6e8802923

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:45` | `cowrie.session.connect` |
| `2026-06-24 05:08:46` | `cowrie.login.success` |
| `2026-06-24 05:08:47` | `cowrie.session.params` |
| `2026-06-24 05:08:49` | `cowrie.command.input` |
| `2026-06-24 05:08:49` | `cowrie.command.input` |
| `2026-06-24 05:08:49` | `cowrie.command.failed` |
| `2026-06-24 05:08:49` | `cowrie.command.input` |
| `2026-06-24 05:08:49` | `cowrie.command.input` |
| `2026-06-24 05:08:49` | `cowrie.command.input` |
| `2026-06-24 05:08:49` | `cowrie.log.closed` |
| `2026-06-24 05:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a35e4f6d90cf

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:46` | `cowrie.session.connect` |
| `2026-06-24 05:08:46` | `cowrie.client.version` |
| `2026-06-24 05:08:47` | `cowrie.client.kex` |
| `2026-06-24 05:08:49` | `cowrie.login.success` |
| `2026-06-24 05:08:50` | `cowrie.session.params` |
| `2026-06-24 05:08:50` | `cowrie.command.input` |
| `2026-06-24 05:08:50` | `cowrie.command.failed` |
| `2026-06-24 05:08:51` | `cowrie.log.closed` |
| `2026-06-24 05:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eadb711050bb

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:46` | `cowrie.session.connect` |
| `2026-06-24 05:08:47` | `cowrie.login.success` |
| `2026-06-24 05:08:49` | `cowrie.session.params` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.failed` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.log.closed` |
| `2026-06-24 05:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92abec7dd1b5

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:47` | `cowrie.session.connect` |
| `2026-06-24 05:08:49` | `cowrie.login.success` |
| `2026-06-24 05:08:49` | `cowrie.session.params` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.failed` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.log.closed` |
| `2026-06-24 05:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f92c9221a96

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:49` | `cowrie.session.connect` |
| `2026-06-24 05:08:50` | `cowrie.login.success` |
| `2026-06-24 05:08:51` | `cowrie.session.params` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.failed` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:51` | `cowrie.command.input` |
| `2026-06-24 05:08:52` | `cowrie.log.closed` |
| `2026-06-24 05:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5039869c813d

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:51` | `cowrie.session.connect` |
| `2026-06-24 05:08:51` | `cowrie.client.version` |
| `2026-06-24 05:08:51` | `cowrie.client.kex` |
| `2026-06-24 05:08:53` | `cowrie.login.success` |
| `2026-06-24 05:08:54` | `cowrie.session.params` |
| `2026-06-24 05:08:54` | `cowrie.command.input` |
| `2026-06-24 05:08:54` | `cowrie.command.failed` |
| `2026-06-24 05:08:55` | `cowrie.log.closed` |
| `2026-06-24 05:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3f3ff8d44b

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:51` | `cowrie.session.connect` |
| `2026-06-24 05:08:51` | `cowrie.login.success` |
| `2026-06-24 05:08:52` | `cowrie.session.params` |
| `2026-06-24 05:08:53` | `cowrie.command.input` |
| `2026-06-24 05:08:53` | `cowrie.command.input` |
| `2026-06-24 05:08:53` | `cowrie.command.failed` |
| `2026-06-24 05:08:53` | `cowrie.command.input` |
| `2026-06-24 05:08:53` | `cowrie.command.input` |
| `2026-06-24 05:08:53` | `cowrie.command.input` |
| `2026-06-24 05:08:53` | `cowrie.log.closed` |
| `2026-06-24 05:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d20dac3a77

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:51` | `cowrie.session.connect` |
| `2026-06-24 05:08:51` | `cowrie.client.version` |
| `2026-06-24 05:08:52` | `cowrie.client.kex` |
| `2026-06-24 05:08:53` | `cowrie.login.success` |
| `2026-06-24 05:08:55` | `cowrie.session.params` |
| `2026-06-24 05:08:55` | `cowrie.command.input` |
| `2026-06-24 05:08:55` | `cowrie.command.failed` |
| `2026-06-24 05:08:55` | `cowrie.log.closed` |
| `2026-06-24 05:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd1e7119779

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:51` | `cowrie.session.connect` |
| `2026-06-24 05:08:52` | `cowrie.login.success` |
| `2026-06-24 05:08:53` | `cowrie.session.params` |
| `2026-06-24 05:08:54` | `cowrie.command.input` |
| `2026-06-24 05:08:54` | `cowrie.command.input` |
| `2026-06-24 05:08:54` | `cowrie.command.failed` |
| `2026-06-24 05:08:54` | `cowrie.command.input` |
| `2026-06-24 05:08:54` | `cowrie.command.input` |
| `2026-06-24 05:08:54` | `cowrie.command.input` |
| `2026-06-24 05:08:55` | `cowrie.log.closed` |
| `2026-06-24 05:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2f846a4efe

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:52` | `cowrie.session.connect` |
| `2026-06-24 05:08:52` | `cowrie.client.version` |
| `2026-06-24 05:08:52` | `cowrie.client.kex` |
| `2026-06-24 05:08:55` | `cowrie.login.success` |
| `2026-06-24 05:08:55` | `cowrie.session.params` |
| `2026-06-24 05:08:55` | `cowrie.command.input` |
| `2026-06-24 05:08:55` | `cowrie.command.failed` |
| `2026-06-24 05:08:56` | `cowrie.log.closed` |
| `2026-06-24 05:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13f2ab293bff

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id || uname -a || show version || echo 'AUTH_OK'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:52` | `cowrie.session.connect` |
| `2026-06-24 05:08:52` | `cowrie.client.version` |
| `2026-06-24 05:08:52` | `cowrie.client.kex` |
| `2026-06-24 05:08:55` | `cowrie.login.success` |
| `2026-06-24 05:08:56` | `cowrie.session.params` |
| `2026-06-24 05:08:56` | `cowrie.command.input` |
| `2026-06-24 05:08:56` | `cowrie.command.failed` |
| `2026-06-24 05:08:56` | `cowrie.log.closed` |
| `2026-06-24 05:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64cc3c87797

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:55` | `cowrie.session.connect` |
| `2026-06-24 05:08:56` | `cowrie.login.success` |
| `2026-06-24 05:08:56` | `cowrie.session.params` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.failed` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.log.closed` |
| `2026-06-24 05:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08346d063fa9

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:56` | `cowrie.session.connect` |
| `2026-06-24 05:08:57` | `cowrie.login.success` |
| `2026-06-24 05:08:59` | `cowrie.session.params` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.failed` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:09:00` | `cowrie.log.closed` |
| `2026-06-24 05:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-084c0a7b6608

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:56` | `cowrie.session.connect` |
| `2026-06-24 05:08:57` | `cowrie.login.success` |
| `2026-06-24 05:08:57` | `cowrie.session.params` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.failed` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.command.input` |
| `2026-06-24 05:08:59` | `cowrie.log.closed` |
| `2026-06-24 05:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f55634a3d500

| Field | Detail |
|---|---|
| **Source IP** | `194.26.101[.]146` |
| **First Seen** | 2026-06-24 05:08 |
| **Last Seen** | 2026-06-24 05:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `show version, id, uname -a` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:08:57` | `cowrie.session.connect` |
| `2026-06-24 05:08:59` | `cowrie.login.success` |
| `2026-06-24 05:08:59` | `cowrie.session.params` |
| `2026-06-24 05:09:00` | `cowrie.command.input` |
| `2026-06-24 05:09:00` | `cowrie.command.input` |
| `2026-06-24 05:09:00` | `cowrie.command.failed` |
| `2026-06-24 05:09:00` | `cowrie.command.input` |
| `2026-06-24 05:09:00` | `cowrie.command.input` |
| `2026-06-24 05:09:00` | `cowrie.command.input` |
| `2026-06-24 05:09:00` | `cowrie.log.closed` |
| `2026-06-24 05:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.26.101[.]146` to AbuseIPDB if not already reported
- [ ] Block `194.26.101[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6b1d15a426

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:09 |
| **Last Seen** | 2026-06-24 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:09:09` | `cowrie.session.connect` |
| `2026-06-24 05:09:09` | `cowrie.client.version` |
| `2026-06-24 05:09:09` | `cowrie.client.kex` |
| `2026-06-24 05:09:09` | `cowrie.login.success` |
| `2026-06-24 05:09:10` | `cowrie.session.params` |
| `2026-06-24 05:09:10` | `cowrie.command.input` |
| `2026-06-24 05:09:10` | `cowrie.log.closed` |
| `2026-06-24 05:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42449652410

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:09 |
| **Last Seen** | 2026-06-24 05:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'debian123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:09:55` | `cowrie.session.connect` |
| `2026-06-24 05:09:56` | `cowrie.client.version` |
| `2026-06-24 05:09:56` | `cowrie.client.kex` |
| `2026-06-24 05:10:00` | `cowrie.login.success` |
| `2026-06-24 05:10:02` | `cowrie.session.params` |
| `2026-06-24 05:10:02` | `cowrie.command.input` |
| `2026-06-24 05:10:02` | `cowrie.command.input` |
| `2026-06-24 05:10:02` | `cowrie.command.input` |
| `2026-06-24 05:10:02` | `cowrie.command.input` |
| `2026-06-24 05:10:03` | `cowrie.log.closed` |
| `2026-06-24 05:10:07` | `cowrie.session.params` |
| `2026-06-24 05:10:07` | `cowrie.command.input` |
| `2026-06-24 05:10:07` | `cowrie.command.input` |
| `2026-06-24 05:10:07` | `cowrie.command.failed` |
| `2026-06-24 05:10:07` | `cowrie.command.failed` |
| `2026-06-24 05:10:07` | `cowrie.command.failed` |
| `2026-06-24 05:10:07` | `cowrie.command.failed` |
| `2026-06-24 05:10:08` | `cowrie.log.closed` |
| `2026-06-24 05:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0fac6d409ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:10 |
| **Last Seen** | 2026-06-24 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:10:02` | `cowrie.session.connect` |
| `2026-06-24 05:10:02` | `cowrie.client.version` |
| `2026-06-24 05:10:02` | `cowrie.client.kex` |
| `2026-06-24 05:10:03` | `cowrie.login.success` |
| `2026-06-24 05:10:03` | `cowrie.session.params` |
| `2026-06-24 05:10:03` | `cowrie.command.input` |
| `2026-06-24 05:10:03` | `cowrie.log.closed` |
| `2026-06-24 05:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1989805df34f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 05:10 |
| **Last Seen** | 2026-06-24 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:10:08` | `cowrie.session.connect` |
| `2026-06-24 05:10:08` | `cowrie.client.version` |
| `2026-06-24 05:10:08` | `cowrie.client.kex` |
| `2026-06-24 05:10:08` | `cowrie.login.success` |
| `2026-06-24 05:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96410c4ae06

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 05:10 |
| **Last Seen** | 2026-06-24 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:10:09` | `cowrie.session.connect` |
| `2026-06-24 05:10:09` | `cowrie.client.version` |
| `2026-06-24 05:10:09` | `cowrie.client.kex` |
| `2026-06-24 05:10:09` | `cowrie.login.success` |
| `2026-06-24 05:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee01feed2a5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 05:10 |
| **Last Seen** | 2026-06-24 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:10:15` | `cowrie.session.connect` |
| `2026-06-24 05:10:15` | `cowrie.client.version` |
| `2026-06-24 05:10:15` | `cowrie.client.kex` |
| `2026-06-24 05:10:15` | `cowrie.login.success` |
| `2026-06-24 05:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eacfb56aec5c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 05:10 |
| **Last Seen** | 2026-06-24 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:10:15` | `cowrie.session.connect` |
| `2026-06-24 05:10:15` | `cowrie.client.version` |
| `2026-06-24 05:10:15` | `cowrie.client.kex` |
| `2026-06-24 05:10:15` | `cowrie.login.success` |
| `2026-06-24 05:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc3e69ca15d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:10 |
| **Last Seen** | 2026-06-24 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:10:53` | `cowrie.session.connect` |
| `2026-06-24 05:10:53` | `cowrie.client.version` |
| `2026-06-24 05:10:53` | `cowrie.client.kex` |
| `2026-06-24 05:10:54` | `cowrie.login.success` |
| `2026-06-24 05:10:54` | `cowrie.session.params` |
| `2026-06-24 05:10:54` | `cowrie.command.input` |
| `2026-06-24 05:10:54` | `cowrie.log.closed` |
| `2026-06-24 05:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48645bd528d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:11 |
| **Last Seen** | 2026-06-24 05:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:11:46` | `cowrie.session.connect` |
| `2026-06-24 05:11:46` | `cowrie.client.version` |
| `2026-06-24 05:11:46` | `cowrie.client.kex` |
| `2026-06-24 05:11:46` | `cowrie.login.success` |
| `2026-06-24 05:11:47` | `cowrie.session.params` |
| `2026-06-24 05:11:47` | `cowrie.command.input` |
| `2026-06-24 05:11:47` | `cowrie.log.closed` |
| `2026-06-24 05:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4767f9bd0fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:12 |
| **Last Seen** | 2026-06-24 05:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:12:40` | `cowrie.session.connect` |
| `2026-06-24 05:12:40` | `cowrie.client.version` |
| `2026-06-24 05:12:40` | `cowrie.client.kex` |
| `2026-06-24 05:12:40` | `cowrie.login.success` |
| `2026-06-24 05:12:42` | `cowrie.session.params` |
| `2026-06-24 05:12:42` | `cowrie.command.input` |
| `2026-06-24 05:12:42` | `cowrie.log.closed` |
| `2026-06-24 05:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5af9cb56a1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 05:13 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:13:30` | `cowrie.session.connect` |
| `2026-06-24 05:13:32` | `cowrie.client.version` |
| `2026-06-24 05:13:32` | `cowrie.client.kex` |
| `2026-06-24 05:13:39` | `cowrie.login.success` |
| `2026-06-24 05:13:43` | `cowrie.session.params` |
| `2026-06-24 05:13:43` | `cowrie.command.input` |
| `2026-06-24 05:13:44` | `cowrie.log.closed` |
| `2026-06-24 05:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17f425e906c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:13 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:13:35` | `cowrie.session.connect` |
| `2026-06-24 05:13:35` | `cowrie.client.version` |
| `2026-06-24 05:13:35` | `cowrie.client.kex` |
| `2026-06-24 05:13:36` | `cowrie.login.success` |
| `2026-06-24 05:13:36` | `cowrie.session.params` |
| `2026-06-24 05:13:36` | `cowrie.command.input` |
| `2026-06-24 05:13:37` | `cowrie.log.closed` |
| `2026-06-24 05:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c46a089ae63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:13 |
| **Last Seen** | 2026-06-24 05:14 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'debian2026' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:13:45` | `cowrie.session.connect` |
| `2026-06-24 05:13:46` | `cowrie.client.version` |
| `2026-06-24 05:13:46` | `cowrie.client.kex` |
| `2026-06-24 05:13:51` | `cowrie.login.success` |
| `2026-06-24 05:13:53` | `cowrie.session.params` |
| `2026-06-24 05:13:53` | `cowrie.command.input` |
| `2026-06-24 05:13:53` | `cowrie.command.input` |
| `2026-06-24 05:13:53` | `cowrie.command.input` |
| `2026-06-24 05:13:53` | `cowrie.command.input` |
| `2026-06-24 05:13:55` | `cowrie.log.closed` |
| `2026-06-24 05:14:00` | `cowrie.session.params` |
| `2026-06-24 05:14:00` | `cowrie.command.input` |
| `2026-06-24 05:14:00` | `cowrie.command.input` |
| `2026-06-24 05:14:00` | `cowrie.command.failed` |
| `2026-06-24 05:14:00` | `cowrie.command.failed` |
| `2026-06-24 05:14:00` | `cowrie.command.failed` |
| `2026-06-24 05:14:00` | `cowrie.command.failed` |
| `2026-06-24 05:14:02` | `cowrie.log.closed` |
| `2026-06-24 05:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0635ae6dc8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 05:13 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:13:54` | `cowrie.session.connect` |
| `2026-06-24 05:13:54` | `cowrie.client.version` |
| `2026-06-24 05:13:54` | `cowrie.client.kex` |
| `2026-06-24 05:13:55` | `cowrie.login.success` |
| `2026-06-24 05:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f5b41025466

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 05:13 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:13:54` | `cowrie.session.connect` |
| `2026-06-24 05:13:54` | `cowrie.client.version` |
| `2026-06-24 05:13:55` | `cowrie.client.kex` |
| `2026-06-24 05:13:55` | `cowrie.login.success` |
| `2026-06-24 05:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980ba979c1ed

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 05:13 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:13:55` | `cowrie.session.connect` |
| `2026-06-24 05:13:55` | `cowrie.client.version` |
| `2026-06-24 05:13:56` | `cowrie.client.kex` |
| `2026-06-24 05:13:56` | `cowrie.login.success` |
| `2026-06-24 05:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200c2be4b15e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 05:13 |
| **Last Seen** | 2026-06-24 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:13:56` | `cowrie.session.connect` |
| `2026-06-24 05:13:56` | `cowrie.client.version` |
| `2026-06-24 05:13:56` | `cowrie.client.kex` |
| `2026-06-24 05:13:57` | `cowrie.login.success` |
| `2026-06-24 05:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5442454810f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:14 |
| **Last Seen** | 2026-06-24 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:14:34` | `cowrie.session.connect` |
| `2026-06-24 05:14:34` | `cowrie.client.version` |
| `2026-06-24 05:14:34` | `cowrie.client.kex` |
| `2026-06-24 05:14:35` | `cowrie.login.success` |
| `2026-06-24 05:14:35` | `cowrie.session.params` |
| `2026-06-24 05:14:35` | `cowrie.command.input` |
| `2026-06-24 05:14:35` | `cowrie.log.closed` |
| `2026-06-24 05:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86673c4191a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:15 |
| **Last Seen** | 2026-06-24 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:15:30` | `cowrie.session.connect` |
| `2026-06-24 05:15:30` | `cowrie.client.version` |
| `2026-06-24 05:15:30` | `cowrie.client.kex` |
| `2026-06-24 05:15:30` | `cowrie.login.success` |
| `2026-06-24 05:15:31` | `cowrie.session.params` |
| `2026-06-24 05:15:31` | `cowrie.command.input` |
| `2026-06-24 05:15:31` | `cowrie.log.closed` |
| `2026-06-24 05:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3fa8ea77c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:16 |
| **Last Seen** | 2026-06-24 05:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:16:23` | `cowrie.session.connect` |
| `2026-06-24 05:16:23` | `cowrie.client.version` |
| `2026-06-24 05:16:23` | `cowrie.client.kex` |
| `2026-06-24 05:16:23` | `cowrie.login.success` |
| `2026-06-24 05:16:26` | `cowrie.session.params` |
| `2026-06-24 05:16:26` | `cowrie.command.input` |
| `2026-06-24 05:16:26` | `cowrie.log.closed` |
| `2026-06-24 05:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd78be7c01d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:17 |
| **Last Seen** | 2026-06-24 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:17:16` | `cowrie.session.connect` |
| `2026-06-24 05:17:16` | `cowrie.client.version` |
| `2026-06-24 05:17:16` | `cowrie.client.kex` |
| `2026-06-24 05:17:16` | `cowrie.login.success` |
| `2026-06-24 05:17:17` | `cowrie.session.params` |
| `2026-06-24 05:17:17` | `cowrie.command.input` |
| `2026-06-24 05:17:17` | `cowrie.log.closed` |
| `2026-06-24 05:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec2f7ab0767

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:17 |
| **Last Seen** | 2026-06-24 05:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'letmein' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:17:29` | `cowrie.session.connect` |
| `2026-06-24 05:17:30` | `cowrie.client.version` |
| `2026-06-24 05:17:30` | `cowrie.client.kex` |
| `2026-06-24 05:17:34` | `cowrie.login.success` |
| `2026-06-24 05:17:36` | `cowrie.session.params` |
| `2026-06-24 05:17:36` | `cowrie.command.input` |
| `2026-06-24 05:17:36` | `cowrie.command.input` |
| `2026-06-24 05:17:36` | `cowrie.command.input` |
| `2026-06-24 05:17:36` | `cowrie.command.input` |
| `2026-06-24 05:17:37` | `cowrie.log.closed` |
| `2026-06-24 05:17:39` | `cowrie.session.params` |
| `2026-06-24 05:17:39` | `cowrie.command.input` |
| `2026-06-24 05:17:39` | `cowrie.command.input` |
| `2026-06-24 05:17:39` | `cowrie.command.failed` |
| `2026-06-24 05:17:39` | `cowrie.command.failed` |
| `2026-06-24 05:17:39` | `cowrie.command.failed` |
| `2026-06-24 05:17:39` | `cowrie.command.failed` |
| `2026-06-24 05:17:40` | `cowrie.log.closed` |
| `2026-06-24 05:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef2ff0a5fd4d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:18 |
| **Last Seen** | 2026-06-24 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:18:10` | `cowrie.session.connect` |
| `2026-06-24 05:18:10` | `cowrie.client.version` |
| `2026-06-24 05:18:10` | `cowrie.client.kex` |
| `2026-06-24 05:18:10` | `cowrie.login.success` |
| `2026-06-24 05:18:11` | `cowrie.session.params` |
| `2026-06-24 05:18:11` | `cowrie.command.input` |
| `2026-06-24 05:18:11` | `cowrie.log.closed` |
| `2026-06-24 05:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81b7f4664a98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:19 |
| **Last Seen** | 2026-06-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:19:05` | `cowrie.session.connect` |
| `2026-06-24 05:19:05` | `cowrie.client.version` |
| `2026-06-24 05:19:05` | `cowrie.client.kex` |
| `2026-06-24 05:19:05` | `cowrie.login.success` |
| `2026-06-24 05:19:06` | `cowrie.session.params` |
| `2026-06-24 05:19:06` | `cowrie.command.input` |
| `2026-06-24 05:19:06` | `cowrie.log.closed` |
| `2026-06-24 05:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb550d20d73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:20 |
| **Last Seen** | 2026-06-24 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:20:01` | `cowrie.session.connect` |
| `2026-06-24 05:20:01` | `cowrie.client.version` |
| `2026-06-24 05:20:01` | `cowrie.client.kex` |
| `2026-06-24 05:20:01` | `cowrie.login.success` |
| `2026-06-24 05:20:02` | `cowrie.session.params` |
| `2026-06-24 05:20:02` | `cowrie.command.input` |
| `2026-06-24 05:20:02` | `cowrie.log.closed` |
| `2026-06-24 05:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe635a216f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:21 |
| **Last Seen** | 2026-06-24 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:21:02` | `cowrie.session.connect` |
| `2026-06-24 05:21:02` | `cowrie.client.version` |
| `2026-06-24 05:21:02` | `cowrie.client.kex` |
| `2026-06-24 05:21:02` | `cowrie.login.success` |
| `2026-06-24 05:21:03` | `cowrie.session.params` |
| `2026-06-24 05:21:03` | `cowrie.command.input` |
| `2026-06-24 05:21:03` | `cowrie.log.closed` |
| `2026-06-24 05:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0b78eaa300

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:21 |
| **Last Seen** | 2026-06-24 05:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'pa55word' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:21:23` | `cowrie.session.connect` |
| `2026-06-24 05:21:24` | `cowrie.client.version` |
| `2026-06-24 05:21:24` | `cowrie.client.kex` |
| `2026-06-24 05:21:29` | `cowrie.login.success` |
| `2026-06-24 05:21:32` | `cowrie.session.params` |
| `2026-06-24 05:21:32` | `cowrie.command.input` |
| `2026-06-24 05:21:32` | `cowrie.command.input` |
| `2026-06-24 05:21:32` | `cowrie.command.input` |
| `2026-06-24 05:21:32` | `cowrie.command.input` |
| `2026-06-24 05:21:33` | `cowrie.log.closed` |
| `2026-06-24 05:21:36` | `cowrie.session.params` |
| `2026-06-24 05:21:36` | `cowrie.command.input` |
| `2026-06-24 05:21:36` | `cowrie.command.input` |
| `2026-06-24 05:21:36` | `cowrie.command.failed` |
| `2026-06-24 05:21:36` | `cowrie.command.failed` |
| `2026-06-24 05:21:36` | `cowrie.command.failed` |
| `2026-06-24 05:21:36` | `cowrie.command.failed` |
| `2026-06-24 05:21:37` | `cowrie.log.closed` |
| `2026-06-24 05:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49561c082105

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:21 |
| **Last Seen** | 2026-06-24 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:21:58` | `cowrie.session.connect` |
| `2026-06-24 05:21:58` | `cowrie.client.version` |
| `2026-06-24 05:21:58` | `cowrie.client.kex` |
| `2026-06-24 05:21:58` | `cowrie.login.success` |
| `2026-06-24 05:21:59` | `cowrie.session.params` |
| `2026-06-24 05:21:59` | `cowrie.command.input` |
| `2026-06-24 05:21:59` | `cowrie.log.closed` |
| `2026-06-24 05:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e163b1c1a3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:22 |
| **Last Seen** | 2026-06-24 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:22:59` | `cowrie.session.connect` |
| `2026-06-24 05:22:59` | `cowrie.client.version` |
| `2026-06-24 05:22:59` | `cowrie.client.kex` |
| `2026-06-24 05:22:59` | `cowrie.login.success` |
| `2026-06-24 05:23:00` | `cowrie.session.params` |
| `2026-06-24 05:23:00` | `cowrie.command.input` |
| `2026-06-24 05:23:00` | `cowrie.log.closed` |
| `2026-06-24 05:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6e40e404bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:23 |
| **Last Seen** | 2026-06-24 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:23:53` | `cowrie.session.connect` |
| `2026-06-24 05:23:53` | `cowrie.client.version` |
| `2026-06-24 05:23:53` | `cowrie.client.kex` |
| `2026-06-24 05:23:53` | `cowrie.login.success` |
| `2026-06-24 05:23:54` | `cowrie.session.params` |
| `2026-06-24 05:23:54` | `cowrie.command.input` |
| `2026-06-24 05:23:54` | `cowrie.log.closed` |
| `2026-06-24 05:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d64dd0eb673

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:24 |
| **Last Seen** | 2026-06-24 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:24:48` | `cowrie.session.connect` |
| `2026-06-24 05:24:48` | `cowrie.client.version` |
| `2026-06-24 05:24:48` | `cowrie.client.kex` |
| `2026-06-24 05:24:48` | `cowrie.login.success` |
| `2026-06-24 05:24:49` | `cowrie.session.params` |
| `2026-06-24 05:24:49` | `cowrie.command.input` |
| `2026-06-24 05:24:49` | `cowrie.log.closed` |
| `2026-06-24 05:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fbef3445da2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:25 |
| **Last Seen** | 2026-06-24 05:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:25:12` | `cowrie.session.connect` |
| `2026-06-24 05:25:14` | `cowrie.client.version` |
| `2026-06-24 05:25:14` | `cowrie.client.kex` |
| `2026-06-24 05:25:19` | `cowrie.login.success` |
| `2026-06-24 05:25:22` | `cowrie.session.params` |
| `2026-06-24 05:25:22` | `cowrie.command.input` |
| `2026-06-24 05:25:22` | `cowrie.command.input` |
| `2026-06-24 05:25:22` | `cowrie.command.input` |
| `2026-06-24 05:25:22` | `cowrie.command.input` |
| `2026-06-24 05:25:23` | `cowrie.log.closed` |
| `2026-06-24 05:25:26` | `cowrie.session.params` |
| `2026-06-24 05:25:26` | `cowrie.command.input` |
| `2026-06-24 05:25:26` | `cowrie.command.input` |
| `2026-06-24 05:25:26` | `cowrie.command.failed` |
| `2026-06-24 05:25:26` | `cowrie.command.failed` |
| `2026-06-24 05:25:26` | `cowrie.command.failed` |
| `2026-06-24 05:25:26` | `cowrie.command.failed` |
| `2026-06-24 05:25:27` | `cowrie.log.closed` |
| `2026-06-24 05:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb553ce7567

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:25 |
| **Last Seen** | 2026-06-24 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:25:43` | `cowrie.session.connect` |
| `2026-06-24 05:25:43` | `cowrie.client.version` |
| `2026-06-24 05:25:43` | `cowrie.client.kex` |
| `2026-06-24 05:25:43` | `cowrie.login.success` |
| `2026-06-24 05:25:44` | `cowrie.session.params` |
| `2026-06-24 05:25:44` | `cowrie.command.input` |
| `2026-06-24 05:25:44` | `cowrie.log.closed` |
| `2026-06-24 05:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042485aceaea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:26 |
| **Last Seen** | 2026-06-24 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:26:44` | `cowrie.session.connect` |
| `2026-06-24 05:26:44` | `cowrie.client.version` |
| `2026-06-24 05:26:44` | `cowrie.client.kex` |
| `2026-06-24 05:26:44` | `cowrie.login.success` |
| `2026-06-24 05:26:45` | `cowrie.session.params` |
| `2026-06-24 05:26:45` | `cowrie.command.input` |
| `2026-06-24 05:26:45` | `cowrie.log.closed` |
| `2026-06-24 05:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9af6799a01f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:27 |
| **Last Seen** | 2026-06-24 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:27:43` | `cowrie.session.connect` |
| `2026-06-24 05:27:43` | `cowrie.client.version` |
| `2026-06-24 05:27:43` | `cowrie.client.kex` |
| `2026-06-24 05:27:43` | `cowrie.login.success` |
| `2026-06-24 05:27:44` | `cowrie.session.params` |
| `2026-06-24 05:27:44` | `cowrie.command.input` |
| `2026-06-24 05:27:44` | `cowrie.log.closed` |
| `2026-06-24 05:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec287bca73e3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 05:28 |
| **Last Seen** | 2026-06-24 05:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:28:18` | `cowrie.session.connect` |
| `2026-06-24 05:28:19` | `cowrie.client.version` |
| `2026-06-24 05:28:19` | `cowrie.client.kex` |
| `2026-06-24 05:28:26` | `cowrie.login.success` |
| `2026-06-24 05:28:30` | `cowrie.session.params` |
| `2026-06-24 05:28:30` | `cowrie.command.input` |
| `2026-06-24 05:28:31` | `cowrie.log.closed` |
| `2026-06-24 05:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fbad5bb78c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:28 |
| **Last Seen** | 2026-06-24 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:28:39` | `cowrie.session.connect` |
| `2026-06-24 05:28:39` | `cowrie.client.version` |
| `2026-06-24 05:28:39` | `cowrie.client.kex` |
| `2026-06-24 05:28:39` | `cowrie.login.success` |
| `2026-06-24 05:28:40` | `cowrie.session.params` |
| `2026-06-24 05:28:40` | `cowrie.command.input` |
| `2026-06-24 05:28:40` | `cowrie.log.closed` |
| `2026-06-24 05:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2799ec1d15aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:28 |
| **Last Seen** | 2026-06-24 05:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:28:58` | `cowrie.session.connect` |
| `2026-06-24 05:28:59` | `cowrie.client.version` |
| `2026-06-24 05:28:59` | `cowrie.client.kex` |
| `2026-06-24 05:29:03` | `cowrie.login.success` |
| `2026-06-24 05:29:07` | `cowrie.session.params` |
| `2026-06-24 05:29:07` | `cowrie.command.input` |
| `2026-06-24 05:29:07` | `cowrie.command.input` |
| `2026-06-24 05:29:07` | `cowrie.command.input` |
| `2026-06-24 05:29:07` | `cowrie.command.input` |
| `2026-06-24 05:29:08` | `cowrie.log.closed` |
| `2026-06-24 05:29:11` | `cowrie.session.params` |
| `2026-06-24 05:29:11` | `cowrie.command.input` |
| `2026-06-24 05:29:11` | `cowrie.command.input` |
| `2026-06-24 05:29:11` | `cowrie.command.failed` |
| `2026-06-24 05:29:11` | `cowrie.command.failed` |
| `2026-06-24 05:29:11` | `cowrie.command.failed` |
| `2026-06-24 05:29:11` | `cowrie.command.failed` |
| `2026-06-24 05:29:12` | `cowrie.log.closed` |
| `2026-06-24 05:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb6e0d8d2d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:29 |
| **Last Seen** | 2026-06-24 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:29:34` | `cowrie.session.connect` |
| `2026-06-24 05:29:34` | `cowrie.client.version` |
| `2026-06-24 05:29:34` | `cowrie.client.kex` |
| `2026-06-24 05:29:34` | `cowrie.login.success` |
| `2026-06-24 05:29:35` | `cowrie.session.params` |
| `2026-06-24 05:29:35` | `cowrie.command.input` |
| `2026-06-24 05:29:35` | `cowrie.log.closed` |
| `2026-06-24 05:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c60aa5e63d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:30 |
| **Last Seen** | 2026-06-24 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:30:28` | `cowrie.session.connect` |
| `2026-06-24 05:30:28` | `cowrie.client.version` |
| `2026-06-24 05:30:29` | `cowrie.client.kex` |
| `2026-06-24 05:30:29` | `cowrie.login.success` |
| `2026-06-24 05:30:30` | `cowrie.session.params` |
| `2026-06-24 05:30:30` | `cowrie.command.input` |
| `2026-06-24 05:30:30` | `cowrie.log.closed` |
| `2026-06-24 05:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745a93fd299e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:31 |
| **Last Seen** | 2026-06-24 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:31:25` | `cowrie.session.connect` |
| `2026-06-24 05:31:25` | `cowrie.client.version` |
| `2026-06-24 05:31:25` | `cowrie.client.kex` |
| `2026-06-24 05:31:26` | `cowrie.login.success` |
| `2026-06-24 05:31:26` | `cowrie.session.params` |
| `2026-06-24 05:31:26` | `cowrie.command.input` |
| `2026-06-24 05:31:26` | `cowrie.log.closed` |
| `2026-06-24 05:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06998349d518

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:32 |
| **Last Seen** | 2026-06-24 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:32:24` | `cowrie.session.connect` |
| `2026-06-24 05:32:24` | `cowrie.client.version` |
| `2026-06-24 05:32:24` | `cowrie.client.kex` |
| `2026-06-24 05:32:24` | `cowrie.login.success` |
| `2026-06-24 05:32:25` | `cowrie.session.params` |
| `2026-06-24 05:32:25` | `cowrie.command.input` |
| `2026-06-24 05:32:25` | `cowrie.log.closed` |
| `2026-06-24 05:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518f4c16544e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:32 |
| **Last Seen** | 2026-06-24 05:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123qwe' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:32:40` | `cowrie.session.connect` |
| `2026-06-24 05:32:40` | `cowrie.client.version` |
| `2026-06-24 05:32:41` | `cowrie.client.kex` |
| `2026-06-24 05:32:45` | `cowrie.login.success` |
| `2026-06-24 05:32:47` | `cowrie.session.params` |
| `2026-06-24 05:32:47` | `cowrie.command.input` |
| `2026-06-24 05:32:47` | `cowrie.command.input` |
| `2026-06-24 05:32:47` | `cowrie.command.input` |
| `2026-06-24 05:32:47` | `cowrie.command.input` |
| `2026-06-24 05:32:49` | `cowrie.log.closed` |
| `2026-06-24 05:32:51` | `cowrie.session.params` |
| `2026-06-24 05:32:51` | `cowrie.command.input` |
| `2026-06-24 05:32:51` | `cowrie.command.input` |
| `2026-06-24 05:32:51` | `cowrie.command.failed` |
| `2026-06-24 05:32:51` | `cowrie.command.failed` |
| `2026-06-24 05:32:51` | `cowrie.command.failed` |
| `2026-06-24 05:32:51` | `cowrie.command.failed` |
| `2026-06-24 05:32:52` | `cowrie.log.closed` |
| `2026-06-24 05:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fda62b0e0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:33 |
| **Last Seen** | 2026-06-24 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:33:21` | `cowrie.session.connect` |
| `2026-06-24 05:33:21` | `cowrie.client.version` |
| `2026-06-24 05:33:21` | `cowrie.client.kex` |
| `2026-06-24 05:33:22` | `cowrie.login.success` |
| `2026-06-24 05:33:22` | `cowrie.session.params` |
| `2026-06-24 05:33:22` | `cowrie.command.input` |
| `2026-06-24 05:33:23` | `cowrie.log.closed` |
| `2026-06-24 05:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab0433df6ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:34 |
| **Last Seen** | 2026-06-24 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:34:21` | `cowrie.session.connect` |
| `2026-06-24 05:34:21` | `cowrie.client.version` |
| `2026-06-24 05:34:21` | `cowrie.client.kex` |
| `2026-06-24 05:34:21` | `cowrie.login.success` |
| `2026-06-24 05:34:22` | `cowrie.session.params` |
| `2026-06-24 05:34:22` | `cowrie.command.input` |
| `2026-06-24 05:34:22` | `cowrie.log.closed` |
| `2026-06-24 05:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6aa41cb3e78

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]44` |
| **First Seen** | 2026-06-24 05:34 |
| **Last Seen** | 2026-06-24 05:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:34:47` | `cowrie.session.connect` |
| `2026-06-24 05:34:47` | `cowrie.login.success` |
| `2026-06-24 05:34:48` | `cowrie.session.params` |
| `2026-06-24 05:34:48` | `cowrie.command.input` |
| `2026-06-24 05:34:49` | `cowrie.command.input` |
| `2026-06-24 05:34:50` | `cowrie.command.input` |
| `2026-06-24 05:34:50` | `cowrie.command.input` |
| `2026-06-24 05:34:50` | `cowrie.command.failed` |
| `2026-06-24 05:34:51` | `cowrie.log.closed` |
| `2026-06-24 05:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]44` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b36fa847de9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:35 |
| **Last Seen** | 2026-06-24 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:35:18` | `cowrie.session.connect` |
| `2026-06-24 05:35:18` | `cowrie.client.version` |
| `2026-06-24 05:35:18` | `cowrie.client.kex` |
| `2026-06-24 05:35:18` | `cowrie.login.success` |
| `2026-06-24 05:35:19` | `cowrie.session.params` |
| `2026-06-24 05:35:19` | `cowrie.command.input` |
| `2026-06-24 05:35:19` | `cowrie.log.closed` |
| `2026-06-24 05:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-debc4ab6d4dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:36 |
| **Last Seen** | 2026-06-24 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:36:16` | `cowrie.session.connect` |
| `2026-06-24 05:36:16` | `cowrie.client.version` |
| `2026-06-24 05:36:16` | `cowrie.client.kex` |
| `2026-06-24 05:36:16` | `cowrie.login.success` |
| `2026-06-24 05:36:17` | `cowrie.session.params` |
| `2026-06-24 05:36:17` | `cowrie.command.input` |
| `2026-06-24 05:36:17` | `cowrie.log.closed` |
| `2026-06-24 05:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d48303d22e45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:36 |
| **Last Seen** | 2026-06-24 05:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:36:26` | `cowrie.session.connect` |
| `2026-06-24 05:36:27` | `cowrie.client.version` |
| `2026-06-24 05:36:27` | `cowrie.client.kex` |
| `2026-06-24 05:36:30` | `cowrie.login.success` |
| `2026-06-24 05:36:33` | `cowrie.session.params` |
| `2026-06-24 05:36:33` | `cowrie.command.input` |
| `2026-06-24 05:36:33` | `cowrie.command.input` |
| `2026-06-24 05:36:33` | `cowrie.command.input` |
| `2026-06-24 05:36:33` | `cowrie.command.input` |
| `2026-06-24 05:36:34` | `cowrie.log.closed` |
| `2026-06-24 05:36:37` | `cowrie.session.params` |
| `2026-06-24 05:36:37` | `cowrie.command.input` |
| `2026-06-24 05:36:37` | `cowrie.command.input` |
| `2026-06-24 05:36:37` | `cowrie.command.failed` |
| `2026-06-24 05:36:37` | `cowrie.command.failed` |
| `2026-06-24 05:36:37` | `cowrie.command.failed` |
| `2026-06-24 05:36:37` | `cowrie.command.failed` |
| `2026-06-24 05:36:38` | `cowrie.log.closed` |
| `2026-06-24 05:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8811a1a6c2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:37 |
| **Last Seen** | 2026-06-24 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:37:13` | `cowrie.session.connect` |
| `2026-06-24 05:37:13` | `cowrie.client.version` |
| `2026-06-24 05:37:13` | `cowrie.client.kex` |
| `2026-06-24 05:37:13` | `cowrie.login.success` |
| `2026-06-24 05:37:14` | `cowrie.session.params` |
| `2026-06-24 05:37:14` | `cowrie.command.input` |
| `2026-06-24 05:37:14` | `cowrie.log.closed` |
| `2026-06-24 05:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da463a62710

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:38 |
| **Last Seen** | 2026-06-24 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:38:09` | `cowrie.session.connect` |
| `2026-06-24 05:38:09` | `cowrie.client.version` |
| `2026-06-24 05:38:09` | `cowrie.client.kex` |
| `2026-06-24 05:38:10` | `cowrie.login.success` |
| `2026-06-24 05:38:11` | `cowrie.session.params` |
| `2026-06-24 05:38:11` | `cowrie.command.input` |
| `2026-06-24 05:38:11` | `cowrie.log.closed` |
| `2026-06-24 05:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e526e091b5c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:39 |
| **Last Seen** | 2026-06-24 05:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:39:08` | `cowrie.session.connect` |
| `2026-06-24 05:39:08` | `cowrie.client.version` |
| `2026-06-24 05:39:08` | `cowrie.client.kex` |
| `2026-06-24 05:39:08` | `cowrie.login.success` |
| `2026-06-24 05:39:10` | `cowrie.session.params` |
| `2026-06-24 05:39:10` | `cowrie.command.input` |
| `2026-06-24 05:39:10` | `cowrie.log.closed` |
| `2026-06-24 05:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56cc929d9240

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:40 |
| **Last Seen** | 2026-06-24 05:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '54321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:40:08` | `cowrie.session.connect` |
| `2026-06-24 05:40:09` | `cowrie.client.version` |
| `2026-06-24 05:40:09` | `cowrie.client.kex` |
| `2026-06-24 05:40:13` | `cowrie.login.success` |
| `2026-06-24 05:40:16` | `cowrie.session.params` |
| `2026-06-24 05:40:16` | `cowrie.command.input` |
| `2026-06-24 05:40:16` | `cowrie.command.input` |
| `2026-06-24 05:40:16` | `cowrie.command.input` |
| `2026-06-24 05:40:16` | `cowrie.command.input` |
| `2026-06-24 05:40:18` | `cowrie.log.closed` |
| `2026-06-24 05:40:20` | `cowrie.session.params` |
| `2026-06-24 05:40:20` | `cowrie.command.input` |
| `2026-06-24 05:40:20` | `cowrie.command.input` |
| `2026-06-24 05:40:20` | `cowrie.command.failed` |
| `2026-06-24 05:40:20` | `cowrie.command.failed` |
| `2026-06-24 05:40:20` | `cowrie.command.failed` |
| `2026-06-24 05:40:20` | `cowrie.command.failed` |
| `2026-06-24 05:40:21` | `cowrie.log.closed` |
| `2026-06-24 05:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1893749fa68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:41 |
| **Last Seen** | 2026-06-24 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:41:10` | `cowrie.session.connect` |
| `2026-06-24 05:41:10` | `cowrie.client.version` |
| `2026-06-24 05:41:11` | `cowrie.client.kex` |
| `2026-06-24 05:41:11` | `cowrie.login.success` |
| `2026-06-24 05:41:12` | `cowrie.session.params` |
| `2026-06-24 05:41:12` | `cowrie.command.input` |
| `2026-06-24 05:41:12` | `cowrie.log.closed` |
| `2026-06-24 05:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8fde5ad84f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:42 |
| **Last Seen** | 2026-06-24 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:42:08` | `cowrie.session.connect` |
| `2026-06-24 05:42:08` | `cowrie.client.version` |
| `2026-06-24 05:42:08` | `cowrie.client.kex` |
| `2026-06-24 05:42:09` | `cowrie.login.success` |
| `2026-06-24 05:42:09` | `cowrie.session.params` |
| `2026-06-24 05:42:09` | `cowrie.command.input` |
| `2026-06-24 05:42:09` | `cowrie.log.closed` |
| `2026-06-24 05:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3746433dbd

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 05:42 |
| **Last Seen** | 2026-06-24 05:42 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:42:42` | `cowrie.session.connect` |
| `2026-06-24 05:42:43` | `cowrie.client.version` |
| `2026-06-24 05:42:43` | `cowrie.client.kex` |
| `2026-06-24 05:42:50` | `cowrie.login.success` |
| `2026-06-24 05:42:54` | `cowrie.session.params` |
| `2026-06-24 05:42:54` | `cowrie.command.input` |
| `2026-06-24 05:42:56` | `cowrie.log.closed` |
| `2026-06-24 05:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cce6ca3a83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:43 |
| **Last Seen** | 2026-06-24 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:43:05` | `cowrie.session.connect` |
| `2026-06-24 05:43:05` | `cowrie.client.version` |
| `2026-06-24 05:43:05` | `cowrie.client.kex` |
| `2026-06-24 05:43:06` | `cowrie.login.success` |
| `2026-06-24 05:43:06` | `cowrie.session.params` |
| `2026-06-24 05:43:06` | `cowrie.command.input` |
| `2026-06-24 05:43:06` | `cowrie.log.closed` |
| `2026-06-24 05:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f587cd9ef170

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:44 |
| **Last Seen** | 2026-06-24 05:44 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'dev' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:44:02` | `cowrie.session.connect` |
| `2026-06-24 05:44:04` | `cowrie.client.version` |
| `2026-06-24 05:44:04` | `cowrie.client.kex` |
| `2026-06-24 05:44:09` | `cowrie.login.success` |
| `2026-06-24 05:44:12` | `cowrie.session.params` |
| `2026-06-24 05:44:12` | `cowrie.command.input` |
| `2026-06-24 05:44:12` | `cowrie.command.input` |
| `2026-06-24 05:44:12` | `cowrie.command.input` |
| `2026-06-24 05:44:12` | `cowrie.command.input` |
| `2026-06-24 05:44:13` | `cowrie.log.closed` |
| `2026-06-24 05:44:16` | `cowrie.session.params` |
| `2026-06-24 05:44:16` | `cowrie.command.input` |
| `2026-06-24 05:44:16` | `cowrie.command.input` |
| `2026-06-24 05:44:16` | `cowrie.command.failed` |
| `2026-06-24 05:44:16` | `cowrie.command.failed` |
| `2026-06-24 05:44:16` | `cowrie.command.failed` |
| `2026-06-24 05:44:16` | `cowrie.command.failed` |
| `2026-06-24 05:44:17` | `cowrie.log.closed` |
| `2026-06-24 05:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8622703dfd1f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:44 |
| **Last Seen** | 2026-06-24 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:44:05` | `cowrie.session.connect` |
| `2026-06-24 05:44:05` | `cowrie.client.version` |
| `2026-06-24 05:44:05` | `cowrie.client.kex` |
| `2026-06-24 05:44:06` | `cowrie.login.success` |
| `2026-06-24 05:44:07` | `cowrie.session.params` |
| `2026-06-24 05:44:07` | `cowrie.command.input` |
| `2026-06-24 05:44:07` | `cowrie.log.closed` |
| `2026-06-24 05:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1232d206a2e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:45 |
| **Last Seen** | 2026-06-24 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:45:04` | `cowrie.session.connect` |
| `2026-06-24 05:45:04` | `cowrie.client.version` |
| `2026-06-24 05:45:04` | `cowrie.client.kex` |
| `2026-06-24 05:45:05` | `cowrie.login.success` |
| `2026-06-24 05:45:05` | `cowrie.session.params` |
| `2026-06-24 05:45:05` | `cowrie.command.input` |
| `2026-06-24 05:45:06` | `cowrie.log.closed` |
| `2026-06-24 05:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62c05556f09

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:46 |
| **Last Seen** | 2026-06-24 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:46:03` | `cowrie.session.connect` |
| `2026-06-24 05:46:03` | `cowrie.client.version` |
| `2026-06-24 05:46:03` | `cowrie.client.kex` |
| `2026-06-24 05:46:03` | `cowrie.login.success` |
| `2026-06-24 05:46:04` | `cowrie.session.params` |
| `2026-06-24 05:46:04` | `cowrie.command.input` |
| `2026-06-24 05:46:04` | `cowrie.log.closed` |
| `2026-06-24 05:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ffd01eefa3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:47 |
| **Last Seen** | 2026-06-24 05:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:47:00` | `cowrie.session.connect` |
| `2026-06-24 05:47:00` | `cowrie.client.version` |
| `2026-06-24 05:47:01` | `cowrie.client.kex` |
| `2026-06-24 05:47:01` | `cowrie.login.success` |
| `2026-06-24 05:47:02` | `cowrie.session.params` |
| `2026-06-24 05:47:02` | `cowrie.command.input` |
| `2026-06-24 05:47:02` | `cowrie.log.closed` |
| `2026-06-24 05:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e202fde7ae35

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:47 |
| **Last Seen** | 2026-06-24 05:48 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'dev1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:47:59` | `cowrie.session.connect` |
| `2026-06-24 05:48:01` | `cowrie.client.version` |
| `2026-06-24 05:48:01` | `cowrie.client.kex` |
| `2026-06-24 05:48:05` | `cowrie.login.success` |
| `2026-06-24 05:48:08` | `cowrie.session.params` |
| `2026-06-24 05:48:08` | `cowrie.command.input` |
| `2026-06-24 05:48:08` | `cowrie.command.input` |
| `2026-06-24 05:48:08` | `cowrie.command.input` |
| `2026-06-24 05:48:08` | `cowrie.command.input` |
| `2026-06-24 05:48:09` | `cowrie.log.closed` |
| `2026-06-24 05:48:13` | `cowrie.session.params` |
| `2026-06-24 05:48:13` | `cowrie.command.input` |
| `2026-06-24 05:48:13` | `cowrie.command.input` |
| `2026-06-24 05:48:13` | `cowrie.command.failed` |
| `2026-06-24 05:48:13` | `cowrie.command.failed` |
| `2026-06-24 05:48:13` | `cowrie.command.failed` |
| `2026-06-24 05:48:13` | `cowrie.command.failed` |
| `2026-06-24 05:48:14` | `cowrie.log.closed` |
| `2026-06-24 05:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6105fc4f8a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:47 |
| **Last Seen** | 2026-06-24 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:47:59` | `cowrie.session.connect` |
| `2026-06-24 05:47:59` | `cowrie.client.version` |
| `2026-06-24 05:47:59` | `cowrie.client.kex` |
| `2026-06-24 05:48:00` | `cowrie.login.success` |
| `2026-06-24 05:48:00` | `cowrie.session.params` |
| `2026-06-24 05:48:00` | `cowrie.command.input` |
| `2026-06-24 05:48:01` | `cowrie.log.closed` |
| `2026-06-24 05:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f75e837ad5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:48 |
| **Last Seen** | 2026-06-24 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:48:56` | `cowrie.session.connect` |
| `2026-06-24 05:48:56` | `cowrie.client.version` |
| `2026-06-24 05:48:56` | `cowrie.client.kex` |
| `2026-06-24 05:48:57` | `cowrie.login.success` |
| `2026-06-24 05:48:57` | `cowrie.session.params` |
| `2026-06-24 05:48:57` | `cowrie.command.input` |
| `2026-06-24 05:48:57` | `cowrie.log.closed` |
| `2026-06-24 05:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3addd30e508

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:49 |
| **Last Seen** | 2026-06-24 05:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:49:52` | `cowrie.session.connect` |
| `2026-06-24 05:49:52` | `cowrie.client.version` |
| `2026-06-24 05:49:52` | `cowrie.client.kex` |
| `2026-06-24 05:49:52` | `cowrie.login.success` |
| `2026-06-24 05:49:53` | `cowrie.session.params` |
| `2026-06-24 05:49:53` | `cowrie.command.input` |
| `2026-06-24 05:49:53` | `cowrie.log.closed` |
| `2026-06-24 05:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9aa7086f8b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:50 |
| **Last Seen** | 2026-06-24 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:50:48` | `cowrie.session.connect` |
| `2026-06-24 05:50:48` | `cowrie.client.version` |
| `2026-06-24 05:50:48` | `cowrie.client.kex` |
| `2026-06-24 05:50:49` | `cowrie.login.success` |
| `2026-06-24 05:50:50` | `cowrie.session.params` |
| `2026-06-24 05:50:50` | `cowrie.command.input` |
| `2026-06-24 05:50:50` | `cowrie.log.closed` |
| `2026-06-24 05:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c679fb52b7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:51 |
| **Last Seen** | 2026-06-24 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:51:46` | `cowrie.session.connect` |
| `2026-06-24 05:51:46` | `cowrie.client.version` |
| `2026-06-24 05:51:46` | `cowrie.client.kex` |
| `2026-06-24 05:51:47` | `cowrie.login.success` |
| `2026-06-24 05:51:48` | `cowrie.session.params` |
| `2026-06-24 05:51:48` | `cowrie.command.input` |
| `2026-06-24 05:51:48` | `cowrie.log.closed` |
| `2026-06-24 05:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de13b4544cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:51 |
| **Last Seen** | 2026-06-24 05:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'dev123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:51:53` | `cowrie.session.connect` |
| `2026-06-24 05:51:54` | `cowrie.client.version` |
| `2026-06-24 05:51:54` | `cowrie.client.kex` |
| `2026-06-24 05:51:59` | `cowrie.login.success` |
| `2026-06-24 05:52:01` | `cowrie.session.params` |
| `2026-06-24 05:52:01` | `cowrie.command.input` |
| `2026-06-24 05:52:01` | `cowrie.command.input` |
| `2026-06-24 05:52:01` | `cowrie.command.input` |
| `2026-06-24 05:52:01` | `cowrie.command.input` |
| `2026-06-24 05:52:02` | `cowrie.log.closed` |
| `2026-06-24 05:52:05` | `cowrie.session.params` |
| `2026-06-24 05:52:05` | `cowrie.command.input` |
| `2026-06-24 05:52:05` | `cowrie.command.input` |
| `2026-06-24 05:52:05` | `cowrie.command.failed` |
| `2026-06-24 05:52:05` | `cowrie.command.failed` |
| `2026-06-24 05:52:05` | `cowrie.command.failed` |
| `2026-06-24 05:52:05` | `cowrie.command.failed` |
| `2026-06-24 05:52:06` | `cowrie.log.closed` |
| `2026-06-24 05:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d2cd9516d7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:52 |
| **Last Seen** | 2026-06-24 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:52:46` | `cowrie.session.connect` |
| `2026-06-24 05:52:46` | `cowrie.client.version` |
| `2026-06-24 05:52:46` | `cowrie.client.kex` |
| `2026-06-24 05:52:47` | `cowrie.login.success` |
| `2026-06-24 05:52:47` | `cowrie.session.params` |
| `2026-06-24 05:52:47` | `cowrie.command.input` |
| `2026-06-24 05:52:47` | `cowrie.log.closed` |
| `2026-06-24 05:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab12151c7a2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:53 |
| **Last Seen** | 2026-06-24 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:53:46` | `cowrie.session.connect` |
| `2026-06-24 05:53:46` | `cowrie.client.version` |
| `2026-06-24 05:53:46` | `cowrie.client.kex` |
| `2026-06-24 05:53:46` | `cowrie.login.success` |
| `2026-06-24 05:53:47` | `cowrie.session.params` |
| `2026-06-24 05:53:47` | `cowrie.command.input` |
| `2026-06-24 05:53:47` | `cowrie.log.closed` |
| `2026-06-24 05:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84637c05e301

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:54 |
| **Last Seen** | 2026-06-24 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:54:45` | `cowrie.session.connect` |
| `2026-06-24 05:54:45` | `cowrie.client.version` |
| `2026-06-24 05:54:45` | `cowrie.client.kex` |
| `2026-06-24 05:54:45` | `cowrie.login.success` |
| `2026-06-24 05:54:46` | `cowrie.session.params` |
| `2026-06-24 05:54:46` | `cowrie.command.input` |
| `2026-06-24 05:54:46` | `cowrie.log.closed` |
| `2026-06-24 05:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed1f1461b75

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:55 |
| **Last Seen** | 2026-06-24 05:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:55:37` | `cowrie.session.connect` |
| `2026-06-24 05:55:38` | `cowrie.client.version` |
| `2026-06-24 05:55:38` | `cowrie.client.kex` |
| `2026-06-24 05:55:43` | `cowrie.login.success` |
| `2026-06-24 05:55:46` | `cowrie.session.params` |
| `2026-06-24 05:55:46` | `cowrie.command.input` |
| `2026-06-24 05:55:46` | `cowrie.command.input` |
| `2026-06-24 05:55:46` | `cowrie.command.input` |
| `2026-06-24 05:55:46` | `cowrie.command.input` |
| `2026-06-24 05:55:47` | `cowrie.log.closed` |
| `2026-06-24 05:55:50` | `cowrie.session.params` |
| `2026-06-24 05:55:50` | `cowrie.command.input` |
| `2026-06-24 05:55:50` | `cowrie.command.input` |
| `2026-06-24 05:55:50` | `cowrie.command.failed` |
| `2026-06-24 05:55:50` | `cowrie.command.failed` |
| `2026-06-24 05:55:50` | `cowrie.command.failed` |
| `2026-06-24 05:55:50` | `cowrie.command.failed` |
| `2026-06-24 05:55:51` | `cowrie.log.closed` |
| `2026-06-24 05:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba58a87ffe0c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:55 |
| **Last Seen** | 2026-06-24 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:55:45` | `cowrie.session.connect` |
| `2026-06-24 05:55:45` | `cowrie.client.version` |
| `2026-06-24 05:55:45` | `cowrie.client.kex` |
| `2026-06-24 05:55:45` | `cowrie.login.success` |
| `2026-06-24 05:55:47` | `cowrie.session.params` |
| `2026-06-24 05:55:47` | `cowrie.command.input` |
| `2026-06-24 05:55:47` | `cowrie.log.closed` |
| `2026-06-24 05:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af28f7d1ae4e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:56 |
| **Last Seen** | 2026-06-24 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:56:43` | `cowrie.session.connect` |
| `2026-06-24 05:56:43` | `cowrie.client.version` |
| `2026-06-24 05:56:43` | `cowrie.client.kex` |
| `2026-06-24 05:56:44` | `cowrie.login.success` |
| `2026-06-24 05:56:44` | `cowrie.session.params` |
| `2026-06-24 05:56:44` | `cowrie.command.input` |
| `2026-06-24 05:56:45` | `cowrie.log.closed` |
| `2026-06-24 05:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c49832a3ee

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 05:57 |
| **Last Seen** | 2026-06-24 05:57 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:57:25` | `cowrie.session.connect` |
| `2026-06-24 05:57:27` | `cowrie.client.version` |
| `2026-06-24 05:57:27` | `cowrie.client.kex` |
| `2026-06-24 05:57:34` | `cowrie.login.success` |
| `2026-06-24 05:57:38` | `cowrie.session.params` |
| `2026-06-24 05:57:38` | `cowrie.command.input` |
| `2026-06-24 05:57:39` | `cowrie.log.closed` |
| `2026-06-24 05:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6a5d4ab09d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:57 |
| **Last Seen** | 2026-06-24 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:57:41` | `cowrie.session.connect` |
| `2026-06-24 05:57:41` | `cowrie.client.version` |
| `2026-06-24 05:57:41` | `cowrie.client.kex` |
| `2026-06-24 05:57:41` | `cowrie.login.success` |
| `2026-06-24 05:57:42` | `cowrie.session.params` |
| `2026-06-24 05:57:42` | `cowrie.command.input` |
| `2026-06-24 05:57:42` | `cowrie.log.closed` |
| `2026-06-24 05:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc935e209e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:58 |
| **Last Seen** | 2026-06-24 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:58:39` | `cowrie.session.connect` |
| `2026-06-24 05:58:39` | `cowrie.client.version` |
| `2026-06-24 05:58:39` | `cowrie.client.kex` |
| `2026-06-24 05:58:39` | `cowrie.login.success` |
| `2026-06-24 05:58:40` | `cowrie.session.params` |
| `2026-06-24 05:58:40` | `cowrie.command.input` |
| `2026-06-24 05:58:40` | `cowrie.log.closed` |
| `2026-06-24 05:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd47ed599ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]231` |
| **First Seen** | 2026-06-24 05:59 |
| **Last Seen** | 2026-06-24 05:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'developer' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:59:24` | `cowrie.session.connect` |
| `2026-06-24 05:59:25` | `cowrie.client.version` |
| `2026-06-24 05:59:25` | `cowrie.client.kex` |
| `2026-06-24 05:59:30` | `cowrie.login.success` |
| `2026-06-24 05:59:33` | `cowrie.session.params` |
| `2026-06-24 05:59:33` | `cowrie.command.input` |
| `2026-06-24 05:59:33` | `cowrie.command.input` |
| `2026-06-24 05:59:33` | `cowrie.command.input` |
| `2026-06-24 05:59:33` | `cowrie.command.input` |
| `2026-06-24 05:59:34` | `cowrie.log.closed` |
| `2026-06-24 05:59:36` | `cowrie.session.params` |
| `2026-06-24 05:59:36` | `cowrie.command.input` |
| `2026-06-24 05:59:36` | `cowrie.command.input` |
| `2026-06-24 05:59:36` | `cowrie.command.failed` |
| `2026-06-24 05:59:36` | `cowrie.command.failed` |
| `2026-06-24 05:59:36` | `cowrie.command.failed` |
| `2026-06-24 05:59:36` | `cowrie.command.failed` |
| `2026-06-24 05:59:37` | `cowrie.log.closed` |
| `2026-06-24 05:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b9a594609b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 05:59 |
| **Last Seen** | 2026-06-24 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 05:59:37` | `cowrie.session.connect` |
| `2026-06-24 05:59:37` | `cowrie.client.version` |
| `2026-06-24 05:59:37` | `cowrie.client.kex` |
| `2026-06-24 05:59:38` | `cowrie.login.success` |
| `2026-06-24 05:59:39` | `cowrie.session.params` |
| `2026-06-24 05:59:39` | `cowrie.command.input` |
| `2026-06-24 05:59:39` | `cowrie.log.closed` |
| `2026-06-24 05:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe31c124d34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:00 |
| **Last Seen** | 2026-06-24 06:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:00:31` | `cowrie.session.connect` |
| `2026-06-24 06:00:31` | `cowrie.client.version` |
| `2026-06-24 06:00:31` | `cowrie.client.kex` |
| `2026-06-24 06:00:31` | `cowrie.login.success` |
| `2026-06-24 06:00:32` | `cowrie.session.params` |
| `2026-06-24 06:00:32` | `cowrie.command.input` |
| `2026-06-24 06:00:32` | `cowrie.log.closed` |
| `2026-06-24 06:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de291e1dc5af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:01 |
| **Last Seen** | 2026-06-24 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:01:16` | `cowrie.session.connect` |
| `2026-06-24 06:01:16` | `cowrie.client.version` |
| `2026-06-24 06:01:16` | `cowrie.client.kex` |
| `2026-06-24 06:01:16` | `cowrie.login.success` |
| `2026-06-24 06:01:17` | `cowrie.session.params` |
| `2026-06-24 06:01:17` | `cowrie.command.input` |
| `2026-06-24 06:01:17` | `cowrie.log.closed` |
| `2026-06-24 06:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc1b0fa89a9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:02 |
| **Last Seen** | 2026-06-24 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:02:01` | `cowrie.session.connect` |
| `2026-06-24 06:02:01` | `cowrie.client.version` |
| `2026-06-24 06:02:01` | `cowrie.client.kex` |
| `2026-06-24 06:02:01` | `cowrie.login.success` |
| `2026-06-24 06:02:02` | `cowrie.session.params` |
| `2026-06-24 06:02:02` | `cowrie.command.input` |
| `2026-06-24 06:02:02` | `cowrie.log.closed` |
| `2026-06-24 06:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155b21b8ada5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:02 |
| **Last Seen** | 2026-06-24 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:02:45` | `cowrie.session.connect` |
| `2026-06-24 06:02:45` | `cowrie.client.version` |
| `2026-06-24 06:02:45` | `cowrie.client.kex` |
| `2026-06-24 06:02:46` | `cowrie.login.success` |
| `2026-06-24 06:02:47` | `cowrie.session.params` |
| `2026-06-24 06:02:47` | `cowrie.command.input` |
| `2026-06-24 06:02:47` | `cowrie.log.closed` |
| `2026-06-24 06:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7f86f02f69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:03 |
| **Last Seen** | 2026-06-24 06:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:03:31` | `cowrie.session.connect` |
| `2026-06-24 06:03:31` | `cowrie.client.version` |
| `2026-06-24 06:03:32` | `cowrie.client.kex` |
| `2026-06-24 06:03:32` | `cowrie.login.success` |
| `2026-06-24 06:03:32` | `cowrie.session.params` |
| `2026-06-24 06:03:32` | `cowrie.command.input` |
| `2026-06-24 06:03:33` | `cowrie.log.closed` |
| `2026-06-24 06:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82077b36ff94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:04 |
| **Last Seen** | 2026-06-24 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:04:18` | `cowrie.session.connect` |
| `2026-06-24 06:04:18` | `cowrie.client.version` |
| `2026-06-24 06:04:19` | `cowrie.client.kex` |
| `2026-06-24 06:04:19` | `cowrie.login.success` |
| `2026-06-24 06:04:20` | `cowrie.session.params` |
| `2026-06-24 06:04:20` | `cowrie.command.input` |
| `2026-06-24 06:04:20` | `cowrie.log.closed` |
| `2026-06-24 06:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170c3a7bcd42

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:05 |
| **Last Seen** | 2026-06-24 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:05:05` | `cowrie.session.connect` |
| `2026-06-24 06:05:05` | `cowrie.client.version` |
| `2026-06-24 06:05:05` | `cowrie.client.kex` |
| `2026-06-24 06:05:06` | `cowrie.login.success` |
| `2026-06-24 06:05:07` | `cowrie.session.params` |
| `2026-06-24 06:05:07` | `cowrie.command.input` |
| `2026-06-24 06:05:07` | `cowrie.log.closed` |
| `2026-06-24 06:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d78b1c18b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:05 |
| **Last Seen** | 2026-06-24 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:05:54` | `cowrie.session.connect` |
| `2026-06-24 06:05:54` | `cowrie.client.version` |
| `2026-06-24 06:05:54` | `cowrie.client.kex` |
| `2026-06-24 06:05:54` | `cowrie.login.success` |
| `2026-06-24 06:05:55` | `cowrie.session.params` |
| `2026-06-24 06:05:55` | `cowrie.command.input` |
| `2026-06-24 06:05:55` | `cowrie.log.closed` |
| `2026-06-24 06:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf69060bab7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:06 |
| **Last Seen** | 2026-06-24 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:06:41` | `cowrie.session.connect` |
| `2026-06-24 06:06:41` | `cowrie.client.version` |
| `2026-06-24 06:06:42` | `cowrie.client.kex` |
| `2026-06-24 06:06:42` | `cowrie.login.success` |
| `2026-06-24 06:06:43` | `cowrie.session.params` |
| `2026-06-24 06:06:43` | `cowrie.command.input` |
| `2026-06-24 06:06:43` | `cowrie.log.closed` |
| `2026-06-24 06:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eacede46206a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:07 |
| **Last Seen** | 2026-06-24 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:07:29` | `cowrie.session.connect` |
| `2026-06-24 06:07:29` | `cowrie.client.version` |
| `2026-06-24 06:07:29` | `cowrie.client.kex` |
| `2026-06-24 06:07:29` | `cowrie.login.success` |
| `2026-06-24 06:07:30` | `cowrie.session.params` |
| `2026-06-24 06:07:30` | `cowrie.command.input` |
| `2026-06-24 06:07:30` | `cowrie.log.closed` |
| `2026-06-24 06:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8e74bc10bb0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:08 |
| **Last Seen** | 2026-06-24 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:08:15` | `cowrie.session.connect` |
| `2026-06-24 06:08:15` | `cowrie.client.version` |
| `2026-06-24 06:08:15` | `cowrie.client.kex` |
| `2026-06-24 06:08:16` | `cowrie.login.success` |
| `2026-06-24 06:08:16` | `cowrie.session.params` |
| `2026-06-24 06:08:16` | `cowrie.command.input` |
| `2026-06-24 06:08:16` | `cowrie.log.closed` |
| `2026-06-24 06:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2820a83f5f5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:09 |
| **Last Seen** | 2026-06-24 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:09:00` | `cowrie.session.connect` |
| `2026-06-24 06:09:00` | `cowrie.client.version` |
| `2026-06-24 06:09:01` | `cowrie.client.kex` |
| `2026-06-24 06:09:01` | `cowrie.login.success` |
| `2026-06-24 06:09:02` | `cowrie.session.params` |
| `2026-06-24 06:09:02` | `cowrie.command.input` |
| `2026-06-24 06:09:02` | `cowrie.log.closed` |
| `2026-06-24 06:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4635a4c2b4e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:09 |
| **Last Seen** | 2026-06-24 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:09:47` | `cowrie.session.connect` |
| `2026-06-24 06:09:47` | `cowrie.client.version` |
| `2026-06-24 06:09:47` | `cowrie.client.kex` |
| `2026-06-24 06:09:47` | `cowrie.login.success` |
| `2026-06-24 06:09:48` | `cowrie.session.params` |
| `2026-06-24 06:09:48` | `cowrie.command.input` |
| `2026-06-24 06:09:48` | `cowrie.log.closed` |
| `2026-06-24 06:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6deb2e18731

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:10 |
| **Last Seen** | 2026-06-24 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:10:33` | `cowrie.session.connect` |
| `2026-06-24 06:10:33` | `cowrie.client.version` |
| `2026-06-24 06:10:33` | `cowrie.client.kex` |
| `2026-06-24 06:10:34` | `cowrie.login.success` |
| `2026-06-24 06:10:34` | `cowrie.session.params` |
| `2026-06-24 06:10:34` | `cowrie.command.input` |
| `2026-06-24 06:10:34` | `cowrie.log.closed` |
| `2026-06-24 06:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95516c8b7fdf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:11 |
| **Last Seen** | 2026-06-24 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:11:21` | `cowrie.session.connect` |
| `2026-06-24 06:11:21` | `cowrie.client.version` |
| `2026-06-24 06:11:21` | `cowrie.client.kex` |
| `2026-06-24 06:11:21` | `cowrie.login.success` |
| `2026-06-24 06:11:22` | `cowrie.session.params` |
| `2026-06-24 06:11:22` | `cowrie.command.input` |
| `2026-06-24 06:11:22` | `cowrie.log.closed` |
| `2026-06-24 06:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a648f5618e17

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 06:12 |
| **Last Seen** | 2026-06-24 06:12 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:12:00` | `cowrie.session.connect` |
| `2026-06-24 06:12:01` | `cowrie.client.version` |
| `2026-06-24 06:12:01` | `cowrie.client.kex` |
| `2026-06-24 06:12:08` | `cowrie.login.success` |
| `2026-06-24 06:12:13` | `cowrie.session.params` |
| `2026-06-24 06:12:13` | `cowrie.command.input` |
| `2026-06-24 06:12:14` | `cowrie.log.closed` |
| `2026-06-24 06:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3718343c9db3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:12 |
| **Last Seen** | 2026-06-24 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:12:10` | `cowrie.session.connect` |
| `2026-06-24 06:12:10` | `cowrie.client.version` |
| `2026-06-24 06:12:10` | `cowrie.client.kex` |
| `2026-06-24 06:12:10` | `cowrie.login.success` |
| `2026-06-24 06:12:11` | `cowrie.session.params` |
| `2026-06-24 06:12:11` | `cowrie.command.input` |
| `2026-06-24 06:12:11` | `cowrie.log.closed` |
| `2026-06-24 06:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915487936122

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:12 |
| **Last Seen** | 2026-06-24 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:12:58` | `cowrie.session.connect` |
| `2026-06-24 06:12:58` | `cowrie.client.version` |
| `2026-06-24 06:12:58` | `cowrie.client.kex` |
| `2026-06-24 06:12:58` | `cowrie.login.success` |
| `2026-06-24 06:12:59` | `cowrie.session.params` |
| `2026-06-24 06:12:59` | `cowrie.command.input` |
| `2026-06-24 06:12:59` | `cowrie.log.closed` |
| `2026-06-24 06:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc65c8ad957

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:13 |
| **Last Seen** | 2026-06-24 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:13:45` | `cowrie.session.connect` |
| `2026-06-24 06:13:45` | `cowrie.client.version` |
| `2026-06-24 06:13:45` | `cowrie.client.kex` |
| `2026-06-24 06:13:45` | `cowrie.login.success` |
| `2026-06-24 06:13:46` | `cowrie.session.params` |
| `2026-06-24 06:13:46` | `cowrie.command.input` |
| `2026-06-24 06:13:46` | `cowrie.log.closed` |
| `2026-06-24 06:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39c6ad35a05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:14 |
| **Last Seen** | 2026-06-24 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:14:32` | `cowrie.session.connect` |
| `2026-06-24 06:14:32` | `cowrie.client.version` |
| `2026-06-24 06:14:32` | `cowrie.client.kex` |
| `2026-06-24 06:14:33` | `cowrie.login.success` |
| `2026-06-24 06:14:33` | `cowrie.session.params` |
| `2026-06-24 06:14:33` | `cowrie.command.input` |
| `2026-06-24 06:14:34` | `cowrie.log.closed` |
| `2026-06-24 06:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f25a64f661e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:15 |
| **Last Seen** | 2026-06-24 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:15:19` | `cowrie.session.connect` |
| `2026-06-24 06:15:19` | `cowrie.client.version` |
| `2026-06-24 06:15:19` | `cowrie.client.kex` |
| `2026-06-24 06:15:19` | `cowrie.login.success` |
| `2026-06-24 06:15:20` | `cowrie.session.params` |
| `2026-06-24 06:15:20` | `cowrie.command.input` |
| `2026-06-24 06:15:20` | `cowrie.log.closed` |
| `2026-06-24 06:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e35db269a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:16 |
| **Last Seen** | 2026-06-24 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:16:05` | `cowrie.session.connect` |
| `2026-06-24 06:16:05` | `cowrie.client.version` |
| `2026-06-24 06:16:05` | `cowrie.client.kex` |
| `2026-06-24 06:16:06` | `cowrie.login.success` |
| `2026-06-24 06:16:06` | `cowrie.session.params` |
| `2026-06-24 06:16:06` | `cowrie.command.input` |
| `2026-06-24 06:16:06` | `cowrie.log.closed` |
| `2026-06-24 06:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4c22a4e048

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:16 |
| **Last Seen** | 2026-06-24 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:16:53` | `cowrie.session.connect` |
| `2026-06-24 06:16:53` | `cowrie.client.version` |
| `2026-06-24 06:16:53` | `cowrie.client.kex` |
| `2026-06-24 06:16:54` | `cowrie.login.success` |
| `2026-06-24 06:16:55` | `cowrie.session.params` |
| `2026-06-24 06:16:55` | `cowrie.command.input` |
| `2026-06-24 06:16:55` | `cowrie.log.closed` |
| `2026-06-24 06:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f01527a1ce1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:17 |
| **Last Seen** | 2026-06-24 06:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:17:43` | `cowrie.session.connect` |
| `2026-06-24 06:17:43` | `cowrie.client.version` |
| `2026-06-24 06:17:43` | `cowrie.client.kex` |
| `2026-06-24 06:17:43` | `cowrie.login.success` |
| `2026-06-24 06:17:44` | `cowrie.session.params` |
| `2026-06-24 06:17:44` | `cowrie.command.input` |
| `2026-06-24 06:17:44` | `cowrie.log.closed` |
| `2026-06-24 06:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f8ea12654b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:18 |
| **Last Seen** | 2026-06-24 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:18:33` | `cowrie.session.connect` |
| `2026-06-24 06:18:33` | `cowrie.client.version` |
| `2026-06-24 06:18:34` | `cowrie.client.kex` |
| `2026-06-24 06:18:34` | `cowrie.login.success` |
| `2026-06-24 06:18:35` | `cowrie.session.params` |
| `2026-06-24 06:18:35` | `cowrie.command.input` |
| `2026-06-24 06:18:35` | `cowrie.log.closed` |
| `2026-06-24 06:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9052e4777a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:19 |
| **Last Seen** | 2026-06-24 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:19:26` | `cowrie.session.connect` |
| `2026-06-24 06:19:26` | `cowrie.client.version` |
| `2026-06-24 06:19:26` | `cowrie.client.kex` |
| `2026-06-24 06:19:27` | `cowrie.login.success` |
| `2026-06-24 06:19:28` | `cowrie.session.params` |
| `2026-06-24 06:19:28` | `cowrie.command.input` |
| `2026-06-24 06:19:28` | `cowrie.log.closed` |
| `2026-06-24 06:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ffbddcbbcd1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:20 |
| **Last Seen** | 2026-06-24 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:20:15` | `cowrie.session.connect` |
| `2026-06-24 06:20:15` | `cowrie.client.version` |
| `2026-06-24 06:20:15` | `cowrie.client.kex` |
| `2026-06-24 06:20:15` | `cowrie.login.success` |
| `2026-06-24 06:20:16` | `cowrie.session.params` |
| `2026-06-24 06:20:16` | `cowrie.command.input` |
| `2026-06-24 06:20:16` | `cowrie.log.closed` |
| `2026-06-24 06:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff44a2856c62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:21 |
| **Last Seen** | 2026-06-24 06:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:21:07` | `cowrie.session.connect` |
| `2026-06-24 06:21:07` | `cowrie.client.version` |
| `2026-06-24 06:21:07` | `cowrie.client.kex` |
| `2026-06-24 06:21:07` | `cowrie.login.success` |
| `2026-06-24 06:21:08` | `cowrie.session.params` |
| `2026-06-24 06:21:08` | `cowrie.command.input` |
| `2026-06-24 06:21:08` | `cowrie.log.closed` |
| `2026-06-24 06:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f888cf5f572c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:21 |
| **Last Seen** | 2026-06-24 06:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:21:58` | `cowrie.session.connect` |
| `2026-06-24 06:21:58` | `cowrie.client.version` |
| `2026-06-24 06:21:58` | `cowrie.client.kex` |
| `2026-06-24 06:21:58` | `cowrie.login.success` |
| `2026-06-24 06:21:59` | `cowrie.session.params` |
| `2026-06-24 06:21:59` | `cowrie.command.input` |
| `2026-06-24 06:21:59` | `cowrie.log.closed` |
| `2026-06-24 06:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea29eeb436f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:22 |
| **Last Seen** | 2026-06-24 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:22:46` | `cowrie.session.connect` |
| `2026-06-24 06:22:46` | `cowrie.client.version` |
| `2026-06-24 06:22:47` | `cowrie.client.kex` |
| `2026-06-24 06:22:47` | `cowrie.login.success` |
| `2026-06-24 06:22:48` | `cowrie.session.params` |
| `2026-06-24 06:22:48` | `cowrie.command.input` |
| `2026-06-24 06:22:48` | `cowrie.log.closed` |
| `2026-06-24 06:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b734dcac7e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:23 |
| **Last Seen** | 2026-06-24 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:23:36` | `cowrie.session.connect` |
| `2026-06-24 06:23:36` | `cowrie.client.version` |
| `2026-06-24 06:23:36` | `cowrie.client.kex` |
| `2026-06-24 06:23:36` | `cowrie.login.success` |
| `2026-06-24 06:23:37` | `cowrie.session.params` |
| `2026-06-24 06:23:37` | `cowrie.command.input` |
| `2026-06-24 06:23:37` | `cowrie.log.closed` |
| `2026-06-24 06:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a016a2de1b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:24 |
| **Last Seen** | 2026-06-24 06:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:24:26` | `cowrie.session.connect` |
| `2026-06-24 06:24:26` | `cowrie.client.version` |
| `2026-06-24 06:24:27` | `cowrie.client.kex` |
| `2026-06-24 06:24:27` | `cowrie.login.success` |
| `2026-06-24 06:24:28` | `cowrie.session.params` |
| `2026-06-24 06:24:28` | `cowrie.command.input` |
| `2026-06-24 06:24:28` | `cowrie.log.closed` |
| `2026-06-24 06:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1baff9ba33e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:25 |
| **Last Seen** | 2026-06-24 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:25:17` | `cowrie.session.connect` |
| `2026-06-24 06:25:17` | `cowrie.client.version` |
| `2026-06-24 06:25:17` | `cowrie.client.kex` |
| `2026-06-24 06:25:17` | `cowrie.login.success` |
| `2026-06-24 06:25:18` | `cowrie.session.params` |
| `2026-06-24 06:25:18` | `cowrie.command.input` |
| `2026-06-24 06:25:18` | `cowrie.log.closed` |
| `2026-06-24 06:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda744acc504

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:26 |
| **Last Seen** | 2026-06-24 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:26:07` | `cowrie.session.connect` |
| `2026-06-24 06:26:07` | `cowrie.client.version` |
| `2026-06-24 06:26:08` | `cowrie.client.kex` |
| `2026-06-24 06:26:08` | `cowrie.login.success` |
| `2026-06-24 06:26:09` | `cowrie.session.params` |
| `2026-06-24 06:26:09` | `cowrie.command.input` |
| `2026-06-24 06:26:09` | `cowrie.log.closed` |
| `2026-06-24 06:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d955e50cd4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 06:26 |
| **Last Seen** | 2026-06-24 06:26 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:26:20` | `cowrie.session.connect` |
| `2026-06-24 06:26:22` | `cowrie.client.version` |
| `2026-06-24 06:26:22` | `cowrie.client.kex` |
| `2026-06-24 06:26:28` | `cowrie.login.success` |
| `2026-06-24 06:26:33` | `cowrie.session.params` |
| `2026-06-24 06:26:33` | `cowrie.command.input` |
| `2026-06-24 06:26:34` | `cowrie.log.closed` |
| `2026-06-24 06:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b3eab65d71

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:26 |
| **Last Seen** | 2026-06-24 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:26:58` | `cowrie.session.connect` |
| `2026-06-24 06:26:58` | `cowrie.client.version` |
| `2026-06-24 06:26:58` | `cowrie.client.kex` |
| `2026-06-24 06:26:58` | `cowrie.login.success` |
| `2026-06-24 06:26:59` | `cowrie.session.params` |
| `2026-06-24 06:26:59` | `cowrie.command.input` |
| `2026-06-24 06:26:59` | `cowrie.log.closed` |
| `2026-06-24 06:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b19b8802d68b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:27 |
| **Last Seen** | 2026-06-24 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:27:48` | `cowrie.session.connect` |
| `2026-06-24 06:27:48` | `cowrie.client.version` |
| `2026-06-24 06:27:48` | `cowrie.client.kex` |
| `2026-06-24 06:27:48` | `cowrie.login.success` |
| `2026-06-24 06:27:49` | `cowrie.session.params` |
| `2026-06-24 06:27:49` | `cowrie.command.input` |
| `2026-06-24 06:27:49` | `cowrie.log.closed` |
| `2026-06-24 06:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f795652cdd3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:28 |
| **Last Seen** | 2026-06-24 06:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:28:42` | `cowrie.session.connect` |
| `2026-06-24 06:28:42` | `cowrie.client.version` |
| `2026-06-24 06:28:42` | `cowrie.client.kex` |
| `2026-06-24 06:28:42` | `cowrie.login.success` |
| `2026-06-24 06:28:43` | `cowrie.session.params` |
| `2026-06-24 06:28:43` | `cowrie.command.input` |
| `2026-06-24 06:28:43` | `cowrie.log.closed` |
| `2026-06-24 06:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e4de3828c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:29 |
| **Last Seen** | 2026-06-24 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:29:31` | `cowrie.session.connect` |
| `2026-06-24 06:29:31` | `cowrie.client.version` |
| `2026-06-24 06:29:32` | `cowrie.client.kex` |
| `2026-06-24 06:29:32` | `cowrie.login.success` |
| `2026-06-24 06:29:33` | `cowrie.session.params` |
| `2026-06-24 06:29:33` | `cowrie.command.input` |
| `2026-06-24 06:29:33` | `cowrie.log.closed` |
| `2026-06-24 06:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f89a98b22d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:30 |
| **Last Seen** | 2026-06-24 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:30:26` | `cowrie.session.connect` |
| `2026-06-24 06:30:26` | `cowrie.client.version` |
| `2026-06-24 06:30:26` | `cowrie.client.kex` |
| `2026-06-24 06:30:26` | `cowrie.login.success` |
| `2026-06-24 06:30:27` | `cowrie.session.params` |
| `2026-06-24 06:30:27` | `cowrie.command.input` |
| `2026-06-24 06:30:27` | `cowrie.log.closed` |
| `2026-06-24 06:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d897e1068ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:31 |
| **Last Seen** | 2026-06-24 06:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:31:18` | `cowrie.session.connect` |
| `2026-06-24 06:31:18` | `cowrie.client.version` |
| `2026-06-24 06:31:18` | `cowrie.client.kex` |
| `2026-06-24 06:31:18` | `cowrie.login.success` |
| `2026-06-24 06:31:19` | `cowrie.session.params` |
| `2026-06-24 06:31:19` | `cowrie.command.input` |
| `2026-06-24 06:31:19` | `cowrie.log.closed` |
| `2026-06-24 06:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba0c1835b02

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:32 |
| **Last Seen** | 2026-06-24 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:32:07` | `cowrie.session.connect` |
| `2026-06-24 06:32:07` | `cowrie.client.version` |
| `2026-06-24 06:32:07` | `cowrie.client.kex` |
| `2026-06-24 06:32:08` | `cowrie.login.success` |
| `2026-06-24 06:32:08` | `cowrie.session.params` |
| `2026-06-24 06:32:08` | `cowrie.command.input` |
| `2026-06-24 06:32:09` | `cowrie.log.closed` |
| `2026-06-24 06:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bbb61f5ba61

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:32 |
| **Last Seen** | 2026-06-24 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:32:56` | `cowrie.session.connect` |
| `2026-06-24 06:32:56` | `cowrie.client.version` |
| `2026-06-24 06:32:56` | `cowrie.client.kex` |
| `2026-06-24 06:32:57` | `cowrie.login.success` |
| `2026-06-24 06:32:57` | `cowrie.session.params` |
| `2026-06-24 06:32:57` | `cowrie.command.input` |
| `2026-06-24 06:32:58` | `cowrie.log.closed` |
| `2026-06-24 06:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39e3394faae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:33 |
| **Last Seen** | 2026-06-24 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:33:49` | `cowrie.session.connect` |
| `2026-06-24 06:33:49` | `cowrie.client.version` |
| `2026-06-24 06:33:49` | `cowrie.client.kex` |
| `2026-06-24 06:33:49` | `cowrie.login.success` |
| `2026-06-24 06:33:50` | `cowrie.session.params` |
| `2026-06-24 06:33:50` | `cowrie.command.input` |
| `2026-06-24 06:33:50` | `cowrie.log.closed` |
| `2026-06-24 06:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5bfeb5867d0

| Field | Detail |
|---|---|
| **Source IP** | `180.76.61[.]232` |
| **First Seen** | 2026-06-24 06:34 |
| **Last Seen** | 2026-06-24 06:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:34:40` | `cowrie.session.connect` |
| `2026-06-24 06:34:40` | `cowrie.client.version` |
| `2026-06-24 06:34:40` | `cowrie.client.kex` |
| `2026-06-24 06:34:41` | `cowrie.login.success` |
| `2026-06-24 06:34:42` | `cowrie.session.params` |
| `2026-06-24 06:34:42` | `cowrie.command.input` |
| `2026-06-24 06:34:43` | `cowrie.log.closed` |
| `2026-06-24 06:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.61[.]232` to AbuseIPDB if not already reported
- [ ] Block `180.76.61[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a24c113d37c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:34 |
| **Last Seen** | 2026-06-24 06:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:34:44` | `cowrie.session.connect` |
| `2026-06-24 06:34:44` | `cowrie.client.version` |
| `2026-06-24 06:34:44` | `cowrie.client.kex` |
| `2026-06-24 06:34:44` | `cowrie.login.success` |
| `2026-06-24 06:34:45` | `cowrie.session.params` |
| `2026-06-24 06:34:45` | `cowrie.command.input` |
| `2026-06-24 06:34:45` | `cowrie.log.closed` |
| `2026-06-24 06:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-850ae3b9efaf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:35 |
| **Last Seen** | 2026-06-24 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:35:33` | `cowrie.session.connect` |
| `2026-06-24 06:35:33` | `cowrie.client.version` |
| `2026-06-24 06:35:33` | `cowrie.client.kex` |
| `2026-06-24 06:35:33` | `cowrie.login.success` |
| `2026-06-24 06:35:34` | `cowrie.session.params` |
| `2026-06-24 06:35:34` | `cowrie.command.input` |
| `2026-06-24 06:35:34` | `cowrie.log.closed` |
| `2026-06-24 06:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d7941d9bde4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:36 |
| **Last Seen** | 2026-06-24 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:36:22` | `cowrie.session.connect` |
| `2026-06-24 06:36:22` | `cowrie.client.version` |
| `2026-06-24 06:36:22` | `cowrie.client.kex` |
| `2026-06-24 06:36:22` | `cowrie.login.success` |
| `2026-06-24 06:36:23` | `cowrie.session.params` |
| `2026-06-24 06:36:23` | `cowrie.command.input` |
| `2026-06-24 06:36:23` | `cowrie.log.closed` |
| `2026-06-24 06:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71dee53574fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:37 |
| **Last Seen** | 2026-06-24 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:37:12` | `cowrie.session.connect` |
| `2026-06-24 06:37:12` | `cowrie.client.version` |
| `2026-06-24 06:37:12` | `cowrie.client.kex` |
| `2026-06-24 06:37:12` | `cowrie.login.success` |
| `2026-06-24 06:37:13` | `cowrie.session.params` |
| `2026-06-24 06:37:13` | `cowrie.command.input` |
| `2026-06-24 06:37:13` | `cowrie.log.closed` |
| `2026-06-24 06:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87e6e4af450

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:38 |
| **Last Seen** | 2026-06-24 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:38:02` | `cowrie.session.connect` |
| `2026-06-24 06:38:02` | `cowrie.client.version` |
| `2026-06-24 06:38:02` | `cowrie.client.kex` |
| `2026-06-24 06:38:02` | `cowrie.login.success` |
| `2026-06-24 06:38:03` | `cowrie.session.params` |
| `2026-06-24 06:38:03` | `cowrie.command.input` |
| `2026-06-24 06:38:03` | `cowrie.log.closed` |
| `2026-06-24 06:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01559fdf8164

| Field | Detail |
|---|---|
| **Source IP** | `85.215.192[.]100` |
| **First Seen** | 2026-06-24 06:38 |
| **Last Seen** | 2026-06-24 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:38:22` | `cowrie.session.connect` |
| `2026-06-24 06:38:22` | `cowrie.client.version` |
| `2026-06-24 06:38:22` | `cowrie.client.kex` |
| `2026-06-24 06:38:23` | `cowrie.login.success` |
| `2026-06-24 06:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.215.192[.]100` to AbuseIPDB if not already reported
- [ ] Block `85.215.192[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f325b6980613

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:38 |
| **Last Seen** | 2026-06-24 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:38:51` | `cowrie.session.connect` |
| `2026-06-24 06:38:51` | `cowrie.client.version` |
| `2026-06-24 06:38:51` | `cowrie.client.kex` |
| `2026-06-24 06:38:52` | `cowrie.login.success` |
| `2026-06-24 06:38:52` | `cowrie.session.params` |
| `2026-06-24 06:38:52` | `cowrie.command.input` |
| `2026-06-24 06:38:52` | `cowrie.log.closed` |
| `2026-06-24 06:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b436fd5e79ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:39 |
| **Last Seen** | 2026-06-24 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:39:40` | `cowrie.session.connect` |
| `2026-06-24 06:39:40` | `cowrie.client.version` |
| `2026-06-24 06:39:40` | `cowrie.client.kex` |
| `2026-06-24 06:39:40` | `cowrie.login.success` |
| `2026-06-24 06:39:41` | `cowrie.session.params` |
| `2026-06-24 06:39:41` | `cowrie.command.input` |
| `2026-06-24 06:39:41` | `cowrie.log.closed` |
| `2026-06-24 06:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d88dce5209

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:40 |
| **Last Seen** | 2026-06-24 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:40:28` | `cowrie.session.connect` |
| `2026-06-24 06:40:28` | `cowrie.client.version` |
| `2026-06-24 06:40:28` | `cowrie.client.kex` |
| `2026-06-24 06:40:28` | `cowrie.login.success` |
| `2026-06-24 06:40:29` | `cowrie.session.params` |
| `2026-06-24 06:40:29` | `cowrie.command.input` |
| `2026-06-24 06:40:29` | `cowrie.log.closed` |
| `2026-06-24 06:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b642ec25c33

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 06:40 |
| **Last Seen** | 2026-06-24 06:40 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:40:40` | `cowrie.session.connect` |
| `2026-06-24 06:40:41` | `cowrie.client.version` |
| `2026-06-24 06:40:41` | `cowrie.client.kex` |
| `2026-06-24 06:40:48` | `cowrie.login.success` |
| `2026-06-24 06:40:52` | `cowrie.session.params` |
| `2026-06-24 06:40:52` | `cowrie.command.input` |
| `2026-06-24 06:40:54` | `cowrie.log.closed` |
| `2026-06-24 06:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8469ef2eb014

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:41 |
| **Last Seen** | 2026-06-24 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:41:16` | `cowrie.session.connect` |
| `2026-06-24 06:41:16` | `cowrie.client.version` |
| `2026-06-24 06:41:16` | `cowrie.client.kex` |
| `2026-06-24 06:41:17` | `cowrie.login.success` |
| `2026-06-24 06:41:17` | `cowrie.session.params` |
| `2026-06-24 06:41:17` | `cowrie.command.input` |
| `2026-06-24 06:41:18` | `cowrie.log.closed` |
| `2026-06-24 06:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5a23c9d751

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:42 |
| **Last Seen** | 2026-06-24 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:42:05` | `cowrie.session.connect` |
| `2026-06-24 06:42:05` | `cowrie.client.version` |
| `2026-06-24 06:42:05` | `cowrie.client.kex` |
| `2026-06-24 06:42:05` | `cowrie.login.success` |
| `2026-06-24 06:42:06` | `cowrie.session.params` |
| `2026-06-24 06:42:06` | `cowrie.command.input` |
| `2026-06-24 06:42:06` | `cowrie.log.closed` |
| `2026-06-24 06:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db906ddf5f8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:42 |
| **Last Seen** | 2026-06-24 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:42:54` | `cowrie.session.connect` |
| `2026-06-24 06:42:54` | `cowrie.client.version` |
| `2026-06-24 06:42:54` | `cowrie.client.kex` |
| `2026-06-24 06:42:55` | `cowrie.login.success` |
| `2026-06-24 06:42:55` | `cowrie.session.params` |
| `2026-06-24 06:42:55` | `cowrie.command.input` |
| `2026-06-24 06:42:56` | `cowrie.log.closed` |
| `2026-06-24 06:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a63852a1c08

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:43 |
| **Last Seen** | 2026-06-24 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:43:45` | `cowrie.session.connect` |
| `2026-06-24 06:43:45` | `cowrie.client.version` |
| `2026-06-24 06:43:45` | `cowrie.client.kex` |
| `2026-06-24 06:43:46` | `cowrie.login.success` |
| `2026-06-24 06:43:46` | `cowrie.session.params` |
| `2026-06-24 06:43:46` | `cowrie.command.input` |
| `2026-06-24 06:43:47` | `cowrie.log.closed` |
| `2026-06-24 06:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8e5b773971

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:44 |
| **Last Seen** | 2026-06-24 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:44:36` | `cowrie.session.connect` |
| `2026-06-24 06:44:36` | `cowrie.client.version` |
| `2026-06-24 06:44:36` | `cowrie.client.kex` |
| `2026-06-24 06:44:36` | `cowrie.login.success` |
| `2026-06-24 06:44:37` | `cowrie.session.params` |
| `2026-06-24 06:44:37` | `cowrie.command.input` |
| `2026-06-24 06:44:37` | `cowrie.log.closed` |
| `2026-06-24 06:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea96c201f12

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:45 |
| **Last Seen** | 2026-06-24 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:45:27` | `cowrie.session.connect` |
| `2026-06-24 06:45:27` | `cowrie.client.version` |
| `2026-06-24 06:45:27` | `cowrie.client.kex` |
| `2026-06-24 06:45:28` | `cowrie.login.success` |
| `2026-06-24 06:45:29` | `cowrie.session.params` |
| `2026-06-24 06:45:29` | `cowrie.command.input` |
| `2026-06-24 06:45:29` | `cowrie.log.closed` |
| `2026-06-24 06:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a3d5a35d668

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:46 |
| **Last Seen** | 2026-06-24 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:46:23` | `cowrie.session.connect` |
| `2026-06-24 06:46:23` | `cowrie.client.version` |
| `2026-06-24 06:46:23` | `cowrie.client.kex` |
| `2026-06-24 06:46:23` | `cowrie.login.success` |
| `2026-06-24 06:46:24` | `cowrie.session.params` |
| `2026-06-24 06:46:24` | `cowrie.command.input` |
| `2026-06-24 06:46:24` | `cowrie.log.closed` |
| `2026-06-24 06:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f22dcfbe542

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:47 |
| **Last Seen** | 2026-06-24 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:47:12` | `cowrie.session.connect` |
| `2026-06-24 06:47:12` | `cowrie.client.version` |
| `2026-06-24 06:47:12` | `cowrie.client.kex` |
| `2026-06-24 06:47:13` | `cowrie.login.success` |
| `2026-06-24 06:47:13` | `cowrie.session.params` |
| `2026-06-24 06:47:13` | `cowrie.command.input` |
| `2026-06-24 06:47:13` | `cowrie.log.closed` |
| `2026-06-24 06:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0669f29d1057

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:48 |
| **Last Seen** | 2026-06-24 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:48:06` | `cowrie.session.connect` |
| `2026-06-24 06:48:06` | `cowrie.client.version` |
| `2026-06-24 06:48:06` | `cowrie.client.kex` |
| `2026-06-24 06:48:06` | `cowrie.login.success` |
| `2026-06-24 06:48:07` | `cowrie.session.params` |
| `2026-06-24 06:48:07` | `cowrie.command.input` |
| `2026-06-24 06:48:07` | `cowrie.log.closed` |
| `2026-06-24 06:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4891469fbbe3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 06:48 |
| **Last Seen** | 2026-06-24 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:48:35` | `cowrie.session.connect` |
| `2026-06-24 06:48:35` | `cowrie.client.version` |
| `2026-06-24 06:48:35` | `cowrie.client.kex` |
| `2026-06-24 06:48:36` | `cowrie.login.success` |
| `2026-06-24 06:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37763e6d112d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 06:48 |
| **Last Seen** | 2026-06-24 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:48:37` | `cowrie.session.connect` |
| `2026-06-24 06:48:37` | `cowrie.client.version` |
| `2026-06-24 06:48:37` | `cowrie.client.kex` |
| `2026-06-24 06:48:37` | `cowrie.login.success` |
| `2026-06-24 06:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31079d1a289

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 06:48 |
| **Last Seen** | 2026-06-24 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:48:43` | `cowrie.session.connect` |
| `2026-06-24 06:48:43` | `cowrie.client.version` |
| `2026-06-24 06:48:43` | `cowrie.client.kex` |
| `2026-06-24 06:48:43` | `cowrie.login.success` |
| `2026-06-24 06:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67963aaddc56

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 06:48 |
| **Last Seen** | 2026-06-24 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:48:43` | `cowrie.session.connect` |
| `2026-06-24 06:48:43` | `cowrie.client.version` |
| `2026-06-24 06:48:44` | `cowrie.client.kex` |
| `2026-06-24 06:48:44` | `cowrie.login.success` |
| `2026-06-24 06:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2120f59c18

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:48 |
| **Last Seen** | 2026-06-24 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:48:57` | `cowrie.session.connect` |
| `2026-06-24 06:48:57` | `cowrie.client.version` |
| `2026-06-24 06:48:57` | `cowrie.client.kex` |
| `2026-06-24 06:48:57` | `cowrie.login.success` |
| `2026-06-24 06:48:58` | `cowrie.session.params` |
| `2026-06-24 06:48:58` | `cowrie.command.input` |
| `2026-06-24 06:48:58` | `cowrie.log.closed` |
| `2026-06-24 06:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd4184fbe82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:49 |
| **Last Seen** | 2026-06-24 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:49:49` | `cowrie.session.connect` |
| `2026-06-24 06:49:49` | `cowrie.client.version` |
| `2026-06-24 06:49:50` | `cowrie.client.kex` |
| `2026-06-24 06:49:50` | `cowrie.login.success` |
| `2026-06-24 06:49:51` | `cowrie.session.params` |
| `2026-06-24 06:49:51` | `cowrie.command.input` |
| `2026-06-24 06:49:51` | `cowrie.log.closed` |
| `2026-06-24 06:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ae8bfa509f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:50 |
| **Last Seen** | 2026-06-24 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:50:42` | `cowrie.session.connect` |
| `2026-06-24 06:50:42` | `cowrie.client.version` |
| `2026-06-24 06:50:42` | `cowrie.client.kex` |
| `2026-06-24 06:50:43` | `cowrie.login.success` |
| `2026-06-24 06:50:43` | `cowrie.session.params` |
| `2026-06-24 06:50:43` | `cowrie.command.input` |
| `2026-06-24 06:50:44` | `cowrie.log.closed` |
| `2026-06-24 06:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409b4bfee201

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:51 |
| **Last Seen** | 2026-06-24 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:51:32` | `cowrie.session.connect` |
| `2026-06-24 06:51:32` | `cowrie.client.version` |
| `2026-06-24 06:51:32` | `cowrie.client.kex` |
| `2026-06-24 06:51:33` | `cowrie.login.success` |
| `2026-06-24 06:51:33` | `cowrie.session.params` |
| `2026-06-24 06:51:33` | `cowrie.command.input` |
| `2026-06-24 06:51:34` | `cowrie.log.closed` |
| `2026-06-24 06:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbf112961942

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:52 |
| **Last Seen** | 2026-06-24 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:52:21` | `cowrie.session.connect` |
| `2026-06-24 06:52:21` | `cowrie.client.version` |
| `2026-06-24 06:52:21` | `cowrie.client.kex` |
| `2026-06-24 06:52:21` | `cowrie.login.success` |
| `2026-06-24 06:52:22` | `cowrie.session.params` |
| `2026-06-24 06:52:22` | `cowrie.command.input` |
| `2026-06-24 06:52:22` | `cowrie.log.closed` |
| `2026-06-24 06:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb57f14438cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:53 |
| **Last Seen** | 2026-06-24 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:53:09` | `cowrie.session.connect` |
| `2026-06-24 06:53:09` | `cowrie.client.version` |
| `2026-06-24 06:53:09` | `cowrie.client.kex` |
| `2026-06-24 06:53:09` | `cowrie.login.success` |
| `2026-06-24 06:53:10` | `cowrie.session.params` |
| `2026-06-24 06:53:10` | `cowrie.command.input` |
| `2026-06-24 06:53:10` | `cowrie.log.closed` |
| `2026-06-24 06:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85ec9b164f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:53 |
| **Last Seen** | 2026-06-24 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:53:56` | `cowrie.session.connect` |
| `2026-06-24 06:53:56` | `cowrie.client.version` |
| `2026-06-24 06:53:57` | `cowrie.client.kex` |
| `2026-06-24 06:53:57` | `cowrie.login.success` |
| `2026-06-24 06:53:57` | `cowrie.session.params` |
| `2026-06-24 06:53:57` | `cowrie.command.input` |
| `2026-06-24 06:53:58` | `cowrie.log.closed` |
| `2026-06-24 06:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59851f0b7249

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:54 |
| **Last Seen** | 2026-06-24 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:54:45` | `cowrie.session.connect` |
| `2026-06-24 06:54:45` | `cowrie.client.version` |
| `2026-06-24 06:54:45` | `cowrie.client.kex` |
| `2026-06-24 06:54:46` | `cowrie.login.success` |
| `2026-06-24 06:54:47` | `cowrie.session.params` |
| `2026-06-24 06:54:47` | `cowrie.command.input` |
| `2026-06-24 06:54:47` | `cowrie.log.closed` |
| `2026-06-24 06:54:47` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **275** | 2026-06-24 02:55 | 2026-06-24 06:54 | 0m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.205.70[.]223` | **7** | 2026-06-24 04:50 | 2026-06-24 04:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-24 04:31 | 2026-06-24 05:14 | 3m | 0 | `T1592` | 🟢 LOW |
| `52.248.40[.]89` | **2** | 2026-06-24 03:55 | 2026-06-24 03:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | **2** | 2026-06-24 05:32 | 2026-06-24 05:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]58` | **2** | 2026-06-24 06:35 | 2026-06-24 06:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.145.104[.]105` | 1 | 2026-06-24 04:17 | 2026-06-24 04:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]44` | 1 | 2026-06-24 05:34 | 2026-06-24 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.71.207[.]229` | 1 | 2026-06-24 06:29 | 2026-06-24 06:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.76.61[.]232` | 1 | 2026-06-24 06:34 | 2026-06-24 06:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]169` | 1 | 2026-06-24 04:09 | 2026-06-24 04:09 | 1s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]251` | 1 | 2026-06-24 04:58 | 2026-06-24 04:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]226` | 1 | 2026-06-24 04:49 | 2026-06-24 04:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]142` | 1 | 2026-06-24 04:04 | 2026-06-24 04:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.62.154[.]45` | 1 | 2026-06-24 04:49 | 2026-06-24 04:49 | 4s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-06-24 03:58 | 2026-06-24 04:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.185.50[.]192` | 1 | 2026-06-24 03:01 | 2026-06-24 03:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]42` | 1 | 2026-06-24 06:54 | 2026-06-24 06:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-24 04:43 | 2026-06-24 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-06-24 05:40 | 2026-06-24 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-06-24 06:38 | 2026-06-24 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-24 05:30 | 2026-06-24 05:32 | 104s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]192` | 1 | 2026-06-24 05:07 | 2026-06-24 05:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]30` | 1 | 2026-06-24 06:27 | 2026-06-24 06:27 | 4s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]148` | 1 | 2026-06-24 04:48 | 2026-06-24 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]246` | 1 | 2026-06-24 04:34 | 2026-06-24 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]120` | 1 | 2026-06-24 04:58 | 2026-06-24 04:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]95` | 1 | 2026-06-24 04:34 | 2026-06-24 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]62` | 1 | 2026-06-24 03:43 | 2026-06-24 03:43 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `34.62.154[.]45` | BE | Google LLC | **100** ⚠️ | 0 |
| `35.205.70[.]223` | BE | Google LLC | **100** ⚠️ | 0 |
| `85.215.192[.]100` | DE | IONOS SE | **100** ⚠️ | 7 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `81.19.216[.]120` | NL | Infrawatch Limited | **100** ⚠️ | 16 |
| `176.65.139[.]44` | NL | Storm Industries LLC | **100** ⚠️ | 50 |
| `69.5.169[.]148` | DE | Infrawatch Limited | **100** ⚠️ | 30 |
| `185.247.137[.]169` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `39.185.50[.]192` | CN | China Mobile Communications Corporation | **100** ⚠️ | 3 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 417 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 417 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 52 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 51 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 13 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 750 cases |
| Tool 34  | Credential Extractor        | ✅ 422 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (2.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 29 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 416 priority case(s) shown individually · 29 recon entry/entries in table (6 group(s) consolidating 290 session(s)).

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
_Report time: 2026-06-24T07:49:33Z_

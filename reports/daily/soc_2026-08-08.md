# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T22:33:02Z |
| **Shift Time** | 22:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **121** |
| Confirmed Threats | **0** |
| False Positives Filtered | **121** (100.0%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **0** |
| High Severity Cases | **48** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **73** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **246** |
| Unique Credential Pairs | **208** |
| Unique Usernames | **11** |
| Unique Passwords | **206** |
| Successful Auth Pairs | **238** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 212 |
| `support` | 8 |
| `thomas` | 4 |
| `admin` | 4 |
| `apache` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 4 |
| `thomas` | 4 |
| `Support10` | 4 |
| `LeitboGi0ro` | 4 |
| `admin` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 4 |
| `thomas` | `thomas` | 4 |
| `support` | `Support10` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `apache` | `apache` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test` | `test123` | `111.70.32.49` | 2026-08-08T19:04:40 |
| `test` | `test123` | `14.194.128.158` | 2026-08-08T19:04:48 |
| `apache` | `apache` | `121.202.198.98` | 2026-08-08T19:10:59 |
| `apache` | `apache` | `178.178.194.134` | 2026-08-08T19:11:18 |
| `apache` | `apache` | `185.81.94.58` | 2026-08-08T19:11:31 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T19:19:11 |
| `thomas` | `thomas` | `10.0.0.73` | 2026-08-08T19:21:11 |
| `monitor` | `monitor` | `202.138.229.190` | 2026-08-08T19:21:12 |
| `thomas` | `thomas` | `119.160.166.237` | 2026-08-08T19:22:39 |
| `thomas` | `thomas` | `181.212.174.166` | 2026-08-08T19:22:52 |
| `support` | `Support10` | `10.0.0.73` | 2026-08-08T19:26:23 |
| `monitor` | `monitor` | `10.0.0.73` | 2026-08-08T19:32:47 |
| `thomas` | `thomas` | `122.117.30.20` | 2026-08-08T19:39:04 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T19:43:47 |
| `support` | `Support10` | `208.96.233.67` | 2026-08-08T19:44:52 |
| `support` | `Support10` | `41.220.3.101` | 2026-08-08T19:45:11 |
| `support` | `Support10` | `223.107.72.234` | 2026-08-08T19:45:24 |
| `monitor` | `monitor` | `81.214.75.248` | 2026-08-08T19:50:05 |
| `root` | `12` | `10.0.0.73` | 2026-08-08T19:57:46 |
| `root` | `123` | `10.0.0.73` | 2026-08-08T19:57:56 |
| `root` | `1234` | `10.0.0.73` | 2026-08-08T19:58:11 |
| `root` | `12345` | `10.0.0.73` | 2026-08-08T19:58:23 |
| `root` | `123321` | `10.0.0.73` | 2026-08-08T19:58:52 |
| `root` | `123123` | `10.0.0.73` | 2026-08-08T19:59:05 |
| `root` | `102030` | `10.0.0.73` | 2026-08-08T19:59:31 |
| `root` | `112233332211` | `10.0.0.73` | 2026-08-08T19:59:58 |
| `root` | `1234567` | `10.0.0.73` | 2026-08-08T20:00:10 |
| `root` | `123456789` | `10.0.0.73` | 2026-08-08T20:00:34 |
| `git` | `git` | `10.0.0.73` | 2026-08-08T20:00:40 |
| `root` | `0987654321` | `10.0.0.73` | 2026-08-08T20:00:59 |
| `root` | `87654321` | `10.0.0.73` | 2026-08-08T20:01:24 |
| `root` | `654321` | `10.0.0.73` | 2026-08-08T20:01:48 |
| `root` | `54321` | `10.0.0.73` | 2026-08-08T20:02:01 |
| `root` | `4321` | `10.0.0.73` | 2026-08-08T20:02:12 |
| `root` | `321` | `10.0.0.73` | 2026-08-08T20:02:23 |
| `root` | `00` | `10.0.0.73` | 2026-08-08T20:02:47 |
| `root` | `0000` | `10.0.0.73` | 2026-08-08T20:03:11 |
| `root` | `000000` | `10.0.0.73` | 2026-08-08T20:03:34 |
| `root` | `00000000` | `10.0.0.73` | 2026-08-08T20:03:59 |
| `root` | `000000000` | `10.0.0.73` | 2026-08-08T20:04:14 |
| `root` | `0000000000` | `10.0.0.73` | 2026-08-08T20:04:24 |
| `root` | `Qazwsxedc123` | `10.0.0.73` | 2026-08-08T20:04:37 |
| `root` | `smart@123` | `10.0.0.73` | 2026-08-08T20:04:51 |
| `root` | `Dell@1234` | `10.0.0.73` | 2026-08-08T20:05:01 |
| `root` | `Aa123123` | `10.0.0.73` | 2026-08-08T20:05:25 |
| `root` | `1qaz@WSX3edc` | `10.0.0.73` | 2026-08-08T20:05:50 |
| `root` | `123456789a` | `10.0.0.73` | 2026-08-08T20:06:17 |
| `root` | `Passw0rd123` | `10.0.0.73` | 2026-08-08T20:06:29 |
| `root` | `Abc123!@#` | `10.0.0.73` | 2026-08-08T20:06:54 |
| `roberto` | `roberto` | `10.0.0.73` | 2026-08-08T20:07:02 |
| `root` | `Aaa123456` | `10.0.0.73` | 2026-08-08T20:07:21 |
| `root` | `Aa123456.` | `10.0.0.73` | 2026-08-08T20:07:35 |
| `root` | `root@123` | `10.0.0.73` | 2026-08-08T20:07:49 |
| `root` | `Qwe123456` | `10.0.0.73` | 2026-08-08T20:08:00 |
| `root` | `123456Abc` | `10.0.0.73` | 2026-08-08T20:08:25 |
| `root` | `root123` | `10.0.0.73` | 2026-08-08T20:08:40 |
| `root` | `Root1234` | `10.0.0.73` | 2026-08-08T20:08:54 |
| `root` | `AAAaaa123` | `10.0.0.73` | 2026-08-08T20:09:05 |
| `root` | `abc123` | `10.0.0.73` | 2026-08-08T20:09:32 |
| `root` | `admin1234` | `10.0.0.73` | 2026-08-08T20:09:46 |
| `root` | `Root@1234` | `10.0.0.73` | 2026-08-08T20:10:12 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-08T20:10:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-08T20:10:18 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-08T20:10:26 |
| `root` | `!QAZ2wsx#EDC` | `10.0.0.73` | 2026-08-08T20:10:28 |
| `root` | `Admin@12` | `10.0.0.73` | 2026-08-08T20:10:41 |
| `root` | `Yy123456` | `10.0.0.73` | 2026-08-08T20:10:53 |
| `root` | `Admin@123456` | `10.0.0.73` | 2026-08-08T20:11:21 |
| `root` | `123456aA` | `10.0.0.73` | 2026-08-08T20:11:34 |
| `root` | `P@ssWord123` | `10.0.0.73` | 2026-08-08T20:12:02 |
| `root` | `!234Qwer` | `10.0.0.73` | 2026-08-08T20:12:17 |
| `root` | `computer123` | `10.0.0.73` | 2026-08-08T20:12:31 |
| `root` | `Pa$$w0rt` | `10.0.0.73` | 2026-08-08T20:12:42 |
| `root` | `Adm1n1$trat0r` | `10.0.0.73` | 2026-08-08T20:12:59 |
| `root` | `123456a?` | `10.0.0.73` | 2026-08-08T20:13:11 |
| `user` | `1qaz@WSX3edc` | `189.56.0.19` | 2026-08-08T20:13:15 |
| `root` | `Password0!` | `10.0.0.73` | 2026-08-08T20:13:24 |
| `user` | `1qaz@WSX3edc` | `41.220.3.101` | 2026-08-08T20:13:28 |
| `root` | `1qaz2wsx.` | `10.0.0.73` | 2026-08-08T20:13:52 |
| `root` | `roz@#2536` | `10.0.0.73` | 2026-08-08T20:14:07 |
| `root` | `Asd123456` | `10.0.0.73` | 2026-08-08T20:14:23 |
| `root` | `QWEqwe123` | `10.0.0.73` | 2026-08-08T20:14:34 |
| `root` | `Password123!` | `10.0.0.73` | 2026-08-08T20:14:49 |
| `root` | `P@ssw0rd` | `10.0.0.73` | 2026-08-08T20:15:03 |
| `root` | `abcd1234` | `10.0.0.73` | 2026-08-08T20:15:14 |
| `root` | `123qwe` | `10.0.0.73` | 2026-08-08T20:15:43 |
| `root` | `123.com` | `10.0.0.73` | 2026-08-08T20:15:56 |
| `root` | `Aa112211@` | `10.0.0.73` | 2026-08-08T20:16:23 |
| `root` | `1qaz2wsx` | `10.0.0.73` | 2026-08-08T20:16:38 |
| `root` | `Abc123456` | `10.0.0.73` | 2026-08-08T20:16:54 |
| `root` | `1q2w3e4r.` | `10.0.0.73` | 2026-08-08T20:17:05 |
| `root` | `admin` | `10.0.0.73` | 2026-08-08T20:17:21 |
| `root` | `password` | `10.0.0.73` | 2026-08-08T20:17:35 |
| `root` | `Huawei12#$` | `10.0.0.73` | 2026-08-08T20:17:47 |
| `root` | `Passw0rd` | `10.0.0.73` | 2026-08-08T20:18:15 |
| `root` | `Zx123456` | `10.0.0.73` | 2026-08-08T20:18:28 |
| `root` | `Aa123456..` | `10.0.0.73` | 2026-08-08T20:18:57 |
| `git` | `git` | `49.124.153.37` | 2026-08-08T20:19:07 |
| `root` | `!qaz@wsx3edc` | `10.0.0.73` | 2026-08-08T20:19:11 |
| `git` | `git` | `64.72.74.162` | 2026-08-08T20:19:23 |
| `root` | `qweasdzxc123!@#` | `10.0.0.73` | 2026-08-08T20:19:40 |
| `root` | `q1w2e3R$` | `10.0.0.73` | 2026-08-08T20:19:46 |
| `root` | `Ad123` | `10.0.0.73` | 2026-08-08T20:19:54 |
| `root` | `Qwe123123` | `10.0.0.73` | 2026-08-08T20:20:22 |
| `root` | `Zxc@123123` | `10.0.0.73` | 2026-08-08T20:20:37 |
| `root` | `Abc123.` | `10.0.0.73` | 2026-08-08T20:20:48 |
| `root` | `12qw12qw` | `10.0.0.73` | 2026-08-08T20:21:05 |
| `root` | `1234abcd!` | `10.0.0.73` | 2026-08-08T20:21:20 |
| `root` | `aa123123` | `10.0.0.73` | 2026-08-08T20:21:36 |
| `root` | `aaaa8888` | `10.0.0.73` | 2026-08-08T20:21:48 |
| `root` | `hp@123` | `10.0.0.73` | 2026-08-08T20:22:03 |
| `root` | `Cc123456` | `10.0.0.73` | 2026-08-08T20:22:31 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-08T20:22:34 |
| `root` | `1qaz2wsx!@` | `10.0.0.73` | 2026-08-08T20:22:46 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-08T20:22:54 |
| `root` | `Aa1234567890` | `10.0.0.73` | 2026-08-08T20:23:13 |
| `root` | `Abc1234567` | `10.0.0.73` | 2026-08-08T20:23:29 |
| `root` | `Aa123321` | `10.0.0.73` | 2026-08-08T20:23:44 |
| `root` | `Aa123456789!` | `10.0.0.73` | 2026-08-08T20:24:05 |
| `root` | `Qq123456` | `10.0.0.73` | 2026-08-08T20:24:17 |
| `roberto` | `roberto` | `103.103.53.44` | 2026-08-08T20:24:19 |
| `root` | `ZXCzxc123` | `10.0.0.73` | 2026-08-08T20:24:26 |
| `roberto` | `roberto` | `222.92.61.242` | 2026-08-08T20:24:28 |
| `root` | `1qazZAQ!` | `10.0.0.73` | 2026-08-08T20:24:39 |
| `root` | `Qwer1234` | `10.0.0.73` | 2026-08-08T20:24:55 |
| `root` | `a123456@` | `10.0.0.73` | 2026-08-08T20:25:08 |
| `root` | `Abc@123456` | `10.0.0.73` | 2026-08-08T20:25:20 |
| `root` | `Aa123123@` | `10.0.0.73` | 2026-08-08T20:25:49 |
| `root` | `123@123a` | `10.0.0.73` | 2026-08-08T20:26:02 |
| `root` | `a123456.` | `10.0.0.73` | 2026-08-08T20:26:31 |
| `root` | `Qwe112233` | `10.0.0.73` | 2026-08-08T20:26:45 |
| `root` | `Password1$` | `10.0.0.73` | 2026-08-08T20:27:13 |
| `root` | `Password1` | `10.0.0.73` | 2026-08-08T20:27:27 |
| `root` | `111111` | `92.118.39.14` | 2026-08-08T20:27:43 |
| `root` | `A123456` | `10.0.0.73` | 2026-08-08T20:27:56 |
| `root` | `Qwerty@123` | `10.0.0.73` | 2026-08-08T20:28:11 |
| `admin` | `admin` | `159.65.138.39` | 2026-08-08T20:28:21 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-08T20:28:22 |
| `root` | `admin` | `192.42.116.143` | 2026-08-08T20:28:27 |
| `root` | `qwe!@#123` | `10.0.0.73` | 2026-08-08T20:28:38 |
| `root` | `p@ssw0rd` | `10.0.0.73` | 2026-08-08T20:28:53 |
| `root` | `Aa111111` | `10.0.0.73` | 2026-08-08T20:29:08 |
| `root` | `qweqaz123` | `10.0.0.73` | 2026-08-08T20:29:21 |
| `ubnt` | `qwerty` | `116.48.143.166` | 2026-08-08T20:29:29 |
| `root` | `office` | `10.0.0.73` | 2026-08-08T20:29:37 |
| `root` | `123` | `92.118.39.14` | 2026-08-08T20:29:48 |
| `root` | `Huawei@123` | `10.0.0.73` | 2026-08-08T20:29:52 |
| `root` | `Aa123456` | `10.0.0.73` | 2026-08-08T20:30:05 |
| `root` | `123@com` | `10.0.0.73` | 2026-08-08T20:30:20 |
| `root` | `Admin@123` | `10.0.0.73` | 2026-08-08T20:30:29 |
| `root` | `Admin123456` | `10.0.0.73` | 2026-08-08T20:30:49 |
| `root` | `Zxc123!@#` | `10.0.0.73` | 2026-08-08T20:31:03 |
| `root` | `1qaz@WSX` | `10.0.0.73` | 2026-08-08T20:31:19 |
| `root` | `P@ssw0rd123` | `10.0.0.73` | 2026-08-08T20:31:28 |
| `root` | `Admin123` | `10.0.0.73` | 2026-08-08T20:31:44 |
| `root` | `ABCabc123` | `10.0.0.73` | 2026-08-08T20:31:51 |
| `root` | `123123` | `92.118.39.14` | 2026-08-08T20:31:54 |
| `root` | `Pa$$wort` | `10.0.0.73` | 2026-08-08T20:32:15 |
| `root` | `qwe@12345` | `10.0.0.73` | 2026-08-08T20:32:47 |
| `root` | `123.Com` | `10.0.0.73` | 2026-08-08T20:33:07 |
| `root` | `www.163.com` | `10.0.0.73` | 2026-08-08T20:33:14 |
| `root` | `now.cn123` | `10.0.0.73` | 2026-08-08T20:33:37 |
| `root` | `123321` | `92.118.39.14` | 2026-08-08T20:33:57 |
| `root` | `qwer.1234` | `10.0.0.73` | 2026-08-08T20:34:02 |
| `root` | `oracle@123` | `10.0.0.73` | 2026-08-08T20:34:26 |
| `root` | `Passw0rd@123` | `10.0.0.73` | 2026-08-08T20:34:40 |
| `root` | `qaz-123456` | `10.0.0.73` | 2026-08-08T20:34:56 |
| `root` | `test.123` | `10.0.0.73` | 2026-08-08T20:35:01 |
| `root` | `1qaz1QAZ` | `10.0.0.73` | 2026-08-08T20:35:23 |
| `root` | `qwer@123` | `10.0.0.73` | 2026-08-08T20:35:44 |
| `root` | `1234` | `92.118.39.14` | 2026-08-08T20:35:58 |
| `root` | `Admin@12345` | `10.0.0.73` | 2026-08-08T20:36:07 |
| `root` | `Test123!@` | `10.0.0.73` | 2026-08-08T20:36:29 |
| `root` | `R00t@1234` | `10.0.0.73` | 2026-08-08T20:36:53 |
| `root` | `1qaz2wsx$` | `10.0.0.73` | 2026-08-08T20:37:17 |
| `root` | `!1q2w3e4r` | `10.0.0.73` | 2026-08-08T20:37:41 |
| `root` | `12345` | `92.118.39.14` | 2026-08-08T20:37:55 |
| `root` | `Zz123456` | `10.0.0.73` | 2026-08-08T20:38:07 |
| `root` | `qwe123asd123zxc` | `10.0.0.73` | 2026-08-08T20:38:16 |
| `root` | `abc123456!` | `10.0.0.73` | 2026-08-08T20:38:38 |
| `root` | `Passw0rd2` | `10.0.0.73` | 2026-08-08T20:39:01 |
| `root` | `Admin@` | `10.0.0.73` | 2026-08-08T20:39:24 |
| `root` | `Q1w2e3r4` | `10.0.0.73` | 2026-08-08T20:39:46 |
| `root` | `Admin@123321` | `10.0.0.73` | 2026-08-08T20:40:14 |
| `root` | `!QAZ2wsx3edc` | `10.0.0.73` | 2026-08-08T20:40:25 |
| `root` | `P@ssw0rd1!` | `10.0.0.73` | 2026-08-08T20:40:47 |
| `root` | `1234@qwer` | `10.0.0.73` | 2026-08-08T20:41:08 |
| `ubnt` | `qwerty` | `10.0.0.73` | 2026-08-08T20:41:11 |
| `root` | `QWEqwe123456` | `10.0.0.73` | 2026-08-08T20:41:31 |
| `root` | `1234567` | `92.118.39.14` | 2026-08-08T20:41:38 |
| `root` | `1q2w3e` | `10.0.0.73` | 2026-08-08T20:41:54 |
| `root` | `Aa123456!` | `10.0.0.73` | 2026-08-08T20:42:18 |
| `root` | `1qaz@WSX#EDC` | `10.0.0.73` | 2026-08-08T20:42:42 |
| `root` | `!p@ssw0rd` | `10.0.0.73` | 2026-08-08T20:43:07 |
| `root` | `Huawei@1234` | `10.0.0.73` | 2026-08-08T20:43:18 |
| `root` | `12345678` | `92.118.39.14` | 2026-08-08T20:43:30 |
| `root` | `PA55WORD` | `10.0.0.73` | 2026-08-08T20:43:40 |
| `root` | `Jj123456` | `10.0.0.73` | 2026-08-08T20:44:02 |
| `root` | `admin123###` | `10.0.0.73` | 2026-08-08T20:44:24 |
| `root` | `Zxcv123456` | `10.0.0.73` | 2026-08-08T20:44:47 |
| `root` | `Setup123!` | `10.0.0.73` | 2026-08-08T20:45:12 |
| `root` | `123456789` | `92.118.39.14` | 2026-08-08T20:45:20 |
| `root` | `P@ssw0rd123?` | `10.0.0.73` | 2026-08-08T20:45:40 |
| `root` | `Zz123456789` | `10.0.0.73` | 2026-08-08T20:45:48 |
| `root` | `passw0rd` | `10.0.0.73` | 2026-08-08T20:46:11 |
| `root` | `123456a!` | `10.0.0.73` | 2026-08-08T20:46:35 |
| `root` | `test@1234` | `10.0.0.73` | 2026-08-08T20:47:00 |
| `root` | `1234abcD` | `10.0.0.73` | 2026-08-08T20:47:17 |
| `root` | `1234abcd` | `92.118.39.14` | 2026-08-08T20:47:19 |
| `root` | `QWE1QWE!` | `10.0.0.73` | 2026-08-08T20:47:29 |
| `root` | `Admin@123#` | `10.0.0.73` | 2026-08-08T20:47:38 |
| `root` | `gyk@658` | `10.0.0.73` | 2026-08-08T20:47:50 |
| `root` | `Test!@#123` | `10.0.0.73` | 2026-08-08T20:48:01 |
| `root` | `Admin@1234#` | `10.0.0.73` | 2026-08-08T20:48:28 |
| `root` | `ABC@@123` | `10.0.0.73` | 2026-08-08T20:48:48 |
| `root` | `Cisco@123` | `10.0.0.73` | 2026-08-08T20:49:15 |
| `root` | `123abc` | `92.118.39.14` | 2026-08-08T20:49:18 |
| `root` | `Aa654321` | `10.0.0.73` | 2026-08-08T20:49:47 |
| `root` | `Abc12345` | `10.0.0.73` | 2026-08-08T20:50:10 |
| `root` | `root12345` | `10.0.0.73` | 2026-08-08T20:50:32 |
| `root` | `Temp@123` | `10.0.0.73` | 2026-08-08T20:50:56 |
| `root` | `123qwe` | `92.118.39.14` | 2026-08-08T20:51:19 |
| `root` | `Password!` | `10.0.0.73` | 2026-08-08T20:51:24 |
| `root` | `qwe123+` | `10.0.0.73` | 2026-08-08T20:51:31 |
| `root` | `Ab123456789` | `10.0.0.73` | 2026-08-08T20:51:50 |
| `root` | `QWER!@#$1234` | `10.0.0.73` | 2026-08-08T20:51:58 |
| `root` | `12qw!@QW` | `10.0.0.73` | 2026-08-08T20:52:21 |
| `root` | `P@ssword123456` | `10.0.0.73` | 2026-08-08T20:52:47 |
| `root` | `Aa@123456` | `10.0.0.73` | 2026-08-08T20:53:04 |
| `admin` | `zhone` | `64.72.74.162` | 2026-08-08T20:53:06 |
| `root` | `1q2w3e` | `92.118.39.14` | 2026-08-08T20:53:22 |
| `root` | `abc123!!` | `10.0.0.73` | 2026-08-08T20:53:25 |
| `admin` | `zhone` | `200.232.114.71` | 2026-08-08T20:53:26 |
| `root` | `qwe123` | `10.0.0.73` | 2026-08-08T20:53:37 |
| `root` | `Admin@123$` | `10.0.0.73` | 2026-08-08T20:53:47 |
| `root` | `Qazws@123` | `10.0.0.73` | 2026-08-08T20:54:09 |
| `root` | `Welc0me@123` | `10.0.0.73` | 2026-08-08T20:54:32 |
| `root` | `2wsxXSW@` | `10.0.0.73` | 2026-08-08T20:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **121** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 24 |
| Go SSH scanner | 22 |
| libssh | 10 |
| Paramiko (Python) | 8 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 22 | 20 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 22 | 20 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `b893695067f9...` | OpenSSH | 1 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 13 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.14`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **54** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | LOW |
| `AS396982` | Google LLC | 3 | LOW |
| `AS46562` | Performive LLC | 3 | LOW |
| `AS22773` | Cox Communications Inc. | 3 | LOW |
| `AS398324` | Censys, Inc. | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 48 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 15 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 13 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 13 |

---

## 🔕 False Positive Summary (121 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 121 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 121 cases |
| Tool 34  | Credential Extractor        | ✅ 246 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 121 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-08-08T22:33:02Z_

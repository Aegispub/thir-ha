# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-09 |
| **Generated At** | 2026-08-09T07:01:30Z |
| **Shift Time** | 07:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **192** |
| Confirmed Threats | **175** |
| False Positives Filtered | **17** (8.8%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **24** |
| High Severity Cases | **38** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **154** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **262** |
| Unique Credential Pairs | **238** |
| Unique Usernames | **11** |
| Unique Passwords | **236** |
| Successful Auth Pairs | **255** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 226 |
| `support` | 9 |
| `test` | 8 |
| `GET / HTTP/1.1` | 4 |
| `*1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 5 |
| `test2020` | 5 |
| `11111` | 5 |
| `support` | 4 |
| `Host: 129.80.119.236:23` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `test2020` | 5 |
| `support` | `11111` | 5 |
| `support` | `support` | 4 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 4 |
| `test` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-08-09T04:55:12 |
| `root` | `Admin]` | `10.0.0.73` | 2026-08-09T04:57:10 |
| `root` | `**` | `10.0.0.73` | 2026-08-09T04:57:51 |
| `root` | `123-Abc` | `10.0.0.73` | 2026-08-09T04:57:57 |
| `root` | `Password-` | `10.0.0.73` | 2026-08-09T04:58:26 |
| `root` | `Letmein!!!` | `10.0.0.73` | 2026-08-09T04:59:17 |
| `root` | `!QAZasd!QAZ` | `10.0.0.73` | 2026-08-09T04:59:45 |
| `root` | `AdminClient!` | `10.0.0.73` | 2026-08-09T05:00:16 |
| `root` | `Admin123456...` | `10.0.0.73` | 2026-08-09T05:00:48 |
| `root` | `123!@#wsx` | `10.0.0.73` | 2026-08-09T05:01:40 |
| `root` | `123start` | `10.0.0.73` | 2026-08-09T05:01:44 |
| `root` | `Owner12345@` | `10.0.0.73` | 2026-08-09T05:02:10 |
| `root` | `Pass@word!` | `10.0.0.73` | 2026-08-09T05:02:14 |
| `root` | `qwer!@#$` | `10.0.0.73` | 2026-08-09T05:02:25 |
| `root` | `P@ssw0rd234` | `10.0.0.73` | 2026-08-09T05:02:41 |
| `root` | `abc**` | `10.0.0.73` | 2026-08-09T05:03:45 |
| `root` | `Password)` | `10.0.0.73` | 2026-08-09T05:03:45 |
| `root` | `Admin$012` | `10.0.0.73` | 2026-08-09T05:04:07 |
| `root` | `Abc@123!@#` | `10.0.0.73` | 2026-08-09T05:05:56 |
| `root` | `A123!` | `10.0.0.73` | 2026-08-09T05:06:05 |
| `root` | `123root123` | `10.0.0.73` | 2026-08-09T05:06:28 |
| `root` | `qaz@asd` | `10.0.0.73` | 2026-08-09T05:06:55 |
| `root` | `ASD)123` | `10.0.0.73` | 2026-08-09T05:07:31 |
| `root` | `!@#$%.qwert` | `10.0.0.73` | 2026-08-09T05:07:59 |
| `root` | `Qweasd_2wsx` | `10.0.0.73` | 2026-08-09T05:08:04 |
| `test` | `admin` | `10.0.0.73` | 2026-08-09T05:08:14 |
| `root` | `P@$$word123!@#` | `10.0.0.73` | 2026-08-09T05:08:16 |
| `root` | `1234qweQWE.` | `10.0.0.73` | 2026-08-09T05:08:36 |
| `root` | `Admin_123123` | `10.0.0.73` | 2026-08-09T05:08:49 |
| `root` | `Adm!n!$tr@t0r@` | `10.0.0.73` | 2026-08-09T05:09:03 |
| `root` | `qqq@123` | `10.0.0.73` | 2026-08-09T05:09:16 |
| `root` | `zaq_12345` | `10.0.0.73` | 2026-08-09T05:10:19 |
| `root` | `1q2w3e4r!@#$%` | `10.0.0.73` | 2026-08-09T05:10:58 |
| `root` | `P@$$w0rd-123` | `10.0.0.73` | 2026-08-09T05:11:08 |
| `ubnt` | `88` | `10.0.0.73` | 2026-08-09T05:11:40 |
| `root` | `Qwer!123` | `10.0.0.73` | 2026-08-09T05:11:45 |
| `root` | `12345.a` | `10.0.0.73` | 2026-08-09T05:12:30 |
| `root` | `administrator!@#$%` | `10.0.0.73` | 2026-08-09T05:12:45 |
| `root` | `qazwsx!@#!@#` | `10.0.0.73` | 2026-08-09T05:12:57 |
| `root` | `mysql.user` | `10.0.0.73` | 2026-08-09T05:14:32 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.189.244.51` | 2026-08-09T05:14:39 |
| `root` | `Admin1234.qwe` | `10.0.0.73` | 2026-08-09T05:14:46 |
| `*1` | `$4` | `35.189.244.51` | 2026-08-09T05:14:49 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 549` | `35.189.244.51` | 2026-08-09T05:14:50 |
| `root` | `!@#$%@QWERT` | `10.0.0.73` | 2026-08-09T05:15:07 |
| `root` | `Qaz@1234` | `10.0.0.73` | 2026-08-09T05:15:24 |
| `root` | `Server54321` | `10.0.0.73` | 2026-08-09T05:16:13 |
| `root` | `!Administrator*` | `10.0.0.73` | 2026-08-09T05:16:28 |
| `root` | `Pa55w0rd123.` | `10.0.0.73` | 2026-08-09T05:16:37 |
| `root` | `Q12345678!` | `10.0.0.73` | 2026-08-09T05:16:44 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `184.105.247.196` | 2026-08-09T05:17:17 |
| `root` | `P@55w0rd@12345` | `10.0.0.73` | 2026-08-09T05:18:23 |
| `guest` | `11111111` | `62.220.104.155` | 2026-08-09T05:18:24 |
| `root` | `wsxzaq123!@` | `10.0.0.73` | 2026-08-09T05:19:15 |
| `root` | `Passw0rd2012` | `10.0.0.73` | 2026-08-09T05:19:46 |
| `root` | `P@$$w0rd@` | `10.0.0.73` | 2026-08-09T05:20:33 |
| `root` | `PASSw@rd` | `10.0.0.73` | 2026-08-09T05:21:19 |
| `root` | `@dm1n@123` | `10.0.0.73` | 2026-08-09T05:21:51 |
| `root` | `~!@#QWE` | `10.0.0.73` | 2026-08-09T05:22:57 |
| `root` | `!qwer1234@` | `10.0.0.73` | 2026-08-09T05:23:11 |
| `root` | `Q!1q2w3e` | `10.0.0.73` | 2026-08-09T05:23:22 |
| `root` | `xyz!` | `10.0.0.73` | 2026-08-09T05:23:52 |
| `root` | `123456789@a` | `10.0.0.73` | 2026-08-09T05:23:58 |
| `root` | `adminpassword12345` | `10.0.0.73` | 2026-08-09T05:24:09 |
| `root` | `Qaz.12345678` | `10.0.0.73` | 2026-08-09T05:24:15 |
| `root` | `Abc123!@@` | `10.0.0.73` | 2026-08-09T05:24:31 |
| `root` | `welcome_123` | `10.0.0.73` | 2026-08-09T05:24:44 |
| `root` | `!@#123$%^` | `10.0.0.73` | 2026-08-09T05:25:10 |
| `root` | `1qaz!@2wsx` | `10.0.0.73` | 2026-08-09T05:25:17 |
| `root` | `P@55w0rd@0` | `10.0.0.73` | 2026-08-09T05:26:21 |
| `root` | `123@1qaz` | `10.0.0.73` | 2026-08-09T05:26:35 |
| `root` | `Qwerty@12345` | `10.0.0.73` | 2026-08-09T05:26:50 |
| `test` | `admin` | `177.174.89.99` | 2026-08-09T05:27:01 |
| `root` | `P55w0rd!@#` | `10.0.0.73` | 2026-08-09T05:27:03 |
| `test` | `admin` | `195.133.156.116` | 2026-08-09T05:27:15 |
| `root` | `QWE!12345` | `10.0.0.73` | 2026-08-09T05:27:17 |
| `root` | `administrator-123` | `10.0.0.73` | 2026-08-09T05:28:20 |
| `root` | `ASDF$#@!` | `10.0.0.73` | 2026-08-09T05:29:36 |
| `root` | `@dm!n_123` | `10.0.0.73` | 2026-08-09T05:29:46 |
| `root` | `qwe12345678` | `10.0.0.73` | 2026-08-09T05:29:58 |
| `root` | `server_123456` | `10.0.0.73` | 2026-08-09T05:30:08 |
| `root` | `Qq123#` | `10.0.0.73` | 2026-08-09T05:31:07 |
| `root` | `As123!` | `10.0.0.73` | 2026-08-09T05:32:20 |
| `root` | `1234$abcd` | `10.0.0.73` | 2026-08-09T05:32:54 |
| `root` | `@QAZXSW@` | `10.0.0.73` | 2026-08-09T05:32:57 |
| `root` | `Qwezaq123!@` | `10.0.0.73` | 2026-08-09T05:33:57 |
| `root` | `O*!` | `10.0.0.73` | 2026-08-09T05:35:38 |
| `root` | `123.com!@#` | `10.0.0.73` | 2026-08-09T05:37:47 |
| `root` | `Abc-asd123` | `10.0.0.73` | 2026-08-09T05:38:00 |
| `root` | `Qaz!@#123` | `10.0.0.73` | 2026-08-09T05:38:14 |
| `root` | `Admin1234!@#` | `10.0.0.73` | 2026-08-09T05:38:46 |
| `root` | `pa@ssord` | `10.0.0.73` | 2026-08-09T05:38:48 |
| `root` | `321.123` | `10.0.0.73` | 2026-08-09T05:38:59 |
| `root` | `access!` | `10.0.0.73` | 2026-08-09T05:39:47 |
| `root` | `!Password*` | `10.0.0.73` | 2026-08-09T05:40:04 |
| `root` | `Passw0rd123!@#` | `10.0.0.73` | 2026-08-09T05:40:46 |
| `root` | `Qq1234567!@#` | `10.0.0.73` | 2026-08-09T05:41:04 |
| `root` | `R00tAdm!n123` | `10.0.0.73` | 2026-08-09T05:41:31 |
| `root` | `123QWEasdf` | `10.0.0.73` | 2026-08-09T05:42:00 |
| `test` | `test2020` | `10.0.0.73` | 2026-08-09T05:42:45 |
| `root` | `123@aaa` | `10.0.0.73` | 2026-08-09T05:42:45 |
| `root` | `1234qwe` | `10.0.0.73` | 2026-08-09T05:43:01 |
| `root` | `QAZXSW_123` | `10.0.0.73` | 2026-08-09T05:44:12 |
| `root` | `1qaz@WSX!` | `10.0.0.73` | 2026-08-09T05:44:37 |
| `root` | `R00tServer123` | `10.0.0.73` | 2026-08-09T05:45:19 |
| `root` | `$etuP123` | `10.0.0.73` | 2026-08-09T05:46:16 |
| `root` | `Demo,123` | `10.0.0.73` | 2026-08-09T05:46:27 |
| `root` | `testpass123` | `10.0.0.73` | 2026-08-09T05:46:43 |
| `root` | `Passw0rd...` | `10.0.0.73` | 2026-08-09T05:47:03 |
| `root` | `Admin.1234.` | `10.0.0.73` | 2026-08-09T05:48:35 |
| `root` | `p@sswd#@!` | `10.0.0.73` | 2026-08-09T05:49:16 |
| `root` | `Qaz.321.321` | `10.0.0.73` | 2026-08-09T05:50:50 |
| `root` | `Qw123!!**` | `10.0.0.73` | 2026-08-09T05:52:00 |
| `root` | `Admin@user!@#` | `10.0.0.73` | 2026-08-09T05:52:19 |
| `root` | `Owner.123456` | `10.0.0.73` | 2026-08-09T05:52:26 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.126.75` | 2026-08-09T05:52:52 |
| `root` | `QWEASD@12345` | `10.0.0.73` | 2026-08-09T05:53:03 |
| `admin` | `t1l2cm3r` | `153.37.177.219` | 2026-08-09T05:53:05 |
| `*1` | `$4` | `207.175.126.75` | 2026-08-09T05:53:06 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4900` | `207.175.126.75` | 2026-08-09T05:53:08 |
| `root` | `Qwert.123` | `10.0.0.73` | 2026-08-09T05:53:13 |
| `root` | `12345aA!!` | `10.0.0.73` | 2026-08-09T05:53:25 |
| `root` | `abcd@123456` | `10.0.0.73` | 2026-08-09T05:53:53 |
| `root` | `Pa55word!.` | `10.0.0.73` | 2026-08-09T05:54:29 |
| `root` | `Asdfqwer1234` | `10.0.0.73` | 2026-08-09T05:54:43 |
| `root` | `$erver@12345` | `10.0.0.73` | 2026-08-09T05:55:59 |
| `root` | `123456!QAZ` | `10.0.0.73` | 2026-08-09T05:56:59 |
| `root` | `Qwerty.12345` | `10.0.0.73` | 2026-08-09T05:57:05 |
| `root` | `P@ssw0rd@1234` | `10.0.0.73` | 2026-08-09T05:57:16 |
| `root` | `Q123q!@#` | `10.0.0.73` | 2026-08-09T05:58:48 |
| `root` | `Pass@w0rd.` | `10.0.0.73` | 2026-08-09T05:59:22 |
| `root` | `Abcde1234` | `10.0.0.73` | 2026-08-09T05:59:25 |
| `root` | `123pass!` | `10.0.0.73` | 2026-08-09T05:59:36 |
| `root` | `Admin1234567@` | `10.0.0.73` | 2026-08-09T06:00:29 |
| `root` | `@dm!nistrator` | `10.0.0.73` | 2026-08-09T06:00:35 |
| `root` | `QQaa123!**` | `10.0.0.73` | 2026-08-09T06:01:09 |
| `root` | `123-QWE` | `10.0.0.73` | 2026-08-09T06:01:41 |
| `test` | `test2020` | `61.145.181.7` | 2026-08-09T06:01:48 |
| `test` | `test2020` | `95.35.29.192` | 2026-08-09T06:02:00 |
| `test` | `test2020` | `117.253.130.123` | 2026-08-09T06:02:01 |
| `root` | `Pass1234567@` | `10.0.0.73` | 2026-08-09T06:02:32 |
| `root` | `Asdwsx123` | `10.0.0.73` | 2026-08-09T06:02:49 |
| `root` | `$erver!` | `10.0.0.73` | 2026-08-09T06:03:14 |
| `debian` | `debian` | `189.56.0.19` | 2026-08-09T06:03:40 |
| `debian` | `debian` | `218.26.205.154` | 2026-08-09T06:03:49 |
| `root` | `1234!@#` | `10.0.0.73` | 2026-08-09T06:04:05 |
| `support` | `support` | `176.53.159.196` | 2026-08-09T06:05:17 |
| `root` | `Pass@word321` | `10.0.0.73` | 2026-08-09T06:05:19 |
| `root` | `Letmein!qaz` | `10.0.0.73` | 2026-08-09T06:05:48 |
| `root` | `Acc0unt` | `10.0.0.73` | 2026-08-09T06:05:59 |
| `root` | `12345(qwert` | `10.0.0.73` | 2026-08-09T06:06:14 |
| `root` | `Pass@123456` | `10.0.0.73` | 2026-08-09T06:06:22 |
| `root` | `pa33w0rd@!` | `10.0.0.73` | 2026-08-09T06:06:46 |
| `root` | `1q!` | `10.0.0.73` | 2026-08-09T06:07:43 |
| `root` | `Pass1234567!@#` | `10.0.0.73` | 2026-08-09T06:07:46 |
| `root` | `Asdfgh.1234` | `10.0.0.73` | 2026-08-09T06:08:57 |
| `support` | `11111` | `10.0.0.73` | 2026-08-09T06:09:38 |
| `root` | `Asdf123qwer@` | `10.0.0.73` | 2026-08-09T06:09:47 |
| `root` | `Qaz1234` | `10.0.0.73` | 2026-08-09T06:09:55 |
| `root` | `qwe123asd!@#` | `10.0.0.73` | 2026-08-09T06:09:58 |
| `root` | `Asdfg123!@#` | `10.0.0.73` | 2026-08-09T06:10:12 |
| `root` | `Asd123.123` | `10.0.0.73` | 2026-08-09T06:10:41 |
| `support` | `11111` | `153.37.177.219` | 2026-08-09T06:11:15 |
| `support` | `11111` | `103.29.185.162` | 2026-08-09T06:11:28 |
| `root` | `!23Qwe` | `10.0.0.73` | 2026-08-09T06:11:50 |
| `root` | `0wner` | `10.0.0.73` | 2026-08-09T06:12:50 |
| `root` | `zaq!.@wsx` | `10.0.0.73` | 2026-08-09T06:13:30 |
| `root` | `Letmein@$` | `10.0.0.73` | 2026-08-09T06:13:33 |
| `root` | `Master!@#` | `10.0.0.73` | 2026-08-09T06:13:56 |
| `root` | `Admin#,9ol.` | `10.0.0.73` | 2026-08-09T06:14:06 |
| `root` | `Admi@n12.` | `10.0.0.73` | 2026-08-09T06:14:27 |
| `root` | `1q2w3e.123` | `10.0.0.73` | 2026-08-09T06:14:47 |
| `root` | `QQaa123*` | `10.0.0.73` | 2026-08-09T06:17:01 |
| `root` | `Qw12345678!` | `10.0.0.73` | 2026-08-09T06:17:12 |
| `root` | `Server-` | `10.0.0.73` | 2026-08-09T06:17:23 |
| `root` | `Q123456!` | `10.0.0.73` | 2026-08-09T06:17:27 |
| `root` | `Admin@321321` | `10.0.0.73` | 2026-08-09T06:17:48 |
| `root` | `@Passw0rd@123` | `10.0.0.73` | 2026-08-09T06:18:22 |
| `root` | `Computer123` | `10.0.0.73` | 2026-08-09T06:18:40 |
| `root` | `Pass_123$` | `10.0.0.73` | 2026-08-09T06:18:47 |
| `root` | `ab!@` | `10.0.0.73` | 2026-08-09T06:20:21 |
| `root` | `123123.com` | `10.0.0.73` | 2026-08-09T06:20:30 |
| `root` | `Asdf432!` | `10.0.0.73` | 2026-08-09T06:21:06 |
| `root` | `$upp0rt@123` | `10.0.0.73` | 2026-08-09T06:21:29 |
| `root` | `Admin_12345` | `10.0.0.73` | 2026-08-09T06:21:58 |
| `root` | `p@ssword0` | `10.0.0.73` | 2026-08-09T06:22:28 |
| `root` | `P@$$v0rd@` | `10.0.0.73` | 2026-08-09T06:22:33 |
| `root` | `-admin_admin` | `10.0.0.73` | 2026-08-09T06:23:14 |
| `root` | `admin.!@#` | `10.0.0.73` | 2026-08-09T06:23:38 |
| `root` | `p@5sword123` | `10.0.0.73` | 2026-08-09T06:23:43 |
| `admin` | `admin` | `34.156.218.171` | 2026-08-09T06:24:00 |
| `root` | `Letmein!^` | `10.0.0.73` | 2026-08-09T06:24:10 |
| `root` | `!administrator%` | `10.0.0.73` | 2026-08-09T06:24:13 |
| `root` | `12345qwe` | `10.0.0.73` | 2026-08-09T06:24:54 |
| `root` | `pass0rd123` | `10.0.0.73` | 2026-08-09T06:26:19 |
| `support` | `11111` | `195.222.57.183` | 2026-08-09T06:27:42 |
| `root` | `P@$$w0rd.123` | `10.0.0.73` | 2026-08-09T06:27:47 |
| `support` | `11111` | `64.53.7.231` | 2026-08-09T06:27:49 |
| `root` | `test321` | `10.0.0.73` | 2026-08-09T06:27:55 |
| `root` | `!@#qwe"` | `10.0.0.73` | 2026-08-09T06:28:37 |
| `root` | `Admini@1234` | `10.0.0.73` | 2026-08-09T06:28:56 |
| `root` | `@dm1n@!` | `10.0.0.73` | 2026-08-09T06:29:12 |
| `root` | `!Passw0rd123` | `10.0.0.73` | 2026-08-09T06:29:14 |
| `root` | `P@assw0rd#@!` | `10.0.0.73` | 2026-08-09T06:30:19 |
| `root` | `Adminabc123!` | `10.0.0.73` | 2026-08-09T06:31:05 |
| `root` | `wsx@qaz` | `10.0.0.73` | 2026-08-09T06:31:37 |
| `root` | `123a123@` | `10.0.0.73` | 2026-08-09T06:32:15 |
| `root` | `admin123wsx` | `10.0.0.73` | 2026-08-09T06:32:19 |
| `root` | `zxc1234567` | `10.0.0.73` | 2026-08-09T06:32:39 |
| `root` | `@dministrator!@#$%^` | `10.0.0.73` | 2026-08-09T06:32:55 |
| `root` | `1q1q2w2w` | `10.0.0.73` | 2026-08-09T06:33:14 |
| `root` | `admin012345` | `10.0.0.73` | 2026-08-09T06:34:37 |
| `root` | `!QAZ.XSW@` | `10.0.0.73` | 2026-08-09T06:35:22 |
| `root` | `scanner123` | `10.0.0.73` | 2026-08-09T06:35:53 |
| `root` | `123456!@#$%^` | `10.0.0.73` | 2026-08-09T06:36:01 |
| `install` | `install` | `65.20.211.96` | 2026-08-09T06:36:22 |
| `install` | `install` | `61.184.128.210` | 2026-08-09T06:36:35 |
| `root` | `Passw0rd` | `180.71.9.31` | 2026-08-09T06:38:28 |
| `root` | `Master@123456` | `10.0.0.73` | 2026-08-09T06:38:33 |
| `root` | `Passw0rd` | `116.72.9.151` | 2026-08-09T06:38:38 |
| `root` | `asdfghjk@` | `10.0.0.73` | 2026-08-09T06:39:41 |
| `root` | `cisco123@` | `10.0.0.73` | 2026-08-09T06:39:45 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-09T06:41:08 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-09T06:41:09 |
| `root` | `Ab12345!` | `10.0.0.73` | 2026-08-09T06:42:41 |
| `root` | `P@$$w0rd@12345` | `10.0.0.73` | 2026-08-09T06:42:44 |
| `root` | `admin` | `164.92.109.155` | 2026-08-09T06:43:07 |
| `root` | `P@$$w0rd@123456` | `10.0.0.73` | 2026-08-09T06:44:00 |
| `root` | `qwe0` | `10.0.0.73` | 2026-08-09T06:44:07 |
| `root` | `Passw0rd_.123` | `10.0.0.73` | 2026-08-09T06:44:33 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5593` | `35.189.244.51` | 2026-08-09T06:44:35 |
| `root` | `P@sswords1234` | `10.0.0.73` | 2026-08-09T06:44:41 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-09T06:45:32 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-09T06:45:32 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-09T06:45:32 |
| `admin` | `Password123!` | `182.75.227.178` | 2026-08-09T06:45:53 |
| `root` | `Q123456789!@#` | `10.0.0.73` | 2026-08-09T06:46:20 |
| `root` | `Admin@abc123` | `10.0.0.73` | 2026-08-09T06:46:50 |
| `root` | `!@#qwertrewq` | `10.0.0.73` | 2026-08-09T06:47:15 |
| `root` | `Administr@tor.@` | `10.0.0.73` | 2026-08-09T06:47:33 |
| `root` | `power0.123` | `10.0.0.73` | 2026-08-09T06:47:52 |
| `root` | `qazwsx123456` | `10.0.0.73` | 2026-08-09T06:47:59 |
| `root` | `PA$$w0rd.123` | `10.0.0.73` | 2026-08-09T06:48:06 |
| `root` | `admin12345asd` | `10.0.0.73` | 2026-08-09T06:48:45 |
| `root` | `$admin$` | `10.0.0.73` | 2026-08-09T06:49:00 |
| `root` | `zxcasd321` | `10.0.0.73` | 2026-08-09T06:49:30 |
| `root` | `Asd123_` | `10.0.0.73` | 2026-08-09T06:49:41 |
| `root` | `admin_pass` | `10.0.0.73` | 2026-08-09T06:50:14 |
| `root` | `A112233$` | `10.0.0.73` | 2026-08-09T06:50:26 |
| `root` | `Qwerty@0123` | `10.0.0.73` | 2026-08-09T06:51:08 |
| `root` | `ASDASD123123` | `10.0.0.73` | 2026-08-09T06:52:39 |
| `root` | `Qaz12345@` | `10.0.0.73` | 2026-08-09T06:53:01 |
| `root` | `Admin0.0.0` | `10.0.0.73` | 2026-08-09T06:53:14 |
| `root` | `Adm1n.!` | `10.0.0.73` | 2026-08-09T06:54:20 |
| `root` | `Asdf)1234` | `10.0.0.73` | 2026-08-09T06:54:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **192** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 19 |
| libssh | 7 |
| Paramiko (Python) | 6 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 18 | 17 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 18 | 17 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `b4b8ae3d7241...` | libssh | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **42** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (38)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a9c9faf8a49c

| Field | Detail |
|---|---|
| **Source IP** | `35.189.244[.]51` |
| **First Seen** | 2026-08-09 05:14 |
| **Last Seen** | 2026-08-09 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:14:39` | `cowrie.session.connect` |
| `2026-08-09 05:14:39` | `cowrie.login.success` |
| `2026-08-09 05:14:40` | `cowrie.session.params` |
| `2026-08-09 05:14:40` | `cowrie.command.input` |
| `2026-08-09 05:14:40` | `cowrie.command.input` |
| `2026-08-09 05:14:40` | `cowrie.command.failed` |
| `2026-08-09 05:14:40` | `cowrie.command.input` |
| `2026-08-09 05:14:40` | `cowrie.log.closed` |
| `2026-08-09 05:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.244[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.189.244[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1def410bb13f

| Field | Detail |
|---|---|
| **Source IP** | `35.189.244[.]51` |
| **First Seen** | 2026-08-09 05:14 |
| **Last Seen** | 2026-08-09 05:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:14:49` | `cowrie.session.connect` |
| `2026-08-09 05:14:49` | `cowrie.login.success` |
| `2026-08-09 05:14:49` | `cowrie.session.params` |
| `2026-08-09 05:14:49` | `cowrie.command.input` |
| `2026-08-09 05:14:49` | `cowrie.command.failed` |
| `2026-08-09 05:15:01` | `cowrie.log.closed` |
| `2026-08-09 05:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.244[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.189.244[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27b9dfef354

| Field | Detail |
|---|---|
| **Source IP** | `35.189.244[.]51` |
| **First Seen** | 2026-08-09 05:14 |
| **Last Seen** | 2026-08-09 05:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:14:50` | `cowrie.session.connect` |
| `2026-08-09 05:14:50` | `cowrie.login.success` |
| `2026-08-09 05:14:51` | `cowrie.session.params` |
| `2026-08-09 05:14:51` | `cowrie.command.input` |
| `2026-08-09 05:15:01` | `cowrie.log.closed` |
| `2026-08-09 05:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.244[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.189.244[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df67fdfdc58

| Field | Detail |
|---|---|
| **Source IP** | `184.105.247[.]196` |
| **First Seen** | 2026-08-09 05:17 |
| **Last Seen** | 2026-08-09 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:17:17` | `cowrie.session.connect` |
| `2026-08-09 05:17:17` | `cowrie.login.success` |
| `2026-08-09 05:17:18` | `cowrie.session.params` |
| `2026-08-09 05:17:18` | `cowrie.command.input` |
| `2026-08-09 05:17:18` | `cowrie.command.input` |
| `2026-08-09 05:17:18` | `cowrie.command.failed` |
| `2026-08-09 05:17:18` | `cowrie.command.input` |
| `2026-08-09 05:17:18` | `cowrie.command.failed` |
| `2026-08-09 05:17:18` | `cowrie.command.input` |
| `2026-08-09 05:17:18` | `cowrie.log.closed` |
| `2026-08-09 05:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.105.247[.]196` to AbuseIPDB if not already reported
- [ ] Block `184.105.247[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a811874be8

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-08-09 05:18 |
| **Last Seen** | 2026-08-09 05:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:18:21` | `cowrie.session.connect` |
| `2026-08-09 05:18:22` | `cowrie.client.version` |
| `2026-08-09 05:18:22` | `cowrie.client.kex` |
| `2026-08-09 05:18:24` | `cowrie.login.success` |
| `2026-08-09 05:18:25` | `cowrie.direct-tcpip.request` |
| `2026-08-09 05:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0590c032341b

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-09 05:26 |
| **Last Seen** | 2026-08-09 05:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:26:59` | `cowrie.session.connect` |
| `2026-08-09 05:26:59` | `cowrie.client.version` |
| `2026-08-09 05:26:59` | `cowrie.client.kex` |
| `2026-08-09 05:27:01` | `cowrie.login.success` |
| `2026-08-09 05:27:02` | `cowrie.direct-tcpip.request` |
| `2026-08-09 05:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48359924a2e

| Field | Detail |
|---|---|
| **Source IP** | `195.133.156[.]116` |
| **First Seen** | 2026-08-09 05:27 |
| **Last Seen** | 2026-08-09 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:27:13` | `cowrie.session.connect` |
| `2026-08-09 05:27:13` | `cowrie.client.version` |
| `2026-08-09 05:27:13` | `cowrie.client.kex` |
| `2026-08-09 05:27:15` | `cowrie.login.success` |
| `2026-08-09 05:27:15` | `cowrie.direct-tcpip.request` |
| `2026-08-09 05:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.133.156[.]116` to AbuseIPDB if not already reported
- [ ] Block `195.133.156[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace25a391edf

| Field | Detail |
|---|---|
| **Source IP** | `207.175.126[.]75` |
| **First Seen** | 2026-08-09 05:52 |
| **Last Seen** | 2026-08-09 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:52:52` | `cowrie.session.connect` |
| `2026-08-09 05:52:52` | `cowrie.login.success` |
| `2026-08-09 05:52:53` | `cowrie.session.params` |
| `2026-08-09 05:52:53` | `cowrie.command.input` |
| `2026-08-09 05:52:53` | `cowrie.command.input` |
| `2026-08-09 05:52:53` | `cowrie.command.failed` |
| `2026-08-09 05:52:53` | `cowrie.command.input` |
| `2026-08-09 05:52:53` | `cowrie.log.closed` |
| `2026-08-09 05:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.126[.]75` to AbuseIPDB if not already reported
- [ ] Block `207.175.126[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f0c560ef4c

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-09 05:53 |
| **Last Seen** | 2026-08-09 05:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:53:02` | `cowrie.session.connect` |
| `2026-08-09 05:53:03` | `cowrie.client.version` |
| `2026-08-09 05:53:03` | `cowrie.client.kex` |
| `2026-08-09 05:53:05` | `cowrie.login.success` |
| `2026-08-09 05:53:06` | `cowrie.direct-tcpip.request` |
| `2026-08-09 05:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c49dd74872

| Field | Detail |
|---|---|
| **Source IP** | `207.175.126[.]75` |
| **First Seen** | 2026-08-09 05:53 |
| **Last Seen** | 2026-08-09 05:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:53:06` | `cowrie.session.connect` |
| `2026-08-09 05:53:06` | `cowrie.login.success` |
| `2026-08-09 05:53:07` | `cowrie.session.params` |
| `2026-08-09 05:53:07` | `cowrie.command.input` |
| `2026-08-09 05:53:07` | `cowrie.command.failed` |
| `2026-08-09 05:53:14` | `cowrie.log.closed` |
| `2026-08-09 05:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.126[.]75` to AbuseIPDB if not already reported
- [ ] Block `207.175.126[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dfaa3f7c972

| Field | Detail |
|---|---|
| **Source IP** | `207.175.126[.]75` |
| **First Seen** | 2026-08-09 05:53 |
| **Last Seen** | 2026-08-09 05:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 05:53:08` | `cowrie.session.connect` |
| `2026-08-09 05:53:08` | `cowrie.login.success` |
| `2026-08-09 05:53:09` | `cowrie.session.params` |
| `2026-08-09 05:53:09` | `cowrie.command.input` |
| `2026-08-09 05:53:14` | `cowrie.log.closed` |
| `2026-08-09 05:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.126[.]75` to AbuseIPDB if not already reported
- [ ] Block `207.175.126[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ae02db5b92

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-08-09 06:01 |
| **Last Seen** | 2026-08-09 06:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:01:45` | `cowrie.session.connect` |
| `2026-08-09 06:01:46` | `cowrie.client.version` |
| `2026-08-09 06:01:46` | `cowrie.client.kex` |
| `2026-08-09 06:01:48` | `cowrie.login.success` |
| `2026-08-09 06:01:49` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8df372003b

| Field | Detail |
|---|---|
| **Source IP** | `117.253.130[.]123` |
| **First Seen** | 2026-08-09 06:01 |
| **Last Seen** | 2026-08-09 06:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:01:58` | `cowrie.session.connect` |
| `2026-08-09 06:01:59` | `cowrie.client.version` |
| `2026-08-09 06:01:59` | `cowrie.client.kex` |
| `2026-08-09 06:02:01` | `cowrie.login.success` |
| `2026-08-09 06:02:01` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.253.130[.]123` to AbuseIPDB if not already reported
- [ ] Block `117.253.130[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577b76a994ec

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-08-09 06:01 |
| **Last Seen** | 2026-08-09 06:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:01:58` | `cowrie.session.connect` |
| `2026-08-09 06:01:59` | `cowrie.client.version` |
| `2026-08-09 06:01:59` | `cowrie.client.kex` |
| `2026-08-09 06:02:00` | `cowrie.login.success` |
| `2026-08-09 06:02:00` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b2a77958302

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-09 06:03 |
| **Last Seen** | 2026-08-09 06:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:03:35` | `cowrie.session.connect` |
| `2026-08-09 06:03:37` | `cowrie.client.version` |
| `2026-08-09 06:03:37` | `cowrie.client.kex` |
| `2026-08-09 06:03:40` | `cowrie.login.success` |
| `2026-08-09 06:03:41` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e623014b0a99

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-08-09 06:03 |
| **Last Seen** | 2026-08-09 06:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:03:46` | `cowrie.session.connect` |
| `2026-08-09 06:03:47` | `cowrie.client.version` |
| `2026-08-09 06:03:47` | `cowrie.client.kex` |
| `2026-08-09 06:03:49` | `cowrie.login.success` |
| `2026-08-09 06:03:50` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ca11ff1885

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 06:05 |
| **Last Seen** | 2026-08-09 06:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:05:16` | `cowrie.session.connect` |
| `2026-08-09 06:05:16` | `cowrie.client.version` |
| `2026-08-09 06:05:16` | `cowrie.client.kex` |
| `2026-08-09 06:05:17` | `cowrie.login.success` |
| `2026-08-09 06:05:17` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:05:17` | `cowrie.direct-tcpip.data` |
| `2026-08-09 06:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e891e3138e46

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-09 06:11 |
| **Last Seen** | 2026-08-09 06:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:11:12` | `cowrie.session.connect` |
| `2026-08-09 06:11:13` | `cowrie.client.version` |
| `2026-08-09 06:11:13` | `cowrie.client.kex` |
| `2026-08-09 06:11:15` | `cowrie.login.success` |
| `2026-08-09 06:11:15` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd62c7341f63

| Field | Detail |
|---|---|
| **Source IP** | `103.29.185[.]162` |
| **First Seen** | 2026-08-09 06:11 |
| **Last Seen** | 2026-08-09 06:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:11:25` | `cowrie.session.connect` |
| `2026-08-09 06:11:26` | `cowrie.client.version` |
| `2026-08-09 06:11:26` | `cowrie.client.kex` |
| `2026-08-09 06:11:28` | `cowrie.login.success` |
| `2026-08-09 06:11:28` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.29.185[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.29.185[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1da4f30c4e

| Field | Detail |
|---|---|
| **Source IP** | `34.156.218[.]171` |
| **First Seen** | 2026-08-09 06:23 |
| **Last Seen** | 2026-08-09 06:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:23:57` | `cowrie.session.connect` |
| `2026-08-09 06:23:57` | `cowrie.client.version` |
| `2026-08-09 06:23:57` | `cowrie.client.kex` |
| `2026-08-09 06:24:00` | `cowrie.login.success` |
| `2026-08-09 06:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.218[.]171` to AbuseIPDB if not already reported
- [ ] Block `34.156.218[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a243e4294fed

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-09 06:27 |
| **Last Seen** | 2026-08-09 06:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:27:41` | `cowrie.session.connect` |
| `2026-08-09 06:27:42` | `cowrie.client.version` |
| `2026-08-09 06:27:42` | `cowrie.client.kex` |
| `2026-08-09 06:27:42` | `cowrie.login.success` |
| `2026-08-09 06:27:43` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449b1cdefc1d

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-08-09 06:27 |
| **Last Seen** | 2026-08-09 06:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:27:48` | `cowrie.session.connect` |
| `2026-08-09 06:27:48` | `cowrie.client.version` |
| `2026-08-09 06:27:48` | `cowrie.client.kex` |
| `2026-08-09 06:27:49` | `cowrie.login.success` |
| `2026-08-09 06:27:49` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5024d4d87069

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-08-09 06:36 |
| **Last Seen** | 2026-08-09 06:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:36:19` | `cowrie.session.connect` |
| `2026-08-09 06:36:20` | `cowrie.client.version` |
| `2026-08-09 06:36:20` | `cowrie.client.kex` |
| `2026-08-09 06:36:22` | `cowrie.login.success` |
| `2026-08-09 06:36:22` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac02ec86857

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-09 06:36 |
| **Last Seen** | 2026-08-09 06:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:36:32` | `cowrie.session.connect` |
| `2026-08-09 06:36:33` | `cowrie.client.version` |
| `2026-08-09 06:36:33` | `cowrie.client.kex` |
| `2026-08-09 06:36:35` | `cowrie.login.success` |
| `2026-08-09 06:36:36` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5bd48b3dac8

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-08-09 06:38 |
| **Last Seen** | 2026-08-09 06:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:38:25` | `cowrie.session.connect` |
| `2026-08-09 06:38:26` | `cowrie.client.version` |
| `2026-08-09 06:38:26` | `cowrie.client.kex` |
| `2026-08-09 06:38:28` | `cowrie.login.success` |
| `2026-08-09 06:38:29` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbefae665922

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-09 06:38 |
| **Last Seen** | 2026-08-09 06:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:38:34` | `cowrie.session.connect` |
| `2026-08-09 06:38:35` | `cowrie.client.version` |
| `2026-08-09 06:38:35` | `cowrie.client.kex` |
| `2026-08-09 06:38:38` | `cowrie.login.success` |
| `2026-08-09 06:38:39` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f1368ebd881

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 06:39 |
| **Last Seen** | 2026-08-09 06:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:39:21` | `cowrie.session.connect` |
| `2026-08-09 06:39:21` | `cowrie.client.version` |
| `2026-08-09 06:39:21` | `cowrie.client.kex` |
| `2026-08-09 06:39:22` | `cowrie.login.success` |
| `2026-08-09 06:39:22` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:39:22` | `cowrie.direct-tcpip.data` |
| `2026-08-09 06:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91b7b4dc422

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-09 06:41 |
| **Last Seen** | 2026-08-09 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:41:07` | `cowrie.session.connect` |
| `2026-08-09 06:41:07` | `cowrie.client.version` |
| `2026-08-09 06:41:07` | `cowrie.client.kex` |
| `2026-08-09 06:41:08` | `cowrie.login.success` |
| `2026-08-09 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edefc97bf705

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-09 06:41 |
| **Last Seen** | 2026-08-09 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:41:07` | `cowrie.session.connect` |
| `2026-08-09 06:41:07` | `cowrie.client.version` |
| `2026-08-09 06:41:08` | `cowrie.client.kex` |
| `2026-08-09 06:41:09` | `cowrie.login.success` |
| `2026-08-09 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2febad9fab4d

| Field | Detail |
|---|---|
| **Source IP** | `164.92.109[.]155` |
| **First Seen** | 2026-08-09 06:43 |
| **Last Seen** | 2026-08-09 06:43 |
| **Session Duration** | 25s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:43:06` | `cowrie.session.connect` |
| `2026-08-09 06:43:06` | `cowrie.client.version` |
| `2026-08-09 06:43:06` | `cowrie.client.kex` |
| `2026-08-09 06:43:06` | `cowrie.login.failed` |
| `2026-08-09 06:43:07` | `cowrie.login.success` |
| `2026-08-09 06:43:08` | `cowrie.session.params` |
| `2026-08-09 06:43:08` | `cowrie.command.input` |
| `2026-08-09 06:43:08` | `cowrie.command.failed` |
| `2026-08-09 06:43:08` | `cowrie.log.closed` |
| `2026-08-09 06:43:09` | `cowrie.session.params` |
| `2026-08-09 06:43:09` | `cowrie.command.input` |
| `2026-08-09 06:43:09` | `cowrie.log.closed` |
| `2026-08-09 06:43:10` | `cowrie.session.params` |
| `2026-08-09 06:43:10` | `cowrie.command.input` |
| `2026-08-09 06:43:10` | `cowrie.log.closed` |
| `2026-08-09 06:43:11` | `cowrie.session.params` |
| `2026-08-09 06:43:11` | `cowrie.command.input` |
| `2026-08-09 06:43:11` | `cowrie.log.closed` |
| `2026-08-09 06:43:11` | `cowrie.session.params` |
| `2026-08-09 06:43:11` | `cowrie.command.input` |
| `2026-08-09 06:43:11` | `cowrie.log.closed` |
| `2026-08-09 06:43:12` | `cowrie.session.params` |
| `2026-08-09 06:43:12` | `cowrie.command.input` |
| `2026-08-09 06:43:12` | `cowrie.log.closed` |
| `2026-08-09 06:43:13` | `cowrie.session.params` |
| `2026-08-09 06:43:13` | `cowrie.command.input` |
| `2026-08-09 06:43:13` | `cowrie.log.closed` |
| `2026-08-09 06:43:14` | `cowrie.session.params` |
| `2026-08-09 06:43:14` | `cowrie.command.input` |
| `2026-08-09 06:43:14` | `cowrie.log.closed` |
| `2026-08-09 06:43:15` | `cowrie.session.params` |
| `2026-08-09 06:43:15` | `cowrie.command.input` |
| `2026-08-09 06:43:15` | `cowrie.log.closed` |
| `2026-08-09 06:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.109[.]155` to AbuseIPDB if not already reported
- [ ] Block `164.92.109[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e5124363e6

| Field | Detail |
|---|---|
| **Source IP** | `35.189.244[.]51` |
| **First Seen** | 2026-08-09 06:44 |
| **Last Seen** | 2026-08-09 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:44:19` | `cowrie.session.connect` |
| `2026-08-09 06:44:19` | `cowrie.login.success` |
| `2026-08-09 06:44:19` | `cowrie.session.params` |
| `2026-08-09 06:44:19` | `cowrie.command.input` |
| `2026-08-09 06:44:19` | `cowrie.command.input` |
| `2026-08-09 06:44:19` | `cowrie.command.failed` |
| `2026-08-09 06:44:19` | `cowrie.command.input` |
| `2026-08-09 06:44:20` | `cowrie.log.closed` |
| `2026-08-09 06:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.244[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.189.244[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004419a74ac8

| Field | Detail |
|---|---|
| **Source IP** | `35.189.244[.]51` |
| **First Seen** | 2026-08-09 06:44 |
| **Last Seen** | 2026-08-09 06:44 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:44:32` | `cowrie.session.connect` |
| `2026-08-09 06:44:32` | `cowrie.login.success` |
| `2026-08-09 06:44:33` | `cowrie.session.params` |
| `2026-08-09 06:44:33` | `cowrie.command.input` |
| `2026-08-09 06:44:33` | `cowrie.command.failed` |
| `2026-08-09 06:44:48` | `cowrie.log.closed` |
| `2026-08-09 06:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.244[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.189.244[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bbfcdbf112

| Field | Detail |
|---|---|
| **Source IP** | `35.189.244[.]51` |
| **First Seen** | 2026-08-09 06:44 |
| **Last Seen** | 2026-08-09 06:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:44:35` | `cowrie.session.connect` |
| `2026-08-09 06:44:35` | `cowrie.login.success` |
| `2026-08-09 06:44:35` | `cowrie.session.params` |
| `2026-08-09 06:44:35` | `cowrie.command.input` |
| `2026-08-09 06:44:48` | `cowrie.log.closed` |
| `2026-08-09 06:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.189.244[.]51` to AbuseIPDB if not already reported
- [ ] Block `35.189.244[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ecaae8a4ed4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 06:45 |
| **Last Seen** | 2026-08-09 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:45:32` | `cowrie.session.connect` |
| `2026-08-09 06:45:32` | `cowrie.client.version` |
| `2026-08-09 06:45:32` | `cowrie.client.kex` |
| `2026-08-09 06:45:32` | `cowrie.login.success` |
| `2026-08-09 06:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de0a47b449f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 06:45 |
| **Last Seen** | 2026-08-09 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:45:32` | `cowrie.session.connect` |
| `2026-08-09 06:45:32` | `cowrie.client.version` |
| `2026-08-09 06:45:32` | `cowrie.client.kex` |
| `2026-08-09 06:45:32` | `cowrie.login.success` |
| `2026-08-09 06:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32b9d72d2b8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 06:45 |
| **Last Seen** | 2026-08-09 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:45:32` | `cowrie.session.connect` |
| `2026-08-09 06:45:32` | `cowrie.client.version` |
| `2026-08-09 06:45:32` | `cowrie.client.kex` |
| `2026-08-09 06:45:32` | `cowrie.login.success` |
| `2026-08-09 06:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a401e0adb0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 06:45 |
| **Last Seen** | 2026-08-09 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:45:32` | `cowrie.session.connect` |
| `2026-08-09 06:45:32` | `cowrie.client.version` |
| `2026-08-09 06:45:32` | `cowrie.client.kex` |
| `2026-08-09 06:45:33` | `cowrie.login.success` |
| `2026-08-09 06:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580e1480c6c2

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-08-09 06:45 |
| **Last Seen** | 2026-08-09 06:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 06:45:50` | `cowrie.session.connect` |
| `2026-08-09 06:45:51` | `cowrie.client.version` |
| `2026-08-09 06:45:51` | `cowrie.client.kex` |
| `2026-08-09 06:45:53` | `cowrie.login.success` |
| `2026-08-09 06:45:54` | `cowrie.direct-tcpip.request` |
| `2026-08-09 06:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `35.189.244[.]51` | **60** | 2026-08-09 05:14 | 2026-08-09 06:44 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.126[.]75` | **30** | 2026-08-09 05:52 | 2026-08-09 05:53 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-09 05:01 | 2026-08-09 06:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-09 05:17 | 2026-08-09 06:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-09 05:30 | 2026-08-09 05:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-09 06:28 | 2026-08-09 06:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-09 06:50 | 2026-08-09 06:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.89.125[.]26` | **2** | 2026-08-09 05:41 | 2026-08-09 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | **2** | 2026-08-09 05:35 | 2026-08-09 06:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]100` | **2** | 2026-08-09 05:30 | 2026-08-09 05:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]46` | **2** | 2026-08-09 06:41 | 2026-08-09 06:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `207.175.135[.]190` | **2** | 2026-08-09 06:24 | 2026-08-09 06:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]47` | **2** | 2026-08-09 06:49 | 2026-08-09 06:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-08-09 05:09 | 2026-08-09 05:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]147` | 1 | 2026-08-09 05:34 | 2026-08-09 05:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-09 04:59 | 2026-08-09 04:59 | 36s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-08-09 06:51 | 2026-08-09 06:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-08-09 06:29 | 2026-08-09 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.224.223[.]212` | 1 | 2026-08-09 05:08 | 2026-08-09 05:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.30.203[.]249` | 1 | 2026-08-09 06:34 | 2026-08-09 06:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-08-09 06:50 | 2026-08-09 06:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.206.136[.]24` | 1 | 2026-08-09 05:04 | 2026-08-09 05:04 | 2s | 0 | `T1592` | 🟢 LOW |
| `220.189.253[.]198` | 1 | 2026-08-09 06:37 | 2026-08-09 06:38 | 38s | 0 | `T1592` | 🟢 LOW |
| `34.156.218[.]171` | 1 | 2026-08-09 06:23 | 2026-08-09 06:24 | 5s | 0 | `T1592` | 🟢 LOW |
| `39.67.150[.]186` | 1 | 2026-08-09 06:22 | 2026-08-09 06:22 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.12.24[.]87` | 1 | 2026-08-09 06:46 | 2026-08-09 06:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-08-09 06:39 | 2026-08-09 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-08-09 06:39 | 2026-08-09 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]94` | 1 | 2026-08-09 05:54 | 2026-08-09 05:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]190` | 1 | 2026-08-09 05:30 | 2026-08-09 05:30 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
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
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **23/75** 🔴 |
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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.156.218[.]171` | BE | Google LLC | **100** ⚠️ | 0 |
| `181.224.223[.]212` | AR | ALDERETE RIVAS JORDAN TOMAS SEBASTIAN (COMUNICATE INTERNET) | **100** ⚠️ | 6 |
| `194.165.16[.]121` | LT | Flyservers S.A. | **100** ⚠️ | 13 |
| `195.222.57[.]183` | BA | Public Enterprise BH Telecom DD | **100** ⚠️ | 50 |
| `64.53.7[.]231` | US | Home Telephone Company, Inc. | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `194.165.16[.]123` | LT | Flyservers S.A. | **100** ⚠️ | 11 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `45.33.14[.]5` | US | Linode | **100** ⚠️ | 50 |
| `61.145.181[.]7` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 38 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 192 cases |
| Tool 34  | Credential Extractor        | ✅ 262 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (8.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 42 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 38 priority case(s) shown individually · 30 recon entry/entries in table (13 group(s) consolidating 120 session(s)).

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
_Report time: 2026-08-09T07:01:30Z_

